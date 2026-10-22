"""Generator recipes: one TOML file says how a model's pipeline is loaded, fed and set, so the adapter stays generic."""

from __future__ import annotations

import hashlib
import json
import math
import re
import tomllib
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from virtual_unstaging.domain import ROLES, JsonScalar
from virtual_unstaging.serve.errors import ApiError, ServeConfigError

RECIPE_DIR = Path(__file__).parent / "recipes"
ADAPTERS = ("diffusers", "fake")
DTYPES = ("bfloat16", "float16", "float32")
PLACEMENTS = ("cuda", "model_cpu_offload")
IMAGE_PASSING = ("list", "single_when_one")
OUTPUT_SIDE_SETTING = "output_side"  # adapter-level: about side x side pixels for the output
OUTPUT_SIDE_RANGE = (256, 2048)
CONDITION_SIDE_SETTING = "condition_side"  # adapter-level: condition images reduced to about side x side; 0 = as given
OUTPUT_ASPECT_SETTING = "output_aspect"  # adapter-level, text-only recipes: width / height of an output made from text alone
OUTPUT_ASPECT_RANGE = (0.25, 4.0)
# The adapter's own settings, never passed to the pipeline.
ADAPTER_SETTINGS = (OUTPUT_SIDE_SETTING, CONDITION_SIDE_SETTING, OUTPUT_ASPECT_SETTING)

_NAME = re.compile(r"^[a-z][a-z0-9_]{0,63}$")
_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
_REPOSITORY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*$")
_REVISION = re.compile(r"^[0-9a-f]{40}$")
UNPINNED = "unpinned"

# Recipe fields (flat names) that a recipe may list as unverified.
FIELDS = (
    "pipeline_class", "repository", "revision", "dtype", "placement", "fp8_storage", "lora", "scheduler", "roles",
    "max_images", "native_mask", "text_only",
    "mask_argument", "max_images_with_native_mask", "image_argument", "image_passing", "prompt_argument",
    "seed_argument", "output_side", "output_multiple", "width_argument", "height_argument", "steps_argument",
    "defaults", "licence",
)

_TOP_KEYS = {"name", "adapter", "licence", "unverified", "notes", "pipeline", "inputs", "output", "settings"}
_PIPELINE_KEYS = {"class", "repository", "revision", "dtype", "placement", "fp8_storage", "lora", "scheduler",
                  "scheduler_none"}
_LORA_KEYS = {"repository", "revision", "weight_name", "scale"}
_WEIGHT_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}\.safetensors$")
_INPUTS_KEYS = {
    "roles", "max_images", "native_mask", "mask_argument", "max_images_with_native_mask", "image_argument",
    "image_passing", "prompt_argument", "seed_argument", "text_only",
}
_OUTPUT_KEYS = {"side", "multiple", "width_argument", "height_argument"}
_SETTINGS_KEYS = {"steps_argument", "defaults"}


@dataclass(frozen=True)
class Lora:
    """Adapter weights fused into the pipeline at load (a step-distillation LoRA, for instance)."""

    repository: str
    revision: str
    weight_name: str
    scale: float = 1.0


