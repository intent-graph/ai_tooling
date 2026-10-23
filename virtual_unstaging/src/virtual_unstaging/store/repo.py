"""Every query of the project database. Writes are called inside `db.transaction`; reads anywhere."""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

from virtual_unstaging.domain import (
    Box,
    DefectStep,
    DefectType,
    Dimension,
    Finding,
    Level,
    Move,
    Point,
    Release,
    Score,
    Spent,
    canonical_json,
    sha256_text,
)


def now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def _one(conn: sqlite3.Connection, sql: str, params: Sequence[object] = ()) -> sqlite3.Row | None:
    row: sqlite3.Row | None = conn.execute(sql, params).fetchone()
    return row


def _id(cursor: sqlite3.Cursor) -> int:
    assert cursor.lastrowid is not None
    return cursor.lastrowid


# --- Reference data ------------------------------------------------------------------------------------------


def ensure_defect_types(conn: sqlite3.Connection, defects: Iterable[DefectType]) -> None:
    conn.executemany(
        "INSERT INTO defect_type (code, label, description) VALUES (?, ?, ?) "
        "ON CONFLICT (code) DO UPDATE SET label = excluded.label, description = excluded.description",
        [(d.code, d.label, d.description) for d in defects],
    )


def ensure_model(conn: sqlite3.Connection, role: str, name: str, revision: str) -> int:
    conn.execute("INSERT OR IGNORE INTO model (role, name, revision) VALUES (?, ?, ?)", (role, name, revision))
    row = _one(conn, "SELECT model_id FROM model WHERE role = ? AND name = ? AND revision = ?", (role, name, revision))
    assert row is not None
    return int(row[0])


def ensure_instruction_set(
    conn: sqlite3.Connection, role: str, target_model: str, layer: str, body: str, layered_on_id: int | None
) -> int:
    sha = sha256_text(canonical_json([role, target_model, layer, layered_on_id, body]))
    row = _one(conn, "SELECT instruction_set_id FROM instruction_set WHERE sha256 = ?", (sha,))
    if row:
        return int(row[0])
    previous = _one(
        conn,
        "SELECT MAX(instruction_set_id) FROM instruction_set WHERE role = ? AND target_model = ? AND layer = ?",
        (role, target_model, layer),
    )
    cursor = conn.execute(
        "INSERT INTO instruction_set (role, target_model, layer, layered_on_id, previous_id, body, sha256, created_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (role, target_model, layer, layered_on_id, previous[0] if previous else None, body, sha, now()),
    )
    return _id(cursor)


def ensure_release(conn: sqlite3.Connection, release: Release) -> tuple[int, dict[str, int]]:
    """Store a registry release and its dimensions (deduplicated by content hash); return the ids."""
    ids: dict[str, int] = {}
    for dim in release.dimensions:
        sha = sha256_text(canonical_json(dim.definition()))
        row = _one(conn, "SELECT dimension_id FROM dimension WHERE sha256 = ?", (sha,))
        if row:
            ids[dim.key] = int(row[0])
            continue
        cursor = conn.execute(
            "INSERT INTO dimension (key, input, realizer, slot, role, setting, layer, origin, default_ordinal, "
            "probe_cost, sha256) VALUES (?, ?, ?, ?, ?, ?, 'base', 'preloaded', ?, ?, ?)",
            (dim.key, dim.input, dim.realizer, dim.slot, dim.role, dim.setting, dim.default_ordinal, dim.probe_cost, sha),
        )
        dim_id = _id(cursor)
        ids[dim.key] = dim_id
        conn.executemany(
            "INSERT INTO dimension_level (dimension_id, ordinal, label, realization_json) VALUES (?, ?, ?, ?)",
            [(dim_id, lv.ordinal, lv.label, canonical_json(dict(lv.realization))) for lv in dim.levels],
        )
        conn.executemany(
            "INSERT INTO dimension_target (dimension_id, defect_code) VALUES (?, ?)", [(dim_id, t) for t in dim.targets]
        )
    row = _one(conn, "SELECT registry_release_id FROM registry_release WHERE sha256 = ?", (release.sha256,))
    if row:
        return int(row[0]), ids
    release_id = _id(
        conn.execute("INSERT INTO registry_release (sha256, created_at) VALUES (?, ?)", (release.sha256, now()))
    )
    conn.executemany(
        "INSERT INTO release_dimension (registry_release_id, dimension_id, position) VALUES (?, ?, ?)",
        [(release_id, ids[d.key], pos) for pos, d in enumerate(release.dimensions)],
    )
    conn.executemany(
        "INSERT INTO defect_dimension (registry_release_id, defect_code, dimension_id, direction, priority) "
        "VALUES (?, ?, ?, ?, ?)",
        [(release_id, s.defect, ids[s.dimension], s.direction, s.priority) for s in release.defect_map],
    )
    return release_id, ids


