"""The tool server: FastAPI app (blobs, capabilities, generate, tools, health), the deadline watch, and `run_server`."""

from __future__ import annotations

import logging
import os
import threading
import time
from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from datetime import datetime
from importlib import metadata
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from PIL import Image
from pydantic import BaseModel, ConfigDict, Field
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import RequestResponseEndpoint

from virtual_unstaging.domain import ROLES, JsonScalar, sha256_bytes
from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.auth import bearer_matches, load_key
from virtual_unstaging.serve.blobdir import BlobDir, is_sha256
from virtual_unstaging.serve.deadline import Deadline, parse_deadline, utc_now
from virtual_unstaging.serve.errors import ApiError, ServeConfigError
from virtual_unstaging.serve.generation import (
    GenerationJob,
    Generator,
    ImageInput,
    build_generator,
    check_request,
)
from virtual_unstaging.serve.jobs import Execute, JobBoard, wants_async
from virtual_unstaging.serve.recipe import available_recipes, load_recipe
from virtual_unstaging.serve.timing import Stopwatch, measure
from virtual_unstaging.serve.tools import build_tools
from virtual_unstaging.serve.tools.base import MASK, ServerTool

LOG = logging.getLogger("virtual_unstaging.serve")
API_VERSION = "1.2"
MAX_BLOB_BYTES = 64 * 1024 * 1024
SHA_PATTERN = r"^[0-9a-f]{64}$"
GRACE_SECONDS = 120.0


# --- request bodies: parsed once, at the edge ----------------------------------------------------------------


class ImageRef(BaseModel):
    model_config = ConfigDict(extra="forbid")
    role: str = Field(pattern=r"^[a-z_]{1,32}$")
    sha256: str = Field(pattern=SHA_PATTERN)


class GenerateBody(BaseModel):
    model_config = ConfigDict(extra="forbid")
    prompt: str = Field(min_length=1, max_length=10_000)
    seed: int = Field(ge=0, lt=2**63)
    settings: dict[str, JsonScalar] = Field(default_factory=dict, max_length=32)
    images: list[ImageRef] = Field(default_factory=list, max_length=32)  # none: from text alone, if the recipe allows it


class GeneratorBody(BaseModel):
    model_config = ConfigDict(extra="forbid")
    recipe: str = Field(min_length=1, max_length=64)


class ToolBody(BaseModel):
    model_config = ConfigDict(extra="forbid")
    inputs: list[str] = Field(min_length=1, max_length=8)
    params: dict[str, Any] = Field(default_factory=dict, max_length=32)


# --- shared state ----------------------------------------------------------------------------------------------


class ServerState:
    """What the handlers share: key, deadline, blobs, the generator and tools, the one GPU lock, calls in flight."""

    def __init__(
        self,
        key: str,
        deadline: Deadline,
        blobs: BlobDir,
        generator: Generator | None,
        tools: Mapping[str, ServerTool],
        server_version: str,
    ) -> None:
        self.key = key
        self.deadline = deadline
        self.blobs = blobs
        self.generator = generator
        self.tools = dict(tools)
        self.server_version = server_version
        self.lock = threading.Lock()
        self._count_lock = threading.Lock()
        self._in_flight = 0
        self.jobs = JobBoard()

    def enter(self) -> None:
        with self._count_lock:
            self._in_flight += 1

    def leave(self) -> None:
        with self._count_lock:
            self._in_flight -= 1

    @property
    def in_flight(self) -> int:
        """Requests being served plus asynchronous jobs queued or running."""
        with self._count_lock:
            return self._in_flight + self.jobs.active()

    @contextmanager
    def gpu(self) -> Iterator[None]:
        """One piece of GPU work at a time; work that waited past the deadline is refused, not started."""
        with self.lock:
            if self.deadline.expired():
                raise ApiError("deadline_reached", "the server's deadline has passed")
            yield


def _error_response(error: ApiError) -> JSONResponse:
    headers = {"WWW-Authenticate": "Bearer"} if error.code == "unauthorized" else None
    return JSONResponse(status_code=error.status, content=error.body(), headers=headers)


def _decode(data: bytes, role: str, mask: bool) -> Image.Image:
    try:
        return imaging.decode(data, "L" if mask else "RGB")
    except ValueError as error:
        raise ApiError("bad_request", f"the image for {role} cannot be used: {error}") from None