@dataclass(frozen=True)
class Recipe:
    name: str
    adapter: str
    licence: str
    pipeline_class: str
    repository: str
    revision: str
    dtype: str
    placement: str
    fp8_storage: tuple[str, ...]
    lora: Lora | None
    scheduler: Mapping[str, JsonScalar | None]  # overrides of the pipeline scheduler's configuration
    roles: tuple[str, ...]
    max_images: int
    native_mask: bool
    mask_argument: str
    max_images_with_native_mask: int | None
    image_argument: str
    image_passing: str
    prompt_argument: str
    seed_argument: str
    output_side: int
    output_multiple: int
    width_argument: str
    height_argument: str
    steps_argument: str
    defaults: Mapping[str, JsonScalar]
    unverified: tuple[str, ...] = ()
    notes: tuple[str, ...] = field(default=())
    text_only: bool = False  # the pipeline also makes an image from the prompt alone, called without its image argument

    def profile(self) -> dict[str, Any]:
        """The generator's capability profile as `GET /capabilities` reports it."""
        profile: dict[str, Any] = {
            "model": self.repository,
            "revision": self.weights_revision(),
            "max_images": self.max_images,
            "roles": list(self.roles),
            "native_mask": self.native_mask,
            "text_only": self.text_only,
            "settings": self.adapter_defaults(),
            "licence": self.licence,
            "recipe": self.name,
            "unverified": list(self.unverified),
        }
        if self.native_mask and self.max_images_with_native_mask is not None:
            profile["max_images_with_native_mask"] = self.max_images_with_native_mask
        return profile

    def weights_revision(self) -> str:
        """The revision of the weights as run: the commit, marked by whatever changes the images (an adapter fused,
        a scheduler changed, components stored in FP8)."""
        revision = self.revision
        if self.lora is not None:
            revision += f"+lora:{self.lora.weight_name}@{self.lora.revision[:12]}x{self.lora.scale:g}"
        if self.scheduler:
            digest = hashlib.sha256(json.dumps(dict(self.scheduler), sort_keys=True).encode()).hexdigest()[:8]
            revision += f"+scheduler:{digest}"
        if self.fp8_storage:
            revision += f"+fp8:{','.join(self.fp8_storage)}"
        return revision

    def adapter_defaults(self) -> dict[str, JsonScalar]:
        """Every settable name with its default: the pipeline's, then the adapter's own."""
        defaults: dict[str, JsonScalar] = {**self.defaults, OUTPUT_SIDE_SETTING: self.output_side, CONDITION_SIDE_SETTING: 0}
        if self.text_only:
            defaults[OUTPUT_ASPECT_SETTING] = 1.0
        return defaults

    def settings_for(self, requested: Mapping[str, JsonScalar]) -> dict[str, JsonScalar]:
        """Defaults overridden by the request's settings; unknown names and out-of-range values are rejected."""
        merged = self.adapter_defaults()
        for name, value in requested.items():
            if name not in merged:
                allowed = ", ".join(sorted(merged))
                raise ApiError("bad_request", f"unknown setting {name!r} for recipe {self.name} (allowed: {allowed})")
            merged[name] = check_setting(name, value, merged[name])
        return merged


def check_setting(name: str, value: object, default: JsonScalar) -> JsonScalar:
    """A setting value of the same kind as its default, inside a bounded range."""
    if name == OUTPUT_ASPECT_SETTING:
        low_ratio, high_ratio = OUTPUT_ASPECT_RANGE
        if (isinstance(value, bool) or not isinstance(value, int | float) or not math.isfinite(value)
                or not low_ratio <= value <= high_ratio):
            raise ApiError("bad_request", f"setting {name} must be a number in [{low_ratio}, {high_ratio}] (width / height)")
        return float(value)
    if name in ADAPTER_SETTINGS:
        low, high = OUTPUT_SIDE_RANGE
        zero = name == CONDITION_SIDE_SETTING and value == 0
        if isinstance(value, bool) or not isinstance(value, int) or not (zero or low <= value <= high):
            raise ApiError("bad_request", f"setting {name} must be an integer in [{low}, {high}]" + (" or 0" if name == CONDITION_SIDE_SETTING else ""))
        return value
    if isinstance(default, bool):
        if not isinstance(value, bool):
            raise ApiError("bad_request", f"setting {name} must be true or false")
        return value
    if isinstance(default, int):
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 1000:
            raise ApiError("bad_request", f"setting {name} must be an integer in [1, 1000]")
        return value
    if isinstance(default, float):
        if isinstance(value, bool) or not isinstance(value, int | float) or not math.isfinite(value) or not 0 <= value <= 100:
            raise ApiError("bad_request", f"setting {name} must be a number in [0, 100]")
        return float(value)
    if not isinstance(value, str) or len(value) > 2000:
        raise ApiError("bad_request", f"setting {name} must be a text of at most 2000 characters")
    return value


def available_recipes() -> list[str]:
    return sorted(path.stem for path in RECIPE_DIR.glob("*.toml"))


def load_recipe(spec: str) -> Recipe:
    """A recipe by packaged name (see `available_recipes`) or by path of a TOML file."""
    if _NAME.fullmatch(spec) and (RECIPE_DIR / f"{spec}.toml").is_file():
        path = RECIPE_DIR / f"{spec}.toml"
    elif spec.endswith(".toml") and Path(spec).is_file():
        path = Path(spec)
    else:
        raise ServeConfigError(f"unknown recipe {spec!r}; packaged recipes: {', '.join(available_recipes())}")
    return parse_recipe(path.read_text(encoding="utf-8"), source=str(path))


