"""Every query of the store: fixed SQL text with bound parameters. Callers wrap writes in `db.transaction`."""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass

from virtual_unstaging import imaging
from virtual_unstaging.domain import sha256_text
from virtual_unstaging.store.blobs import BlobStore

from clutter_pairs.domain import (
    Box,
    ExchangeRecord,
    Finding,
    Judgment,
    Lesson,
    Measure,
    ModelId,
    NewLesson,
    Part,
    RegionItems,
)
from clutter_pairs.space import Space, Target

Values = tuple[tuple[str, str], ...]
BAD_ANSWER = "bad_answer"  # a call answered, but not on its contract


# --- Rows ------------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class SceneRow:
    id: int
    room_id: int
    building_id: int
    space_version_id: int
    seed: int
    values: Values  # the room's and the scene's


@dataclass(frozen=True)
class SpecRow:
    id: int
    scene_id: int
    variant: int
    seed: int
    values: Values  # the clutter spec's own
    items: tuple[Values, ...]
    item_ids: tuple[int, ...]


@dataclass(frozen=True)
class LoopRow:
    id: int
    wave_id: int
    stage: str
    scene_id: int | None
    clutter_spec_id: int | None
    input_image: str | None
    lessons_arm: str
    engine: str
    max_iterations: int
    stop_reason: str | None


@dataclass(frozen=True)
class IterationRow:
    id: int
    loop_run_id: int
    n: int
    action: str
    seed: int
    verdict: str | None


@dataclass(frozen=True)
class CallRow:
    id: int
    loop_run_id: int
    iteration_id: int | None
    role: str
    model_id: int
    composer_sha: str
    request_sha: str
    answer: str | None
    output_image: str | None
    reused_call_id: int | None
    error_code: str | None


@dataclass(frozen=True)
class AssessmentRow:
    id: int
    iteration_id: int
    kind: str
    verdict: str
    model_call_id: int | None
    judgment: Judgment
    measures: tuple[Measure, ...]  # what was measured, each with the threshold it was compared to
    thresholds: dict[str, float]  # every pixel threshold in force


@dataclass(frozen=True)
class ImportedRow:
    scene_id: int
    import_set_id: int
    line: int
    original_sha: str
    pixel_sha: str
    image_sha: str
    source_model_id: int
    group_name: str | None
    origin: str | None


@dataclass(frozen=True)
class ImportSetRow:
    id: int
    output_side: int
    size_multiple: int
    condition_max_pixels: int
    resampler: str


@dataclass(frozen=True)
class PartRow:
    ordinal: int
    slot: str
    source_kind: str
    file_sha: str | None
    lesson_id: int | None
    assessment_id: int | None
    call_id: int | None
    image_sha: str | None
    setting_name: str | None
    origin: str | None
    text: str | None


# --- Files, texts, images, models ------------------------------------------------------------------------------


def record_file(conn: sqlite3.Connection, kind: str, path: str, content: str, now: str) -> str:
    sha = sha256_text(content)
    conn.execute("INSERT INTO source_file (sha256, kind, path, content, first_used) VALUES (?, ?, ?, ?, ?)"
                 " ON CONFLICT (sha256) DO NOTHING", (sha, kind, path, content, now))
    return sha


def file_content(conn: sqlite3.Connection, sha: str) -> str:
    row = conn.execute("SELECT content FROM source_file WHERE sha256 = ?", (sha,)).fetchone()
    if row is None:
        raise LookupError(f"no source file {sha}")
    return str(row[0])


def record_text(conn: sqlite3.Connection, text: str) -> str:
    sha = sha256_text(text)
    conn.execute("INSERT INTO text_blob (sha256, content) VALUES (?, ?) ON CONFLICT (sha256) DO NOTHING", (sha, text))
    return sha


def text(conn: sqlite3.Connection, sha: str | None) -> str | None:
    if sha is None:
        return None
    row = conn.execute("SELECT content FROM text_blob WHERE sha256 = ?", (sha,)).fetchone()
    if row is None:
        raise LookupError(f"no text {sha}")
    return str(row[0])


def record_image(conn: sqlite3.Connection, blobs: BlobStore, data: bytes) -> str:
    width, height, media_type = imaging.describe(data)
    sha = blobs.put(data)
    conn.execute("INSERT INTO image (sha256, media_type, width, height) VALUES (?, ?, ?, ?)"
                 " ON CONFLICT (sha256) DO NOTHING", (sha, media_type, width, height))
    return sha


def image_size(conn: sqlite3.Connection, sha: str) -> tuple[int, int]:
    row = conn.execute("SELECT width, height FROM image WHERE sha256 = ?", (sha,)).fetchone()
    if row is None:
        raise LookupError(f"no image {sha}")
    return int(row[0]), int(row[1])


def all_image_shas(conn: sqlite3.Connection) -> list[str]:
    return [str(r[0]) for r in conn.execute("SELECT sha256 FROM image ORDER BY sha256")]


def model_row(conn: sqlite3.Connection, model: ModelId) -> int:
    """The model's id, recorded on first use. A known (name, revision) with another family or licence is an error."""
    row = conn.execute("SELECT id, family, licence FROM model WHERE name = ? AND revision = ?",
                       (model.name, model.revision)).fetchone()
    if row is not None:
        if (row[1], row[2]) != (model.family, model.licence):
            raise ValueError(f"model {model.name}@{model.revision} is recorded with family {row[1]} and licence {row[2]}")
        return int(row[0])
    cur = conn.execute("INSERT INTO model (name, revision, family, licence) VALUES (?, ?, ?, ?)",
                       (model.name, model.revision, model.family, model.licence))
    return int(cur.lastrowid or 0)


def model_by_id(conn: sqlite3.Connection, model_id: int) -> ModelId:
    row = conn.execute("SELECT name, revision, family, licence FROM model WHERE id = ?", (model_id,)).fetchone()
    return ModelId(str(row[0]), str(row[1]), str(row[2]), str(row[3]))


# --- Imported clean images -------------------------------------------------------------------------------------


def create_import_set(conn: sqlite3.Connection, manifest_sha: str, now: str, output_side: int, size_multiple: int,
                      condition_max_pixels: int, resampler: str) -> int:
    return int(conn.execute(
        "INSERT INTO import_set (manifest_sha, imported_at, output_side, size_multiple, condition_max_pixels,"
        " resampler) VALUES (?, ?, ?, ?, ?, ?)",
        (manifest_sha, now, output_side, size_multiple, condition_max_pixels, resampler)).lastrowid or 0)


def import_set(conn: sqlite3.Connection, import_set_id: int) -> ImportSetRow:
    row = conn.execute("SELECT id, output_side, size_multiple, condition_max_pixels, resampler FROM import_set"
                       " WHERE id = ?", (import_set_id,)).fetchone()
    if row is None:
        raise LookupError(f"no import set {import_set_id}")
    return ImportSetRow(*row)


def import_manifest(conn: sqlite3.Connection, import_set_id: int) -> str:
    """The manifest text an import set stored."""
    row = conn.execute("SELECT manifest_sha FROM import_set WHERE id = ?", (import_set_id,)).fetchone()
    if row is None:
        raise LookupError(f"no import set {import_set_id}")
    return file_content(conn, str(row[0]))


