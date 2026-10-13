#!/usr/bin/env python3
"""Check branches/CHANGE_FLOW/branch.md against the routing and the L2 tree.

Proves: every row routed to CHANGE_FLOW is attached to exactly one node of the branch (none
unattached, none attached twice, none foreign); every uid follows the UID rules; the tree and
the records agree; every attached row appears in its node's positions; every link target
exists in tree_l2.md or in the branch. Run: python3 check_branch.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKEL = HERE.parent.parent  # 02_skeleton
BRANCH = "CHANGE_FLOW"
L1_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
KEY_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
VERBS = {"Realizes", "Requires", "Conflicts", "Refines", "Related"}

errors = []


def err(msg):
    errors.append(msg)


# --- routed rows of this branch ---
routed_all = {}
for line in (SKEL / "routing.md").read_text().splitlines():
    m = re.match(r"^(L\d+) ([A-Z][A-Z0-9_.]*)", line)
    if m:
        routed_all[m.group(1)] = m.group(2)
routed = {r for r, n in routed_all.items() if n == BRANCH or n.startswith(BRANCH + ".")}
routed_l2 = {r: n for r, n in routed_all.items() if r in routed}

# --- uids of tree_l2.md ---
tree_l2_uids = set(re.findall(r"`([A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)*)`", (SKEL / "tree_l2.md").read_text()))

# --- branch.md ---
text = (HERE / "branch.md").read_text()
tree_block = re.search(r"## Tree\n\n```text\n(.*?)```", text, re.S).group(1)
tree = {}
for line in tree_block.splitlines():
    uid, _, name = line.partition("  ")
    tree[uid.strip()] = name.strip()

# records
records = {}
cur = None
for line in text.splitlines():
    m = re.match(r"^#{2,3} (CHANGE_FLOW[A-Z0-9_.]*) (.+)$", line)
    if m:
        cur = m.group(1)
        records[cur] = {"name": m.group(2), "lines": []}
    elif cur:
        records[cur]["lines"].append(line)

# uid rules
for uid in tree:
    parts = uid.split(".")
    if parts[0] != BRANCH or not L1_RE.match(parts[0]):
        err(f"bad L1 in {uid}")
    if len(parts) >= 2 and not KEY_RE.match(parts[1]):
        err(f"L2 keyword invalid in {uid}")
    if len(parts) >= 2 and f"{parts[0]}.{parts[1]}" not in tree_l2_uids:
        err(f"L2 uid not in tree_l2.md: {uid}")
    for p in parts[2:]:
        if not re.match(r"^[0-9]+$", p):
            err(f"L3+ suffix must be numeric in {uid}")
    if len(parts) > 2 and ".".join(parts[:-1]) not in tree:
        err(f"parent missing for {uid}")
if set(tree) != set(records):
    err(f"tree/records differ: {sorted(set(tree) ^ set(records))}")
for uid, n in tree.items():
    if uid in records and records[uid]["name"] != n:
        err(f"name differs for {uid}")
# L2 nodes of tree_l2 present, same names
for uid in tree_l2_uids:
    if uid.startswith(BRANCH + ".") and uid.count(".") == 1 and uid not in tree:
        err(f"L2 node missing: {uid}")

# attached rows
attached = {}
l3_nodes = [u for u in tree if u.count(".") >= 2]
for uid, rec in records.items():
    body = "\n".join(rec["lines"])
    m = re.search(r"^- Rows: (.*)$", body, re.M)
    if not m:
        err(f"no Rows line: {uid}")
        continue
    rows_text = m.group(1)
    if rows_text.startswith("none"):
        if uid.count(".") >= 2:
            err(f"L3 node without rows: {uid}")
        continue
    if uid.count(".") < 2:
        err(f"rows attached to a non-leaf node: {uid}")
    ids = re.findall(r"L\d+", rows_text)
    cnt = re.search(r"\((\d+)\)\s*$", rows_text)
    if not cnt or int(cnt.group(1)) != len(ids):
        err(f"row count mismatch in {uid}")
    pos = body.split("- Positions:")[1].split("- Context variables:")[0] if "- Positions:" in body else ""
    if not re.search(r"^  - P1 ", pos, re.M):
        err(f"no position P1 in {uid}")
    for r in ids:
        attached.setdefault(r, []).append(uid)
        if r not in re.findall(r"L\d+", pos):
            err(f"{r} attached to {uid} but not cited in its positions")

twice = {r: u for r, u in attached.items() if len(u) > 1}
unattached = sorted(routed - set(attached))
foreign = sorted(set(attached) - routed)
for r in unattached:
    err(f"unattached row {r}")
for r in foreign:
    err(f"foreign row attached {r} (routed to {routed_all.get(r)})")
for r, u in twice.items():
    err(f"row attached twice {r}: {u}")
# cited rows exist
for r in set(re.findall(r"\bL\d{3,4}\b", text)):
    if r not in routed_all:
        err(f"cited row not in routing: {r}")

# links
branch_uids = set(tree)
n_links = 0
for uid, rec in records.items():
    for line in rec["lines"]:
        if line.startswith("- Links: "):
            for seg in line[len("- Links: "):].split(";"):
                toks = seg.strip().split()
                if not toks:
                    continue
                n_links += 1
                verb, target = toks[0], toks[1].rstrip(".,;:)") if len(toks) > 1 else ""
                if verb not in VERBS:
                    err(f"unknown link verb '{verb}' in {uid}")
                if target not in tree_l2_uids and target not in branch_uids and target != "ROOT":
                    err(f"link target not found '{target}' in {uid}")

n_pos = len(re.findall(r"^  - P\d+ ", text, re.M))
n_objections = len(re.findall(r"^- L\d+ ", text.split("## Routing objections")[1].split("\n## ")[0], re.M))
n_nodes = len(tree)
l2 = sum(1 for u in tree if u.count(".") == 1)
l3 = sum(1 for u in tree if u.count(".") == 2)
print(f"nodes {n_nodes} (L1 1, L2 {l2}, L3 {l3}); rows routed {len(routed)}; attached {len(attached)}; "
      f"unattached {len(unattached)}; attached twice {len(twice)}; foreign {len(foreign)}; "
      f"positions {n_pos}; links {n_links}; routing objections {n_objections}")
if errors:
    print("FAIL: " + str(len(errors)) + " problem(s)")
    for e in errors:
        print(" - " + e)
    sys.exit(1)
print("PASS: all routed rows attached once, uids valid, links resolve")