def parse_recipe(text: str, source: str = "recipe") -> Recipe:
    try:
        raw = tomllib.loads(text)
    except tomllib.TOMLDecodeError as error:
        raise ServeConfigError(f"{source}: not valid TOML ({error})") from None
    try:
        return _build(raw)
    except (KeyError, TypeError, ValueError) as error:
        raise ServeConfigError(f"{source}: {error.args[0] if isinstance(error, KeyError) else error}") from None


def _table(raw: Mapping[str, Any], key: str, allowed: set[str]) -> Mapping[str, Any]:
    table = raw.get(key)
    if not isinstance(table, dict):
        raise ValueError(f"missing table [{key}]")
    unknown = set(table) - allowed
    if unknown:
        raise ValueError(f"unknown keys in [{key}]: {', '.join(sorted(unknown))}")
    return table


def _text(table: Mapping[str, Any], key: str, pattern: re.Pattern[str] | None = None, optional: bool = False) -> str:
    value = table.get(key, "" if optional else None)
    if not isinstance(value, str) or (not optional and not value):
        raise ValueError(f"{key} must be a text")
    if value and pattern is not None and not pattern.fullmatch(value):
        raise ValueError(f"{key} {value!r} is not valid")
    return value


def _integer(table: Mapping[str, Any], key: str, low: int, high: int) -> int:
    value = table.get(key)
    if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
        raise ValueError(f"{key} must be an integer in [{low}, {high}]")
    return value


def _lora(raw: object) -> Lora | None:
    if raw is None:
        return None
    if not isinstance(raw, dict) or set(raw) - _LORA_KEYS:
        raise ValueError(f"[pipeline.lora] takes only {', '.join(sorted(_LORA_KEYS))}")
    revision = _text(raw, "revision", _REVISION)
    scale = raw.get("scale", 1.0)
    if isinstance(scale, bool) or not isinstance(scale, int | float) or not 0 < scale <= 4:
        raise ValueError("[pipeline.lora] scale must be a number in (0, 4]")
    return Lora(_text(raw, "repository", _REPOSITORY), revision, _text(raw, "weight_name", _WEIGHT_NAME), float(scale))


def _scheduler(raw: object, unset: object) -> dict[str, JsonScalar | None]:
    """Scheduler configuration overrides; `scheduler_none` lists keys set to None (TOML has no null)."""
    overrides: dict[str, JsonScalar | None] = {}
    if raw is not None:
        if not isinstance(raw, dict):
            raise ValueError("[pipeline.scheduler] must be a table")
        for key, value in raw.items():
            if not _IDENTIFIER.fullmatch(key) or not isinstance(value, str | int | float | bool):
                raise ValueError(f"scheduler setting {key!r} is not valid")
            overrides[key] = value
    if unset is not None:
        if not isinstance(unset, list) or not all(isinstance(k, str) and _IDENTIFIER.fullmatch(k) for k in unset):
            raise ValueError("scheduler_none must list scheduler setting names")
        overrides.update({key: None for key in unset})
    return overrides