def add_imported_image(conn: sqlite3.Connection, scene_id: int, import_set_id: int, line: int, original_sha: str,
                       pixel_sha: str, image_sha: str, source_model_id: int, group_name: str | None,
                       origin: str | None) -> None:
    conn.execute("INSERT INTO imported_image (scene_id, import_set_id, line, original_sha, pixel_sha, image_sha,"
                 " source_model_id, group_name, origin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                 (scene_id, import_set_id, line, original_sha, pixel_sha, image_sha, source_model_id, group_name, origin))


_IMPORTED = ("SELECT scene_id, import_set_id, line, original_sha, pixel_sha, image_sha, source_model_id, group_name,"
             " origin FROM imported_image")


def imported_image(conn: sqlite3.Connection, scene_id: int) -> ImportedRow | None:
    row = conn.execute(f"{_IMPORTED} WHERE scene_id = ?", (scene_id,)).fetchone()
    return None if row is None else ImportedRow(*row)


def imported_images(conn: sqlite3.Connection) -> list[ImportedRow]:
    return [ImportedRow(*r) for r in conn.execute(f"{_IMPORTED} ORDER BY scene_id")]


def imported_hashes(conn: sqlite3.Connection) -> tuple[set[str], set[str], set[str]]:
    """The hashes already imported: originals' bytes, decoded pixels, resized images. One picture enters once."""
    rows = conn.execute("SELECT original_sha, pixel_sha, image_sha FROM imported_image").fetchall()
    return {str(r[0]) for r in rows}, {str(r[1]) for r in rows}, {str(r[2]) for r in rows}


def find_model(conn: sqlite3.Connection, name: str, revision: str) -> ModelId | None:
    row = conn.execute("SELECT name, revision, family, licence FROM model WHERE name = ? AND revision = ?",
                       (name, revision)).fetchone()
    return None if row is None else ModelId(str(row[0]), str(row[1]), str(row[2]), str(row[3]))


def group_room(conn: sqlite3.Connection, name: str, revision: str, group: str) -> tuple[int, Values] | None:
    """The room an earlier import gave a group (of the same source): its id and values."""
    row = conn.execute(
        "SELECT s.room_id FROM imported_image i JOIN scene s ON s.id = i.scene_id JOIN model m ON m.id = i.source_model_id"
        " WHERE m.name = ? AND m.revision = ? AND i.group_name = ? ORDER BY i.scene_id LIMIT 1",
        (name, revision, group)).fetchone()
    if row is None:
        return None
    values = tuple((str(a), str(v)) for a, v in conn.execute(
        "SELECT axis, value FROM room_value WHERE room_id = ? ORDER BY axis", (row[0],)))
    return int(row[0]), values


def misplaced_imported_iteration_images(conn: sqlite3.Connection) -> list[int]:
    """Iterations whose `imported` image is not the image recorded for the scene's import."""
    return [int(r[0]) for r in conn.execute(
        "SELECT ii.iteration_id FROM iteration_image ii JOIN iteration it ON it.id = ii.iteration_id"
        " JOIN loop_run l ON l.id = it.loop_run_id JOIN imported_image im ON im.scene_id = l.scene_id"
        " WHERE ii.role = 'imported' AND ii.image_sha <> im.image_sha ORDER BY ii.iteration_id")]


def accepted_clutter_iterations_without_pair(conn: sqlite3.Connection) -> list[int]:
    """Accepted clutter iterations that the `pair` view does not show: a pair that went missing."""
    return [int(r[0]) for r in conn.execute(
        "SELECT it.id FROM iteration it JOIN loop_run l ON l.id = it.loop_run_id"
        " WHERE l.stage = 'clutter' AND it.verdict = 'accept'"
        " AND NOT EXISTS (SELECT 1 FROM pair p WHERE p.pair_id = it.id) ORDER BY it.id")]


def badly_grouped_rooms(conn: sqlite3.Connection) -> list[int]:
    """Rooms of imported scenes whose scenes do not share one group and one source (or share a room with no group)."""
    return [int(r[0]) for r in conn.execute(
        "SELECT s.room_id FROM imported_image i JOIN scene s ON s.id = i.scene_id GROUP BY s.room_id"
        " HAVING COUNT(DISTINCT COALESCE(i.group_name, '')) > 1 OR COUNT(DISTINCT i.source_model_id) > 1"
        "    OR (COUNT(*) > 1 AND SUM(i.group_name IS NULL) > 0) ORDER BY s.room_id")]


def imported_owners(conn: sqlite3.Connection) -> set[tuple[str, int]]:
    """The rooms and scenes of imported scenes, as (kind, id): they hold the values the manifest gave."""
    return {(str(r[0]), int(r[1])) for r in conn.execute(
        "SELECT 'scene', s.id FROM imported_image i JOIN scene s ON s.id = i.scene_id"
        " UNION ALL SELECT 'room', s.room_id FROM imported_image i JOIN scene s ON s.id = i.scene_id")}


def misplaced_import_actions(conn: sqlite3.Connection) -> list[int]:
    """Iterations whose action does not fit their loop: `import` only in the clean loop of an imported scene, and
    nothing but `import` there."""
    return [int(r[0]) for r in conn.execute(
        "SELECT it.id FROM iteration it JOIN loop_run l ON l.id = it.loop_run_id"
        " WHERE (it.action = 'import') <> (l.stage = 'clean' AND EXISTS"
        "   (SELECT 1 FROM imported_image im WHERE im.scene_id = l.scene_id)) ORDER BY it.id")]


# --- Reasons, space, targets ---------------------------------------------------------------------------------


def register_reasons(conn: sqlite3.Connection, reasons: Mapping[str, tuple[str, str]], file_sha: str) -> None:
    for code, (stage, severity) in reasons.items():
        row = conn.execute("SELECT stage, severity FROM reason WHERE code = ?", (code,)).fetchone()
        if row is None:
            conn.execute("INSERT INTO reason (code, stage, severity, file_sha) VALUES (?, ?, ?, ?)",
                         (code, stage, severity, file_sha))
        elif (row[0], row[1]) != (stage, severity):
            raise ValueError(f"reason {code} is recorded as {row[0]}/{row[1]}: a changed severity needs a new code")


def severities(conn: sqlite3.Connection) -> dict[str, str]:
    return {str(r[0]): str(r[1]) for r in conn.execute("SELECT code, severity FROM reason")}


def register_space(conn: sqlite3.Connection, space: Space, ontology_sha: str, taxonomy_sha: str) -> int:
    for name, axis in space.axes.items():
        row = conn.execute("SELECT applies_to FROM axis WHERE name = ?", (name,)).fetchone()
        if row is None:
            conn.execute("INSERT INTO axis (name, applies_to) VALUES (?, ?)", (name, axis.applies_to))
        elif row[0] != axis.applies_to:
            raise ValueError(f"axis {name} is recorded as applying to {row[0]}, not {axis.applies_to}")
    conn.executemany("INSERT INTO axis_value (axis, value) VALUES (?, ?) ON CONFLICT DO NOTHING", space.pairs())
    conn.execute("INSERT INTO space_version (ontology_sha, taxonomy_sha) VALUES (?, ?) ON CONFLICT DO NOTHING",
                 (ontology_sha, taxonomy_sha))
    version = int(conn.execute("SELECT id FROM space_version WHERE ontology_sha = ? AND taxonomy_sha = ?",
                               (ontology_sha, taxonomy_sha)).fetchone()[0])
    conn.executemany("INSERT INTO space_value (space_version_id, axis, value) VALUES (?, ?, ?) ON CONFLICT DO NOTHING",
                     [(version, a, v) for a, v in space.pairs()])
    return version


def register_targets(conn: sqlite3.Connection, space_version_id: int, targets_sha: str, targets: Sequence[Target]) -> int:
    row = conn.execute("SELECT id FROM target_set WHERE space_version_id = ? AND targets_sha = ?",
                       (space_version_id, targets_sha)).fetchone()
    if row is not None:
        return int(row[0])
    cur = conn.execute("INSERT INTO target_set (space_version_id, targets_sha) VALUES (?, ?)",
                       (space_version_id, targets_sha))
    set_id = int(cur.lastrowid or 0)
    for target in targets:
        tid = conn.execute("INSERT INTO target (target_set_id, pairs) VALUES (?, ?)", (set_id, target.pairs)).lastrowid
        conn.executemany("INSERT INTO target_value (target_id, axis, value) VALUES (?, ?, ?)",
                         [(tid, a, v) for a, v in target.cell])
    return set_id


def targets(conn: sqlite3.Connection, target_set_id: int) -> list[tuple[int, int, Values]]:
    """(target id, pairs wanted, cell values) of a target set."""
    out = []
    for tid, pairs in conn.execute("SELECT id, pairs FROM target WHERE target_set_id = ? ORDER BY id", (target_set_id,)):
        values = tuple((str(a), str(v)) for a, v in conn.execute(
            "SELECT axis, value FROM target_value WHERE target_id = ? ORDER BY axis", (tid,)))
        out.append((int(tid), int(pairs), values))
    return out


# --- Buildings, rooms, scenes, clutter specs -----------------------------------------------------------------


def create_room(conn: sqlite3.Connection, space_version_id: int, room_values: Mapping[str, str]) -> int:
    """A building and its one room, with the room's values; returns the room's id."""
    building = conn.execute("INSERT INTO building (space_version_id) VALUES (?)", (space_version_id,)).lastrowid
    room = int(conn.execute("INSERT INTO room (building_id) VALUES (?)", (building,)).lastrowid or 0)
    conn.executemany("INSERT INTO room_value (room_id, axis, value) VALUES (?, ?, ?)",
                     [(room, a, v) for a, v in room_values.items()])
    return room


def create_scene_in_room(conn: sqlite3.Connection, room_id: int, scene_values: Mapping[str, str], seed: int,
                         specs: Sequence[tuple[int, int, Mapping[str, str], Sequence[Mapping[str, str]]]]) -> int:
    """A scene of a room and its clutter specs: (variant, seed, values, items)."""
    scene = int(conn.execute("INSERT INTO scene (room_id, seed) VALUES (?, ?)", (room_id, seed)).lastrowid or 0)
    conn.executemany("INSERT INTO scene_value (scene_id, axis, value) VALUES (?, ?, ?)",
                     [(scene, a, v) for a, v in scene_values.items()])
    for variant, spec_seed, values, items in specs:
        spec = conn.execute("INSERT INTO clutter_spec (scene_id, variant, seed) VALUES (?, ?, ?)",
                            (scene, variant, spec_seed)).lastrowid
        conn.executemany("INSERT INTO clutter_spec_value (clutter_spec_id, axis, value) VALUES (?, ?, ?)",
                         [(spec, a, v) for a, v in values.items()])
        for ordinal, item in enumerate(items, start=1):
            iid = conn.execute("INSERT INTO clutter_item (clutter_spec_id, ordinal) VALUES (?, ?)",
                               (spec, ordinal)).lastrowid
            conn.executemany("INSERT INTO clutter_item_value (clutter_item_id, axis, value) VALUES (?, ?, ?)",
                             [(iid, a, v) for a, v in item.items()])
    return scene


def create_scene(conn: sqlite3.Connection, space_version_id: int, room_values: Mapping[str, str],
                 scene_values: Mapping[str, str], seed: int,
                 specs: Sequence[tuple[int, int, Mapping[str, str], Sequence[Mapping[str, str]]]]) -> int:
    """One building, one room, one scene (the planner's rule), and its clutter specs: (variant, seed, values, items)."""
    return create_scene_in_room(conn, create_room(conn, space_version_id, room_values), scene_values, seed, specs)


def scene_count(conn: sqlite3.Connection) -> int:
    return int(conn.execute("SELECT COUNT(*) FROM scene").fetchone()[0])


def scene(conn: sqlite3.Connection, scene_id: int) -> SceneRow:
    row = conn.execute(
        "SELECT s.id, s.room_id, r.building_id, b.space_version_id, s.seed FROM scene s JOIN room r ON r.id = s.room_id"
        " JOIN building b ON b.id = r.building_id WHERE s.id = ?", (scene_id,)).fetchone()
    if row is None:
        raise LookupError(f"no scene {scene_id}")
    values = tuple((str(a), str(v)) for a, v in conn.execute(
        "SELECT axis, value FROM room_value WHERE room_id = ? UNION ALL"
        " SELECT axis, value FROM scene_value WHERE scene_id = ?", (row[1], scene_id)))
    return SceneRow(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), values)