def load_release(conn: sqlite3.Connection, release_id: int) -> Release:
    """Rebuild a release from the database, so a resumed run uses what it started with, whatever the files say."""
    rows = conn.execute(
        "SELECT d.* FROM release_dimension r JOIN dimension d USING (dimension_id) "
        "WHERE r.registry_release_id = ? ORDER BY r.position",
        (release_id,),
    ).fetchall()
    dimensions: list[Dimension] = []
    for row in rows:
        levels = tuple(
            Level(int(r[0]), str(r[1]), json.loads(r[2]))
            for r in conn.execute(
                "SELECT ordinal, label, realization_json FROM dimension_level WHERE dimension_id = ? ORDER BY ordinal",
                (row["dimension_id"],),
            )
        )
        targets = tuple(
            str(r[0])
            for r in conn.execute(
                "SELECT defect_code FROM dimension_target WHERE dimension_id = ? ORDER BY defect_code",
                (row["dimension_id"],),
            )
        )
        dimensions.append(
            Dimension(
                key=row["key"], input=row["input"], realizer=row["realizer"], levels=levels,
                default_ordinal=int(row["default_ordinal"]), probe_cost=float(row["probe_cost"]), targets=targets,
                slot=row["slot"], role=row["role"], setting=row["setting"],
            )
        )
    steps = tuple(
        DefectStep(str(r[0]), str(r[1]), int(r[2]), int(r[3]))
        for r in conn.execute(
            "SELECT m.defect_code, d.key, m.direction, m.priority FROM defect_dimension m JOIN dimension d "
            "USING (dimension_id) WHERE m.registry_release_id = ? ORDER BY m.defect_code, m.priority",
            (release_id,),
        )
    )
    sha = _one(conn, "SELECT sha256 FROM registry_release WHERE registry_release_id = ?", (release_id,))
    assert sha is not None
    return Release(tuple(dimensions), steps, str(sha[0]))


def instruction_layers(conn: sqlite3.Connection, instruction_set_id: int) -> tuple[str, str | None, str]:
    """(base body, project overlay body or None, target model) of an instruction set and what it is layered on."""
    row = _one(
        conn, "SELECT body, layer, layered_on_id, target_model FROM instruction_set WHERE instruction_set_id = ?",
        (instruction_set_id,),
    )
    if row is None:
        raise LookupError(f"no instruction set {instruction_set_id}")
    if row["layer"] == "base":
        return str(row["body"]), None, str(row["target_model"])
    base = _one(conn, "SELECT body FROM instruction_set WHERE instruction_set_id = ?", (row["layered_on_id"],))
    assert base is not None
    return str(base[0]), str(row["body"]), str(row["target_model"])


def model_ref(conn: sqlite3.Connection, model_id: int) -> tuple[str, str]:
    row = _one(conn, "SELECT name, revision FROM model WHERE model_id = ?", (model_id,))
    assert row is not None
    return str(row[0]), str(row[1])


def defect_types(conn: sqlite3.Connection) -> tuple[DefectType, ...]:
    return tuple(
        DefectType(str(r[0]), str(r[1]), str(r[2]))
        for r in conn.execute("SELECT code, label, description FROM defect_type ORDER BY rowid")
    )


def release_dimension_ids(conn: sqlite3.Connection, release_id: int) -> dict[str, int]:
    rows = conn.execute(
        "SELECT d.key, d.dimension_id FROM release_dimension r JOIN dimension d USING (dimension_id) "
        "WHERE r.registry_release_id = ?",
        (release_id,),
    )
    return {str(r[0]): int(r[1]) for r in rows}


# --- Project content -----------------------------------------------------------------------------------------


def ensure_image(conn: sqlite3.Connection, sha: str, width: int, height: int, media_type: str) -> None:
    conn.execute(
        "INSERT OR IGNORE INTO image (sha256, width, height, media_type) VALUES (?, ?, ?, ?)",
        (sha, width, height, media_type),
    )


def ensure_group(conn: sqlite3.Connection, name: str) -> int:
    conn.execute("INSERT OR IGNORE INTO photo_group (name) VALUES (?)", (name,))
    row = _one(conn, "SELECT group_id FROM photo_group WHERE name = ?", (name,))
    assert row is not None
    return int(row[0])


def add_photo(conn: sqlite3.Connection, group_id: int | None, sha: str, source_name: str) -> tuple[int, bool]:
    """Insert a photo; importing the same file again is a no-op, a different file under a known name an error."""
    row = _one(conn, "SELECT photo_id, image_sha256 FROM photo WHERE source_name = ?", (source_name,))
    if row:
        if row[1] != sha:
            raise ValueError(f"a different photo is already imported as {source_name!r}")
        return int(row[0]), False
    cursor = conn.execute(
        "INSERT INTO photo (group_id, image_sha256, source_name, added_at) VALUES (?, ?, ?, ?)",
        (group_id, sha, source_name, now()),
    )
    return _id(cursor), True


