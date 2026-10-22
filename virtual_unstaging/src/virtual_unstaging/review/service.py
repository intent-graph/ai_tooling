"""What the review page shows and stores: views built from queries, and typed judgments written in one transaction."""

from __future__ import annotations

import hashlib
import sqlite3
from typing import Any

from virtual_unstaging.review.errors import ReviewError
from virtual_unstaging.review.parse import DeliveryIn, PreferenceIn, ReviewIn
from virtual_unstaging.store import review_queries as q
from virtual_unstaging.store.db import transaction


def human(reviewer: str) -> str:
    """The `decided_by` of a person: `deliver_by_rule` never overrides a decision that starts with `human:`."""
    return f"human:{reviewer}"


def shown_left_for(reviewer: str, photo_id: int, attempt_a: int, attempt_b: int) -> int:
    """Which of two attempts a reviewer sees on the left: pseudo-random, fixed per reviewer and photo and pair."""
    low, high = sorted((attempt_a, attempt_b))
    digest = hashlib.sha256(f"{reviewer}\0{photo_id}\0{low}\0{high}".encode()).digest()
    return low if digest[0] % 2 == 0 else high


def _finding_json(finding: q.FindingRow) -> dict[str, Any]:
    box = None
    if finding.box is not None:
        box = {"x0": finding.box.x0, "y0": finding.box.y0, "x1": finding.box.x1, "y1": finding.box.y1}
    return {"defect_code": finding.code, "severity": finding.severity, "box": box, "comment": finding.comment}


# --- Reads -----------------------------------------------------------------------------------------------------


def meta(conn: sqlite3.Connection, reviewer: str) -> dict[str, Any]:
    return {
        "reviewer": reviewer,
        "defects": [{"code": d.code, "label": d.label, "description": d.description} for d in q.defect_rows(conn)],
        "runs": [
            {"run_id": r.run_id, "label": r.label, "photos": r.photos, "candidates": r.candidates, "reviewed": r.reviewed}
            for r in q.run_rows(conn, reviewer)
        ],
    }


def review_queue(conn: sqlite3.Connection, run_id: int, reviewer: str) -> dict[str, Any]:
    if not q.run_exists(conn, run_id):
        raise ReviewError(404, "unknown_run", "no such run")
    items = [
        {
            "photo_id": r.photo_id, "name": r.name, "attempt_id": r.attempt_id, "original": r.original_sha,
            "candidate": r.candidate_sha, "my_verdict": r.my_verdict,
        }
        for r in q.review_queue(conn, run_id, reviewer)
    ]
    return {"run_id": run_id, "total": len(items), "left": sum(1 for i in items if i["my_verdict"] is None), "items": items}


def attempt_view(conn: sqlite3.Connection, attempt_id: int, reviewer: str) -> dict[str, Any]:
    header = q.attempt_header(conn, attempt_id)
    if header is None or header.output_sha is None:
        raise ReviewError(404, "unknown_attempt", "no such attempt, or it produced no image")
    judgment = q.latest_judgment(conn, attempt_id)
    outline = q.outline_image(conn, attempt_id)
    region: dict[str, str | None] | None = {"kind": "outline", "image": outline} if outline else None
    if region is None:
        mask = q.removal_mask_image(conn, header.photo_id, header.rule_set_id)
        region = {"kind": "removal_mask", "image": mask} if mask else {"kind": "none", "image": None}
    mine = q.latest_review(conn, attempt_id, reviewer)
    return {
        "attempt_id": header.attempt_id, "seq": header.seq, "run_id": header.run_id, "photo_id": header.photo_id,
        "is_best": header.is_best, "name": header.name, "group": header.group, "original": header.original_sha,
        "candidate": header.output_sha, "region": region,
        "judge": None if judgment is None else {
            "own_verdict": judgment.own_verdict, "critique": judgment.critique,
            "findings": [_finding_json(f) for f in judgment.findings],
        },
        "mine": None if mine is None else {
            "verdict": mine.verdict, "comment": mine.comment, "findings": [_finding_json(f) for f in mine.findings],
        },
    }


