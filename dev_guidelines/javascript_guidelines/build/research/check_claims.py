"""Check stage-3 claim tables against the audited source register.

For every build/research/<slot>/result.md, reads the claim table (header
`| id | claim | level | stack | since | sources | agreement | certainty | mechanism | quote | tags |`)
and reports:

- ERROR  a cited SRC id that is not in build/audit/source_register.md (unadmitted source);
- ERROR  a claim marked consensus or majority whose sources fall below the plan's threshold
         (one T1, or two T2);
- ERROR  a malformed row or a duplicate claim id;
- NOTE   a claim citing a restricted source, so its use can be reviewed against the restriction.

Usage: python3 check_claims.py [slot ...]   (default: every slot). Exit 1 on any ERROR.
"""

import re
import sys
from collections import Counter
from pathlib import Path

BUILD = Path(__file__).resolve().parent.parent
HEADER = ["id", "claim", "level", "stack", "since", "sources", "agreement", "certainty", "mechanism", "quote", "tags"]
SRC_RE = re.compile(r"SRC-\d{3}")


def load_register() -> dict[str, dict]:
    register = {}
    for line in (BUILD / "audit" / "source_register.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"SRC-\d{3}", cells[0]):
            register[cells[0]] = {"tier": cells[1], "verdict": cells[2], "restriction": cells[7]}
    return register


def claim_rows(path: Path):
    in_table = False
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
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
        yield lineno, cells


def main(slots: list[str]) -> int:
    register = load_register()
    errors, notes, totals = [], [], Counter()
    paths = [BUILD / "research" / s / "result.md" for s in slots] if slots else sorted(
        (BUILD / "research").glob("*/result.md"))
    for path in paths:
        slot = path.parent.name
        seen, agreement = set(), Counter()
        for lineno, cells in claim_rows(path):
            where = f"{slot}:{lineno}"
            if len(cells) != len(HEADER):
                errors.append(f"{where}: {len(cells)} cells, expected {len(HEADER)}")
                continue
            row = dict(zip(HEADER, cells))
            if row["id"] in seen:
                errors.append(f"{where}: duplicate id {row['id']}")
            seen.add(row["id"])
            agreement[row["agreement"]] += 1
            cited = SRC_RE.findall(row["sources"])
            if not cited:
                errors.append(f"{where}: {row['id']} cites no register source")
            unknown = [s for s in cited if s not in register]
            if unknown:
                errors.append(f"{where}: {row['id']} cites unadmitted {', '.join(unknown)}")
            tiers = Counter(register[s]["tier"] for s in set(cited) if s in register)
            if row["agreement"] in ("consensus", "majority") and not (tiers["T1"] >= 1 or tiers["T2"] >= 2):
                errors.append(f"{where}: {row['id']} is {row['agreement']} on {dict(tiers)}, below threshold")
            restricted = [s for s in set(cited) if s in register and register[s]["verdict"] == "admit-restricted"]
            for s in restricted:
                notes.append(f"{where}: {row['id']} cites restricted {s} ({register[s]['restriction']})")
        totals.update(agreement)
        print(f"{slot}: {sum(agreement.values())} claims {dict(agreement)}")
    print(f"total: {sum(totals.values())} claims {dict(totals)}; errors {len(errors)}; restricted citations {len(notes)}")
    for e in errors:
        print("ERROR", e)
    for n in notes:
        print("NOTE ", n)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
