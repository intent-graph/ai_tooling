"""Switch the generator or the judge of a live session, so that one rental clocks or compares several models."""

from __future__ import annotations

import json
import tomllib
from collections.abc import Callable
from typing import Any

from virtual_unstaging.provision import userfiles
from virtual_unstaging.provision.errors import ProvisionError
from virtual_unstaging.provision.lifecycle import Context

Probe = Callable[[], tuple[str | None, str]]  # (state, detail of a failure)


def switch_generator(ctx: Context, recipe: str) -> dict[str, Any]:
    """Load another packaged recipe on the machine's tool server; returns the new generator's profile."""
    tools, key = _session(ctx, "tools")
    status, reply = _call(ctx, "PUT", f"{tools}/generator", key, {"recipe": recipe})
    if status != 200:
        raise ProvisionError("switch_failed", f"the tool server refused {recipe!r}: {_message(reply, status)}")
    ctx.progress(f"loading {recipe} on the machine (weights download at the first load)")

    def probe() -> tuple[str | None, str]:
        code, health = _call(ctx, "GET", f"{tools}/health", key)
        state = (health.get("models") or {}).get("generator") if code == 200 else None
        if state != "failed":
            return state, ""
        _, capabilities = _call(ctx, "GET", f"{tools}/capabilities", key)
        return state, str((capabilities.get("generator") or {}).get("error", ""))

    seconds = _wait(ctx, f"generator {recipe}", probe)
    ctx.progress(f"{recipe} ready after {seconds:.0f} s")
    _, capabilities = _call(ctx, "GET", f"{tools}/capabilities", key)
    return dict(capabilities.get("generator") or {})


def switch_judge(ctx: Context) -> str:
    """Serve the judge named in the project's `[judge]` on the machine, with the session's server options."""
    judge = ctx.plan_source(ctx.project, ctx.overrides).judge
    if judge is None:
        raise ProvisionError("judge_model_missing", "the project has no judge to serve", "set [judge] model in project.toml")
    endpoint, key = _session(ctx, "judge")
    front = endpoint.removesuffix("/v1")
    body: dict[str, Any] = {"model": judge.model, "revision": judge.revision}
    if judge.gpu_memory_utilization is not None:  # its memory share may change with the judge (a smaller one leaves more)
        body["gpu_memory_utilization"] = judge.gpu_memory_utilization
    status, reply = _call(ctx, "POST", f"{front}/unstage/judge", key, body)
    if status != 202:
        raise ProvisionError("switch_failed", f"the machine refused the judge {judge.model}: {_message(reply, status)}")
    ctx.progress(f"restarting the judge server with {judge.model} (weights download at the first load)")

    def probe() -> tuple[str | None, str]:
        code, snapshot = _call(ctx, "GET", f"{front}/unstage/status", key)
        section = snapshot.get("judge") or {} if code == 200 else {}
        if section.get("model") != judge.model:
            return None, ""
        return section.get("state"), str(section.get("detail", ""))

    seconds = _wait(ctx, f"judge {judge.model}", probe)
    ctx.progress(f"{judge.model} ready after {seconds:.0f} s")
    return judge.model


def _session(ctx: Context, section: str) -> tuple[str, str]:
    """The live session's endpoint for a section and the key that opens it (read from its key file, never printed)."""
    if not ctx.session_path.is_file():
        raise ProvisionError("no_session", "this project has no live session", "start one with `unstage gpu up`")
    entry = tomllib.loads(ctx.session_path.read_text(encoding="utf-8")).get(section) or {}
    endpoint, key_file = str(entry.get("endpoint", "")), str(entry.get("key_file", ""))
    if not endpoint or not key_file:
        raise ProvisionError("no_session", f"the session file names no {section} endpoint")
    return endpoint, userfiles.read_key(userfiles.KeySource(key_file=key_file), "session key")


def _call(ctx: Context, method: str, url: str, key: str, payload: dict[str, Any] | None = None) -> tuple[int, dict[str, Any]]:
    headers = {"Authorization": f"Bearer {key}", "Accept": "application/json"}
    body = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload).encode()
    try:
        reply = ctx.transport(method, url, headers, body, 120.0)
    except ProvisionError as error:
        if error.code == "provider_unreachable":
            return 0, {}
        raise
    try:
        parsed = json.loads(reply.body)
    except ValueError:
        parsed = {}
    return reply.status, parsed if isinstance(parsed, dict) else {}


def _wait(ctx: Context, what: str, probe: Probe) -> float:
    """Seconds until `probe` says ready; a failure or the startup timeout raises."""
    started = ctx.monotonic()
    while ctx.monotonic() - started < ctx.startup_timeout:
        state, detail = probe()
        if state == "ready":
            return ctx.monotonic() - started
        if state == "failed":
            raise ProvisionError("switch_failed", f"{what} failed to load on the machine: {detail[-1600:]}")
        ctx.sleep(ctx.poll_seconds)
    raise ProvisionError("switch_timeout", f"{what} was not ready after {int(ctx.startup_timeout)} s")


def _message(reply: dict[str, Any], status: int) -> str:
    error = reply.get("error") or {}
    return str(error.get("message") or f"HTTP {status}")
