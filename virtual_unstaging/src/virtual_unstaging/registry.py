"""Dimension registry: parse and validate the registry and defect files, prune levels a generator cannot take."""

from __future__ import annotations

import tomllib
from collections.abc import Mapping, Sequence
from dataclasses import replace
from importlib import resources
from pathlib import Path
from typing import Any, cast

from virtual_unstaging.domain import (
    INPUTS,
    REALIZERS,
    ROLES,
    DefectStep,
    DefectType,
    Dimension,
    GeneratorCapabilities,
    Input,
    JsonScalar,
    Level,
    Realizer,
    Release,
    Role,
    canonical_json,
    sha256_text,
)

# Per realizer: the realizer-specific dimension field, and the fields and types of each level.
_LEVEL_FIELDS: dict[str, dict[str, type | tuple[type, ...]]] = {
    "text_slot": {"text": str},
    "reference_count": {"count": int},
    "mask_dilation": {"dilation_pct": (int, float)},
    "guide_toggle": {"on": bool},
    "setting": {"value": (int, float, str)},
}
_DIMENSION_FIELD = {"text_slot": "slot", "guide_toggle": "role", "setting": "setting"}
_DIMENSION_KEYS = {"key", "input", "realizer", "default", "targets", "levels", "probe_cost", "slot", "role", "setting"}


class RegistryError(ValueError):
    pass


def read_text_resource(name: str) -> str:
    return resources.files("virtual_unstaging.data").joinpath(name).read_text(encoding="utf-8")


def load_defects(text: str | None = None) -> tuple[DefectType, ...]:
    data = tomllib.loads(text if text is not None else read_text_resource("defects.toml"))
    _only_keys(data, {"defect"}, "defects file")
    defects: list[DefectType] = []
    for entry in data["defect"]:
        _only_keys(entry, {"code", "label", "description"}, "defect")
        defects.append(DefectType(_str(entry, "code"), _str(entry, "label"), _str(entry, "description")))
    codes = [d.code for d in defects]
    if len(set(codes)) != len(codes):
        raise RegistryError("duplicate defect codes")
    return tuple(defects)


def load_release(defects: Sequence[DefectType], text: str | None = None, path: Path | None = None) -> Release:
    """Parse a registry file into a release; every reference (defect, dimension, level) must resolve."""
    if text is None:
        text = path.read_text(encoding="utf-8") if path else read_text_resource("registry.toml")
    data = tomllib.loads(text)
    _only_keys(data, {"dimension", "defect_steps"}, "registry")
    codes = {d.code for d in defects}
    dimensions = tuple(_parse_dimension(entry, codes) for entry in data.get("dimension", []))
    keys = [d.key for d in dimensions]
    if len(set(keys)) != len(keys):
        raise RegistryError("duplicate dimension keys")
    by_key = {d.key: d for d in dimensions}
    steps: list[DefectStep] = []
    for entry in data.get("defect_steps", []):
        _only_keys(entry, {"defect", "dimension", "direction", "priority"}, "defect step")
        step = DefectStep(_str(entry, "defect"), _str(entry, "dimension"), _int(entry, "direction"), _int(entry, "priority"))
        if step.defect not in codes:
            raise RegistryError(f"defect step names unknown defect {step.defect!r}")
        if step.dimension not in by_key:
            raise RegistryError(f"defect step names unknown dimension {step.dimension!r}")
        if step.direction not in (-1, 1) or step.priority < 1:
            raise RegistryError(f"invalid direction or priority in {entry}")
        steps.append(step)
    identity = canonical_json({"dimensions": [d.definition() for d in dimensions],
                               "defect_steps": [vars(s) for s in steps]})
    return Release(dimensions, tuple(steps), sha256_text(identity))