@dataclass(frozen=True)
class PhotoRow:
    photo_id: int
    source_name: str
    image_sha256: str
    group_id: int | None
    group_name: str | None
    width: int
    height: int


def photos(conn: sqlite3.Connection, names: Sequence[str] | None = None) -> list[PhotoRow]:
    sql = (
        "SELECT p.photo_id, p.source_name, p.image_sha256, p.group_id, g.name, i.width, i.height "
        "FROM photo p JOIN image i ON i.sha256 = p.image_sha256 LEFT JOIN photo_group g USING (group_id)"
    )
    rows = conn.execute(sql + " ORDER BY p.source_name").fetchall()
    result = [PhotoRow(*row) for row in rows]
    if names is None:
        return result
    by_name = {p.source_name: p for p in result}
    missing = [n for n in names if n not in by_name]
    if missing:
        raise KeyError(f"unknown photos: {missing}")
    return [by_name[n] for n in names]


def insert_rule_set(conn: sqlite3.Connection, items: Sequence[tuple[str | None, str, str, str | None]]) -> int:
    """Items: (group name or None for the whole project, element, 'fixed' or 'movable', note)."""
    sha = sha256_text(canonical_json(sorted([list(i) for i in items], key=lambda i: [str(x) for x in i])))
    row = _one(conn, "SELECT rule_set_id FROM rule_set WHERE sha256 = ?", (sha,))
    if row:
        return int(row[0])
    rule_set_id = _id(conn.execute("INSERT INTO rule_set (sha256, created_at) VALUES (?, ?)", (sha, now())))
    for group, element, disposition, note in items:
        group_id = ensure_group(conn, group) if group else None
        conn.execute(
            "INSERT INTO rule_item (rule_set_id, group_id, element, disposition, note) VALUES (?, ?, ?, ?, ?)",
            (rule_set_id, group_id, element, disposition, note),
        )
    return rule_set_id


def latest_rule_set(conn: sqlite3.Connection) -> int:
    row = _one(conn, "SELECT MAX(rule_set_id) FROM rule_set")
    if row is None or row[0] is None:
        raise LookupError("no content rules yet: run `rules` first")
    return int(row[0])


def rules_for(conn: sqlite3.Connection, rule_set_id: int, group_id: int | None) -> tuple[list[str], list[str]]:
    """Fixed and movable elements that apply to a group: the project-wide ones and the group's own."""
    rows = conn.execute(
        "SELECT element, disposition FROM rule_item WHERE rule_set_id = ? AND (group_id IS NULL OR group_id IS ?) "
        "ORDER BY group_id IS NOT NULL, rule_item_id",
        (rule_set_id, group_id),
    ).fetchall()
    fixed = [str(r[0]) for r in rows if r[1] == "fixed"]
    movable = [str(r[0]) for r in rows if r[1] == "movable"]
    return fixed, movable


# --- Tool runs and stage 0 -----------------------------------------------------------------------------------


@dataclass(frozen=True)
class ToolRunRow:
    tool_run_id: int
    outputs: dict[str, str]
    measures: dict[str, Any]
    summary: str
    gpu_seconds: float


def tool_run_key(tool: str, version: str, params: Mapping[str, object], inputs: Sequence[str]) -> str:
    return sha256_text(canonical_json({"tool": tool, "version": version, "params": dict(params), "inputs": list(inputs)}))


def find_tool_run(conn: sqlite3.Connection, cache_key: str) -> ToolRunRow | None:
    row = _one(conn, "SELECT tool_run_id, measures_json, summary, gpu_seconds FROM tool_run WHERE cache_key = ?", (cache_key,))
    if row is None:
        return None
    outputs = {
        str(r[0]): str(r[1])
        for r in conn.execute("SELECT name, image_sha256 FROM tool_run_output WHERE tool_run_id = ?", (row[0],))
    }
    return ToolRunRow(int(row[0]), outputs, json.loads(row[1] or "{}"), row[2] or "", float(row[3]))


def insert_tool_run(
    conn: sqlite3.Connection,
    tool: str,
    version: str,
    params: Mapping[str, object],
    inputs: Sequence[str],
    outputs: Mapping[str, str],
    measures: Mapping[str, object],
    summary: str,
    gpu_seconds: float,
) -> ToolRunRow:
    key = tool_run_key(tool, version, params, inputs)
    existing = find_tool_run(conn, key)
    if existing:
        return existing
    tool_run_id = _id(
        conn.execute(
            "INSERT INTO tool_run (tool, tool_version, params_json, cache_key, measures_json, summary, gpu_seconds, "
            "created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (tool, version, canonical_json(dict(params)), key, canonical_json(dict(measures)), summary, gpu_seconds, now()),
        )
    )
    conn.executemany(
        "INSERT INTO tool_run_input (tool_run_id, position, image_sha256) VALUES (?, ?, ?)",
        [(tool_run_id, pos, sha) for pos, sha in enumerate(inputs)],
    )
    conn.executemany(
        "INSERT INTO tool_run_output (tool_run_id, name, image_sha256) VALUES (?, ?, ?)",
        [(tool_run_id, name, sha) for name, sha in outputs.items()],
    )
    return ToolRunRow(tool_run_id, dict(outputs), dict(measures), summary, gpu_seconds)


