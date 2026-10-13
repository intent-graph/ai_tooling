"""Stage 6, step 1: generate the ig-tool inputs of both graphs from the skeleton and the ledger.

Reads   build/distill/skeleton.md, build/distill/claims_ledger.md, build/research/*/ (slot names)
Writes  build/assemble/gen/
          js_philosophy_batch.yaml      node.create + intra link.create   (apply --batch)
          js_defaults_tree.json         uid, name, intent, parent of every defaults node
          js_defaults_batch.yaml        node.set (content) + intra link.create   (apply --batch)
          js_philosophy_inter.sh        ig-tool link create, one per inter link
          js_defaults_inter.sh          idem
          planned_links.json            the planned boundary links (never created)
          model.json                    everything parsed, for the completeness check

Run:    python3 build/assemble/build_batches.py        (from the guideline root)
Deterministic. The graph files themselves are written only by ig-tool (see build_graphs.sh).
"""

import json
import re
import shlex
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKEL = ROOT / "build/distill/skeleton.md"
LEDGER = ROOT / "build/distill/claims_ledger.md"
GEN = ROOT / "build/assemble/gen"
GEN.mkdir(exist_ok=True)

P_ID, D_ID, PY_ID = "js-philosophy", "pig-js-defaults", "python-kb-philosophy"
P_FILE, D_FILE = "intent_graphs/js_philosophy.ig.yaml", "intent_graphs/js_defaults.ig.yaml"
CID = re.compile(r"\b[A-Z]+\d*-C\d+\b")
SRC = re.compile(r"\bSRC-\d+\b")


