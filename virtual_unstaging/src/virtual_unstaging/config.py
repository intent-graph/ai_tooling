"""Project configuration (`project.toml`), parsed strictly; secrets are read from a key file or a command."""

from __future__ import annotations

import os
import stat
import subprocess
import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from virtual_unstaging.domain import (
    MAX_FINDINGS,
    MAX_MOVES,
    ROLES,
    Budget,
    GeneratorCapabilities,
    JudgeRequestOptions,
)

CONFIG_NAME = "project.toml"

TEMPLATE = """\
# virtual_unstaging project. Secrets never go here: name a key file (mode 600) or a key command instead.

[project]
name = "{name}"

[generator]
adapter = "toolserver"            # toolserver | openai_images | fake
endpoint = ""                     # tool server URL, or an OpenAI-style server's base URL ending in /v1
key_file = ""                     # e.g. "~/.config/virtual-unstaging/toolserver.key"
model = ""                        # openai_images only: model name and its capabilities below
revision = "unpinned"
licence = ""
max_images = 4
native_mask = false
roles = ["original", "reference", "removal_mask", "protected_mask"]
instructions = "default"

[judge]
adapter = "openai_chat"           # openai_chat | fake
endpoint = ""                     # base URL ending in /v1
key_file = ""
model = ""
revision = "unpinned"
box_scale = "per_mille"           # per_mille (0-1000 grid) | unit (0-1)
temperature = 0.0
max_tokens = 4096
instructions = "default"
# Speed: what the judge is sent and how long it may answer (0 = as stored, no cap)
image_side = 0                    # long side of every image sent, in pixels
image_format = "png"              # png | jpeg
max_findings = 12
max_moves = 4
comment_chars = 0                 # each finding's comment and each move's reason
critique_chars = 0

[tools]
class_diff = true                 # needs the tool server

[budget]
max_attempts = 6
max_gpu_seconds = 900
max_judge_calls = 14

[search]
minor_tolerance = 1
workers = 2
"""


class ConfigError(ValueError):
    pass


class SecretError(ConfigError):
    """A key could not be read; `code` is stable (`key_unsafe`, `key_missing`). The value is never in a message."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code


@dataclass(frozen=True)
class Secret:
    """Where a key is read from: a file (mode 600) or a command run without a shell. The one reader of keys."""

    key_file: str = ""
    key_command: tuple[str, ...] = ()

    def read(self) -> str | None:
        """The key's text, or None when no source is named."""
        if not self.key_file and not self.key_command:
            return None
        value = ""
        if self.key_file:
            path = Path(self.key_file).expanduser()
            try:
                if path.stat().st_mode & (stat.S_IRWXG | stat.S_IRWXO):
                    raise SecretError("key_unsafe", f"{path} is readable by others: chmod 600 {path}")
                value = path.read_text(encoding="utf-8").strip()
            except FileNotFoundError:
                raise SecretError("key_missing", f"no key file {path}") from None
            except OSError as error:
                raise SecretError("key_missing", f"cannot read {path}: {type(error).__name__}") from None
        else:
            try:
                done = subprocess.run(list(self.key_command), capture_output=True, text=True, timeout=60, check=True)
            except (OSError, subprocess.SubprocessError) as error:
                raise SecretError("key_missing", f"the key command failed ({type(error).__name__})") from None
            value = done.stdout.strip()
        if not value:
            raise SecretError("key_missing", "the key is empty")
        return value


@dataclass(frozen=True)
class GeneratorConfig:
    adapter: str
    endpoint: str
    secret: Secret
    model: str
    revision: str
    licence: str
    capabilities: GeneratorCapabilities
    instructions: str
    settings: dict[str, Any] = field(default_factory=dict)
    fields: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class JudgeConfig:
    adapter: str
    endpoint: str
    secret: Secret
    model: str
    revision: str
    box_scale: str
    temperature: float
    max_tokens: int
    instructions: str
    extra: dict[str, Any] = field(default_factory=dict)
    request: JudgeRequestOptions = field(default_factory=lambda: JudgeRequestOptions())


