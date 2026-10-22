"""The dataset's configuration (`clutter_pairs.toml`), the GPU session file over it, and the data files in force.

Parsed strictly: unknown keys stop the command before any call. Keys only by file or command (`config.Secret`).
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, fields
from importlib import resources
from pathlib import Path
from typing import Any

from virtual_unstaging.config import Secret
from virtual_unstaging.provision.lifecycle import SESSION_FILE

from clutter_pairs.pairs import Thresholds

CONFIG_NAME = "clutter_pairs.toml"
TEMPLATE = "config_template.toml"
DATA_FOLDERS = {"instructions": "instruction", "knowledge": "instruction", "composers": "composer", "schemas": "schema",
                "space": None, "decision_rules": "decision_rule"}
SPACE_KINDS = {"space/ontology.toml": "ontology", "space/taxonomy.toml": "taxonomy", "space/targets.toml": "targets"}
_SECTIONS: dict[str, set[str]] = {
    "dataset": {"seed"},
    "generator": {"recipe", "family", "licence", "size_multiple", "condition_max_pixels", "endpoint", "key_file",
                  "key_command"},
    "judge": {"model", "revision", "family", "licence", "judge_temperature", "writer_temperature", "max_tokens",
              "endpoint", "key_file", "key_command"},
    "run": {"pair_target", "output_side", "max_iterations", "wave_width", "lessons_per_request", "variants",
            "expected_call_seconds"},
    "pixels": {f.name for f in fields(Thresholds)},
    "files": set(),
    "gpu": {"provider", "gpu", "machine", "judge"},
}


class ConfigError(ValueError):
    """A configuration that cannot be used; the message says what to change."""


@dataclass(frozen=True)
class Service:
    endpoint: str
    secret: Secret


@dataclass(frozen=True)
class GeneratorConfig:
    recipe: str
    family: str
    licence: str
    size_multiple: int
    condition_max_pixels: int
    service: Service


@dataclass(frozen=True)
class JudgeConfig:
    model: str
    revision: str
    family: str
    licence: str
    judge_temperature: float
    writer_temperature: float
    max_tokens: int
    service: Service


@dataclass(frozen=True)
class RunConfig:
    pair_target: int
    output_side: int
    max_iterations: int
    wave_width: int
    lessons_per_request: int
    variants: int
    expected_call_seconds: float


@dataclass(frozen=True)
class GpuConfig:
    provider: str
    gpu: str | None
    machine: dict[str, Any]
    judge: dict[str, Any]


@dataclass(frozen=True)
class Config:
    folder: Path
    text: str  # the file as read, recorded on each run
    seed: int
    generator: GeneratorConfig
    judge: JudgeConfig
    run: RunConfig
    pixels: dict[str, float]
    files: dict[str, str]  # packaged path -> dataset-relative replacement
    gpu: GpuConfig
    session_id: str | None  # the GPU session whose endpoints are in force


def template() -> str:
    return resources.files("clutter_pairs.data").joinpath(TEMPLATE).read_text(encoding="utf-8")


def load(folder: Path) -> Config:
    path = folder / CONFIG_NAME
    try:
        text = path.read_text(encoding="utf-8")
        data = tomllib.loads(text)
    except FileNotFoundError:
        raise ConfigError(f"no {CONFIG_NAME} in {folder}: run `cpairs init {folder}` first") from None
    except tomllib.TOMLDecodeError as error:
        raise ConfigError(f"{path}: {error}") from None
    for section, values in data.items():
        if section not in _SECTIONS or not isinstance(values, dict):
            raise ConfigError(f"{CONFIG_NAME}: unknown section [{section}]")
        unknown = set(values) - _SECTIONS[section] if section != "files" else set()
        if unknown:
            raise ConfigError(f"{CONFIG_NAME} [{section}]: unknown keys {sorted(unknown)}")
        if "key" in values or "api_key" in values:
            raise ConfigError(f"[{section}]: a key never goes in {CONFIG_NAME}; use key_file or key_command")
    session_id = _apply_session(folder, data)
    g, j, r, ds = data.get("generator", {}), data.get("judge", {}), data.get("run", {}), data.get("dataset", {})
    files = {str(k): str(v) for k, v in data.get("files", {}).items()}
    for packaged in files:
        if packaged.split("/")[0] not in DATA_FOLDERS or ".." in packaged:
            raise ConfigError(f"[files]: {packaged} is not a packaged data file")
    gpu = data.get("gpu", {})
    pixels = data.get("pixels", {})
    return Config(
        folder=folder, text=text, seed=_int(ds, "seed", 1, 0, 2**31 - 1),
        generator=GeneratorConfig(
            recipe=_str(g, "recipe", "flux2_klein_4b"), family=_str(g, "family", "flux2"),
            licence=_str(g, "licence", "unknown"), size_multiple=_int(g, "size_multiple", 32, 1, 256),
            condition_max_pixels=_int(g, "condition_max_pixels", 1024 * 1024, 65536, 16_000_000), service=_service(g)),
        judge=JudgeConfig(
            model=_str(j, "model", "Qwen/Qwen3-VL-8B-Instruct"), revision=_str(j, "revision", "unpinned"),
            family=_str(j, "family", "qwen3_vl"), licence=_str(j, "licence", "unknown"),
            judge_temperature=_float(j, "judge_temperature", 0.0, 0.0, 2.0),
            writer_temperature=_float(j, "writer_temperature", 0.8, 0.0, 2.0),
            max_tokens=_int(j, "max_tokens", 2048, 64, 32768), service=_service(j)),
        run=RunConfig(
            pair_target=_int(r, "pair_target", 50, 1, 1_000_000), output_side=_int(r, "output_side", 1024, 256, 2048),
            max_iterations=_int(r, "max_iterations", 6, 1, 50), wave_width=_int(r, "wave_width", 4, 1, 64),
            lessons_per_request=_int(r, "lessons_per_request", 5, 0, 50), variants=_int(r, "variants", 3, 1, 20),
            expected_call_seconds=_float(r, "expected_call_seconds", 90.0, 0.0, 3600.0)),
        pixels={k: _float(pixels, k, 0.0, 0.0, 1e6) for k in pixels},
        files=files,
        gpu=GpuConfig(provider=_str(gpu, "provider", "runpod"), gpu=gpu.get("gpu"),
                      machine=dict(gpu.get("machine", {})), judge=dict(gpu.get("judge", {}))),
        session_id=session_id,
    )


def _apply_session(folder: Path, data: dict[str, Any]) -> str | None:
    """The GPU session file's endpoints and key files over the configuration's; its session id."""
    path = folder / SESSION_FILE
    if not path.is_file():
        return None
    content = path.read_text(encoding="utf-8")
    session = tomllib.loads(content)
    for section in ("generator", "judge"):
        values = session.get(section, {})
        if set(values) - {"endpoint", "key_file", "key_command"}:
            raise ConfigError(f"{SESSION_FILE}: only endpoint, key_file and key_command in [{section}]")
        data.setdefault(section, {}).update(values)
    first = content.splitlines()[0] if content else ""
    return first.rsplit(" ", 1)[-1] if first.startswith("#") else None


def thresholds(cfg: Config, decided: dict[str, float]) -> Thresholds:
    """The pixel thresholds in force: the defaults, the configuration's, then the owner's decisions."""
    values: dict[str, Any] = {**cfg.pixels, **decided}
    unknown = set(values) - {f.name for f in fields(Thresholds)}
    if unknown:
        raise ConfigError(f"unknown pixel thresholds {sorted(unknown)}")
    return Thresholds.of(values)


def read_data_file(cfg: Config, packaged: str) -> tuple[str, str]:
    """(label, content) of a data file: the dataset's replacement when [files] names one, the packaged file
    otherwise. The label is the path recorded with it."""
    replacement = cfg.files.get(packaged)
    if replacement is not None:
        path = (cfg.folder / replacement).resolve()
        try:
            return f"dataset:{replacement}", path.read_text(encoding="utf-8")
        except FileNotFoundError:
            raise ConfigError(f"[files] {packaged} = {replacement}: no such file in {cfg.folder}") from None
    folder, _, name = packaged.partition("/")
    resource = resources.files("clutter_pairs.data")
    target = resource.joinpath(packaged) if name else resource.joinpath(folder)
    if not target.is_file():
        raise ConfigError(f"no packaged data file {packaged}")
    return f"package:{packaged}", target.read_text(encoding="utf-8")


def file_kind(packaged: str) -> str:
    if packaged in SPACE_KINDS:
        return SPACE_KINDS[packaged]
    if packaged == "reasons.toml":
        return "reasons"
    kind = DATA_FOLDERS.get(packaged.split("/")[0])
    if kind is None:
        raise ConfigError(f"no kind for data file {packaged}")
    return kind


def _service(section: dict[str, Any]) -> Service:
    command = section.get("key_command", [])
    if not isinstance(command, list) or not all(isinstance(c, str) for c in command):
        raise ConfigError("key_command must be a list of strings (no shell)")
    return Service(str(section.get("endpoint", "")), Secret(str(section.get("key_file", "")), tuple(command)))


def _str(section: dict[str, Any], key: str, default: str) -> str:
    value = section.get(key, default)
    if not isinstance(value, str) or not value:
        raise ConfigError(f"{key} must be a non-empty text")
    return value


def _int(section: dict[str, Any], key: str, default: int, low: int, high: int) -> int:
    value = section.get(key, default)
    if not isinstance(value, int) or isinstance(value, bool) or not low <= value <= high:
        raise ConfigError(f"{key} must be an integer from {low} to {high}")
    return value


def _float(section: dict[str, Any], key: str, default: float, low: float, high: float) -> float:
    value = section.get(key, default)
    if not isinstance(value, (int, float)) or isinstance(value, bool) or not low <= value <= high:
        raise ConfigError(f"{key} must be a number from {low} to {high}")
    return float(value)
