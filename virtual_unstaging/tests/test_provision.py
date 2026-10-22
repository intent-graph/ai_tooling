"""GPU provisioning: limit, confirmation, provider, on-machine guard and bootstrap, session files. No network, no money."""

from __future__ import annotations

import argparse
import hashlib
import http.client
import http.server
import importlib.util
import json
import socket
import stat
import sys
import threading
import time
import tomllib
import urllib.parse
from collections.abc import Iterator
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pytest

from virtual_unstaging import config
from virtual_unstaging.cli import main as cli_main
from virtual_unstaging.provision import lifecycle, machine, plan, sessions, userfiles
from virtual_unstaging.provision.commands import gpu_command
from virtual_unstaging.provision.errors import ProvisionError
from virtual_unstaging.provision.limits import format_seconds, parse_limit
from virtual_unstaging.provision.provider import GONE, RUNNING, GpuOffer, Machine, MachineSpec
from virtual_unstaging.provision.runpod import RunpodProvider
from virtual_unstaging.provision.transport import Response
from virtual_unstaging.provision.wheel import Wheel, build_wheel

PROVISION_DIR = Path(lifecycle.__file__).parent
JUDGE_MODEL = "org/judge-model"
START = datetime(2026, 10, 21, 12, 0, tzinfo=UTC)


# -- nothing leaves the machine running the tests ------------------------------------------------------------