def compare_view(conn: sqlite3.Connection, run_a: int, run_b: int, reviewer: str) -> dict[str, Any]:
    """Pairs to compare, blind: the response names attempts and sides, never the runs they came from."""
    for run_id in (run_a, run_b):
        if not q.run_exists(conn, run_id):
            raise ReviewError(404, "unknown_run", "no such run")
    pairs = q.comparison_pairs(conn, run_a, run_b, reviewer)
    items = []
    for pair in pairs:
        if pair.compared:
            continue
        left = shown_left_for(reviewer, pair.photo_id, pair.attempt_a, pair.attempt_b)
        left_is_a = left == pair.attempt_a
        items.append(
            {
                "photo_id": pair.photo_id, "name": pair.name, "original": pair.original_sha,
                "attempt_a": pair.attempt_a, "attempt_b": pair.attempt_b, "shown_left": left,
                "left": pair.sha_a if left_is_a else pair.sha_b, "right": pair.sha_b if left_is_a else pair.sha_a,
            }
        )
    return {"total": len(pairs), "left": len(items), "items": items}


def delivery_view(conn: sqlite3.Connection, reviewer: str) -> dict[str, Any]:
    by_photo: dict[int, list[dict[str, Any]]] = {}
    for c in q.delivery_candidates(conn, reviewer):
        by_photo.setdefault(c.photo_id, []).append(
            {"attempt_id": c.attempt_id, "run_id": c.run_id, "image": c.output_sha, "blocking": c.blocking,
             "minor": c.minor, "my_verdict": c.my_verdict}
        )
    items: list[dict[str, Any]] = [
        {
            "photo_id": r.photo_id, "name": r.name, "group": r.group, "original": r.original_sha,
            "decision": None if r.outcome is None else
            {"outcome": r.outcome, "attempt_id": r.attempt_id, "decided_by": r.decided_by, "reason": r.reason},
            "candidates": by_photo.get(r.photo_id, []),
        }
        for r in q.delivery_rows(conn)
    ]
    mine = human(reviewer)
    decided_by = [(i["decision"] or {}).get("decided_by") or "" for i in items]
    return {
        "total": len(items),
        "left": sum(1 for d in decided_by if not d.startswith("human:")),
        "decided_by_me": sum(1 for d in decided_by if d == mine),
        "items": items,
    }


# --- Writes ----------------------------------------------------------------------------------------------------


def record_review(conn: sqlite3.Connection, reviewer: str, review: ReviewIn) -> dict[str, Any]:
    found = q.attempt_photo(conn, review.attempt_id)
    if found is None or found[1] is None:
        raise ReviewError(404, "unknown_attempt", "attempt_id: no such attempt, or it produced no image")
    findings = [q.NewFinding(f.defect_code, f.severity, f.box, f.comment) for f in review.findings]
    with transaction(conn):
        review_id = q.insert_review(conn, review.attempt_id, reviewer, review.verdict, review.comment, findings)
    return {"review_id": review_id, "findings": len(findings)}


def record_preference(conn: sqlite3.Connection, reviewer: str, pref: PreferenceIn) -> dict[str, Any]:
    first, second = q.attempt_photo(conn, pref.attempt_a), q.attempt_photo(conn, pref.attempt_b)
    if first is None or second is None or first[1] is None or second[1] is None:
        raise ReviewError(404, "unknown_attempt", "attempt_a, attempt_b: no such attempt, or no image")
    if first[0] != second[0]:
        raise ReviewError(400, "invalid_body", "attempt_a, attempt_b: the attempts belong to different photos")
    if pref.shown_left != shown_left_for(reviewer, first[0], pref.attempt_a, pref.attempt_b):
        raise ReviewError(400, "shown_left_mismatch", "shown_left: not the side this reviewer was shown")
    with transaction(conn):
        if q.preference_exists(conn, reviewer, pref.attempt_a, pref.attempt_b):
            raise ReviewError(409, "already_compared", "this reviewer already compared these two attempts")
        preference_id = q.insert_preference(conn, reviewer, pref.attempt_a, pref.attempt_b, pref.shown_left, pref.choice)
    return {"preference_id": preference_id}


def record_delivery(conn: sqlite3.Connection, reviewer: str, delivery: DeliveryIn) -> dict[str, Any]:
    if not q.photo_exists(conn, delivery.photo_id):
        raise ReviewError(404, "unknown_photo", "photo_id: no such photo")
    if delivery.attempt_id is not None:
        found = q.attempt_photo(conn, delivery.attempt_id)
        if found is None or found[1] is None:
            raise ReviewError(404, "unknown_attempt", "attempt_id: no such attempt, or it produced no image")
        if found[0] != delivery.photo_id:
            raise ReviewError(400, "invalid_body", "attempt_id: the attempt belongs to another photo")
    with transaction(conn):
        q.upsert_human_delivery(conn, delivery.photo_id, delivery.outcome, delivery.attempt_id, human(reviewer), delivery.reason)
    return {"photo_id": delivery.photo_id, "decided_by": human(reviewer)}
