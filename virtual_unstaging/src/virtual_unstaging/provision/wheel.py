"""Build the package into a wheel on the owner's machine: the code is not on any index, so it travels as a file."""

from __future__ import annotations

import hashlib
import re
import subprocess
import tempfile
import tomllib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import virtual_unstaging
from virtual_unstaging.provision.errors import ProvisionError

MAX_WHEEL_BYTES = 64 * 1024 * 1024
WHEEL_NAME = re.compile(r"^[A-Za-z0-9_.]+-[A-Za-z0-9_.!+]+-py3-none-any\.whl$")
PACKAGE_NAME = "virtual-unstaging"

Runner = Callable[..., Any]


@dataclass(frozen=True)
class Wheel:
    path: Path
    filename: str
    sha256: str
    size: int

    def read(self) -> bytes:
        return self.path.read_bytes()


def source_root() -> Path:
    """The source checkout this package runs from (the folder holding its `pyproject.toml`)."""
    for parent in Path(virtual_unstaging.__file__).resolve().parents:
        candidate = parent / "pyproject.toml"
        if candidate.is_file():
            try:
                name = tomllib.loads(candidate.read_text(encoding="utf-8")).get("project", {}).get("name")
            except (OSError, tomllib.TOMLDecodeError):
                continue
            if name == PACKAGE_NAME:
                return parent
    raise ProvisionError(
        "wheel_source_missing",
        "the package source (its pyproject.toml) was not found above the installed code",
        "run `unstage gpu up` from a source checkout installed in editable mode",
    )


def build_wheel(root: Path, out_dir: Path, runner: Runner = subprocess.run) -> Wheel:
    """`uv build --wheel` of the source tree; no shell. Exactly one wheel must come out, of a plain name and size."""
    try:
        done = runner(
            ["uv", "build", "--wheel", "--out-dir", str(out_dir), str(root)],
            capture_output=True, text=True, timeout=600, check=False,
        )
    except (OSError, subprocess.SubprocessError) as error:
        raise ProvisionError("wheel_build_failed", f"cannot run uv build ({type(error).__name__})", "install uv") from None
    if done.returncode != 0:
        tail = "\n".join(str(done.stderr or "").splitlines()[-8:])
        raise ProvisionError("wheel_build_failed", f"uv build failed:\n{tail}")
    wheels = sorted(out_dir.glob("*.whl"))
    if len(wheels) != 1 or not WHEEL_NAME.fullmatch(wheels[0].name):
        raise ProvisionError("wheel_build_failed", f"expected one plain wheel in {out_dir}, found {[w.name for w in wheels]}")
    data = wheels[0].read_bytes()
    if not 0 < len(data) <= MAX_WHEEL_BYTES:
        raise ProvisionError("wheel_build_failed", f"the wheel is {len(data)} bytes")
    return Wheel(wheels[0], wheels[0].name, hashlib.sha256(data).hexdigest(), len(data))


def build_default(runner: Runner = subprocess.run) -> tuple[Wheel, tempfile.TemporaryDirectory[str]]:
    """Build into a temporary folder; the caller keeps the returned folder object alive while the wheel is used."""
    folder = tempfile.TemporaryDirectory(prefix="unstage-wheel-")
    try:
        return build_wheel(source_root(), Path(folder.name), runner), folder
    except BaseException:
        folder.cleanup()
        raise
