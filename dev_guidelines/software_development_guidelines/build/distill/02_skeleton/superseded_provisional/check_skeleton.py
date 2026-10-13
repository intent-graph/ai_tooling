#!/usr/bin/env python3
"""Check the skeleton against the claims ledger.

Proves, from the written files only:
  1. every ledger row is attached to exactly one node of skeleton.md (none twice, none missing, none unknown);
  2. the tree block and the node records agree (same uids, same rows);
  3. every uid follows the IntentGraph UID rules (ROOT; L1 keyword; L2 {parent}.{number} or {parent}.{KEYWORD};
     L3 and deeper {parent}.{number}), is unique and has an existing parent; names hold no forbidden characters;
  4. every context variable and every Realizes target resolves; awaiting-scope rows exist in the ledger;
  5. judge_plan.md puts every node in exactly one unit and its units own every ledger row once.
Prints the counts and one PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE.parent / '01_consolidate' / 'claims_ledger.md'
SKELETON = HERE / 'skeleton.md'
PLAN = HERE / 'judge_plan.md'

errors = []

def err(msg):
    errors.append(msg)

def expand(spec):
    out = []
    for tok in [t.strip() for t in spec.split(',') if t.strip()]:
        m = re.fullmatch(r'L(\d{3})-L(\d{3})', tok)
        if m:
            out += ['L%03d' % i for i in range(int(m.group(1)), int(m.group(2)) + 1)]
        elif re.fullmatch(r'L\d{3}', tok):
            out.append(tok)
        else:
            err('unreadable row token %r' % tok)
    return out

# ---- ledger
ledger = []
for line in LEDGER.read_text().splitlines():
    m = re.match(r'\| (L\d{3}) \|', line)
    if m:
        ledger.append(m.group(1))
if len(ledger) != len(set(ledger)):
    err('ledger has duplicate ids')
ledger_set = set(ledger)
pinned = re.search(r'Rows out: (\d+) ledger rows|Rows out: (\d+)', LEDGER.read_text())
if pinned and int(pinned.group(1) or pinned.group(2)) != len(ledger):
    err('ledger pins %s rows, found %d' % (pinned.group(1) or pinned.group(2), len(ledger)))

# ---- skeleton: node records
text = SKELETON.read_text()
records = {}
order = []
cur = None
for line in text.splitlines():
    m = re.match(r'#### (\S+) (.+)$', line)
    if m:
        cur = m.group(1)
        if cur in records:
            err('node record repeated: %s' % cur)
        records[cur] = dict(name=m.group(2), rows=None, ctx=None, real='', decides=None)
        order.append(cur)
        continue
    if cur is None:
        continue
    if line.startswith('Rows:'):
        body = line[5:].strip()
        records[cur]['rows'] = [] if body == '-' else expand(re.sub(r'\s*\(\d+\)\s*$', '', body))
    elif line.startswith('Context:'):
        records[cur]['ctx'] = line[8:].strip()
    elif line.startswith('Realizes:'):
        records[cur]['real'] = line[9:].strip()
    elif line.startswith('Decides:'):
        records[cur]['decides'] = line[8:].strip()

# ---- skeleton: tree block
tree = {}
m = re.search(r'## Tree\n\n```text\n(.*?)\n```', text, re.S)
if not m:
    err('tree block not found')
    tree_lines = []
else:
    tree_lines = m.group(1).splitlines()
for tl in tree_lines:
    mm = re.match(r'^( *)(\S+)  (.+)  \((.*)\)$', tl)
    if not mm:
        err('tree line unreadable: %r' % tl)
        continue
    uid, rowspec = mm.group(2), mm.group(4)
    tree[uid] = [] if rowspec == '-' else expand(rowspec)

if set(tree) != set(records):
    err('tree and node records differ in uids: %s' % sorted(set(tree) ^ set(records)))
for uid in set(tree) & set(records):
    if sorted(tree[uid]) != sorted(records[uid]['rows'] or []):
        err('tree and record differ in rows for %s' % uid)
    if records[uid]['rows'] is None:
        err('node without Rows line: %s' % uid)
    if not records[uid]['decides']:
        err('node without Decides line: %s' % uid)
    if records[uid]['ctx'] is None:
        err('node without Context line: %s' % uid)

# ---- 1. attachment
owner = {}
twice = 0
for uid, rec in records.items():
    for i in rec['rows'] or []:
        if i not in ledger_set:
            err('unknown ledger id %s on %s' % (i, uid))
        if i in owner:
            twice += 1
            err('row %s attached twice: %s and %s' % (i, owner[i], uid))
        owner[i] = uid
unattached = sorted(ledger_set - set(owner))
if unattached:
    err('unattached rows: %s' % ', '.join(unattached))
attached = len([i for i in owner if i in ledger_set])

# ---- 3. uid rules
L1_RE = re.compile(r'^[A-Z][A-Z0-9_]*$')
KEY_RE = re.compile(r'^[A-Z][A-Z0-9_]*$')
NUM_RE = re.compile(r'^[0-9]+$')
FORBIDDEN = set('/\\:*?"<>|[]#^')
levels = Counter()
for uid, rec in records.items():
    parts = uid.split('.')
    if uid == 'ROOT':
        levels[0] += 1
        continue
    if parts[0] == 'ROOT':
        err('uid must not start with ROOT.: %s' % uid)
    depth = len(parts)
    levels[depth] += 1
    if depth == 1:
        if not L1_RE.match(uid):
            err('bad L1 uid: %s' % uid)
    else:
        parent = '.'.join(parts[:-1])
        last = parts[-1]
        if parent not in records:
            err('parent of %s missing' % uid)
        if depth == 2:
            if not (NUM_RE.match(last) or KEY_RE.match(last)):
                err('bad L2 uid: %s' % uid)
        else:
            if not NUM_RE.match(last):
                err('L3+ uid must end in a number: %s' % uid)
    if any(c in FORBIDDEN for c in rec['name']):
        err('forbidden character in name of %s' % uid)
if 'ROOT' not in records:
    err('ROOT missing')

# ---- 4. context variables and links
vars_defined = set(re.findall(r'^\| ([A-Z_]+) \|', text, re.M)) - {'variable'}
for uid, rec in records.items():
    c = rec['ctx']
    if c and c not in ('-', 'see children'):
        for v in [x.strip() for x in c.split(',')]:
            if v not in vars_defined:
                err('unknown context variable %s on %s' % (v, uid))
    for r in [x.strip() for x in rec['real'].split(',') if x.strip()]:
        if r not in records:
            err('Realizes target %s of %s does not resolve' % (r, uid))
aw = re.search(r'## Awaiting scope\n(.*?)\n## Tree', text, re.S)
awaiting_ids = set()
if not aw:
    err('Awaiting scope section missing')
else:
    for i in re.findall(r'\bL\d{3}\b', aw.group(1)):
        awaiting_ids.add(i)
    for i in awaiting_ids:
        if i not in ledger_set:
            err('awaiting-scope id not in ledger: %s' % i)
        elif i not in owner:
            err('awaiting-scope id not attached: %s' % i)
# ids cited in positions exist
for i in set(re.findall(r'\bL\d{3}\b', text)):
    if i not in ledger_set:
        err('skeleton cites unknown ledger id %s' % i)

# ---- 5. judge plan
plan = PLAN.read_text()
unit_nodes = []
unit_rows = []
for line in plan.splitlines():
    m = re.match(r'Nodes \((\d+)\): (.+)$', line)
    if m:
        nodes = [x.strip() for x in m.group(2).split(',')]
        if len(nodes) != int(m.group(1)):
            err('unit node count mismatch: %s' % line[:60])
        unit_nodes += nodes
    m = re.match(r'Rows owned, read in full \((\d+)\): (.+)$', line)
    if m:
        rows = [] if m.group(2).strip() == '-' else expand(m.group(2))
        if len(rows) != int(m.group(1)):
            err('unit row count mismatch: %s' % line[:60])
        unit_rows += rows
cn = Counter(unit_nodes)
for uid in records:
    if cn[uid] != 1:
        err('node %s in %d judge-plan units' % (uid, cn[uid]))
for uid in cn:
    if uid not in records:
        err('judge-plan node %s not in skeleton' % uid)
cr = Counter(unit_rows)
for i in ledger_set:
    if cr[i] != 1:
        err('row %s owned by %d judge-plan units' % (i, cr[i]))

# ---- report
branch = Counter(uid.split('.')[0] for uid in records if uid != 'ROOT')
print('ledger rows: %d; attached: %d; unattached: %d; attached twice: %d' % (
    len(ledger_set), attached, len(unattached), twice))
print('nodes: %d (ROOT 1; %s)' % (len(records), '; '.join('%s %d' % (b, branch[b]) for b in
                                                           ['OWNERSHIP', 'ASSURANCE', 'CHANGE_FLOW', 'OPERATION', 'TRANSVERSE'])))
print('by level: L1 %d, L2 %d, L3 %d, deeper %d' % (levels[1], levels[2], levels[3], sum(v for k, v in levels.items() if k > 3)))
print('awaiting-scope ids: %d (all attached)' % len(awaiting_ids))
if errors:
    for e in errors[:40]:
        print('  - ' + e)
    print('FAIL: %d problem(s)' % len(errors))
    sys.exit(1)
print('PASS: all %d ledger rows attached exactly once, 0 unattached, uids follow the rules, tree and records agree, judge plan covers every node and row' % len(ledger_set))
