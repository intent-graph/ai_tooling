"""Stage 6, step 3: completeness of the built graphs against the skeleton and the ledger.

Run from the guideline root:  python3 build/assemble/check_complete.py
Exit 0 only if every check holds. Reads the two graph files (YAML) and re-parses the skeleton and ledger
with the same parser that generated the batches.
"""
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batches as b  # noqa: E402

ROOT = b.ROOT
G = {b.P_ID: yaml.safe_load((ROOT / b.P_FILE).read_text()), b.D_ID: yaml.safe_load((ROOT / b.D_FILE).read_text())}
model = b.parse_skeleton()
ledger = b.parse_ledger()
slots = b.claim_slots()
fails, report = [], {}


def check(ok, msg):
    if not ok:
        fails.append(msg)


for gid in (b.P_ID, b.D_ID):
    g = G[gid]
    nodes = {n["uid"]: n for n in g["nodes"]}
    sk = model["nodes"][gid]
    check(len(nodes) == len(sk), f"{gid}: node count {len(nodes)} vs skeleton {len(sk)}")
    for s in sk:
        n = nodes.get(s["uid"])
        if not n:
            fails.append(f"{gid}: missing node {s['uid']}")
            continue
        check(n["name"] == s["name"], f"{s['uid']}: name differs")
        check(" ".join(n["intent"].split()) == " ".join(s["intent"].split()), f"{s['uid']}: intent differs")
        check(n.get("epistemic_state") == s["epistemic"], f"{s['uid']}: epistemic_state differs")
        check("\\|" not in n.get("epistemic_state", ""), f"{s['uid']}: escaped separator left")
    # tree: every non-root node has a treearc, parent = uid minus last segment
    arcs = {a["child"]: a["parent"] for a in g["treearcs"]}
    root_uid = "ROOT" if gid == b.P_ID else "PIG-JS.ROOT"
    check(set(arcs) == set(nodes) - {root_uid}, f"{gid}: treearcs do not cover all non-root nodes")
    for c, p in arcs.items():
        want = root_uid if c.rsplit(".", 1)[0] in ("PIG-JS",) or ("." not in c) else c.rsplit(".", 1)[0]
        check(p == want, f"{gid}: parent of {c} is {p}, expected {want}")
    # ledger: every claim in impl_pointers of its node; constraints count; rejected beliefs
    rows = [r for r in ledger if r["graph"] == gid]
    nclaims, nrows = 0, 0
    for r in rows:
        n = nodes[r["node"]]
        nrows += 1
        for c in r["claims"]:
            nclaims += 1
            check(f"build/research/{slots[c]}/result.md::{c}" in n.get("impl_pointers", []), f"{r['row']}: {c} not in impl_pointers of {r['node']}")
        if not r["claims"] and r["role"] == "rejected":
            check("Rejected beliefs: " in n.get("design_notes", "") and b.scrub_notes(re.sub(r"^Belief rejected:\s*", "", r["statement"]))[:60] in n["design_notes"], f"{r['row']}: rejected belief not in design_notes")
        if not r["claims"]:
            check(all(not p.endswith("::-") for p in n.get("impl_pointers", [])), f"{r['node']}: dash pointer")
    for uid, n in nodes.items():
        mine = [r for r in rows if r["node"] == uid]
        want = sum(r["role"] in ("decision", "acceptable-when") for r in mine)
        check(len(n.get("constraints", [])) == want, f"{uid}: constraints {len(n.get('constraints', []))} vs {want}")
        check(all(c.startswith(("MUST", "SHOULD", "Acceptable only when")) and not c.startswith("MUST hold:") for c in n.get("constraints", [])), f"{uid}: constraint form")
        wantp = {f"build/research/{slots[c]}/result.md::{c}" for r in mine for c in r["claims"]}
        check(set(n.get("impl_pointers", [])) == wantp, f"{uid}: impl_pointers differ from the ledger claims")
        if gid == b.D_ID and any(r["role"] == "decision" for r in mine):
            check("Judge record" in n.get("design_notes", ""), f"{uid}: no judge record")
    # intra links
    got = {(l["src"], l["dst"], l["shape"]["type"], " ".join(l["intent"].split())) for l in g["intentlinks"]}
    want = {(k["src"], k["dst"], k["type"], " ".join(k["sentence"].split())) for k in model["intra"][gid]}
    check(got == want and len(g["intentlinks"]) == len(want), f"{gid}: intra links differ ({len(got)} vs {len(want)})")
    # inter links
    other = b.PY_ID if gid == b.P_ID else b.P_ID
    got = {(l["src"], l["dst"], l["shape"]["type"], " ".join(l["intent"].split())) for l in g.get("inter_intentlinks", [])}
    want = {(f"{gid}:{k['src']}", k["dst"] if ":" in k["dst"] else f"{other}:{k['dst']}", k["type"], " ".join(k["sentence"].split()))
            for k in model["inter"][gid]}
    check(got == want and len(g["inter_intentlinks"]) == len(want), f"{gid}: inter links differ ({len(got)} vs {len(want)})")
    # planned links are not created
    blob = json.dumps(g)
    check("web-app-philosophy" not in blob and "pig-web-defaults" not in blob, f"{gid}: planned link created")
    report[gid] = dict(nodes=len(nodes), intra=len(g["intentlinks"]), inter=len(g["inter_intentlinks"]),
                       ledger_rows=nrows, claims_in_pointers=nclaims,
                       impl_pointers=sum(len(n.get("impl_pointers", [])) for n in nodes.values()),
                       constraints=sum(len(n.get("constraints", [])) for n in nodes.values()))

# public-repo hygiene over everything written
for p in list((ROOT / "intent_graphs").glob("*")) + list((ROOT / "build/assemble").rglob("*")):
    if p.is_file() and p.suffix in (".yaml", ".md", ".py", ".sh", ".json") and p.name != "result.md":
        t = p.read_text()
        for pat in ("/Us" + "ers/", "/ho" + "me/", "remi" + "cura", "~" + "/"):
            check(not re.search(pat, t), f"{p.relative_to(ROOT)}: matches {pat}")
print(json.dumps(report, indent=1))
print("FAILS:", len(fails))
for f in fails[:40]:
    print(" -", f)
sys.exit(1 if fails else 0)
