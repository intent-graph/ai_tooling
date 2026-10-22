"""Reports: coverage per target, the iteration curve, carry-forward under its decision rule, cost per accepted pair."""

from __future__ import annotations

from datetime import datetime
from typing import Any

import numpy as np

from clutter_pairs.dataset import DECISION_RULE, Dataset
from clutter_pairs.store import repo


def build(ds: Dataset) -> dict[str, Any]:
    conn = ds.conn
    target_set = repo.latest_target_set(conn) or ds.target_set_id
    coverage = [{"cell": dict(repo.target_values(conn, int(r["target_id"]))), "wanted": r["wanted"],  # type: ignore[call-overload]
                 "accepted": r["accepted"]}
                for r in repo.query(conn, "coverage") if r["target_set_id"] == target_set]
    curve = repo.query(conn, "iteration_curve")
    return {
        "pairs": repo.accepted_pairs(conn),
        "coverage": coverage,
        "iteration_curve": _curve(curve),
        "carry_forward": carry_forward(repo.query(conn, "carry_forward_loop"), ds.rule, ds.file(DECISION_RULE)[0]),
        "cost": cost(repo.runs(conn), repo.query(conn, "call_cost"), repo.accepted_pairs(conn)),
    }


def _curve(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Per stage and wave: loops, finished loops, mean iterations, accepted loops."""
    out: dict[str, list[dict[str, Any]]] = {}
    by_wave: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for r in rows:
        by_wave.setdefault((str(r["stage"]), int(r["wave_id"])), []).append(r)
    for (stage, wave), loops in sorted(by_wave.items()):
        finished = [r for r in loops if r["stop_reason"] is not None]
        out.setdefault(stage, []).append({
            "wave": wave, "loops": len(loops), "finished": len(finished),
            "accepted": sum(1 for r in finished if r["stop_reason"] == "accepted"),
            "mean_iterations": round(float(np.mean([r["iterations"] for r in finished])), 2) if finished else None,
        })
    return out


def carry_forward(rows: list[dict[str, Any]], rule: dict[str, Any], rule_sha: str) -> dict[str, Any]:
    """The decision rule of decision_rules/carry_forward.md, applied per stage to the compared loops."""
    verdicts: dict[str, Any] = {}
    for stage in ("clean", "clutter"):
        arms = {arm: [r for r in rows if r["stage"] == stage and r["lessons_arm"] == arm] for arm in ("on", "off")}
        accepted = {arm: [int(r["iterations"]) for r in loops if r["stop_reason"] == "accepted"]
                    for arm, loops in arms.items()}
        share = {arm: (len(accepted[arm]) / len(loops) if loops else None) for arm, loops in arms.items()}
        mean = {arm: (float(np.mean(v)) if v else None) for arm, v in accepted.items()}
        entry: dict[str, Any] = {"loops": {a: len(v) for a, v in arms.items()}, "accepted_share": share,
                                 "mean_iterations_to_accept": mean, "difference": None, "p_value": None}
        if min(len(v) for v in accepted.values()) < int(rule["min_loops_per_arm"]):
            entry["verdict"] = "undecided"
            entry["why"] = f"fewer than {rule['min_loops_per_arm']} accepted loops in an arm"
        else:
            difference = float(np.mean(accepted["off"]) - np.mean(accepted["on"]))
            p = permutation_p(accepted["on"], accepted["off"], int(rule["permutations"]), int(rule["permutation_seed"]))
            entry["difference"], entry["p_value"] = round(difference, 3), round(p, 4)
            share_ok = (share["on"] or 0.0) >= (share["off"] or 0.0)
            if difference >= float(rule["min_difference"]) and p < float(rule["alpha"]) and share_ok:
                entry["verdict"] = "helps"
            elif difference <= 0:
                entry["verdict"] = "does_not_help"
            else:
                entry["verdict"] = "undecided"
        verdicts[stage] = entry
    return {"rule_file": rule_sha, "rule": rule, "stages": verdicts}


def permutation_p(on: list[int], off: list[int], permutations: int, seed: int) -> float:
    """One-sided: the share of relabellings whose mean(off) - mean(on) is at least the observed one."""
    values = np.array(on + off, dtype=float)
    observed = float(np.mean(off) - np.mean(on))
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(permutations):
        rng.shuffle(values)
        if float(values[len(on):].mean() - values[:len(on)].mean()) >= observed - 1e-12:
            count += 1
    return (count + 1) / (permutations + 1)


def cost(runs: list[dict[str, Any]], calls: list[dict[str, Any]], pairs: int) -> dict[str, Any]:
    """Per run: the rental's price times the run's wall clock; per stage, role and model: calls and seconds."""
    per_run, total = [], 0.0
    for r in runs:
        hours = _hours(r["started_at"], r["ended_at"])
        price = float(r["price_per_hour"] or 0.0)
        per_run.append({"run": r["id"], "hours": round(hours, 3), "price_per_hour": price,
                        "cost": round(hours * price, 2)})
        total += hours * price
    return {"runs": per_run, "calls": calls, "total": round(total, 2),
            "per_accepted_pair": round(total / pairs, 3) if pairs else None}


def _hours(start: object, end: object) -> float:
    if not start or not end:
        return 0.0
    return max(0.0, (datetime.fromisoformat(str(end)) - datetime.fromisoformat(str(start))).total_seconds() / 3600)


def render_text(report: dict[str, Any]) -> str:
    lines = [f"accepted pairs: {report['pairs']}", "", "coverage (wanted / accepted):"]
    for row in report["coverage"]:
        cell = ", ".join(f"{k}={v}" for k, v in row["cell"].items())
        lines.append(f"  {row['accepted']:>3} / {row['wanted']:<3} {cell}")
    lines += ["", "iteration curve (per wave: loops, accepted, mean iterations):"]
    for stage, waves in report["iteration_curve"].items():
        for w in waves:
            lines.append(f"  {stage:<8} wave {w['wave']:>3}: {w['loops']:>3} loops, {w['accepted']:>3} accepted, "
                         f"mean {w['mean_iterations']}")
    cf = report["carry_forward"]
    lines += ["", f"carry-forward (decision rule {cf['rule_file'][:12]}):"]
    for stage, e in cf["stages"].items():
        lines.append(f"  {stage:<8} {e['verdict']}: loops on/off {e['loops']['on']}/{e['loops']['off']}, mean iterations "
                     f"{_fmt(e['mean_iterations_to_accept']['on'])}/{_fmt(e['mean_iterations_to_accept']['off'])}, "
                     f"difference {e['difference']}, p {e['p_value']}")
    c = report["cost"]
    lines += ["", f"cost: {c['total']} in all, {c['per_accepted_pair']} per accepted pair"]
    for r in c["runs"]:
        lines.append(f"  run {r['run']}: {r['hours']} h at {r['price_per_hour']}/h = {r['cost']}")
    for row in c["calls"]:
        lines.append(f"  run {row['run_id']} {row['stage']:<8} {row['role']:<8} {row['model']}: {row['calls']} calls "
                     f"({row['reused']} reused), {row['wall_seconds']:.0f} s wall, {row['gpu_seconds']:.0f} s GPU")
    return "\n".join(lines)


def _fmt(value: float | None) -> str:
    return "-" if value is None else f"{value:.2f}"
