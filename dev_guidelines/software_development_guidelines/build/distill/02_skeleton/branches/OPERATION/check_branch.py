#!/usr/bin/env python3
"""Check branch.md of the OPERATION branch against routing.md and tree_l2.md.

Proves: every row routed to OPERATION.* is attached to exactly one branch node (and no other
row is attached); every uid follows the UID rules; every link target exists in tree_l2.md or
the branch; every MAINT row (maintainer practice) carries a named (MAINT) position.
Run from anywhere: python3 check_branch.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKEL = HERE.parent.parent  # 02_skeleton/
BRANCH = "OPERATION"
KEYWORD = re.compile(r"^[A-Z][A-Z0-9_]*$")
UID_TOKEN = re.compile(r"\b[A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)+\b")
LINK_TYPES = ("Realizes", "Requires", "Conflicts", "Refines", "Related")

errors = []


def err(msg):
    errors.append(msg)


# routed rows
routed = {}
for line in (SKEL / "routing.md").read_text().splitlines():
    m = re.match(r"^(L\d+) (\S+)", line)
    if m and (m.group(2) == BRANCH or m.group(2).startswith(BRANCH + ".")):
        routed[m.group(1)] = m.group(2)

# tree_l2 uids
tree_uids = set(re.findall(r"`([A-Z][A-Z0-9_]*(?:\.[A-Z][A-Z0-9_]*)?)`", (SKEL / "tree_l2.md").read_text()))
tree_uids.add("ROOT")

# branch nodes
text = (HERE / "branch.md").read_text()
body = text.split("## Node records", 1)[1].split("## Routing objections", 1)[0]
records = re.split(r"\n### ", "\n" + body)[1:]
nodes = {}
for rec in records:
    uid = re.search(r"- uid: `([^`]+)`", rec)
    if not uid:
        err("record without uid line")
        continue
    uid = uid.group(1)
    if uid in nodes:
        err(f"duplicate node {uid}")
    rows_line = re.search(r"^- rows: (.*)$", rec, re.M).group(1)
    rows = re.findall(r"\bL\d+\b", rows_line)
    links_line = re.search(r"^- links: (.*)$", rec, re.M).group(1)
    nodes[uid] = dict(rows=rows, links=links_line, rec=rec)

# uid rules
for uid in nodes:
    parts = uid.split(".")
    if parts[0] != BRANCH:
        err(f"{uid}: not in branch {BRANCH}")
    if len(parts) >= 2 and not KEYWORD.match(parts[1]):
        err(f"{uid}: L2 keyword invalid")
    if len(parts) > 3 or any(not p.isdigit() for p in parts[2:]):
        err(f"{uid}: L3+ must be numeric suffixes (depth at most 3 here)")
    if len(parts) == 2 and uid not in tree_uids:
        err(f"{uid}: L2 node not in tree_l2.md")
    if len(parts) >= 2 and ".".join(parts[:-1]) not in nodes:
        err(f"{uid}: parent missing")
for u in sorted({t for t in tree_uids if t.startswith(BRANCH + ".")} - set(nodes)):
    err(f"L2 node {u} of tree_l2.md missing from branch")

# attachment
attach = {}
for uid, n in nodes.items():
    for r in n["rows"]:
        attach.setdefault(r, []).append(uid)
for r in routed:
    if r not in attach:
        err(f"row {r} routed to {routed[r]} but unattached")
for r, where in attach.items():
    if r not in routed:
        err(f"row {r} attached to {where} but not routed to {BRANCH}")
    if len(where) > 1:
        err(f"row {r} attached to several nodes: {where}")
    elif r in routed and not where[0].startswith(routed[r]):
        err(f"row {r} routed to {routed[r]} but attached under {where[0]}")
for uid, n in nodes.items():
    if n["rows"] and any(k.startswith(uid + ".") for k in nodes):
        err(f"{uid}: has children and also rows")

# links
for uid, n in nodes.items():
    if n["links"].startswith("none"):
        continue
    for item in n["links"].split("; "):
        if not item.startswith(LINK_TYPES):
            err(f"{uid}: link '{item[:40]}' does not start with one of {LINK_TYPES}")
        for tgt in UID_TOKEN.findall(item):
            if tgt not in nodes and tgt not in tree_uids:
                err(f"{uid}: link target {tgt} not in tree_l2.md or branch")

# MAINT rows: ledger rows whose merges column names a MAINT claim
ledger_dir = SKEL.parent / "01_consolidate"
for lf in (ledger_dir / "claims_ledger.md", ledger_dir / "part2" / "claims_ledger_part2.md",
           ledger_dir / "part3" / "claims_ledger_part3.md"):
    for line in lf.read_text().splitlines():
        m = re.match(r"\| (L\d+) \|", line)
        if m and m.group(1) in routed and "MAINT-C" in line.split("|")[3]:
            where = attach.get(m.group(1), [None])[0]
            if where and "(MAINT)" not in nodes[where]["rec"]:
                err(f"MAINT row {m.group(1)} has no named (MAINT) position on {where}")

n_nodes = len(nodes)
n_attached = sum(1 for r in routed if r in attach)
n_unattached = len(routed) - n_attached
if errors:
    for e in errors:
        print("ERROR:", e)
    print(f"FAIL: nodes {n_nodes}, routed rows {len(routed)}, attached {n_attached}, unattached {n_unattached}, errors {len(errors)}")
    sys.exit(1)
print(f"PASS: nodes {n_nodes}, routed rows {len(routed)}, attached {n_attached}, unattached {n_unattached}, attached twice 0, errors 0")