def create_app(
    key: str,
    deadline: Deadline,
    data_dir: Path,
    generator: Generator | None = None,
    tools: Mapping[str, ServerTool] | None = None,
    server_version: str | None = None,
) -> FastAPI:
    """The app, ready to serve: no model is loaded here, no torch imported, no thread started."""
    try:
        version = server_version or metadata.version("virtual-unstaging")
    except metadata.PackageNotFoundError:
        version = "unknown"
    state = ServerState(key, deadline, BlobDir(Path(data_dir) / "blobs"), generator, tools or {}, version)
    app = FastAPI(title="virtual_unstaging tool server", version=API_VERSION)
    app.state.server = state

    @app.middleware("http")
    async def guard(request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.url.path == "/health":
            return await call_next(request)
        if not bearer_matches(request.headers.get("authorization"), state.key):
            return _error_response(ApiError("unauthorized", "a valid bearer key is required"))
        polling = request.method == "GET" and request.url.path.startswith("/jobs/")
        if state.deadline.expired() and not polling:  # a job already submitted stays pollable until the process exits
            return _error_response(ApiError("deadline_reached", "the server's deadline has passed"))
        state.enter()
        try:
            return await call_next(request)
        finally:
            state.leave()

    @app.exception_handler(ApiError)
    async def api_error(_: Request, error: ApiError) -> JSONResponse:
        return _error_response(error)

    @app.exception_handler(RequestValidationError)
    async def invalid_request(_: Request, error: RequestValidationError) -> JSONResponse:
        problems = "; ".join(f"{'.'.join(str(part) for part in item['loc'])}: {item['msg']}" for item in error.errors()[:5])
        return _error_response(ApiError("bad_request", problems))

    @app.exception_handler(StarletteHTTPException)
    async def http_error(_: Request, error: StarletteHTTPException) -> JSONResponse:
        if error.status_code == 404:
            return _error_response(ApiError("not_found", "no such endpoint"))
        return _error_response(ApiError("bad_request", f"HTTP {error.status_code}: {error.detail}"))

    # --- health and capabilities --------------------------------------------------------------------------------

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "deadline_reached" if state.deadline.expired() else "ok",
            "api_version": API_VERSION,
            "deadline": state.deadline.iso(),
            "seconds_left": state.deadline.seconds_left(),
            "busy": state.lock.locked(),
            "jobs": state.jobs.active(),
            "models": {
                "generator": state.generator.state() if state.generator else None,
                "tools": {name: tool.state() for name, tool in state.tools.items()},
            },
        }

    @app.get("/capabilities")
    def capabilities() -> dict[str, Any]:
        return {
            "api_version": API_VERSION,
            "server_version": state.server_version,
            "generator": state.generator.profile() if state.generator else None,
            "tools": [{**tool.describe(), "state": tool.state()} for tool in state.tools.values()],
        }

    # --- blobs ------------------------------------------------------------------------------------------------------

    @app.head("/blobs/{sha256}")
    def head_blob(sha256: str) -> Response:
        if not state.blobs.has(sha256):
            return Response(status_code=404)
        return Response(status_code=200, media_type=imaging.sniff_media_type(state.blobs.get(sha256)) or "application/octet-stream")

    @app.get("/blobs/{sha256}")
    def get_blob(sha256: str) -> Response:
        data = state.blobs.get(sha256)
        return Response(content=data, media_type=imaging.sniff_media_type(data) or "application/octet-stream")

    @app.put("/blobs/{sha256}", status_code=201)
    async def put_blob(sha256: str, request: Request) -> dict[str, Any]:
        if not is_sha256(sha256):
            raise ApiError("bad_request", "a blob address is 64 lowercase hexadecimal characters")
        media_type = request.headers.get("content-type", "").split(";")[0].strip().lower()
        if media_type not in imaging.MEDIA_TYPES:
            raise ApiError("bad_request", f"Content-Type must be one of {', '.join(imaging.MEDIA_TYPES)}")
        declared = request.headers.get("content-length", "")
        if declared.isdigit() and int(declared) > MAX_BLOB_BYTES:
            raise ApiError("bad_request", f"a blob is at most {MAX_BLOB_BYTES} bytes")
        chunks: list[bytes] = []
        size = 0
        async for chunk in request.stream():
            size += len(chunk)
            if size > MAX_BLOB_BYTES:
                raise ApiError("bad_request", f"a blob is at most {MAX_BLOB_BYTES} bytes")
            chunks.append(chunk)
        data = b"".join(chunks)
        if sha256_bytes(data) != sha256:
            raise ApiError("hash_mismatch", f"the bytes do not hash to {sha256}")
        if imaging.sniff_media_type(data) != media_type:
            raise ApiError("bad_request", f"the bytes are not {media_type}")
        try:
            imaging.check_header(data)
        except ValueError as error:
            raise ApiError("bad_request", str(error)) from None
        state.blobs.put(sha256, data)
        return {"sha256": sha256, "bytes": len(data)}

    # --- generation ---------------------------------------------------------------------------------------------------

    @app.put("/generator")
    def switch_generator(body: GeneratorBody) -> dict[str, Any]:
        """Replace the generator by another packaged recipe: the old one is released, the new one loads in the
        background (`/health` shows it). One rental can then clock or compare several generators."""
        if body.recipe not in available_recipes():
            raise ApiError("bad_request", f"unknown recipe {body.recipe!r} (packaged: {', '.join(available_recipes())})")
        recipe = load_recipe(body.recipe)
        with state.gpu():
            if state.generator is not None:
                state.generator.unload()
            state.generator = build_generator(recipe)
        threading.Thread(target=warm_generator, args=(state,), name="warm-generator", daemon=True).start()
        return {"recipe": recipe.name, "state": state.generator.state()}

    @app.post("/generate")
    def generate(body: GenerateBody, request: Request) -> Response:
        return _answer(state, request, _prepare_generate(state, body), "generator_failed")

    # --- tools --------------------------------------------------------------------------------------------------------

    @app.post("/tools/{name}")
    def run_tool(name: str, body: ToolBody, request: Request) -> Response:
        return _answer(state, request, _prepare_tool(state, name, body), "tool_failed")

    @app.get("/jobs/{job_id}")
    def get_job(job_id: str) -> dict[str, Any]:
        return state.jobs.get(job_id)

    return app


