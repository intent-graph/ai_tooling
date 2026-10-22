"""Every query of the review page: what to show a reviewer, and the typed judgments the reviewer stores.

Reads run anywhere; writes (`insert_review`, `insert_preference`, `upsert_human_delivery`) run inside
`db.transaction`. Every statement is fixed text with bound parameters.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Sequence
from dataclasses import dataclass

from virtual_unstaging.domain import Box, Severity
from virtual_unstaging.store.repo import now

# --- Reference data and images ---------------------------------------------------------------------------------


@dataclass(frozen=True)
class DefectRow:
    code: str
    label: str
    description: str


def defect_rows(conn: sqlite3.Connection) -> list[DefectRow]:
    rows = conn.execute("SELECT code, label, description FROM defect_type ORDER BY rowid").fetchall()
    return [DefectRow(str(r[0]), str(r[1]), str(r[2])) for r in rows]


def image_media_type(conn: sqlite3.Connection, sha: str) -> str | None:
    row = conn.execute("SELECT media_type FROM image WHERE sha256 = ?", (sha,)).fetchone()
    return str(row[0]) if row else None


# --- Runs ------------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class RunRow:
    run_id: int
    label: str | None
    photos: int  # optimizations in the run
    candidates: int  # of those, with a best attempt that has an output
    reviewed: int  # of those, reviewed by this reviewer


def run_rows(conn: sqlite3.Connection, reviewer: str) -> list[RunRow]:
    rows = conn.execute(
        "SELECT r.run_id, r.label, "
        "  (SELECT COUNT(*) FROM optimization o WHERE o.run_id = r.run_id), "
        "  (SELECT COUNT(*) FROM optimization o JOIN attempt a ON a.attempt_id = o.best_attempt_id "
        "     WHERE o.run_id = r.run_id AND a.output_sha256 IS NOT NULL), "
        "  (SELECT COUNT(*) FROM optimization o JOIN attempt a ON a.attempt_id = o.best_attempt_id "
        "     WHERE o.run_id = r.run_id AND a.output_sha256 IS NOT NULL "
        "       AND EXISTS (SELECT 1 FROM review v WHERE v.attempt_id = a.attempt_id AND v.reviewer = ?)) "
        "FROM run r ORDER BY r.run_id",
        (reviewer,),
    ).fetchall()
    return [RunRow(int(r[0]), r[1], int(r[2]), int(r[3]), int(r[4])) for r in rows]


def run_exists(conn: sqlite3.Connection, run_id: int) -> bool:
    return conn.execute("SELECT 1 FROM run WHERE run_id = ?", (run_id,)).fetchone() is not None


# --- Typed review ----------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class QueueRow:
    photo_id: int
    name: str
    attempt_id: int
    original_sha: str
    candidate_sha: str
    my_verdict: str | None  # this reviewer's latest verdict on this attempt


def review_queue(conn: sqlite3.Connection, run_id: int, reviewer: str) -> list[QueueRow]:
    """The best attempt of each photo of a run (only those that produced an image), in photo order."""
    rows = conn.execute(
        "SELECT o.photo_id, p.source_name, a.attempt_id, p.image_sha256, a.output_sha256, "
        "  (SELECT v.verdict FROM review v WHERE v.attempt_id = a.attempt_id AND v.reviewer = ? "
        "     ORDER BY v.review_id DESC LIMIT 1) "
        "FROM optimization o JOIN photo p ON p.photo_id = o.photo_id "
        "JOIN attempt a ON a.attempt_id = o.best_attempt_id "
        "WHERE o.run_id = ? AND a.output_sha256 IS NOT NULL ORDER BY p.source_name",
        (reviewer, run_id),
    ).fetchall()
    return [QueueRow(int(r[0]), str(r[1]), int(r[2]), str(r[3]), str(r[4]), r[5]) for r in rows]


@dataclass(frozen=True)
class AttemptHeader:
    attempt_id: int
    seq: int
    output_sha: str | None
    run_id: int
    photo_id: int
    is_best: bool
    name: str
    group: str | None
    original_sha: str
    rule_set_id: int


def attempt_header(conn: sqlite3.Connection, attempt_id: int) -> AttemptHeader | None:
    row = conn.execute(
        "SELECT a.attempt_id, a.seq, a.output_sha256, o.run_id, o.photo_id, o.best_attempt_id = a.attempt_id, "
        "  p.source_name, g.name, p.image_sha256, r.rule_set_id "
        "FROM attempt a JOIN optimization o ON o.optimization_id = a.optimization_id "
        "JOIN photo p ON p.photo_id = o.photo_id LEFT JOIN photo_group g ON g.group_id = p.group_id "
        "JOIN run r ON r.run_id = o.run_id WHERE a.attempt_id = ?",
        (attempt_id,),
    ).fetchone()
    if row is None:
        return None
    return AttemptHeader(
        int(row[0]), int(row[1]), row[2], int(row[3]), int(row[4]), bool(row[5]), str(row[6]), row[7], str(row[8]),
        int(row[9]),
    )


@dataclass(frozen=True)
class FindingRow:
    code: str
    severity: str
    box: Box | None
    comment: str


def _finding(row: Sequence[object]) -> FindingRow:
    box = Box(float(row[2]), float(row[3]), float(row[4]), float(row[5])) if row[2] is not None else None  # type: ignore[arg-type]
    return FindingRow(str(row[0]), str(row[1]), box, str(row[6] or ""))


@dataclass(frozen=True)
class JudgmentView:
    own_verdict: str | None
    critique: str
    findings: list[FindingRow]


def latest_judgment(conn: sqlite3.Connection, attempt_id: int) -> JudgmentView | None:
    """The attempt's latest judgment that parsed, with its findings."""
    row = conn.execute(
        "SELECT judgment_id, own_verdict, critique FROM judgment WHERE attempt_id = ? AND parse_error IS NULL "
        "ORDER BY judgment_id DESC LIMIT 1",
        (attempt_id,),
    ).fetchone()
    if row is None:
        return None
    findings = conn.execute(
        "SELECT defect_code, severity, x0, y0, x1, y1, comment FROM finding WHERE judgment_id = ? ORDER BY finding_id",
        (row[0],),
    ).fetchall()
    return JudgmentView(row[1], str(row[2] or ""), [_finding(f) for f in findings])