def set_eligibility(
    conn: sqlite3.Connection,
    photo_id: int,
    rule_set_id: int,
    decision: str,
    reason: str | None,
    measures: Mapping[str, object],
    removal_mask_tool_run_id: int | None,
    protected_mask_tool_run_id: int | None,
) -> None:
    conn.execute(
        "INSERT INTO eligibility (photo_id, rule_set_id, decision, reason, measures_json, removal_mask_tool_run_id, "
        "protected_mask_tool_run_id, decided_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?) "
        "ON CONFLICT (photo_id, rule_set_id) DO UPDATE SET decision = excluded.decision, reason = excluded.reason, "
        "measures_json = excluded.measures_json, removal_mask_tool_run_id = excluded.removal_mask_tool_run_id, "
        "protected_mask_tool_run_id = excluded.protected_mask_tool_run_id, decided_at = excluded.decided_at",
        (photo_id, rule_set_id, decision, reason, canonical_json(dict(measures)), removal_mask_tool_run_id,
         protected_mask_tool_run_id, now()),
    )


@dataclass(frozen=True)
class EligibilityRow:
    decision: str
    reason: str | None
    measures: dict[str, Any]
    removal_mask: str | None
    protected_mask: str | None


def eligibility(conn: sqlite3.Connection, photo_id: int, rule_set_id: int) -> EligibilityRow | None:
    row = _one(
        conn,
        "SELECT e.decision, e.reason, e.measures_json, rm.image_sha256, pm.image_sha256 FROM eligibility e "
        "LEFT JOIN tool_run_output rm ON rm.tool_run_id = e.removal_mask_tool_run_id AND rm.name = 'mask' "
        "LEFT JOIN tool_run_output pm ON pm.tool_run_id = e.protected_mask_tool_run_id AND pm.name = 'mask' "
        "WHERE e.photo_id = ? AND e.rule_set_id = ?",
        (photo_id, rule_set_id),
    )
    if row is None:
        return None
    return EligibilityRow(row[0], row[1], json.loads(row[2]), row[3], row[4])


# --- Runs and optimizations ----------------------------------------------------------------------------------


def create_run(conn: sqlite3.Connection, **fields: object) -> int:
    columns = ", ".join(fields)
    marks = ", ".join("?" for _ in fields)
    return _id(conn.execute(f"INSERT INTO run ({columns}, started_at) VALUES ({marks}, ?)", (*fields.values(), now())))


def run_row(conn: sqlite3.Connection, run_id: int) -> sqlite3.Row:
    row = _one(conn, "SELECT * FROM run WHERE run_id = ?", (run_id,))
    if row is None:
        raise LookupError(f"no run {run_id}")
    return row


def end_run(conn: sqlite3.Connection, run_id: int) -> None:
    conn.execute(
        "UPDATE run SET ended_at = ? WHERE run_id = ? AND NOT EXISTS "
        "(SELECT 1 FROM optimization WHERE run_id = ? AND status = 'running')",
        (now(), run_id, run_id),
    )


def create_optimization(conn: sqlite3.Connection, run_id: int, photo_id: int, seed: int) -> int:
    cursor = conn.execute(
        "INSERT INTO optimization (run_id, photo_id, seed, status, started_at) VALUES (?, ?, ?, 'running', ?)",
        (run_id, photo_id, seed, now()),
    )
    return _id(cursor)


def optimizations(conn: sqlite3.Connection, run_id: int, status: str | None = None) -> list[sqlite3.Row]:
    sql = "SELECT * FROM optimization WHERE run_id = ?"
    params: list[object] = [run_id]
    if status:
        sql += " AND status = ?"
        params.append(status)
    return conn.execute(sql + " ORDER BY optimization_id", params).fetchall()


def finish_optimization(
    conn: sqlite3.Connection, optimization_id: int, status: str, stop_reason: str, error: str | None = None
) -> int | None:
    """Close an optimization and record its best attempt: best score, then earliest (one SQL definition)."""
    best = _one(
        conn,
        "SELECT a.attempt_id FROM attempt a JOIN judgment_score s ON s.attempt_id = a.attempt_id "
        "WHERE a.optimization_id = ? ORDER BY s.blocking, s.minor, a.seq LIMIT 1",
        (optimization_id,),
    )
    best_id = int(best[0]) if best else None
    conn.execute(
        "UPDATE optimization SET status = ?, stop_reason = ?, best_attempt_id = ?, error = ?, ended_at = ? "
        "WHERE optimization_id = ?",
        (status, stop_reason, best_id, error, now(), optimization_id),
    )
    return best_id