def clutter_specs(conn: sqlite3.Connection, scene_id: int) -> list[SpecRow]:
    return [clutter_spec(conn, int(r[0])) for r in
            conn.execute("SELECT id FROM clutter_spec WHERE scene_id = ? ORDER BY variant", (scene_id,))]


def clutter_spec(conn: sqlite3.Connection, spec_id: int) -> SpecRow:
    row = conn.execute("SELECT id, scene_id, variant, seed FROM clutter_spec WHERE id = ?", (spec_id,)).fetchone()
    if row is None:
        raise LookupError(f"no clutter spec {spec_id}")
    values = tuple((str(a), str(v)) for a, v in conn.execute(
        "SELECT axis, value FROM clutter_spec_value WHERE clutter_spec_id = ?", (spec_id,)))
    items, ids = [], []
    for iid, _ in conn.execute("SELECT id, ordinal FROM clutter_item WHERE clutter_spec_id = ? ORDER BY ordinal",
                               (spec_id,)).fetchall():
        ids.append(int(iid))
        items.append(tuple((str(a), str(v)) for a, v in conn.execute(
            "SELECT axis, value FROM clutter_item_value WHERE clutter_item_id = ?", (iid,))))
    return SpecRow(int(row[0]), int(row[1]), int(row[2]), int(row[3]), values, tuple(items), tuple(ids))


def owner_values(conn: sqlite3.Connection) -> list[tuple[str, int, int, str, str]]:
    """Every owner's values with its building's space version: (kind, owner id, space version, axis, value)."""
    return [(str(r[0]), int(r[1]), int(r[2]), str(r[3]), str(r[4])) for r in conn.execute(
        "SELECT 'room', r.id, b.space_version_id, v.axis, v.value FROM room_value v JOIN room r ON r.id = v.room_id"
        " JOIN building b ON b.id = r.building_id"
        " UNION ALL SELECT 'scene', s.id, b.space_version_id, v.axis, v.value FROM scene_value v"
        " JOIN scene s ON s.id = v.scene_id JOIN room r ON r.id = s.room_id JOIN building b ON b.id = r.building_id"
        " UNION ALL SELECT 'clutter_spec', c.id, b.space_version_id, v.axis, v.value FROM clutter_spec_value v"
        " JOIN clutter_spec c ON c.id = v.clutter_spec_id JOIN scene s ON s.id = c.scene_id"
        " JOIN room r ON r.id = s.room_id JOIN building b ON b.id = r.building_id"
        " UNION ALL SELECT 'clutter_item', i.id, b.space_version_id, v.axis, v.value FROM clutter_item_value v"
        " JOIN clutter_item i ON i.id = v.clutter_item_id JOIN clutter_spec c ON c.id = i.clutter_spec_id"
        " JOIN scene s ON s.id = c.scene_id JOIN room r ON r.id = s.room_id JOIN building b ON b.id = r.building_id")]


