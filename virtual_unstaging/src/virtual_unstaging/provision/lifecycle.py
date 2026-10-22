"""The operations: `up` (rent, arm, install, verify), `down`, `ls` (with reconciliation) and `price`.

All effects go through the `Context`: the provider, the HTTP transport, the clock, the folders, the questions asked.
Nothing here reads the environment or the terminal, so every path runs in tests on fakes.
"""

from __future__ import annotations

import json
import os
import re
import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from virtual_unstaging.config import SESSION_NAME
from virtual_unstaging.provision import machine as machine_module
from virtual_unstaging.provision import providers, sessions, userfiles
from virtual_unstaging.provision.errors import ProvisionError
from virtual_unstaging.provision.limits import format_seconds, parse_limit
from virtual_unstaging.provision.machine import FRONT_PORT, GRACE_SECONDS, NAME_PREFIX, TOOLS_PORT
from virtual_unstaging.provision.plan import GPU_ID, ProjectPlan, check_recipe, load_plan
from virtual_unstaging.provision.provider import (
    FAILED,
    GONE,
    STOPPED,
    GpuOffer,
    Machine,
    Provider,
    datacenters_by_stock,
)
from virtual_unstaging.provision.sessions import SESSION_MARK, Session
from virtual_unstaging.provision.transport import Response, Transport, urllib_transport
from virtual_unstaging.provision.wheel import Wheel, build_default

SESSION_FILE = SESSION_NAME  # the project's session file, as `config.load` reads it
STARTUP_TIMEOUT_SECONDS = 45 * 60
_COUNT_PREFIX = re.compile(r"^([1-8])x\s*(.+)$")


@dataclass
class Context:
    project: Path
    config_folder: Path
    state_folder: Path
    transport: Transport = urllib_transport
    make_provider: Callable[[str, str, Transport], Provider] = providers.make_provider
    build_wheel: Callable[[], tuple[Wheel, Any]] = build_default
    interactive: bool = False
    confirm: Callable[[str], bool] = lambda prompt: False
    progress: Callable[[str], None] = lambda message: None
    now: Callable[[], datetime] = lambda: datetime.now(UTC)
    sleep: Callable[[float], None] = time.sleep
    monotonic: Callable[[], float] = time.monotonic
    startup_timeout: float = STARTUP_TIMEOUT_SECONDS
    poll_seconds: float = 5.0
    overrides: tuple[Path, ...] = ()  # override files layered over project.toml and gpu.toml (design D13)

    @property
    def project_key(self) -> str:
        return str(self.project.resolve())

    @property
    def session_path(self) -> Path:
        return self.project / SESSION_FILE


@dataclass(frozen=True)
class Listing:
    sessions: list[Session]
    warnings: list[str] = field(default_factory=list)


# -- providers and keys ---------------------------------------------------------------------------------


def open_provider(ctx: Context, name: str) -> Provider:
    if name not in providers.provider_names():
        raise ProvisionError("provider_unknown", f"no provider named {name!r}", f"known: {', '.join(providers.provider_names())}")
    source = userfiles.key_source(ctx.config_folder, name, f"{name}.key")
    return ctx.make_provider(name, userfiles.read_key(source, f"{name} API key"), ctx.transport)


def optional_token(ctx: Context, section: str) -> str | None:
    """A token that is only needed for some models (gated repositories): absent is fine."""
    source = userfiles.key_source(ctx.config_folder, section, f"{section}.key")
    if not source.key_command and not Path(source.key_file).expanduser().is_file():
        return None
    return userfiles.read_key(source, f"{section} token")


# -- choosing the machine -------------------------------------------------------------------------------


def parse_gpu(text: str | None) -> tuple[int, str | None]:
    """`NAME` or `2xNAME`: the GPU type to rent and how many."""
    if text is None:
        return 1, None
    count, name = 1, text.strip()
    match = _COUNT_PREFIX.match(name)
    if match:
        count, name = int(match.group(1)), match.group(2).strip()
    if not GPU_ID.fullmatch(name):
        raise ProvisionError("gpu_invalid", f"{text!r} is not a GPU type name", "see `unstage gpu price` for the names")
    return count, name