# ----------------------------------------------------------------------------- parsing
def split_cells(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    cells, cur, i = [], "", 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "\\|"
            i += 2
            continue
        if s[i] == "|":
            cells.append(cur.strip())
            cur = ""
            i += 1
            continue
        cur += s[i]
        i += 1
    cells.append(cur.strip())
    return cells


def unesc(s):
    """Skeleton escapes the IG separator as \\|; the graph writes it as ' | '."""
    return re.sub(r"\s*\\\|\s*", " | ", s).strip()


def plain(s):
    return s.replace("\\|", "|").strip()


def tables(lines, start, end):
    """Yield (heading, header, rows) for each markdown table between lines[start:end]."""
    heading, cur = "", None
    for n in range(start, end):
        line = lines[n]
        if line.startswith("#"):
            heading, cur = line.lstrip("#").strip(), None
        elif line.startswith("|"):
            c = split_cells(line)
            if cur is None:
                cur = dict(heading=heading, header=[x.lower() for x in c], rows=[])
                yield_list.append(cur)
            elif set(line.replace("|", "").strip()) <= set("-: "):
                pass
            else:
                cur["rows"].append(c)
        else:
            cur = None


yield_list = []


def parse_skeleton():
    lines = SKEL.read_text().splitlines()
    idx = {l: n for n, l in enumerate(lines) if l.startswith("## ")}
    p0 = idx["## Graph js-philosophy"]
    d0 = idx["## Graph pig-js-defaults"]
    pl0 = idx["## Planned boundary links to the web-architecture graphs (planned, not created)"]
    j0 = idx["## Judge records"]
    model = dict(nodes={P_ID: [], D_ID: []}, intra={P_ID: [], D_ID: []}, inter={P_ID: [], D_ID: []},
                 planned=[], judge={}, integration_notes=[])
    for gid, a, b in ((P_ID, p0, d0), (D_ID, d0, pl0)):
        yield_list.clear()
        tables(lines, a, b)
        for t in list(yield_list):
            h = t["heading"]
            if t["header"][:2] == ["uid", "name"]:
                for c in t["rows"]:
                    assert len(c) == 5, c
                    model["nodes"][gid].append(dict(uid=c[0], name=plain(c[1]), intent=plain(c[2]),
                                                    epistemic=unesc(c[3]), rows=c[4]))
            elif t["header"][:4] == ["#", "from", "to", "type"]:
                kind = "inter" if h.startswith("Inter links") else "intra"
                for c in t["rows"]:
                    model[kind][gid].append(dict(src=c[1], dst=c[2], type=c[3], sentence=plain(c[4]), table=h))
    yield_list.clear()
    tables(lines, pl0, j0)
    for c in yield_list[0]["rows"]:
        model["planned"].append(dict(n=c[0], src=c[1], graph=c[2], owned=plain(c[3])))
    parse_judge(lines[j0:], model)
    return model


def parse_judge(lines, model):
    """Judge records come in seven layouts; each is normalised to 'Label: text' lines keyed by node uid."""
    uid_re = re.compile(r"(PIG-JS\.[A-Z0-9_]+(?:\.[A-Z0-9_]+)*)")
    rec, cur = {}, None
    table_hdr = None

    def add(uid, text):
        rec.setdefault(uid, []).append(text)

    for ln in lines:
        s = ln.rstrip()
        if s.startswith("Integration note"):
            model["integration_notes"].append(s)
            cur = None
            continue
        if s.startswith("### "):
            cur, table_hdr = None, None
            continue
        if s.startswith("#### "):
            m = uid_re.search(s)
            cur, table_hdr = (m.group(1) if m else None), None
            continue
        m = re.match(r"\*\*(PIG-JS\.[A-Z0-9_.]*[A-Z0-9_])(?: to \.(\d+))?\.?\*\*\.?\s*(.*)$", s)
        if m:
            cur, table_hdr = m.group(1), None
            rest = m.group(3).strip()
            if m.group(2):  # one record shared by a run of sibling nodes: X.a to .b
                base, a = cur.rsplit(".", 1)
                group = [f"{base}.{i}" for i in range(int(a), int(m.group(2)) + 1)]
                for u in group:
                    add(u, f"Shared record of {group[0]} to .{m.group(2)}: " + rest)
                cur = None
            elif rest:
                add(cur, rest)
            continue
        if s.startswith("|"):
            c = split_cells(s)
            if set(s.replace("|", "").strip()) <= set("-: "):
                continue
            if c[0].lower() == "node":
                table_hdr = [x.split(" (")[0].capitalize() for x in c]
                continue
            if c[0].lower() == "element":
                continue
            if c[0].startswith("PIG-JS.") and table_hdr:
                for lab, val in zip(table_hdr[1:], c[1:]):
                    add(c[0], f"{lab}: {plain(val)}")
                cur = None
                continue
            if cur and len(c) == 2:
                add(cur, f"{c[0]}: {plain(c[1])}")
            continue
        if not s.strip():
            continue
        if cur and (s.startswith("- ") or cur in rec):
            add(cur, plain(s[2:] if s.startswith("- ") else s))
    model["judge"] = {k: "\n".join(v) for k, v in rec.items()}


def parse_ledger():
    rows = []
    for line in LEDGER.read_text().splitlines():
        if re.match(r"\| [A-Z]+-\d+ \|", line):
            c = split_cells(line)
            assert len(c) == 7, line
            rows.append(dict(row=c[0], claims=CID.findall(c[1]), claim_cell=c[1], node=c[2], graph=c[3],
                             statement=plain(c[4]), agreement=c[5], role=c[6]))
    return rows


def claim_slots():
    """claim-id prefix -> research slot folder, read from the claims index."""
    idx = (ROOT / "build/distill/claims_index.md").read_text().splitlines()
    m = {}
    for line in idx:
        c = split_cells(line) if line.startswith("| ") else []
        if len(c) >= 2 and re.match(r"^[A-Z]+\d*-C\d+$", c[0]):
            m[c[0]] = c[1]
    # slot 14 (second security gap round) is folded by patch and has no row in the generated index
    for path in sorted((ROOT / "build/research").glob("14_*/result.md")):
        for line in path.read_text().splitlines():
            c = split_cells(line) if line.startswith("| ") else []
            if c and re.match(r"^[A-Z]+\d*-C\d+$", c[0]):
                m[c[0]] = path.parent.name
    return m


# ----------------------------------------------------------------------------- sentence forms
NONIMP = {"In", "When", "With", "Before", "To", "For", "After", "Where", "Under", "From", "A", "An", "The",
          "Compiling", "Performance", "Object", "Module", "JSON", "GitHub", "Files", "Every", "Most", "Boundary",
          "Input", "Thread", "setAttribute", "node:test", "Promise.all", "Any", "Some"}


def must(stmt):
    s = stmt.strip()
    if s.startswith(("MUST", "SHOULD")):
        return s
    first = s.split(" ", 1)[0]
    rest = s[len(first):].lstrip()
    if s.startswith("Do not "):
        return "MUST NOT " + s[7:]
    if first == "Never":
        return "MUST NOT " + rest
    if first == "Always":
        return "MUST " + rest
    if first in NONIMP or not first[0].isupper() or any(ch in first for ch in ".:"):
        return "MUST hold: " + s
    return "MUST " + first[0].lower() + first[1:] + (" " + rest if rest else "")


# Acceptable-when rows whose statement does not open with "Acceptable when <condition>: <practice>".
ACCEPT = {
    "SUBSET-015": ("+0 and -0 must be distinguished (meta-programming)", "Object.is; everywhere else ==="),
    "SUBSET-020": ("a team adopts it as a convention completing the explicit-conversion rule",
                   "never call new on Boolean, Number, String or Symbol, call them as functions to coerce (Google JS guide position, demoted from evidence)"),
    "SUBSET-038": ("a team adopts it as a convention",
                   "prefer arrow functions over f.bind(this) and const self = this (Google JS guide position, demoted from evidence)"),
    "SUBSET-039": ("a team adopts it as a convention",
                   "use this only in class constructors and methods, in arrows inside them, or in functions with an explicit @this (Google JS guide position, demoted from evidence)"),
    "SUBSET-049": ("a team adopts it as a convention (the built-in part is carried by the decision row)",
                   "do not manipulate prototypes directly, use the class keyword (Google JS guide position, demoted from evidence)"),
    "SUBSET-052": ("the target lacks Object.hasOwn",
                   "obj.hasOwnProperty, because lookup and iteration traverse the prototype chain and one of the two own-property tests is necessary (MDN)"),
    "SUBSET-058": ("the data is JSON-safe only", "the JSON round trip as a deep copy; the belief that it is the way to deep copy is restricted to that condition (MDN structuredClone; folklore audit, restricted)"),
    "SUBSET-069": ("a team wants a rule that needs no judgment of cost", "no getter or setter properties at all, methods only (Google JS guide position, the stricter form; inferred condition, no admitted source states it)"),
    "SUBSET-070": ("a formatter and lint rules that catch insertion hazards both run in CI and the team adopts a no-semicolon style", "reliance on automatic semicolon insertion (inferred; no admitted source states the hazards or the style)"),
    "CONTROL-057": ("the work cannot move to a worker (condition inferred)", "a long computation that stays on the event loop is partitioned into small steps that yield between them (for instance with setImmediate)"),
    "STRUCTURE-030": ("the application has over about 100 modules or a dependency depth over 5", "keep bundling for production while writing small fine-grained modules (V8's 2018 position, dated and restricted)"),
    "DEFENSE-097": ("the environment is high-sensitivity and tested for breakage", "freeze built-in prototypes or lock down the realm (SES is MDN's example); Object.freeze is shallow, belief rejected: freeze makes nested data immutable"),
    "DEFENSE-156": ("the code is a code loader", "eval and Function(string) (Google's JavaScript guide forbids them except there; a position of one style guide, not evidence)"),
    "VERIFICATION-010": ("an organization with Google-like test infrastructure sets a mix", "a test mix of about 80% narrow unit tests, 15% medium integration tests and 5% end-to-end (Google's stated practice, not a general rule)"),
    "VERIFICATION-015": ("a team wants properties beside the code", "write properties in the same module as the functions they test, as checkable documentation (the QuickCheck authors' practice, outside the method the source is admitted for)"),
    "VERIFICATION-030": ("Biome is the linter", "only safe fixes are guaranteed not to change semantics, so review unsafe fixes by hand; type-aware rules switch on Biome's scanner only when enabled (facts about Biome only)"),
    "VERIFICATION-034": ("the alternative satisfies FORMAT.1 and FORMAT.2: Biome when it is the linter, @stylistic or dprint when a team accepts the stated cost",
                         "a formatter other than Prettier; the ESLint technical steering committee names Prettier, dprint or @stylistic, Biome documents one tool whose formatter handles all formatting decisions beside its linter, and no admitted source ranks them"),
    "RUNTIME-009": ("a profile shows the creation cost on a hot path", "avoiding function creation inside functions where no closure is needed (each instance carries its own scope and closure); MDN states the cost without a measurement"),
    "RUNTIME-010": ("a profile shows the cost", "setting an object's prototype at creation rather than with setPrototypeOf or __proto__ as a speed motive (later changes disrupt engine optimisations and may cause deoptimising recompilation)"),
    "RUNTIME-020": ("V8 profiles do not suffice", "perf flame graphs: run Node with --perf-basic-prof or the -only-functions variant (the --interpreted-frames-native-stack part is not reconfirmed against current CLI docs, open) and read the most saturated bars first"),
    "RUNTIME-025": ("a snapshot is wanted at the moment the heap nears its limit", "capture it with --heapsnapshot-near-heap-limit=N (stable); several snapshots may be written because collection during snapshotting can lower usage"),
}
ACC_RE = re.compile(r"^Acceptable (?:only )?(?:when|where) (.+?): (.+)$", re.S)


def acceptable(row):
    if row["row"] in ACCEPT:
        cond, prac = ACCEPT[row["row"]]
    else:
        m = ACC_RE.match(row["statement"])
        if not m:
            raise SystemExit(f"acceptable-when row without a condition rule: {row['row']}: {row['statement'][:80]}")
        cond, prac = m.group(1), m.group(2)
    return f"Acceptable only when {cond}: {prac.rstrip('.')}."


# ----------------------------------------------------------------------------- node content
ROWID = r"(?:SUBSET|CONTRACTS|CONTROL|STRUCTURE|DEFENSE|DEPENDENCIES|VERIFICATION|RUNTIME)-\d{3}"


def scrub_notes(text):
    """Build bookkeeping never reaches design_notes (stage 7, F09): ledger row ids, gap ids, merge notes, slot labels."""
    t = re.sub(r"\s*\((?:see )?" + ROWID + r"\)", "", text)
    t = re.sub(r"\s*\(" + ROWID + r", (inferred)\)", r" (\1)", t)
    t = re.sub(r"[;,] (?:see )?" + ROWID + r"(?=\))", "", t)
    t = re.sub(r"(?<=\()" + ROWID + r", ", "", t)
    t = re.sub(r",? " + ROWID + r"(?=\)|\.|,)", "", t)
    t = re.sub(r"[,;]? \(?G-[LM]\d+\)?", "", t)
    t = re.sub(r"\s*Merged(?: at integration)?[^.]*\.", "", t)
    t = re.sub(r"12_dissent(?: (?:topic \d+|X\d+))?", "the dissent audit", t)
    return t


def node_content(n, rows, judge, slots, notes, problems):
    mine = [r for r in rows if r["node"] == n["uid"]]
    dec = [r for r in mine if r["role"] == "decision"]
    acc = [r for r in mine if r["role"] == "acceptable-when"]
    constraints = [must(r["statement"]) for r in dec] + [acceptable(r) for r in acc]
    for c in constraints:
        if c.startswith("MUST hold:"):
            problems.append(f"{n['uid']}: a statement is not a rule (move it to a fact row): {c[:70]}")
    pointers, seen = [], set()
    for r in mine:
        for c in r["claims"]:
            if c not in slots:
                problems.append(f"{r['row']}: claim {c} not in claims_index")
                continue
            p = f"build/research/{slots[c]}/result.md::{c}"
            if p not in seen:
                seen.add(p)
                pointers.append(p)
    lines = []
    if n["uid"] in judge:
        lines.append("Judge record:\n" + judge[n["uid"]])
    for r in mine:
        if r["role"] == "rejected" and not r["claims"]:
            lines.append("Rejected beliefs: " + re.sub(r"^Belief rejected:\s*", "", r["statement"]))
    for r in mine:
        if r["role"] == "rejected" and r["claims"]:
            lines.append(f"Rejected [{r['agreement']}]: " + r["statement"])
    for r in mine:
        if r["role"] == "deferred":
            lines.append("Deferred: " + r["statement"])
    for r in mine:
        if r["role"] == "fact":
            lines.append(f"Fact [{r['agreement']}]: " + r["statement"])
    # stage 7: row lists and integration notes are build bookkeeping; they stay in the ledger and the skeleton.
    srcs = sorted(set(SRC.findall(" ".join(r["statement"] for r in mine) + " " + judge.get(n["uid"], ""))))
    if srcs:
        lines.append("Sources cited: " + ", ".join(srcs))
    return constraints, scrub_notes("\n".join(lines).strip()), pointers


def main():
    model = parse_skeleton()
    ledger = parse_ledger()
    slots = claim_slots()
    problems = []
    for gid in (P_ID, D_ID):
        uids = {n["uid"] for n in model["nodes"][gid]}
        for n in model["nodes"][gid]:
            bad = set(n["name"]) & set('/\\:*?"<>|[]#^')
            if bad:
                problems.append(f"{n['uid']}: name has unsafe characters {sorted(bad)}")
        for r in ledger:
            if r["graph"] == (gid if gid == P_ID else D_ID) and r["node"] not in uids:
                problems.append(f"{r['row']}: node {r['node']} not in skeleton")
    all_nodes = {n["uid"] for g in model["nodes"].values() for n in g}
    for uid in model["judge"]:
        if uid not in all_nodes:
            problems.append(f"judge record for unknown node {uid}")
    notes = model["integration_notes"]

    content = {}
    for gid in (P_ID, D_ID):
        for n in model["nodes"][gid]:
            rows = [r for r in ledger if r["graph"] == gid]
            content[n["uid"]] = node_content(n, rows, model["judge"], slots, notes, problems)

    # ---- philosophy batch: node.create with parent, then intra links
    def parent_of(uid, gid):
        if gid == P_ID:
            return None if uid == "ROOT" else ("ROOT" if "." not in uid else uid.rsplit(".", 1)[0])
        if uid == "PIG-JS.ROOT":
            return None
        p = uid.rsplit(".", 1)[0]
        return "PIG-JS.ROOT" if p == "PIG-JS" else p

    for gid in (P_ID, D_ID):
        uids = {n["uid"] for n in model["nodes"][gid]}
        for n in model["nodes"][gid]:
            p = parent_of(n["uid"], gid)
            if p is not None and p not in uids:
                problems.append(f"{n['uid']}: parent {p} not a node")

    def link_ops(gid):
        ops, seen = [], defaultdict(int)
        for k in model["intra"][gid]:
            seen[(k["src"], k["dst"])] += 1
        used = defaultdict(int)
        for k in model["intra"][gid]:
            op = dict(op="link.create", src=k["src"], dst=k["dst"], intent=k["sentence"], shape=dict(type=k["type"]))
            if seen[(k["src"], k["dst"])] > 1:
                op["tag"] = k["type"] + (str(used[(k["src"], k["dst"])] + 1) if used[(k["src"], k["dst"])] else "")
            used[(k["src"], k["dst"])] += 1
            ops.append(op)
        return ops

    def dump(path, data):
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=10_000))

    ops = []
    for n in model["nodes"][P_ID]:
        if n["uid"] == "ROOT":
            continue
        cons, dn, ptr = content[n["uid"]]
        op = dict(op="node.create", uid=n["uid"], name=n["name"], intent=n["intent"], parent=parent_of(n["uid"], P_ID),
                  epistemic_state=n["epistemic"])
        if cons:
            op["constraints"] = cons
        if dn:
            op["design_notes"] = dn
        if ptr:
            op["impl_pointers"] = ptr
        ops.append(op)
    root = next(n for n in model["nodes"][P_ID] if n["uid"] == "ROOT")
    ops.insert(0, dict(op="node.set", uid="ROOT", epistemic_state=root["epistemic"]))
    ops += link_ops(P_ID)
    dump(GEN / "js_philosophy_batch.yaml", dict(operations=ops))
    (GEN / "js_philosophy_root.json").write_text(json.dumps(dict(name=root["name"], intent=root["intent"])))

    # ---- defaults: tree file (structure only) and content batch
    tree = [dict(uid=n["uid"], name=n["name"], intent=n["intent"], parent=parent_of(n["uid"], D_ID))
            for n in model["nodes"][D_ID]]
    (GEN / "js_defaults_tree.json").write_text(json.dumps(tree, indent=1))
    ops = []
    for n in model["nodes"][D_ID]:
        cons, dn, ptr = content[n["uid"]]
        op = dict(op="node.set", uid=n["uid"], epistemic_state=n["epistemic"])
        if cons:
            op["constraints"] = cons
        if dn:
            op["design_notes"] = dn
        if ptr:
            op["impl_pointers"] = ptr
        ops.append(op)
    ops += link_ops(D_ID)
    dump(GEN / "js_defaults_batch.yaml", dict(operations=ops))

    # ---- inter links: ig-tool link create, both endpoints qualified
    for gid, gfile, own, other in ((P_ID, P_FILE, P_ID, None), (D_ID, D_FILE, D_ID, P_ID)):
        out, seen, used = [], defaultdict(int), defaultdict(int)
        for k in model["inter"][gid]:
            seen[(k["src"], k["dst"])] += 1
        for k in model["inter"][gid]:
            src = f"{own}:{k['src']}"
            dst = k["dst"] if ":" in k["dst"] else f"{other}:{k['dst']}"
            args = ["ig-tool", "link", "create", "-g", gfile, "-o", gfile, "--src", src, "--dst", dst,
                    "--intent", k["sentence"], "--shape", json.dumps(dict(type=k["type"])),
                    "--role", "assembler", "-m", f"inter link {own} to {dst.split(':')[0]}: add from the skeleton"]
            if seen[(k["src"], k["dst"])] > 1:
                args += ["--tag", k["type"] + str(used[(k["src"], k["dst"])] + 1)]
            used[(k["src"], k["dst"])] += 1
            out.append(" ".join(shlex.quote(a) for a in args) + " > /dev/null || exit 1")
        (GEN / f"{'js_philosophy' if gid == P_ID else 'js_defaults'}_inter.sh").write_text(
            "set -e\n" + "\n".join(out) + "\n")

    (GEN / "planned_links.json").write_text(json.dumps(model["planned"], indent=1))
    (GEN / "model.json").write_text(json.dumps(dict(
        nodes=model["nodes"], intra=model["intra"], inter=model["inter"],
        content={u: dict(constraints=c[0], design_notes=c[1], impl_pointers=c[2]) for u, c in content.items()},
        judge_keys=sorted(model["judge"])), indent=1))

    dec_nodes = {r["node"] for r in ledger if r["role"] == "decision" and r["graph"] == D_ID}
    miss = sorted(dec_nodes - set(model["judge"]))
    stats = dict(nodes={g: len(model["nodes"][g]) for g in model["nodes"]},
                 intra={g: len(model["intra"][g]) for g in model["intra"]},
                 inter={g: len(model["inter"][g]) for g in model["inter"]},
                 planned=len(model["planned"]), judge_records=len(model["judge"]),
                 decision_nodes_without_record=miss, ledger_rows=len(ledger), problems=problems)
    print(json.dumps(stats, indent=1))
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