def owners(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    return [(str(r[0]), int(r[1])) for r in conn.execute(
        "SELECT 'room', id FROM room UNION ALL SELECT 'scene', id FROM scene"
        " UNION ALL SELECT 'clutter_spec', id FROM clutter_spec UNION ALL SELECT 'clutter_item', id FROM clutter_item")]


def owner_space_version(conn: sqlite3.Connection, kind: str, owner: int) -> int:
    queries = {
        "room": "SELECT b.space_version_id FROM room r JOIN building b ON b.id = r.building_id WHERE r.id = ?",
        "scene": "SELECT b.space_version_id FROM scene s JOIN room r ON r.id = s.room_id"
                 " JOIN building b ON b.id = r.building_id WHERE s.id = ?",
        "clutter_spec": "SELECT b.space_version_id FROM clutter_spec c JOIN scene s ON s.id = c.scene_id"
                        " JOIN room r ON r.id = s.room_id JOIN building b ON b.id = r.building_id WHERE c.id = ?",
        "clutter_item": "SELECT b.space_version_id FROM clutter_item i JOIN clutter_spec c ON c.id = i.clutter_spec_id"
                        " JOIN scene s ON s.id = c.scene_id JOIN room r ON r.id = s.room_id"
                        " JOIN building b ON b.id = r.building_id WHERE i.id = ?",
    }
    return int(conn.execute(queries[kind], (owner,)).fetchone()[0])


def axes_by_kind(conn: sqlite3.Connection) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for name, kind in conn.execute("SELECT name, applies_to FROM axis"):
        out.setdefault(str(kind), set()).add(str(name))
    return out


def space_values(conn: sqlite3.Connection) -> set[tuple[int, str, str]]:
    return {(int(r[0]), str(r[1]), str(r[2])) for r in
            conn.execute("SELECT space_version_id, axis, value FROM space_value")}


def space_version_files(conn: sqlite3.Connection, space_version_id: int) -> tuple[str, str]:
    row = conn.execute("SELECT ontology_sha, taxonomy_sha FROM space_version WHERE id = ?", (space_version_id,)).fetchone()
    return str(row[0]), str(row[1])


def alive_specs_per_target(conn: sqlite3.Connection, target_set_id: int) -> dict[int, int]:
    """Per target: the clutter specs that may still become pairs (no loop yet, accepted, unfinished, or stopped by
    a deadline), and whose clean loop has not failed; counted by relational division on (axis, value)."""
    rows = conn.execute(
        "WITH alive AS ("
        "  SELECT c.id FROM clutter_spec c"
        "  WHERE NOT EXISTS (SELECT 1 FROM loop_run l WHERE l.clutter_spec_id = c.id"
        "                    AND l.stop_reason IN ('no_progress', 'max_iterations', 'error'))"
        "    AND NOT EXISTS (SELECT 1 FROM loop_run l WHERE l.scene_id = c.scene_id AND l.stage = 'clean'"
        "                    AND l.stop_reason IN ('no_progress', 'max_iterations', 'error')"
        "                    AND NOT EXISTS (SELECT 1 FROM clean_image ci WHERE ci.scene_id = c.scene_id))),"
        " spec_value AS ("
        "  SELECT c.id AS spec_id, v.axis, v.value FROM clutter_spec c JOIN clutter_spec_value v ON v.clutter_spec_id = c.id"
        "  UNION ALL SELECT c.id, v.axis, v.value FROM clutter_spec c JOIN scene_value v ON v.scene_id = c.scene_id"
        "  UNION ALL SELECT c.id, v.axis, v.value FROM clutter_spec c JOIN scene s ON s.id = c.scene_id"
        "   JOIN room_value v ON v.room_id = s.room_id)"
        " SELECT t.id, (SELECT COUNT(*) FROM alive a WHERE NOT EXISTS ("
        "   SELECT 1 FROM target_value tv WHERE tv.target_id = t.id AND NOT EXISTS ("
        "     SELECT 1 FROM spec_value sv WHERE sv.spec_id = a.id AND sv.axis = tv.axis AND sv.value = tv.value)))"
        " FROM target t WHERE t.target_set_id = ?", (target_set_id,))
    return {int(r[0]): int(r[1]) for r in rows}


# --- Rentals, runs, waves ------------------------------------------------------------------------------------


def create_rental(conn: sqlite3.Connection, provider: str, session_id: str, gpu: str, gpu_count: int,
                  price_per_hour: float, started_at: str, deadline: str) -> int:
    row = conn.execute("SELECT id FROM rental WHERE provider = ? AND session_id = ?", (provider, session_id)).fetchone()
    if row is not None:
        return int(row[0])
    return int(conn.execute(
        "INSERT INTO rental (provider, session_id, gpu, gpu_count, price_per_hour, started_at, deadline)"
        " VALUES (?, ?, ?, ?, ?, ?, ?)",
        (provider, session_id, gpu, gpu_count, price_per_hour, started_at, deadline)).lastrowid or 0)


def rental_by_session(conn: sqlite3.Connection, session_id: str) -> tuple[int, str] | None:
    row = conn.execute("SELECT id, deadline FROM rental WHERE session_id = ?", (session_id,)).fetchone()
    return None if row is None else (int(row[0]), str(row[1]))


def end_rental(conn: sqlite3.Connection, session_id: str, now: str) -> None:
    conn.execute("UPDATE rental SET ended_at = ? WHERE session_id = ? AND ended_at IS NULL", (now, session_id))


def create_run(conn: sqlite3.Connection, config_sha: str, target_set_id: int, target_pairs: int,
               rental_id: int | None, now: str) -> int:
    return int(conn.execute(
        "INSERT INTO run (config_sha, target_set_id, target_pairs, rental_id, started_at) VALUES (?, ?, ?, ?, ?)",
        (config_sha, target_set_id, target_pairs, rental_id, now)).lastrowid or 0)


def end_run(conn: sqlite3.Connection, run_id: int, now: str) -> None:
    conn.execute("UPDATE run SET ended_at = ? WHERE id = ?", (now, run_id))


def rental_has_waves(conn: sqlite3.Connection, rental_id: int) -> bool:
    return conn.execute("SELECT 1 FROM wave w JOIN run r ON r.id = w.run_id WHERE r.rental_id = ? LIMIT 1",
                        (rental_id,)).fetchone() is not None


def create_wave(conn: sqlite3.Connection, run_id: int, smoke: bool, now: str) -> int:
    ordinal = int(conn.execute("SELECT COALESCE(MAX(ordinal), 0) + 1 FROM wave WHERE run_id = ?", (run_id,)).fetchone()[0])
    return int(conn.execute("INSERT INTO wave (run_id, ordinal, smoke, started_at) VALUES (?, ?, ?, ?)",
                            (run_id, ordinal, int(smoke), now)).lastrowid or 0)


def accepted_pairs(conn: sqlite3.Connection) -> int:
    return int(conn.execute("SELECT COUNT(*) FROM pair").fetchone()[0])


def wave_scenes(conn: sqlite3.Connection, limit: int) -> list[int]:
    """Scenes with work left, in this order: an unfinished loop to resume (or one a deadline stopped); an accepted
    clean image with clutter specs not yet looped; no clean loop yet."""
    rows = conn.execute(
        "SELECT s.id,"
        "  CASE WHEN EXISTS (SELECT 1 FROM loop_run l LEFT JOIN clutter_spec c ON c.id = l.clutter_spec_id"
        "                    WHERE (l.scene_id = s.id OR c.scene_id = s.id)"
        "                      AND (l.stop_reason IS NULL OR l.stop_reason = 'deadline')) THEN 0"
        "       WHEN EXISTS (SELECT 1 FROM clean_image ci WHERE ci.scene_id = s.id)"
        "        AND EXISTS (SELECT 1 FROM clutter_spec c WHERE c.scene_id = s.id"
        "                    AND NOT EXISTS (SELECT 1 FROM loop_run l WHERE l.clutter_spec_id = c.id)) THEN 1"
        "       WHEN NOT EXISTS (SELECT 1 FROM loop_run l WHERE l.scene_id = s.id) THEN 2"
        "       ELSE 3 END AS rank"
        " FROM scene s ORDER BY rank, s.id")
    return [int(r[0]) for r in rows if r[1] < 3][:limit]


# --- Loops and iterations ------------------------------------------------------------------------------------

_LOOP = ("SELECT id, wave_id, stage, scene_id, clutter_spec_id, input_image, lessons_arm, engine, max_iterations,"
         " stop_reason FROM loop_run")


def _loop(row: sqlite3.Row) -> LoopRow:
    return LoopRow(int(row[0]), int(row[1]), str(row[2]), row[3], row[4], row[5], str(row[6]), str(row[7]),
                   int(row[8]), row[9])


def find_loop(conn: sqlite3.Connection, stage: str, subject_id: int) -> LoopRow | None:
    column = "scene_id" if stage == "clean" else "clutter_spec_id"
    row = conn.execute(f"{_LOOP} WHERE stage = ? AND {column} = ? ORDER BY id DESC LIMIT 1", (stage, subject_id)).fetchone()
    return None if row is None else _loop(row)


def loop(conn: sqlite3.Connection, loop_id: int) -> LoopRow:
    row = conn.execute(f"{_LOOP} WHERE id = ?", (loop_id,)).fetchone()
    if row is None:
        raise LookupError(f"no loop {loop_id}")
    return _loop(row)


def all_loops(conn: sqlite3.Connection) -> list[LoopRow]:
    return [_loop(r) for r in conn.execute(f"{_LOOP} ORDER BY id")]


def create_loop(conn: sqlite3.Connection, wave_id: int, stage: str, subject_id: int, input_image: str | None,
                arm: str, engine: str, max_iterations: int) -> int:
    scene_id, spec_id = (subject_id, None) if stage == "clean" else (None, subject_id)
    return int(conn.execute(
        "INSERT INTO loop_run (wave_id, stage, scene_id, clutter_spec_id, input_image, lessons_arm, engine,"
        " max_iterations) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (wave_id, stage, scene_id, spec_id, input_image, arm, engine, max_iterations)).lastrowid or 0)


def set_stop(conn: sqlite3.Connection, loop_id: int, reason: str | None) -> None:
    conn.execute("UPDATE loop_run SET stop_reason = ? WHERE id = ?", (reason, loop_id))


def iterations(conn: sqlite3.Connection, loop_id: int) -> list[IterationRow]:
    return [IterationRow(int(r[0]), loop_id, int(r[1]), str(r[2]), int(r[3]), r[4]) for r in conn.execute(
        "SELECT id, n, action, seed, verdict FROM iteration WHERE loop_run_id = ? ORDER BY n", (loop_id,))]


def create_iteration(conn: sqlite3.Connection, loop_id: int, n: int, action: str, seed: int) -> int:
    return int(conn.execute("INSERT INTO iteration (loop_run_id, n, action, seed) VALUES (?, ?, ?, ?)",
                            (loop_id, n, action, seed)).lastrowid or 0)


def set_verdict(conn: sqlite3.Connection, iteration_id: int, verdict: str) -> None:
    conn.execute("UPDATE iteration SET verdict = ? WHERE id = ?", (verdict, iteration_id))


def add_iteration_image(conn: sqlite3.Connection, iteration_id: int, role: str, sha: str) -> None:
    conn.execute("INSERT INTO iteration_image (iteration_id, role, image_sha) VALUES (?, ?, ?)"
                 " ON CONFLICT (iteration_id, role) DO UPDATE SET image_sha = excluded.image_sha", (iteration_id, role, sha))


def iteration_images(conn: sqlite3.Connection, iteration_id: int) -> dict[str, str]:
    return {str(r[0]): str(r[1]) for r in
            conn.execute("SELECT role, image_sha FROM iteration_image WHERE iteration_id = ?", (iteration_id,))}


def clear_iteration_results(conn: sqlite3.Connection, iteration_id: int) -> None:
    """Before an unfinished iteration is redone: its images and assessments go; its calls stay, answered again from
    the store."""
    for aid in [int(r[0]) for r in conn.execute("SELECT id FROM assessment WHERE iteration_id = ?", (iteration_id,))]:
        conn.execute("DELETE FROM finding_region WHERE finding_id IN (SELECT id FROM finding WHERE assessment_id = ?)",
                     (aid,))
        for table in ("finding", "guidance", "region_item", "region_answer", "measure"):
            conn.execute(f"DELETE FROM {table} WHERE assessment_id = ?", (aid,))
        conn.execute("DELETE FROM assessment WHERE id = ?", (aid,))
    conn.execute("DELETE FROM mask_region WHERE iteration_id = ?", (iteration_id,))
    conn.execute("DELETE FROM region_set WHERE iteration_id = ?", (iteration_id,))
    conn.execute("DELETE FROM iteration_image WHERE iteration_id = ?", (iteration_id,))


def add_region_set(conn: sqlite3.Connection, iteration_id: int, params: Mapping[str, int], speck_px: int,
                   regions: Sequence[tuple[int, Box, int]]) -> None:
    """An iteration's region set (region_group_px, region_min_px, max_regions, drawing) and its numbered regions:
    (number, box, mask pixels)."""
    conn.execute("INSERT INTO region_set (iteration_id, region_group_px, region_min_px, max_regions, drawing, speck_px)"
                 " VALUES (?, ?, ?, ?, ?, ?)", (iteration_id, params["region_group_px"], params["region_min_px"],
                                                params["max_regions"], params["drawing"], speck_px))
    conn.executemany("INSERT INTO mask_region (iteration_id, n, x0, y0, x1, y1, px) VALUES (?, ?, ?, ?, ?, ?, ?)",
                     [(iteration_id, n, b.x0, b.y0, b.x1, b.y1, px) for n, b, px in regions])


def mask_regions(conn: sqlite3.Connection, iteration_id: int) -> list[tuple[int, Box, int]]:
    return [(int(r[0]), Box(r[1], r[2], r[3], r[4]), int(r[5])) for r in conn.execute(
        "SELECT n, x0, y0, x1, y1, px FROM mask_region WHERE iteration_id = ? ORDER BY n", (iteration_id,))]


def region_set(conn: sqlite3.Connection, iteration_id: int) -> tuple[dict[str, int], int] | None:
    """An iteration's region parameters (region_group_px, region_min_px, max_regions, drawing) and speck pixels."""
    row = conn.execute("SELECT region_group_px, region_min_px, max_regions, drawing, speck_px FROM region_set"
                       " WHERE iteration_id = ?", (iteration_id,)).fetchone()
    if row is None:
        return None
    return dict(zip(("region_group_px", "region_min_px", "max_regions", "drawing"), map(int, row[:4]), strict=True)), int(row[4])


def pair_judged_iterations(conn: sqlite3.Connection) -> list[int]:
    """Clutter iterations the pair judge was called on, and those with a region set."""
    return [int(r[0]) for r in conn.execute(
        "SELECT mc.iteration_id FROM model_call mc JOIN loop_run l ON l.id = mc.loop_run_id"
        " WHERE mc.role = 'judge' AND l.stage = 'clutter' AND mc.iteration_id IS NOT NULL"
        " UNION SELECT iteration_id FROM region_set ORDER BY 1")]


def accepted_clean_image(conn: sqlite3.Connection, scene_id: int) -> str | None:
    row = conn.execute("SELECT image_sha FROM clean_image WHERE scene_id = ? ORDER BY loop_run_id LIMIT 1",
                       (scene_id,)).fetchone()
    return None if row is None else str(row[0])


# --- Calls ------------------------------------------------------------------------------------------------------

_CALL = ("SELECT id, loop_run_id, iteration_id, role, model_id, composer_sha, request_sha, answer_sha, output_image,"
         " reused_call_id, error_code FROM model_call")


def _call(conn: sqlite3.Connection, row: sqlite3.Row) -> CallRow:
    return CallRow(int(row[0]), int(row[1]), row[2], str(row[3]), int(row[4]), str(row[5]), str(row[6]),
                   text(conn, row[7]), row[8], row[9], row[10])


def find_answered_call(conn: sqlite3.Connection, request_sha: str, model_id: int) -> CallRow | None:
    """The earliest successful call with this canonical request on this model: its answer can be reused."""
    row = conn.execute(f"{_CALL} WHERE request_sha = ? AND model_id = ? AND answer_sha IS NOT NULL"
                       f" AND (error_code IS NULL OR error_code = '{BAD_ANSWER}') ORDER BY id LIMIT 1",
                       (request_sha, model_id)).fetchone()
    return None if row is None else _call(conn, row)


def find_own_call(conn: sqlite3.Connection, loop_id: int, iteration_id: int | None, role: str,
                  request_sha: str) -> CallRow | None:
    """This loop's successful call of this role and request, in this iteration (or after the loop): a redone step."""
    row = conn.execute(
        f"{_CALL} WHERE loop_run_id = ? AND iteration_id IS ? AND role = ? AND request_sha = ? AND answer_sha IS NOT NULL"
        f" AND (error_code IS NULL OR error_code = '{BAD_ANSWER}') ORDER BY id LIMIT 1",
        (loop_id, iteration_id, role, request_sha)).fetchone()
    return None if row is None else _call(conn, row)


def mark_bad_answer(conn: sqlite3.Connection, call_id: int, message: str) -> None:
    """The model answered, but not on its contract: the answer stays, the call is marked (a replay meets it again)."""
    conn.execute("UPDATE model_call SET error_code = ?, error_message = ? WHERE id = ?", (BAD_ANSWER, message, call_id))


def call(conn: sqlite3.Connection, call_id: int) -> CallRow:
    row = conn.execute(f"{_CALL} WHERE id = ?", (call_id,)).fetchone()
    if row is None:
        raise LookupError(f"no call {call_id}")
    return _call(conn, row)


def calls_of_iteration(conn: sqlite3.Connection, iteration_id: int) -> list[CallRow]:
    return [_call(conn, r) for r in conn.execute(f"{_CALL} WHERE iteration_id = ? ORDER BY id", (iteration_id,))]


def calls_of_loop(conn: sqlite3.Connection, loop_id: int) -> list[CallRow]:
    return [_call(conn, r) for r in conn.execute(f"{_CALL} WHERE loop_run_id = ? ORDER BY id", (loop_id,))]


def all_calls(conn: sqlite3.Connection) -> list[CallRow]:
    return [_call(conn, r) for r in conn.execute(f"{_CALL} ORDER BY id")]


def actual_call_count(conn: sqlite3.Connection) -> int:
    """Calls that reached a model: neither reused nor failed before an answer."""
    return int(conn.execute("SELECT COUNT(*) FROM model_call WHERE reused_call_id IS NULL").fetchone()[0])


def insert_call(conn: sqlite3.Connection, blobs: BlobStore, *, loop_id: int, iteration_id: int | None, role: str,
                model_id: int, composer_sha: str, request_text: str, answer: str | None, output_image: str | None,
                reused_call_id: int | None, started_at: str, wall_seconds: float | None, gpu_seconds: float | None,
                error_code: str | None, error_message: str | None, parts: Sequence[Part],
                exchanges: Sequence[ExchangeRecord]) -> int:
    request_sha = record_text(conn, request_text)
    answer_sha = None if answer is None else record_text(conn, answer)
    call_id = int(conn.execute(
        "INSERT INTO model_call (loop_run_id, iteration_id, role, model_id, composer_sha, request_sha, answer_sha,"
        " output_image, reused_call_id, started_at, wall_seconds, gpu_seconds, error_code, error_message)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (loop_id, iteration_id, role, model_id, composer_sha, request_sha, answer_sha, output_image, reused_call_id,
         started_at, wall_seconds, gpu_seconds, error_code, error_message)).lastrowid or 0)
    for ordinal, part in enumerate(parts, start=1):
        s = part.source
        conn.execute(
            "INSERT INTO composition_part (model_call_id, ordinal, slot, source_kind, file_sha, lesson_id,"
            " assessment_id, call_id, image_sha, setting_name, origin, text_sha) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (call_id, ordinal, part.slot, part.kind, s.file_sha, s.lesson_id, s.assessment_id, s.call_id,
             part.image_sha, s.setting_name, s.origin, None if part.text is None else record_text(conn, part.text)))
    for ordinal, x in enumerate(exchanges, start=1):
        for data in x.images.values():
            record_image(conn, blobs, data)
        conn.execute(
            "INSERT INTO exchange (model_call_id, ordinal, method, path, attempt, status, body_text_sha, body_image,"
            " wire_sha, response_text_sha, response_image, content_type, seconds, error_code)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (call_id, ordinal, x.method, x.path, x.attempt, x.status,
             None if x.body_text is None else record_text(conn, x.body_text),
             None if x.body_image is None else record_image(conn, blobs, x.body_image), x.wire_sha,
             None if x.response_text is None else record_text(conn, x.response_text),
             None if x.response_image is None else record_image(conn, blobs, x.response_image),
             x.content_type, x.seconds, x.error))
    return call_id