def choose_offer(offers: list[GpuOffer], wanted: str | None, plan: ProjectPlan) -> GpuOffer:
    by_id = {offer.gpu_id: offer for offer in offers}
    if wanted:
        lowered = wanted.lower()
        matches = [o for o in offers if o.gpu_id.lower() == lowered] or [
            o for o in offers if lowered in o.gpu_id.lower() or lowered in o.name.lower()
        ]
        if len(matches) != 1:
            kind = "no GPU type matches" if not matches else f"{len(matches)} GPU types match"
            raise ProvisionError("gpu_invalid", f"{kind} {wanted!r}", "see `unstage gpu price`; give the full name")
        chosen = matches[0]
    else:
        stocked = [by_id[name] for name in plan.gpu_prefer if name in by_id and datacenters_by_stock(by_id[name])]
        if not stocked:
            raise ProvisionError(
                "no_capacity", "none of the preferred GPU types is in stock",
                f"preferred: {', '.join(plan.gpu_prefer)}; try again later, or pass --gpu (see `unstage gpu price`)",
            )
        chosen = stocked[0]
    if not datacenters_by_stock(chosen):
        raise ProvisionError("no_capacity", f"{chosen.gpu_id} is not in stock anywhere", "try again later, or pick another with --gpu")
    return chosen


# -- the session file -----------------------------------------------------------------------------------


def render_session_file(session: str, tools_url: str, judge_url: str | None, key_file: str, generator: bool) -> str:
    """The endpoints and key files of one session, in the form `config.load` accepts over project.toml."""

    def section(name: str, url: str) -> str:
        return f"[{name}]\nendpoint = {json.dumps(url)}\nkey_file = {json.dumps(key_file)}\n"

    parts = [f"{SESSION_MARK}{session}\n# Written by `unstage gpu up`, removed by `unstage gpu down`. Holds no key, only key file paths.\n"]
    if generator:
        parts.append(section("generator", tools_url))
    if judge_url:
        parts.append(section("judge", judge_url))
    parts.append(section("tools", tools_url))
    return "\n".join(parts)


def check_session_file_free(ctx: Context) -> None:
    """A session file this tool did not write is the user's: it is never overwritten."""
    path = ctx.session_path
    if path.is_file() and not path.read_text(encoding="utf-8").startswith(SESSION_MARK):
        raise ProvisionError("session_file_foreign", f"{path} exists and was not written by `gpu up`", "move it away first")


def write_session_file(ctx: Context, text: str) -> None:
    temporary = ctx.session_path.with_suffix(".toml.part")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, ctx.session_path)


def remove_session_file(ctx: Context, session: str) -> bool:
    """Remove the project's session file if it is this session's. False when it is someone else's or absent."""
    path = ctx.session_path
    if path.is_file() and path.read_text(encoding="utf-8").startswith(f"{SESSION_MARK}{session}\n"):
        path.unlink()
        return True
    return False


# -- up -------------------------------------------------------------------------------------------------


def up(
    ctx: Context, *, provider_name: str, gpu: str | None, limit: str | None, recipe: str | None, assume_yes: bool
) -> Session:
    # Every check that costs nothing comes first; nothing is rented before the last of them.
    seconds = parse_limit(limit)
    recipe = check_recipe(recipe)
    plan = load_plan(ctx.project, ctx.overrides)
    count, wanted = parse_gpu(gpu)
    live = [s for s in sessions.load(ctx.state_folder) if s.live and s.project == ctx.project_key]
    if live:
        raise ProvisionError("session_exists", f"this project already has session {live[0].id}", "`unstage gpu down` first")
    check_session_file_free(ctx)
    provider = open_provider(ctx, provider_name)
    hf_token = optional_token(ctx, "huggingface")
    offer = choose_offer(provider.offers(plan.min_cuda), wanted, plan)
    price = offer.price_per_hour * count
    if offer.memory_gb * count < plan.min_vram_gb:
        ctx.progress(f"warning: {offer.memory_gb * count} GB of GPU memory is below the project's minimum of {plan.min_vram_gb} GB")

    ctx.progress(f"GPU       {count} x {offer.name} ({offer.gpu_id}), {offer.memory_gb} GB each, stock {offer.stock.lower()}")
    ctx.progress(f"price     ${price:.2f} per hour (list price)")
    ctx.progress(
        f"limit     {format_seconds(seconds)} from the moment the machine is created: it deletes itself then, "
        f"even if this computer is off; at most ${price * seconds / 3600:.2f}"
    )
    ctx.progress(f"serves    tool server{' + recipe ' + recipe if recipe else ' (tools only: no --recipe)'}"
                 f"{', judge ' + plan.judge.model if plan.judge else ', no judge (the project uses another judge adapter)'}")
    if not assume_yes:
        if not ctx.interactive:
            raise ProvisionError("confirmation_required", "renting needs a confirmation and there is no terminal", "pass --yes")
        if not ctx.confirm("Rent this machine? [y/N] "):
            raise ProvisionError("not_confirmed", "not confirmed: nothing was rented")

    wheel, keep = ctx.build_wheel()  # before any spending: a build failure costs nothing
    requested_at = ctx.now()  # the limit counts from here, not from the moment the question was answered
    deadline = requested_at + timedelta(seconds=seconds)
    try:
        return _rent(ctx, provider, plan, wheel, offer, count, wanted_recipe=recipe, hf_token=hf_token,
                     seconds=seconds, requested_at=requested_at, deadline=deadline, provider_name=provider_name)
    finally:
        cleanup = getattr(keep, "cleanup", None)
        if callable(cleanup):
            cleanup()


