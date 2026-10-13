#!/usr/bin/env python3
"""Prove that the claims ledger and the source register lose nothing.

Reads the 10 claim-bearing research results (build/research/<slot>/result.md, L3 sections),
claims_ledger.md and sources.md next to this script. Checks:
  1. every original claim id appears exactly once in the `merges` column of the ledger;
  2. no ledger row names an unknown claim id; ledger ids are unique and sequential;
  3. dropped = 0 (original id missing) and unplaced = 0 (origin area missing from the row's areas);
  4. every original source id appears in exactly one row of sources.md, with the highest origin tier;
  5. every source id cited by an original claim resolves in its register, and its distinct source
     is cited by the ledger row that holds the claim; every source id cited by the ledger resolves.
Prints counts and one final line PASS or FAIL. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent / "research"
SLOTS = {
    "01_sourcing": "SRC", "02_adoption": "ADOPT", "03_verification": "VERIFY",
    "04_delivery": "DELIVER", "05_operation": "OPERATE", "06_transverse": "TRANS",
    "07_maintainer_doctrine": "MAINT", "09_external_services": "EXT",
    "10_data_change": "DATA", "11_performance_readiness": "PERF",
}
CLAIM_START = re.compile(r"^(?:[-*] id: |\*\*|- \*\*)?([A-Z]+-C\d+[a-z]?)\b")
TOKEN = re.compile(r"(?<![A-Za-z0-9-])((?:[A-Z]+-)?S\d+)(?![A-Za-z0-9])")
errors = []


def fail(msg):
    errors.append(msg)


def l3_text(slot):
    text = (RESEARCH / slot / "result.md").read_text()
    return text[text.index("\n## L3"):]


def read_claims(slot):
    """Return {claim id: block text} from the Claims section of the L3."""
    text = l3_text(slot)
    start = text.index("### Claims")
    end = text.find("\n### Gaps", start)
    section = text[start:end if end > 0 else len(text)].splitlines()
    out, cur = {}, None
    for line in section:
        m = CLAIM_START.match(line)
        if m:
            cur = m.group(1)
            if cur in out:
                fail(f"duplicate original claim id {cur}")
            out[cur] = [line]
        elif cur is not None:
            if line.startswith("#"):
                cur = None
            else:
                out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def read_register(slot):
    """Return {source id: tier} from the L3 source register (table rows or bullets)."""
    tiers = {}
    for line in l3_text(slot).splitlines():
        m = re.match(r"\| ([A-Z]+-S\d+) \| (T\d)", line)
        if m:
            tiers[m.group(1)] = m.group(2)
            continue
        m = re.match(r"- ([A-Z]+-S\d+)(?:,| \()\s*(T\d)?", line)
        if m:
            tiers[m.group(1)] = m.group(2) or "maintainer"
    return tiers


def cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]


# ---- originals
orig_claims, orig_tiers = {}, {}
for slot, code in SLOTS.items():
    for cid, block in read_claims(slot).items():
        orig_claims[cid] = (code, block)
    orig_tiers.update(read_register(slot))
rank = {"T1": 1, "T2": 2, "T3": 3, "T4": 4, "maintainer": 9}

# ---- sources.md
reg_rows = {}
replaced_by = {}
for line in (HERE / "sources.md").read_text().splitlines():
    if not re.match(r"\| REG-\d+ \|", line):
        continue
    c = cells(line)
    rid, tier, replaces = c[0], c[1], [x.strip() for x in c[6].split(",")]
    if rid in reg_rows:
        fail(f"duplicate register id {rid}")
    reg_rows[rid] = (tier, replaces)
    for sid in replaces:
        if sid in replaced_by:
            fail(f"source id {sid} replaced twice ({replaced_by[sid]}, {rid})")
        replaced_by[sid] = rid
for sid in orig_tiers:
    if sid not in replaced_by:
        fail(f"original source id {sid} not in sources.md")
for sid in replaced_by:
    if sid not in orig_tiers:
        fail(f"sources.md names unknown original source id {sid}")
for rid, (tier, replaces) in reg_rows.items():
    best = min((orig_tiers[s] for s in replaces if s in orig_tiers), key=lambda t: rank[t], default=None)
    if best is not None and best != tier:
        fail(f"{rid}: tier {tier} is not the highest origin tier {best}")

# ---- ledger
ledger = {}
seen = {}
for line in (HERE / "claims_ledger.md").read_text().splitlines():
    if not re.match(r"\| L\d+ \|", line):
        continue
    c = cells(line)
    if len(c) != 10:
        fail(f"{c[0]}: {len(c)} columns instead of 10")
        continue
    lid, merges, areas, srcs = c[0], [x.strip() for x in c[2].split(",")], c[3], c[9]
    if lid in ledger:
        fail(f"duplicate ledger id {lid}")
    ledger[lid] = (merges, areas, srcs)
    for cid in merges:
        seen.setdefault(cid, []).append(lid)
ids = sorted(ledger)
if ids != [f"L{n:03d}" for n in range(1, len(ids) + 1)]:
    fail("ledger ids are not sequential from L001")

multi = [c for c, v in seen.items() if len(v) != 1]
unknown = [c for c in seen if c not in orig_claims]
dropped = [c for c in orig_claims if c not in seen]
unplaced = []
for lid, (merges, areas, _) in ledger.items():
    for cid in merges:
        if cid in orig_claims and not re.search(r"\b" + orig_claims[cid][0] + r"\b", areas):
            unplaced.append(cid)
for c in multi:
    fail(f"claim {c} appears in {len(seen[c])} rows")
for c in unknown:
    fail(f"ledger names unknown claim id {c}")
for c in dropped:
    fail(f"claim {c} dropped")
for c in unplaced:
    fail(f"claim {c} placed in a row without its origin area")

# ---- citations
cited_orig = 0
cited_ledger = set()
for lid, (merges, areas, srcs) in ledger.items():
    row_regs = {s.strip() for s in srcs.split(",") if s.strip() and s.strip() != "-"}
    cited_ledger |= row_regs
    for r in row_regs:
        if r not in reg_rows:
            fail(f"{lid}: cited source {r} does not resolve in sources.md")
    for cid in merges:
        if cid not in orig_claims:
            continue
        code, block = orig_claims[cid]
        for m in TOKEN.finditer(block):
            sid = m.group(1) if "-" in m.group(1) else f"{code}-{m.group(1)}"
            cited_orig += 1
            if sid not in orig_tiers:
                fail(f"{cid}: cited source {sid} does not resolve in its register")
            elif replaced_by.get(sid) not in row_regs:
                fail(f"{cid}: source {sid} ({replaced_by.get(sid)}) missing from the sources of {lid}")

merged_rows = [l for l, (m, _, _) in ledger.items() if len(m) > 1]
print(f"claims in: {len(orig_claims)} from {len(SLOTS)} results")
print(f"rows out: {len(ledger)}; merged rows: {len(merged_rows)} merging {sum(len(ledger[l][0]) for l in merged_rows)} originals")
print(f"dropped: {len(dropped)}; unplaced: {len(unplaced)}; claims in more than one row: {len(multi)}; unknown ids: {len(unknown)}")
print(f"sources: {len(orig_tiers)} original ids -> {len(reg_rows)} distinct; citations checked in origin claims: {cited_orig}; distinct sources cited by the ledger: {len(cited_ledger)}")
for e in errors[:40]:
    print("  error:", e)
if errors:
    print(f"FAIL: {len(errors)} error(s)")
    sys.exit(1)
print("PASS: every original claim id appears exactly once, none dropped, none unplaced, every cited source resolves")
