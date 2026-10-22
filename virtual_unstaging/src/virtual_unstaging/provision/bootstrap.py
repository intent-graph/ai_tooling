"""On-machine bootstrap, stdlib only: arms the self-delete guard, serves the judge, receives and starts the tool server.

Shipped to the rented machine as text (never imported there by name): the provider's guard source is appended and
`main(<guard class>)` is called last (see `machine.py`). Nothing here runs at import time.

What it does, in order:
1. Arms the guard: asks the provider's `SelfDelete` whether the machine can delete itself, reports it in `/unstage/status`.
2. Serves one authenticated port: `/unstage/status`, `/unstage/wheel` (PUT, once, hash-checked) and `/v1/*`, a
   key-checking pass-through to the judge server that listens on loopback only (so no other route of the judge
   server is reachable from outside).
3. Starts the judge server at once; when the wheel arrives, installs it and starts the tool server.
4. At the absolute deadline plus a short grace, or when a service dies and stays dead, or when it cannot start
   safely, deletes the machine. It fails closed: any error ends the machine rather than leaving it idle. If every
   way of deleting fails, it exits, which stops the container.

The session key arrives in an environment variable (the recorded exception in the design: the platform offers no
other way); it is checked here and never printed.
"""

from __future__ import annotations

import hashlib
import hmac
import http.client
import http.server
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping
from typing import Any

TAG = "[unstage-boot]"
UNARMED_WAIT_SECONDS = 600.0
RELEASE_ROUNDS = 3
RELEASE_PAUSE_SECONDS = 20.0
INSTALL_TIMEOUT_SECONDS = 1800
READY_POLL_SECONDS = 5.0
TAIL_CHARS = 1500  # of a dead service's output, reported in its status
TAIL_READ_BYTES = 256 * 1024
ERROR_LINE = re.compile(r"\w(Error|Exception)\b|\bERROR\b|error:|out of memory|CUDA error|Killed")
ANSI = re.compile(r"\x1b\[[0-9;]*m")
MODEL_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,95}/[A-Za-z0-9][A-Za-z0-9._-]{0,95}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
STOP_WAIT_SECONDS = 60.0
MAX_BODY_BYTES = 256 * 1024 * 1024
PROXY_PATH = re.compile(r"^/v1/[A-Za-z0-9_./-]*$")
WHEEL_NAME = re.compile(r"^[A-Za-z0-9_.]+-[A-Za-z0-9_.!+]+-py3-none-any\.whl$")
HOP_BY_HOP = {"connection", "keep-alive", "proxy-authenticate", "proxy-authorization", "te", "trailers",
              "transfer-encoding", "upgrade", "host", "content-length"}


def log(message: str) -> None:
    print(f"{TAG} {time.strftime('%H:%M:%S')} {message}", flush=True)


class SelfDelete:
    """How this machine deletes itself on one rental service; the provider's source subclasses it."""

    def __init__(self, env: Mapping[str, str]) -> None:
        self.env = env

    def probe(self) -> str | None:
        """A short label of the way the machine can delete itself, or None when it cannot."""
        raise NotImplementedError

    def terminate(self) -> bool:
        raise NotImplementedError

    def stop(self) -> bool:
        """Release the compute at least (the disk may keep billing)."""
        raise NotImplementedError


def key_acceptable(key: str) -> bool:
    """A real key: long enough, printable, no spaces, and not a placeholder the platform failed to substitute."""
    return len(key) >= 24 and key.isprintable() and not any(c.isspace() for c in key) and "{{" not in key


def release_machine(guard: SelfDelete, sleep: Callable[[float], None]) -> bool:
    """Delete the machine; if that is refused, stop it. Rounds, with a pause. True on the first success."""
    for attempt in range(RELEASE_ROUNDS):
        for label, action in (("terminate", guard.terminate), ("stop", guard.stop)):
            try:
                done = action()
            except Exception as error:  # a guard bug must not end the loop
                log(f"{label} raised {type(error).__name__}")
                done = False
            log(f"{label} -> {'ok' if done else 'refused'}")
            if done:
                return True
        if attempt + 1 < RELEASE_ROUNDS:
            sleep(RELEASE_PAUSE_SECONDS)
    return False


