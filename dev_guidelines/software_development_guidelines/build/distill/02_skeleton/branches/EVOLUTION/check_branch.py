#!/usr/bin/env python3
"""Check the EVOLUTION branch against routing.md, tree_l2.md and the ledgers.

Proves, from the written files only:
  1. every row routed to an EVOLUTION node in routing.md is attached to exactly one EVOLUTION node of
     branch.md (none missing, none twice, none foreign, none unknown to the ledgers);
  2. the tree block and the node records agree (same uids); the L1 and L2 uids and names match tree_l2.md;
  3. every uid follows the IntentGraph UID rules (L1 keyword, L2 {L1}.{KEYWORD}, L3 {L2}.{number});
     uids are unique, parents exist, names hold no forbidden characters; L3 nodes carry rows and positions,
     L2 nodes are roll-ups with `Rows: -`;
  4. every link target exists in tree_l2.md or in the branch; routing objections name an existing node and
     a row of the branch;
  5. every MAINT row of the branch (source REG-181) appears as a named maintainer position on its node;
     every row attached to a node is cited in that node's record.
Prints the counts and one PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKEL = HERE.parent.parent            # 02_skeleton
DISTILL = SKEL.parent
BRANCH = 'EVOLUTION'
LEDGERS = [DISTILL / '01_consolidate' / 'claims_ledger.md',
           DISTILL / '01_consolidate' / 'part2' / 'claims_ledger_part2.md',
           DISTILL / '01_consolidate' / 'part3' / 'claims_ledger_part3.md']
errors = []


def err(m):
    errors.append(m)


def expand(spec):
    out = []
    for tok in [t.strip() for t in spec.split(',') if t.strip()]:
        m = re.fullmatch(r'L(\d+)-L(\d+)', tok)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            w = len(m.group(1))
            out += ['L%0*d' % (w, i) for i in range(a, b + 1)]
        elif re.fullmatch(r'L\d+', tok):
            out.append(tok)
        else:
            err('unreadable row token %r' % tok)
    return out


# ---- ledgers
ledger = {}
for f in LEDGERS:
    for line in f.read_text().splitlines():
        m = re.match(r'\| (L\d+) \|', line)
        if m:
            if m.group(1) in ledger:
                err('duplicate ledger id %s' % m.group(1))
            ledger[m.group(1)] = line
maint = {i for i, l in ledger.items() if 'REG-181' in l.split('|')[-2] or 'MAINT-S01' in l}

# ---- routing: rows routed to this branch
routed = {}
for line in (SKEL / 'routing.md').read_text().splitlines():
    m = re.match(r'(L\d+) (\S+)', line)
    if m and m.group(2).split('.')[0] == BRANCH:
        routed[m.group(1)] = m.group(2)

# ---- tree_l2
l2_text = (SKEL / 'tree_l2.md').read_text()
l2_nodes = {}
for line in l2_text.splitlines():
    m = re.match(r'\| `([A-Z][A-Z0-9_.]*)` \| ([^|]+) \| ', line)
    if m:
        l2_nodes[m.group(1)] = m.group(2).strip()
l2_rows = {}
for line in l2_text.splitlines():
    m = re.match(r'\| `([A-Z][A-Z0-9_.]*)` \|.*\| (\d+) \|', line)
    if m:
        l2_rows[m.group(1)] = int(m.group(2))

# ---- branch.md
text = (HERE / 'branch.md').read_text()
records, order = {}, []
cur = None
for line in text.splitlines():
    m = re.match(r'#### (\S+) (.+)$', line)
    if m:
        cur = m.group(1)
        if cur in records:
            err('node record repeated: %s' % cur)
        records[cur] = dict(name=m.group(2), rows=None, links='', body=[], intent=None, pos=0)
        order.append(cur)
        continue
    if line.startswith('## '):
        cur = None
    if cur is None:
        continue
    r = records[cur]
    r['body'].append(line)
    if line.startswith('Rows:'):
        b = line[5:].strip()
        r['rows'] = [] if b == '-' else expand(b)
    elif line.startswith('Intent:'):
        r['intent'] = line[7:].strip()
    elif line.startswith('Links:'):
        r['links'] = line[6:].strip()
    elif re.match(r'- P\d ', line):
        r['pos'] += 1

tm = re.search(r'## Tree\n\n```text\n(.*?)\n```', text, re.S)
tree = []
if not tm:
    err('tree block not found')
else:
    for tl in tm.group(1).splitlines():
        mm = re.match(r'^( *)(\S+)  (.+)$', tl)
        if not mm:
            err('tree line unreadable: %r' % tl)
            continue
        tree.append((mm.group(2), mm.group(3)))
if sorted(u for u, _ in tree) != sorted(records):
    err('tree and records differ: %s' % sorted(set(u for u, _ in tree) ^ set(records)))
for u, n in tree:
    if u in records and records[u]['name'] != n:
        err('name differs between tree and record for %s' % u)

# ---- 2/3. L1, L2 against tree_l2, uid rules
KEY = re.compile(r'^[A-Z][A-Z0-9_]*$')
NUM = re.compile(r'^[0-9]+$')
FORBIDDEN = set('/\\:*?"<>|[]#^')
levels = Counter()
for uid, r in records.items():
    parts = uid.split('.')
    if parts[0] != BRANCH:
        err('node outside branch: %s' % uid)
    depth = len(parts)
    levels[depth] += 1
    if depth == 1:
        if not KEY.match(uid):
            err('bad L1 uid %s' % uid)
    else:
        parent = '.'.join(parts[:-1])
        if parent not in records:
            err('parent of %s missing' % uid)
        if depth == 2 and not KEY.match(parts[-1]):
            err('bad L2 uid %s' % uid)
        if depth >= 3 and not NUM.match(parts[-1]):
            err('L3+ uid must end in a number: %s' % uid)
    if depth <= 2:
        if uid not in l2_nodes:
            err('%s not in tree_l2.md' % uid)
        elif l2_nodes[uid] != r['name']:
            err('name of %s differs from tree_l2.md' % uid)
    if any(c in FORBIDDEN for c in r['name']):
        err('forbidden character in name of %s' % uid)
    if not r['intent']:
        err('node without Intent: %s' % uid)
    if r['rows'] is None:
        err('node without Rows: %s' % uid)
l2_expected = {u for u in l2_nodes if u.split('.')[0] == BRANCH}
if l2_expected != {u for u in records if len(u.split('.')) <= 2}:
    err('L1/L2 set differs from tree_l2.md: %s' % sorted(l2_expected ^ {u for u in records if len(u.split('.')) <= 2}))
children = Counter('.'.join(u.split('.')[:-1]) for u in records if u != BRANCH)
for uid, r in records.items():
    depth = len(uid.split('.'))
    if depth == 3:
        if not r['rows']:
            err('L3 node without rows: %s' % uid)
        if r['pos'] == 0:
            err('L3 node without positions: %s' % uid)
    else:
        if r['rows'] not in ([], None):
            err('L1/L2 node must be a roll-up (Rows: -): %s' % uid)
    if depth == 2 and children[uid] == 1:
        err('L2 node with a single child: %s' % uid)

# ---- 1. attachment
owner = {}
twice = 0
for uid, r in records.items():
    for i in r['rows'] or []:
        if i not in ledger:
            err('unknown ledger id %s on %s' % (i, uid))
        if i in owner:
            twice += 1
            err('row %s attached twice: %s and %s' % (i, owner[i], uid))
        owner[i] = uid
unattached = sorted(set(routed) - set(owner))
foreign = sorted(set(owner) - set(routed))
if unattached:
    err('unattached routed rows: %s' % ', '.join(unattached))
if foreign:
    err('attached rows not routed to this branch: %s' % ', '.join(foreign))
for i, node in owner.items():
    if i in routed and not routed[i].startswith(node.split('.')[0] + '.' + node.split('.')[1]):
        err('row %s attached under %s but routed to %s' % (i, node, routed[i]))
# counts per L2 against tree_l2
per_l2 = Counter('.'.join(n.split('.')[:2]) for n in owner.values())
for u in l2_expected:
    if len(u.split('.')) == 2 and per_l2[u] != l2_rows.get(u):
        err('row count of %s is %d, tree_l2.md says %s' % (u, per_l2[u], l2_rows.get(u)))
if len(routed) != l2_rows.get(BRANCH):
    err('routed rows %d, tree_l2.md says %s for %s' % (len(routed), l2_rows.get(BRANCH), BRANCH))

# ---- 4. links and objections
LINK = re.compile(r'(Realizes|Requires|Conflicts|Refines|See) ([A-Z][A-Z0-9_]*(?:\.[A-Z0-9_]+)*)')
valid = set(l2_nodes) | set(records)
nlinks = 0
for uid, r in records.items():
    for t, tgt in LINK.findall(r['links']):
        nlinks += 1
        if tgt not in valid:
            err('link target %s of %s does not exist' % (tgt, uid))
    if r['links'] and not LINK.search(r['links']):
        err('unreadable Links line on %s' % uid)
om = re.search(r'## Routing objections\n(.*?)\n## Records', text, re.S)
objections = []
if not om:
    err('Routing objections section missing')
else:
    for line in om.group(1).splitlines():
        m = re.match(r'- (L\d+) -> (\S+) :', line)
        if m:
            objections.append(m.groups())
            if m.group(1) not in routed:
                err('objection row %s is not a row of this branch' % m.group(1))
            if m.group(2) not in l2_nodes:
                err('objection target %s not in tree_l2.md' % m.group(2))
            elif m.group(2).split('.')[0] == BRANCH:
                err('objection target %s is inside the branch' % m.group(2))

# ---- 5. MAINT rows named, every attached row cited in its record
for i in sorted(maint & set(routed)):
    node = owner.get(i)
    if not node or 'Maintainer' not in '\n'.join(records[node]['body']):
        err('MAINT row %s lacks a named maintainer position on %s' % (i, node))
for i, node in owner.items():
    if not re.search(r'\b%s\b' % i, '\n'.join(records[node]['body'][1:])):
        # Rows line itself names it; require a citation beyond it
        cites = sum(len(re.findall(r'\b%s\b' % i, l)) for l in records[node]['body'] if not l.startswith('Rows:'))
        if cites == 0:
            err('row %s not cited in positions of %s' % (i, node))

# ---- report
print('rows routed to %s: %d; attached: %d; unattached: %d; attached twice: %d; foreign: %d' % (
    BRANCH, len(routed), len(set(owner) & set(routed)), len(unattached), twice, len(foreign)))
print('nodes: %d (L1 %d, L2 %d, L3 %d)' % (len(records), levels[1], levels[2], levels[3]))
print('MAINT rows in branch: %d (%s); links: %d; routing objections: %d' % (
    len(maint & set(routed)), ', '.join(sorted(maint & set(routed))), nlinks, len(objections)))
if errors:
    for e in errors[:40]:
        print('  - ' + e)
    print('FAIL: %d problem(s)' % len(errors))
    sys.exit(1)
print('PASS: all %d routed rows attached exactly once, 0 unattached, uids follow the rules, every link target exists, MAINT rows named' % len(routed))