def _parse_dimension(entry: Mapping[str, Any], codes: set[str]) -> Dimension:
    _only_keys(entry, _DIMENSION_KEYS, "dimension")
    key, input_, realizer = _str(entry, "key"), _str(entry, "input"), _str(entry, "realizer")
    if input_ not in INPUTS:
        raise RegistryError(f"{key}: unknown input {input_!r}")
    if realizer not in REALIZERS:
        raise RegistryError(f"{key}: unknown realizer {realizer!r}")
    fields = _LEVEL_FIELDS[realizer]
    raw_levels = entry.get("levels")
    if not isinstance(raw_levels, list) or not 2 <= len(raw_levels) <= 4:
        raise RegistryError(f"{key}: a dimension has two to four levels")
    levels: list[Level] = []
    for ordinal, raw in enumerate(raw_levels):
        _only_keys(raw, {"label", *fields}, f"level of {key}")
        realization: dict[str, JsonScalar] = {}
        for name, kind in fields.items():
            value = raw.get(name)
            if value is None or not isinstance(value, kind) or (kind is int and isinstance(value, bool)):
                raise RegistryError(f"{key}: level {ordinal} needs {name!r} of type {kind}")
            realization[name] = cast(JsonScalar, value)
        levels.append(Level(ordinal, _str(raw, "label"), realization))
    labels = [lv.label for lv in levels]
    if len(set(labels)) != len(labels):
        raise RegistryError(f"{key}: duplicate level labels")
    default = _str(entry, "default")
    if default not in labels:
        raise RegistryError(f"{key}: default {default!r} is not a level")
    targets = tuple(entry.get("targets", ()))
    unknown = [t for t in targets if t not in codes]
    if unknown:
        raise RegistryError(f"{key}: unknown target defects {unknown}")
    extra: dict[str, str | None] = {"slot": None, "role": None, "setting": None}
    special = _DIMENSION_FIELD.get(realizer)
    for name in extra:
        if name == special:
            extra[name] = _str(entry, name)
        elif name in entry:
            raise RegistryError(f"{key}: {name!r} does not apply to realizer {realizer}")
    if extra["role"] is not None and extra["role"] not in ROLES:
        raise RegistryError(f"{key}: unknown role {extra['role']!r}")
    probe_cost = entry.get("probe_cost", 0.0)
    if not isinstance(probe_cost, (int, float)) or probe_cost < 0:
        raise RegistryError(f"{key}: probe_cost must be a non-negative number")
    return Dimension(
        key=key,
        input=cast(Input, input_),
        realizer=cast(Realizer, realizer),
        levels=tuple(levels),
        default_ordinal=labels.index(default),
        probe_cost=float(probe_cost),
        targets=targets,
        slot=extra["slot"],
        role=cast(Role | None, extra["role"]),
        setting=extra["setting"],
    )


def prune(release: Release, capabilities: GeneratorCapabilities) -> tuple[Dimension, ...]:
    """Drop the levels a generator cannot take; drop a dimension left with one level.

    Only the highest levels of a dimension are ever dropped, so ordinals stay those of the registry.
    """
    protected_possible = any(d.realizer == "guide_toggle" and d.role == "protected_mask" for d in release.dimensions)
    reference_slots = capabilities.max_images - 1 - capabilities.images_used_by_guides(protected_possible)
    kept: list[Dimension] = []
    for dim in release.dimensions:
        levels = dim.levels
        if dim.realizer == "reference_count":
            if "reference" not in capabilities.roles:
                reference_slots = 0
            levels = tuple(lv for lv in levels if int(lv.realization["count"]) <= max(reference_slots, 0))
        elif dim.realizer == "guide_toggle" and (dim.role not in capabilities.roles):
            levels = tuple(lv for lv in levels if not lv.realization["on"])
        elif dim.realizer == "mask_dilation" and "removal_mask" not in capabilities.roles:
            levels = levels[:1]
        if [lv.ordinal for lv in levels] != list(range(len(levels))):
            raise RegistryError(f"{dim.key}: pruning would leave non-contiguous levels")
        if len(levels) < 2:
            continue
        default = min(dim.default_ordinal, len(levels) - 1)
        kept.append(replace(dim, levels=levels, default_ordinal=default))
    return tuple(kept)


def _only_keys(entry: Mapping[str, Any], allowed: set[str], what: str) -> None:
    unknown = set(entry) - allowed
    if unknown:
        raise RegistryError(f"{what}: unknown keys {sorted(unknown)}")


def _str(entry: Mapping[str, Any], name: str) -> str:
    value = entry.get(name)
    if not isinstance(value, str) or not value:
        raise RegistryError(f"{name!r} must be a non-empty string in {dict(entry)}")
    return value


def _int(entry: Mapping[str, Any], name: str) -> int:
    value = entry.get(name)
    if not isinstance(value, int) or isinstance(value, bool):
        raise RegistryError(f"{name!r} must be an integer in {dict(entry)}")
    return value
