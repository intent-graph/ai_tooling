#!/usr/bin/env python3
"""Check branch.md of the TRANSVERSE branch against routing.md, tree_l2.md and the claims ledger.

Proves, from the written files only:
  1. rows routed to a TRANSVERSE.* node in routing.md (the branch's rows) are each attached to exactly one
     node record of branch.md; no row is unattached, attached twice, or unknown to the ledger;
  2. uids follow the IntentGraph UID rules: L1 `TRANSVERSE`; L2 `TRANSVERSE.<KEYWORD>` exactly as tree_l2.md
     names them; L3 `<L2 uid>.<n>` numeric; every uid unique; names hold none of /\\:*?"<>|[]#^;
  3. the branch tree at the top of branch.md matches the node records (same uids, same order);
  4. an L2 node with children carries `Rows: -`; every L3 node carries at least one row;
  5. every link target (uid in backticks on a Links line) exists in tree_l2.md or the branch;
  6. every maintainer row (areas starting with MAINT in the ledger) of the branch is named as a position;
  7. every node record carries Intent, Rows, Positions (L3), Links; no absolute or home path is written;
  8. the rows count of each L2 node (sum of its L3 rows) equals the count in tree_l2.md.
Prints the counts and one PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DISTILL = HERE.parents[2]
SKEL = DISTILL / '02_skeleton'
ROUTING = SKEL / 'routing.md'
TREE = SKEL / 'tree_l2.md'
BRANCH = HERE / 'branch.md'
LEDGERS = [DISTILL / '01_consolidate' / 'claims_ledger.md',
           DISTILL / '01_consolidate' / 'part2' / 'claims_ledger_part2.md',
           DISTILL / '01_consolidate' / 'part3' / 'claims_ledger_part3.md']
L1 = 'TRANSVERSE'
errors = []


def err(m):
    errors.append(m)


# ledger rows (id -> areas column)
ledger = {}
for f in LEDGERS:
    for line in f.read_text().splitlines():
        m = re.match(r'\| (L\d+) \|', line)
        if m:
            cells = [c.strip() for c in line.strip().strip('|').split(' | ')]
            ledger[m.group(1)] = cells[3] if len(cells) > 3 else ''

# routing: this branch's rows
routed = {}
for line in ROUTING.read_text().splitlines():
    m = re.match(r'(L\d+) (\S+)', line)
    if m and m.group(2).startswith(L1 + '.'):
        routed[m.group(1)] = m.group(2)

# tree_l2: uids and rows column
tree_uids, tree_rows = set(), {}
for line in TREE.read_text().splitlines():
    m = re.match(r'\| `([A-Z0-9_.]+)` \| [^|]+ \| .* \| (\d+|-) \|', line)
    if m:
        tree_uids.add(m.group(1))
        if m.group(2) != '-':
            tree_rows[m.group(1)] = int(m.group(2))
for u in ['ROOT', L1]:
    if u not in tree_uids:
        err('tree_l2.md lacks ' + u)
l2_expected = sorted(u for u in tree_uids if u.startswith(L1 + '.') and u.count('.') == 1)

text = BRANCH.read_text()
head, _, body = text.partition('## Node records')
tree_part = head.split('## Branch tree')[1] if '## Branch tree' in head else ''
tree_listed = re.findall(r'^\s*- `([A-Z0-9_.]+)` (.+)$', tree_part, re.M)

# node records
recs = []
for m in re.finditer(r'^### `([A-Z0-9_.]+)` ([^\n]+)\n(.*?)(?=^### |^## |\Z)', body, re.M | re.S):
    recs.append((m.group(1), m.group(2).strip(), m.group(3)))
# the L1 record is also under Node records
uids = [u for u, _, _ in recs]
if len(uids) != len(set(uids)):
    err('node uids repeat: %s' % [u for u, c in Counter(uids).items() if c > 1])
if [u for u, _ in tree_listed] != uids:
    err('branch tree and node records differ in uids or order')
if dict(tree_listed) != {u: n for u, n, _ in recs}:
    err('names differ between branch tree and records')

L2 = [u for u in uids if u.count('.') == 1]
L3 = [u for u in uids if u.count('.') == 2]
if uids and uids[0] != L1:
    err('first record is not ' + L1)
if sorted(L2) != l2_expected:
    err('L2 nodes differ from tree_l2.md: %s vs %s' % (sorted(L2), l2_expected))
kw = re.compile(r'^[A-Z][A-Z0-9_]*$')
for u in uids:
    p = u.split('.')
    if u == L1:
        ok = bool(kw.match(u))
    elif len(p) == 2:
        ok = p[0] == L1 and bool(kw.match(p[1]))
    elif len(p) == 3:
        ok = p[0] == L1 and bool(kw.match(p[1])) and p[2].isdigit() and (L1 + '.' + p[1]) in uids
    else:
        ok = False
    if not ok:
        err('bad uid ' + u)
for u, n, _ in recs:
    if re.search(r'[/\\:*?"<>|\[\]#^]', n):
        err('name of %s holds a forbidden character' % u)
# L3 numbering is 1..n per L2
for l2 in L2:
    nums = [int(u.split('.')[2]) for u in L3 if u.startswith(l2 + '.')]
    if nums != list(range(1, len(nums) + 1)):
        err('L3 numbering of %s is not 1..n: %s' % (l2, nums))

# attached rows
attached = Counter()
node_rows = {}
rows_dash = {}
for u, n, b in recs:
    m = re.search(r'^- Rows: (.*)$', b, re.M)
    if not m:
        err('%s lacks Rows' % u)
        continue
    val = m.group(1).strip()
    if val.startswith('-'):
        rows_dash[u] = True
        node_rows[u] = []
        continue
    ids = re.findall(r'L\d+', val.split('(')[0])
    node_rows[u] = ids
    for i in ids:
        attached[i] += 1
    for key in ('Intent', 'Links'):
        if not re.search(r'^- %s: ' % key, b, re.M):
            err('%s lacks %s' % (u, key))
    if u in L3 and not re.search(r'^- Positions:', b, re.M):
        err('%s lacks Positions' % u)
    if u in L3 and not ids:
        err('%s holds no row' % u)
for u in uids:
    if u not in L3:
        if u in node_rows and node_rows[u]:
            err('%s is not a leaf but holds rows' % u)
        if u != L1 and not rows_dash.get(u):
            err('%s lacks the roll-up marker "Rows: -"' % u)
unattached = sorted(set(routed) - set(attached))
twice = sorted(i for i, c in attached.items() if c > 1)
extra = sorted(set(attached) - set(routed))
unknown = sorted(i for i in attached if i not in ledger)
if unattached:
    err('rows routed but unattached: %s' % unattached)
if twice:
    err('rows attached twice: %s' % twice)
if extra:
    err('rows attached but not routed to this branch: %s' % extra)
if unknown:
    err('rows unknown to the ledger: %s' % unknown)
# row's node must sit under the routed L2
for u in L3:
    for i in node_rows.get(u, []):
        if i in routed and routed[i] != u.rsplit('.', 1)[0]:
            err('%s attached under %s but routed to %s' % (i, u, routed[i]))
# rows count per L2
for l2 in L2:
    n = sum(len(node_rows[u]) for u in L3 if u.startswith(l2 + '.'))
    if tree_rows.get(l2) != n:
        err('%s: %d rows attached, tree_l2.md says %s' % (l2, n, tree_rows.get(l2)))

# links
for u, n, b in recs:
    m = re.search(r'^- Links: (.*)$', b, re.M)
    if m:
        for t in re.findall(r'`([A-Z][A-Z0-9_.]*)`', m.group(1)):
            if t not in tree_uids and t not in uids:
                err('%s links to unknown %s' % (u, t))

# maintainer rows are named positions
maint = sorted(i for i in routed if ledger.get(i, '').startswith('MAINT'))
for i in maint:
    holder = [u for u in L3 if i in node_rows.get(u, [])]
    if not holder:
        continue
    b = [x for x in recs if x[0] == holder[0]][0][2]
    if not re.search(r'%s \(MAINT' % i, b):
        err('maintainer row %s is not named as a MAINT position on %s' % (i, holder[0]))

# routing objections
obj = re.search(r'^## Routing objections\n(.*)\Z', text, re.M | re.S)
objections = re.findall(r'^\d+\. (L\d+)', obj.group(1), re.M) if obj else []

# no absolute or home path in branch.md
if re.search(r'(^|[\s`(])(/(Users|home|private|tmp)/|~/)', text):
    err('branch.md holds an absolute or home path')

nodes = len(uids)
print('nodes: %d (L1 %d, L2 %d, L3 %d)' % (nodes, 1, len(L2), len(L3)))
print('rows routed to the branch: %d; attached: %d; unattached: %d; attached twice: %d' % (
    len(routed), len(set(attached) & set(routed)), len(unattached), len(twice)))
print('maintainer rows named as positions: %s' % maint)
print('routing objections: %d %s' % (len(objections), objections))
if errors:
    for e in errors:
        print('ERROR: ' + e)
    print('FAIL: %d errors' % len(errors))
    sys.exit(1)
print('PASS: %d nodes, %d of %d rows attached once, 0 unattached, links and uids valid' % (
    nodes, len(set(attached)), len(routed)))