def _rent(
    ctx: Context, provider: Provider, plan: ProjectPlan, wheel: Wheel, offer: GpuOffer, count: int, *,
    wanted_recipe: str | None, hf_token: str | None, seconds: int, requested_at: datetime, deadline: datetime,
    provider_name: str,
) -> Session:
    sid = uuid.uuid4().hex[:8]
    name = f"{NAME_PREFIX}{sid}"
    key = userfiles.new_session_key()
    key_path = userfiles.write_session_key(ctx.config_folder, sid, key)
    sessions.append(
        ctx.state_folder, "requested", sid, requested_at,
        project=ctx.project_key, provider=provider_name, machine_name=name, gpu=offer.gpu_id, gpu_count=count,
        limit_seconds=seconds, deadline=sessions.to_iso(deadline), estimated_price_per_hour=offer.price_per_hour * count,
        key_file=str(key_path), session_file=str(ctx.session_path),
    )
    try:
        machine = _create_first_fit(ctx, provider, plan, wheel, offer, count, name, key, hf_token, deadline, wanted_recipe)
    except BaseException as error:
        reason = error.code if isinstance(error, ProvisionError) else type(error).__name__
        sessions.append(ctx.state_folder, "failed", sid, ctx.now(), reason=reason)
        _end_stray(ctx, provider, name, sid)
        sessions.append(ctx.state_folder, "ended", sid, ctx.now(), by="not-created")
        userfiles.remove_session_key(key_path)
        raise
    price = machine.price_per_hour or offer.price_per_hour * count
    sessions.append(ctx.state_folder, "created", sid, ctx.now(), machine_id=machine.id, datacenter=machine.datacenter,
                    price_per_hour=price)
    ctx.progress(f"session {sid}: machine {machine.id} in {machine.datacenter or 'an unknown data center'} created at "
                 f"${price:.2f}/h; deadline {deadline.astimezone().strftime('%H:%M %Z')}")
    try:
        measurements = _start(ctx, provider, plan, wheel, machine, key, key_path, sid, deadline)
    except BaseException as error:
        _abort(ctx, provider, sid, machine, key_path, error)
        raise AssertionError("unreachable") from error
    sessions.append(ctx.state_folder, "ready", sid, ctx.now(), measurements=measurements)
    return next(s for s in sessions.load(ctx.state_folder) if s.id == sid)


def _end_stray(ctx: Context, provider: Provider, name: str, sid: str) -> None:
    """After a failed or interrupted create: a machine may exist although no answer reached us. Look by name, delete it."""
    try:
        stray = provider.find(name)
    except ProvisionError:
        stray = None
    if stray is not None:
        try:
            _delete_and_confirm(ctx, provider, stray.id, f"session {sid}")
        except ProvisionError as failure:
            raise ProvisionError("machine_delete_failed", f"a machine was created and could not be deleted: {failure.message}",
                                 failure.hint) from failure


