"""Check the stage-5 claims ledger against the stage-3 claim tables and the skeleton.

Verifies that every claim id of build/research/<slot>/result.md (slots 01 to 10) appears exactly
once in build/distill/claims_ledger.md, that the ledger cites no unknown claim id, that every
ledger row's node exists in build/distill/skeleton.md, and reports counts per graph and role.

Usage: python3 check_ledger.py [BRANCH]   (BRANCH: check branches/BRANCH/ledger.md and
skeleton.md against branches/BRANCH/claims.md)   Exit 1 on any error.
"""

import re
import sys
from collections import Counter
from pathlib import Path

BUILD = Path(__file__).resolve().parent.parent
LEDGER_HEADER = ["row", "claim_ids", "node", "graph", "statement", "agreement", "role"]
CLAIM_ID = re.compile(r"\b[A-Z]+\d*-C\d+\b")


def table_rows(path: Path, header: list[str]):
    in_table = False
    for line in path.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if [c.lower() for c in cells] == header:
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if set(line.replace("|", "").strip()) <= set("-: "):
            continue
        yield cells


def main(branch: str | None = None) -> int:
    errors = []
    claims = set()
    if branch:
        # Branch mode: the claims routed to this branch, its own ledger and skeleton.
        folder = BUILD / "distill" / "branches" / branch
        for line in (folder / "claims.md").read_text().splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if line.startswith("|") and len(cells) > 2 and CLAIM_ID.fullmatch(cells[2]):
                claims.add(cells[2])
    else:
        folder = BUILD / "distill"
        for path in sorted((BUILD / "research").glob("[01][0-9]_*/result.md")):
            for line in path.read_text().splitlines():
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if line.startswith("|") and CLAIM_ID.fullmatch(cells[0]):
                    claims.add(cells[0])

    skeleton_text = (folder / "skeleton.md").read_text()
    nodes = set(re.findall(r"^\|\s*((?:PIG-JS\.)?[A-Z][A-Z0-9_.]*)\s*\|", skeleton_text, re.M))

    placed = Counter()
    roles, graphs = Counter(), Counter()
    for cells in table_rows(folder / ("ledger.md" if branch else "claims_ledger.md"), LEDGER_HEADER):
        if len(cells) != len(LEDGER_HEADER):
            errors.append(f"ledger row {cells[0]}: {len(cells)} cells")
            continue
        row = dict(zip(LEDGER_HEADER, cells))
        ids = CLAIM_ID.findall(row["claim_ids"])
        placed.update(ids)
        roles[row["role"]] += 1
        graphs[row["graph"]] += 1
        if row["node"] not in nodes:
            errors.append(f"ledger row {row['row']}: node {row['node']} not in skeleton")

    missing = sorted(claims - set(placed))
    duplicated = sorted(c for c, n in placed.items() if n > 1)
    unknown = sorted(set(placed) - claims)
    errors += [f"claim {c} not placed" for c in missing]
    errors += [f"claim {c} placed {placed[c]} times" for c in duplicated]
    errors += [f"ledger cites unknown claim {c}" for c in unknown]

    print(f"claims in: {len(claims)}; placed: {len(set(placed) & claims)}; missing {len(missing)}; "
          f"duplicated {len(duplicated)}; unknown {len(unknown)}")
    print(f"ledger rows by graph: {dict(graphs)}; by role: {dict(roles)}; skeleton nodes: {len(nodes)}")
    for e in errors:
        print("ERROR", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