def parts_of(conn: sqlite3.Connection, call_id: int) -> list[PartRow]:
    return [PartRow(int(r[0]), str(r[1]), str(r[2]), r[3], r[4], r[5], r[6], r[7], r[8], r[9], text(conn, r[10]))
            for r in conn.execute(
                "SELECT ordinal, slot, source_kind, file_sha, lesson_id, assessment_id, call_id, image_sha, setting_name,"
                " origin, text_sha FROM composition_part WHERE model_call_id = ? ORDER BY ordinal", (call_id,))]


def prompt_call_of(conn: sqlite3.Connection, iteration_id: int) -> int | None:
    """The writer or reviser call whose answer the iteration's generate or edit call used as its prompt."""
    row = conn.execute(
        "SELECT cp.call_id FROM model_call mc JOIN composition_part cp ON cp.model_call_id = mc.id"
        " WHERE mc.iteration_id = ? AND mc.role IN ('generate', 'edit') AND cp.source_kind = 'call_output'"
        " ORDER BY mc.id LIMIT 1", (iteration_id,)).fetchone()
    return None if row is None else int(row[0])


def exchanges_of(conn: sqlite3.Connection, call_id: int) -> list[tuple[int, str | None, str | None, str | None]]:
    """(ordinal, stored text body, body image hash, wire hash) per exchange of a call."""
    return [(int(r[0]), text(conn, r[1]), r[2], r[3]) for r in conn.execute(
        "SELECT ordinal, body_text_sha, body_image, wire_sha FROM exchange WHERE model_call_id = ? ORDER BY ordinal",
        (call_id,))]