def _build(raw: Mapping[str, Any]) -> Recipe:
    unknown = set(raw) - _TOP_KEYS
    if unknown:
        raise ValueError(f"unknown keys: {', '.join(sorted(unknown))}")
    name = _text(raw, "name", _NAME)
    adapter = _text(raw, "adapter")
    if adapter not in ADAPTERS:
        raise ValueError(f"adapter must be one of {ADAPTERS}")
    pipeline = _table(raw, "pipeline", _PIPELINE_KEYS)
    inputs = _table(raw, "inputs", _INPUTS_KEYS)
    output = _table(raw, "output", _OUTPUT_KEYS)
    settings = _table(raw, "settings", _SETTINGS_KEYS)

    revision = _text(pipeline, "revision")
    if revision != UNPINNED and not _REVISION.fullmatch(revision) and adapter == "diffusers":
        raise ValueError(f"revision must be a 40-character commit or {UNPINNED!r}")
    dtype, placement = _text(pipeline, "dtype"), _text(pipeline, "placement")
    if dtype not in DTYPES or placement not in PLACEMENTS:
        raise ValueError(f"dtype must be one of {DTYPES} and placement one of {PLACEMENTS}")
    lora = _lora(pipeline.get("lora"))
    scheduler = _scheduler(pipeline.get("scheduler"), pipeline.get("scheduler_none"))
    fp8_storage = pipeline.get("fp8_storage", [])
    if (not isinstance(fp8_storage, list) or len(fp8_storage) > 8 or len(set(fp8_storage)) != len(fp8_storage)
            or not all(isinstance(c, str) and _IDENTIFIER.fullmatch(c) for c in fp8_storage)):
        raise ValueError("fp8_storage must list distinct pipeline component names (at most 8)")

    roles = inputs.get("roles")
    if not isinstance(roles, list) or not roles or not all(r in ROLES for r in roles) or "original" not in roles:
        raise ValueError(f"roles must be a list drawn from {ROLES} that includes 'original'")
    max_images = _integer(inputs, "max_images", 1, 32)
    native_mask = inputs.get("native_mask")
    if not isinstance(native_mask, bool):
        raise ValueError("native_mask must be true or false")
    mask_argument = _text(inputs, "mask_argument", _IDENTIFIER, optional=True)
    if native_mask and (not mask_argument or "removal_mask" not in roles):
        raise ValueError("native_mask needs a mask_argument and the removal_mask role")
    if not native_mask and mask_argument:
        raise ValueError("mask_argument is set but native_mask is false")
    with_mask = inputs.get("max_images_with_native_mask")
    if with_mask is not None:
        if not native_mask:
            raise ValueError("max_images_with_native_mask needs native_mask")
        with_mask = _integer(inputs, "max_images_with_native_mask", 1, max_images)
    image_passing = _text(inputs, "image_passing")
    if image_passing not in IMAGE_PASSING:
        raise ValueError(f"image_passing must be one of {IMAGE_PASSING}")
    text_only = inputs.get("text_only", False)
    if not isinstance(text_only, bool):
        raise ValueError("text_only must be true or false")

    defaults = settings.get("defaults")
    if not isinstance(defaults, dict):
        raise ValueError("missing table [settings.defaults]")
    for key, value in defaults.items():
        if not _IDENTIFIER.fullmatch(key) or key in ADAPTER_SETTINGS or not isinstance(value, str | int | float | bool):
            raise ValueError(f"setting {key!r} is not a valid default")
    steps_argument = _text(settings, "steps_argument", _IDENTIFIER)
    if steps_argument not in defaults:
        raise ValueError("steps_argument must name one of the default settings")

    unverified = raw.get("unverified", [])
    if not isinstance(unverified, list) or not all(item in FIELDS for item in unverified):
        raise ValueError(f"unverified must list recipe fields among {FIELDS}")
    notes = raw.get("notes", [])
    if not isinstance(notes, list) or not all(isinstance(note, str) for note in notes):
        raise ValueError("notes must be a list of texts")

    return Recipe(
        name=name,
        adapter=adapter,
        licence=_text(raw, "licence"),
        pipeline_class=_text(pipeline, "class", re.compile(r"^[A-Za-z][A-Za-z0-9]*$")),
        repository=_text(pipeline, "repository", _REPOSITORY),
        revision=revision,
        dtype=dtype,
        placement=placement,
        fp8_storage=tuple(fp8_storage),
        lora=lora,
        scheduler=scheduler,
        roles=tuple(roles),
        max_images=max_images,
        native_mask=native_mask,
        mask_argument=mask_argument,
        max_images_with_native_mask=with_mask,
        image_argument=_text(inputs, "image_argument", _IDENTIFIER),
        image_passing=image_passing,
        prompt_argument=_text(inputs, "prompt_argument", _IDENTIFIER),
        seed_argument=_text(inputs, "seed_argument", _IDENTIFIER),
        output_side=_integer(output, "side", *OUTPUT_SIDE_RANGE),
        output_multiple=_integer(output, "multiple", 1, 256),
        width_argument=_text(output, "width_argument", _IDENTIFIER),
        height_argument=_text(output, "height_argument", _IDENTIFIER),
        steps_argument=steps_argument,
        defaults=dict(defaults),
        unverified=tuple(unverified),
        notes=tuple(notes),
        text_only=text_only,
    )
