"""Turn a project plan, a wheel and a deadline into what a provider rents: image, entrypoint, environment, ports."""

from __future__ import annotations

import base64
import json
import re
from importlib import resources

from virtual_unstaging.provision.plan import ProjectPlan, judge_argv
from virtual_unstaging.provision.provider import MachineSpec, Provider
from virtual_unstaging.provision.wheel import MAX_WHEEL_BYTES, Wheel

NAME_PREFIX = "unstage-"
KEY_ENV = "UNSTAGE_SESSION_KEY"
TOOLS_PORT = 8000  # the tool server, authenticated by its own key check
FRONT_PORT = 8001  # the bootstrap: status, wheel upload, and the key-checking pass-through to the judge
JUDGE_PORT = 8002  # the judge server, on loopback only
GRACE_SECONDS = 30  # after the deadline, so the tool server can finish its own exit before the machine goes
CHILD_EXIT_GRACE_SECONDS = 600  # a service that died and stays down ends the machine after this
INSTALL_DIR = "/opt/unstage"
BOOT_ENTRYPOINT = ("python3", "-c", "import base64,os;exec(base64.b64decode(os.environ['UNSTAGE_BOOT']))")
_CLASS_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")


def bootstrap_source(provider: Provider) -> str:
    """The script the machine runs: the generic bootstrap, the provider's self-delete, then the call that starts it."""
    if not _CLASS_NAME.fullmatch(provider.guard_class):
        raise ValueError("guard_class must be a plain class name")
    base = resources.files("virtual_unstaging.provision").joinpath("bootstrap.py").read_text("utf-8")
    return f"{base}\n\n{provider.guard_source}\n\nmain({provider.guard_class})\n"


def machine_plan(
    plan: ProjectPlan, wheel: Wheel, deadline_epoch: float, deadline_iso: str, gpu_count: int, recipe: str | None
) -> dict[str, object]:
    """The JSON the bootstrap reads (UNSTAGE_PLAN): the absolute deadline, the services' commands, the wheel's hash."""
    shared = gpu_count < 2
    tools_argv = ["serve", "--host", "0.0.0.0", "--port", str(TOOLS_PORT), "--deadline", deadline_iso,
                  "--key-env", KEY_ENV]
    if plan.tools is not None:
        tools_argv += ["--tools", ",".join(plan.tools)]
    if recipe:
        tools_argv += ["--recipe", recipe]
    return {
        "deadline": deadline_epoch,
        "grace_seconds": GRACE_SECONDS,
        "child_exit_grace_seconds": CHILD_EXIT_GRACE_SECONDS,
        "key_env": KEY_ENV,
        "front_port": FRONT_PORT,
        "tools_port": TOOLS_PORT,
        "judge_port": JUDGE_PORT,
        "judge_argv": judge_argv(plan.judge, JUDGE_PORT, shared) if plan.judge else None,
        "judge_gpu": None if shared else "1",
        "tools_argv": tools_argv,
        "tools_gpu": None if shared else "0",
        "wheel": {"filename": wheel.filename, "sha256": wheel.sha256, "max_bytes": MAX_WHEEL_BYTES},
        "install_dir": INSTALL_DIR,
        "log_dir": f"{INSTALL_DIR}/logs",
    }


def build_spec(
    provider: Provider,
    plan: ProjectPlan,
    wheel: Wheel,
    *,
    name: str,
    gpu_id: str,
    gpu_count: int,
    datacenter: str,
    key: str,
    hf_token: str | None,
    deadline_epoch: float,
    deadline_iso: str,
    recipe: str | None,
) -> MachineSpec:
    """The machine to rent. The deadline is an argument with no default: a spec cannot be built without one."""
    script = base64.b64encode(bootstrap_source(provider).encode("utf-8")).decode("ascii")
    env = {
        "UNSTAGE_BOOT": script,
        "UNSTAGE_PLAN": json.dumps(machine_plan(plan, wheel, deadline_epoch, deadline_iso, gpu_count, recipe)),
        KEY_ENV: key,
        # No usage statistics leave the machine.
        "VLLM_NO_USAGE_STATS": "1",
        "DO_NOT_TRACK": "1",
        "HF_HUB_DISABLE_TELEMETRY": "1",
    }
    if hf_token:
        env["HF_TOKEN"] = hf_token
    return MachineSpec(
        name=name,
        gpu_id=gpu_id,
        gpu_count=gpu_count,
        datacenter=datacenter,
        image=plan.image,
        disk_gb=plan.disk_gb,
        ports=(TOOLS_PORT, FRONT_PORT),
        env=env,
        entrypoint=BOOT_ENTRYPOINT,
        min_cuda=plan.min_cuda,
    )
