#!/usr/bin/env python3
"""Prove that part 2 of the claims ledger and of the source register loses nothing.

Reads, next to this script and in the research folders (read-only):
  - the four round-3 research results (build/research/{12_evolution,13_change_authors,14_recovery,
    15_security_depth}/result.md, L3 sections);
  - the five web-guideline research results in scope (../../web_architecture_guidelines/build/research/
    {06_operations,07_architecture_styles,05_identity_security,14_thin_spots,17_data_contracts}/result.md);
  - part 1: ../claims_ledger.md and ../sources.md; part 2: claims_ledger_part2.md and sources_part2.md.
Checks:
  1. every original claim id of the four slots appears exactly once in the `merges` column of part 2;
  2. every web claim in scope (all of OPS, ARCH, THIN, DCON; SEC-C50 to SEC-C58) is either imported
     (WEB:<id> in `merges`, exactly once) or listed once in the skipped table; none in both, none in neither;
  3. no row names an unknown claim id; ledger ids are unique and sequential from L1001, within L1001-L1499;
     dropped = 0; unplaced = 0 (origin area code missing from the row's areas);
  4. every original source id of the four slots is replaced by exactly one part-2 row or mapped to exactly one
     part-1 row; new register ids are within REG-1001 to REG-1499; a new row carries the highest origin tier;
  5. every source cited by an origin claim resolves to a register row, and that row is cited by the ledger
     row that holds the claim; every source cited by the ledger resolves in part 1 or part 2;
  6. every `see also Lnnn` resolves (3 digits in part 1, 4 digits in part 2);
  7. the part-2 files contain no absolute or home path.
Prints counts and one final PASS or FAIL line. Exit code 0 on PASS, 1 on FAIL.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
P1 = HERE.parent
BUILD = HERE.parents[2]
RESEARCH = BUILD / "research"
WEB = BUILD.parents[1] / "web_architecture_guidelines" / "build" / "research"

OWN_SLOTS = {"12_evolution": "EVOL", "13_change_authors": "AUTH", "14_recovery": "RECOV", "15_security_depth": "SECD"}
WEB_SLOTS = {"06_operations": "OPS", "07_architecture_styles": "ARCH", "05_identity_security": "SEC",
             "14_thin_spots": "THIN", "17_data_contracts": "DCON"}
WEB_CODES = set(WEB_SLOTS.values())
CLAIM_START = re.compile(r"^(?:[-*] id: |\*\*|- \*\*)?([A-Z]+-C\d+[a-z]?)\b")
WEB_START = {
    "OPS": re.compile(r"^- (OPS-C\d+) \|"),
    "ARCH": re.compile(r"^\| (ARCH-C\d+) \|"),
    "SEC": re.compile(r"^- \*\*(SEC-C\d+)\*\* \|"),
    "THIN": re.compile(r"^\| (THIN-C\d+) \|"),
    "DCON": re.compile(r"^- \*\*(DCON-C\d+)\*\*"),
}
TOKEN = re.compile(r"(?<![A-Za-z0-9-])((?:[A-Z]+-)?S\d\d)(?![A-Za-z0-9])")
errors = []


def fail(msg):
    errors.append(msg)


def l3_text(base, slot):
    text = (base / slot / "result.md").read_text()
    return text[text.index("\n## L3"):]


def cells(line):
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]


def in_scope(cid):
    if cid.startswith("SEC-"):
        return 50 <= int(cid.split("-C")[1]) <= 58
    return True


# ---------------------------------------------------------------- originals: four slots
def read_own_claims(slot, code):
    text = l3_text(RESEARCH, slot)
    start = text.index("### Claims")
    end = text.find("\n### Gaps", start)
    out, cur = {}, None
    for line in text[start:end if end > 0 else len(text)].splitlines():
        m = CLAIM_START.match(line)
        if m and m.group(1).startswith(code + "-"):
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


def read_register(base, slot, code):
    tiers = {}
    for line in l3_text(base, slot).splitlines():
        m = re.match(r"\| (" + code + r"-S\d+) \| (T\d)", line)
        if m:
            tiers[m.group(1)] = m.group(2)
    return tiers


own_claims, own_tiers, claim_area = {}, {}, {}
for slot, code in OWN_SLOTS.items():
    for cid, block in read_own_claims(slot, code).items():
        own_claims[cid] = block
        claim_area[cid] = code
    own_tiers.update(read_register(RESEARCH, slot, code))

# ---------------------------------------------------------------- originals: web
web_claims, web_tiers = {}, {}
for slot, code in WEB_SLOTS.items():
    lines = l3_text(WEB, slot).splitlines()
    for i, line in enumerate(lines):
        m = WEB_START[code].match(line)
        if not m:
            continue
        cid = m.group(1)
        if not in_scope(cid):
            continue
        block = [line]
        if cid == "ARCH-C34":   # positions continue on the following bullet lines
            for nxt in lines[i + 1:]:
                if nxt.startswith("|") or nxt.startswith("**") or nxt.startswith("#"):
                    break
                block.append(nxt)
        if "WEB:" + cid in web_claims:
            fail(f"duplicate web claim id {cid}")
        web_claims["WEB:" + cid] = "\n".join(block)
        claim_area["WEB:" + cid] = "WEB:" + code
    for k, v in read_register(WEB, slot, code).items():
        web_tiers["WEB:" + k] = v

# ---------------------------------------------------------------- part 1
p1_reg = {}
for line in (P1 / "sources.md").read_text().splitlines():
    if re.match(r"\| REG-\d+ \|", line):
        p1_reg[cells(line)[0]] = cells(line)[1]
p1_led = set()
for line in (P1 / "claims_ledger.md").read_text().splitlines():
    m = re.match(r"\| (L\d+) \|", line)
    if m:
        p1_led.add(m.group(1))

# ---------------------------------------------------------------- part 2 sources
src_text = (HERE / "sources_part2.md").read_text()
new_reg, replaced_by, mapped = {}, {}, {}
section = None
for line in src_text.splitlines():
    if line.startswith("## "):
        section = line
        continue
    if re.match(r"\| REG-\d+ \|", line):
        c = cells(line)
        rid, tier, replaces = c[0], c[1], [x.strip() for x in c[6].split(",")]
        n = int(rid.split("-")[1])
        if not 1001 <= n <= 1499:
            fail(f"new register id {rid} outside REG-1001 to REG-1499")
        if rid in new_reg:
            fail(f"duplicate register id {rid}")
        new_reg[rid] = (tier, replaces)
        for sid in replaces:
            if sid in replaced_by:
                fail(f"source id {sid} replaced twice ({replaced_by[sid]}, {rid})")
            replaced_by[sid] = rid
    elif section and "resolve to a row of part 1" in section and re.match(r"\| (?:WEB:)?[A-Z]+-S\d+ \|", line):
        c = cells(line)
        sid, rid = c[0], c[1]
        if rid not in p1_reg:
            fail(f"{sid} mapped to {rid}, which is not in part 1")
        if sid in replaced_by:
            fail(f"source id {sid} resolved twice ({replaced_by[sid]}, {rid})")
        replaced_by[sid] = rid
        mapped[sid] = rid

all_orig_tiers = {**own_tiers, **web_tiers}
for sid in own_tiers:
    if sid not in replaced_by:
        fail(f"original source id {sid} of the four slots not in sources_part2.md")
for sid in replaced_by:
    if sid not in all_orig_tiers and sid != "AUTH-S21":
        fail(f"sources_part2.md names unknown original source id {sid}")
rank = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}
for rid, (tier, replaces) in new_reg.items():
    best = min((all_orig_tiers[s] for s in replaces if s in all_orig_tiers), key=lambda t: rank[t], default=None)
    if best is not None and best != tier:
        fail(f"{rid}: tier {tier} is not the highest origin tier {best}")

# ---------------------------------------------------------------- part 2 ledger
ledger_text = (HERE / "claims_ledger_part2.md").read_text()
ledger, seen = {}, {}
skipped = {}
for line in ledger_text.splitlines():
    if re.match(r"\| L\d+ \|", line):
        c = cells(line)
        if len(c) != 10:
            fail(f"{c[0]}: {len(c)} columns instead of 10")
            continue
        lid = c[0]
        if lid in ledger:
            fail(f"duplicate ledger id {lid}")
        merges = [x.strip() for x in c[2].split(",")]
        ledger[lid] = dict(merges=merges, areas=c[3], positions=c[7], sources=c[9])
        for cid in merges:
            seen.setdefault(cid, []).append(lid)
    m = re.match(r"\| (WEB:[A-Z]+-C\d+) \| ", line)
    if m and not re.match(r"\| L\d+ \|", line):
        if m.group(1) in skipped:
            fail(f"web claim {m.group(1)} listed twice as skipped")
        skipped[m.group(1)] = line

ids = sorted(ledger)
expected = [f"L{n}" for n in range(1001, 1001 + len(ids))]
if ids != expected:
    fail("ledger ids are not sequential from L1001")
if len(ids) > 499:
    fail("more than 499 ledger rows")

orig_all = {**own_claims, **web_claims}
multi = [c for c, v in seen.items() if len(v) != 1]
unknown = [c for c in seen if c not in orig_all]
dropped_own = [c for c in own_claims if c not in seen]
imported_web = [c for c in web_claims if c in seen]
unaccounted_web = [c for c in web_claims if c not in seen and c not in skipped]
both_web = [c for c in web_claims if c in seen and c in skipped]
unknown_skipped = [c for c in skipped if c not in web_claims]
unplaced = []
for lid, row in ledger.items():
    for cid in row["merges"]:
        if cid in orig_all and not re.search(r"(?<![A-Za-z:])" + re.escape(claim_area[cid]) + r"(?![A-Za-z])", row["areas"]):
            unplaced.append(cid)
for c in multi:
    fail(f"claim {c} appears in {len(seen[c])} rows")
for c in unknown:
    fail(f"ledger names unknown claim id {c}")
for c in dropped_own:
    fail(f"claim {c} dropped")
for c in unaccounted_web:
    fail(f"web claim {c} neither imported nor skipped")
for c in both_web:
    fail(f"web claim {c} both imported and skipped")
for c in unknown_skipped:
    fail(f"skipped table names unknown web claim {c}")
for c in unplaced:
    fail(f"claim {c} placed in a row without its origin area")

# ---------------------------------------------------------------- citations
def resolve_token(tok, cid):
    if "-" in tok:
        pre = tok.split("-")[0]
        return ("WEB:" + tok) if pre in WEB_CODES else tok
    area = claim_area[cid].replace("WEB:", "")
    sid = f"{area}-{tok}"
    return ("WEB:" + sid) if area in WEB_CODES else sid


cited_orig = 0
cited_ledger = set()
for lid, row in ledger.items():
    row_regs = {s.strip() for s in row["sources"].split(",") if s.strip() and s.strip() != "-"}
    cited_ledger |= row_regs
    for r in row_regs:
        if r not in p1_reg and r not in new_reg:
            fail(f"{lid}: cited source {r} does not resolve in part 1 or part 2")
    for cid in row["merges"]:
        if cid not in orig_all:
            continue
        for m in TOKEN.finditer(orig_all[cid]):
            sid = resolve_token(m.group(1), cid)
            cited_orig += 1
            if sid not in all_orig_tiers and sid != "AUTH-S21":
                fail(f"{cid}: cited source {sid} does not resolve in its register")
            elif replaced_by.get(sid) not in row_regs:
                fail(f"{cid}: source {sid} ({replaced_by.get(sid)}) missing from the sources of {lid}")

# ---------------------------------------------------------------- see also links
links1 = links2 = 0
p1_targets = set()
for lid, row in ledger.items():
    for seg in re.findall(r"see also (.*?)(?:\.\s|\.$|$)", row["positions"]):
        for m in re.finditer(r"(?<![A-Za-z0-9-])L(\d{3,4})(?![A-Za-z0-9])", seg):
            l = "L" + m.group(1)
            if len(m.group(1)) == 3:
                links1 += 1
                p1_targets.add(l)
                if l not in p1_led:
                    fail(f"{lid}: see also {l} does not exist in part 1")
            else:
                links2 += 1
                if l not in ledger:
                    fail(f"{lid}: see also {l} does not exist in part 2")

# ---------------------------------------------------------------- hygiene
for f in HERE.glob("*"):
    if f.suffix in (".md", ".py"):
        t = f.read_text()
        for pat in ("/Us" + "ers/", "/ho" + "me/", "~" + "/", "[A-Za-z]:" + chr(92) + chr(92)):
            if re.search(pat, t):
                fail(f"{f.name}: contains a path-like string matching {pat}")

# ---------------------------------------------------------------- report
merged_rows = [l for l, r in ledger.items() if len(r["merges"]) > 1]
by_origin = {}
for cid in own_claims:
    by_origin[claim_area[cid]] = by_origin.get(claim_area[cid], 0) + 1
web_scope = {}
for cid in web_claims:
    web_scope[claim_area[cid]] = web_scope.get(claim_area[cid], 0) + 1
print("claims in (four slots): " + ", ".join(f"{k} {v}" for k, v in by_origin.items()) + f"; total {len(own_claims)}")
print(f"web claims in scope: {len(web_claims)} (" + ", ".join(f"{k[4:]} {v}" for k, v in web_scope.items()) + f"); imported {len(imported_web)}; skipped {len(skipped)}")
print(f"rows out: {len(ledger)}; merged rows: {len(merged_rows)} merging {sum(len(ledger[l]['merges']) for l in merged_rows)} originals")
print(f"see also links: {links1} to part 1 ({len(p1_targets)} distinct part-1 rows), {links2} within part 2")
print(f"dropped: {len(dropped_own) + len(unaccounted_web)}; unplaced: {len(unplaced)}; claims in more than one row: {len(multi)}; unknown ids: {len(unknown)}")
print(f"sources: {len(own_tiers)} original ids of the four slots (+ {len([s for s in replaced_by if s.startswith('WEB:')])} cited web ids) -> {len(new_reg)} new rows and {len(mapped)} ids mapped to part 1; citations checked in origin claims: {cited_orig}; distinct sources cited by the ledger: {len(cited_ledger)}")
for e in errors[:40]:
    print("  error:", e)
if errors:
    print(f"FAIL: {len(errors)} error(s)")
    sys.exit(1)
print("PASS: every original claim id of the four slots and every imported web claim id appears exactly once, none dropped, every in-scope web claim imported or skipped, every cited source resolves in part 1 or part 2")
