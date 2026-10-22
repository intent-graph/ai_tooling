"""What a project asks of a rented machine: read from `project.toml` and the optional `gpu.toml`, parsed strictly."""

from __future__ import annotations

import json
import re
import tomllib
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from virtual_unstaging import config
from virtual_unstaging.provision.errors import ProvisionError

PROJECT_NAME = "project.toml"
OPTIONS_NAME = "gpu.toml"

DEFAULT_IMAGE = "vllm/vllm-openai:v0.28.0"
DEFAULT_MIN_CUDA = "13.0"
DEFAULT_DISK_GB = 200
DEFAULT_MIN_VRAM_GB = 80
DEFAULT_GPU_PREFER = (
    "NVIDIA RTX PRO 6000 Blackwell Server Edition",
    "NVIDIA H100 80GB HBM3",
    "NVIDIA H100 NVL",
    "NVIDIA A100-SXM4-80GB",
)
QUANTIZATIONS = frozenset({"fp8", "awq", "gptq", "bitsandbytes", "compressed-tensors", "awq_marlin", "gptq_marlin"})

_MODEL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,95}/[A-Za-z0-9][A-Za-z0-9._-]{0,95}$")
_REVISION = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]{0,127}$")
_IMAGE = re.compile(r"^[a-z0-9][a-z0-9._/-]{0,127}:[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
_CUDA = re.compile(r"^[0-9]{1,2}\.[0-9]{1,2}$")
GPU_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ._()/-]{0,95}$")
_RECIPE = re.compile(r"^[a-z][a-z0-9_]{0,63}$")  # the tool server's own rule for a recipe name

_OPTION_KEYS = {
    "machine": {"image", "min_cuda", "disk_gb", "min_vram_gb", "gpu_prefer"},
    "judge": {"quantization", "max_model_len", "images_per_prompt", "gpu_memory_utilization", "max_num_seqs"},
}


@dataclass(frozen=True)
class JudgePlan:
    """The judge server (vLLM): the model from the project's [judge], the server options from `gpu.toml`."""

    model: str
    revision: str | None
    quantization: str | None
    max_model_len: int
    images_per_prompt: int
    gpu_memory_utilization: float | None
    max_num_seqs: int = 16


@dataclass(frozen=True)
class ProjectPlan:
    name: str
    serves_generator_endpoint: bool
    judge: JudgePlan | None
    image: str
    min_cuda: str
    disk_gb: int
    min_vram_gb: int
    gpu_prefer: tuple[str, ...]
    tools: tuple[str, ...] | None = None  # the tool server's tools by name; None: the server's own default set


def check_recipe(recipe: str | None) -> str | None:
    """A generator recipe is named, never a path: the machine only knows the recipes shipped in the wheel."""
    if recipe is None:
        return None
    if not _RECIPE.fullmatch(recipe):
        raise ProvisionError(
            "recipe_invalid", f"{recipe!r} is not a recipe name", "use the name of a packaged recipe (no path, no .toml)"
        )
    return recipe


def load_plan(project: Path, overrides: Sequence[Path] = ()) -> ProjectPlan:
    """The plan from `project.toml` and `gpu.toml`, with the override files over both (design D13)."""
    path = project / PROJECT_NAME
    if not path.is_file():
        raise ProvisionError("project_missing", f"no {PROJECT_NAME} in {project}", "run `unstage init` first")
    try:
        data = config.project_data(project, overrides)
        options = _checked_options(config.merged(_load_options(project / OPTIONS_NAME), config.gpu_options(overrides)),
                                   "the options with the override files")
    except tomllib.TOMLDecodeError as error:
        raise ProvisionError("project_invalid", f"{path}: {error}") from error
    except config.ConfigError as error:
        raise ProvisionError("options_invalid", str(error)) from error
    machine, judge_options = options.get("machine", {}), options.get("judge", {})
    generator, judge = data.get("generator", {}), data.get("judge", {})
    judge_plan = None
    if str(judge.get("adapter", "openai_chat")) == "openai_chat":
        judge_plan = _judge_plan(judge, judge_options)
    return ProjectPlan(
        name=str(data.get("project", {}).get("name", project.resolve().name)),
        serves_generator_endpoint=str(generator.get("adapter", "toolserver")) == "toolserver",
        judge=judge_plan,
        image=_text(machine, "image", DEFAULT_IMAGE, _IMAGE, "an image with a version tag, like repo/name:1.2.3"),
        min_cuda=_text(machine, "min_cuda", DEFAULT_MIN_CUDA, _CUDA, "a version like 13.0"),
        disk_gb=_integer(machine, "disk_gb", DEFAULT_DISK_GB, 20, 2000),
        min_vram_gb=_integer(machine, "min_vram_gb", DEFAULT_MIN_VRAM_GB, 8, 1000),
        gpu_prefer=_gpu_list(machine.get("gpu_prefer", list(DEFAULT_GPU_PREFER))),
    )