def spent(conn: sqlite3.Connection, optimization_id: int) -> Spent:
    row = _one(
        conn,
        "SELECT (SELECT COUNT(*) FROM attempt WHERE optimization_id = ?), "
        "(SELECT COALESCE(SUM(gpu_seconds), 0) FROM attempt WHERE optimization_id = ?) + "
        "(SELECT COALESCE(SUM(t.gpu_seconds), 0) FROM judgment j JOIN judgment_tool_run jt USING (judgment_id) "
        "  JOIN tool_run t USING (tool_run_id) JOIN attempt a USING (attempt_id) WHERE a.optimization_id = ?), "
        "(SELECT COUNT(*) FILTER (WHERE j.cached = 0) FROM judgment j JOIN attempt a USING (attempt_id) "
        "  WHERE a.optimization_id = ?)",
        (optimization_id, optimization_id, optimization_id, optimization_id),
    )
    assert row is not None
    return Spent(int(row[0]), float(row[1]), int(row[2]))


# --- Attempts and judgments ----------------------------------------------------------------------------------


def find_generation(conn: sqlite3.Connection, request_sha: str) -> str | None:
    """The output of an earlier, successful attempt with the same request: the generation cache (design D12)."""
    row = _one(
        conn,
        "SELECT output_sha256 FROM attempt WHERE request_sha256 = ? AND output_sha256 IS NOT NULL "
        "ORDER BY attempt_id LIMIT 1",
        (request_sha,),
    )
    return str(row[0]) if row else None


def next_seq(conn: sqlite3.Connection, optimization_id: int) -> int:
    row = _one(conn, "SELECT COALESCE(MAX(seq), 0) + 1 FROM attempt WHERE optimization_id = ?", (optimization_id,))
    assert row is not None
    return int(row[0])


def insert_attempt(
    conn: sqlite3.Connection,
    optimization_id: int,
    seed: int,
    prompt: str,
    settings: Mapping[str, object],
    request_sha: str,
    output_sha: str | None,
    gpu_seconds: float,
    cached: bool,
    error: str | None,
    levels: Mapping[int, int],
    images: Sequence[tuple[str, str, int | None]],
) -> int:
    """`levels`: dimension id -> ordinal. `images`: (role, sha, tool run that built it) in the order sent."""
    attempt_id = _id(
        conn.execute(
            "INSERT INTO attempt (optimization_id, seq, seed, prompt, settings_json, request_sha256, output_sha256, "
            "gpu_seconds, cached, error, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (optimization_id, next_seq(conn, optimization_id), seed, prompt, canonical_json(dict(settings)), request_sha,
             output_sha, gpu_seconds, int(cached), error, now()),
        )
    )
    conn.executemany(
        "INSERT INTO attempt_level (attempt_id, dimension_id, ordinal) VALUES (?, ?, ?)",
        [(attempt_id, dim_id, ordinal) for dim_id, ordinal in levels.items()],
    )
    conn.executemany(
        "INSERT INTO attempt_image (attempt_id, position, role, image_sha256, tool_run_id) VALUES (?, ?, ?, ?, ?)",
        [(attempt_id, pos, role, sha, tool_run) for pos, (role, sha, tool_run) in enumerate(images)],
    )
    return attempt_id


@dataclass(frozen=True)
class StoredJudgment:
    raw_response: str
    own_verdict: str | None
    critique: str
    findings: tuple[Finding, ...]
    moves: tuple[Move, ...]


def find_judgment(conn: sqlite3.Connection, request_sha: str, judge_model_id: int, instruction_set_id: int) -> int | None:
    row = _one(
        conn,
        "SELECT judgment_id FROM judgment WHERE request_sha256 = ? AND judge_model_id = ? AND instruction_set_id = ? "
        "AND parse_error IS NULL ORDER BY judgment_id LIMIT 1",
        (request_sha, judge_model_id, instruction_set_id),
    )
    return int(row[0]) if row else None


def load_judgment(conn: sqlite3.Connection, judgment_id: int) -> StoredJudgment:
    row = _one(conn, "SELECT raw_response, own_verdict, critique FROM judgment WHERE judgment_id = ?", (judgment_id,))
    assert row is not None
    findings = tuple(
        Finding(r[0], r[1], Box(r[2], r[3], r[4], r[5]) if r[2] is not None else None, r[6] or "")
        for r in conn.execute(
            "SELECT defect_code, severity, x0, y0, x1, y1, comment FROM finding WHERE judgment_id = ? ORDER BY finding_id",
            (judgment_id,),
        )
    )
    moves = tuple(
        Move(r[0], int(r[1]), r[2], r[3] or "")
        for r in conn.execute(
            "SELECT d.key, m.to_ordinal, m.targets_defect, m.reason FROM move m JOIN dimension d USING (dimension_id) "
            "WHERE m.judgment_id = ? ORDER BY m.rank",
            (judgment_id,),
        )
    )
    return StoredJudgment(row[0], row[1], row[2] or "", findings, moves)