def outline_image(conn: sqlite3.Connection, attempt_id: int) -> str | None:
    """Hash of the original with the removal region outlined (tool `outline`) that fed this attempt's judgment."""
    row = conn.execute(
        "SELECT o.image_sha256 FROM judgment j JOIN judgment_tool_run jt ON jt.judgment_id = j.judgment_id "
        "JOIN tool_run t ON t.tool_run_id = jt.tool_run_id AND t.tool = 'outline' "
        "JOIN tool_run_output o ON o.tool_run_id = t.tool_run_id AND o.name = 'image' "
        "WHERE j.attempt_id = ? ORDER BY t.tool_run_id DESC LIMIT 1",
        (attempt_id,),
    ).fetchone()
    return str(row[0]) if row else None


def removal_mask_image(conn: sqlite3.Connection, photo_id: int, rule_set_id: int) -> str | None:
    """Hash of the photo's removal mask from stage 0: the outline's fallback."""
    row = conn.execute(
        "SELECT o.image_sha256 FROM eligibility e JOIN tool_run_output o "
        "ON o.tool_run_id = e.removal_mask_tool_run_id AND o.name = 'mask' WHERE e.photo_id = ? AND e.rule_set_id = ?",
        (photo_id, rule_set_id),
    ).fetchone()
    return str(row[0]) if row else None


@dataclass(frozen=True)
class ReviewView:
    review_id: int
    verdict: str
    comment: str
    findings: list[FindingRow]