def install_commands(venv: str, wheel: str, python: str, has_uv: bool) -> list[list[str]]:
    """Argv lists (no shell) that create an environment sharing the image's packages and install the wheel into it."""
    target = f"{wheel}[serve]"
    if has_uv:
        return [
            ["uv", "venv", "--system-site-packages", "--python", python, venv],
            ["uv", "pip", "install", "--python", f"{venv}/bin/python", target],
        ]
    return [
        [python, "-m", "venv", "--system-site-packages", venv],
        [f"{venv}/bin/python", "-m", "pip", "install", "--quiet", target],
    ]


def http_ok(url: str, key: str) -> bool:
    """True when a GET on a loopback URL answers 200 with the key."""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    request = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}"})
    try:
        with opener.open(request, timeout=5) as reply:
            return bool(reply.status == 200)
    except (OSError, http.client.HTTPException):
        return False


class Status:
    """What `/unstage/status` reports; updated from several threads."""

    def __init__(self, deadline: float | None) -> None:
        self._lock = threading.Lock()
        self._data: dict[str, dict[str, Any]] = {
            "guard": {"armed": None, "api": None},
            "judge": {"state": "off"},
            "tools": {"state": "waiting_wheel", "detail": ""},
            "wheel": {"state": "waiting"},
        }
        self.deadline = deadline

    def update(self, section: str, **fields: Any) -> None:
        with self._lock:
            self._data[section].update(fields)

    def get(self, section: str, name: str) -> Any:
        with self._lock:
            return self._data[section].get(name)

    def snapshot(self, now: float) -> dict[str, Any]:
        with self._lock:
            sections: dict[str, Any] = {name: dict(values) for name, values in self._data.items()}
        sections["deadline"] = self.deadline
        sections["seconds_left"] = None if self.deadline is None else int(self.deadline - now)
        return sections