def insert_judgment(
    conn: sqlite3.Connection,
    attempt_id: int,
    judge_model_id: int,
    instruction_set_id: int,
    raw_response: str,
    request_sha: str,
    wall_seconds: float,
    cached: bool,
    parse_error: str | None,
    own_verdict: str | None = None,
    critique: str | None = None,
    findings: Sequence[Finding] = (),
    moves: Sequence[Move] = (),
    dimension_ids: Mapping[str, int] | None = None,
    tool_run_ids: Sequence[int] = (),
) -> int:
    judgment_id = _id(
        conn.execute(
            "INSERT INTO judgment (attempt_id, judge_model_id, instruction_set_id, own_verdict, critique, raw_response, "
            "parse_error, request_sha256, cached, wall_seconds, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (attempt_id, judge_model_id, instruction_set_id, own_verdict, critique, raw_response, parse_error,
             request_sha, int(cached), wall_seconds, now()),
        )
    )
    conn.executemany(
        "INSERT INTO finding (judgment_id, defect_code, severity, x0, y0, x1, y1, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (judgment_id, f.code, f.severity, *((f.box.x0, f.box.y0, f.box.x1, f.box.y1) if f.box else (None,) * 4), f.comment)
            for f in findings
        ],
    )
    if moves:
        assert dimension_ids is not None
        conn.executemany(
            "INSERT INTO move (judgment_id, rank, dimension_id, to_ordinal, targets_defect, reason) VALUES (?, ?, ?, ?, ?, ?)",
            [(judgment_id, rank, dimension_ids[m.dimension], m.to_ordinal, m.targets, m.reason)
             for rank, m in enumerate(moves, start=1)],
        )
    conn.executemany(
        "INSERT OR IGNORE INTO judgment_tool_run (judgment_id, tool_run_id) VALUES (?, ?)",
        [(judgment_id, t) for t in tool_run_ids],
    )
    return judgment_id


def judgment_score(conn: sqlite3.Connection, judgment_id: int) -> Score | None:
    row = _one(conn, "SELECT blocking, minor FROM judgment_score WHERE judgment_id = ?", (judgment_id,))
    return Score(int(row[0]), int(row[1])) if row else None


@dataclass(frozen=True)
class HistoryEntry:
    attempt_id: int
    seq: int
    point: Point
    output_sha256: str | None
    judgment_id: int | None  # the latest valid judgment by the run's judge
    judged: bool  # any judgment by the run's judge, valid or not
    gpu_seconds: float


def history(conn: sqlite3.Connection, optimization_id: int, judge_model_id: int, instruction_set_id: int) -> list[HistoryEntry]:
    """The attempts of an optimization, in order, each with its point and its latest valid judgment by this judge."""
    attempts = conn.execute(
        "SELECT attempt_id, seq, gpu_seconds, output_sha256 FROM attempt WHERE optimization_id = ? ORDER BY seq",
        (optimization_id,),
    ).fetchall()
    entries: list[HistoryEntry] = []
    for attempt_id, seq, gpu_seconds, output in attempts:
        levels = {
            str(r[0]): int(r[1])
            for r in conn.execute(
                "SELECT d.key, l.ordinal FROM attempt_level l JOIN dimension d USING (dimension_id) WHERE l.attempt_id = ?",
                (attempt_id,),
            )
        }
        judgment = _one(
            conn,
            "SELECT MAX(judgment_id) FILTER (WHERE parse_error IS NULL), COUNT(*) FROM judgment "
            "WHERE attempt_id = ? AND judge_model_id = ? AND instruction_set_id = ?",
            (attempt_id, judge_model_id, instruction_set_id),
        )
        assert judgment is not None
        judgment_id = int(judgment[0]) if judgment[0] is not None else None
        entries.append(
            HistoryEntry(int(attempt_id), int(seq), Point.of(levels), output, judgment_id, int(judgment[1]) > 0,
                         float(gpu_seconds))
        )
    return entries


# --- Delivery ------------------------------------------------------------------------------------------------