def latest_review(conn: sqlite3.Connection, attempt_id: int, reviewer: str) -> ReviewView | None:
    row = conn.execute(
        "SELECT review_id, verdict, comment FROM review WHERE attempt_id = ? AND reviewer = ? "
        "ORDER BY review_id DESC LIMIT 1",
        (attempt_id, reviewer),
    ).fetchone()
    if row is None:
        return None
    findings = conn.execute(
        "SELECT defect_code, severity, x0, y0, x1, y1, comment FROM finding WHERE review_id = ? ORDER BY finding_id",
        (row[0],),
    ).fetchall()
    return ReviewView(int(row[0]), str(row[1]), str(row[2] or ""), [_finding(f) for f in findings])


@dataclass(frozen=True)
class NewFinding:
    defect_code: str
    severity: Severity
    box: Box | None
    comment: str | None


def insert_review(
    conn: sqlite3.Connection, attempt_id: int, reviewer: str, verdict: str, comment: str | None,
    findings: Sequence[NewFinding],
) -> int:
    cursor = conn.execute(
        "INSERT INTO review (attempt_id, reviewer, verdict, comment, created_at) VALUES (?, ?, ?, ?, ?)",
        (attempt_id, reviewer, verdict, comment, now()),
    )
    review_id = cursor.lastrowid
    assert review_id is not None
    conn.executemany(
        "INSERT INTO finding (review_id, defect_code, severity, x0, y0, x1, y1, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (review_id, f.defect_code, f.severity, *((f.box.x0, f.box.y0, f.box.x1, f.box.y1) if f.box else (None,) * 4),
             f.comment)
            for f in findings
        ],
    )
    return review_id


def attempt_photo(conn: sqlite3.Connection, attempt_id: int) -> tuple[int, str | None] | None:
    """(photo id, output hash) of an attempt, or None when no such attempt exists."""
    row = conn.execute(
        "SELECT o.photo_id, a.output_sha256 FROM attempt a JOIN optimization o ON o.optimization_id = a.optimization_id "
        "WHERE a.attempt_id = ?",
        (attempt_id,),
    ).fetchone()
    return (int(row[0]), row[1]) if row else None


# --- Blind comparison ------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class PairRow:
    photo_id: int
    name: str
    original_sha: str
    attempt_a: int  # best attempt of the first run
    attempt_b: int  # best attempt of the second run
    sha_a: str
    sha_b: str
    compared: bool  # this reviewer already compared these two attempts


def comparison_pairs(conn: sqlite3.Connection, run_a: int, run_b: int, reviewer: str) -> list[PairRow]:
    """Photos present in both runs whose best attempts produced different images, in photo order."""
    rows = conn.execute(
        "SELECT p.photo_id, p.source_name, p.image_sha256, oa.best_attempt_id, ob.best_attempt_id, "
        "  aa.output_sha256, ab.output_sha256, "
        "  EXISTS (SELECT 1 FROM preference f WHERE f.reviewer = ? AND "
        "    ((f.attempt_a = oa.best_attempt_id AND f.attempt_b = ob.best_attempt_id) "
        "     OR (f.attempt_a = ob.best_attempt_id AND f.attempt_b = oa.best_attempt_id))) "
        "FROM optimization oa JOIN optimization ob ON ob.photo_id = oa.photo_id AND ob.run_id = ? "
        "JOIN photo p ON p.photo_id = oa.photo_id "
        "JOIN attempt aa ON aa.attempt_id = oa.best_attempt_id "
        "JOIN attempt ab ON ab.attempt_id = ob.best_attempt_id "
        "WHERE oa.run_id = ? AND aa.output_sha256 IS NOT NULL AND ab.output_sha256 IS NOT NULL "
        "  AND aa.output_sha256 <> ab.output_sha256 ORDER BY p.source_name",
        (reviewer, run_b, run_a),
    ).fetchall()
    return [PairRow(int(r[0]), str(r[1]), str(r[2]), int(r[3]), int(r[4]), str(r[5]), str(r[6]), bool(r[7])) for r in rows]


