"""The declared space: room ontology, clutter taxonomy, coverage targets; parsed strictly, sampled with a seeded RNG.

Pure: texts in, typed space out. The image-size check (design/loops.md, "Image size") lives here because the
camera aspects are part of the space.
"""

from __future__ import annotations

import itertools
import random
import tomllib
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Any

from virtual_unstaging.serve.images import output_size

from clutter_pairs.domain import OWNER_KINDS, ItemSpec, OwnerKind, Stage, SubjectSpec, ValueText

ROOM_TYPE, DENSITY, CATEGORY, PLACEMENT, CAMERA = "room_type", "density", "category", "placement", "camera"
ASPECT_RANGE = (0.25, 4.0)  # the tool server's bounds on output_aspect


class SpaceError(ValueError):
    """A space or targets file that does not hold together."""


@dataclass(frozen=True)
class ValueDef:
    name: str
    text: str
    attrs: Mapping[str, Any]


@dataclass(frozen=True)
class AxisDef:
    name: str
    applies_to: OwnerKind
    values: Mapping[str, ValueDef]


@dataclass(frozen=True)
class Space:
    axes: Mapping[str, AxisDef]  # ontology axes first, then taxonomy axes, each in file order
    fixed_text: str
    fixed_by_room: Mapping[str, str]  # the fixed elements of a room type whose elements differ

    def fixed_for(self, room_type: str | None) -> str:
        return self.fixed_by_room.get(room_type or "", self.fixed_text)

    def axes_for(self, kind: OwnerKind) -> tuple[str, ...]:
        return tuple(name for name, axis in self.axes.items() if axis.applies_to == kind)

    def value(self, axis: str, value: str) -> ValueDef:
        try:
            return self.axes[axis].values[value]
        except KeyError:
            raise SpaceError(f"{axis}={value} is not declared") from None

    def pairs(self) -> list[tuple[str, str]]:
        return [(axis.name, v) for axis in self.axes.values() for v in axis.values]


@dataclass(frozen=True)
class Target:
    pairs: int
    cell: tuple[tuple[str, str], ...]  # (axis, value), in the space's axis order


def parse_space(ontology_text: str, taxonomy_text: str) -> Space:
    ontology, taxonomy = _toml(ontology_text, "ontology"), _toml(taxonomy_text, "taxonomy")
    _only(ontology, {"axes"}, "ontology")
    _only(taxonomy, {"axes", "fixed"}, "taxonomy")
    axes: dict[str, AxisDef] = {}
    for source, data in (("ontology", ontology), ("taxonomy", taxonomy)):
        for name, raw in _table(data.get("axes", {}), f"{source} [axes]").items():
            if name in axes:
                raise SpaceError(f"axis {name} is declared twice")
            axes[name] = _axis(name, _table(raw, f"axis {name}"))
    fixed = _table(taxonomy.get("fixed", {}), "taxonomy [fixed]")
    _only(fixed, {"text", "rooms"}, "taxonomy [fixed]")
    by_room = _table(fixed.get("rooms", {}), "taxonomy [fixed.rooms]")
    space = Space(axes, _text(fixed, "text", "taxonomy [fixed]"),
                  {room: _text(by_room, room, "taxonomy [fixed.rooms]") for room in by_room})
    _check_relations(space)
    unknown_rooms = set(by_room) - set(space.axes[ROOM_TYPE].values)
    if unknown_rooms:
        raise SpaceError(f"taxonomy [fixed.rooms]: unknown room types {sorted(unknown_rooms)}")
    return space


def _axis(name: str, raw: dict[str, Any]) -> AxisDef:
    _only(raw, {"applies_to", "values"}, f"axis {name}")
    applies_to = raw.get("applies_to")
    if applies_to not in OWNER_KINDS:
        raise SpaceError(f"axis {name}: applies_to must be one of {OWNER_KINDS}")
    values: dict[str, ValueDef] = {}
    for value, body in _table(raw.get("values", {}), f"axis {name} values").items():
        body = _table(body, f"{name}={value}")
        values[value] = ValueDef(value, _text(body, "text", f"{name}={value}"),
                                 {k: v for k, v in body.items() if k != "text"})
    if not values:
        raise SpaceError(f"axis {name} has no value")
    return AxisDef(name, applies_to, values)