# --- Assessments ------------------------------------------------------------------------------------------------


def add_assessment(conn: sqlite3.Connection, iteration_id: int, kind: str, verdict: str, call_id: int | None,
                   judgment: Judgment, measures: Sequence[Measure], item_ids: Sequence[int] = (),
                   thresholds: Mapping[str, float] | None = None) -> int:
    aid = int(conn.execute("INSERT INTO assessment (iteration_id, kind, verdict, model_call_id) VALUES (?, ?, ?, ?)",
                           (iteration_id, kind, verdict, call_id)).lastrowid or 0)
    for f in judgment.findings:
        box = (None,) * 4 if f.box is None else (f.box.x0, f.box.y0, f.box.x1, f.box.y1)
        fid = conn.execute("INSERT INTO finding (assessment_id, code, judged_severity, x0, y0, x1, y1, comment)"
                           " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (aid, f.code, f.judged_severity, *box, f.comment)).lastrowid
        conn.executemany("INSERT INTO finding_region (finding_id, n) VALUES (?, ?)", [(fid, n) for n in f.regions])
    for rank, guidance in enumerate(judgment.guidance, start=1):
        conn.execute("INSERT INTO guidance (assessment_id, rank, text_sha) VALUES (?, ?, ?)",
                     (aid, rank, record_text(conn, guidance)))
    answered = [r for r in judgment.regions if r.answered]
    conn.executemany("INSERT INTO region_answer (assessment_id, n, other_change) VALUES (?, ?, ?)",
                     [(aid, r.region, int(r.other_change)) for r in answered])
    conn.executemany("INSERT INTO region_item (assessment_id, n, clutter_item_id) VALUES (?, ?, ?)",
                     [(aid, r.region, item_ids[i - 1]) for r in answered for i in r.items])
    for m in measures:
        conn.execute("INSERT INTO measure (assessment_id, name, kind, value) VALUES (?, ?, 'value', ?)", (aid, m.name, m.value))
        if m.threshold is not None:
            conn.execute("INSERT INTO measure (assessment_id, name, kind, value) VALUES (?, ?, 'threshold', ?)",
                         (aid, m.name, m.threshold))
    for name, value in (thresholds or {}).items():
        conn.execute("INSERT INTO measure (assessment_id, name, kind, value) VALUES (?, ?, 'threshold', ?)",
                     (aid, name, value))
    return aid


def assessments(conn: sqlite3.Connection, iteration_id: int) -> list[AssessmentRow]:
    return [assessment(conn, int(r[0])) for r in
            conn.execute("SELECT id FROM assessment WHERE iteration_id = ? ORDER BY id", (iteration_id,))]


def assessment(conn: sqlite3.Connection, assessment_id: int) -> AssessmentRow:
    row = conn.execute("SELECT id, iteration_id, kind, verdict, model_call_id FROM assessment WHERE id = ?",
                       (assessment_id,)).fetchone()
    if row is None:
        raise LookupError(f"no assessment {assessment_id}")
    findings = tuple(
        Finding(str(r[0]), r[1], None if r[2] is None else Box(r[2], r[3], r[4], r[5]), str(r[6] or ""),
                tuple(int(n[0]) for n in conn.execute("SELECT n FROM finding_region WHERE finding_id = ? ORDER BY n",
                                                      (r[7],))))
        for r in conn.execute("SELECT code, judged_severity, x0, y0, x1, y1, comment, id FROM finding"
                              " WHERE assessment_id = ? ORDER BY id", (assessment_id,)).fetchall())
    guidance = tuple(str(text(conn, r[0])) for r in
                     conn.execute("SELECT text_sha FROM guidance WHERE assessment_id = ? ORDER BY rank", (assessment_id,)))
    regions: tuple[RegionItems, ...] = ()
    if row[2] == "judge" and region_set(conn, int(row[1])) is not None:  # every numbered region, answered or not
        other = {int(r[0]): bool(r[1]) for r in conn.execute(
            "SELECT n, other_change FROM region_answer WHERE assessment_id = ?", (assessment_id,))}
        held: dict[int, list[int]] = {}
        for n, ordinal in conn.execute("SELECT r.n, i.ordinal FROM region_item r JOIN clutter_item i"
                                       " ON i.id = r.clutter_item_id WHERE r.assessment_id = ? ORDER BY r.n, i.ordinal",
                                       (assessment_id,)):
            held.setdefault(int(n), []).append(int(ordinal))
        regions = tuple(RegionItems(n, tuple(held.get(n, [])), other.get(n, False), n in other)
                        for n, _, _ in mask_regions(conn, int(row[1])))
    values: dict[str, list[float | None]] = {}
    for name, kind, value in conn.execute("SELECT name, kind, value FROM measure WHERE assessment_id = ?"
                                          " ORDER BY rowid", (assessment_id,)):
        values.setdefault(str(name), [None, None])[0 if kind == "value" else 1] = float(value)
    measures = tuple(Measure(n, v[0], v[1]) for n, v in values.items() if v[0] is not None)
    thresholds = {n: float(v[1]) for n, v in values.items() if v[0] is None and v[1] is not None}
    return AssessmentRow(int(row[0]), int(row[1]), str(row[2]), str(row[3]), row[4],
                         Judgment(findings, guidance, regions), measures, thresholds)


def all_assessment_ids(conn: sqlite3.Connection) -> list[int]:
    return [int(r[0]) for r in conn.execute("SELECT id FROM assessment ORDER BY id")]


# --- Lessons and decisions ---------------------------------------------------------------------------------------


def active_lessons(conn: sqlite3.Connection, stage: str, wave_id: int) -> list[Lesson]:
    rows = conn.execute(
        "SELECT id, text_sha FROM lesson WHERE stage = ? AND active_from_wave_id <= ?"
        " AND (ended_wave_id IS NULL OR ended_wave_id > ?) ORDER BY id", (stage, wave_id, wave_id)).fetchall()
    return [Lesson(int(r[0]), stage, str(text(conn, r[1])), lesson_scope(conn, int(r[0]))) for r in rows]  # type: ignore[arg-type]


def lesson(conn: sqlite3.Connection, lesson_id: int) -> Lesson:
    row = conn.execute("SELECT id, stage, text_sha FROM lesson WHERE id = ?", (lesson_id,)).fetchone()
    if row is None:
        raise LookupError(f"no lesson {lesson_id}")
    return Lesson(int(row[0]), row[1], str(text(conn, row[2])), lesson_scope(conn, lesson_id))


def lesson_scope(conn: sqlite3.Connection, lesson_id: int) -> tuple[tuple[str, str], ...]:
    return tuple((str(a), str(v)) for a, v in conn.execute(
        "SELECT axis, value FROM lesson_scope WHERE lesson_id = ? ORDER BY axis", (lesson_id,)))


def lessons_table(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute(
        "SELECT l.id, l.stage, l.text_sha, l.active_from_wave_id, l.ended_wave_id, l.end_kind, l.replaces_lesson_id,"
        " (SELECT COUNT(*) FROM lesson_use u WHERE u.lesson_id = l.id) FROM lesson l ORDER BY l.id").fetchall()
    return [{"id": r[0], "stage": r[1], "text": text(conn, r[2]), "active_from_wave": r[3], "ended_wave": r[4],
             "end_kind": r[5], "replaces": r[6], "scope": [list(s) for s in lesson_scope(conn, int(r[0]))],
             "used_by_loops": r[7]} for r in rows]


def unprocessed_distill_calls(conn: sqlite3.Connection, actor: str) -> list[CallRow]:
    """Distill calls that answered and that the activation rule (`actor`) has not processed yet."""
    done = {int(json.loads(d)["distill_call"]) for (d,) in
            conn.execute("SELECT detail FROM decision WHERE actor = ? AND action = 'decision_rule'", (actor,))}
    calls = [_call(conn, r) for r in conn.execute(
        f"{_CALL} WHERE role = 'distill' AND error_code IS NULL AND reused_call_id IS NULL ORDER BY id")]
    return [c for c in calls if c.id not in done]


def insert_lesson(conn: sqlite3.Connection, stage: str, new: NewLesson, distill_call_id: int, wave_id: int,
                  evidence_iteration_ids: Iterable[int]) -> int:
    lid = int(conn.execute(
        "INSERT INTO lesson (stage, text_sha, distill_call_id, replaces_lesson_id, active_from_wave_id)"
        " VALUES (?, ?, ?, ?, ?)",
        (stage, record_text(conn, new.text), distill_call_id, new.replaces, wave_id)).lastrowid or 0)
    conn.executemany("INSERT INTO lesson_evidence (lesson_id, iteration_id) VALUES (?, ?) ON CONFLICT DO NOTHING",
                     [(lid, i) for i in evidence_iteration_ids])
    conn.executemany("INSERT INTO lesson_scope (lesson_id, axis, value) VALUES (?, ?, ?)",
                     [(lid, a, v) for a, v in new.scope])
    return lid


def end_lesson(conn: sqlite3.Connection, lesson_id: int, wave_id: int, kind: str) -> bool:
    cur = conn.execute("UPDATE lesson SET ended_wave_id = ?, end_kind = ? WHERE id = ? AND ended_wave_id IS NULL",
                       (wave_id, kind, lesson_id))
    return cur.rowcount > 0


def pending_lesson_ends(conn: sqlite3.Connection) -> list[tuple[int, str]]:
    """The owner's retirements and promotions of lessons still active: (lesson id, end kind)."""
    return [(int(r[0]), "retired" if r[1] == "lesson_retire" else "promoted") for r in conn.execute(
        "SELECT d.lesson_id, d.action FROM decision d JOIN lesson l ON l.id = d.lesson_id"
        " WHERE d.action IN ('lesson_retire', 'lesson_promote') AND l.ended_wave_id IS NULL ORDER BY d.id")]


def add_decision(conn: sqlite3.Connection, now: str, actor: str, action: str, detail: Mapping[str, object],
                 lesson_id: int | None = None, assessment_id: int | None = None) -> int:
    return int(conn.execute(
        "INSERT INTO decision (at, actor, action, lesson_id, assessment_id, detail) VALUES (?, ?, ?, ?, ?, ?)",
        (now, actor, action, lesson_id, assessment_id, json.dumps(detail, sort_keys=True))).lastrowid or 0)


def threshold_decisions(conn: sqlite3.Connection) -> dict[str, float]:
    """The owner's thresholds in force: the latest value set for each name."""
    out: dict[str, float] = {}
    for (detail,) in conn.execute("SELECT detail FROM decision WHERE action = 'threshold_set' ORDER BY id"):
        data = json.loads(detail)
        out[str(data["name"])] = float(data["value"])
    return out


def evidence_iterations(conn: sqlite3.Connection, loop_id: int) -> dict[int, int]:
    """Iteration number to id, for a loop."""
    return {int(r[0]): int(r[1]) for r in conn.execute("SELECT n, id FROM iteration WHERE loop_run_id = ?", (loop_id,))}


# --- Views for the report, the audit and the export ----------------------------------------------------------


def query(conn: sqlite3.Connection, view: str) -> list[dict[str, object]]:
    """All rows of a view, by its name from a fixed list."""
    allowed = {"coverage", "iteration_curve", "carry_forward", "carry_forward_loop", "lesson_use", "call_cost", "pair"}
    if view not in allowed:
        raise ValueError(f"unknown view {view}")
    cur = conn.execute(f"SELECT * FROM {view}")
    names = [d[0] for d in cur.description]
    return [dict(zip(names, row, strict=True)) for row in cur.fetchall()]


def target_values(conn: sqlite3.Connection, target_id: int) -> Values:
    return tuple((str(a), str(v)) for a, v in conn.execute(
        "SELECT axis, value FROM target_value WHERE target_id = ? ORDER BY axis", (target_id,)))


def latest_target_set(conn: sqlite3.Connection) -> int | None:
    row = conn.execute("SELECT target_set_id FROM run ORDER BY id DESC LIMIT 1").fetchone()
    if row is None:
        row = conn.execute("SELECT MAX(id) FROM target_set").fetchone()
    return None if row is None or row[0] is None else int(row[0])


def runs(conn: sqlite3.Connection) -> list[dict[str, object]]:
    cur = conn.execute(
        "SELECT r.id, r.started_at, r.ended_at, r.target_pairs, r.rental_id, t.price_per_hour, t.started_at AS rental_start,"
        " t.ended_at AS rental_end, t.deadline FROM run r LEFT JOIN rental t ON t.id = r.rental_id ORDER BY r.id")
    names = [d[0] for d in cur.description]
    return [dict(zip(names, row, strict=True)) for row in cur.fetchall()]


def pair_values(conn: sqlite3.Connection, pair_id: int) -> Values:
    return tuple(sorted((str(a), str(v)) for a, v in
                        conn.execute("SELECT axis, value FROM pair_value WHERE pair_id = ?", (pair_id,))))


def create_export(conn: sqlite3.Connection, name: str, now: str, manifest_sha: str,
                  splits: Mapping[int, str], pair_ids: Iterable[int]) -> int:
    eid = int(conn.execute("INSERT INTO export (name, created_at, manifest_sha) VALUES (?, ?, ?)",
                           (name, now, manifest_sha)).lastrowid or 0)
    conn.executemany("INSERT INTO export_building (export_id, building_id, split) VALUES (?, ?, ?)",
                     [(eid, b, s) for b, s in splits.items()])
    conn.executemany("INSERT INTO export_pair (export_id, iteration_id) VALUES (?, ?)", [(eid, p) for p in pair_ids])
    return eid


def export_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute("SELECT 1 FROM export WHERE name = ?", (name,)).fetchone() is not None


def export_problems(conn: sqlite3.Connection) -> list[str]:
    """Exported pairs that are not accepted pairs, or whose building has no split in that export (P6)."""
    out = [f"export {r[0]}: iteration {r[1]} is not an accepted pair" for r in conn.execute(
        "SELECT e.export_id, e.iteration_id FROM export_pair e WHERE NOT EXISTS"
        " (SELECT 1 FROM pair p WHERE p.pair_id = e.iteration_id)")]
    out += [f"export {r[0]}: pair {r[1]}'s building has no split" for r in conn.execute(
        "SELECT e.export_id, e.iteration_id FROM export_pair e JOIN pair p ON p.pair_id = e.iteration_id"
        " WHERE NOT EXISTS (SELECT 1 FROM export_building b WHERE b.export_id = e.export_id"
        " AND b.building_id = p.building_id)")]
    return out


def loops_with_bad_input(conn: sqlite3.Connection) -> list[int]:
    """Clutter loops whose input image is not an accepted clean image of their scene."""
    return [int(r[0]) for r in conn.execute(
        "SELECT l.id FROM loop_run l JOIN clutter_spec c ON c.id = l.clutter_spec_id WHERE l.stage = 'clutter'"
        " AND NOT EXISTS (SELECT 1 FROM clean_image ci WHERE ci.scene_id = c.scene_id AND ci.image_sha = l.input_image)")]


def misplaced_image_roles(conn: sqlite3.Connection) -> list[tuple[int, str]]:
    """Images whose role does not fit their loop: `generated` on the clean loop of a scene that was not imported,
    `imported` on the one of an imported scene, the other roles on clutter loops."""
    return [(int(r[0]), str(r[1])) for r in conn.execute(
        "SELECT ii.iteration_id, ii.role FROM iteration_image ii JOIN iteration it ON it.id = ii.iteration_id"
        " JOIN loop_run l ON l.id = it.loop_run_id"
        " WHERE NOT ((l.stage = 'clean' AND ii.role = 'generated'"
        "             AND NOT EXISTS (SELECT 1 FROM imported_image im WHERE im.scene_id = l.scene_id))"
        "         OR (l.stage = 'clean' AND ii.role = 'imported'"
        "             AND EXISTS (SELECT 1 FROM imported_image im WHERE im.scene_id = l.scene_id))"
        "         OR (l.stage = 'clutter' AND ii.role NOT IN ('generated', 'imported')))")]


def loop_of_iteration(conn: sqlite3.Connection, iteration_id: int) -> int:
    return int(conn.execute("SELECT loop_run_id FROM iteration WHERE id = ?", (iteration_id,)).fetchone()[0])


def all_iterations(conn: sqlite3.Connection) -> list[IterationRow]:
    return [IterationRow(int(r[0]), int(r[1]), int(r[2]), str(r[3]), int(r[4]), r[5]) for r in conn.execute(
        "SELECT id, loop_run_id, n, action, seed, verdict FROM iteration ORDER BY id")]