@dataclass(frozen=True)
class ProjectConfig:
    name: str
    generator: GeneratorConfig
    judge: JudgeConfig
    class_diff: bool
    tools_endpoint: str
    tools_secret: Secret
    budget: Budget
    minor_tolerance: int
    workers: int


_SECTIONS = {
    "project": {"name"},
    "generator": {"adapter", "endpoint", "key_file", "key_command", "model", "revision", "licence", "max_images",
                  "native_mask", "roles", "instructions", "settings", "fields"},
    "judge": {"adapter", "endpoint", "key_file", "key_command", "model", "revision", "box_scale", "temperature",
              "max_tokens", "instructions", "extra", "image_side", "image_format", "max_findings", "max_moves",
              "comment_chars", "critique_chars"},
    "tools": {"class_diff", "endpoint", "key_file", "key_command"},
    "budget": {"max_attempts", "max_gpu_seconds", "max_judge_calls"},
    "search": {"minor_tolerance", "workers"},
}


SESSION_NAME = "gpu_session.toml"
# What a GPU session may set over project.toml: where the rented machine's endpoints are, and their key files.
_SESSION_KEYS = {"endpoint", "key_file", "key_command"}

# Override files (design D13): the sections they may set; `gpu` holds gpu.toml's sections. Endpoints and keys never.
OVERRIDE_SECTIONS = ("generator", "judge", "tools", "budget", "search", "gpu")
_NOT_OVERRIDABLE = {"endpoint", "key_file", "key_command", "key", "api_key"}


def read_overrides(paths: Sequence[Path]) -> list[dict[str, Any]]:
    """Override files in the order given, parsed and checked for what they may never set (design D13)."""
    layers: list[dict[str, Any]] = []
    for path in paths:
        try:
            data = tomllib.loads(Path(path).read_text(encoding="utf-8"))
        except FileNotFoundError:
            raise ConfigError(f"no override file {path}") from None
        except tomllib.TOMLDecodeError as error:
            raise ConfigError(f"override file {path}: {error}") from None
        for section, values in data.items():
            if section not in OVERRIDE_SECTIONS or not isinstance(values, dict):
                raise ConfigError(f"override file {path}: [{section}] cannot be overridden (only {', '.join(OVERRIDE_SECTIONS)})")
            tables = list(values.values()) if section == "gpu" else [values]
            if not all(isinstance(table, dict) for table in tables):
                raise ConfigError(f"override file {path}: [gpu] holds only tables, such as [gpu.judge]")
            forbidden = sorted(set().union(*(set(table) & _NOT_OVERRIDABLE for table in tables)))
            if forbidden:
                raise ConfigError(f"override file {path}: {', '.join(forbidden)} come only from the project and its GPU session")
        layers.append(data)
    return layers


def merged(base: Mapping[str, Any], layer: Mapping[str, Any]) -> dict[str, Any]:
    """`base` with `layer` over it: tables merge key by key, any other value (a list included) is replaced."""
    result = dict(base)
    for key, value in layer.items():
        below = result.get(key)
        result[key] = merged(below, value) if isinstance(value, dict) and isinstance(below, dict) else value
    return result


def project_data(project_dir: Path, overrides: Sequence[Path] = ()) -> dict[str, Any]:
    """`project.toml` with the override files' project sections over it, unchecked: each reader checks what it reads."""
    path = project_dir / CONFIG_NAME
    try:
        data: dict[str, Any] = tomllib.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ConfigError(f"no {CONFIG_NAME} in {project_dir}: run `init` first") from None
    for layer in read_overrides(overrides):
        data = merged(data, {section: values for section, values in layer.items() if section != "gpu"})
    return data