def _create_first_fit(
    ctx: Context, provider: Provider, plan: ProjectPlan, wheel: Wheel, offer: GpuOffer, count: int, name: str,
    key: str, hf_token: str | None, deadline: datetime, recipe: str | None,
) -> Machine:
    """Create on the first data center that accepts. A lost answer never leaves an unknown machine: look it up by name."""
    refused = []
    for datacenter in datacenters_by_stock(offer):
        spec = machine_module.build_spec(
            provider, plan, wheel, name=name, gpu_id=offer.gpu_id, gpu_count=count, datacenter=datacenter, key=key,
            hf_token=hf_token, deadline_epoch=deadline.timestamp(),
            deadline_iso=deadline.astimezone(UTC).isoformat(timespec="seconds"), recipe=recipe,
        )
        try:
            return provider.create(spec)
        except ProvisionError as error:
            if error.code == "provider_refused":
                ctx.progress(f"{offer.gpu_id} in {datacenter} refused: {error.message}")
                refused.append(datacenter)
                continue
            if error.code in ("provider_unreachable", "provider_error"):
                found = provider.find(name)  # the machine may exist although the answer was lost
                if found is not None:
                    return found
            raise
    raise ProvisionError("no_capacity", f"{offer.gpu_id} was refused in all {len(refused)} data centers in stock",
                         "try again later, or pick another GPU with --gpu")


# -- starting up: guard, wheel, services, endpoints -----------------------------------------------------