def _check_relations(space: Space) -> None:
    """The attributes the planner and the pixel tests read: camera aspects, density ranges, category relations."""
    for required, kind in ((ROOM_TYPE, "room"), (CAMERA, "scene"), (DENSITY, "clutter_spec"),
                           (CATEGORY, "clutter_item"), (PLACEMENT, "clutter_item")):
        if required not in space.axes or space.axes[required].applies_to != kind:
            raise SpaceError(f"the space needs an axis {required} applying to {kind}")
    for value in space.axes[CAMERA].values.values():
        aspect = value.attrs.get("aspect")
        if not isinstance(aspect, (int, float)) or isinstance(aspect, bool) or not ASPECT_RANGE[0] <= aspect <= ASPECT_RANGE[1]:
            raise SpaceError(f"camera={value.name}: aspect must be a number in {ASPECT_RANGE}")
    for value in space.axes[DENSITY].values.values():
        items: Any = value.attrs.get("items")
        share: Any = value.attrs.get("mask_share")
        if not _range(items, int) or items[0] < 1:
            raise SpaceError(f"density={value.name}: items must be [min, max], 1 <= min <= max")
        if not _range(share, float) or not 0 <= share[0] < share[1] <= 1:
            raise SpaceError(f"density={value.name}: mask_share must be [min, max] in [0, 1]")
    rooms, placements = set(space.axes[ROOM_TYPE].values), set(space.axes[PLACEMENT].values)
    for value in space.axes[CATEGORY].values.values():
        fits, takes = value.attrs.get("rooms"), value.attrs.get("placements")
        if not isinstance(fits, list) or not fits or not set(fits) <= rooms:
            raise SpaceError(f"category={value.name}: rooms must be a non-empty list of room types")
        if not isinstance(takes, list) or not takes or not set(takes) <= placements:
            raise SpaceError(f"category={value.name}: placements must be a non-empty list of placements")
    for value in space.axes[PLACEMENT].values.values():
        if not isinstance(value.attrs.get("rule"), str):
            raise SpaceError(f"placement={value.name}: a rule text is required")
    for room in rooms:
        if not any(room in c.attrs["rooms"] for c in space.axes[CATEGORY].values.values()):
            raise SpaceError(f"room_type={room}: no category fits it")


def parse_targets(text: str, space: Space) -> tuple[Target, ...]:
    data = _toml(text, "targets")
    _only(data, {"cross", "target"}, "targets")
    order = list(space.axes)
    cells: dict[tuple[tuple[str, str], ...], int] = {}
    for kind in ("cross", "target"):
        entries = data.get(kind, [])
        if not isinstance(entries, list):
            raise SpaceError(f"targets: [[{kind}]] must be an array of tables")
        for entry in entries:
            entry = _table(entry, f"targets [[{kind}]]")
            pairs = entry.get("pairs")
            if not isinstance(pairs, int) or isinstance(pairs, bool) or pairs < 1:
                raise SpaceError(f"targets [[{kind}]]: pairs must be a positive integer")
            axes = sorted((k for k in entry if k != "pairs"), key=lambda a: order.index(a) if a in order else -1)
            lists = [entry[a] if kind == "cross" else [entry[a]] for a in axes]
            for combo in itertools.product(*lists):
                cell = tuple(zip(axes, combo, strict=True))
                for axis, value in cell:
                    space.value(axis, str(value))
                    if space.axes[axis].applies_to == "clutter_item":
                        raise SpaceError(f"targets: {axis} applies to clutter items; a cell names room, scene or "
                                         "clutter spec axes")
                if cell in cells:
                    raise SpaceError(f"targets: cell {cell} is named twice")
                cells[cell] = pairs
    if not cells:
        raise SpaceError("targets: no cell")
    return tuple(Target(pairs, cell) for cell, pairs in cells.items())


# --- The image-size check ------------------------------------------------------------------------------------


def size_for_aspect(aspect: float, side: int, multiple: int) -> tuple[int, int]:
    """The size the tool server gives an image made from text alone at this aspect (its own rule)."""
    return output_size((round(aspect * 1000), 1000), side, multiple)