@pytest.fixture(autouse=True)
def no_outside_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Any connection that is not to this computer fails the test: no cloud resource can be reached from here."""
    real = socket.socket.connect

    def guarded(self: socket.socket, address: Any) -> Any:
        host = address[0] if isinstance(address, tuple) else address
        if self.family == socket.AF_UNIX or host in ("127.0.0.1", "::1", "localhost"):
            return real(self, address)
        raise AssertionError(f"test tried to connect to {address!r}")

    monkeypatch.setattr(socket.socket, "connect", guarded)


@pytest.fixture(autouse=True)
def user_folders(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "xdg_config"))
    monkeypatch.setenv("XDG_STATE_HOME", str(tmp_path / "xdg_state"))


# -- fakes -----------------------------------------------------------------------------------------------------


class Clock:
    def __init__(self) -> None:
        self.at = START
        self.mono = 0.0

    def now(self) -> datetime:
        return self.at

    def sleep(self, seconds: float) -> None:
        self.at += timedelta(seconds=seconds)
        self.mono += seconds

    def monotonic(self) -> float:
        return self.mono


class FakeWorld:
    """A provider and the machine it rents, in one object: records every call, answers like the real thing."""

    name = "runpod"
    guard_class = "RunpodSelfDelete"

    def __init__(self, *, armed: bool | None = True) -> None:
        self.armed = armed
        self.guard_source = (PROVISION_DIR / "runpod_guard.py").read_text(encoding="utf-8")
        self.offer_list = [
            GpuOffer("NVIDIA H100 80GB HBM3", "H100", 80, 2.99, "MEDIUM", (("US-A", "LOW"), ("US-B", "HIGH"))),
            GpuOffer("NVIDIA RTX PRO 6000 Blackwell Server Edition", "RTX PRO 6000", 96, 1.89, "HIGH",
                     (("EU-1", "HIGH"), ("EU-2", "MEDIUM"))),
            GpuOffer("NVIDIA A100 80GB PCIe", "A100", 80, 1.39, "NONE", (("EU-3", "NONE"),)),
        ]
        self.refused: set[str] = set()
        self.created: list[MachineSpec] = []
        self.deleted: list[str] = []
        self.delete_failures = 0
        self.create_error: ProvisionError | None = None
        self.create_then_lose_answer = False
        self.machines: dict[str, Machine] = {}
        self.requests: list[tuple[str, str]] = []
        self.not_ready_polls = 2
        self.status_calls = 0
        self.ready_polls = 0
        self.wheel_received = False
        self.tools_state = "ready"
        self.judge_state = "ready"
        self.open_endpoints = False
        self.key = ""

    # provider interface
    def offers(self, min_cuda: str | None = None) -> list[GpuOffer]:
        return list(self.offer_list)

    def create(self, spec: MachineSpec) -> Machine:
        if self.create_error is not None:
            raise self.create_error
        if spec.datacenter in self.refused:
            raise ProvisionError("provider_refused", f"no capacity in {spec.datacenter}")
        self.created.append(spec)
        self.key = spec.env[machine.KEY_ENV]
        made = Machine("pod12345", spec.name, RUNNING, 1.89 * spec.gpu_count, spec.datacenter)
        self.machines[made.id] = made
        if self.create_then_lose_answer:
            raise ProvisionError("provider_unreachable", "the answer was lost")
        return made

    def get(self, machine_id: str) -> Machine | None:
        return self.machines.get(machine_id)

    def find(self, name: str) -> Machine | None:
        return next((m for m in self.machines.values() if m.name == name), None)

    def list_machines(self, name_prefix: str) -> list[Machine]:
        return [m for m in self.machines.values() if m.name.startswith(name_prefix)]

    def delete(self, machine_id: str) -> None:
        if self.delete_failures:
            self.delete_failures -= 1
            raise ProvisionError("provider_error", "delete refused")
        self.machines.pop(machine_id, None)
        self.deleted.append(machine_id)

    def url(self, machine_id: str, port: int) -> str:
        return f"https://{machine_id}-{port}.proxy.test"

    # the machine's HTTP surface
    def transport(self, method: str, url: str, headers: dict[str, str], body: bytes | None, timeout: float) -> Response:
        self.requests.append((method, url))
        parts = urllib.parse.urlsplit(url)
        machine_id, port = str(parts.hostname).split(".")[0].rsplit("-", 1)
        if machine_id not in self.machines:
            return Response(404, b"")
        token = headers.get("Authorization", "")[7:]
        authorized = token == self.key or self.open_endpoints
        path = parts.path
        if port == "8001":
            if not authorized:
                return Response(401, b"{}")
            return self._front(method, path, body)
        if port == "8000":
            if path == "/health":
                return Response(200, b'{"status": "ok"}')
            if path == "/capabilities":
                return Response(200, b"{}") if authorized else Response(401, b"{}")
        return Response(404, b"")

    def _front(self, method: str, path: str, body: bytes | None) -> Response:
        if path == "/v1/models":
            return Response(200, json.dumps({"data": [{"id": JUDGE_MODEL}]}).encode())
        if path == "/unstage/wheel" and method == "PUT":
            plan_json = json.loads(self.created[-1].env["UNSTAGE_PLAN"])
            if hashlib.sha256(body or b"").hexdigest() != plan_json["wheel"]["sha256"]:
                return Response(400, b'{"error": {"code": "hash_mismatch"}}')
            self.wheel_received = True
            return Response(201, b"{}")
        if path == "/unstage/status":
            self.status_calls += 1
            if self.status_calls <= self.not_ready_polls:
                return Response(502, b"bad gateway")
            if self.wheel_received:
                self.ready_polls += 1
            done = self.wheel_received and self.ready_polls >= 2
            tools = self.tools_state if done else ("installing" if self.wheel_received else "waiting_wheel")
            judge = self.judge_state if done else "starting"
            status = {
                "guard": {"armed": self.armed, "api": "rest-v2"},
                "tools": {"state": tools, "detail": "pip failed: no space left"},
                "judge": {"state": judge, "detail": ""},
                "wheel": {"state": "received" if self.wheel_received else "waiting"},
                "seconds_left": 9000,
            }
            return Response(200, json.dumps(status).encode())
        return Response(404, b"")


def make_wheel(folder: Path) -> Wheel:
    data = b"not a real wheel, but bytes with a hash"
    path = folder / "virtual_unstaging-0.1.0-py3-none-any.whl"
    path.write_bytes(data)
    return Wheel(path, path.name, hashlib.sha256(data).hexdigest(), len(data))


@pytest.fixture
def gpu_project(tmp_path: Path) -> Path:
    project = tmp_path / "project"
    assert cli_main(["--project", str(project), "init", "--name", "unit"]) == 0
    text = (project / "project.toml").read_text(encoding="utf-8")
    (project / "project.toml").write_text(text.replace('model = ""\nrevision = "unpinned"\nbox_scale',
                                                        f'model = "{JUDGE_MODEL}"\nrevision = "unpinned"\nbox_scale'),
                                          encoding="utf-8")
    return project


@pytest.fixture
def clock() -> Clock:
    return Clock()


@pytest.fixture
def world() -> FakeWorld:
    return FakeWorld()


def write_api_key(tmp_path: Path, name: str = "runpod.key", mode: int = 0o600) -> Path:
    folder = tmp_path / "xdg_config" / userfiles.APP_FOLDER
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / name
    path.write_text("rpa_secret_api_key_value\n", encoding="utf-8")
    path.chmod(mode)
    return path


def make_context(tmp_path: Path, project: Path, world: FakeWorld, clock: Clock, **overrides: Any) -> lifecycle.Context:
    write_api_key(tmp_path)
    messages: list[str] = []
    values: dict[str, Any] = {
        "project": project,
        "config_folder": tmp_path / "xdg_config" / userfiles.APP_FOLDER,
        "state_folder": tmp_path / "xdg_state" / userfiles.APP_FOLDER,
        "transport": world.transport,
        "make_provider": lambda name, key, transport: world,
        "build_wheel": lambda: (make_wheel(tmp_path), None),
        "progress": messages.append,
        "now": clock.now,
        "sleep": clock.sleep,
        "monotonic": clock.monotonic,
        "poll_seconds": 1.0,
    }
    values.update(overrides)
    ctx = lifecycle.Context(**values)
    ctx.messages = messages  # type: ignore[attr-defined]
    return ctx


def run_up(ctx: lifecycle.Context, **overrides: Any) -> sessions.Session:
    values: dict[str, Any] = {"provider_name": "runpod", "gpu": None, "limit": "3h", "recipe": None, "assume_yes": True}
    values.update(overrides)
    return lifecycle.up(ctx, **values)


def namespace(project: Path, action: str, **overrides: Any) -> argparse.Namespace:
    values: dict[str, Any] = {"action": action, "provider": "runpod", "gpu": None, "limit": None, "recipe": None,
                              "yes": False, "project": str(project)}
    values.update(overrides)
    return argparse.Namespace(**values)


# -- the time limit cannot be skipped ----------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("text", "seconds"),
    [("3h", 10800), ("90m", 5400), ("1h30m", 5400), ("45m30s", 2730), ("5m", 300), ("24h", 86400), (" 2H ", 7200)],
)
def test_limit_grammar(text: str, seconds: int) -> None:
    assert parse_limit(text) == seconds


@pytest.mark.parametrize("text", ["", "   ", "3", "h", "3 h", "-1h", "1.5h", "3h30", "abc", "3hh", "1d", "4m5h"])
def test_limit_rejects_what_is_not_a_duration(text: str) -> None:
    with pytest.raises(ProvisionError) as caught:
        parse_limit(text)
    assert caught.value.code in ("limit_required", "limit_invalid")


@pytest.mark.parametrize("text", ["4m", "25h", "0h", "1441m"])
def test_limit_is_bounded(text: str) -> None:
    with pytest.raises(ProvisionError) as caught:
        parse_limit(text)
    assert caught.value.code == "limit_out_of_range"


def test_limit_none_is_refused_with_a_usage_code() -> None:
    with pytest.raises(ProvisionError) as caught:
        parse_limit(None)
    assert (caught.value.code, caught.value.exit_code) == ("limit_required", 2)
    assert format_seconds(5400) == "1h30m"


def test_up_without_limit_touches_nothing(gpu_project: Path, tmp_path: Path, clock: Clock) -> None:
    def forbidden(*args: object) -> None:
        raise AssertionError("the provider was reached although no limit was given")

    ctx = make_context(tmp_path, gpu_project, FakeWorld(), clock, make_provider=forbidden)
    assert gpu_command(namespace(gpu_project, "up", yes=True), ctx) == 2
    assert not (tmp_path / "xdg_state").exists()
    assert not (gpu_project / "gpu_session.toml").exists()


def test_cli_gpu_up_without_limit_exits_2_before_any_effect(gpu_project: Path, tmp_path: Path) -> None:
    assert cli_main(["--project", str(gpu_project), "gpu", "up", "--yes"]) == 2
    assert not (tmp_path / "xdg_state").exists()
    assert not (tmp_path / "xdg_config").exists()


def test_the_machine_spec_cannot_be_built_without_a_deadline() -> None:
    signature = machine.build_spec.__kwdefaults__ or {}
    assert "deadline_epoch" not in signature and "deadline_iso" not in signature


# -- confirmation ---------------------------------------------------------------------------------------------


def test_no_terminal_and_no_yes_refuses_and_rents_nothing(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock, interactive=False)
    assert gpu_command(namespace(gpu_project, "up", limit="3h"), ctx) == 2
    assert world.created == []


def test_declined_confirmation_rents_nothing(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    asked: list[str] = []
    ctx = make_context(tmp_path, gpu_project, world, clock, interactive=True, confirm=lambda prompt: asked.append(prompt) or False)
    assert gpu_command(namespace(gpu_project, "up", limit="3h"), ctx) == 1
    assert asked and world.created == []
    shown = "\n".join(ctx.messages)  # type: ignore[attr-defined]
    assert "RTX PRO 6000" in shown and "$1.89 per hour" in shown and "3h00m" in shown and "even if this computer is off" in shown


def test_the_limit_counts_from_after_the_question_is_answered(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    def slow_answer(prompt: str) -> bool:
        clock.sleep(600)  # ten minutes at the prompt
        return True

    ctx = make_context(tmp_path, gpu_project, world, clock, interactive=True, confirm=slow_answer)
    session = run_up(ctx, assume_yes=False)
    assert session.deadline >= START + timedelta(minutes=600 // 60) + timedelta(hours=3)


def test_accepted_confirmation_rents(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock, interactive=True, confirm=lambda prompt: True)
    assert gpu_command(namespace(gpu_project, "up", limit="3h"), ctx) == 0
    assert len(world.created) == 1


# -- up: the whole path ---------------------------------------------------------------------------------------


def test_up_rents_arms_uploads_verifies_and_writes_the_session(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock, capsys: pytest.CaptureFixture[str]
) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    assert gpu_command(namespace(gpu_project, "up", limit="3h", recipe="some_recipe", yes=True), ctx) == 0
    spec = world.created[0]
    assert spec.gpu_id == "NVIDIA RTX PRO 6000 Blackwell Server Edition"  # the first preferred GPU in stock
    assert spec.datacenter == "EU-1"  # the best stocked
    assert spec.ports == (8000, 8001) and spec.name.startswith("unstage-")
    plan_json = json.loads(spec.env["UNSTAGE_PLAN"])
    assert plan_json["deadline"] == (START + timedelta(hours=3)).timestamp()  # absolute
    assert plan_json["tools_argv"][-2:] == ["--recipe", "some_recipe"]
    assert plan_json["tools_argv"][plan_json["tools_argv"].index("--deadline") + 1] == "2026-10-21T15:00:00+00:00"  # absolute, UTC
    assert "--deadline" in plan_json["tools_argv"] and "--key-env" in plan_json["tools_argv"]
    assert plan_json["judge_argv"][:3] == ["vllm", "serve", JUDGE_MODEL]
    assert plan_json["wheel"]["sha256"] == hashlib.sha256(b"not a real wheel, but bytes with a hash").hexdigest()
    assert world.wheel_received
    out = capsys.readouterr().out.splitlines()
    assert out[0].startswith("session\t") and "tools\thttps://pod12345-8000.proxy.test" in out
    assert "judge\thttps://pod12345-8001.proxy.test/v1" in out
    assert out[-1] == f"deadline\t{(START + timedelta(hours=3)).isoformat()}"

    # the key: generated per session, in a mode 600 file, never in the session file or the log
    key = world.key
    key_files = list((tmp_path / "xdg_config" / userfiles.APP_FOLDER / "keys").glob("session-*.key"))
    assert len(key_files) == 1 and key_files[0].read_text().strip() == key
    assert stat.S_IMODE(key_files[0].stat().st_mode) == 0o600
    session_text = (gpu_project / "gpu_session.toml").read_text()
    assert key not in session_text and key_files[0].as_posix() in session_text
    log_text = (tmp_path / "xdg_state" / userfiles.APP_FOLDER / sessions.LOG_NAME).read_text()
    assert key not in log_text and "rpa_secret_api_key_value" not in log_text
    # the provider's API key never reaches the machine
    assert all("rpa_secret_api_key_value" not in value for value in spec.env.values())

    # the project reads the session over project.toml
    cfg = config.load(gpu_project)
    assert cfg.tools_endpoint == "https://pod12345-8000.proxy.test"
    assert cfg.generator.endpoint == "https://pod12345-8000.proxy.test"
    assert cfg.judge.endpoint == "https://pod12345-8001.proxy.test/v1"
    assert cfg.judge.secret.read() == key and cfg.generator.secret.read() == key and cfg.tools_secret.read() == key


def test_the_deadline_given_to_the_tool_server_is_one_it_parses_and_is_the_same_instant(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock
) -> None:
    from virtual_unstaging.serve.deadline import parse_deadline

    run_up(make_context(tmp_path, gpu_project, world, clock), recipe="fake")
    argv = json.loads(world.created[0].env["UNSTAGE_PLAN"])["tools_argv"]
    assert parse_deadline(argv[argv.index("--deadline") + 1], START) == START + timedelta(hours=3)
    from virtual_unstaging.serve.recipe import RECIPE_DIR

    assert (RECIPE_DIR / "fake.toml").is_file()  # the recipe name travels as a name; the wheel carries the file


def test_up_log_records_the_session_append_only(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    session = run_up(ctx)
    events = sessions.read(tmp_path / "xdg_state" / userfiles.APP_FOLDER)
    assert [e["event"] for e in events] == ["requested", "created", "ready"]
    assert session.state == "ready" and session.price_per_hour == 1.89 and session.limit_seconds == 10800
    assert session.deadline == START + timedelta(hours=3)


def test_up_prefers_nothing_in_stock_it_cannot_get(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    world.offer_list = [GpuOffer("NVIDIA A100 80GB PCIe", "A100", 80, 1.39, "NONE", (("EU-3", "NONE"),))]
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "no_capacity" and world.created == []


def test_up_explicit_gpu_by_unique_substring_and_count(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx, gpu="2xH100")
    spec = world.created[0]
    assert (spec.gpu_id, spec.gpu_count, spec.datacenter) == ("NVIDIA H100 80GB HBM3", 2, "US-B")
    plan_json = json.loads(spec.env["UNSTAGE_PLAN"])
    assert (plan_json["judge_gpu"], plan_json["tools_gpu"]) == ("1", "0")  # two GPUs: one each
    assert "--gpu-memory-utilization" in plan_json["judge_argv"]


def test_up_unknown_or_ambiguous_gpu_is_a_usage_error(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    for wanted in ("nothing like it", "NVIDIA"):
        with pytest.raises(ProvisionError) as caught:
            run_up(ctx, gpu=wanted)
        assert caught.value.code == "gpu_invalid" and caught.value.exit_code == 2
    assert world.created == []


def test_up_tries_the_next_data_center_when_refused(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    world.refused = {"EU-1"}
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    assert world.created[0].datacenter == "EU-2"


def test_up_all_refused_is_no_capacity_and_leaves_nothing(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    world.refused = {"EU-1", "EU-2"}
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "no_capacity"
    assert not list((tmp_path / "xdg_config" / userfiles.APP_FOLDER / "keys").glob("*.key"))
    assert all(not s.live for s in sessions.load(tmp_path / "xdg_state" / userfiles.APP_FOLDER))


def test_a_lost_create_answer_finds_the_machine_by_name(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    world.create_then_lose_answer = True
    ctx = make_context(tmp_path, gpu_project, world, clock)
    session = run_up(ctx)
    assert session.machine_id == "pod12345" and len(world.created) == 1


def test_an_interrupted_create_deletes_a_machine_that_may_exist(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    original = world.create

    def interrupted(spec: MachineSpec) -> Machine:
        original(spec)  # the machine is created, then the user presses Ctrl-C before the answer arrives
        raise KeyboardInterrupt

    world.create = interrupted  # type: ignore[method-assign]
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(KeyboardInterrupt):
        run_up(ctx)
    assert world.deleted == ["pod12345"] and not world.machines


def test_up_refuses_a_second_live_session_for_the_project(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "session_exists" and len(world.created) == 1


def test_up_never_overwrites_a_session_file_it_did_not_write(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    (gpu_project / "gpu_session.toml").write_text("[tools]\nendpoint = 'http://mine'\n", encoding="utf-8")
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "session_file_foreign" and world.created == []


def test_up_without_a_judge_adapter_serves_tools_only(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    text = (gpu_project / "project.toml").read_text().replace('adapter = "openai_chat"', 'adapter = "fake"')
    (gpu_project / "project.toml").write_text(text, encoding="utf-8")
    world.judge_state = "off"
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    plan_json = json.loads(world.created[0].env["UNSTAGE_PLAN"])
    assert plan_json["judge_argv"] is None
    assert "[judge]" not in (gpu_project / "gpu_session.toml").read_text()


def test_up_takes_its_plan_from_an_injected_source(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    own_plan = replace(plan.load_plan(gpu_project), tools=("change_map",))
    folder = tmp_path / "caller_folder"  # a caller's own folder: no project.toml, only the session file lands here
    folder.mkdir()
    ctx = make_context(tmp_path, folder, world, clock, plan_source=lambda project, overrides: own_plan)
    run_up(ctx, recipe="fake")
    argv = json.loads(world.created[0].env["UNSTAGE_PLAN"])["tools_argv"]
    assert argv[argv.index("--tools") + 1] == "change_map" and argv[-2:] == ["--recipe", "fake"]
    assert (folder / "gpu_session.toml").is_file() and not (folder / "project.toml").exists()


def test_the_tool_list_is_passed_only_when_the_plan_names_one(gpu_project: Path, tmp_path: Path) -> None:
    default = plan.load_plan(gpu_project)
    wheel = make_wheel(tmp_path)
    argv = machine.machine_plan(default, wheel, 0.0, "2026-01-01T00:00:00+00:00", 1, None)["tools_argv"]
    assert isinstance(argv, list) and "--tools" not in argv  # the server's own default set
    none = machine.machine_plan(replace(default, tools=()), wheel, 0.0, "2026-01-01T00:00:00+00:00", 1, None)["tools_argv"]
    assert isinstance(none, list) and none[-2:] == ["--tools", ""]


def test_up_needs_the_judge_model_named_in_the_project(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    text = (gpu_project / "project.toml").read_text().replace(f'model = "{JUDGE_MODEL}"', 'model = ""')
    (gpu_project / "project.toml").write_text(text, encoding="utf-8")
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "judge_model_missing" and world.created == []


def test_up_does_not_pass_a_path_as_recipe(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    for bad in ("recipes/mine.toml", "../x", "a b", "--help", "mine.toml", "Upper", "a-b"):
        with pytest.raises(ProvisionError) as caught:
            run_up(ctx, recipe=bad)
        assert caught.value.code == "recipe_invalid"
    assert world.created == []


# -- the guard must arm, or the machine goes -----------------------------------------------------------------


@pytest.mark.parametrize(("armed", "code"), [(False, "guard_not_armed"), (None, "guard_not_reported")])
def test_a_machine_whose_guard_did_not_arm_is_deleted_and_not_kept(
    gpu_project: Path, tmp_path: Path, clock: Clock, armed: bool | None, code: str
) -> None:
    world = FakeWorld(armed=armed)
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == code
    assert world.deleted == ["pod12345"] and not world.machines
    assert not world.wheel_received  # nothing was installed on an unguarded machine
    assert not (gpu_project / "gpu_session.toml").exists()
    assert not list((tmp_path / "xdg_config" / userfiles.APP_FOLDER / "keys").glob("*.key"))
    found = sessions.load(tmp_path / "xdg_state" / userfiles.APP_FOLDER)
    assert found[0].state == "ended (startup-failure)" and found[0].failure == code


def test_a_machine_that_never_answers_is_deleted_at_the_startup_timeout(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock
) -> None:
    world.not_ready_polls = 10**9
    ctx = make_context(tmp_path, gpu_project, world, clock, startup_timeout=120.0)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "startup_timeout" and world.deleted == ["pod12345"]


@pytest.mark.parametrize("which", ["tools_state", "judge_state"])
def test_a_failed_service_deletes_the_machine_and_says_why(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock, which: str
) -> None:
    setattr(world, which, "failed")
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "startup_failed" and world.deleted == ["pod12345"]
    assert not (gpu_project / "gpu_session.toml").exists()


def test_endpoints_that_answer_without_a_key_fail_the_start(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    world.open_endpoints = True
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "endpoint_unverified" and world.deleted == ["pod12345"]


def test_ctrl_c_during_startup_deletes_the_machine(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    real_sleep = ctx.sleep
    calls = {"n": 0}

    def interrupting(seconds: float) -> None:
        calls["n"] += 1
        if calls["n"] == 2:
            raise KeyboardInterrupt
        real_sleep(seconds)

    ctx.sleep = interrupting
    with pytest.raises(KeyboardInterrupt):
        run_up(ctx)
    assert world.deleted == ["pod12345"]
    assert sessions.load(tmp_path / "xdg_state" / userfiles.APP_FOLDER)[0].state == "ended (interrupted)"


def test_exit_code_130_after_an_interrupted_up(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    real_sleep = ctx.sleep

    def interrupting(seconds: float) -> None:
        if world.created:
            raise KeyboardInterrupt
        real_sleep(seconds)

    ctx.sleep = interrupting
    assert gpu_command(namespace(gpu_project, "up", limit="3h", yes=True), ctx) == 130
    assert world.deleted == ["pod12345"]


def test_a_failed_delete_says_the_machine_may_still_bill(gpu_project: Path, tmp_path: Path, clock: Clock) -> None:
    world = FakeWorld(armed=False)
    world.delete_failures = 99
    ctx = make_context(tmp_path, gpu_project, world, clock)
    with pytest.raises(ProvisionError) as caught:
        run_up(ctx)
    assert caught.value.code == "machine_delete_failed"
    assert "may still be billing" in caught.value.hint and "pod12345" in caught.value.hint


def test_a_wheel_build_failure_costs_nothing(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    def broken() -> tuple[Wheel, None]:
        raise ProvisionError("wheel_build_failed", "uv build failed")

    ctx = make_context(tmp_path, gpu_project, world, clock, build_wheel=broken)
    with pytest.raises(ProvisionError):
        run_up(ctx)
    assert world.created == []


# -- down, ls, price -------------------------------------------------------------------------------------------


def test_down_deletes_the_machine_the_session_file_and_the_key(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock, capsys: pytest.CaptureFixture[str]
) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    clock.sleep(5400)
    capsys.readouterr()
    assert gpu_command(namespace(gpu_project, "down"), ctx) == 0
    assert world.deleted == ["pod12345"] and not world.machines
    assert not (gpu_project / "gpu_session.toml").exists()
    assert not list((tmp_path / "xdg_config" / userfiles.APP_FOLDER / "keys").glob("*.key"))
    ended = sessions.load(tmp_path / "xdg_state" / userfiles.APP_FOLDER)[0]
    assert ended.state == "ended (down)"
    assert "1.50 h" in capsys.readouterr().out
    assert config.load(gpu_project).tools_endpoint == ""  # the project is back to its own configuration


def test_down_with_nothing_live_is_an_error(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    assert gpu_command(namespace(gpu_project, "down"), ctx) == 1


def test_down_leaves_a_session_file_it_did_not_write(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    (gpu_project / "gpu_session.toml").write_text("[tools]\nendpoint = 'http://other'\n", encoding="utf-8")
    lifecycle.down(ctx)
    assert (gpu_project / "gpu_session.toml").read_text().startswith("[tools]")


def test_down_when_the_machine_is_already_gone_still_closes_the_session(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock
) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    world.machines.clear()  # the guard deleted it
    lifecycle.down(ctx)
    assert sessions.load(tmp_path / "xdg_state" / userfiles.APP_FOLDER)[0].live is False
    assert world.deleted == []


def test_down_refuses_a_machine_whose_name_is_not_the_sessions(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    world.machines["pod12345"] = Machine("pod12345", "someone-elses", RUNNING, 1.0, "EU-1")
    with pytest.raises(ProvisionError) as caught:
        lifecycle.down(ctx)
    assert caught.value.code == "machine_mismatch" and world.deleted == []


def test_ls_lists_sessions_with_hours_cost_and_deadline(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock, capsys: pytest.CaptureFixture[str]
) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    clock.sleep(3600 * 2)
    capsys.readouterr()
    assert gpu_command(namespace(gpu_project, "ls"), ctx) == 0
    header, row = capsys.readouterr().out.splitlines()[:2]
    assert header.split("\t")[-3:] == ["hours", "est_cost", "deadline"]
    columns = row.split("\t")
    assert columns[1] == "ready" and float(columns[5]) >= 2.0
    assert float(columns[6]) == pytest.approx(float(columns[5]) * 1.89, abs=0.02)
    assert columns[-1] == (START + timedelta(hours=3)).isoformat()


def test_ls_closes_a_session_whose_machine_the_guard_deleted(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    world.machines.clear()
    clock.sleep(3600 * 10)  # long after the deadline
    listing = lifecycle.ls(ctx)
    session = listing.sessions[0]
    assert session.end_reason == "machine-gone"
    assert session.ended_at == START + timedelta(hours=3, seconds=machine.GRACE_SECONDS)  # billed no later than that
    assert session.cost(clock.now()) <= round(3.01 * 1.89, 2)


def test_ls_warns_about_a_machine_alive_past_its_deadline_and_about_unknown_ones(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock
) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    world.machines["other999"] = Machine("other999", "unstage-feedbeef", RUNNING, 2.0, "EU-1")
    clock.sleep(3600 * 4)
    warnings = lifecycle.ls(ctx).warnings
    assert any("guard failed" in w for w in warnings) and any("other999" in w and "not in the session log" in w for w in warnings)


def test_ls_without_a_readable_key_still_lists_from_the_log(gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    run_up(ctx)
    (tmp_path / "xdg_config" / userfiles.APP_FOLDER / "runpod.key").unlink()
    listing = lifecycle.ls(ctx)
    assert len(listing.sessions) == 1 and listing.warnings and "local log only" in listing.warnings[0]


def test_price_lists_gpu_types_by_price(
    gpu_project: Path, tmp_path: Path, world: FakeWorld, clock: Clock, capsys: pytest.CaptureFixture[str]
) -> None:
    ctx = make_context(tmp_path, gpu_project, world, clock)
    assert gpu_command(namespace(gpu_project, "price"), ctx) == 0
    lines = capsys.readouterr().out.splitlines()
    assert lines[0].split("\t")[:3] == ["gpu", "memory_gb", "price_per_hour"]
    assert [line.split("\t")[2] for line in lines[1:]] == ["1.39", "1.89", "2.99"]
    assert gpu_command(namespace(gpu_project, "price", gpu="H100"), ctx) == 0
    assert capsys.readouterr().out.count("\n") == 2


def test_the_session_log_survives_a_torn_line(tmp_path: Path) -> None:
    folder = tmp_path / "state"
    sessions.append(folder, "requested", "a1", START, project="p", provider="runpod", machine_name="unstage-a1", gpu="g")
    with (folder / sessions.LOG_NAME).open("a") as handle:
        handle.write('{"ts": "2026-10-21T12:00:00+00:00", "event": "cre')
    assert [s.id for s in sessions.load(folder)] == ["a1"]
    assert stat.S_IMODE((folder / sessions.LOG_NAME).stat().st_mode) == 0o600


# -- keys and user files --------------------------------------------------------------------------------------


def test_provider_key_from_a_file_needs_mode_600(tmp_path: Path) -> None:
    path = write_api_key(tmp_path, mode=0o644)
    source = userfiles.key_source(path.parent, "runpod", "runpod.key")
    with pytest.raises(ProvisionError) as caught:
        userfiles.read_key(source, "runpod API key")
    assert caught.value.code == "key_unsafe"
    path.chmod(0o600)
    assert userfiles.read_key(source, "runpod API key") == "rpa_secret_api_key_value"


def test_provider_key_missing_names_the_file_not_the_value(tmp_path: Path) -> None:
    with pytest.raises(ProvisionError) as caught:
        userfiles.read_key(userfiles.KeySource(key_file=str(tmp_path / "none.key")), "runpod API key")
    assert caught.value.code == "key_missing"


def test_provider_key_from_a_command_runs_without_a_shell(tmp_path: Path) -> None:
    folder = tmp_path / "cfg"
    folder.mkdir()
    (folder / userfiles.USER_CONFIG_NAME).write_text(
        f'[runpod]\nkey_command = [{json.dumps(sys.executable)}, "-c", "print(\'from-command\')"]\n', encoding="utf-8")
    source = userfiles.key_source(folder, "runpod", "runpod.key")
    assert source.key_command and not source.key_file
    assert userfiles.read_key(source, "runpod API key") == "from-command"
    # a shell string would not be a list of arguments
    (folder / userfiles.USER_CONFIG_NAME).write_text('[runpod]\nkey_command = "echo $HOME"\n', encoding="utf-8")
    with pytest.raises(ProvisionError):
        userfiles.key_source(folder, "runpod", "runpod.key")


def test_a_key_value_in_the_user_config_is_refused(tmp_path: Path) -> None:
    (tmp_path / userfiles.USER_CONFIG_NAME).write_text('[runpod]\nkey = "abc"\n', encoding="utf-8")
    with pytest.raises(ProvisionError) as caught:
        userfiles.key_source(tmp_path, "runpod", "runpod.key")
    assert caught.value.code == "user_config_invalid"


def test_keys_are_read_by_the_projects_one_reader(tmp_path: Path) -> None:
    good = write_api_key(tmp_path)
    assert userfiles.read_key(userfiles.KeySource(key_file=str(good)), "x") == config.Secret(key_file=str(good)).read()
    good.chmod(0o640)
    with pytest.raises(config.SecretError) as theirs:
        config.Secret(key_file=str(good)).read()
    with pytest.raises(ProvisionError) as ours:
        userfiles.read_key(userfiles.KeySource(key_file=str(good)), "x")
    assert ours.value.code == theirs.value.code == "key_unsafe"


def test_each_session_gets_its_own_key(tmp_path: Path) -> None:
    assert userfiles.new_session_key() != userfiles.new_session_key()
    first = userfiles.write_session_key(tmp_path, "abc12345", "k" * 43)
    with pytest.raises(FileExistsError):
        userfiles.write_session_key(tmp_path, "abc12345", "other")
    assert stat.S_IMODE(first.stat().st_mode) == 0o600
    assert stat.S_IMODE(first.parent.stat().st_mode) == 0o700


def test_a_rendered_session_file_is_accepted_by_config(gpu_project: Path) -> None:
    text = lifecycle.render_session_file("abc12345", "https://t.example", "https://j.example/v1", "/k/session.key", True)
    assert tomllib.loads(text)["judge"] == {"endpoint": "https://j.example/v1", "key_file": "/k/session.key"}
    (gpu_project / config.SESSION_NAME).write_text(text, encoding="utf-8")
    cfg = config.load(gpu_project)
    assert (cfg.tools_endpoint, cfg.judge.endpoint) == ("https://t.example", "https://j.example/v1")


def test_a_project_with_its_own_generator_endpoint_keeps_it(gpu_project: Path) -> None:
    text = lifecycle.render_session_file("abc12345", "https://t.example", "https://j.example/v1", "/k", generator=False)
    assert "[generator]" not in text


# -- the plan read from the project -----------------------------------------------------------------------------


def test_plan_reads_the_judge_and_the_options(gpu_project: Path) -> None:
    (gpu_project / "gpu.toml").write_text(
        '[machine]\ndisk_gb = 300\nmin_vram_gb = 48\ngpu_prefer = ["NVIDIA L40S"]\n'
        "[judge]\nquantization = \"fp8\"\nmax_model_len = 8192\nimages_per_prompt = 6\ngpu_memory_utilization = 0.5\n",
        encoding="utf-8")
    loaded = plan.load_plan(gpu_project)
    assert (loaded.disk_gb, loaded.min_vram_gb, loaded.gpu_prefer) == (300, 48, ("NVIDIA L40S",))
    assert loaded.judge is not None
    argv = plan.judge_argv(loaded.judge, 8002, shared_gpu=True)
    assert argv[:3] == ["vllm", "serve", JUDGE_MODEL]
    assert argv[argv.index("--quantization") + 1] == "fp8"
    assert argv[argv.index("--limit-mm-per-prompt") + 1] == '{"image": 6}'
    assert argv[argv.index("--gpu-memory-utilization") + 1] == "0.50"
    assert argv[argv.index("--max-num-seqs") + 1] == "16"  # the default: a few judgments at a time
    assert argv[argv.index("--host") + 1] == "127.0.0.1"  # the judge is never reachable except through the key check
    assert not any("key" in item.lower() for item in argv)  # the key never goes on a command line


@pytest.mark.parametrize(
    "text",
    [
        "[judge]\nquantization = \"fp4; rm -rf\"\n",
        "[judge]\nmax_model_len = 3\n",
        "[judge]\nimages_per_prompt = 99\n",
        "[judge]\ngpu_memory_utilization = 2.0\n",
        "[judge]\nmax_num_seqs = 0\n",
        "[machine]\nimage = \"vllm/vllm-openai\"\n",  # no version tag
        "[machine]\nmin_cuda = \"latest\"\n",
        "[machine]\ngpu_prefer = []\n",
        "[machine]\nunknown = 1\n",
        "[other]\nx = 1\n",
    ],
)
def test_plan_rejects_options_outside_the_positive_definition(gpu_project: Path, text: str) -> None:
    (gpu_project / "gpu.toml").write_text(text, encoding="utf-8")
    with pytest.raises(ProvisionError) as caught:
        plan.load_plan(gpu_project)
    assert caught.value.code == "options_invalid"


def test_override_files_layer_over_the_project_in_order_and_never_rewrite_it(gpu_project: Path, tmp_path: Path) -> None:
    from virtual_unstaging import config

    (gpu_project / "gpu.toml").write_text("[judge]\nmax_model_len = 8192\ngpu_memory_utilization = 0.55\n", encoding="utf-8")
    before = {name: (gpu_project / name).read_bytes() for name in ("project.toml", "gpu.toml")}
    small, faster = tmp_path / "small_judge.toml", tmp_path / "faster.toml"
    small.write_text('[judge]\nmodel = "org/small"\nrevision = "' + "c" * 40 + '"\n[gpu.judge]\ngpu_memory_utilization = 0.3\n'
                     '[generator]\nsettings = {output_side = 768, condition_side = 768}\n', encoding="utf-8")
    faster.write_text('[gpu.judge]\ngpu_memory_utilization = 0.25\n[generator.settings]\noutput_side = 512\n'
                      '[judge]\nimage_side = 768\nimage_format = "jpeg"\nmax_findings = 4\ncomment_chars = 60\n', encoding="utf-8")
    loaded = plan.load_plan(gpu_project, (small, faster))
    assert loaded.judge is not None and loaded.judge.model == "org/small" and loaded.judge.revision == "c" * 40
    assert (loaded.judge.gpu_memory_utilization, loaded.judge.max_model_len) == (0.25, 8192)  # the last file wins, key by key
    cfg = config.load(gpu_project, (small, faster))
    assert cfg.generator.settings == {"output_side": 512, "condition_side": 768}  # tables merge key by key
    assert cfg.judge.request.revision_suffix() == "+jpeg@768+answer:4/4/60/0"
    assert config.load(gpu_project).judge.model == JUDGE_MODEL and plan.load_plan(gpu_project).judge.gpu_memory_utilization == 0.55  # type: ignore[union-attr]
    assert before == {name: (gpu_project / name).read_bytes() for name in before}


@pytest.mark.parametrize("text", [
    '[judge]\nendpoint = "https://elsewhere.example/v1"\n',
    '[tools]\nkey_file = "~/other.key"\n',
    '[generator]\nkey_command = ["cat", "key"]\n',
    '[gpu.judge]\nkey = "secret"\n',
    '[project]\nname = "other"\n',
    "[gpu]\nx = 1\n",
    "[other]\nx = 1\n",
    "not toml [",
])
def test_override_files_never_set_endpoints_keys_or_the_project(gpu_project: Path, tmp_path: Path, text: str) -> None:
    from virtual_unstaging import config

    path = tmp_path / "override.toml"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(config.ConfigError):
        config.load(gpu_project, (path,))
    with pytest.raises(ProvisionError) as caught:
        plan.load_plan(gpu_project, (path,))
    assert caught.value.code == "options_invalid"
    with pytest.raises(config.ConfigError, match="no override file"):
        config.load(gpu_project, (tmp_path / "absent.toml",))


def test_the_project_narrows_what_the_recipe_accepts(gpu_project: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from virtual_unstaging import cli, config

    class Client:
        def capabilities(self) -> dict[str, Any]:
            return {"generator": {"roles": ["original", "reference", "removal_mask", "protected_mask"], "max_images": 4,
                                  "native_mask": False, "model": "org/gen", "revision": "r", "licence": "x"}}

    monkeypatch.setattr(cli, "_toolserver", lambda cfg: Client())
    assert cli._generator(config.load(gpu_project)).capabilities.max_images == 4  # the default narrows nothing
    xfast = tmp_path / "xfast.toml"
    xfast.write_text('[generator]\nmax_images = 2\nroles = ["original", "removal_mask", "depth"]\n', encoding="utf-8")
    narrowed = cli._generator(config.load(gpu_project, (xfast,))).capabilities
    assert narrowed.max_images == 2 and narrowed.roles == frozenset({"original", "removal_mask"})  # never widened


@pytest.mark.parametrize("line", ["image_side = 100", 'image_format = "webp"', "max_findings = 13", "max_findings = 0",
                                  "max_moves = 5", "comment_chars = 5", "critique_chars = 900", "image_side = true"])
def test_judge_speed_options_are_checked(gpu_project: Path, tmp_path: Path, line: str) -> None:
    from virtual_unstaging import config

    path = tmp_path / "override.toml"
    path.write_text(f"[judge]\n{line}\n", encoding="utf-8")
    with pytest.raises(config.ConfigError):
        config.load(gpu_project, (path,))


@pytest.mark.parametrize("model", ["--help", "a b/c", "org/model; id", "../x", "no-slash", "org/-x"])
def test_plan_rejects_a_judge_model_that_is_not_a_repository_id(gpu_project: Path, model: str) -> None:
    text = (gpu_project / "project.toml").read_text().replace(f'model = "{JUDGE_MODEL}"', f'model = "{model}"')
    (gpu_project / "project.toml").write_text(text, encoding="utf-8")
    with pytest.raises(ProvisionError):
        plan.load_plan(gpu_project)


# -- the Runpod provider, against recorded-shape answers ---------------------------------------------------------


class RecordingTransport:
    def __init__(self, *replies: Response) -> None:
        self.replies = list(replies)
        self.calls: list[tuple[str, str, dict[str, str], bytes | None]] = []

    def __call__(self, method: str, url: str, headers: dict[str, str], body: bytes | None, timeout: float) -> Response:
        self.calls.append((method, url, headers, body))
        return self.replies.pop(0) if len(self.replies) > 1 else self.replies[0]


def answer(status: int, payload: object = None) -> Response:
    return Response(status, b"" if payload is None else json.dumps(payload).encode())


def runpod(transport: RecordingTransport) -> RunpodProvider:
    return RunpodProvider("rpa_secret_api_key_value", transport, sleep=lambda s: None)


def spec(**overrides: Any) -> MachineSpec:
    values: dict[str, Any] = {
        "name": "unstage-abc12345", "gpu_id": "NVIDIA H100 80GB HBM3", "gpu_count": 2, "datacenter": "US-B", "image": "vllm/vllm-openai:v1",
        "disk_gb": 200, "ports": (8000, 8001), "env": {"UNSTAGE_SESSION_KEY": "session-key-value-1234567890"},
        "entrypoint": ("python3", "-c", "pass"), "min_cuda": "13.0",
    }
    values.update(overrides)
    return MachineSpec(**values)


def test_runpod_offers_come_from_the_v2_catalog() -> None:
    catalog = {"gpus": [
        {"id": "NVIDIA H100 80GB HBM3", "name": "H100", "memory": 80, "secure": True, "community": True,
         "price": {"secure": 2.99, "community": 2.0}, "availability": "MEDIUM",
         "dataCenters": [{"id": "US-B", "name": "B", "availability": "HIGH"}, {"id": "US-A", "name": "A", "availability": "NONE"}]},
        {"id": "NVIDIA only community", "name": "x", "memory": 24, "secure": False, "community": True, "price": {"community": 0.3}},
    ]}
    transport = RecordingTransport(answer(200, catalog))
    offers = runpod(transport).offers("13.0")
    assert [o.gpu_id for o in offers] == ["NVIDIA H100 80GB HBM3"]
    assert offers[0].price_per_hour == 2.99 and offers[0].datacenters == (("US-B", "HIGH"), ("US-A", "NONE"))
    method, url, headers, _ = transport.calls[0]
    assert method == "GET" and url.startswith("https://api.runpod.io/v2/catalog/gpus?")
    query = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
    assert query == {"include": ["AVAILABILITY"], "product": ["POD"], "cloud": ["SECURE"], "minCudaVersion": ["13.0"]}
    assert headers["Authorization"] == "Bearer rpa_secret_api_key_value"


def test_runpod_create_body_follows_the_v2_schema() -> None:
    pod = {"id": "abcd1234", "name": "unstage-abc12345", "status": "PROVISIONING", "cost": 5.98, "dataCenterId": "US-B"}
    transport = RecordingTransport(answer(201, pod))
    made = runpod(transport).create(spec())
    assert (made.id, made.status, made.price_per_hour, made.datacenter) == ("abcd1234", "starting", 5.98, "US-B")
    method, url, _, body = transport.calls[0]
    assert (method, url) == ("POST", "https://api.runpod.io/v2/pods")
    sent = json.loads(body or b"")
    assert sent["cloud"] == "SECURE" and sent["gpu"] == {"id": "NVIDIA H100 80GB HBM3", "count": 2, "minCudaVersion": "13.0"}
    assert sent["dataCenterIds"] == ["US-B"] and sent["ports"] == ["8000/http", "8001/http"]
    assert sent["entrypoint"] == ["python3", "-c", "pass"] and sent["disk"] == 200 and sent["image"] == "vllm/vllm-openai:v1"
    assert sent["env"] == {"UNSTAGE_SESSION_KEY": "session-key-value-1234567890"}
    assert set(sent) == {"name", "image", "cloud", "gpu", "dataCenterIds", "entrypoint", "disk", "ports", "env"}


def test_runpod_400_on_create_means_try_the_next_candidate_and_hides_the_env() -> None:
    reply = answer(400, {"title": "Bad Request", "status": 400, "detail": "no capacity",
                         "errors": ["env: session-key-value-1234567890 is odd"]})
    with pytest.raises(ProvisionError) as caught:
        runpod(RecordingTransport(reply)).create(spec())
    assert caught.value.code == "provider_refused"
    assert "session-key-value-1234567890" not in str(caught.value) and "[hidden]" in str(caught.value)


@pytest.mark.parametrize(("status", "code"), [(401, "provider_auth"), (403, "provider_auth"), (402, "provider_balance"), (422, "provider_error")])
def test_runpod_error_statuses_map_to_stable_codes(status: int, code: str) -> None:
    with pytest.raises(ProvisionError) as caught:
        runpod(RecordingTransport(answer(status, {"title": "t", "status": status, "detail": "d"}))).create(spec())
    assert caught.value.code == code


def test_runpod_never_retries_a_post_after_a_5xx_but_retries_a_get() -> None:
    post = RecordingTransport(answer(503, {"title": "x", "status": 503, "detail": "y"}))
    with pytest.raises(ProvisionError):
        runpod(post).create(spec())
    assert len(post.calls) == 1
    get = RecordingTransport(answer(503), answer(503), answer(200, {"id": "abcd1234", "name": "n", "status": "RUNNING", "cost": 1.0}))
    assert runpod(get).get("abcd1234") is not None and len(get.calls) == 3


def test_runpod_retries_a_429_even_for_a_post() -> None:
    transport = RecordingTransport(answer(429), answer(201, {"id": "abcd1234", "name": "n", "status": "RUNNING", "cost": 1.0}))
    assert runpod(transport).create(spec()).id == "abcd1234" and len(transport.calls) == 2


def test_runpod_get_maps_status_and_404_is_none() -> None:
    assert runpod(RecordingTransport(answer(404, {"title": "Not Found", "status": 404, "detail": "x"}))).get("abcd1234") is None
    for status, expected in (("RUNNING", "running"), ("EXITED", "stopped"), ("ERROR", "failed"), ("TERMINATED", GONE)):
        reply = answer(200, {"id": "abcd1234", "name": "n", "status": status, "cost": 0.0})
        found = runpod(RecordingTransport(reply)).get("abcd1234")
        assert found is not None and found.status == expected


def test_runpod_delete_is_idempotent_and_checks_the_id() -> None:
    transport = RecordingTransport(Response(204, b""))
    runpod(transport).delete("abcd1234")
    assert transport.calls[0][:2] == ("DELETE", "https://api.runpod.io/v2/pods/abcd1234")
    runpod(RecordingTransport(answer(404, {"title": "Not Found", "status": 404, "detail": "x"}))).delete("abcd1234")
    for bad in ("../account", "a b", "x"):
        with pytest.raises(ProvisionError):
            runpod(RecordingTransport(Response(204, b""))).delete(bad)


def test_runpod_lists_all_pages_and_finds_by_exact_name() -> None:
    page1 = {"pods": [{"id": "pod00001", "name": "unstage-aaaaaaaa", "status": "RUNNING", "cost": 1}],
             "pagination": {"nextCursor": "next"}}
    page2 = {"pods": [{"id": "pod00002", "name": "unstage-bbbbbbbb", "status": "RUNNING", "cost": 1},
                      {"id": "pod00003", "name": "unstage-cccccccc", "status": "TERMINATED", "cost": 0},
                      {"id": "pod00004", "name": "other", "status": "RUNNING", "cost": 1}], "pagination": {}}
    transport = RecordingTransport(answer(200, page1), answer(200, page2))
    assert [m.id for m in runpod(transport).list_machines("unstage-")] == ["pod00001", "pod00002"]
    assert "cursor=next" in transport.calls[1][1]
    again = RecordingTransport(answer(200, page1), answer(200, page2))
    found = runpod(again).find("unstage-bbbbbbbb")
    assert found is not None and found.id == "pod00002"


def test_runpod_urls_are_the_https_proxy() -> None:
    assert runpod(RecordingTransport(answer(200))).url("abcd1234", 8001) == "https://abcd1234-8001.proxy.runpod.net"


def test_a_provider_can_be_plugged_in_through_the_table() -> None:
    from virtual_unstaging.provision import providers

    assert providers.provider_names() == ["runpod"]
    with pytest.raises(ProvisionError) as caught:
        providers.make_provider("other", "k", lambda *a: Response(200, b""))
    assert caught.value.code == "provider_unknown" and caught.value.exit_code == 2


def test_the_default_transport_refuses_plain_http() -> None:
    from virtual_unstaging.provision.transport import urllib_transport

    with pytest.raises(ProvisionError) as caught:
        urllib_transport("GET", "http://example.org/x", {}, None, 1.0)
    assert caught.value.code == "insecure_url"


# -- the wheel --------------------------------------------------------------------------------------------------


def test_build_wheel_runs_uv_without_a_shell_and_hashes_the_result(tmp_path: Path) -> None:
    out = tmp_path / "out"
    out.mkdir()
    seen: list[Any] = []

    def runner(argv: list[str], **kwargs: Any) -> Any:
        seen.append((argv, kwargs))
        (out / "virtual_unstaging-0.1.0-py3-none-any.whl").write_bytes(b"wheel")
        return argparse.Namespace(returncode=0, stderr="")

    built = build_wheel(tmp_path, out, runner)
    assert seen[0][0][:3] == ["uv", "build", "--wheel"] and "shell" not in seen[0][1]
    assert built.sha256 == hashlib.sha256(b"wheel").hexdigest() and built.size == 5


def test_build_wheel_failures_are_stable_errors(tmp_path: Path) -> None:
    with pytest.raises(ProvisionError) as caught:
        build_wheel(tmp_path, tmp_path, lambda argv, **kw: argparse.Namespace(returncode=1, stderr="boom"))
    assert caught.value.code == "wheel_build_failed"

    def missing(argv: list[str], **kwargs: Any) -> Any:
        raise FileNotFoundError("uv")

    with pytest.raises(ProvisionError) as caught:
        build_wheel(tmp_path, tmp_path, missing)
    assert caught.value.code == "wheel_build_failed"
    with pytest.raises(ProvisionError):  # no wheel produced
        build_wheel(tmp_path, tmp_path, lambda argv, **kw: argparse.Namespace(returncode=0, stderr=""))


def test_the_source_root_of_this_checkout_is_found() -> None:
    from virtual_unstaging.provision.wheel import source_root

    assert (source_root() / "pyproject.toml").is_file()


# -- the machine side: the guard and the bootstrap --------------------------------------------------------------


def load_bootstrap() -> Any:
    spec_ = importlib.util.spec_from_file_location("unstage_bootstrap_under_test", PROVISION_DIR / "bootstrap.py")
    assert spec_ and spec_.loader
    module = importlib.util.module_from_spec(spec_)
    sys.modules["unstage_bootstrap_under_test"] = module
    spec_.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def boot() -> Any:
    return load_bootstrap()


class FakeGuard:
    def __init__(self, boot: Any, *, probe: str | None = "rest-v2", terminate: bool = True, stop: bool = True) -> None:
        self.base = boot.SelfDelete
        self.probe_value, self.terminate_ok, self.stop_ok = probe, terminate, stop
        self.calls: list[str] = []

    def probe(self) -> str | None:
        self.calls.append("probe")
        return self.probe_value

    def terminate(self) -> bool:
        self.calls.append("terminate")
        return self.terminate_ok

    def stop(self) -> bool:
        self.calls.append("stop")
        return self.stop_ok


class FakeProcess:
    def __init__(self, exits_after: float | None = None, clock: Clock | None = None) -> None:
        self.exits_after, self.clock, self.returncode = exits_after, clock, None
        self.terminated = False

    def poll(self) -> int | None:
        if self.exits_after is not None and self.clock is not None and self.clock.mono >= self.exits_after:
            self.returncode = 1
            return 1
        return None

    def terminate(self) -> None:
        self.terminated = True


KEY = "a-real-looking-session-key-0123456789"


def supervisor(boot: Any, plan_: dict[str, Any], guard: FakeGuard, clock: Clock, env: dict[str, str] | None = None, **kwargs: Any) -> Any:
    exits: list[int] = []
    defaults: dict[str, Any] = {
        "now": lambda: START.timestamp() + clock.mono, "sleep": clock.sleep, "exit_process": exits.append,
        "serve_front": False, "forever": False, "ready": lambda url, key: True,
    }
    defaults.update(kwargs)
    sup = boot.Supervisor(plan_, {"UNSTAGE_SESSION_KEY": KEY} if env is None else env, guard, **defaults)
    sup.exits = exits
    sup.stop_at = START.timestamp() + 7200  # `run` sets it from the plan; direct calls need one
    return sup


def base_plan(**overrides: Any) -> dict[str, Any]:
    values: dict[str, Any] = {
        "deadline": START.timestamp() + 3600, "grace_seconds": 30, "child_exit_grace_seconds": 600, "key_env": "UNSTAGE_SESSION_KEY",
        "front_port": 0, "tools_port": 8000, "judge_port": 8002, "judge_argv": None, "judge_gpu": None,
        "tools_argv": ["serve", "--port", "8000"], "tools_gpu": None,
        "wheel": {"filename": "virtual_unstaging-0.1.0-py3-none-any.whl", "sha256": "0" * 64, "max_bytes": 1000},
        "install_dir": "/nonexistent",
    }
    values.update(overrides)
    return values


def test_guard_deletes_the_machine_at_the_deadline_plus_grace(boot: Any, clock: Clock) -> None:
    guard = FakeGuard(boot)
    sup = supervisor(boot, base_plan(), guard, clock)
    assert sup.run() == "deadline"
    assert clock.mono >= 3600 + 30 and clock.mono < 3600 + 30 + 10
    assert guard.calls == ["probe", "terminate"] and sup.exits == []


def test_guard_that_cannot_terminate_stops_the_machine(boot: Any, clock: Clock) -> None:
    guard = FakeGuard(boot, terminate=False)
    supervisor(boot, base_plan(deadline=START.timestamp() + 60), guard, clock).run()
    assert guard.calls[-2:] == ["terminate", "stop"]


def test_guard_that_can_do_nothing_exits_the_process_so_the_container_stops(boot: Any, clock: Clock) -> None:
    guard = FakeGuard(boot, terminate=False, stop=False)
    sup = supervisor(boot, base_plan(deadline=START.timestamp() + 60), guard, clock)
    sup.run()
    assert sup.exits == [0] and guard.calls.count("terminate") == boot.RELEASE_ROUNDS


def test_a_guard_that_raises_is_treated_as_a_refusal(boot: Any, clock: Clock) -> None:
    class Raising(FakeGuard):
        def terminate(self) -> bool:
            raise RuntimeError("bug")

    guard = Raising(boot)
    supervisor(boot, base_plan(deadline=START.timestamp() + 60), guard, clock).run()
    assert "stop" in guard.calls


def test_an_unarmed_guard_starts_nothing_and_still_ends_the_machine(boot: Any, clock: Clock) -> None:
    started: list[Any] = []
    guard = FakeGuard(boot, probe=None)
    sup = supervisor(boot, base_plan(judge_argv=["vllm", "serve", "m"]), guard, clock, popen=lambda *a, **k: started.append(a))
    assert sup.run() == "guard not armed"
    assert started == [] and sup.status.get("guard", "armed") is False
    assert clock.mono >= boot.UNARMED_WAIT_SECONDS


@pytest.mark.parametrize("plan_", [{}, {"key_env": "UNSTAGE_SESSION_KEY"}])
def test_no_deadline_in_the_plan_ends_the_machine_at_once(boot: Any, clock: Clock, plan_: dict[str, Any]) -> None:
    guard = FakeGuard(boot)
    sup = supervisor(boot, plan_, guard, clock)
    assert sup.run() == "no deadline in the plan" and "terminate" in guard.calls and clock.mono == 0


@pytest.mark.parametrize("value", ["", "{{ RUNPOD_SECRET_x }}", "short", "has space in it 0123456789abcdef"])
def test_an_unusable_key_ends_the_machine_before_anything_starts(boot: Any, clock: Clock, value: str) -> None:
    started: list[Any] = []
    guard = FakeGuard(boot)
    sup = supervisor(boot, base_plan(judge_argv=["vllm"]), guard, clock, env={"UNSTAGE_SESSION_KEY": value},
                     popen=lambda *a, **k: started.append(a))
    assert sup.run() == "no usable session key" and started == []


def test_a_deadline_already_passed_at_start_ends_the_machine_even_after_a_container_restart(boot: Any, clock: Clock) -> None:
    started: list[Any] = []
    guard = FakeGuard(boot)
    sup = supervisor(boot, base_plan(deadline=START.timestamp() - 500, judge_argv=["vllm"]), guard, clock,
                     popen=lambda *a, **k: started.append(a))
    assert sup.run() == "deadline already passed at start" and started == []


def test_an_error_inside_the_supervisor_fails_closed(boot: Any, clock: Clock) -> None:
    guard = FakeGuard(boot)
    sup = supervisor(boot, base_plan(judge_argv=["vllm"]), guard, clock, popen=lambda *a, **k: 1 / 0)
    assert sup.run().startswith("supervisor error") and "terminate" in guard.calls


def test_the_judge_is_started_with_the_key_in_its_environment_only(boot: Any, clock: Clock) -> None:
    seen: list[tuple[list[str], dict[str, str]]] = []

    def popen(argv: list[str], env: dict[str, str]) -> FakeProcess:
        seen.append((argv, env))
        return FakeProcess()

    judge = ["vllm", "serve", JUDGE_MODEL, "--port", "8002"]
    sup = supervisor(boot, base_plan(judge_argv=judge, judge_gpu="1"), FakeGuard(boot), clock, popen=popen)
    sup.run()
    argv, env = seen[0]
    assert argv == judge and KEY not in " ".join(argv)
    assert env["VLLM_API_KEY"] == KEY and env["CUDA_VISIBLE_DEVICES"] == "1"


def test_a_service_that_dies_and_stays_down_ends_the_machine_early(boot: Any, clock: Clock) -> None:
    process = FakeProcess(exits_after=100.0, clock=clock)
    sup = supervisor(boot, base_plan(deadline=START.timestamp() + 7200, judge_argv=["vllm"]), FakeGuard(boot), clock,
                     popen=lambda *a, **k: process)
    assert sup.run() == "a service exited and stayed down"
    assert 700 <= clock.mono < 720 and process.terminated  # 100 s up, then the 600 s grace


def test_a_dead_service_is_reported_with_the_end_of_its_output(boot: Any, clock: Clock, tmp_path: Path) -> None:
    def popen(argv: list[str], env: dict[str, str], stdout: Any = None, stderr: Any = None) -> FakeProcess:
        stdout.write(("\x1b[1mINFO\x1b[0m loading weights\n" * 400).encode())
        stdout.write(f"(EngineCore pid=9) ValueError: no memory left for the KV cache (key {KEY})\n".encode())
        stdout.write(('(APIServer pid=7)   File "core_client.py", line 990, in __init__\n' * 40).encode())
        stdout.write(b"(APIServer pid=7) RuntimeError: Engine core initialization failed. See root cause above.\n")
        return FakeProcess(exits_after=100.0, clock=clock)

    plan_ = base_plan(deadline=START.timestamp() + 7200, judge_argv=["vllm"], log_dir=str(tmp_path / "logs"))
    sup = supervisor(boot, plan_, FakeGuard(boot), clock, popen=popen)
    assert sup.run() == "a service exited and stayed down"
    detail = sup.status.get("judge", "detail")
    assert detail.startswith("exited with 1; last output: errors: (EngineCore pid=9) ValueError: no memory left")
    assert "for the KV cache (key <session key>) | (APIServer pid=7) RuntimeError: Engine core" in detail
    assert detail.endswith("Engine core initialization failed. See root cause above.")
    assert KEY not in detail and "\x1b" not in detail and "INFO" not in detail and len(detail) < 1600
    assert (tmp_path / "logs" / "judge.log").is_file()


def test_install_runs_argument_lists_and_then_starts_the_tool_server(boot: Any, clock: Clock) -> None:
    steps: list[list[str]] = []
    started: list[list[str]] = []

    def run(argv: list[str], **kwargs: Any) -> Any:
        steps.append(argv)
        return argparse.Namespace(returncode=0, stdout="")

    def popen(argv: list[str], env: dict[str, str]) -> FakeProcess:
        started.append(argv)
        return FakeProcess()

    sup = supervisor(boot, base_plan(install_dir="/opt/x", tools_gpu="0"), FakeGuard(boot), clock, popen=popen, run=run)
    sup._install_and_serve("/opt/x/wheels/virtual_unstaging-0.1.0-py3-none-any.whl")
    assert sup.status.get("tools", "state") == "ready"
    assert all(isinstance(part, str) for argv in steps for part in argv)
    assert steps[-1][-1] == "/opt/x/wheels/virtual_unstaging-0.1.0-py3-none-any.whl[serve]"
    assert started == [["/opt/x/venv/bin/unstage", "serve", "--port", "8000"]]


def test_the_tool_server_starts_only_once_the_judge_is_up(boot: Any, clock: Clock) -> None:
    started: list[tuple[float, list[str]]] = []

    def popen(argv: list[str], env: dict[str, str], **kwargs: Any) -> FakeProcess:
        started.append((clock.mono, argv))
        return FakeProcess()

    sup = supervisor(boot, base_plan(install_dir="/opt/x"), FakeGuard(boot), clock, popen=popen,
                     run=lambda argv, **k: argparse.Namespace(returncode=0, stdout=""))
    sup.status.update("judge", state="starting")
    clock_at_ready = 300.0
    real_sleep = clock.sleep

    def sleep(seconds: float) -> None:
        real_sleep(seconds)
        if clock.mono >= clock_at_ready:
            sup.status.update("judge", state="ready")

    sup.sleep = sleep
    sup._install_and_serve("/opt/x/wheels/virtual_unstaging-0.1.0-py3-none-any.whl")
    assert [argv[0] for _, argv in started] == ["/opt/x/venv/bin/unstage"] and started[0][0] >= clock_at_ready


def test_install_failure_is_reported_with_the_tail_of_the_output(boot: Any, clock: Clock) -> None:
    sup = supervisor(boot, base_plan(), FakeGuard(boot), clock, run=lambda argv, **k: argparse.Namespace(returncode=1, stdout="a\nb\nno space left"))
    sup._install_and_serve("/x/w.whl")
    assert sup.status.get("tools", "state") == "failed" and "no space left" in sup.status.get("tools", "detail")


def test_install_commands_prefer_uv_and_share_the_images_packages(boot: Any) -> None:
    with_uv = boot.install_commands("/v", "/w.whl", "/usr/bin/python3", True)
    assert with_uv[0][:3] == ["uv", "venv", "--system-site-packages"]
    without = boot.install_commands("/v", "/w.whl", "/usr/bin/python3", False)
    assert without[0] == ["/usr/bin/python3", "-m", "venv", "--system-site-packages", "/v"]


def test_the_assembled_script_compiles_and_the_runpod_guard_climbs_its_ladder() -> None:
    source = machine.bootstrap_source(FakeWorld())
    compile(source, "<bootstrap>", "exec")
    assert source.rstrip().endswith("main(RunpodSelfDelete)")
    namespace_: dict[str, Any] = {"__name__": "assembled"}
    exec(source.rsplit("\nmain(", 1)[0], namespace_)  # defines everything, calls nothing
    calls: list[tuple[str, str, Any]] = []
    statuses = iter([409, 500, 200])  # terminate refused, delete failed, graphql ok

    def fake_call(method: str, url: str, key: str, body: Any = None, key_in_query: bool = False, graphql: bool = False) -> int:
        calls.append((method, url, body))
        return next(statuses)

    guard = namespace_["RunpodSelfDelete"]({"RUNPOD_POD_ID": "abc12345", "RUNPOD_API_KEY": "pod-scoped-key"})
    guard.call = fake_call
    assert guard.terminate() is True
    assert calls[0] == ("POST", "https://api.runpod.io/v2/pods/abc12345/action", {"action": "terminate"})
    assert calls[1][:2] == ("DELETE", "https://api.runpod.io/v2/pods/abc12345")
    assert calls[2][1] == "https://api.runpod.io/graphql" and "podTerminate" in calls[2][2]["query"]


def test_the_runpod_guard_probes_with_a_read_and_refuses_a_hostile_pod_id() -> None:
    namespace_: dict[str, Any] = {"__name__": "assembled"}
    exec(machine.bootstrap_source(FakeWorld()).rsplit("\nmain(", 1)[0], namespace_)
    seen: list[str] = []

    def fake_call(method: str, url: str, key: str, body: Any = None, **kwargs: Any) -> int:
        seen.append(f"{method} {url}")
        return 200

    good = namespace_["RunpodSelfDelete"]({"RUNPOD_POD_ID": "abc12345", "RUNPOD_API_KEY": "k"})
    good.call = fake_call
    assert good.probe() == "rest-v2" and seen == ["GET https://api.runpod.io/v2/pods/abc12345"]
    for bad_id in ("", "a/../b", 'x"}) { evil', "abc 123"):
        bad = namespace_["RunpodSelfDelete"]({"RUNPOD_POD_ID": bad_id, "RUNPOD_API_KEY": "k"})
        bad.call = fake_call
        assert bad.probe() is None and bad.terminate() is False and bad.stop() is False
    assert namespace_["RunpodSelfDelete"]({"RUNPOD_POD_ID": "abc12345"}).probe() is None


# -- the bootstrap's HTTP front, on loopback --------------------------------------------------------------------


class Upstream(http.server.BaseHTTPRequestHandler):
    seen: list[tuple[str, str, bytes, str]] = []

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _answer(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        Upstream.seen.append((self.command, self.path, body, self.headers.get("Authorization", "")))
        payload = json.dumps({"echo": len(body), "path": self.path}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    do_GET = do_POST = _answer


@pytest.fixture
def front(boot: Any, clock: Clock, tmp_path: Path) -> Iterator[tuple[Any, int, int]]:
    upstream = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
    threading.Thread(target=upstream.serve_forever, daemon=True).start()
    Upstream.seen = []
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    wheel_bytes = b"wheel bytes"
    plan_ = base_plan(front_port=port, judge_port=upstream.server_address[1], judge_argv=["vllm"], install_dir=str(tmp_path / "install"),
                      wheel={"filename": "virtual_unstaging-0.1.0-py3-none-any.whl", "sha256": hashlib.sha256(wheel_bytes).hexdigest(),
                             "max_bytes": 1000})
    sup = supervisor(boot, plan_, FakeGuard(boot), clock, serve_front=True)
    sup.accepted = []
    sup.accept_wheel = sup.accepted.append
    sup.stop_at = START.timestamp() + 3600
    sup._start_front()
    try:
        yield sup, port, upstream.server_address[1]
    finally:
        sup.server.shutdown()
        sup.server.server_close()
        upstream.shutdown()
        upstream.server_close()


def call(port: int, method: str, path: str, body: bytes | None = None, key: str | None = KEY) -> tuple[int, bytes]:
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=10)
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    connection.request(method, path, body, headers)
    reply = connection.getresponse()
    data = reply.read()
    connection.close()
    return reply.status, data


def test_front_refuses_every_route_without_the_key(front: tuple[Any, int, int]) -> None:
    _, port, _ = front
    for method, path in (("GET", "/unstage/status"), ("PUT", "/unstage/wheel"), ("POST", "/v1/chat/completions"), ("GET", "/anything")):
        assert call(port, method, path, b"x" if method != "GET" else None, key=None)[0] == 401
        assert call(port, method, path, b"x" if method != "GET" else None, key="wrong-key-0123456789abcdefgh")[0] == 401


def test_front_status_reports_the_guard_and_the_time_left(front: tuple[Any, int, int]) -> None:
    sup, port, _ = front
    sup.status.update("guard", armed=True, api="rest-v2")
    status, data = call(port, "GET", "/unstage/status")
    body = json.loads(data)
    assert status == 200 and body["guard"] == {"armed": True, "api": "rest-v2"} and body["seconds_left"] == 3600
    assert body["tools"]["state"] == "waiting_wheel" and body["wheel"]["state"] == "waiting"


def test_front_accepts_the_one_wheel_whose_hash_was_promised(front: tuple[Any, int, int], tmp_path: Path) -> None:
    sup, port, _ = front
    assert call(port, "PUT", "/unstage/wheel", b"some other bytes")[0] == 400
    assert sup.status.get("wheel", "state") == "waiting" and sup.accepted == []
    assert call(port, "PUT", "/unstage/wheel", b"x" * 5000)[0] == 413
    assert call(port, "PUT", "/unstage/wheel", b"wheel bytes")[0] == 201
    target = tmp_path / "install" / "wheels" / "virtual_unstaging-0.1.0-py3-none-any.whl"
    assert target.read_bytes() == b"wheel bytes" and sup.accepted == [str(target)]
    assert call(port, "PUT", "/unstage/wheel", b"wheel bytes")[0] == 409  # once only
    assert len(sup.accepted) == 1


def test_front_passes_only_v1_paths_to_the_judge(front: tuple[Any, int, int]) -> None:
    _, port, _ = front
    status, data = call(port, "POST", "/v1/chat/completions?x=1", b'{"model": "m"}')
    assert status == 200 and json.loads(data) == {"echo": 14, "path": "/v1/chat/completions?x=1"}
    method, path, body, authorization = Upstream.seen[0]
    assert (method, body, authorization) == ("POST", b'{"model": "m"}', f"Bearer {KEY}")
    seen_before = len(Upstream.seen)
    for path in ("/invocations", "/metrics", "/health", "/tokenize", "/v1/../invocations", "/v1/%2e%2e/metrics", "/unstage/other"):
        assert call(port, "POST", path, b"{}")[0] == 404, path
    assert len(Upstream.seen) == seen_before  # nothing reached the judge server


def test_the_judge_command_follows_another_model(boot: Any) -> None:
    template = ["vllm", "serve", "org/a", "--served-model-name", "org/a", "--max-num-seqs", "16", "--revision", "a" * 40]
    assert boot.judge_argv_for(template, "org/b", None) == ["vllm", "serve", "org/b", "--served-model-name", "org/b",
                                                           "--max-num-seqs", "16"]
    assert boot.judge_argv_for(template, "org/b", "b" * 40)[-2:] == ["--revision", "b" * 40]


def test_switching_the_judge_stops_the_old_one_and_starts_the_new(boot: Any, clock: Clock) -> None:
    started: list[list[str]] = []

    def popen(argv: list[str], env: dict[str, str], **kwargs: Any) -> FakeProcess:
        started.append(argv)
        return FakeProcess()

    template = ["vllm", "serve", "org/a", "--served-model-name", "org/a"]
    sup = supervisor(boot, base_plan(judge_argv=template), FakeGuard(boot), clock, popen=popen)
    sup._start_judge()
    old = sup.children["judge"]
    old.poll = lambda: 0 if old.terminated else None  # exits once asked to
    sup.switch_judge("org/b", None)
    assert old.terminated and sup.children["judge"] is not old
    assert started == [template, ["vllm", "serve", "org/b", "--served-model-name", "org/b"]]
    assert sup.status.get("judge", "model") == "org/b"


def test_the_front_switches_the_judge_on_a_valid_request_only(front: tuple[Any, int, int]) -> None:
    sup, port, _ = front
    asked: list[tuple[str, str | None, float | None]] = []
    sup.switch_judge = lambda model, revision, share: asked.append((model, revision, share))
    for body in (b'{"model": "../etc"}', b'{"model": "org/b", "revision": "main"}', b"not json", b"{}",
                 b'{"model": "org/b", "gpu_memory_utilization": 0.99}', b'{"model": "org/b", "gpu_memory_utilization": "0.3"}',
                 b'{"model": "org/b", "gpu_memory_utilization": true}'):
        assert call(port, "POST", "/unstage/judge", body)[0] == 400, body
    assert call(port, "POST", "/unstage/judge", b'{"model": "org/b"}', key="wrong-key-0123456789")[0] == 401
    status, data = call(port, "POST", "/unstage/judge", b'{"model": "org/b", "revision": null}')
    assert status == 202 and json.loads(data) == {"judge": {"state": "starting", "model": "org/b"}}
    assert call(port, "POST", "/unstage/judge", b'{"model": "org/c", "gpu_memory_utilization": 0.3}')[0] == 202
    for _ in range(50):
        if len(asked) == 2:
            break
        time.sleep(0.01)
    assert sorted(asked, key=lambda a: a[0]) == [("org/b", None, None), ("org/c", None, 0.3)]


def test_a_judge_switch_may_change_the_memory_share(boot: Any) -> None:
    template = ["vllm", "serve", "org/a", "--served-model-name", "org/a", "--gpu-memory-utilization", "0.55",
                "--revision", "a" * 40]
    argv = boot.judge_argv_for(template, "org/b", None, 0.3)
    assert argv[2] == "org/b" and argv[argv.index("--served-model-name") + 1] == "org/b" and "--revision" not in argv
    assert argv.count("--gpu-memory-utilization") == 1 and argv[argv.index("--gpu-memory-utilization") + 1] == "0.30"
    kept = boot.judge_argv_for(template, "org/b", None)
    assert kept[kept.index("--gpu-memory-utilization") + 1] == "0.55"


def test_front_without_a_judge_serves_no_v1(boot: Any, clock: Clock, tmp_path: Path) -> None:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    sup = supervisor(boot, base_plan(front_port=port, judge_argv=None, install_dir=str(tmp_path)), FakeGuard(boot), clock, serve_front=True)
    sup._start_front()
    try:
        assert call(port, "POST", "/v1/chat/completions", b"{}")[0] == 404
    finally:
        sup.server.shutdown()
        sup.server.server_close()


def test_front_says_503_when_the_judge_is_not_listening(boot: Any, clock: Clock, tmp_path: Path) -> None:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    dead = sock.getsockname()[1]
    sock.close()
    sock2 = socket.socket()
    sock2.bind(("127.0.0.1", 0))
    port = sock2.getsockname()[1]
    sock2.close()
    sup = supervisor(boot, base_plan(front_port=port, judge_port=dead, judge_argv=["vllm"], install_dir=str(tmp_path)), FakeGuard(boot),
                     clock, serve_front=True)
    sup._start_front()
    try:
        assert call(port, "GET", "/v1/models")[0] == 503
    finally:
        sup.server.shutdown()
        sup.server.server_close()


def test_bootstrap_has_no_effect_at_import_and_uses_only_the_standard_library() -> None:
    import ast

    tree = ast.parse((PROVISION_DIR / "bootstrap.py").read_text())
    imported = {n.names[0].name.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.Import)}
    imported |= {n.module.split(".")[0] for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.module}
    assert not any(name.startswith("virtual_unstaging") for name in imported)
    assert imported <= set(sys.stdlib_module_names)
    guard_tree = ast.parse((PROVISION_DIR / "runpod_guard.py").read_text())
    guard_imports = {n.names[0].name.split(".")[0] for n in ast.walk(guard_tree) if isinstance(n, ast.Import)}
    guard_imports |= {n.module.split(".")[0] for n in ast.walk(guard_tree) if isinstance(n, ast.ImportFrom) and n.module}
    assert guard_imports <= set(sys.stdlib_module_names)


def test_the_machine_spec_carries_the_bootstrap_the_key_and_no_provider_api_key(tmp_path: Path, gpu_project: Path) -> None:
    loaded = plan.load_plan(gpu_project)
    deadline = START + timedelta(hours=1)
    made = machine.build_spec(FakeWorld(), loaded, make_wheel(tmp_path), name="unstage-x", gpu_id="g", gpu_count=1, datacenter="d",
                              key="k" * 43, hf_token="hf_token_value", deadline_epoch=deadline.timestamp(),
                              deadline_iso="2026-10-21T13:00:00+00:00", recipe=None)
    import base64

    assert base64.b64decode(made.env["UNSTAGE_BOOT"]).decode().rstrip().endswith("main(RunpodSelfDelete)")
    assert made.entrypoint[:2] == ("python3", "-c") and made.env["HF_TOKEN"] == "hf_token_value"
    assert made.env["VLLM_NO_USAGE_STATS"] == "1" and made.env[machine.KEY_ENV] == "k" * 43
    assert made.image == plan.DEFAULT_IMAGE and ":latest" not in made.image


def test_the_machine_scripts_ship_inside_the_package_files() -> None:
    for name in ("bootstrap.py", "runpod_guard.py"):
        assert (PROVISION_DIR / name).is_file()


# --- switching the live generator or judge ------------------------------------------------------------------------


def switch_context(project: Path, tmp_path: Path, answers: dict[tuple[str, str], list[tuple[int, dict[str, Any]]]]) -> tuple[Any, list[tuple[str, str, Any]]]:
    """A context whose transport answers from scripted replies (the last reply of a list repeats)."""
    from virtual_unstaging.provision.lifecycle import Context
    from virtual_unstaging.provision.transport import Response

    key_file = tmp_path / "session.key"
    key_file.write_text(KEY + "\n", encoding="utf-8")
    key_file.chmod(0o600)
    (project / "gpu_session.toml").write_text(
        f'[tools]\nendpoint = "https://pod-8000.example"\nkey_file = "{key_file}"\n'
        f'[judge]\nendpoint = "https://pod-8001.example/v1"\nkey_file = "{key_file}"\n', encoding="utf-8")
    seen: list[tuple[str, str, Any]] = []
    tick = {"t": 0.0}

    def transport(method: str, url: str, headers: dict[str, str], body: bytes | None, timeout: float) -> Response:
        assert headers["Authorization"] == f"Bearer {KEY}"
        seen.append((method, url, json.loads(body) if body else None))
        replies = answers[(method, url)]
        status, payload = replies.pop(0) if len(replies) > 1 else replies[0]
        return Response(status, json.dumps(payload).encode())

    def sleep(seconds: float) -> None:
        tick["t"] += seconds

    ctx = Context(project=project, config_folder=tmp_path / "config", state_folder=tmp_path / "state", transport=transport,
                  sleep=sleep, monotonic=lambda: tick["t"])
    return ctx, seen


def test_gpu_recipe_loads_another_generator_and_waits_until_ready(gpu_project: Path, tmp_path: Path) -> None:
    from virtual_unstaging.provision import switch

    tools = "https://pod-8000.example"
    ctx, seen = switch_context(gpu_project, tmp_path, {
        ("PUT", f"{tools}/generator"): [(200, {"recipe": "flux2_klein_4b", "state": "not_loaded"})],
        ("GET", f"{tools}/health"): [(200, {"models": {"generator": "loading"}}), (200, {"models": {"generator": "ready"}})],
        ("GET", f"{tools}/capabilities"): [(200, {"generator": {"recipe": "flux2_klein_4b", "model": "bfl/klein"}})],
    })
    assert switch.switch_generator(ctx, "flux2_klein_4b") == {"recipe": "flux2_klein_4b", "model": "bfl/klein"}
    assert seen[0] == ("PUT", f"{tools}/generator", {"recipe": "flux2_klein_4b"})


def test_gpu_recipe_reports_a_load_failure(gpu_project: Path, tmp_path: Path) -> None:
    from virtual_unstaging.provision import switch

    tools = "https://pod-8000.example"
    ctx, _ = switch_context(gpu_project, tmp_path, {
        ("PUT", f"{tools}/generator"): [(200, {})],
        ("GET", f"{tools}/health"): [(200, {"models": {"generator": "failed"}})],
        ("GET", f"{tools}/capabilities"): [(200, {"generator": {"error": "OutOfMemoryError: CUDA out of memory"}})],
    })
    with pytest.raises(ProvisionError, match="CUDA out of memory"):
        switch.switch_generator(ctx, "qwen_image_edit_2511")


def test_gpu_judge_serves_the_project_judge_and_waits_for_it(gpu_project: Path, tmp_path: Path) -> None:
    from virtual_unstaging.provision import switch

    front = "https://pod-8001.example"
    ctx, seen = switch_context(gpu_project, tmp_path, {
        ("POST", f"{front}/unstage/judge"): [(202, {"judge": {"state": "starting"}})],
        ("GET", f"{front}/unstage/status"): [
            (200, {"judge": {"state": "ready", "model": "org/old"}}),  # the old judge's state is never taken as ready
            (200, {"judge": {"state": "starting", "model": JUDGE_MODEL}}),
            (200, {"judge": {"state": "ready", "model": JUDGE_MODEL}}),
        ],
    })
    assert switch.switch_judge(ctx) == JUDGE_MODEL
    assert seen[0] == ("POST", f"{front}/unstage/judge", {"model": JUDGE_MODEL, "revision": None})
    assert len([s for s in seen if s[1].endswith("/unstage/status")]) == 3


def test_gpu_judge_sends_the_memory_share_of_the_override_files(gpu_project: Path, tmp_path: Path) -> None:
    from virtual_unstaging.provision import switch

    front = "https://pod-8001.example"
    ctx, seen = switch_context(gpu_project, tmp_path, {
        ("POST", f"{front}/unstage/judge"): [(202, {"judge": {"state": "starting"}})],
        ("GET", f"{front}/unstage/status"): [(200, {"judge": {"state": "ready", "model": "org/small"}})],
    })
    override = tmp_path / "small_judge.toml"
    override.write_text('[judge]\nmodel = "org/small"\n[gpu.judge]\ngpu_memory_utilization = 0.3\n', encoding="utf-8")
    ctx.overrides = (override,)
    assert switch.switch_judge(ctx) == "org/small"
    assert seen[0] == ("POST", f"{front}/unstage/judge", {"model": "org/small", "revision": None, "gpu_memory_utilization": 0.3})


def test_gpu_judge_without_a_session_says_so(gpu_project: Path, tmp_path: Path) -> None:
    from virtual_unstaging.provision import switch
    from virtual_unstaging.provision.lifecycle import Context

    ctx = Context(project=gpu_project, config_folder=tmp_path, state_folder=tmp_path)
    with pytest.raises(ProvisionError) as missing:
        switch.switch_judge(ctx)
    assert missing.value.code == "no_session"
