#!/usr/bin/env python3
"""Check the ASSURANCE branch refinement (branch.md, result.md) against routing.md and tree_l2.md.

Proves, from the written files only:
  1. every row routed to an ASSURANCE L2 node in routing.md is attached to exactly one L3 node of branch.md,
     none is missing, none is unknown to the ledger, none is attached twice;
  2. each row is attached under the L2 node it is routed to (the branch does not move rows);
  3. the tree at the top of branch.md equals the node records, uids follow the IntentGraph UID rules
     (L1 ^[A-Z][A-Z0-9_]*$, L2 {L1}.{KEYWORD} existing in tree_l2.md, L3 numeric suffix only), names hold
     none of /\\:*?"<>|[]#^, every L3 holds at least one row and its stated count, each L2 count equals
     the count of tree_l2.md;
  4. every node uid cited anywhere in branch.md exists in tree_l2.md or in the branch;
  5. the pinned counts of branch.md and result.md equal the recomputed ones; the objection rows exist in the
     ledger and are attached;
  6. the written files hold no absolute or home path.
Prints the counts and one PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKELETON = HERE.parent.parent
DISTILL = SKELETON.parent
LEDGERS = [DISTILL / '01_consolidate' / 'claims_ledger.md',
           DISTILL / '01_consolidate' / 'part2' / 'claims_ledger_part2.md',
           DISTILL / '01_consolidate' / 'part3' / 'claims_ledger_part3.md']
TREE = SKELETON / 'tree_l2.md'
ROUTING = SKELETON / 'routing.md'
BRANCH = HERE / 'branch.md'
RESULT = HERE / 'result.md'
L1 = 'ASSURANCE'

errors = []


def err(msg):
    errors.append(msg)


# ---- ledger ids
ledger = set()
for f in LEDGERS:
    for line in f.read_text().splitlines():
        m = re.match(r'\| (L\d+) \|', line)
        if m:
            ledger.add(m.group(1))

# ---- routing: rows routed to this branch
routed = {}
for line in ROUTING.read_text().splitlines():
    m = re.match(r'(L\d+) (' + L1 + r'\.[A-Z][A-Z0-9_]*)(?: \|.*)?$', line)
    if m:
        routed[m.group(1)] = m.group(2)
for r in routed:
    if r not in ledger:
        err('routed row %s not in the ledger' % r)

# ---- tree_l2: all uids and the row counts of this branch
tree_uids = set()
tree_rows = {}
for line in TREE.read_text().splitlines():
    m = re.match(r'\| `([A-Z][A-Z0-9_.]*)` \| (.*?) \| .*? \| (\d+|-) \|', line)
    if m:
        tree_uids.add(m.group(1))
        if m.group(3) != '-':
            tree_rows[m.group(1)] = int(m.group(3))

text = BRANCH.read_text()

# ---- branch tree block
block = re.search(r'## Tree\s+```text\n(.*?)```', text, re.S)
tree_branch = []
if not block:
    err('no tree block in branch.md')
else:
    for line in block.group(1).splitlines():
        m = re.match(r'\s*(\S+) (.+)$', line)
        if m:
            tree_branch.append((m.group(1), m.group(2)))

# ---- node records
records = []  # (uid, name, rows list, stated count or None)
cur = None
for line in text.splitlines():
    m = re.match(r'#{2,3} (' + L1 + r'(?:\.[A-Za-z0-9_]+)*) (.+)$', line)
    if m:
        cur = {'uid': m.group(1), 'name': m.group(2), 'rows': None, 'count': None}
        records.append(cur)
        continue
    if cur and line.startswith('Rows:'):
        body = line[len('Rows:'):].strip()
        if body.startswith('-'):
            cur['rows'] = []
            cm = re.search(r'(\d+) rows', body)
            cur['count'] = int(cm.group(1)) if cm else None
            cur['rollup'] = True
        else:
            ids = re.findall(r'\bL\d+\b', body)
            cm = re.search(r'\((\d+)\)\s*$', body)
            cur['rows'] = ids
            cur['count'] = int(cm.group(1)) if cm else None
            cur['rollup'] = False

rec = {r['uid']: r for r in records}
if len(rec) != len(records):
    err('a node record uid repeats')
if [u for u, _ in tree_branch] != [r['uid'] for r in records]:
    err('tree block and node records differ (uids or order)')
if dict(tree_branch) != {r['uid']: r['name'] for r in records}:
    err('tree block names differ from record names')

# ---- uid rules, names
l2_set = set()
l3_set = set()
for r in records:
    u = r['uid']
    parts = u.split('.')
    if len(parts) == 1:
        if u != L1 or not re.fullmatch(r'[A-Z][A-Z0-9_]*', u):
            err('bad L1 uid %s' % u)
    elif len(parts) == 2:
        if not re.fullmatch(r'[A-Z][A-Z0-9_]*', parts[1]):
            err('bad L2 keyword in %s' % u)
        if u not in tree_uids:
            err('L2 uid %s not in tree_l2.md' % u)
        l2_set.add(u)
    elif len(parts) == 3:
        if not re.fullmatch(r'[1-9][0-9]*', parts[2]):
            err('L3 suffix of %s is not numeric' % u)
        if '.'.join(parts[:2]) not in tree_uids:
            err('L3 parent of %s not in tree_l2.md' % u)
        l3_set.add(u)
    else:
        err('uid %s is deeper than L3' % u)
    if re.search(r'[/\\:*?"<>|\[\]#^]', r['name']):
        err('name of %s holds a forbidden character' % u)
    if r['rows'] is None:
        err('record %s has no Rows line' % u)

tree_l2_branch = {u for u in tree_uids if u.startswith(L1 + '.')}
if l2_set != tree_l2_branch:
    err('L2 nodes differ from tree_l2.md: missing %s, extra %s' % (sorted(tree_l2_branch - l2_set), sorted(l2_set - tree_l2_branch)))
for u in l2_set:
    kids = [k for k in l3_set if k.startswith(u + '.')]
    if not kids:
        err('L2 node %s has no L3 child (every L2 here is a roll-up)' % u)
    if len(kids) == 1:
        err('L2 node %s has a single L3 child' % u)

# ---- attachment
attached = Counter()
where = {}
for r in records:
    if r['uid'] in l3_set:
        if not r['rows']:
            err('L3 node %s holds no row' % r['uid'])
        if r['count'] != len(r['rows']):
            err('L3 node %s states %s rows but lists %d' % (r['uid'], r['count'], len(r['rows'])))
        for i in r['rows']:
            attached[i] += 1
            where[i] = r['uid']
    elif r['rows']:
        err('non-leaf node %s attaches rows' % r['uid'])
twice = sorted(i for i, n in attached.items() if n > 1)
if twice:
    err('attached twice: %s' % twice[:10])
unattached = sorted(set(routed) - set(attached))
extra = sorted(set(attached) - set(routed))
if unattached:
    err('unattached: %s' % unattached[:10])
if extra:
    err('attached but not routed here: %s' % extra[:10])
for i, u in where.items():
    if i in routed and '.'.join(u.split('.')[:2]) != routed[i]:
        err('row %s attached under %s but routed to %s' % (i, u, routed[i]))

# ---- L2 counts
l2_count = Counter()
for i, u in where.items():
    l2_count['.'.join(u.split('.')[:2])] += 1
for u in l2_set:
    if tree_rows.get(u) != l2_count[u]:
        err('rows of %s: tree_l2.md says %s, branch holds %d' % (u, tree_rows.get(u), l2_count[u]))
    if rec[u]['count'] is not None and rec[u]['count'] != l2_count[u]:
        err('roll-up count of %s states %s, recomputed %d' % (u, rec[u]['count'], l2_count[u]))
if rec[L1]['count'] is not None and rec[L1]['count'] != len(attached):
    err('L1 roll-up count %s differs from %d' % (rec[L1]['count'], len(attached)))

# ---- link targets: every uid cited anywhere resolves
valid = set(tree_uids) | set(rec) | {'ROOT'}
cited = set(re.findall(r'\b(?:OWNERSHIP|ASSURANCE|CONSTRUCTION|CHANGE_FLOW|OPERATION|EVOLUTION|TRANSVERSE)(?:\.[A-Z][A-Z0-9_]*)(?:\.[0-9]+)*', text))
for c in sorted(cited):
    if c not in valid:
        err('cited uid %s exists neither in tree_l2.md nor in the branch' % c)
for line in text.splitlines():
    if line.startswith('Links:'):
        for t in re.findall(r'\b[A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)+', line):
            if t not in valid:
                err('link target %s unknown' % t)

# ---- objections
obj = []
sec = text.split('## Routing objections', 1)
if len(sec) == 2:
    for line in sec[1].splitlines():
        m = re.match(r'\| (L\d+) \| (\S+) \| (\S+) \|', line)
        if m:
            obj.append(m.groups())
for row, now, to, *_ in obj:
    if row not in routed:
        err('objection row %s not routed to this branch' % row)
    elif where.get(row) != now:
        err('objection row %s is attached to %s, not %s' % (row, where.get(row), now))
    if to not in tree_uids:
        err('objection target %s not in tree_l2.md' % to)
    if to.startswith(L1 + '.'):
        err('objection target %s is inside this branch' % to)

# ---- pins
n_nodes = len(records)
n_att = len(attached)
n_un = len(unattached)
n_obj = len(obj)
n_l1, n_l2, n_l3 = 1, len(l2_set), len(l3_set)
pins_b = [
    'Nodes: %d (L1 %d, L2 %d, L3 %d).' % (n_nodes, n_l1, n_l2, n_l3),
    'Rows attached: %d of %d; unattached: %d; attached twice: %d.' % (n_att, len(routed), n_un, len(twice)),
    'Routing objections: %d' % n_obj,
]
for p in pins_b:
    if p not in text:
        err('branch.md pin missing or wrong: %s' % p)
if RESULT.exists():
    rt = RESULT.read_text()
    secs = re.split(r'(?m)^(?=## )', rt)
    names = [s.split('\n', 1)[0] for s in secs if s.startswith('## ')]
    if names != ['## L1 headline', '## L2 claims', '## L3 full']:
        err('result.md sections are %s' % names)
    for s in secs:
        if not s.startswith('## '):
            continue
        for p in ['Nodes: %d' % n_nodes, 'Rows attached: %d of %d' % (n_att, len(routed)), 'unattached: %d' % n_un,
                  'Routing objections: %d' % n_obj]:
            if p not in s:
                err('result.md section "%s" lacks the pin "%s"' % (s.split('\n', 1)[0], p))
        if not re.search(r'check_branch\.py: PASS|check_branch\.py: FAIL', s):
            err('result.md section "%s" lacks the script pass/fail line' % s.split('\n', 1)[0])
else:
    err('result.md missing')

# ---- no absolute or home paths in the written files
for f in (BRANCH, RESULT, Path(__file__)):
    if f.exists():
        t = f.read_text()
        for pat in (r'/Users/', r'/home/', r'(?<![A-Za-z0-9.])~/', r'[A-Za-z]:\\\\'):
            if re.search(pat, t.replace("r'/Users/'", '').replace("r'/home/'", '')) and f != Path(__file__):
                err('%s holds an absolute or home path (%s)' % (f.name, pat))

print('nodes %d (L1 %d, L2 %d, L3 %d); rows routed to ASSURANCE %d, attached %d, unattached %d, attached twice %d; '
      'routing objections %d' % (n_nodes, n_l1, n_l2, n_l3, len(routed), n_att, n_un, len(twice), n_obj))
if errors:
    for e in errors[:40]:
        print('  - ' + e)
    print('check_branch.py: FAIL (%d problem%s)' % (len(errors), '' if len(errors) == 1 else 's'))
    sys.exit(1)
print('check_branch.py: PASS')