def deliver_by_rule(conn: sqlite3.Connection, run_id: int, minor_tolerance: int) -> int:
    """Rule `best_accepted`: the run's best attempt if the judge accepted it and no review found it unusable,
    else the original. Never overrides a decision taken by a person. Returns the number of photos decided."""
    rows = conn.execute(
        "SELECT o.photo_id, o.best_attempt_id, s.blocking, s.minor, "
        "  (SELECT r.verdict FROM review r WHERE r.attempt_id = o.best_attempt_id ORDER BY r.review_id DESC LIMIT 1) "
        "FROM optimization o LEFT JOIN judgment_score s ON s.attempt_id = o.best_attempt_id "
        "WHERE o.run_id = ? AND o.status = 'done'",
        (run_id,),
    ).fetchall()
    decided = 0
    for photo_id, attempt_id, blocking, minor, verdict in rows:
        human = _one(conn, "SELECT 1 FROM delivery WHERE photo_id = ? AND decided_by LIKE 'human:%'", (photo_id,))
        if human:
            continue
        good = attempt_id is not None and blocking == 0 and minor <= minor_tolerance and verdict != "unusable"
        conn.execute(
            "INSERT INTO delivery (photo_id, outcome, attempt_id, decided_by, reason, decided_at) VALUES (?, ?, ?, ?, ?, ?) "
            "ON CONFLICT (photo_id) DO UPDATE SET outcome = excluded.outcome, attempt_id = excluded.attempt_id, "
            "decided_by = excluded.decided_by, reason = excluded.reason, decided_at = excluded.decided_at",
            (photo_id, "emptied" if good else "original", attempt_id if good else None, "rule:best_accepted",
             f"run {run_id}", now()),
        )
        decided += 1
    return decided


def deliveries(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT p.source_name, d.outcome, d.decided_by, a.output_sha256, p.image_sha256 FROM delivery d "
        "JOIN photo p USING (photo_id) LEFT JOIN attempt a ON a.attempt_id = d.attempt_id ORDER BY p.source_name"
    ).fetchall()


# --- Reports -------------------------------------------------------------------------------------------------


def run_summary(conn: sqlite3.Connection, run_id: int, minor_tolerance: int) -> dict[str, Any]:
    row = _one(
        conn,
        "WITH best AS (SELECT o.optimization_id, s.blocking, s.minor FROM optimization o "
        "  LEFT JOIN judgment_score s ON s.attempt_id = o.best_attempt_id WHERE o.run_id = ?) "
        "SELECT COUNT(*), COUNT(*) FILTER (WHERE blocking = 0 AND minor <= ?), "
        "COUNT(*) FILTER (WHERE blocking IS NULL) FROM best",
        (run_id, minor_tolerance),
    )
    assert row is not None
    reasons = dict(
        conn.execute(
            "SELECT COALESCE(stop_reason, 'running'), COUNT(*) FROM optimization WHERE run_id = ? GROUP BY 1", (run_id,)
        ).fetchall()
    )
    costs = _one(
        conn,
        "SELECT COUNT(*), COUNT(*) FILTER (WHERE a.cached = 1), COALESCE(SUM(a.gpu_seconds), 0) FROM attempt a "
        "JOIN optimization o USING (optimization_id) WHERE o.run_id = ?",
        (run_id,),
    )
    assert costs is not None
    usable = _one(
        conn,
        "SELECT COUNT(DISTINCT o.photo_id) FROM optimization o JOIN review r ON r.attempt_id = o.best_attempt_id "
        "WHERE o.run_id = ? AND r.verdict = 'usable' AND r.review_id = (SELECT MAX(review_id) FROM review "
        "WHERE attempt_id = o.best_attempt_id)",
        (run_id,),
    )
    return {
        "photos": int(row[0]),
        "accepted_by_judge": int(row[1]),
        "without_evaluation": int(row[2]),
        "stop_reasons": {str(k): int(v) for k, v in reasons.items()},
        "attempts": int(costs[0]),
        "attempts_cached": int(costs[1]),
        "generation_gpu_seconds": round(float(costs[2]), 1),
        "usable_by_review": int(usable[0]) if usable else 0,
    }


def preferences_between(conn: sqlite3.Connection, run_a: int, run_b: int) -> dict[str, int]:
    """Blind comparisons of the best attempts of two runs on the same photos: wins of a, wins of b, others."""
    rows = conn.execute(
        "SELECT p.choice, p.attempt_a = oa.best_attempt_id AS a_first FROM preference p "
        "JOIN optimization oa ON oa.run_id = ? JOIN optimization ob ON ob.run_id = ? AND ob.photo_id = oa.photo_id "
        "WHERE (p.attempt_a = oa.best_attempt_id AND p.attempt_b = ob.best_attempt_id) "
        "   OR (p.attempt_a = ob.best_attempt_id AND p.attempt_b = oa.best_attempt_id)",
        (run_a, run_b),
    ).fetchall()
    tally = {"a_wins": 0, "b_wins": 0, "equal": 0, "both_unusable": 0}
    for choice, a_first in rows:
        if choice in ("a", "b"):
            winner_is_a = (choice == "a") == bool(a_first)
            tally["a_wins" if winner_is_a else "b_wins"] += 1
        else:
            tally[str(choice)] += 1
    return tally