def gpu_options(overrides: Sequence[Path]) -> dict[str, Any]:
    """The `gpu.toml` sections set by the override files, merged in order."""
    options: dict[str, Any] = {}
    for layer in read_overrides(overrides):
        options = merged(options, layer.get("gpu", {}))
    return options


def load(project_dir: Path, overrides: Sequence[Path] = ()) -> ProjectConfig:
    data = project_data(project_dir, overrides)
    session_path = project_dir / SESSION_NAME
    if session_path.is_file():
        session = tomllib.loads(session_path.read_text(encoding="utf-8"))
        for section, values in session.items():
            if section not in ("generator", "judge", "tools") or set(values) - _SESSION_KEYS:
                raise ConfigError(f"{SESSION_NAME}: only endpoint, key_file, key_command in [generator], [judge], [tools]")
            data.setdefault(section, {}).update(values)
    for section, values in data.items():
        if section not in _SECTIONS:
            raise ConfigError(f"unknown section [{section}]")
        unknown = set(values) - _SECTIONS[section]
        if unknown:
            raise ConfigError(f"[{section}]: unknown keys {sorted(unknown)}")
        if "key" in values or "api_key" in values:
            raise ConfigError(f"[{section}]: a key never goes in {CONFIG_NAME}; use key_file or key_command")
    g, j = data.get("generator", {}), data.get("judge", {})
    t, b, s = data.get("tools", {}), data.get("budget", {}), data.get("search", {})
    roles = frozenset(g.get("roles", ["original", "reference", "removal_mask", "protected_mask"]))
    if not roles <= set(ROLES) or "original" not in roles:
        raise ConfigError(f"[generator] roles must include 'original' and be among {ROLES}")
    adapter = _choice(g, "adapter", "toolserver", ("toolserver", "openai_images", "fake"))
    generator = GeneratorConfig(
        adapter=adapter,
        endpoint=str(g.get("endpoint", "")),
        secret=_secret(g),
        model=str(g.get("model", "")),
        revision=str(g.get("revision", "unpinned")),
        licence=str(g.get("licence", "")),
        capabilities=GeneratorCapabilities(roles, _int(g, "max_images", 4, 1), bool(g.get("native_mask", False))),
        instructions=str(g.get("instructions", "default")),
        settings=dict(g.get("settings", {})),
        fields={str(k): str(v) for k, v in dict(g.get("fields", {})).items()},
    )
    judge = JudgeConfig(
        adapter=_choice(j, "adapter", "openai_chat", ("openai_chat", "fake")),
        endpoint=str(j.get("endpoint", "")),
        secret=_secret(j),
        model=str(j.get("model", "")),
        revision=str(j.get("revision", "unpinned")),
        box_scale=_choice(j, "box_scale", "per_mille", ("per_mille", "unit")),
        temperature=float(j.get("temperature", 0.0)),
        max_tokens=_int(j, "max_tokens", 4096, 256),
        instructions=str(j.get("instructions", "default")),
        extra=dict(j.get("extra", {})),
        request=JudgeRequestOptions(
            image_side=_zero_or(j, "image_side", 256, 4096),
            image_format="jpeg" if _choice(j, "image_format", "png", ("png", "jpeg")) == "jpeg" else "png",
            max_findings=_within(j, "max_findings", MAX_FINDINGS, 1, MAX_FINDINGS),
            max_moves=_within(j, "max_moves", MAX_MOVES, 0, MAX_MOVES),
            comment_chars=_zero_or(j, "comment_chars", 20, 600),
            critique_chars=_zero_or(j, "critique_chars", 20, 600),
        ),
    )
    tools_endpoint = str(t.get("endpoint", generator.endpoint if adapter == "toolserver" else ""))
    return ProjectConfig(
        name=str(data.get("project", {}).get("name", project_dir.name)),
        generator=generator,
        judge=judge,
        class_diff=bool(t.get("class_diff", True)),
        tools_endpoint=tools_endpoint,
        tools_secret=_secret(t) if ("key_file" in t or "key_command" in t) else generator.secret,
        budget=Budget(_int(b, "max_attempts", 6, 1), float(b.get("max_gpu_seconds", 900)), _int(b, "max_judge_calls", 14, 1)),
        minor_tolerance=_int(s, "minor_tolerance", 1, 0),
        workers=_int(s, "workers", 2, 1),
    )