def _status_call(ctx: Context, method: str, url: str, key: str | None, body: bytes | None = None) -> Response:
    headers = {"Accept": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    if body is not None:
        headers["Content-Type"] = "application/octet-stream"
    try:
        return ctx.transport(method, url, headers, body, 120.0)
    except ProvisionError as error:
        if error.code == "provider_unreachable":
            return Response(0, b"")  # not reachable yet
        raise


def _json(reply: Response) -> dict[str, Any]:
    try:
        parsed = json.loads(reply.body)
    except ValueError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def _start(
    ctx: Context, provider: Provider, plan: ProjectPlan, wheel: Wheel, machine: Machine, key: str, key_path: Path,
    sid: str, deadline: datetime,
) -> dict[str, Any]:
    tools_url = provider.url(machine.id, TOOLS_PORT)
    front_url = provider.url(machine.id, FRONT_PORT)
    judge_url = f"{front_url}/v1" if plan.judge else None
    started = ctx.monotonic()
    give_up = started + ctx.startup_timeout
    measurements: dict[str, Any] = {}

    def alive() -> None:
        current = provider.get(machine.id)
        if current is None and ctx.monotonic() - started < 60.0:
            return  # a machine just created may not be listed yet
        if current is None or current.status in (GONE, FAILED, STOPPED):
            raise ProvisionError("startup_failed", f"the machine is {'gone' if current is None else current.status}")

    def wait(what: str) -> None:
        if ctx.monotonic() > give_up:
            raise ProvisionError("startup_timeout", f"{what} did not happen within {format_seconds(ctx.startup_timeout)}")
        ctx.sleep(ctx.poll_seconds)

    # 1. The guard: the machine must report that it can delete itself. Without it the machine is not kept.
    status: dict[str, Any] = {}
    while not status:
        alive()
        reply = _status_call(ctx, "GET", f"{front_url}/unstage/status", key)
        if reply.status == 200:
            status = _json(reply)
        elif reply.status in (401, 403):
            raise ProvisionError("startup_failed", "the machine rejected the session key")
        else:
            wait("the machine's answer")
    guard = status.get("guard") or {}
    if guard.get("armed") is not True:
        raise ProvisionError(
            "guard_not_armed" if guard.get("armed") is False else "guard_not_reported",
            "the machine's self-delete guard did not arm: a machine that cannot delete itself is not kept",
            "the machine is being deleted; try again, and `unstage gpu ls` to check that nothing is left",
        )
    measurements["guard_api"] = guard.get("api")
    measurements["guard_after_s"] = round(ctx.monotonic() - started)
    ctx.progress(f"guard armed ({guard.get('api')}); uploading the wheel ({wheel.size} bytes)")

    # 2. The wheel: the package is on no index, so it travels as one hash-checked file.
    _upload_wheel(ctx, front_url, key, wheel, wait)

    # 3. The services.
    while True:
        alive()
        status = _json(_status_call(ctx, "GET", f"{front_url}/unstage/status", key))
        tools, judge = status.get("tools") or {}, status.get("judge") or {}
        for service, state in (("tool server", tools), ("judge server", judge)):
            if state.get("state") == "failed":
                detail = str(state.get("detail", ""))
                detail = detail if len(detail) <= 1600 else "…" + detail[-1600:]  # the end holds the error
                raise ProvisionError("startup_failed", f"the {service} failed on the machine: {detail}")
        if tools.get("state") == "ready" and judge.get("state") in ("ready", "off"):
            break
        wait("the services")
    measurements["services_after_s"] = round(ctx.monotonic() - started)

    # 4. Healthy means authenticated: each endpoint answers with the key and refuses without it.
    _verify_endpoints(ctx, tools_url, judge_url, plan, key)
    measurements["seconds_left"] = status.get("seconds_left")
    left = int((deadline - ctx.now()).total_seconds())
    ctx.progress(f"ready after {format_seconds(ctx.monotonic() - started)}; {format_seconds(max(0, left))} of the limit remain")

    text = render_session_file(sid, tools_url, judge_url, str(key_path), plan.serves_generator_endpoint)
    write_session_file(ctx, text)
    return measurements


def _upload_wheel(ctx: Context, front_url: str, key: str, wheel: Wheel, wait: Callable[[str], None]) -> None:
    for _ in range(4):
        reply = _status_call(ctx, "PUT", f"{front_url}/unstage/wheel", key, wheel.read())
        if reply.status == 201:
            return
        if reply.status == 409:  # a retry after a lost answer: fine if the machine has it
            state = _json(_status_call(ctx, "GET", f"{front_url}/unstage/status", key)).get("wheel") or {}
            if state.get("state") == "received":
                return
        if reply.status in (400, 411, 413, 500):
            raise ProvisionError("upload_failed", f"the machine refused the wheel: HTTP {reply.status} {_json(reply).get('error', {})}")
        wait("the wheel upload")
    raise ProvisionError("upload_failed", "the wheel could not be uploaded")


def _verify_endpoints(ctx: Context, tools_url: str, judge_url: str | None, plan: ProjectPlan, key: str) -> None:
    health = _status_call(ctx, "GET", f"{tools_url}/health", None)
    if health.status != 200:
        raise ProvisionError("endpoint_unverified", f"the tool server's /health answers HTTP {health.status}")
    checks = [(f"{tools_url}/capabilities", "tool server")]
    if judge_url:
        checks.append((f"{judge_url}/models", "judge server"))
    for url, label in checks:
        with_key = _status_call(ctx, "GET", url, key)
        if with_key.status != 200:
            raise ProvisionError("endpoint_unverified", f"the {label} refuses the session key: HTTP {with_key.status}")
        if _status_call(ctx, "GET", url, None).status not in (401, 403):
            raise ProvisionError("endpoint_unverified", f"the {label} answers without a key: authentication is off")
    if judge_url and plan.judge:
        listed = [m.get("id") for m in _json(_status_call(ctx, "GET", f"{judge_url}/models", key)).get("data", []) if isinstance(m, dict)]
        if plan.judge.model not in listed:
            raise ProvisionError("endpoint_unverified", f"the judge server does not list {plan.judge.model}")


# -- ending machines ------------------------------------------------------------------------------------


def _delete_and_confirm(ctx: Context, provider: Provider, machine_id: str, label: str) -> None:
    """Delete, retrying, then check it is gone. A failure says plainly that the machine may still be billing."""
    still = f"the machine may still be billing: run `unstage gpu down`, or delete {machine_id} in the provider's console"
    last: ProvisionError | None = None
    for attempt in range(3):
        try:
            provider.delete(machine_id)
            last = None
            break
        except ProvisionError as error:
            last = error
            if attempt < 2:
                ctx.sleep(5.0)
    if last is not None:
        raise ProvisionError("machine_delete_failed", f"could not delete the machine of {label}: {last.message}", still)
    for _ in range(6):
        current = provider.get(machine_id)
        if current is None or current.status == GONE:
            return
        ctx.sleep(5.0)
    raise ProvisionError("machine_delete_failed", f"the machine of {label} is still listed after the delete", still)


def _abort(ctx: Context, provider: Provider, sid: str, machine: Machine, key_path: Path, error: BaseException) -> None:
    """Startup failed or was interrupted after the machine exists: delete it, then raise. Nothing is kept."""
    interrupted = isinstance(error, (KeyboardInterrupt, SystemExit))
    sessions.append(ctx.state_folder, "failed", sid, ctx.now(),
                    reason=error.code if isinstance(error, ProvisionError) else type(error).__name__)
    try:
        _delete_and_confirm(ctx, provider, machine.id, f"session {sid}")
    except ProvisionError as failure:
        raise ProvisionError(
            "machine_delete_failed", f"start failed ({error}) and the machine could not be deleted: {failure.message}",
            failure.hint,
        ) from failure
    sessions.append(ctx.state_folder, "ended", sid, ctx.now(), by="interrupted" if interrupted else "startup-failure")
    userfiles.remove_session_key(key_path)
    remove_session_file(ctx, sid)
    if interrupted or isinstance(error, ProvisionError):
        raise error
    raise ProvisionError("startup_failed", f"{type(error).__name__}: {error}") from error


def end_session(ctx: Context, session: Session, by: str) -> Session:
    provider = open_provider(ctx, session.provider)
    machine_id = session.machine_id
    if not machine_id:  # requested, but the answer was lost before it was recorded
        found = provider.find(session.machine_name)
        machine_id = found.id if found else ""
    if machine_id:
        current = provider.get(machine_id)
        if current is not None and current.name != session.machine_name:
            raise ProvisionError("machine_mismatch", f"machine {machine_id} is not the one rented for session {session.id}",
                                 "it is left alone; check the provider's console")
        if current is not None and current.status != GONE:
            _delete_and_confirm(ctx, provider, machine_id, f"session {session.id}")
    sessions.append(ctx.state_folder, "ended", session.id, ctx.now(), by=by)
    if session.key_file:
        userfiles.remove_session_key(Path(session.key_file))
    remove_session_file(ctx, session.id)
    return next(s for s in sessions.load(ctx.state_folder) if s.id == session.id)


def down(ctx: Context) -> list[Session]:
    live = [s for s in sessions.load(ctx.state_folder) if s.live and s.project == ctx.project_key]
    if not live:
        raise ProvisionError("session_not_found", f"no live GPU session for {ctx.project_key}", "`unstage gpu ls` lists them all")
    return [end_session(ctx, s, "down") for s in live]


# -- ls and price ---------------------------------------------------------------------------------------


def reconcile(ctx: Context, all_sessions: list[Session]) -> list[str]:
    """Compare live sessions with the provider's machines: close the vanished ones, warn on the late and the unknown."""
    warnings: list[str] = []
    now = ctx.now()
    for provider_name in sorted({s.provider for s in all_sessions if s.live}):
        try:
            provider = open_provider(ctx, provider_name)
            machines = {m.id: m for m in provider.list_machines(NAME_PREFIX)}
        except ProvisionError as error:
            warnings.append(f"{provider_name}: could not compare with the provider ({error.code}); the local log only")
            continue
        known_names = {s.machine_name for s in all_sessions}
        for s in all_sessions:
            if not s.live or s.provider != provider_name or not s.machine_id:
                continue
            if s.machine_id not in machines:
                at = min(now, s.deadline + timedelta(seconds=GRACE_SECONDS))
                sessions.append(ctx.state_folder, "ended", s.id, at, by="machine-gone")
                continue
            if now > s.deadline + timedelta(seconds=GRACE_SECONDS + 300):
                late = int((now - s.deadline).total_seconds() // 60)
                warnings.append(f"session {s.id}: its machine is still there {late} min past the deadline, so the guard failed: "
                                f"`unstage --project {s.project} gpu down`")
        warnings += [f"machine {m.id} ({m.name}) is not in the session log: delete it in the provider's console if it is yours"
                     for m in machines.values() if m.name not in known_names]
    return warnings


def ls(ctx: Context) -> Listing:
    found = sessions.load(ctx.state_folder)
    warnings = reconcile(ctx, found) if any(s.live for s in found) else []
    return Listing(sessions.load(ctx.state_folder), warnings)


def price(ctx: Context, provider_name: str, wanted: str | None) -> list[GpuOffer]:
    provider = open_provider(ctx, provider_name)
    offers = [o for o in provider.offers(None) if o.price_per_hour > 0]
    if wanted:
        _, name = parse_gpu(wanted)
        lowered = (name or "").lower()
        offers = [o for o in offers if lowered in o.gpu_id.lower() or lowered in o.name.lower()]
    return sorted(offers, key=lambda o: (o.price_per_hour, o.gpu_id))