def _answer(state: ServerState, request: Request, execute: Execute, fallback_code: str) -> Response:
    """Run the prepared call now (the synchronous answer), or as a job when the client prefers `respond-async`."""
    if wants_async(request.headers.get("prefer")):
        job_id = state.jobs.submit(execute, fallback_code)
        headers = {"Preference-Applied": "respond-async", "Location": f"/jobs/{job_id}"}
        return JSONResponse(status_code=202, content={"job": job_id, "status": "queued"}, headers=headers)
    return JSONResponse(content=execute(lambda: None))


def _prepare_generate(state: ServerState, body: GenerateBody) -> Execute:
    """Validate and decode a generate request now (errors answer at once); the returned call does the GPU work."""
    generator = state.generator
    if generator is None:
        raise ApiError("generator_unavailable", "this server runs without a generator")
    roles = [item.role for item in body.images]
    unknown = [role for role in roles if role not in ROLES]
    if unknown:
        raise ApiError("bad_request", f"unknown image role {unknown[0]!r} (roles: {', '.join(ROLES)})")
    settings = check_request(generator.recipe, roles, body.settings)
    _require_blobs(state, [item.sha256 for item in body.images])
    pictures = tuple(
        ImageInput(item.role, _decode(state.blobs.get(item.sha256), item.role, item.role.endswith("_mask")))
        for item in body.images
    )
    job = GenerationJob(body.prompt, body.seed, settings, pictures)

    def execute(started: Callable[[], None]) -> dict[str, Any]:
        with state.gpu():
            if state.generator is not generator:
                raise ApiError("generator_changed", "the generator was replaced after this request was accepted")
            started()
            result = generator.generate(job)
        sha = state.blobs.add(result.png)
        return {
            "output_sha256": sha,
            "media_type": "image/png",
            "width": result.width,
            "height": result.height,
            "gpu_seconds": round(result.gpu_seconds, 3),
            "load_seconds": round(result.load_seconds, 3),
            "peak_gpu_gb": result.peak_gpu_gb,
        }

    return execute


def _prepare_tool(state: ServerState, name: str, body: ToolBody) -> Execute:
    """Validate and decode a tool request now (errors answer at once); the returned call does the GPU work."""
    tool = state.tools.get(name)
    if tool is None:
        raise ApiError("tool_unknown", f"this server has no tool {name!r} (tools: {', '.join(state.tools) or 'none'})")
    params = tool.parse_params(body.params)
    if len(body.inputs) != len(tool.input_kinds):
        raise ApiError("bad_request", f"{name} takes {len(tool.input_kinds)} input image(s), {len(body.inputs)} given")
    if not all(is_sha256(sha) for sha in body.inputs):
        raise ApiError("bad_request", "inputs are blob addresses: 64 lowercase hexadecimal characters")
    _require_blobs(state, body.inputs)
    pictures = [
        _decode(state.blobs.get(sha), f"input {index}", kind == MASK)
        for index, (sha, kind) in enumerate(zip(body.inputs, tool.input_kinds, strict=True))
    ]

    def execute(started: Callable[[], None]) -> dict[str, Any]:
        watch = Stopwatch()
        with state.gpu():
            started()
            try:
                with measure(watch):
                    output = tool.run(pictures, params)
            except ApiError:
                raise
            except Exception as error:
                LOG.exception("tool %s failed", name)
                raise ApiError("tool_failed", f"{name}: {type(error).__name__}: {str(error)[:300]}") from error
        outputs = {label: state.blobs.add(imaging.encode_png(picture)) for label, picture in output.images.items()}
        return {
            "tool": name,
            "version": tool.version,
            "outputs": outputs,
            "measures": output.measures,
            "summary": output.summary,
            "gpu_seconds": round(watch.seconds, 3),
        }

    return execute


