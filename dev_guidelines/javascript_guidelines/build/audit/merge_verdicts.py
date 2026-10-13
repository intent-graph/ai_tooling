"""Merge the stage-2 audit verdict tables into one source register and one rejection list.

Reads every build/audit/<group>/result.md, takes the rows of its verdict table (header
`| id | slot | title | url | verdict | tier | restriction | gate | reason | standing_check |`),
deduplicates by normalized URL, and writes:

- build/audit/source_register.md: admitted and restricted sources, one SRC id per document;
- build/audit/rejections.md: rejected sources with the gate that failed.

When two auditors judged the same document differently, the strictest outcome wins (reject over
restricted over admit; the lower tier, T3 over T2 over T1), in line with the default-to-refuted
rule of the audit brief, and the disagreement is listed. One exception: a restriction concerns
one area's use of a source, so when one auditor restricted and another admitted outright, the
restriction is scoped to the restricting auditor's slots.

Usage: python3 merge_verdicts.py   (run from anywhere; paths are relative to this file)
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

AUDIT_DIR = Path(__file__).resolve().parent
HEADER = ["id", "slot", "title", "url", "verdict", "tier", "restriction", "gate", "reason", "standing_check"]
VERDICT_RANK = {"admit": 0, "admit-restricted": 1, "reject": 2}
TIER_RANK = {"T1": 0, "T2": 1, "T3": 2, "-": 3}


def normalize_url(url: str) -> str:
    url = url.strip().strip("<>").split("#")[0]
    url = re.sub(r"^https?://", "", url)
    url = re.sub(r"^www\.", "", url)
    return url.rstrip("/").lower()


def parse_tables() -> tuple[list[dict], list[str]]:
    rows, errors = [], []
    for result in sorted(AUDIT_DIR.glob("*/result.md")):
        group = result.parent.name
        in_table = False
        for lineno, line in enumerate(result.read_text().splitlines(), 1):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if [c.lower() for c in cells] == HEADER:
                in_table = True
                continue
            if not in_table:
                continue
            if not line.startswith("|"):
                in_table = False
                continue
            if set(line.replace("|", "").strip()) <= set("-: "):
                continue
            if len(cells) != len(HEADER):
                errors.append(f"{group}/result.md:{lineno}: {len(cells)} cells, expected {len(HEADER)}")
                continue
            row = dict(zip(HEADER, cells))
            row["verdict"] = row["verdict"].lower()
            row["group"] = group
            if row["verdict"] not in VERDICT_RANK:
                errors.append(f"{group}/result.md:{lineno}: unknown verdict {row['verdict']!r}")
                continue
            rows.append(row)
    return rows, errors


def strictest(judgments: list[dict]) -> dict:
    return max(judgments, key=lambda r: (VERDICT_RANK[r["verdict"]], TIER_RANK.get(r["tier"], 3)))


def main() -> int:
    rows, errors = parse_tables()
    by_doc: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_doc[normalize_url(row["url"])].append(row)

    merged, conflicts = [], []
    for url, judgments in by_doc.items():
        final = dict(strictest(judgments))
        final["replaces"] = ", ".join(sorted({j["id"] for j in judgments}))
        final["slots"] = ", ".join(sorted({j["slot"] for j in judgments}))
        # A rejection is about the document and holds everywhere; a restriction is about one
        # area's use of it, so when auditors differ it is scoped to the slots that imposed it.
        restricted = [j for j in judgments if j["verdict"] == "admit-restricted"]
        open_slots = sorted({j["slot"] for j in judgments if j["verdict"] == "admit"})
        distinct = {j["restriction"] for j in restricted}
        if restricted and open_slots and final["verdict"] != "reject":
            scoped = [f"{j['slot']}: {j['restriction']}" for j in restricted]
            final["restriction"] = f"unrestricted for {', '.join(open_slots)}; " + "; ".join(scoped)
        elif len(distinct) > 1 and final["verdict"] != "reject":
            # Different restrictions from different areas: keep each tied to its slot.
            final["restriction"] = "; ".join(f"{j['slot']}: {j['restriction']}" for j in restricted)
        else:
            final["restriction"] = "; ".join(sorted({j["restriction"] for j in restricted})) or "-"
        outcomes = {(j["verdict"], j["tier"]) for j in judgments}
        if len(outcomes) > 1:
            detail = "; ".join(f"{j['id']} ({j['group']}): {j['verdict']} {j['tier']}" for j in judgments)
            conflicts.append(f"- {final['title']}: {detail}; kept {final['verdict']} {final['tier']}")
        merged.append(final)

    kept = [r for r in merged if r["verdict"] != "reject"]
    rejected = [r for r in merged if r["verdict"] == "reject"]
    # Ids are stable across re-runs: claims cite them. A document already in the register keeps
    # its id; a new document gets the next free number.
    previous = {}
    register_path = AUDIT_DIR / "source_register.md"
    if register_path.exists():
        for line in register_path.read_text().splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.fullmatch(r"SRC-\d{3}", cells[0]):
                previous[normalize_url(cells[4])] = cells[0]
    kept.sort(key=lambda r: (TIER_RANK.get(r["tier"], 3), r["slots"], r["title"].lower()))
    next_id = max((int(s[4:]) for s in previous.values()), default=0) + 1
    for row in kept:
        old = previous.get(normalize_url(row["url"]))
        if old:
            row["src"] = old
        else:
            row["src"] = f"SRC-{next_id:03d}"
            next_id += 1
    kept.sort(key=lambda r: r["src"])

    tiers = defaultdict(int)
    for row in kept:
        tiers[row["tier"]] += 1
    restricted = sum(r["verdict"] == "admit-restricted" for r in kept)
    pinned = [
        f"- Candidate rows read: {len(rows)}, from {len({r['group'] for r in rows})} audit groups; distinct documents: {len(merged)}.",
        f"- Register entries: {len(kept)} (T1 {tiers['T1']}, T2 {tiers['T2']}, T3 {tiers['T3']}), of which restricted {restricted}.",
        f"- Rejected documents: {len(rejected)}.",
        f"- Auditor disagreements on one document: {len(conflicts)}; parse errors: {len(errors)}.",
    ]

    register = [
        "# Source register: admitted sources, deduplicated across audit groups",
        "",
        "Generated by `merge_verdicts.py` from the verdict tables in `*/result.md`. Do not edit by hand;",
        "fix the audit result and re-run. One row per document; `replaces` lists the candidate ids it",
        "absorbs. Restricted sources may ground only what `restriction` states.",
        "",
        "Pinned:",
        *pinned,
        "",
        "| src | tier | verdict | title | url | slots | replaces | restriction |",
        "|---|---|---|---|---|---|---|---|",
    ]
    register += [
        f"| {r['src']} | {r['tier']} | {r['verdict']} | {r['title']} | {r['url']} | {r['slots']} | {r['replaces']} | {r['restriction']} |"
        for r in kept
    ]
    register += ["", "## Auditor disagreements", "", *(conflicts or ["None."]), ""]
    if errors:
        register += ["## Parse errors", "", *(f"- {e}" for e in errors), ""]
    (AUDIT_DIR / "source_register.md").write_text("\n".join(register))

    gates = defaultdict(int)
    for row in rejected:
        gates[row["gate"]] += 1
    rejections = [
        "# Rejections: every candidate the audit refused, with the gate it failed",
        "",
        "Generated by `merge_verdicts.py`. Kept as evidence that the admission filter ran.",
        "",
        "Pinned:",
        *pinned,
        "- Rejections by gate: " + ", ".join(f"{g} {n}" for g, n in sorted(gates.items())) + ".",
        "",
        "| ids | slots | title | url | gate | reason |",
        "|---|---|---|---|---|---|",
    ]
    rejections += [
        f"| {r['replaces']} | {r['slots']} | {r['title']} | {r['url']} | {r['gate']} | {r['reason']} |"
        for r in sorted(rejected, key=lambda r: (r["gate"], r["slots"]))
    ]
    (AUDIT_DIR / "rejections.md").write_text("\n".join(rejections) + "\n")

    print("\n".join(pinned))
    for e in errors:
        print("ERROR", e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
