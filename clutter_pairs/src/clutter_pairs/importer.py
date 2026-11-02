"""Import: a folder of images and a manifest becomes scenes with their clean image and their clutter specs
(design/imports.md).

One scene per image, with the values the manifest gives; views of one room (a shared `group`) share one room and one
building, any other image has its own. The image is made opaque RGB and resized to the size the editor returns at the
run's `output_side`; the original is kept with its hash; the K clutter specs are planned as for a generated scene.
Validated whole before anything is written, written in one transaction.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from virtual_unstaging import imaging
from virtual_unstaging.domain import sha256_bytes

from clutter_pairs.dataset import Dataset
from clutter_pairs.domain import ModelId, derive_seed
from clutter_pairs.manifest import MANIFEST_NAME, ImportEntry, ManifestError, parse_manifest
from clutter_pairs.sizing import RESAMPLER, opaque_rgb, pixel_sha, resized
from clutter_pairs.space import ROOM_TYPE, SpaceError, imported_size, sample_clutter_specs
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction, utc_now

MAX_PROBLEMS_SHOWN = 20
GroupKey = tuple[str, str, str]  # source name, source revision, group


@dataclass(frozen=True)
class ImportSummary:
    import_set_id: int | None  # none when every image was already imported
    scenes: int
    buildings: int  # new buildings: a group is one
    specs: int
    skipped: tuple[str, ...]  # files whose picture is already in the dataset


@dataclass(frozen=True)
class Prepared:
    """An entry that passed validation, with what the write needs to recognise the same file again."""

    entry: ImportEntry
    original_sha: str
    pixel_sha: str
    image_sha: str  # the resized image's
    size: tuple[int, int]


def import_folder(ds: Dataset, folder: Path) -> ImportSummary:
    """Import the images a folder's `manifest.jsonl` lists. All or nothing: every problem found is reported together.
    A picture already in the dataset (the same bytes, or the same decoded pixels) is skipped, never imported twice."""
    folder = folder.resolve()
    try:
        text = (folder / MANIFEST_NAME).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise ManifestError(f"no {MANIFEST_NAME} in {folder}") from None
    entries = parse_manifest(text, ds.space)
    ready, skipped, problems = _validated(ds, folder, entries)
    if problems:
        shown = problems[:MAX_PROBLEMS_SHOWN]
        more = [f"... and {len(problems) - len(shown)} more"] if len(problems) > len(shown) else []
        raise ManifestError("nothing imported:\n" + "\n".join([*shown, *more]))
    if not ready:
        return ImportSummary(None, 0, 0, 0, tuple(skipped))
    conn, cfg = ds.conn, ds.cfg
    now = utc_now()
    rooms: dict[GroupKey, int] = {}
    with transaction(conn):
        manifest_sha = repo.record_file(conn, "import_manifest", f"{folder.name}/{MANIFEST_NAME}", text, now)
        set_id = repo.create_import_set(conn, manifest_sha, now, cfg.run.output_side, cfg.generator.size_multiple,
                                        cfg.generator.condition_max_pixels, RESAMPLER)
        before = conn.execute("SELECT COUNT(*) FROM building").fetchone()[0]
        for prepared in ready:
            _write(ds, folder, set_id, prepared, rooms)
        buildings = conn.execute("SELECT COUNT(*) FROM building").fetchone()[0] - before
    return ImportSummary(set_id, len(ready), buildings, len(ready) * cfg.run.variants, tuple(skipped))


def room_values_of(ds: Dataset, entry: ImportEntry) -> dict[str, str]:
    """The values a room holds: the room type, and the room axes the manifest gave."""
    room_axes = set(ds.space.axes_for("room"))
    return {ROOM_TYPE: entry.room_type, **{a: v for a, v in entry.values if a in room_axes}}


def _write(ds: Dataset, folder: Path, set_id: int, prepared: Prepared, rooms: dict[GroupKey, int]) -> None:
    """One image's scene (in its group's room when it has one), clutter specs and imported image. Call in a
    transaction."""
    conn, cfg, entry = ds.conn, ds.cfg, prepared.entry
    data = (folder / entry.file).read_bytes()
    if sha256_bytes(data) != prepared.original_sha:  # read again after validation: it must be the same file
        raise ManifestError(f"line {entry.line} ({entry.file}): the file changed during the import; run it again")
    original = repo.record_image(conn, ds.blobs, data)
    rgb = opaque_rgb(imaging.decode(data))
    clean = repo.record_image(conn, ds.blobs, imaging.encode_png(resized(rgb, prepared.size)))
    model_id = repo.model_row(conn, entry.source)
    room_values = room_values_of(ds, entry)
    if entry.group is None:
        room_id = repo.create_room(conn, ds.space_version_id, room_values)
    else:
        key = (entry.source.name, entry.source.revision, entry.group)
        if key not in rooms:
            found = repo.group_room(conn, *key)
            rooms[key] = found[0] if found else repo.create_room(conn, ds.space_version_id, room_values)
        room_id = rooms[key]
    scene_seed = derive_seed(cfg.seed, "import", original)
    scene_values = {a: v for a, v in entry.values if a not in room_values}
    specs = sample_clutter_specs(ds.space, entry.room_type, scene_seed, cfg.run.variants)
    scene_id = repo.create_scene_in_room(conn, room_id, scene_values, scene_seed, specs)
    repo.add_imported_image(conn, scene_id, set_id, entry.line, original, prepared.pixel_sha, clean,
                            model_id, entry.group, entry.origin)


def _validated(ds: Dataset, folder: Path,
               entries: list[ImportEntry]) -> tuple[list[Prepared], list[str], list[str]]:
    """(entries to import, files skipped as already imported, problems)."""
    cfg = ds.cfg
    known_bytes, known_pixels, known_images = repo.imported_hashes(ds.conn)
    ready: list[Prepared] = []
    skipped: list[str] = []
    problems: list[str] = []
    sources: dict[tuple[str, str], tuple[ModelId, int]] = {}  # (name, revision) -> source, first line
    groups: dict[GroupKey, tuple[tuple[tuple[str, str], ...], int]] = {}  # group -> room values, first line
    for entry in entries:
        where = f"line {entry.line} ({entry.file})"
        path = (folder / entry.file).resolve()
        if not path.is_relative_to(folder):
            problems.append(f"{where}: outside the import folder")
            continue
        try:
            data = path.read_bytes()
            rgb = opaque_rgb(imaging.decode(data))
            size = imported_size(rgb.size, cfg.run.output_side, cfg.generator.size_multiple,
                                 cfg.generator.condition_max_pixels)
            image_sha = sha256_bytes(imaging.encode_png(resized(rgb, size)))
        except (OSError, ValueError, SpaceError) as error:
            problems.append(f"{where}: {error}")
            continue
        original_sha, pixels = sha256_bytes(data), pixel_sha(rgb)
        if original_sha in known_bytes or pixels in known_pixels:
            skipped.append(entry.file)
            continue
        if image_sha in known_images:
            problems.append(f"{where}: resized, it is the same clean image as another import's")
            continue
        problems += _source_problems(ds, entry, where, sources) + _group_problems(ds, entry, where, groups)
        known_bytes.add(original_sha)
        known_pixels.add(pixels)
        known_images.add(image_sha)
        ready.append(Prepared(entry, original_sha, pixels, image_sha, size))
    return ready, skipped, problems


def _source_problems(ds: Dataset, entry: ImportEntry, where: str,
                     sources: dict[tuple[str, str], tuple[ModelId, int]]) -> list[str]:
    """A source is a model row, unique on (name, revision): one family and one licence for it."""
    key = (entry.source.name, entry.source.revision)
    recorded = repo.find_model(ds.conn, *key)
    if recorded is not None and recorded != entry.source:
        return [f"{where}: source {key[0]}@{key[1]} is recorded with family {recorded.family} and licence "
                f"{recorded.licence}; use one source name per licence"]
    if key in sources and sources[key][0] != entry.source:
        return [f"{where}: source {key[0]}@{key[1]} has another family or licence than on line {sources[key][1]}; "
                "use one source name per licence"]
    sources.setdefault(key, (entry.source, entry.line))
    return []


def _group_problems(ds: Dataset, entry: ImportEntry, where: str,
                    groups: dict[GroupKey, tuple[tuple[tuple[str, str], ...], int]]) -> list[str]:
    """The views of a group share one room: the same room type and room values, here and in an earlier import."""
    if entry.group is None:
        return []
    key = (entry.source.name, entry.source.revision, entry.group)
    values = tuple(sorted(room_values_of(ds, entry).items()))
    earlier = repo.group_room(ds.conn, *key)
    if earlier is not None and earlier[1] != values:
        return [f"{where}: group {entry.group!r} is a room of an earlier import with other values "
                f"({dict(earlier[1])}); a view of that room must give the same room type and room values"]
    if key in groups and groups[key][0] != values:
        return [f"{where}: group {entry.group!r} gives other room type or room values than line {groups[key][1]}"]
    groups.setdefault(key, (values, entry.line))
    return []