def _require_blobs(state: ServerState, shas: Sequence[str]) -> None:
    missing = state.blobs.missing(shas)
    if missing:
        raise ApiError("blob_missing", "missing blobs: " + ", ".join(missing))


# --- process: start-up checks, warm-up, deadline watch ---------------------------------------------------------


def warm_models(state: ServerState) -> None:
    """Load the tools' models, then the generator's, under the GPU lock; a failure is logged and retried on first use."""
    parts: list[tuple[str, Any]] = [(name, tool) for name, tool in state.tools.items()]
    if state.generator is not None:
        parts.append(("generator", state.generator))
    for name, part in parts:
        try:
            with state.gpu():
                part.warm()
            LOG.info("%s is ready", name)
        except ApiError as error:
            LOG.error("warm-up of %s failed: %s", name, error.message)


def warm_generator(state: ServerState) -> None:
    """Load the current generator under the GPU lock; a failure shows in `/health` and is retried on first use."""
    generator = state.generator
    if generator is None:
        return
    try:
        with state.gpu():
            if state.generator is generator:
                generator.warm()
        LOG.info("generator %s is ready", generator.recipe.name)
    except ApiError as error:
        LOG.error("loading generator %s failed: %s", generator.recipe.name, error.message)


def watch_deadline(
    state: ServerState,
    stop: threading.Event,
    on_expired: Any,
    grace_seconds: float = GRACE_SECONDS,
    poll_seconds: float = 1.0,
) -> None:
    """At the deadline: wait for the calls in flight (at most `grace_seconds`), then call `on_expired`."""
    while not state.deadline.expired():
        if stop.wait(min(poll_seconds, max(0.05, state.deadline.seconds_left()))):
            return
    LOG.warning("the deadline has passed: refusing new work, finishing %d call(s) in flight", state.in_flight)
    waited = 0.0
    while (state.in_flight > 0 or state.lock.locked()) and waited < grace_seconds:
        if stop.wait(poll_seconds):
            return
        waited += poll_seconds
    on_expired()


def run_server(
    host: str,
    port: int,
    deadline: str | None,
    key_file: Path | None,
    key_env: str | None,
    recipe: str | None,
    tools: Sequence[str],
    data_dir: Path,
    *,
    warm: bool = True,
    grace_seconds: float = GRACE_SECONDS,
    clock: Any = utc_now,
) -> None:
    """Check the configuration, then serve until the deadline: refuse to start without a deadline or a key."""
    if not deadline:
        raise ServeConfigError("the server needs --deadline: a duration such as 90m or 2h, or an ISO 8601 UTC time")
    moment: datetime = parse_deadline(deadline, clock())
    key = load_key(key_file, key_env)
    generator = build_generator(load_recipe(recipe)) if recipe else None
    toolset = build_tools(list(tools))
    app = create_app(key, Deadline(moment, clock), Path(data_dir), generator, toolset)
    state: ServerState = app.state.server

    import uvicorn

    server = uvicorn.Server(
        uvicorn.Config(app, host=host, port=port, log_level="info", timeout_graceful_shutdown=int(grace_seconds))
    )
    stop = threading.Event()

    def expire() -> None:
        server.should_exit = True

    threading.Thread(target=watch_deadline, args=(state, stop, expire, grace_seconds), name="deadline", daemon=True).start()
    if warm:
        threading.Thread(target=warm_models, args=(state,), name="warm-up", daemon=True).start()
    LOG.info("serving on %s:%d until %s", host, port, state.deadline.iso())
    try:
        server.run()
    finally:
        stop.set()
    if state.lock.locked():  # a GPU call that cannot be cancelled outlived the grace: end the process anyway
        LOG.error("exiting with a GPU call still running")
        time.sleep(0.1)
        os._exit(0)