class Supervisor:
    def __init__(
        self,
        plan: Mapping[str, Any],
        env: Mapping[str, str],
        guard: SelfDelete,
        *,
        now: Callable[[], float] = time.time,
        sleep: Callable[[float], None] = time.sleep,
        popen: Callable[..., Any] = subprocess.Popen,
        run: Callable[..., Any] = subprocess.run,
        ready: Callable[[str, str], bool] = http_ok,
        exit_process: Callable[[int], Any] = os._exit,
        serve_front: bool = True,
        forever: bool = True,
    ) -> None:
        self.plan = plan
        self.env = env
        self.guard = guard
        self.now = now
        self.sleep = sleep
        self.popen = popen
        self.run_step = run
        self.ready = ready
        self.exit_process = exit_process
        self.serve_front = serve_front
        self.forever = forever
        deadline = plan.get("deadline")
        self.status = Status(float(deadline) if isinstance(deadline, (int, float)) else None)
        self.children: dict[str, Any] = {}
        self.outputs: dict[str, str] = {}  # service name -> file holding its output, when the plan names a log_dir
        self._judge_lock = threading.Lock()
        self.key = env.get(str(plan.get("key_env", "")), "")
        self.server: http.server.ThreadingHTTPServer | None = None
        self.stop_at = 0.0

    # -- the whole life of the machine ----------------------------------------------------------------

    def run(self) -> str:
        """Returns why the machine was released (tests); on a real machine this never returns."""
        reason = "deadline"
        try:
            reason = self._life()
        except Exception as error:  # fail closed: any error ends the machine
            reason = f"supervisor error ({type(error).__name__})"
        log(f"releasing the machine: {reason}")
        self._stop_children()
        if not release_machine(self.guard, self.sleep):
            log("every way of deleting the machine was refused: exiting, which stops the container")
            self.exit_process(0)
        while self.forever:  # the container may outlive the delete request for a moment
            self.sleep(3600.0)
        return reason

    def _life(self) -> str:
        if not isinstance(self.status.deadline, float):
            return "no deadline in the plan"
        if not key_acceptable(self.key):
            return "no usable session key"
        self.stop_at = self.status.deadline + float(self.plan.get("grace_seconds", 30))
        api = self.guard.probe()
        self.status.update("guard", armed=api is not None, api=api)
        log(f"guard armed={api is not None} api={api} deadline={int(self.status.deadline)}")
        if self.now() >= self.stop_at:
            return "deadline already passed at start"
        if self.serve_front:
            self._start_front()
        if api is None:
            return self._wait_unarmed()
        self._start_judge()
        return self._watch()

    def _wait_unarmed(self) -> str:
        """Nothing expensive starts without a guard; `up` reads the status and deletes the machine."""
        until = self.now() + UNARMED_WAIT_SECONDS
        while self.now() < min(until, self.stop_at):
            self.sleep(1.0)
        return "guard not armed"

    def _watch(self) -> str:
        early: float | None = None
        while True:
            now = self.now()
            if now >= self.stop_at:
                return "deadline"
            if early is not None and now >= early:
                return "a service exited and stayed down"
            for name, process in list(self.children.items()):
                if name not in self.children or self.children[name] is not process:  # replaced (a judge switch)
                    continue
                if early is None and process.poll() is not None:
                    tail = self._tail(name)
                    log(f"{name} exited with {process.returncode}" + (f"; its last output:\n{tail}" if tail else ""))
                    self.status.update(name, state="failed",
                                       detail=f"exited with {process.returncode}" + (f"; last output: {tail}" if tail else ""))
                    early = now + float(self.plan.get("child_exit_grace_seconds", 600))
            self.sleep(min(READY_POLL_SECONDS, max(0.5, self.stop_at - now)))

    def _stop_children(self) -> None:
        for process in list(self.children.values()):
            try:
                process.terminate()
            except Exception:  # already gone
                continue
        if self.server is not None:
            threading.Thread(target=self.server.shutdown, daemon=True).start()

    # -- services -------------------------------------------------------------------------------------

    def _child_env(self, gpu: str | None, extra: Mapping[str, str] | None = None) -> dict[str, str]:
        env = dict(self.env)
        if gpu:
            env["CUDA_VISIBLE_DEVICES"] = gpu
        env.update(extra or {})
        return env

    def _start_judge(self, argv: list[str] | None = None) -> None:
        argv = argv or [str(a) for a in self.plan.get("judge_argv") or []]
        if not argv:
            return
        self.status.update("judge", state="starting", model=argv[2] if len(argv) > 2 else "", detail="")
        env = self._child_env(self.plan.get("judge_gpu"), {"VLLM_API_KEY": self.key})
        self._spawn("judge", argv, env)
        url = f"http://127.0.0.1:{int(self.plan['judge_port'])}/v1/models"
        threading.Thread(target=self._poll_ready, args=("judge", url), daemon=True).start()

    def _spawn(self, name: str, argv: list[str], env: dict[str, str]) -> None:
        """Start a service; with a log_dir in the plan its output goes to a file, so a crash can be reported."""
        log_dir = self.plan.get("log_dir")
        if not log_dir:
            self.children[name] = self.popen(argv, env=env)
            return
        os.makedirs(str(log_dir), exist_ok=True)
        path = os.path.join(str(log_dir), f"{name}.log")
        with open(path, "ab") as output:  # the child keeps its own copy of the descriptor
            self.children[name] = self.popen(argv, env=env, stdout=output, stderr=subprocess.STDOUT)
        self.outputs[name] = path

    def _tail(self, name: str) -> str:
        """What a dead service said: its last error lines (the root cause sits above the final traceback), then its
        last lines; the session key masked. Empty when its output was not captured."""
        path = self.outputs.get(name)
        if not path:
            return ""
        try:
            with open(path, "rb") as output:
                output.seek(max(0, os.path.getsize(path) - TAIL_READ_BYTES))
                text = output.read().decode("utf-8", "replace")
        except OSError as error:
            return f"(output unreadable: {type(error).__name__})"
        if self.key:
            text = text.replace(self.key, "<session key>")
        lines = [ANSI.sub("", line).strip() for line in text.splitlines()]
        lines = [line for line in lines if line]
        errors: list[str] = []
        for line in reversed(lines):  # the last occurrence of each error line, newest kept
            if ERROR_LINE.search(line) and line[:220] not in errors:
                errors.insert(0, line[:220])
        report = "errors: " + " | ".join(errors[-6:]) + " || last: " if errors else "last: "
        return (report + " | ".join(line[:200] for line in lines[-3:]))[:TAIL_CHARS]

    def switch_judge(self, model: str, revision: str | None, utilization: float | None = None) -> None:
        """Serve another judge model with the same options, or another memory share: the running one is stopped first
        (its GPU memory freed)."""
        template = [str(a) for a in self.plan.get("judge_argv") or []]
        if not template:
            raise ValueError("this machine serves no judge")
        with self._judge_lock:
            old = self.children.pop("judge", None)
            if old is not None:
                self._stop(old)
            log(f"switching the judge to {model}")
            self._start_judge(judge_argv_for(template, model, revision, utilization))

    def _stop(self, process: Any) -> None:
        try:
            process.terminate()
            waited = 0.0
            while process.poll() is None and waited < STOP_WAIT_SECONDS:
                self.sleep(1.0)
                waited += 1.0
            if process.poll() is None:
                process.kill()
        except Exception as error:  # already gone
            log(f"stopping a service raised {type(error).__name__}")

    def _poll_ready(self, section: str, url: str) -> None:
        while self.now() < self.stop_at and self.status.get(section, "state") not in ("ready", "failed"):
            if self.ready(url, self.key):
                self.status.update(section, state="ready")
                log(f"{section} is ready")
                return
            self.sleep(READY_POLL_SECONDS)

    def accept_wheel(self, data_path: str) -> None:
        threading.Thread(target=self._install_and_serve, args=(data_path,), daemon=True).start()

    def _install_and_serve(self, wheel: str) -> None:
        try:
            self.status.update("tools", state="installing")
            install_dir = str(self.plan["install_dir"])
            venv = f"{install_dir}/venv"
            for argv in install_commands(venv, wheel, sys.executable, shutil.which("uv") is not None):
                done = self.run_step(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                     timeout=INSTALL_TIMEOUT_SECONDS)
                if done.returncode != 0:
                    tail = "\n".join(str(done.stdout or "").splitlines()[-15:])
                    self.status.update("tools", state="failed", detail=f"{argv[0]} failed: {tail}"[:2000])
                    return
            # The judge first: vLLM measures free GPU memory at start and fails if another process takes
            # some meanwhile, which the tool server's warm-up would do on a shared GPU.
            self.status.update("tools", state="waiting_judge")
            while self.status.get("judge", "state") == "starting" and self.now() < self.stop_at:
                self.sleep(READY_POLL_SECONDS)
            self.status.update("tools", state="starting")
            argv = [f"{venv}/bin/unstage", *[str(a) for a in self.plan["tools_argv"]]]
            self._spawn("tools", argv, self._child_env(self.plan.get("tools_gpu")))
            url = f"http://127.0.0.1:{int(self.plan['tools_port'])}/health"
            self._poll_ready("tools", url)
        except Exception as error:
            self.status.update("tools", state="failed", detail=f"{type(error).__name__}")

    def _start_front(self) -> None:
        handler = make_handler(self)
        self.server = http.server.ThreadingHTTPServer(("0.0.0.0", int(self.plan["front_port"])), handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()


def judge_argv_for(template: list[str], model: str, revision: str | None, utilization: float | None = None) -> list[str]:
    """The planned judge command with another model: the served name follows it, the revision is set or dropped, and
    the memory share is replaced when one is given."""
    argv = list(template)
    if utilization is not None:
        if "--gpu-memory-utilization" in argv:
            at = argv.index("--gpu-memory-utilization")
            del argv[at:at + 2]
        argv += ["--gpu-memory-utilization", f"{utilization:.2f}"]
    argv[2] = model
    if "--served-model-name" in argv:
        argv[argv.index("--served-model-name") + 1] = model
    if "--revision" in argv:
        at = argv.index("--revision")
        del argv[at:at + 2]
    if revision:
        argv += ["--revision", revision]
    return argv


def make_handler(supervisor: Supervisor) -> type[http.server.BaseHTTPRequestHandler]:
    plan = supervisor.plan
    wheel_plan = plan.get("wheel") or {}
    wheel_lock = threading.Lock()

    class Handler(http.server.BaseHTTPRequestHandler):
        server_version = "unstage-boot"

        def log_message(self, format: str, *args: Any) -> None:
            return

        def _reply(self, status: int, payload: Mapping[str, Any]) -> None:
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _error(self, status: int, code: str, message: str) -> None:
            self._reply(status, {"error": {"code": code, "message": message}})

        def _authorized(self) -> bool:
            header = self.headers.get("Authorization", "")
            token = header[7:] if header.startswith("Bearer ") else ""
            return hmac.compare_digest(token.encode(), supervisor.key.encode())

        def _route(self, method: str) -> None:
            if not self._authorized():
                self._error(401, "unauthorized", "a valid bearer key is required")
                return
            path = urllib.parse.urlsplit(self.path).path
            if path == "/unstage/status" and method == "GET":
                self._reply(200, supervisor.status.snapshot(supervisor.now()))
            elif path == "/unstage/wheel" and method == "PUT":
                self._wheel()
            elif path == "/unstage/judge" and method == "POST":
                self._judge()
            elif PROXY_PATH.fullmatch(path) and ".." not in path and method in ("GET", "POST"):
                self._proxy(method)
            else:
                self._error(404, "not_found", "no such route")

        def do_GET(self) -> None:
            self._route("GET")

        def do_POST(self) -> None:
            self._route("POST")

        def do_PUT(self) -> None:
            self._route("PUT")

        def _body_length(self, limit: int) -> int | None:
            if self.headers.get("Transfer-Encoding"):
                self._error(411, "length_required", "send a Content-Length")
                return None
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                length = -1
            if not 0 <= length <= limit:
                self._error(413, "too_large", "body size is not accepted")
                return None
            return length

        def _judge(self) -> None:
            length = self._body_length(4096)
            if length is None:
                return
            try:
                body = json.loads(self.rfile.read(length) or b"{}")
            except ValueError:
                body = None
            model = body.get("model") if isinstance(body, dict) else None
            revision = body.get("revision") if isinstance(body, dict) else None
            if not isinstance(model, str) or not MODEL_ID.fullmatch(model):
                self._error(400, "bad_request", "model must be an org/name repository id")
                return
            if revision is not None and (not isinstance(revision, str) or not COMMIT.fullmatch(revision)):
                self._error(400, "bad_request", "revision must be a 40-character commit or null")
                return
            utilization = body.get("gpu_memory_utilization") if isinstance(body, dict) else None
            if utilization is not None and (isinstance(utilization, bool) or not isinstance(utilization, int | float)
                                            or not 0.1 <= utilization <= 0.95):
                self._error(400, "bad_request", "gpu_memory_utilization must be a number from 0.1 to 0.95")
                return
            if not plan.get("judge_argv"):
                self._error(404, "not_found", "this machine serves no judge")
                return
            supervisor.status.update("judge", state="stopping", model=model, detail="")  # never the old one's "ready"
            share = None if utilization is None else float(utilization)
            threading.Thread(target=supervisor.switch_judge, args=(model, revision, share), daemon=True).start()
            self._reply(202, {"judge": {"state": "starting", "model": model}})

        def _wheel(self) -> None:
            name, expected = str(wheel_plan.get("filename", "")), str(wheel_plan.get("sha256", ""))
            limit = int(wheel_plan.get("max_bytes", 0))
            if not WHEEL_NAME.fullmatch(name) or not re.fullmatch(r"[0-9a-f]{64}", expected):
                self._error(500, "bad_plan", "no valid wheel in the plan")
                return
            length = self._body_length(limit)
            if length is None:
                return
            with wheel_lock:
                if supervisor.status.get("wheel", "state") != "waiting":
                    self._error(409, "already_received", "the wheel was already received")
                    return
                digest, chunks, remaining = hashlib.sha256(), [], length
                while remaining:
                    chunk = self.rfile.read(min(65536, remaining))
                    if not chunk:
                        break
                    digest.update(chunk)
                    chunks.append(chunk)
                    remaining -= len(chunk)
                if remaining or digest.hexdigest() != expected:
                    self._error(400, "hash_mismatch", "the bytes do not hash to the wheel of this session")
                    return
                folder = f"{plan['install_dir']}/wheels"
                os.makedirs(folder, exist_ok=True)
                target = f"{folder}/{name}"
                with open(f"{target}.part", "wb") as handle:
                    handle.write(b"".join(chunks))
                os.replace(f"{target}.part", target)
                supervisor.status.update("wheel", state="received")
            supervisor.accept_wheel(target)
            self._reply(201, {"wheel": "received"})

        def _proxy(self, method: str) -> None:
            if not plan.get("judge_argv"):
                self._error(404, "judge_disabled", "this machine serves no judge")
                return
            length = self._body_length(MAX_BODY_BYTES)
            if length is None:
                return
            body = self.rfile.read(length) if length else None
            headers = {k: v for k, v in self.headers.items() if k.lower() not in HOP_BY_HOP}
            parts = urllib.parse.urlsplit(self.path)
            target = parts.path + (f"?{parts.query}" if parts.query else "")
            connection = http.client.HTTPConnection("127.0.0.1", int(plan["judge_port"]), timeout=1800)
            try:
                connection.request(method, target, body, headers)
                upstream = connection.getresponse()
            except (OSError, http.client.HTTPException):
                self._error(503, "judge_unavailable", "the judge server is not answering")
                return
            self.send_response(upstream.status)
            for name, value in upstream.getheaders():
                if name.lower() not in HOP_BY_HOP:
                    self.send_header(name, value)
            length_header = upstream.getheader("Content-Length")
            if length_header is not None:
                self.send_header("Content-Length", length_header)
            self.send_header("Connection", "close")  # HTTP/1.0: the end of a streamed body is the end of the connection
            self.end_headers()
            try:
                while True:
                    chunk = upstream.read1(65536)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    self.wfile.flush()
            except (OSError, http.client.HTTPException):
                pass
            finally:
                connection.close()

    return Handler


def main(guard_class: type[SelfDelete]) -> None:
    """Entry point on the machine: never returns."""
    try:
        plan = json.loads(os.environ.get("UNSTAGE_PLAN", "{}"))
        if not isinstance(plan, dict):
            plan = {}
    except ValueError:
        plan = {}
    env = dict(os.environ)
    supervisor = Supervisor(plan, env, guard_class(env))

    def on_term(signum: int, frame: Any) -> None:  # the container is being stopped: let it stop
        supervisor._stop_children()
        os._exit(0)

    signal.signal(signal.SIGTERM, on_term)
    supervisor.run()
