#!/usr/bin/env python3
"""Check the level-2 cut: tree_l2.md and routing.md against the three parts of the claims ledger.

Proves, from the written files only:
  1. the ledger holds 814 rows (L001-L460, L1001-L1289, L1501-L1565), each id once;
  2. routing.md has one line per ledger row: every row routed exactly once, none missing, none unknown;
  3. every routed uid is an existing L2 node of tree_l2.md;
  4. uids follow the IntentGraph UID rules: ROOT exactly; seven L1 uids matching ^[A-Z][A-Z0-9_]*$;
     L2 uids {L1}.{KEYWORD} with an existing L1 parent; unique; names hold none of /\\:*?"<>|[]#^;
  5. the rows column of tree_l2.md equals the count recomputed from routing.md, every L2 node holds at least
     one row, and every L1 count is the sum of its L2 counts;
  6. the written files hold no absolute or home path.
Prints the counts and one PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DISTILL = HERE.parent
LEDGERS = [DISTILL / '01_consolidate' / 'claims_ledger.md',
           DISTILL / '01_consolidate' / 'part2' / 'claims_ledger_part2.md',
           DISTILL / '01_consolidate' / 'part3' / 'claims_ledger_part3.md']
TREE = HERE / 'tree_l2.md'
ROUTING = HERE / 'routing.md'
EXPECTED_L1 = ['OWNERSHIP', 'ASSURANCE', 'CONSTRUCTION', 'CHANGE_FLOW', 'OPERATION', 'EVOLUTION', 'TRANSVERSE']

errors = []


def err(msg):
    errors.append(msg)


# ---- 1. ledger
ledger = []
per_part = []
for f in LEDGERS:
    ids = [m.group(1) for l in f.read_text().splitlines() for m in [re.match(r'\| (L\d+) \|', l)] if m]
    per_part.append(len(ids))
    ledger += ids
if len(ledger) != len(set(ledger)):
    err('ledger ids repeat')
expected = ['L%03d' % i for i in range(1, 461)] + ['L%d' % i for i in range(1001, 1290)] + ['L%d' % i for i in range(1501, 1566)]
if sorted(ledger) != sorted(expected):
    err('ledger ids differ from L001-L460, L1001-L1289, L1501-L1565: missing %s, extra %s' % (
        sorted(set(expected) - set(ledger))[:5], sorted(set(ledger) - set(expected))[:5]))
if len(ledger) != 814:
    err('ledger holds %d rows, expected 814' % len(ledger))
ledger_set = set(ledger)

# ---- tree
root = None
l1 = []
l2 = {}
rows_col = {}
names = {}
section_l1 = None
for line in TREE.read_text().splitlines():
    m = re.match(r'\| `([^`]+)` \| (.+?) \| (.+?) \| (\d+|-) \|', line)
    if not m:
        continue
    uid, name, rows = m.group(1), m.group(2), m.group(4)
    names[uid] = name
    rows_col[uid] = None if rows == '-' else int(rows)
    if uid == 'ROOT':
        root = uid
    elif '.' not in uid:
        l1.append(uid)
    else:
        l2[uid] = uid.split('.')[0]

# ---- 4. uid rules
KEY = re.compile(r'^[A-Z][A-Z0-9_]*$')
FORBIDDEN = set('/\\:*?"<>|[]#^')
if root != 'ROOT':
    err('ROOT node missing or not exactly ROOT')
if l1 != EXPECTED_L1:
    err('L1 nodes are %s, expected %s' % (l1, EXPECTED_L1))
for u in l1:
    if not KEY.match(u):
        err('bad L1 uid %s' % u)
for u, parent in l2.items():
    parts = u.split('.')
    if len(parts) != 2:
        err('L2 uid with wrong depth: %s' % u)
    elif parent not in l1:
        err('L2 uid with unknown parent: %s' % u)
    elif not KEY.match(parts[1]):
        err('bad L2 keyword: %s' % u)
all_uids = ['ROOT'] + l1 + list(l2)
if len(all_uids) != len(set(all_uids)):
    err('uids repeat')
for u, n in names.items():
    if set(n) & FORBIDDEN:
        err('forbidden character in name of %s' % u)

# ---- 2, 3. routing
routing = {}
repeats = []
unreadable = 0
in_block = False
for line in ROUTING.read_text().splitlines():
    if line.strip() == '```text':
        in_block = True
        continue
    if line.strip() == '```':
        in_block = False
        continue
    if not in_block:
        continue
    m = re.match(r'^(L\d+) ([A-Z][A-Z0-9_.]*)( \| .+)?$', line)
    if not m:
        unreadable += 1
        err('unreadable routing line: %r' % line)
        continue
    rid, uid = m.group(1), m.group(2)
    if rid in routing:
        repeats.append(rid)
        err('row %s routed twice' % rid)
    routing[rid] = uid
unknown = sorted(set(routing) - ledger_set)
unrouted = sorted(ledger_set - set(routing))
for r in unknown:
    err('routed row not in ledger: %s' % r)
for r in unrouted:
    err('unrouted ledger row: %s' % r)
for rid, uid in routing.items():
    if uid not in l2:
        err('row %s routed to non-existing L2 uid %s' % (rid, uid))

# ---- 5. counts
counts = Counter(routing.values())
for u in l2:
    if counts[u] == 0:
        err('L2 node with no row: %s' % u)
    if rows_col.get(u) != counts[u]:
        err('rows column of %s is %s, routing gives %d' % (u, rows_col.get(u), counts[u]))
by_l1 = Counter()
for u, n in counts.items():
    by_l1[u.split('.')[0]] += n
for u in l1:
    if rows_col.get(u) != by_l1[u]:
        err('rows column of %s is %s, routing gives %d' % (u, rows_col.get(u), by_l1[u]))

# ---- 6. no paths
for f in (TREE, ROUTING):
    txt = f.read_text()
    if re.search(r'/Us' + r'ers/|/ho' + r'me/|~/', txt):
        err('absolute or home path in %s' % f.name)

print('ledger rows: %d (part 1 %d, part 2 %d, part 3 %d)' % ((len(ledger),) + tuple(per_part)))
print('routed: %d; unrouted: %d; routed twice: %d; unknown ids: %d' % (len(routing), len(unrouted), len(repeats), len(unknown)))
print('nodes: ROOT 1, L1 %d, L2 %d (total %d)' % (len(l1), len(l2), len(all_uids)))
for u in l1:
    print('  %-12s L2 nodes %2d, rows %3d' % (u, sum(1 for x in l2 if x.startswith(u + '.')), by_l1[u]))
if errors:
    for e in errors[:40]:
        print('error:', e)
    print('FAIL: %d problem(s)' % len(errors))
    sys.exit(1)
print('PASS: all %d ledger rows routed exactly once to an existing L2 uid, %d unrouted, uids follow the rules, counts agree with tree_l2.md' % (len(routing), len(unrouted)))
