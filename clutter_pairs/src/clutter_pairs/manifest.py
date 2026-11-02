"""An import set's manifest: JSON Lines, one image per line, parsed strictly against the declared space
(design/imports.md, "Manifest line"). Pure: text in, typed entries out."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any

from clutter_pairs.domain import ModelId
from clutter_pairs.space import ROOM_TYPE, Space

MANIFEST_NAME = "manifest.jsonl"
_KEYS = {"file", "room_type", "source", "values", "origin", "group"}
_SOURCE_KEYS = ("name", "revision", "family", "licence")


class ManifestError(ValueError):
    """A manifest that cannot be imported; the message names the line."""


@dataclass(frozen=True)
class ImportEntry:
    line: int  # 1-based, in the manifest file
    file: str  # relative to the import folder
    room_type: str
    source: ModelId
    values: tuple[tuple[str, str], ...]  # the other room and scene axes the manifest gives, sorted by axis
    origin: str | None
    group: str | None  # views of one room share a group: one building, one room, a scene per view


def parse_manifest(text: str, space: Space) -> list[ImportEntry]:
    """Every entry of a manifest (blank lines skipped); a file named twice is an error."""
    entries: list[ImportEntry] = []
    seen: dict[str, int] = {}
    for number, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip():
            continue
        entry = parse_entry(number, raw, space)
        if entry.file in seen:
            raise ManifestError(f"line {number}: {entry.file} is already listed on line {seen[entry.file]}")
        seen[entry.file] = number
        entries.append(entry)
    if not entries:
        raise ManifestError("the manifest lists no image")
    return entries


def parse_entry(number: int, raw: str, space: Space) -> ImportEntry:
    """One manifest line: file, room_type and source are required; values and origin optional."""
    where = f"line {number}"
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ManifestError(f"{where}: not JSON ({error})") from None
    if not isinstance(data, dict):
        raise ManifestError(f"{where}: expected an object")
    unknown = set(data) - _KEYS
    if unknown:
        raise ManifestError(f"{where}: unknown keys {sorted(unknown)}")
    file = _text(data, "file", where)
    path = PurePosixPath(file)
    if path.is_absolute() or ".." in path.parts or file.endswith("/"):
        raise ManifestError(f"{where}: file {file!r} must be a relative path inside the import folder")
    room_type = _text(data, "room_type", where)
    if room_type not in space.axes[ROOM_TYPE].values:
        raise ManifestError(f"{where}: room_type {room_type!r} is not declared; declared: "
                            f"{sorted(space.axes[ROOM_TYPE].values)}")
    source = data.get("source")
    if not isinstance(source, dict) or set(source) != set(_SOURCE_KEYS):
        raise ManifestError(f"{where}: source must be an object with exactly {list(_SOURCE_KEYS)}")
    model = ModelId(*(_text(source, key, f"{where} source") for key in _SOURCE_KEYS))
    origin = data.get("origin")
    if origin is not None and not isinstance(origin, str):
        raise ManifestError(f"{where}: origin must be a text")
    group = data.get("group")
    if group is not None:
        group = _text(data, "group", where)
    return ImportEntry(number, file, room_type, model, _values(data.get("values", {}), space, where), origin, group)


def _values(raw: Any, space: Space, where: str) -> tuple[tuple[str, str], ...]:
    if not isinstance(raw, dict):
        raise ManifestError(f"{where}: values must be an object of axis to value")
    out: list[tuple[str, str]] = []
    for axis, value in raw.items():
        if axis == ROOM_TYPE:
            raise ManifestError(f"{where}: room_type is a key of the line, not one of its values")
        if axis not in space.axes or space.axes[axis].applies_to not in ("room", "scene"):
            raise ManifestError(f"{where}: values name room or scene axes; {axis!r} is not one")
        if not isinstance(value, str) or value not in space.axes[axis].values:
            raise ManifestError(f"{where}: {axis}={value!r} is not declared; declared: {sorted(space.axes[axis].values)}")
        out.append((axis, value))
    return tuple(sorted(out))


def _text(data: dict[str, Any], key: str, where: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{where}: {key} must be a non-empty text")
    return value