def _load_options(path: Path) -> dict[str, dict[str, Any]]:
    if not path.is_file():
        return {}
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as error:
        raise ProvisionError("options_invalid", f"{path}: {error}") from error
    return _checked_options(data, str(path))


def _checked_options(data: dict[str, Any], where: str) -> dict[str, Any]:
    for section, values in data.items():
        if section not in _OPTION_KEYS or not isinstance(values, dict) or set(values) - _OPTION_KEYS[section]:
            raise ProvisionError(
                "options_invalid", f"{where}: only [machine] {sorted(_OPTION_KEYS['machine'])} and [judge] {sorted(_OPTION_KEYS['judge'])}"
            )
    return data


def _judge_plan(judge: dict[str, Any], options: dict[str, Any]) -> JudgePlan:
    model = str(judge.get("model", ""))
    if not model:
        raise ProvisionError("judge_model_missing", "[judge] model is empty in project.toml", "name the model the judge server loads")
    if not _MODEL.fullmatch(model):
        raise ProvisionError("project_invalid", f"[judge] model {model!r} is not an org/name repository id")
    revision = str(judge.get("revision", "unpinned"))
    if revision != "unpinned" and not _REVISION.fullmatch(revision):
        raise ProvisionError("project_invalid", f"[judge] revision {revision!r} is not a commit or branch name")
    quantization = options.get("quantization")
    if quantization is not None and quantization not in QUANTIZATIONS:
        raise ProvisionError("options_invalid", f"[judge] quantization must be one of {sorted(QUANTIZATIONS)}")
    utilization = options.get("gpu_memory_utilization")
    if utilization is not None and (isinstance(utilization, bool) or not isinstance(utilization, (int, float))
                                    or not 0.1 <= utilization <= 0.95):
        raise ProvisionError("options_invalid", "[judge] gpu_memory_utilization must be between 0.1 and 0.95")
    return JudgePlan(
        model=model,
        revision=None if revision == "unpinned" else revision,
        quantization=quantization,
        max_model_len=_integer(options, "max_model_len", 16384, 1024, 1_000_000),
        images_per_prompt=_integer(options, "images_per_prompt", 8, 1, 32),
        gpu_memory_utilization=None if utilization is None else float(utilization),
        # One project's runner sends a few judgments at a time; vLLM's default of 256 reserves a state block per
        # sequence for hybrid (Mamba-style) models and fails to start when they do not fit (measured on a Qwen3.8 judge).
        max_num_seqs=_integer(options, "max_num_seqs", 16, 1, 1024),
    )


def judge_argv(judge: JudgePlan, port: int, shared_gpu: bool) -> list[str]:
    """The judge server's command, as an argument list: vLLM on loopback, the key from its environment (never a flag)."""
    argv = [
        "vllm", "serve", judge.model,
        "--host", "127.0.0.1", "--port", str(port),
        "--served-model-name", judge.model,
        "--max-model-len", str(judge.max_model_len),
        "--limit-mm-per-prompt", json.dumps({"image": judge.images_per_prompt}),
        "--max-num-seqs", str(judge.max_num_seqs),
    ]
    utilization = judge.gpu_memory_utilization if judge.gpu_memory_utilization is not None else (0.45 if shared_gpu else 0.9)
    argv += ["--gpu-memory-utilization", f"{utilization:.2f}"]
    if judge.revision:
        argv += ["--revision", judge.revision]
    if judge.quantization:
        argv += ["--quantization", judge.quantization]
    return argv


def _text(section: dict[str, Any], name: str, default: str, pattern: re.Pattern[str], expected: str) -> str:
    value = section.get(name, default)
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise ProvisionError("options_invalid", f"{name} must be {expected}")
    return value


def _integer(section: dict[str, Any], name: str, default: int, low: int, high: int) -> int:
    value = section.get(name, default)
    if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
        raise ProvisionError("options_invalid", f"{name} must be an integer between {low} and {high}")
    return value


def _gpu_list(value: Any) -> tuple[str, ...]:
    if not isinstance(value, list) or not value or not all(isinstance(v, str) and GPU_ID.fullmatch(v) for v in value):
        raise ProvisionError("options_invalid", "gpu_prefer must be a non-empty list of GPU type names")
    return tuple(value)