def preference_exists(conn: sqlite3.Connection, reviewer: str, attempt_a: int, attempt_b: int) -> bool:
    row = conn.execute(
        "SELECT 1 FROM preference WHERE reviewer = ? AND "
        "((attempt_a = ? AND attempt_b = ?) OR (attempt_a = ? AND attempt_b = ?))",
        (reviewer, attempt_a, attempt_b, attempt_b, attempt_a),
    ).fetchone()
    return row is not None


def insert_preference(
    conn: sqlite3.Connection, reviewer: str, attempt_a: int, attempt_b: int, shown_left: int, choice: str
) -> int:
    cursor = conn.execute(
        "INSERT INTO preference (reviewer, attempt_a, attempt_b, shown_left, choice, created_at) VALUES (?, ?, ?, ?, ?, ?)",
        (reviewer, attempt_a, attempt_b, shown_left, choice, now()),
    )
    assert cursor.lastrowid is not None
    return cursor.lastrowid


# --- Delivery --------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class DeliveryRow:
    photo_id: int
    name: str
    group: str | None
    original_sha: str
    outcome: str | None
    attempt_id: int | None
    decided_by: str | None
    reason: str | None


def delivery_rows(conn: sqlite3.Connection) -> list[DeliveryRow]:
    """Every photo with its current delivery decision, if any."""
    rows = conn.execute(
        "SELECT p.photo_id, p.source_name, g.name, p.image_sha256, d.outcome, d.attempt_id, d.decided_by, d.reason "
        "FROM photo p LEFT JOIN photo_group g ON g.group_id = p.group_id LEFT JOIN delivery d ON d.photo_id = p.photo_id "
        "ORDER BY p.source_name"
    ).fetchall()
    return [DeliveryRow(int(r[0]), str(r[1]), r[2], str(r[3]), r[4], r[5], r[6], r[7]) for r in rows]


@dataclass(frozen=True)
class CandidateRow:
    photo_id: int
    attempt_id: int
    run_id: int
    output_sha: str
    blocking: int | None
    minor: int | None
    my_verdict: str | None


def delivery_candidates(conn: sqlite3.Connection, reviewer: str) -> list[CandidateRow]:
    """The best attempt of every optimization that produced an image, with its score and this reviewer's verdict."""
    rows = conn.execute(
        "SELECT o.photo_id, a.attempt_id, o.run_id, a.output_sha256, s.blocking, s.minor, "
        "  (SELECT v.verdict FROM review v WHERE v.attempt_id = a.attempt_id AND v.reviewer = ? "
        "     ORDER BY v.review_id DESC LIMIT 1) "
        "FROM optimization o JOIN attempt a ON a.attempt_id = o.best_attempt_id "
        "LEFT JOIN judgment_score s ON s.judgment_id = "
        "  (SELECT MAX(x.judgment_id) FROM judgment_score x WHERE x.attempt_id = a.attempt_id) "
        "WHERE a.output_sha256 IS NOT NULL ORDER BY o.photo_id, o.run_id",
        (reviewer,),
    ).fetchall()
    return [
        CandidateRow(int(r[0]), int(r[1]), int(r[2]), str(r[3]), r[4], r[5], r[6]) for r in rows
    ]


def photo_exists(conn: sqlite3.Connection, photo_id: int) -> bool:
    return conn.execute("SELECT 1 FROM photo WHERE photo_id = ?", (photo_id,)).fetchone() is not None


def upsert_human_delivery(
    conn: sqlite3.Connection, photo_id: int, outcome: str, attempt_id: int | None, decided_by: str, reason: str | None
) -> None:
    """A person's decision replaces any earlier one (a rule's or a person's); `deliver_by_rule` never overrides it."""
    conn.execute(
        "INSERT INTO delivery (photo_id, outcome, attempt_id, decided_by, reason, decided_at) VALUES (?, ?, ?, ?, ?, ?) "
        "ON CONFLICT (photo_id) DO UPDATE SET outcome = excluded.outcome, attempt_id = excluded.attempt_id, "
        "decided_by = excluded.decided_by, reason = excluded.reason, decided_at = excluded.decided_at",
        (photo_id, outcome, attempt_id, decided_by, reason, now()),
    )
