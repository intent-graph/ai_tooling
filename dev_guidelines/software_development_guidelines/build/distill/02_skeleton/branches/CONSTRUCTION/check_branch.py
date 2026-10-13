#!/usr/bin/env python3
"""Check branch.md of the CONSTRUCTION branch against tree_l2.md and routing.md.

Proves, from the written files only:
  1. every row routed to a CONSTRUCTION.* node in routing.md is attached (a `Rows:` line) to exactly one
     node of branch.md, no row is attached twice, no unknown or foreign row is attached;
  2. the tree at the top of branch.md and the node records agree (same uids, same order, same names);
  3. uids follow the IntentGraph UID rules: L1 `CONSTRUCTION`; L2 `CONSTRUCTION.KEYWORD` equal to tree_l2.md;
     L3 `<L2 uid>.<n>` numeric suffix only, with an existing parent, unique; names hold none of /\\:*?"<>|[]#^;
  4. every `Rows:` count equals its listed ids; the rows of each L2 node and its children equal the
     count in tree_l2.md; every L2 node of tree_l2.md under CONSTRUCTION has a record;
  5. every uid in a `Links:` line exists in tree_l2.md or in this branch, and is not the record's own uid;
  6. every MAINT row (L309, L311, L315, L329) appears as a named "MAINT position" on its node;
  7. every routing objection names a routed row and an existing target node outside its own node;
  8. the file holds no absolute or home path.
Prints the counts and one PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKEL = HERE.parent.parent
BRANCH = HERE / 'branch.md'
TREE = SKEL / 'tree_l2.md'
ROUTING = SKEL / 'routing.md'
L1 = 'CONSTRUCTION'
MAINT_ROWS = ['L309', 'L311', 'L315', 'L329']
FORBIDDEN = set('/\\:*?"<>|[]#^')
KW = r'[A-Z][A-Z0-9_]*'

errors = []


def err(m):
    errors.append(m)


# ---- tree_l2.md: every L2 uid and its row count
tree_uids = set()
tree_rows = {}
for line in TREE.read_text().splitlines():
    m = re.match(r'\| `([A-Z][A-Za-z0-9_.]*)` \| (.+?) \| .*? \| (\d+|-) \|', line)
    if m:
        tree_uids.add(m.group(1))
        if m.group(3) != '-':
            tree_rows[m.group(1)] = int(m.group(3))

# ---- routing.md: rows routed to CONSTRUCTION.*
routed = {}
for line in ROUTING.read_text().splitlines():
    m = re.match(r'^(L\d+) (\S+)', line)
    if m:
        routed[m.group(1)] = m.group(2)
mine = {r: n for r, n in routed.items() if n.startswith(L1 + '.')}
for r, n in mine.items():
    if n not in tree_uids:
        err('routing sends %s to unknown node %s' % (r, n))

text = BRANCH.read_text()
lines = text.splitlines()

# ---- tree at the top
tree_list = []
in_tree = False
for line in lines:
    if line.startswith('## Tree'):
        in_tree = True
        continue
    if in_tree and line.startswith('## '):
        break
    m = re.match(r'^\s*- `([A-Z][A-Z0-9_.]*)` (.+)$', line)
    if in_tree and m:
        tree_list.append((m.group(1), m.group(2).strip()))

# ---- records
records = []  # (uid, name, rows_line, links_line, body)
cur = None
for line in lines:
    m = re.match(r'^#### (\S+) (.+)$', line)
    if m:
        cur = {'uid': m.group(1), 'name': m.group(2).strip(), 'rows': None, 'links': '', 'body': []}
        records.append(cur)
        continue
    if line.startswith('## '):
        cur = None
    if cur is not None:
        cur['body'].append(line)
        if line.startswith('Rows:'):
            cur['rows'] = line
        if line.startswith('Links:'):
            cur['links'] += line + '\n'

rec_uids = [r['uid'] for r in records]
branch_uids = set(rec_uids)
if len(rec_uids) != len(branch_uids):
    err('duplicate record uids')
if rec_uids != [u for u, _ in tree_list]:
    err('tree at the top and record headings differ (uids or order)')
if [r['name'] for r in records] != [n for _, n in tree_list]:
    err('tree at the top and record headings differ (names)')

# ---- uid rules
l2_uids = []
for r in records:
    u = r['uid']
    for ch in r['name']:
        if ch in FORBIDDEN:
            err('name of %s holds forbidden character %r' % (u, ch))
    if u == L1:
        continue
    if re.fullmatch(L1 + r'\.' + KW, u):
        l2_uids.append(u)
        if u not in tree_uids:
            err('L2 uid %s is not in tree_l2.md' % u)
    elif re.fullmatch(L1 + r'\.' + KW + r'\.[0-9]+', u):
        parent = u.rsplit('.', 1)[0]
        if parent not in branch_uids:
            err('L3 uid %s has no parent record' % u)
    else:
        err('uid %s breaks the UID rules' % u)
for u in tree_uids:
    if u.startswith(L1 + '.') and u not in branch_uids:
        err('tree_l2.md node %s has no record' % u)
if L1 not in branch_uids:
    err('no record for %s' % L1)

# ---- attachments
attached = {}
per_node = {}
for r in records:
    if r['rows'] is None:
        err('record %s has no Rows line' % r['uid'])
        continue
    ids = re.findall(r'\bL\d+\b', r['rows'])
    cm = re.search(r'\((\d+)\)\s*$', r['rows'])
    if not cm or int(cm.group(1)) != len(ids):
        err('record %s: Rows count does not equal its listed ids' % r['uid'])
    per_node[r['uid']] = ids
    for i in ids:
        attached.setdefault(i, []).append(r['uid'])
for i, nodes in attached.items():
    if len(nodes) > 1:
        err('row %s attached to several nodes: %s' % (i, nodes))
    if i not in mine:
        err('row %s attached but not routed to this branch' % i)
unattached = sorted(set(mine) - set(attached))
for i in unattached:
    err('row %s routed to %s is not attached' % (i, mine[i]))
# attached node lies under the routed L2 node
for i, nodes in attached.items():
    if i in mine and not (nodes[0] == mine[i] or nodes[0].startswith(mine[i] + '.')):
        err('row %s attached to %s, outside its routed node %s' % (i, nodes[0], mine[i]))
# per-L2 totals equal tree_l2.md
for u in l2_uids:
    total = sum(len(v) for k, v in per_node.items() if k == u or k.startswith(u + '.'))
    if tree_rows.get(u) != total:
        err('%s holds %d rows, tree_l2.md says %s' % (u, total, tree_rows.get(u)))

# ---- links
for r in records:
    for u in re.findall(r'`([A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)*)`', r['links']):
        if u not in tree_uids and u not in branch_uids and u != 'ROOT':
            err('link target %s of %s does not exist' % (u, r['uid']))
        if u == r['uid']:
            err('record %s links to itself' % r['uid'])

# ---- MAINT rows named as positions
for row in MAINT_ROWS:
    node = (attached.get(row) or [None])[0]
    rec = next((r for r in records if r['uid'] == node), None)
    if rec is None or not any('MAINT position (%s' % row in l for l in rec['body']):
        err('MAINT row %s has no "MAINT position (%s" on its node' % (row, row))

# ---- routing objections
obj_rows = []
in_obj = False
for line in lines:
    if line.startswith('## Routing objections'):
        in_obj = True
        continue
    if in_obj and line.startswith('## '):
        break
    m = re.match(r'^\| (L\d+) \| (\S+) \| (\S+) \|', line)
    if in_obj and m:
        row, frm, to = m.groups()
        obj_rows.append(row)
        if mine.get(row) != frm:
            err('objection %s: routed node %s is not the routing.md node %s' % (row, frm, mine.get(row)))
        if to not in tree_uids:
            err('objection %s: target %s not in tree_l2.md' % (row, to))
        if to == frm:
            err('objection %s: target equals routed node' % row)
if len(obj_rows) != len(set(obj_rows)):
    err('a routing objection is listed twice')

# ---- no absolute or home path
for n, line in enumerate(lines, 1):
    if re.search(r'(/Users/|/home/|~/|[A-Za-z]:\\\\)', line):
        err('line %d holds an absolute or home path' % n)

n_nodes = len(records)
n_l2 = len(l2_uids)
n_l3 = n_nodes - 1 - n_l2
print('nodes: %d (L1 1, L2 %d, L3 %d)' % (n_nodes, n_l2, n_l3))
print('rows routed to CONSTRUCTION: %d' % len(mine))
print('rows attached: %d' % len([i for i in attached if i in mine]))
print('rows unattached: %d' % len(unattached))
print('routing objections: %d' % len(obj_rows))
if errors:
    for e in errors:
        print('ERROR: ' + e)
    print('FAIL: %d error(s)' % len(errors))
    sys.exit(1)
print('PASS: branch CONSTRUCTION: %d nodes, %d rows each attached once, 0 unattached, uids and links valid' % (n_nodes, len(mine)))
sys.exit(0)
