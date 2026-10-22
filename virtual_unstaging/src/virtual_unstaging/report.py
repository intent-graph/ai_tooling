"""Reports on runs: per run, what was accepted, why optimizations stopped, what it cost; blind preferences
between runs; and a comparability check before any comparison (design P5)."""

from __future__ import annotations

import json
import sqlite3
from typing import Any

from virtual_unstaging.store import repo

# Run columns that must match for two runs to be compared.
COMPARABLE = (
    "budget_json", "minor_tolerance", "judge_model_id", "generator_instructions_id", "judge_instructions_id",
    "registry_release_id", "rule_set_id",
)
# The factors a comparison may test, by their run columns: runs may differ in one of them, never in two.
FACTORS = {"engine": ("engine",), "generator": ("generator_model_id", "generator_capabilities_json")}


def comparability(conn: sqlite3.Connection, run_ids: list[int]) -> list[str]:
    """The reasons the runs cannot be compared; empty when they can."""
    rows = [repo.run_row(conn, r) for r in run_ids]

    def differ(col: str) -> bool:
        return len({row[col] for row in rows}) > 1

    problems = [f"runs differ in {col}" for col in COMPARABLE if differ(col)]
    varying = [factor for factor, cols in FACTORS.items() if any(differ(col) for col in cols)]
    if len(varying) > 1:
        problems.append(f"runs differ in more than one factor: {', '.join(varying)}")
    photo_sets = {
        r: frozenset((p[0], p[1]) for p in conn.execute("SELECT photo_id, seed FROM optimization WHERE run_id = ?", (r,)))
        for r in run_ids
    }
    if len(set(photo_sets.values())) > 1:
        problems.append("runs differ in photos or seeds")
    return problems


def build(conn: sqlite3.Connection, run_ids: list[int]) -> dict[str, Any]:
    runs = []
    for run_id in run_ids:
        row = repo.run_row(conn, run_id)
        summary = repo.run_summary(conn, run_id, int(row["minor_tolerance"]))
        generator, _ = repo.model_ref(conn, row["generator_model_id"])
        runs.append({"run": run_id, "engine": row["engine"], "generator": generator, "label": row["label"], **summary})
    comparisons = []
    problems = comparability(conn, run_ids) if len(run_ids) > 1 else []
    if len(run_ids) > 1 and not problems:
        for i, a in enumerate(run_ids):
            for b in run_ids[i + 1 :]:
                comparisons.append({"a": a, "b": b, **repo.preferences_between(conn, a, b)})
    return {"runs": runs, "comparable": not problems, "problems": problems, "preferences": comparisons}


def render_text(report: dict[str, Any]) -> str:
    lines = []
    width = max([len("generator"), *(len(r["generator"]) for r in report["runs"])])
    header = (
        f"{'run':>4}  {'engine':<10} {'generator':<{width}} {'photos':>6} {'accepted':>8} {'usable':>6} {'attempts':>8} "
        f"{'cached':>6} {'GPU s':>8}  stops"
    )
    lines.append(header)
    for r in report["runs"]:
        stops = ", ".join(f"{k} {v}" for k, v in sorted(r["stop_reasons"].items()))
        lines.append(
            f"{r['run']:>4}  {r['engine']:<10} {r['generator']:<{width}} {r['photos']:>6} {r['accepted_by_judge']:>8} {r['usable_by_review']:>6} "
            f"{r['attempts']:>8} {r['attempts_cached']:>6} {r['generation_gpu_seconds']:>8}  {stops}"
        )
    if report["problems"]:
        lines.append("not comparable: " + "; ".join(report["problems"]))
    for c in report["preferences"]:
        lines.append(
            f"blind comparison, run {c['a']} vs run {c['b']}: {c['a_wins']} to {c['b_wins']}, "
            f"equal {c['equal']}, both unusable {c['both_unusable']}"
        )
    return "\n".join(lines)


def to_json(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, sort_keys=True)