def judged_attempts_with_structure(conn: sqlite3.Connection, run_id: int) -> list[dict[str, Any]]:
    """Per judged attempt of a run: the `structure_map` measures its judge read, the judge's defect codes, and the
    latest review's verdict and codes (None when not reviewed); the input of the detector report."""
    rows = conn.execute(
        "SELECT j.judgment_id, j.attempt_id, o.photo_id, "
        "  (SELECT t.measures_json FROM judgment_tool_run jt JOIN tool_run t USING (tool_run_id) "
        "   WHERE jt.judgment_id = j.judgment_id AND t.tool = 'structure_map' ORDER BY t.tool_run_id DESC LIMIT 1) "
        "FROM judgment j JOIN attempt a USING (attempt_id) JOIN optimization o USING (optimization_id) "
        "WHERE o.run_id = ? AND j.parse_error IS NULL ORDER BY j.attempt_id, j.judgment_id",
        (run_id,),
    ).fetchall()
    found = []
    for judgment_id, attempt_id, photo_id, measures in rows:
        judged = {str(r[0]) for r in conn.execute("SELECT defect_code FROM finding WHERE judgment_id = ?", (judgment_id,))}
        review = _one(conn, "SELECT review_id, verdict FROM review WHERE attempt_id = ? ORDER BY review_id DESC LIMIT 1",
                      (attempt_id,))
        reviewed = None if review is None else {
            str(r[0]) for r in conn.execute("SELECT defect_code FROM finding WHERE review_id = ?", (review[0],))}
        found.append({"attempt": int(attempt_id), "photo": int(photo_id), "judgment": int(judgment_id),
                      "structure": None if measures is None else json.loads(measures), "judge_codes": judged,
                      "review_verdict": None if review is None else str(review[1]), "review_codes": reviewed})
    return found


# --- Zoom judge ------------------------------------------------------------------------------------------------


def judged_candidates(conn: sqlite3.Connection, run_ids: Sequence[int]) -> list[dict[str, Any]]:
    """One row per distinct judged picture of the runs (original, candidate, removal region, as its change map read
    them): the first attempt that produced it."""
    marks = ",".join("?" * len(run_ids))
    rows = conn.execute(
        "SELECT MIN(j.attempt_id), ti0.image_sha256, ti1.image_sha256, ti2.image_sha256 FROM judgment j "
        "JOIN attempt a USING (attempt_id) JOIN optimization o USING (optimization_id) "
        "JOIN judgment_tool_run jt ON jt.judgment_id = j.judgment_id JOIN tool_run t ON t.tool_run_id = jt.tool_run_id "
        "JOIN tool_run_input ti0 ON ti0.tool_run_id = t.tool_run_id AND ti0.position = 0 "
        "JOIN tool_run_input ti1 ON ti1.tool_run_id = t.tool_run_id AND ti1.position = 1 "
        "JOIN tool_run_input ti2 ON ti2.tool_run_id = t.tool_run_id AND ti2.position = 2 "
        f"WHERE o.run_id IN ({marks}) AND t.tool IN ('structure_map', 'change_map') "
        "GROUP BY ti0.image_sha256, ti1.image_sha256, ti2.image_sha256 ORDER BY 1",
        tuple(run_ids),
    ).fetchall()
    return [{"attempt": int(r[0]), "original": str(r[1]), "candidate": str(r[2]), "region": str(r[3])} for r in rows]


def find_zoom_judgment(conn: sqlite3.Connection, request_sha: str, judge_model_id: int) -> int | None:
    row = _one(conn, "SELECT zoom_judgment_id FROM zoom_judgment WHERE request_sha256 = ? AND judge_model_id = ? "
                     "AND parse_error IS NULL ORDER BY zoom_judgment_id DESC LIMIT 1", (request_sha, judge_model_id))
    return None if row is None else int(row[0])


def insert_zoom_judgment(
    conn: sqlite3.Connection, attempt_id: int, judge_model_id: int, tool_run_id: int, request_sha: str, raw: str,
    parse_error: str | None, wall_seconds: float,
    zooms: Sequence[tuple[str, Sequence[float], str]] = (),
    answers: Sequence[tuple[int, Sequence[str], str, str]] = (),
) -> int:
    """A zoom judgment with its zooms (place, box, image) and, when parsed, the answers (zoom, answers, severity,
    comment)."""
    zoom_judgment_id = _id(conn.execute(
        "INSERT INTO zoom_judgment (attempt_id, judge_model_id, tool_run_id, request_sha256, raw_response, parse_error, "
        "wall_seconds, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (attempt_id, judge_model_id, tool_run_id, request_sha, raw, parse_error, wall_seconds, now()),
    ))
    by_zoom = {n: (severity, comment) for n, _, severity, comment in answers}
    for n, (place, box, image_sha) in enumerate(zooms, start=1):
        severity, comment = by_zoom.get(n, (None, None))
        conn.execute("INSERT INTO zoom (zoom_judgment_id, n, place, x0, y0, x1, y1, image_sha256, severity, comment) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (zoom_judgment_id, n, place, *box, image_sha, severity, comment))
    for n, chosen, _, _ in answers:
        conn.executemany("INSERT INTO zoom_answer (zoom_judgment_id, n, answer) VALUES (?, ?, ?)",
                         [(zoom_judgment_id, n, a) for a in chosen])
    return zoom_judgment_id
