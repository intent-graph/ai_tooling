#!/usr/bin/env python3
"""Check branch.md of the OWNERSHIP branch against routing.md and tree_l2.md.

Proves: every row routed to an OWNERSHIP L2 node is attached to exactly one node of
this branch, below the L2 node it was routed to; no foreign row is attached; every uid
follows the UID rules; the tree at the top equals the records; every link target exists
in tree_l2.md or in this branch; every L3 node lists positions; every MAINT row appears
in a position of its node; every routing objection names an attached row and a real
target node; the file holds no absolute or home path.
Prints the node and row counts and one final PASS or FAIL line.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKELETON = HERE.parent.parent  # 02_skeleton
BRANCH = "OWNERSHIP"
MAINT_ROWS = {"L308", "L310", "L312", "L330"}

errors = []


def err(msg):
    errors.append(msg)


# --- inputs -----------------------------------------------------------------
routing = {}
for line in (SKELETON / "routing.md").read_text().splitlines():
    m = re.match(r"^(L\d+) ([A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]*)", line)
    if m:
        routing[m.group(1)] = m.group(2)
mine = {r: n for r, n in routing.items() if n.split(".")[0] == BRANCH}

tree_uids = set(re.findall(r"^\| `([A-Z][A-Z0-9_.]*)` \|", (SKELETON / "tree_l2.md").read_text(), re.M))

text = (HERE / "branch.md").read_text()
body_start = text.index("## Records")
obj_start = text.index("## Routing objections")
tree_part = text[text.index("## Branch tree"):body_start]
records = text[body_start:obj_start]
objections = text[obj_start:]

# --- tree vs records --------------------------------------------------------
tree_nodes = re.findall(r"^\s*- `([A-Z][A-Z0-9_.]*)` (.+)$", tree_part, re.M)
rec_heads = re.findall(r"^#{3,5} ([A-Z][A-Z0-9_.]*) (.+)$", records, re.M)
if [u for u, _ in tree_nodes] != [u for u, _ in rec_heads]:
    err("tree order or uids differ from record headings")
if dict(tree_nodes) != dict(rec_heads):
    err("tree names differ from record names")
uids = [u for u, _ in rec_heads]
if len(uids) != len(set(uids)):
    err("duplicate uid")

# --- uid rules --------------------------------------------------------------
kw = re.compile(r"^[A-Z][A-Z0-9_]*$")
level = {}
for u in uids:
    parts = u.split(".")
    if u == BRANCH:
        level[u] = 1
    elif len(parts) == 2 and parts[0] == BRANCH and kw.match(parts[1]):
        level[u] = 2
        if BRANCH not in uids:
            err(f"{u}: parent missing")
    elif len(parts) >= 3 and parts[0] == BRANCH and kw.match(parts[1]) and all(p.isdigit() and not p.startswith("0") for p in parts[2:]):
        level[u] = len(parts)
        parent = ".".join(parts[:-1])
        if parent not in uids:
            err(f"{u}: parent {parent} missing")
    else:
        err(f"{u}: violates the UID format convention")
    if not re.match(r"^[A-Z][A-Z0-9_]*$", parts[0]):
        err(f"{u}: L1 part invalid")

# L2 nodes equal those of tree_l2.md
l2_tree = {u for u in tree_uids if u.startswith(BRANCH + ".") and u.count(".") == 1}
l2_here = {u for u in uids if level[u] == 2}
if l2_tree != l2_here:
    err(f"L2 nodes differ from tree_l2.md: {sorted(l2_tree ^ l2_here)}")

children = defaultdict(list)
for u in uids:
    if "." in u:
        children[u.rsplit(".", 1)[0]].append(u)
for u in uids:
    if level[u] == 2 and len(children[u]) == 1:
        err(f"{u}: a single child")
    if level[u] >= 3 and children[u]:
        err(f"{u}: unexpected deeper level")

# --- records ----------------------------------------------------------------
chunks = re.split(r"^#{3,5} ([A-Z][A-Z0-9_.]*) .+$", records, flags=re.M)
rec = {chunks[i]: chunks[i + 1] for i in range(1, len(chunks), 2)}
attached = defaultdict(list)
node_rows = {}
links = []
for u, ch in rec.items():
    m = re.search(r"^Rows: (.*)$", ch, re.M)
    if not m:
        err(f"{u}: no Rows line")
        continue
    val = m.group(1).strip()
    ids = [] if val.startswith("none") else [x.strip() for x in val.split(",")]
    for x in ids:
        if not re.fullmatch(r"L\d+", x):
            err(f"{u}: bad row id {x!r}")
        attached[x].append(u)
    node_rows[u] = ids
    if level[u] == 1 or level[u] == 2:
        if ids:
            err(f"{u}: rows attached above L3")
    if level[u] >= 3:
        if not re.search(r"^Positions:\s*$", ch, re.M) or not re.search(r"^- P1 ", ch, re.M):
            err(f"{u}: no positions")
        if not re.search(r"^Intent: .+", ch, re.M):
            err(f"{u}: no intent")
        for x in ids:
            if x in MAINT_ROWS:
                pos = ch[ch.index("Positions:"):]
                if not re.search(rf"MAINT[^\n]*\({x};|\({x}[;,][^\n]*REG-181|MAINT[^\n]*{x}", pos):
                    err(f"{u}: MAINT row {x} not a named position")
    for rel, target in re.findall(r"^- (Requires|Conflicts|Refines|Related|Realizes) `([A-Z][A-Z0-9_.]*)`", ch, re.M):
        links.append((u, rel, target))

# --- coverage ---------------------------------------------------------------
unattached = sorted(r for r in mine if r not in attached)
extra = sorted(r for r in attached if r not in mine)
multi = sorted(r for r, n in attached.items() if len(n) > 1)
if unattached:
    err(f"unattached rows: {unattached}")
if extra:
    err(f"rows not routed to this branch: {extra}")
if multi:
    err(f"rows attached more than once: {multi}")
for r, nodes in attached.items():
    if r in mine and not nodes[0].startswith(mine[r] + "."):
        err(f"{r}: attached to {nodes[0]}, routed to {mine[r]}")

# --- links ------------------------------------------------------------------
for u, rel, target in links:
    if target not in tree_uids and target not in uids:
        err(f"{u}: {rel} target {target} not found")

# --- objections -------------------------------------------------------------
n_obj = 0
for line in objections.splitlines():
    m = re.match(r"^\| (L\d+) \| `([^`]+)` \| `([^`]+)`", line)
    if not m:
        continue
    n_obj += 1
    row, here, target = m.groups()
    if row not in attached or here not in attached[row]:
        err(f"objection {row}: not attached to {here}")
    if target not in tree_uids:
        err(f"objection {row}: target {target} not in tree_l2.md")

# --- public repository hygiene ----------------------------------------------
for forbidden in ("/Users/", "/home/", "~/"):
    if forbidden in text:
        err(f"path-like string {forbidden!r} in branch.md")

# --- report -----------------------------------------------------------------
lv = Counter(level.values())
print(f"nodes: {len(uids)} (L1 {lv[1]}, L2 {lv[2]}, L3 {sum(v for k, v in lv.items() if k >= 3)})")
print(f"rows routed to branch: {len(mine)}; attached: {len(mine) - len(unattached)}; unattached: {len(unattached)}")
print(f"routing objections: {n_obj}")
for e in errors:
    print("ERROR:", e)
print("PASS" if not errors else f"FAIL ({len(errors)} errors)")
sys.exit(1 if errors else 0)