def write_template(project_dir: Path, name: str) -> Path:
    path = project_dir / CONFIG_NAME
    if path.exists():
        raise ConfigError(f"{path} exists")
    path.write_text(TEMPLATE.format(name=name.replace('"', "'")), encoding="utf-8")
    return path


def overlay_text(project_dir: Path, role: str) -> str | None:
    """The project overlay of a role's instructions, from `instructions/<role>.md` in the project, if any."""
    path = project_dir / "instructions" / f"{role}.md"
    return path.read_text(encoding="utf-8") if path.is_file() else None


def parse_rules(text: str) -> list[tuple[str | None, str, str, str | None]]:
    """Content rules file: `[all]` and `[groups."<name>"]`, each with `fixed` and `movable` lists of elements."""
    data = tomllib.loads(text)
    unknown = set(data) - {"all", "groups"}
    if unknown:
        raise ConfigError(f"rules: unknown sections {sorted(unknown)}")
    items: list[tuple[str | None, str, str, str | None]] = []
    sections: list[tuple[str | None, dict[str, Any]]] = [(None, data.get("all", {}))]
    sections += [(str(name), dict(body)) for name, body in dict(data.get("groups", {})).items()]
    for group, body in sections:
        if set(body) - {"fixed", "movable"}:
            raise ConfigError(f"rules for {group or 'all'}: only 'fixed' and 'movable' lists")
        for disposition in ("fixed", "movable"):
            elements = body.get(disposition, [])
            if not isinstance(elements, list) or not all(isinstance(e, str) and e.strip() for e in elements):
                raise ConfigError(f"rules for {group or 'all'}: {disposition} must be a list of names")
            items += [(group, e.strip(), disposition, None) for e in elements]
    if not any(i[2] == "movable" for i in items):
        raise ConfigError("rules: no movable element anywhere")
    return items


def _secret(section: dict[str, Any]) -> Secret:
    command = section.get("key_command", [])
    if not isinstance(command, list) or not all(isinstance(c, str) for c in command):
        raise ConfigError("key_command must be a list of strings (no shell)")
    return Secret(str(section.get("key_file", "")), tuple(command))


def _choice(section: dict[str, Any], name: str, default: str, allowed: tuple[str, ...]) -> str:
    value = str(section.get(name, default))
    if value not in allowed:
        raise ConfigError(f"{name} must be one of {allowed}, got {value!r}")
    return value


def _int(section: dict[str, Any], name: str, default: int, minimum: int) -> int:
    value = section.get(name, default)
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        raise ConfigError(f"{name} must be an integer >= {minimum}")
    return value


def _within(section: dict[str, Any], name: str, default: int, low: int, high: int) -> int:
    value = section.get(name, default)
    if not isinstance(value, int) or isinstance(value, bool) or not low <= value <= high:
        raise ConfigError(f"{name} must be an integer from {low} to {high}")
    return value


def _zero_or(section: dict[str, Any], name: str, low: int, high: int) -> int:
    """0 (as stored, no cap) or an integer in [low, high]."""
    value = section.get(name, 0)
    if not isinstance(value, int) or isinstance(value, bool) or not (value == 0 or low <= value <= high):
        raise ConfigError(f"{name} must be 0 or an integer from {low} to {high}")
    return value


def environment_key(name: str) -> str | None:
    """Recorded exception (design: Command line): on the rented machine the key arrives as an environment variable."""
    return os.environ.get(name)
