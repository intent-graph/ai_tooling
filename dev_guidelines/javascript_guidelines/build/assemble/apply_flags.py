"""Stage 7, F05 and F17: put `unvalidated:` on every node whose rules rest on weak ground, by script.

Rule (one rule for both graphs). A node that carries a rule (a `decision` or `acceptable-when` ledger row) gets an
`unvalidated: <why>` issue in its epistemic_state when
  weak     any claim of the node is marked inferred, open or not confirmed in the claim table's `certainty` column;
  single   every rule row of the node is single-source (ledger `agreement` column);
  nosource a rule row carries no claim at all (build judgment);
  noquote  a claim behind a rule row has no quote or only a paraphrase marker in the claim table's `quote` column (F17).
An issue is added only when the node's existing `unvalidated:` issues do not already say it. `conflict:` and any other
issue are kept. The skeleton is edited in place; run before build_batches.py. Idempotent.

Run from the guideline root:  python3 build/assemble/apply_flags.py
"""
import glob
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batches as b  # noqa: E402

ROOT = b.ROOT

claims = {}
for p in sorted(glob.glob(str(ROOT / "build/research/[01][0-9]_*/result.md"))):
    hdr = None
    for line in open(p):
        if line.startswith("| id | claim | level"):
            hdr = [c.strip() for c in b.split_cells(line)]
            continue
        if hdr and line.startswith("|"):
            c = b.split_cells(line)
            if len(c) == len(hdr) and re.match(r"^[A-Z]+\d*-C\d+$", c[0]):
                claims[c[0]] = dict(zip(hdr, c))
        elif hdr:
            hdr = None

WEAK = re.compile(r"\b(inferred|open|not confirmed|not relied)\b")


def no_quote(c):
    q = claims[c]["quote"].strip()
    return q in ("", "-") or "paraphrase" in q.lower()


ledger = b.parse_ledger()
model = b.parse_skeleton()
skel_lines = b.SKEL.read_text().split("\n")
node_line = {}
for n, l in enumerate(skel_lines):
    m = re.match(r"\| ((?:PIG-JS\.)?[A-Z][A-Z0-9_.]*) \| ", l)
    if m and n < next(i for i, x in enumerate(skel_lines) if x.startswith("## Planned boundary links")):
        node_line[m.group(1)] = n

added = defaultdict(list)
changed = []
for gid in (b.P_ID, b.D_ID):
    for n in model["nodes"][gid]:
        uid = n["uid"]
        rows = [r for r in ledger if r["node"] == uid and r["graph"] == gid]
        rule = [r for r in rows if r["role"] in ("decision", "acceptable-when")]
        if not rule:
            continue
        state = n["epistemic"]
        parts = [x.strip() for x in state.split("|")]
        unv = " ".join(x for x in parts[1:] if x.startswith("unvalidated")).lower()
        new = []
        weak = sorted({c for r in rows for c in r["claims"] if c in claims and WEAK.search(claims[c]["certainty"])})
        if weak and not re.search(r"inferred|open|not confirmed", unv):
            new.append(f"unvalidated: rests on claims marked inferred or open ({', '.join(weak)})")
            added["weak"].append(uid)
        claimed = [r for r in rule if r["claims"]]
        if claimed and all(r["agreement"] == "single-source" for r in claimed) and not re.search(r"single|holder|position", unv):
            new.append("unvalidated: rests on single-source claims only")
            added["single"].append(uid)
        if any(not r["claims"] for r in rule) and not unv:
            new.append("unvalidated: a rule has no claim of its own, it is the build's judgment")
            added["nosource"].append(uid)
        nq = sorted({c for r in rule for c in r["claims"] if c in claims and no_quote(c)})
        if nq and "quote not obtained" not in state:
            new.append(f"unvalidated: quote not obtained ({', '.join(nq)})")
            added["noquote"].append(uid)
        if new:
            changed.append(uid)
            cells = b.split_cells(skel_lines[node_line[uid]])
            cells[3] = cells[3] + " \\| " + " \\| ".join(new)
            skel_lines[node_line[uid]] = "| " + " | ".join(cells) + " |"

b.SKEL.write_text("\n".join(skel_lines))
print({k: len(v) for k, v in added.items()}, "nodes changed:", len(changed))
