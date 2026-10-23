"""Reports on runs: per run, what was accepted, why optimizations stopped, what it cost; blind preferences
between runs; a comparability check before any comparison (design P5); and the pixel detectors in shadow, beside the
judge and the reviews (design/defect_detectors.md)."""

from __future__ import annotations

import json
import sqlite3
from typing import Any

from virtual_unstaging import detectors
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


def detector_report(conn: sqlite3.Connection, run_ids: list[int]) -> dict[str, Any]:
    """Per detector code: its bands on every judged attempt, and where it decided, how often the judge and the latest
    review agree with it. A detector's `absent` on `other_picture` (the same picture) is compared with nothing."""
    thresholds = detectors.load_thresholds()
    codes: dict[str, dict[str, Any]] = {
        c: {"bands": {}, "judge": {"agree": 0, "disagree": 0}, "review": {"agree": 0, "disagree": 0}, "disagreements": []}
        for c in detectors.CODES}
    judged = without_map = 0
    for run_id in run_ids:
        for row in repo.judged_attempts_with_structure(conn, run_id):
            judged += 1
            if row["structure"] is None:
                without_map += 1
                continue
            for d in detectors.detect(row["structure"], thresholds):
                entry = codes[d.code]
                entry["bands"][d.band] = entry["bands"].get(d.band, 0) + 1
                if d.band not in (detectors.ABSENT, detectors.PRESENT):
                    continue
                if d.code in detectors.DEFECT_OF and d.band == detectors.ABSENT:
                    continue
                defect = detectors.DEFECT_OF.get(d.code, d.code)
                said = d.band == detectors.PRESENT
                for who, found in (("judge", row["judge_codes"]), ("review", row["review_codes"])):
                    if found is None:
                        continue
                    agree = (defect in found) == said
                    entry[who]["agree" if agree else "disagree"] += 1
                    if not agree and len(entry["disagreements"]) < 20:
                        entry["disagreements"].append({"attempt": row["attempt"], "photo": row["photo"], "with": who,
                                                       "detector": d.band, "reason": d.reason})
    return {"version": detectors.version(thresholds), "judged_attempts": judged, "without_structure_map": without_map,
            "codes": codes}


def render_detectors(report: dict[str, Any]) -> str:
    lines = [f"pixel detectors in shadow ({report['version']}): {report['judged_attempts']} judged attempts, "
             f"{report['without_structure_map']} without a structure map"]
    for code, e in report["codes"].items():
        bands = ", ".join(f"{k} {v}" for k, v in sorted(e["bands"].items())) or "none"
        judge, review = e["judge"], e["review"]
        lines.append(f"  {code:<18} {bands}; where decided, judge agrees {judge['agree']} of "
                     f"{judge['agree'] + judge['disagree']}, review {review['agree']} of {review['agree'] + review['disagree']}")
    return "\n".join(lines)
