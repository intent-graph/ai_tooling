#!/usr/bin/env python3
"""Prove that part 3 of the claims ledger imports every principle sent by the JavaScript guideline.

Reads, next to this script: claims_ledger_part3.md and sources_part3.md; read-only, in the parent folder: part 1's
claims_ledger.md and sources.md; in the sibling JavaScript guideline: the sent package (Part A and Part B), its research
results and its source register. Checks:
  1. every sent node uid of the package (Part A: sent whole, Part B: general parts) is the `JS:` uid of exactly one
     ledger row, or is listed in "Not imported", exactly once and not both; the package outline lists the same set;
  2. no row names an unknown node uid; ledger ids are unique, sequential from L1501 and within L1501 to L1999;
     every row carries `origin: judged in the JavaScript guideline` and has ten columns;
  3. every claim id of the package's claim tables is in exactly one row (unless its node is not imported); every claim
     id in a row is defined in the JavaScript research results (slot by id prefix);
  4. every source cited by those claims resolves: it has a row in sources_part3.md (`JS-SRC-nnn`) or a reused part 1
     REG id, with the same url as the JavaScript register; every REG id cited by a row resolves in part 3 or part 1,
     and the row cites the REG of each source its claims cite; new REG ids lie in REG-1501 to REG-1999 and none is
     unused; reused ids exist in part 1;
  5. every `see also Lnnn` points to a row of part 1 or of part 3 that exists; none of the part 3 files holds an
     absolute or home path.
Prints counts and one final line PASS or FAIL. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PART1 = HERE.parent
JS = HERE.parents[4] / "javascript_guidelines"
PKG = JS / "build" / "handoff" / "to_software_guideline" / "package.md"
errors = []


def fail(msg):
    errors.append(msg)


def cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]


# ---- the package: nodes, claims, sources
pkg = PKG.read_text()
body, _, srcsec = pkg.partition("## Sources cited above")
a_start, b_start, rm = body.index("## Part A"), body.index("## Part B"), body.index("## Removed links")


def node_blocks(seg, level):
    parts = re.split(r"^" + level + r" (.+)$", seg, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]


nodes = {}
for part, seg, level in (("A", body[a_start:b_start], "####"), ("B", body[b_start:rm], "###")):
    for title, blk in node_blocks(seg, level):
        m = re.search(r"- Origin: (?:node|general part of node) `([^`]+)`", blk)
        if not m:
            fail(f"package block without origin uid: {title}")
            continue
        uid = m.group(1)
        if uid in nodes:
            fail(f"package node {uid} appears twice")
        claims = {}
        for line in blk.splitlines():
            if re.match(r"\| [A-Z0-9]+-C\d+ \|", line):
                c = cells(line)
                claims[c[0]] = sorted(set(re.findall(r"SRC-\d+", c[5])))
        nodes[uid] = dict(part=part, claims=claims)
n_a = sum(1 for n in nodes.values() if n["part"] == "A")
n_b = sum(1 for n in nodes.values() if n["part"] == "B")
m = re.search(r"SEND (\d+) nodes.*?SPLIT (\d+) nodes", pkg, re.S)
if m and (n_a, n_b) != (int(m.group(1)), int(m.group(2))):
    fail(f"package says SEND {m.group(1)} / SPLIT {m.group(2)} but Part A has {n_a} and Part B {n_b}")
outline = body[body.index("## Outline of what is sent"):a_start]
outline_sent = set(re.findall(r"- `([A-Z_.0-9]+)` [^\n]*\((?:sent|split)\)", outline))
if outline_sent != set(nodes):
    fail(f"outline sent/split nodes differ from Part A and B nodes: {sorted(outline_sent ^ set(nodes))}")
pkg_claims = {c: s for n in nodes.values() for c, s in n["claims"].items()}
pkg_src = {}
for line in srcsec.splitlines():
    m = re.match(r"\| (SRC-\d+) \| (T\d) \| (\S+) \| (.*?) \| (\S+) \| (.*) \|$", line)
    if m:
        pkg_src[m.group(1)] = m.group(5)

# ---- JavaScript research results and register
SLOT = {"LANG": "01_lang", "TYPES": "02_types", "ASYNC": "03_async", "STRUCT": "04_struct", "RUNSEC": "06_runsec",
        "SUPPLY": "07_supply", "QUALITY": "08_quality", "RUNTIME": "09_runtime", "SRVSEC": "13_srvsec",
        "SECGAP2": "14_secgap2"}
research_ok = (JS / "build" / "research").is_dir()
slot_text = {}


def claim_defined(cid):
    slot = SLOT.get(cid.split("-")[0])
    if slot is None:
        return False
    if slot not in slot_text:
        slot_text[slot] = (JS / "build" / "research" / slot / "result.md").read_text()
    return re.search(r"(?m)^\|? ?(?:- id: |\*\*|- \*\*)?" + re.escape(cid) + r"\b", slot_text[slot]) is not None


reg_js = {}
if (JS / "build" / "audit" / "source_register.md").is_file():
    for line in (JS / "build" / "audit" / "source_register.md").read_text().splitlines():
        m = re.match(r"\| (SRC-\d+) \| T\d \| \S+ \| .*? \| (\S+) \|", line)
        if m:
            reg_js[m.group(1)] = m.group(2)

# ---- part 1
p1_ledger = {cells(l)[0] for l in (PART1 / "claims_ledger.md").read_text().splitlines() if re.match(r"\| L\d+ \|", l)}
p1_reg = {cells(l)[0] for l in (PART1 / "sources.md").read_text().splitlines() if re.match(r"\| REG-\d+ \|", l)}

# ---- part 3 sources
src_text = (HERE / "sources_part3.md").read_text()
new_sec, _, reuse_sec = src_text.partition("## Reused from part 1")
new_reg, js_to_reg = {}, {}
for line in new_sec.splitlines():
    if re.match(r"\| REG-\d+ \|", line):
        c = cells(line)
        if len(c) != 8:
            fail(f"{c[0]}: {len(c)} columns instead of 8")
            continue
        rid = c[0]
        if rid in new_reg:
            fail(f"duplicate register id {rid}")
        if not (1501 <= int(rid[4:]) <= 1999):
            fail(f"{rid} outside REG-1501 to REG-1999")
        if rid in p1_reg:
            fail(f"{rid} collides with part 1")
        new_reg[rid] = c
        for tok in re.findall(r"JS-(SRC-\d+)", c[6]):
            if tok in js_to_reg:
                fail(f"{tok} has two register rows")
            js_to_reg[tok] = rid
            if reg_js and reg_js.get(tok) != c[4]:
                fail(f"{rid}: url differs from the JavaScript register for {tok}")
reused = {}
for line in reuse_sec.splitlines():
    if re.match(r"\| JS-SRC-\d+ \|", line):
        c = cells(line)
        tok = c[0][3:]
        reused[tok] = c[1]
        js_to_reg[tok] = c[1]
        if c[1] not in p1_reg:
            fail(f"reused {c[1]} does not exist in part 1")
        if reg_js and tok in reg_js and tok in pkg_src and pkg_src[tok] != reg_js[tok]:
            fail(f"{tok}: package and register urls differ")

# ---- part 3 ledger
text = (HERE / "claims_ledger_part3.md").read_text()
led_part, _, ni_part = text.partition("## Not imported")
ledger = {}
for line in led_part.splitlines():
    if not re.match(r"\| L\d+ \|", line):
        continue
    c = cells(line)
    if len(c) != 10:
        fail(f"{c[0]}: {len(c)} columns instead of 10")
        continue
    lid = c[0]
    if lid in ledger:
        fail(f"duplicate ledger id {lid}")
    if not (1501 <= int(lid[1:]) <= 1999):
        fail(f"{lid} outside L1501 to L1999")
    if "origin: judged in the JavaScript guideline" not in c[7]:
        fail(f"{lid}: origin marker missing")
    toks = [t.strip() for t in c[2].split(",")]
    ledger[lid] = dict(
        nodes=[t[3:] for t in toks if t.startswith("JS:")],
        claims=[t for t in toks if not t.startswith("JS:")],
        pos=c[7],
        regs=[x.strip() for x in c[9].split(",") if x.strip() and x.strip() != "-"],
    )
ids = sorted(ledger)
if ids != [f"L{n}" for n in range(1501, 1501 + len(ids))]:
    fail("ledger ids are not sequential from L1501")
not_imported = re.findall(r"(?m)^\| JS:([A-Z_.0-9]+) \|", ni_part)

# 1. nodes
seen = {}
for lid, r in ledger.items():
    if len(r["nodes"]) != 1:
        fail(f"{lid}: {len(r['nodes'])} node uids in merges")
    for u in r["nodes"]:
        seen.setdefault(u, []).append(lid)
unknown = [u for u in seen if u not in nodes]
for u in unknown:
    fail(f"row names unknown node uid {u}")
for u in nodes:
    in_rows = len(seen.get(u, []))
    in_ni = not_imported.count(u)
    if in_rows + in_ni != 1:
        fail(f"node {u}: {in_rows} row(s) and {in_ni} not-imported entry(ies); expected exactly one in total")
for u in not_imported:
    if u not in nodes:
        fail(f"not-imported entry names unknown node {u}")

# 3. claims
claim_rows = {}
for lid, r in ledger.items():
    for cid in r["claims"]:
        claim_rows.setdefault(cid, []).append(lid)
multi = [c for c, v in claim_rows.items() if len(v) != 1]
for c in multi:
    fail(f"claim {c} appears in {len(claim_rows[c])} rows")
ni_set = set(not_imported)
node_of_claim = {c: u for u, n in nodes.items() for c in n["claims"]}
dropped = [c for c in pkg_claims if c not in claim_rows and node_of_claim[c] not in ni_set]
for c in dropped:
    fail(f"claim {c} of the package is in no row")
extra = [c for c in claim_rows if c not in pkg_claims]
undefined = []
if research_ok:
    undefined = [c for c in claim_rows if not claim_defined(c)]
    for c in undefined:
        fail(f"claim {c} is not defined in the JavaScript research results")
for c, lids in claim_rows.items():
    if c in node_of_claim and node_of_claim[c] not in ledger[lids[0]]["nodes"]:
        fail(f"claim {c} sits in {lids[0]} but belongs to node {node_of_claim[c]}")

# 4. sources
cited_new = set()
n_checked = 0
for lid, r in ledger.items():
    for rid in r["regs"]:
        if rid in new_reg:
            cited_new.add(rid)
        elif rid not in p1_reg:
            fail(f"{lid}: cited source {rid} does not resolve in part 3 or part 1")
    need = set()
    for cid in r["claims"]:
        for s in pkg_claims.get(cid, []):
            need.add(s)
    for s in need:
        n_checked += 1
        reg = js_to_reg.get(s)
        if reg is None:
            fail(f"{lid}: JavaScript source {s} has no register row in part 3 and is not reused from part 1")
        elif reg not in r["regs"]:
            fail(f"{lid}: source {s} ({reg}) missing from the sources of the row")
for rid in new_reg:
    if rid not in cited_new:
        fail(f"{rid} is in sources_part3.md but no row cites it")
for tok in pkg_src:
    if tok not in js_to_reg:
        fail(f"package source {tok} resolves to no register row")
    elif reg_js and tok not in reg_js:
        fail(f"package source {tok} is not in the JavaScript source register")

# 5. see also, paths
n_see = 0
for lid, r in ledger.items():
    for tgt in re.findall(r"see also (L\d+)", r["pos"]):
        n_see += 1
        if tgt not in p1_ledger:
            fail(f"{lid}: see also {tgt} is not a part 1 row")
    for tgt in re.findall(r"\b(L15\d\d)\b", r["pos"]):
        if tgt not in ledger:
            fail(f"{lid}: link to {tgt} does not exist in part 3")
for f in ("claims_ledger_part3.md", "sources_part3.md", "result.md", "check_part3.py"):
    p = HERE / f
    if p.is_file() and re.search("/Us" + "ers/|/ho" + "me/|[A-Z]:" + r"\\", p.read_text()):
        fail(f"{f} holds an absolute or home path")

n_rows = sum(len(v) for v in seen.values())
print(f"package nodes: {len(nodes)} (Part A {n_a}, Part B {n_b}); rows: {len(ledger)}; not imported: {len(not_imported)}")
print(f"nodes in a row: {len(set(seen) & set(nodes))}; unknown node uids: {len(unknown)}")
print(f"claims in package tables: {len(pkg_claims)}; claim ids in rows: {len(claim_rows)} ({len(extra)} named by the origin, not in a package table); in more than one row: {len(multi)}; dropped: {len(dropped)}; undefined in research results: {len(undefined)}")
print(f"sources: {len(new_reg)} new, {len(reused)} reused from part 1; package sources resolved: {len(pkg_src)}; claim-source citations checked: {n_checked}")
print(f"see also references to part 1: {n_see}")
for e in errors[:40]:
    print("  error:", e)
if errors:
    print(f"FAIL: {len(errors)} error(s)")
    sys.exit(1)
print("PASS: every sent node of the package (Part A and Part B) is a row or listed as not imported exactly once, every claim is in one row, every cited source resolves")