def check_sizes(space: Space, side: int, multiple: int, condition_max_pixels: int) -> dict[str, tuple[int, int]]:
    """Each camera's clean image size, checked: edited at the same `side`, it comes back at the same size (a fixed
    point of the sizing rule), and the editor sees it unscaled (within its condition-image limit)."""
    sizes: dict[str, tuple[int, int]] = {}
    for value in space.axes[CAMERA].values.values():
        size = size_for_aspect(float(value.attrs["aspect"]), side, multiple)
        edited = output_size(size, side, multiple)
        if edited != size:
            raise SpaceError(f"camera={value.name}: an image of {size[0]}x{size[1]} edited at output_side {side} comes "
                             f"back at {edited[0]}x{edited[1]}; choose another aspect or output_side")
        if size[0] * size[1] > condition_max_pixels:
            raise SpaceError(f"camera={value.name}: {size[0]}x{size[1]} exceeds the editor's condition-image limit "
                             f"of {condition_max_pixels} pixels; lower output_side")
        sizes[value.name] = size
    return sizes


# --- Sampling ------------------------------------------------------------------------------------------------


def sample_values(space: Space, kind: OwnerKind, fixed: Mapping[str, str], rng: random.Random,
                  allowed: Mapping[str, Iterable[str]] | None = None) -> dict[str, str]:
    """One value per axis of `kind`: the fixed one when given, otherwise drawn among the allowed (default: all)."""
    values: dict[str, str] = {}
    for axis in space.axes_for(kind):
        if axis in fixed:
            space.value(axis, fixed[axis])
            values[axis] = fixed[axis]
        else:
            choices = sorted((allowed or {}).get(axis, space.axes[axis].values))
            values[axis] = rng.choice(choices)
    return values


def sample_items(space: Space, room_type: str, density: str, rng: random.Random) -> list[dict[str, str]]:
    """The items of one clutter spec: their count from the density, each a category fitting the room and one of its
    placements; other item axes drawn freely."""
    low, high = space.value(DENSITY, density).attrs["items"]
    categories = sorted(c.name for c in space.axes[CATEGORY].values.values() if room_type in c.attrs["rooms"])
    items: list[dict[str, str]] = []
    for _ in range(rng.randint(low, high)):
        category = rng.choice(categories)
        placement = rng.choice(sorted(space.value(CATEGORY, category).attrs["placements"]))
        items.append(sample_values(space, "clutter_item", {CATEGORY: category, PLACEMENT: placement}, rng))
    return items


def mask_share_range(space: Space, density: str) -> tuple[float, float]:
    low, high = space.value(DENSITY, density).attrs["mask_share"]
    return float(low), float(high)


def camera_aspect(space: Space, camera: str) -> float:
    return float(space.value(CAMERA, camera).attrs["aspect"])


def subject_spec(space: Space, stage: Stage, values: Iterable[tuple[str, str]],
                 items: Iterable[Iterable[tuple[str, str]]] = ()) -> SubjectSpec:
    """The subject as the spec renderer receives it: values in the space's axis order with their texts; for a
    clutter loop, its items and the placement rules they invoke; the fixed elements in both stages."""
    order = list(space.axes)
    texts = tuple(ValueText(a, v, space.value(a, v).text) for a, v in sorted(values, key=lambda p: order.index(p[0])))
    item_specs = tuple(
        ItemSpec(n, tuple(ValueText(a, v, space.value(a, v).text) for a, v in sorted(item, key=lambda p: order.index(p[0]))))
        for n, item in enumerate(items, start=1)
    )
    rules = [space.fixed_for(next((v.value for v in texts if v.axis == ROOM_TYPE), None))]
    if stage == "clutter":
        for item in item_specs:
            for v in item.values:
                if v.axis == PLACEMENT:
                    rule = str(space.value(PLACEMENT, v.value).attrs["rule"])
                    if rule not in rules:
                        rules.append(rule)
    return SubjectSpec(stage, texts, item_specs, tuple(rules))


# --- Parsing helpers -----------------------------------------------------------------------------------------


def _toml(text: str, what: str) -> dict[str, Any]:
    try:
        return tomllib.loads(text)
    except tomllib.TOMLDecodeError as error:
        raise SpaceError(f"{what}: {error}") from None


def _table(value: object, where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SpaceError(f"{where}: expected a table")
    return value


def _only(data: Mapping[str, Any], keys: set[str], where: str) -> None:
    unknown = set(data) - keys
    if unknown:
        raise SpaceError(f"{where}: unknown keys {sorted(unknown)}")


def _text(data: Mapping[str, Any], key: str, where: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise SpaceError(f"{where}: {key} must be a non-empty text")
    return value


def _range(value: object, kind: type) -> bool:
    if not isinstance(value, list) or len(value) != 2:
        return False
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in value):
        return False
    if kind is int and not all(isinstance(v, int) for v in value):
        return False
    return bool(value[0] <= value[1])
