"""A stand-in model server for tests and dry runs: the tool server's generator and an OpenAI-compatible chat server
on one local port, deterministic, no GPU.

It runs behind the real clients, so recording, composition and the loops are exercised as they will be on a rental.
Its landscape is scripted around a marker: a prompt that carries MARKER makes an image the judges accept; a writer
puts MARKER in its prompt when its request shows it (in a lesson or in a judge's guidance); the judges ask for it;
the distiller turns it into a lesson. So the first loops need two iterations, and loops given the lesson need one.
"""

from __future__ import annotations

import base64
import io
import json
import re
import threading
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

import numpy as np
from PIL import Image
from virtual_unstaging.domain import sha256_bytes, sha256_text

from clutter_pairs.space import size_for_aspect

MARKER = "[[good]]"
MARKER_RGB = (250, 250, 250)  # the first item's colour in an edit whose prompt carries the marker
_DATA_URL = re.compile(r"data:image/(?:png|jpeg);base64,([A-Za-z0-9+/=]+)")
_ITEM_LINE = re.compile(r"^(\d+)\. ", re.MULTILINE)
SIZE_MULTIPLE = 32


@dataclass
class FakeBehaviour:
    """Switches for tests: answer 503 after a number of model requests; shift the first edit of each clean image;
    assign no item to any region (every change is unexplained); report an invented door; a judge that answers prose instead of JSON."""

    down_after: int | None = None
    misalign_first_edit: bool = False
    locate_items: bool = True
    invent_door: bool = False  # the pair judge reports a door that appeared
    broken_judge: bool = False
    model_requests: int = 0
    edited_originals: set[str] = field(default_factory=set)


class FakeModelServer:
    """`with FakeModelServer() as server:` serves on 127.0.0.1; `server.tools_url`, `server.chat_url`."""

    def __init__(self, behaviour: FakeBehaviour | None = None) -> None:
        self.behaviour = behaviour or FakeBehaviour()
        self.blobs: dict[str, bytes] = {}
        self.lock = threading.Lock()
        handler = _handler(self)
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)

    @property
    def tools_url(self) -> str:
        return f"http://127.0.0.1:{self.httpd.server_address[1]}"

    @property
    def chat_url(self) -> str:
        return f"{self.tools_url}/v1"

    def __enter__(self) -> FakeModelServer:
        self.thread.start()
        return self

    def __exit__(self, *exc: object) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()

    # --- The tool server ---------------------------------------------------------------------------------------

    def capabilities(self) -> dict[str, Any]:
        return {"api_version": "1.2", "server_version": "fake", "tools": [], "generator": {
            "model": "fake/flux", "revision": "1", "max_images": 4, "roles": ["original"], "native_mask": False,
            "text_only": True, "settings": {"output_side": 1024}, "licence": "none (test double)", "recipe": "fake",
            "unverified": [], "state": "loaded"}}

    def generate(self, payload: dict[str, Any]) -> dict[str, Any]:
        prompt, seed = str(payload["prompt"]), int(payload["seed"])
        settings = payload.get("settings", {})
        side = int(settings.get("output_side", 1024))
        rng = np.random.default_rng([seed, int(sha256_text(prompt)[:8], 16)])
        images = payload.get("images", [])
        if not images:
            width, height = size_for_aspect(float(settings.get("output_aspect", 1.0)), side, SIZE_MULTIPLE)
            base = rng.uniform(0.3, 0.8, size=3)
            pixels = np.clip(base + rng.normal(0, 0.02, size=(height, width, 3)), 0, 1)
            out = (pixels * 255).astype(np.uint8)
            if MARKER in prompt:
                out[:8, :8] = 255
        else:
            original_sha = images[0]["sha256"]
            out = np.asarray(Image.open(io.BytesIO(self.blobs[original_sha])).convert("RGB")).copy()
            height, width = out.shape[:2]
            for n in range(1, len(_ITEM_LINE.findall(prompt)) + 1):
                w, h = width // 7, height // 5
                x = int(rng.integers(8, width - w - 8))
                y = int(rng.integers(height // 3, height - h - 8))
                colour = MARKER_RGB if n == 1 and MARKER in prompt else tuple(int(c) for c in rng.integers(0, 200, 3))
                out[y:y + h, x:x + w] = colour
            if self.behaviour.misalign_first_edit and original_sha not in self.behaviour.edited_originals:
                out = np.roll(out, 6, axis=1)
            self.behaviour.edited_originals.add(original_sha)
        data = _png(out)
        sha = sha256_bytes(data)
        self.blobs[sha] = data
        return {"output_sha256": sha, "media_type": "image/png", "width": out.shape[1], "height": out.shape[0],
                "gpu_seconds": 0.5, "load_seconds": 0.0}

    # --- The chat server ---------------------------------------------------------------------------------------

    def chat(self, payload: dict[str, Any]) -> str:
        schema = payload["response_format"]["json_schema"]["schema"]
        texts, images = [], []
        for message in payload["messages"]:
            if message["role"] == "system":
                continue
            for item in message["content"]:
                if item["type"] == "text":
                    texts.append(item["text"])
                else:
                    images.append(_decode(item["image_url"]["url"]))
        text = "\n".join(texts)
        kind = schema.get("title")
        if kind == "text":
            return json.dumps({"text": self._write(text, int(payload.get("seed", 0)))})
        if self.behaviour.broken_judge and kind in ("clean_judgment", "pair_judgment"):
            return "The image looks fine to me."
        if kind == "clean_judgment":
            return json.dumps(self._judge_clean(images[0]))
        if kind == "pair_judgment":
            return json.dumps(self._judge_pair(text, images))
        if kind == "lessons":
            return json.dumps(self._distill(text))
        raise ValueError(f"unknown schema {kind}")

    def _write(self, text: str, seed: int) -> str:
        items = [line for line in text.splitlines() if _ITEM_LINE.match(line)]
        prompt = [f"A plain photograph, variation {seed % 1000}."] + items
        if MARKER in text:
            prompt.append(MARKER)
        return "\n".join(prompt)

    def _judge_clean(self, image: np.ndarray) -> dict[str, Any]:
        if bool((image[:8, :8] == 255).all()):
            return {"findings": [], "guidance": []}
        return {"findings": [{"code": "not_empty", "severity": "blocking", "box": [100, 500, 300, 900],
                              "comment": "a chair stands by the wall"}],
                "guidance": [f"Write {MARKER} in the prompt."]}

    def _judge_pair(self, text: str, images: list[np.ndarray]) -> dict[str, Any]:
        _, cluttered, _ = images
        count = len(_ITEM_LINE.findall(text))
        items = list(range(1, count + 1)) if self.behaviour.locate_items else []
        regions = [{"region": n, "items": items, "other_change": False} for n in range(1, 13)]  # extra numbers dropped
        openings = [{"kind": "window", "where": "back wall", "status": "unchanged", "regions": []}]
        appeared = [{"kind": "door", "where": "left wall", "regions": [1]}] if self.behaviour.invent_door else []
        head = {"openings": openings, "appeared": appeared, "regions": regions}
        marked = np.all(np.abs(cluttered.astype(int) - np.array(MARKER_RGB)) <= 2, axis=-1).sum() > 100
        if marked:
            return {**head, "findings": [], "guidance": []}
        return {**head,
                "findings": [{"code": "clutter_off_spec", "severity": "blocking", "regions": [], "box": None,
                              "comment": "the items are not the ones listed"}],
                "guidance": [f"Write {MARKER} in the instruction."]}

    def _distill(self, text: str) -> dict[str, Any]:
        in_use = re.findall(r"\(lesson (\d+)\) ([^\n]*)", text)
        if any(MARKER in lesson for _, lesson in in_use) or "- finding" not in text:
            return {"lessons": []}
        return {"lessons": [{"text": f"Always write {MARKER} in the prompt.", "scope": [], "evidence": [1],
                             "replaces": None}]}

    def count_model_request(self) -> bool:
        """Count a model request; False when the server plays down."""
        with self.lock:
            self.behaviour.model_requests += 1
            down = self.behaviour.down_after
            return down is None or self.behaviour.model_requests <= down


def _png(pixels: np.ndarray) -> bytes:
    buffer = io.BytesIO()
    Image.fromarray(pixels).save(buffer, format="PNG")
    return buffer.getvalue()


def _decode(url: str) -> np.ndarray:
    match = _DATA_URL.match(url)
    if match is None:
        raise ValueError("not a base64 data URL")
    return np.asarray(Image.open(io.BytesIO(base64.b64decode(match.group(1)))).convert("RGB"))


def _handler(server: FakeModelServer) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format: str, *args: object) -> None:  # quiet
            return

        def _send(self, status: int, body: bytes, kind: str) -> None:
            self.send_response(status)
            self.send_header("Content-Type", kind)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)

        def _json(self, status: int, value: object) -> None:
            self._send(status, json.dumps(value).encode(), "application/json")

        def _body(self) -> bytes:
            return self.rfile.read(int(self.headers.get("Content-Length", "0")))

        def do_HEAD(self) -> None:  # noqa: N802
            sha = self.path.rsplit("/", 1)[-1]
            self._send(200 if sha in server.blobs else 404, b"", "application/json")

        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/capabilities":
                self._json(200, server.capabilities())
            elif self.path == "/health":
                self._json(200, {"status": "ok"})
            elif self.path.startswith("/blobs/"):
                data = server.blobs.get(self.path.rsplit("/", 1)[-1])
                if data is None:
                    self._json(404, {"error": {"code": "blob_missing", "message": self.path}})
                else:
                    self._send(200, data, "image/png")
            else:
                self._json(404, {"error": {"code": "not_found", "message": self.path}})

        def do_PUT(self) -> None:  # noqa: N802
            data = self._body()
            server.blobs[sha256_bytes(data)] = data
            self._json(201, {"sha256": sha256_bytes(data)})

        def do_POST(self) -> None:  # noqa: N802
            payload = json.loads(self._body())
            if not server.count_model_request():
                self._json(503, {"error": {"code": "unavailable", "message": "the fake server plays down"}})
                return
            if self.path == "/generate":
                self._json(200, server.generate(payload))
            elif self.path == "/v1/chat/completions":
                content = server.chat(payload)
                event = json.dumps({"choices": [{"delta": {"content": content}}]})
                self._send(200, f"data: {event}\n\ndata: [DONE]\n\n".encode(), "text/event-stream")
            else:
                self._json(404, {"error": {"code": "not_found", "message": self.path}})

    return Handler
