"""Stage 5c: integrate the eight branch folders into one ledger, one skeleton and one review file.

Reads  build/distill/branches/<BRANCH>/{ledger,skeleton,decisions}.md
Writes build/distill/{claims_ledger,skeleton,decisions_for_review}.md and
       build/distill/5c_integrate/{link_resolution.md,stats.json}

Run:   python3 build/distill/5c_integrate/integrate.py        (from the guideline root)
Never edits the branch folders. Deterministic: re-running rewrites the same files.

What it does, in order:
  1. ledger: all branch ledgers in branch order, two P5 row merges applied (MERGES below).
  2. nodes: every branch node table, breadth-first, epistemic cells normalized to the IG
     separator `\\|`, the ledger-rows column derived from the merged ledger, the T3 relabel
     applied, a few intents adjusted for the P5 merges (NODE_EDITS below).
  3. links: branch-internal links kept, the 101 cross-branch proposals resolved to uids
     (LINKS below, every proposal accounted for), links renumbered per table.
  4. judge records and decisions copied verbatim (headings demoted), integration decisions added.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DISTILL = HERE.parent
BR = DISTILL / "branches"
ORDER = ["SUBSET", "CONTRACTS", "CONTROL", "STRUCTURE", "DEFENSE", "DEPENDENCIES", "VERIFICATION", "RUNTIME"]
CID = re.compile(r"\b[A-Z]+-C\d+\b")
PYTHON_UIDS = {"INTENTIONALITY", "STRUCTURE", "ROUGHTOFINE", "DATACENTRICITY", "COMMUNICATION",
               "REPRODUCIBILITY", "POLYGLOT", "DEFENSIVE"}


# ----------------------------------------------------------------------------- parsing helpers
def split_cells(line: str) -> list[str]:
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


def tables(path: Path):
    out, heading, cur = [], "", None
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("#"):
            heading, cur = line.lstrip("#").strip(), None
            continue
        if line.startswith("|"):
            c = split_cells(line)
            if cur is None:
                cur = dict(heading=heading, header=[x.lower() for x in c], rows=[], line=n)
                out.append(cur)
                continue
            if set(line.replace("|", "").strip()) <= set("-: "):
                continue
            cur["rows"].append((n, c))
        else:
            cur = None
    return out


def is_def(uid: str) -> bool:
    return uid.startswith("PIG-JS.")


def esc(s: str) -> str:
    """Escape bare pipes in a cell; already escaped pipes stay."""
    return re.sub(r"(?<!\\)\|", r"\\|", s)


# ----------------------------------------------------------------------------- 1. ledger
LEDGER_COLS = ["row", "claim_ids", "node", "graph", "statement", "agreement", "role"]


def read_ledger(b: str):
    rows = []
    for line in (BR / b / "ledger.md").read_text().splitlines():
        if line.startswith("|"):
            c = split_cells(line)
            if len(c) == 7 and c[0].startswith(b + "-"):
                rows.append(dict(zip(LEDGER_COLS, c)))
    return rows


MERGES = [
    # (survivor row, absorbed row, new claim_ids, new statement, new agreement)
    dict(
        survivor="CONTROL-078", absorbed="CONTROL-011", node="PIG-JS.CONTROL.PROCESS.2",
        claim_ids="ASYNC-C05, RUNTIME-C37",
        statement=("Treat the unhandledRejection and uncaughtException hooks as last-resort reporting points, "
                   "never as a way to carry on: after an uncaught exception the application state is undefined and "
                   "resuming is unsafe, so use uncaughtException only for synchronous cleanup before exiting and let "
                   "an external supervisor restart the process. Merged at integration (P5, overlap O02): ASYNC-C05 and "
                   "RUNTIME-C37 state one principle, which CONTROL.LIFECYCLE holds as intent."),
        agreement="single-source",
        why="P5: the process-end principle was stated by two rows in two graphs (CONTROL.LIFECYCLE and PIG-JS.CONTROL.PROCESS.2); one row now carries both claims on the node that names the Node hooks",
    ),
    dict(
        survivor="SUBSET-051", absorbed="DEFENSE-091", node="PIG-JS.SUBSET.OBJECTS.6",
        claim_ids="LANG-C55, RUNSEC-C07",
        statement=("Prefer Object.hasOwn(obj, key) over obj.hasOwnProperty(key), because the inherited method may be "
                   "shadowed or absent on a null-prototype object; for untrusted-keyed reads, read with Object.hasOwn and "
                   "iterate with Object.keys or for...of, never for...in, so inherited (possibly polluted) properties are "
                   "not visited. Grounds: MDN prototype pollution and Node security best practices (two T1 sources) for "
                   "untrusted keys, a style-guide position for the general preference; extending it to all reads is "
                   "inferred. Merged at integration (P5, overlap O15): LANG-C55 and RUNSEC-C07 state one rule."),
        agreement="consensus",
        why="P5: the own-property read was a decision in two nodes (PIG-JS.SUBSET.OBJECTS.6 and PIG-JS.DEFENSE.PROTOTYPE.1); one row now carries both claims on the owner node of overlap O15",
    ),
]


def build_ledger():
    allrows, merged_log = [], []
    by_branch = {b: read_ledger(b) for b in ORDER}
    absorbed = {m["absorbed"] for m in MERGES}
    for b in ORDER:
        for r in by_branch[b]:
            if r["row"] in absorbed:
                continue
            for m in MERGES:
                if r["row"] == m["survivor"]:
                    r = dict(r, claim_ids=m["claim_ids"], node=m["node"], statement=m["statement"],
                             agreement=m["agreement"])
                    merged_log.append(m)
            allrows.append(dict(r, branch=b))
    n_in = sum(len(v) for v in by_branch.values())
    return allrows, by_branch, merged_log, n_in


# ----------------------------------------------------------------------------- 2. nodes
# Intent / epistemic edits made at integration (every one is listed in result.md L3).
NODE_EDITS = {
    "PIG-JS.CONTROL.PROCESS.2": dict(
        intent=("Node's uncaughtException hook is used only for synchronous cleanup before the process ends, and "
                "uncaughtExceptionMonitor only to log; the end-and-restart contract itself is CONTROL.LIFECYCLE."),
    ),
    "CONTROL.LIFECYCLE": dict(
        epistemic=("known \\| unvalidated: single T1 source; grounded by the merged row CONTROL-078 on "
                   "PIG-JS.CONTROL.PROCESS.2 (P5 merge); rolls up PIG-JS.CONTROL.PROCESS"),
    ),
    "PIG-JS.DEFENSE.PROTOTYPE.1": dict(
        intent=("No nested write with untrusted keys, no unfiltered merge and no __proto__ accessor; the own-property "
                "read for untrusted keys is the rule of PIG-JS.SUBSET.OBJECTS.6."),
    ),
    "PIG-JS.SUBSET.OBJECTS.6": dict(
        epistemic=("known \\| unvalidated: for-in rule on arrays single T2 source; hasOwn preference grounded for "
                   "untrusted keys by two T1 sources (RUNSEC-C07, merged here), extension to all reads inferred"),
    ),
    "PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE": dict(
        epistemic_replace=("default escaping missing for several candidates",
                           "default escaping missing for several candidates (the Angular and Vue facts sit in PIG-JS.DEFENSE.DOM.6.2)"),
    ),
}

# Nodes whose decision rests on a single T3 source (checked against build/audit/source_register.md).
T3_RELABEL = ["PIG-JS.STRUCTURE.LOADING.6", "PIG-JS.STRUCTURE.DIRECTION.2",
              "VERIFICATION.TEST_SUITE.3", "VERIFICATION.TEST_STABILITY.3"]

ROOT_P = dict(
    uid="ROOT", name="Solid JavaScript",
    intent=("JavaScript code whose behaviour is predictable, whose changes stay cheap and which resists attack, in the "
            "browser and in Node. JavaScript is permissive and widely misused; with strong principles it is made useful "
            "and safe by narrowing it to a checked subset rather than by avoiding it."),
    epistemic="known", rows="-")
ROOT_D = dict(
    uid="PIG-JS.ROOT", name="Solid JavaScript defaults",
    intent=("The concrete rules that make JavaScript predictable, cheap to change and attack-resistant in the browser and "
            "in Node: the safe subset, the type layer and boundary parsing, explicit control of time and failure, "
            "locality of change, hostile-input defence, trusted dependencies, machine verification and measured runtime "
            "behaviour. Each rule is one decision traced to ledger rows."),
    epistemic="known", rows="-")


def read_nodes():
    nodes = {"P": {}, "D": {}}
    order = {"P": [], "D": []}
    for b in ORDER:
        for t in tables(BR / b / "skeleton.md"):
            if t["header"][0] != "uid":
                continue
            for n, c in t["rows"]:
                uid = c[0]
                g = "D" if is_def(uid) else "P"
                assert uid not in nodes[g], uid
                epistemic = " \\| ".join(c[3:-1])
                nodes[g][uid] = dict(uid=uid, name=c[1], intent=c[2], epistemic=epistemic, orig_rows=c[-1], branch=b)
                order[g].append(uid)
    return nodes, order


def parent_of(uid: str):
    if uid in ("ROOT", "PIG-JS.ROOT"):
        return None
    pre = "PIG-JS." if is_def(uid) else ""
    rest = uid[len(pre):]
    if "." not in rest:
        return pre + "ROOT"
    return pre + rest.rsplit(".", 1)[0]


def depth(uid: str) -> int:
    pre = "PIG-JS." if is_def(uid) else ""
    return uid[len(pre):].count(".") + 1


def bfs(nodes_g, order_g, branch):
    uids = [u for u in order_g if nodes_g[u]["branch"] == branch]
    kids = defaultdict(list)
    for u in uids:
        kids[parent_of(u)].append(u)
    roots = [u for u in uids if depth(u) == 1]
    assert len(roots) == 1, (branch, roots)
    out, q = [], [roots[0]]
    while q:
        u = q.pop(0)
        out.append(u)
        q.extend(kids.get(u, []))
    assert len(out) == len(uids), (branch, len(out), len(uids))
    return out


# ----------------------------------------------------------------------------- 3. links
def read_links():
    """Branch-internal links by kind, proposals and planned boundary rows, with source ids."""
    inner = {"P": [], "D": []}          # (branch, from, to, type, sentence)
    inter_dp = []                       # defaults -> philosophy (same or other branch)
    inter_py = []                       # philosophy -> python-kb-philosophy
    proposals = {}                      # (branch, graph, idx) -> dict
    planned = []                        # (branch, from, note)
    for b in ORDER:
        for t in tables(BR / b / "skeleton.md"):
            h = t["header"]
            if h[0] != "#":
                continue
            heading = t["heading"].lower()
            if h[:3] == ["#", "from", "note"] or h[:3] == ["#", "from", "boundary content"]:
                for n, c in t["rows"]:
                    planned.append((b, c[1], c[2]))
                continue
            if len(h) < 5:
                continue
            is_prop = ("proposed" in heading) or ("to (branch)" in h)
            for n, c in t["rows"]:
                idx, frm, to, typ = c[0], c[1], c[2], c[3]
                sent = " | ".join(c[4:])
                frm = re.sub(r"^(js-philosophy|pig-js-defaults):", "", frm)
                if is_prop:
                    g = "D" if (is_def(frm) or is_def(to)) else "P"
                    proposals[(b, g, idx)] = dict(branch=b, graph=g, idx=idx, frm=frm, to=to, type=typ, sentence=sent)
                elif to.startswith("python-kb-philosophy:"):
                    assert to.split(":", 1)[1] in PYTHON_UIDS, to
                    inter_py.append((b, frm, to, typ, sent))
                elif is_def(frm) and not is_def(to):
                    inter_dp.append((b, frm, to if to.startswith("js-philosophy:") else "js-philosophy:" + to, typ, sent))
                elif is_def(frm):
                    inner["D"].append((b, frm, to, typ, sent))
                else:
                    inner["P"].append((b, frm, to, typ, sent))
    return inner, inter_dp, inter_py, proposals, planned


# Resolution of every cross-branch proposal.  Each entry:
#   graph, from, to, type, sentence (None = the first source's sentence), sources, note
# source = (branch, graph, idx, how) with how in: given | flipped | retargeted | retyped | merged
LINKS = []
DROPPED = {}   # (branch, graph, idx) -> reason
PLANNED_PROPOSALS = {}  # (branch, graph, idx) -> planned boundary text


def L(graph, frm, to, typ, sent, srcs, note=""):
    LINKS.append(dict(graph=graph, frm=frm, to=to, type=typ, sentence=sent, srcs=srcs, note=note))


S = lambda b, g, i, how="given": (b, g, str(i), how)

# --- philosophy graph, across branches
L("P", "CONTROL.FAILURE", "SUBSET.FAILURE", "requires", None, [S("SUBSET", "P", 1, "flipped")],
  "direction: the sentence makes CONTROL the dependent")
L("P", "SUBSET.VISIBLE", "CONTRACTS.BOUNDARY", "requires",
  "What an expression does follows from the declared kind of its operands; for data from outside, that kind is established by parsing at the boundary.",
  [S("SUBSET", "P", 2, "retargeted")], "sentence sharpened to a dependency")
L("P", "SUBSET.MATURITY", "DEPENDENCIES.ADMISSION.2", "requires", None, [S("SUBSET", "P", 3, "retargeted")])
L("P", "DEFENSE", "CONTRACTS.BOUNDARY.1", "requires", None, [S("CONTRACTS", "P", "P1", "flipped")],
  "direction: the sentence makes DEFENSE the dependent")
L("P", "DEFENSE.INJECTION", "CONTRACTS.BOUNDARY.2", "refines", None, [S("CONTRACTS", "P", "P2", "flipped")],
  "direction: the allowlist stance specializes positive validation")
L("P", "CONTRACTS.STATIC.1", "VERIFICATION.ENFORCEMENT", "requires", None, [S("CONTRACTS", "P", "P3", "retargeted")])
L("P", "CONTRACTS.SHAPE", "STRUCTURE.NAMING", "refines", None, [S("CONTRACTS", "P", "P4", "retargeted")])
L("P", "STRUCTURE.STATE.2", "SUBSET.STATE", "requires", None, [S("STRUCTURE", "P", 1, "retargeted")])
L("P", "DEPENDENCIES.TRUST.1", "DEFENSE.INJECTION", "requires", None, [S("DEPENDENCIES", "P", 1, "retargeted")])
L("P", "DEPENDENCIES.TRUST.2", "DEFENSE.HOST", "requires", None, [S("DEPENDENCIES", "P", 2, "retargeted")])
L("P", "DEPENDENCIES.ADMISSION.4", "DEFENSE.DOM.1", "requires", None, [S("DEPENDENCIES", "P", 3, "retargeted")])
L("P", "VERIFICATION.ENFORCEMENT", "DEPENDENCIES.CHANGE.1", "requires", None, [S("VERIFICATION", "P", 1, "retargeted")])
L("P", "SUBSET", "VERIFICATION.STATIC_BASELINE.1", "dataflow",
  "SUBSET defines the safe subset; the linter that is switched on is the mechanism that enforces it.",
  [S("VERIFICATION", "P", 2, "flipped")], "direction: SUBSET produces the rules the linter consumes")
L("P", "CONTRACTS.STATIC.2", "VERIFICATION.STATIC_BASELINE.3", "refines",
  "A passing type check is evidence, not proof: the type layer is the instance of the rule that several kinds of check run together and none is the only mechanism.",
  [], "added at integration (P5 link between two statements of one idea)")
L("P", "DEFENSE.HOST.1", "CONTROL.SCHEDULING", "requires",
  "The single shared thread that makes one request able to stall the process is stated once, in CONTROL.SCHEDULING; this node adds that untrusted input must not control the cost.",
  [], "added at integration (P5 link, the premise is not restated)")

# --- defaults graph, across branches
D = "D"
L(D, "PIG-JS.STRUCTURE.FORMAT.1", "PIG-JS.SUBSET.STRICTNESS.2", "requires",
  "The module-format rules presuppose that ES modules are the chosen format, which SUBSET decides; cycles, side-effect-free imports and the Node ESM facts build on ES modules as the unit.",
  [S("SUBSET", D, 1, "flipped"), S("STRUCTURE", D, 1, "merged")], "direction: STRUCTURE builds on SUBSET")
L(D, "PIG-JS.STRUCTURE.LOADING.1", "PIG-JS.SUBSET.STRICTNESS.2", "refines",
  "A module runs once however often it is imported (stated at SUBSET.STRICTNESS.2); the import-order rule builds on that fact and adds the rule to export a function for repeatable work.",
  [S("STRUCTURE", D, 9, "retargeted")], "P5 link: the run-once fact is held once")
L(D, "PIG-JS.SUBSET.STRICTNESS", "PIG-JS.VERIFICATION.LINT.1.1", "requires",
  "no-var and prefer-const are lint rules written in the lint configuration; that is what enforces fixed, block-scoped bindings.",
  [S("SUBSET", D, 2, "retargeted"), S("VERIFICATION", D, 1, "merged")])
L(D, "PIG-JS.SUBSET.CONVERSION", "PIG-JS.VERIFICATION.LINT.1.1", "requires",
  "eqeqeq and no-implicit-coercion are the lint rules, written in the lint configuration, that enforce the conversion rules.",
  [S("SUBSET", D, 3, "retargeted")])
L(D, "PIG-JS.SUBSET.CONVERSION.5", "PIG-JS.CONTRACTS.BOUNDARY", "requires", None, [S("SUBSET", D, 4, "retargeted")])
L(D, "PIG-JS.SUBSET.CONVERSION.6", "PIG-JS.CONTRACTS.MODEL.3", "requires",
  "Optional chaining is used only on values whose type can really be nullish; the rule and its type condition live in CONTRACTS.MODEL.3.",
  [S("SUBSET", D, 5, "retargeted"), S("CONTRACTS", D, "Q8", "merged")])
L(D, "PIG-JS.SUBSET.NUMBERS.4", "PIG-JS.CONTRACTS.BOUNDARY.1", "dataflow", None, [S("SUBSET", D, 6, "retargeted")])
L(D, "PIG-JS.SUBSET.NUMBERS.4", "PIG-JS.DEFENSE.PROTOTYPE.2", "requires", None, [S("SUBSET", D, 7, "retargeted")])
L(D, "PIG-JS.STRUCTURE.SURFACE.3", "PIG-JS.SUBSET.MUTATION.1", "requires",
  "Freezing is shallow, so a frozen exported object still has mutable nested state; the freeze mechanics are owned by SUBSET and this rule builds read-only exports on them.",
  [S("STRUCTURE", D, 6, "retargeted"), S("SUBSET", D, 8, "flipped"), S("STRUCTURE", D, 7, "merged")],
  "freeze hub: three nodes share the shallow-freeze fact, which is held once at MUTATION.1")
L(D, "PIG-JS.DEFENSE.PROTOTYPE.3", "PIG-JS.SUBSET.MUTATION.1", "requires",
  "Freezing application configuration as a hardening step inherits the shallow-freeze limit stated at SUBSET.MUTATION.1.",
  [S("SUBSET", D, 9, "flipped"), S("DEFENSE", D, 3, "merged")], "freeze hub")
L(D, "PIG-JS.SUBSET.OBJECTS.5", "PIG-JS.DEFENSE.PROTOTYPE.3", "conflicts",
  "Freezing or locking down built-ins as hardening is the sanctioned exception to leaving built-ins alone; scope (high-sensitivity, tested environments) separates the two.",
  [S("SUBSET", D, 10, "retargeted"), S("DEFENSE", D, 2, "merged")])
L(D, "PIG-JS.SUBSET.OBJECTS.5", "PIG-JS.RUNTIME.MEASURE.2", "requires", None, [S("SUBSET", D, 11, "retargeted")])
L(D, "PIG-JS.DEFENSE.PROTOTYPE.1", "PIG-JS.SUBSET.OBJECTS.6", "requires",
  "The own-property read for untrusted keys is the rule of SUBSET.OBJECTS.6 (merged row SUBSET-051); this node holds the pollution writes, merges and __proto__.",
  [S("SUBSET", D, 12, "flipped"), S("DEFENSE", D, 1, "merged")], "P5 merge: the rule lives on OBJECTS.6")
L(D, "PIG-JS.SUBSET.EVOLUTION.5", "PIG-JS.VERIFICATION.FORMAT.1", "requires", None, [S("SUBSET", D, 13, "retargeted")])
L(D, "PIG-JS.SUBSET.EVOLUTION.1", "PIG-JS.DEPENDENCIES.UPDATE.2", "requires", None, [S("SUBSET", D, 14, "retargeted")])
L(D, "PIG-JS.CONTRACTS.LAYER.3", "PIG-JS.VERIFICATION.LINT.2", "requires", None, [S("CONTRACTS", D, "Q1", "retargeted")],
  "VERIFICATION defaults hold no tool-neutral gate node; LINT.2 (exit status blocks CI) stands in")
L(D, "PIG-JS.CONTRACTS.ESCAPE.2", "PIG-JS.VERIFICATION.LINT.1.4", "requires", None, [S("CONTRACTS", D, "Q2", "retargeted")])
L(D, "PIG-JS.CONTRACTS.ESCAPE.6", "PIG-JS.VERIFICATION.LINT.2.3", "requires", None, [S("CONTRACTS", D, "Q3", "retargeted")])
L(D, "PIG-JS.CONTRACTS.STRICT.4", "PIG-JS.DEPENDENCIES.UPDATE.2", "requires", None, [S("CONTRACTS", D, "Q4", "retargeted")])
L(D, "PIG-JS.CONTRACTS.LAYER.6", "PIG-JS.STRUCTURE.FORMAT", "refines", None, [S("CONTRACTS", D, "Q5", "retargeted")])
L(D, "PIG-JS.CONTRACTS.LAYER.4", "PIG-JS.SUBSET.EVOLUTION", "refines",
  "The erasable-syntax rule excludes enum and namespaces; SUBSET.EVOLUTION holds the general rule that new code uses only settled features and no legacy syntax (SUBSET lists neither enum nor namespaces).",
  [S("CONTRACTS", D, "Q6", "retargeted")], "sentence corrected: the proposal said SUBSET lists enum and namespaces, it does not")
L(D, "PIG-JS.CONTRACTS.MODEL.2", "PIG-JS.SUBSET.CONVERSION", "refines", None, [S("CONTRACTS", D, "Q7", "retargeted")])
L(D, "PIG-JS.CONTRACTS.BOUNDARY.1", "PIG-JS.CONTROL.ERRORS.2", "requires", None, [S("CONTRACTS", D, "Q10", "retargeted")])
L(D, "PIG-JS.CONTRACTS.BOUNDARY.1", "PIG-JS.DEFENSE.PROTOTYPE.2", "dataflow",
  "A parsed object with an own __proto__ key is harmless until merged; the parse result flows to the hostile-key rules, which treat parsed JSON keys as untrusted.",
  [S("CONTRACTS", D, "Q11", "retyped")], "type refines -> dataflow")
L(D, "PIG-JS.CONTRACTS.BOUNDARY.2", "PIG-JS.DEFENSE.PROTOTYPE.1", "dataflow",
  "The schema allowlist is the first defence against prototype pollution: only declared keys reach the merge and lookup code that PROTOTYPE.1 guards.",
  [S("CONTRACTS", D, "Q12", "retyped")], "type requires -> dataflow")
L(D, "PIG-JS.CONTRACTS.BOUNDARY.3", "PIG-JS.DEFENSE.PROTOTYPE.1", "refines",
  "Binding request data to a dedicated allowlisted object is the key-write control against mass assignment, an untrusted-key hazard beside pollution; DEFENSE has no separate mass-assignment node.",
  [S("CONTRACTS", D, "Q13", "retargeted")], "the proposal named a DEFENSE injection class that DEFENSE does not list")
L(D, "PIG-JS.DEFENSE.INJECTION", "PIG-JS.CONTRACTS.BOUNDARY.4", "requires",
  "Allowlisted input validated before it reaches Node or language APIs underlies the command and path rules.",
  [S("CONTRACTS", D, "Q14", "flipped")], "split in two: INJECTION and HOST.4")
L(D, "PIG-JS.DEFENSE.HOST.4", "PIG-JS.CONTRACTS.BOUNDARY.4", "requires",
  "Allowlisted input validated before it reaches Node or language APIs underlies the regex input bounds.",
  [S("CONTRACTS", D, "Q14", "merged")])
L(D, "PIG-JS.CONTROL.PROMISES.3", "PIG-JS.VERIFICATION.LINT.1.4", "requires",
  "Type-aware lint rules that report floating and misused promises are what enforce these rules (rule documents are cited as positions only).",
  [S("CONTROL", D, 1, "retargeted"), S("VERIFICATION", D, 3, "merged")])
L(D, "PIG-JS.CONTROL.ERRORS.2", "PIG-JS.CONTRACTS.STRICT.1", "requires", None, [S("CONTROL", D, 2, "retargeted")])
L(D, "PIG-JS.CONTROL.SCHEDULING.2", "PIG-JS.DEFENSE.HOST", "dataflow", None, [S("CONTROL", D, 3, "retargeted")])
L(D, "PIG-JS.CONTROL.BOUNDS.2", "PIG-JS.DEFENSE.HOST", "dataflow", None, [S("CONTROL", D, 4, "retargeted")])
L(D, "PIG-JS.CONTROL.FLOW", "PIG-JS.RUNTIME.MEMORY", "dataflow", None, [S("CONTROL", D, 5, "retargeted")])
L(D, "PIG-JS.CONTROL.PROMISES.5", "PIG-JS.SUBSET.EVOLUTION.1", "dataflow", None, [S("CONTROL", D, 7, "retargeted")])
L(D, "PIG-JS.CONTROL.BOUNDS.1", "PIG-JS.CONTRACTS.SIGNATURE", "requires", None, [S("CONTROL", D, 8, "retargeted")],
  "retargeted from STRUCTURE: the API-shape cluster (STRUCT-C48 to C52) was routed to CONTRACTS.SIGNATURE")
L(D, "PIG-JS.STRUCTURE.FORMAT.3", "PIG-JS.CONTRACTS.LAYER.5", "requires", None, [S("STRUCTURE", D, 2, "retargeted")])
L(D, "PIG-JS.STRUCTURE.FORMAT.4", "PIG-JS.CONTRACTS.LAYER.4", "requires", None, [S("STRUCTURE", D, 3, "retargeted")])
L(D, "PIG-JS.STRUCTURE.NODE.1", "PIG-JS.CONTRACTS.LAYER.5", "requires", None, [S("STRUCTURE", D, 4, "retargeted")])
L(D, "PIG-JS.STRUCTURE.SURFACE.5", "PIG-JS.SUBSET.OBJECTS", "requires", None, [S("STRUCTURE", D, 8, "retargeted")])
L(D, "PIG-JS.STRUCTURE.LOADING.4", "PIG-JS.CONTROL.PROCESS", "requires", None, [S("STRUCTURE", D, 10, "retargeted")])
L(D, "PIG-JS.STRUCTURE.LOADING.5", "PIG-JS.VERIFICATION.LINT.2", "requires", None, [S("STRUCTURE", D, 11, "retargeted")],
  "coarse target: VERIFICATION defaults have no build-gate node")
L(D, "PIG-JS.STRUCTURE.DIRECTION.2", "PIG-JS.VERIFICATION.LINT.2", "requires", None, [S("STRUCTURE", D, 12, "retargeted")])
L(D, "PIG-JS.STRUCTURE.DIRECTION.3", "PIG-JS.VERIFICATION.LINT.2", "requires", None, [S("STRUCTURE", D, 13, "retargeted")])
L(D, "PIG-JS.STRUCTURE.PACKAGE.1", "PIG-JS.DEPENDENCIES.PUBLISH", "requires", None, [S("STRUCTURE", D, 14, "retargeted")])
L(D, "PIG-JS.STRUCTURE.LOADING.6", "PIG-JS.RUNTIME.MEASURE.2", "requires",
  "The barrel rule is motivated by load cost and rests on one synthetic measurement; a structure rule motivated by speed needs the measurement gate of RUNTIME.",
  [S("RUNTIME", D, 1, "retargeted")], "the proposal named no STRUCTURE node; LOADING.6 is the speed-motivated one")
L(D, "PIG-JS.DEFENSE.PROTOTYPE.3", "PIG-JS.DEPENDENCIES.UPDATE", "requires", None, [S("DEFENSE", D, 4, "retargeted")])
L(D, "PIG-JS.DEFENSE.INJECTION.1.1", "PIG-JS.VERIFICATION.LINT.1", "requires", None, [S("DEFENSE", D, 5, "retargeted")])
L(D, "PIG-JS.DEFENSE.SECRETS.5", "PIG-JS.VERIFICATION.LINT.2", "requires", None, [S("DEFENSE", D, 6, "retargeted")],
  "coarse target: VERIFICATION defaults have no secret-scan gate node")
L(D, "PIG-JS.DEPENDENCIES.PUBLISH.2", "PIG-JS.DEFENSE.SECRETS.5", "requires",
  "Secrets in published package contents are the leak class that the secret-handling rules of DEFENSE govern.",
  [S("DEPENDENCIES", D, 9, "retargeted"), S("DEFENSE", D, 7, "flipped")])
L(D, "PIG-JS.DEFENSE.HOST.4", "PIG-JS.CONTROL.SCHEDULING.2", "requires", None, [S("DEFENSE", D, 10, "retargeted")])
L(D, "PIG-JS.DEFENSE.HOST.5", "PIG-JS.CONTRACTS.BOUNDARY", "refines", None, [S("DEFENSE", D, 11, "retargeted")])
L(D, "PIG-JS.DEFENSE.HOST.6", "PIG-JS.DEPENDENCIES.INSTALL", "requires", None, [S("DEFENSE", D, 12, "retargeted")])
L(D, "PIG-JS.DEFENSE.INJECTION.4.3", "PIG-JS.CONTROL.ERRORS.2", "requires", None, [S("DEFENSE", D, 13, "retargeted")])
L(D, "PIG-JS.DEFENSE.INJECTION.5", "PIG-JS.CONTRACTS.BOUNDARY", "requires", None, [S("DEFENSE", D, 14, "retargeted")])
L(D, "PIG-JS.DEFENSE.DOM.6", "PIG-JS.DEPENDENCIES.FRAMEWORK_EVIDENCE", "dataflow",
  "Framework security facts recorded in DEFENSE (escape hatches, default encoding, htmx hardening) feed the framework evidence in DEPENDENCIES; they are held once, here.",
  [S("DEFENSE", D, 15, "retargeted")], "P5 link: framework security facts held once, in DEFENSE")
L(D, "PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST", "PIG-JS.DEFENSE.DOM.6", "requires",
  "Gate B of the short list, a documented security model, cites the per-framework facts held in DEFENSE.DOM.6 and does not restate them.",
  [S("DEPENDENCIES", D, 10, "retargeted")], "P5 link: framework security facts held once, in DEFENSE")
L(D, "PIG-JS.DEPENDENCIES.UPDATE.3", "PIG-JS.VERIFICATION.LINT.2", "dataflow", None, [S("DEPENDENCIES", D, 5, "retargeted")],
  "coarse target: VERIFICATION defaults have no tool-neutral gate node")
L(D, "PIG-JS.VERIFICATION.LINT.2", "PIG-JS.DEPENDENCIES.INSTALL.1", "requires",
  "The CI job that runs the gate installs dependencies by the frozen-install rule of DEPENDENCIES.",
  [S("VERIFICATION", D, 6, "retargeted"), S("DEPENDENCIES", D, 4, "merged")])
L(D, "PIG-JS.DEPENDENCIES.PUBLISH.3", "PIG-JS.CONTRACTS.LAYER.1", "requires", None, [S("DEPENDENCIES", D, 8, "retargeted")])
L(D, "PIG-JS.DEPENDENCIES.FRAMEWORK_SHORTLIST", "PIG-JS.CONTRACTS.LAYER.1", "requires", None,
  [S("DEPENDENCIES", D, 11, "retargeted")])
L(D, "PIG-JS.VERIFICATION.LINT.1.4", "PIG-JS.CONTRACTS.LAYER.1", "requires", None, [S("VERIFICATION", D, 2, "retargeted")])
L(D, "PIG-JS.VERIFICATION.LINT.3", "PIG-JS.DEFENSE.INJECTION.1", "dataflow", None, [S("VERIFICATION", D, 4, "retargeted")])
L(D, "PIG-JS.VERIFICATION.TESTS.2", "PIG-JS.SUBSET.CONVERSION.1", "refines", None, [S("VERIFICATION", D, 5, "retargeted")])
L(D, "PIG-JS.RUNTIME.MEASURE.3", "PIG-JS.CONTROL.PROMISES.6", "refines", None, [S("RUNTIME", D, 2, "retargeted")])
L(D, "PIG-JS.RUNTIME.DIAGNOSE.2", "PIG-JS.CONTROL.SCHEDULING.2", "dataflow", None, [S("RUNTIME", D, 3, "retargeted")])
L(D, "PIG-JS.RUNTIME.MEMORY.4", "PIG-JS.DEFENSE.HOST.2", "requires", None, [S("RUNTIME", D, 4, "retargeted")])
L(D, "PIG-JS.RUNTIME.MEMORY.5", "PIG-JS.SUBSET.EVOLUTION", "refines", None, [S("RUNTIME", D, 5, "retargeted")])
L(D, "PIG-JS.RUNTIME.MEMORY.2", "PIG-JS.CONTROL.ERRORS.4", "requires", None, [S("RUNTIME", D, 6, "retargeted")])

# defaults -> philosophy of another branch (inter links), from proposals or added at integration
INTER_EXTRA = [
    dict(frm="PIG-JS.DEFENSE.HOST.1", to="js-philosophy:DEPENDENCIES.TRUST.2", type="refines", sentence=None,
         srcs=[S("DEFENSE", D, 9, "retargeted")], note="no defaults node holds the trust principle; target is the philosophy node"),
    dict(frm="PIG-JS.DEPENDENCIES.SCREEN.1", to="js-philosophy:VERIFICATION.ENFORCEMENT", type="requires", sentence=None,
         srcs=[S("DEPENDENCIES", D, 6, "retargeted")], note="Scorecard checks overlap the merge gate"),
    dict(frm="PIG-JS.CONTROL.PROCESS.2", to="js-philosophy:CONTROL.LIFECYCLE", type="refines",
         sentence="Node's uncaughtException and uncaughtExceptionMonitor hooks render the designed process end; the principle and its single evidence row (CONTROL-078) are held once.",
         srcs=[], note="added at integration (P5 merge link)"),
]

# proposals that become planned boundary links, and proposals dropped (reason)
PLANNED_FROM_PROPOSALS = {
    ("CONTRACTS", "P", "P5"): ("CONTRACTS.BOUNDARY.1", "web-app-philosophy",
                               "server-side authority for validation is architecture owned by the web-architecture guideline (row CONTRACTS-006, deferred)"),
    ("CONTROL", "D", "6"): ("PIG-JS.CONTROL.PROCESS.4", "pig-web-defaults",
                            "the Node side of shutdown (signal listener, server close) and the external supervisor of PROCESS.2 serve the shutdown contract that the web-architecture guideline owns"),
}
DROPS = {
    ("CONTRACTS", "D", "Q9"): "moot: function and object API design is owned by CONTRACTS (target hierarchy), so SIGNATURE has no STRUCTURE counterpart to link to",
    ("STRUCTURE", "P", "2"): "no philosophy node of DEFENSE states a freeze or hardening principle; the defaults freeze hub (SUBSET.MUTATION.1) carries it",
    ("STRUCTURE", "P", "3"): "no philosophy node of SUBSET states the module run-once fact; the defaults link STRUCTURE.LOADING.1 to SUBSET.STRICTNESS.2 carries it",
    ("STRUCTURE", "D", "5"): "no CONTRACTS node states export visibility; the rule stays in STRUCTURE.SURFACE.2",
    ("DEFENSE", "D", "8"): "moot: the allocUnsafe claim (RUNTIME-C13) is placed in DEFENSE (row DEFENSE-117); RUNTIME holds no node on it",
    ("DEPENDENCIES", "D", "7"): "moot: no RUNTIME node holds Node release lifecycle; the fact sits in PIG-JS.DEPENDENCIES.UPDATE.2",
}
# mirror proposals folded into another link (counted under 'merged' via the LINKS sources above)


# ----------------------------------------------------------------------------- output builders
def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return out


def main() -> int:
    errors = []
    ledger_rows, by_branch, merged_log, n_in_rows = build_ledger()
    nodes, order = read_nodes()
    inner, inter_dp, inter_py, proposals, planned = read_links()

    # node rows derived from the merged ledger
    node_rows = defaultdict(list)
    for r in ledger_rows:
        node_rows[r["node"]].append(r["row"])
    # check the branch skeletons' own ledger-rows columns against the ledger (before merges)
    orig_rows = defaultdict(set)
    for b in ORDER:
        for r in by_branch[b]:
            orig_rows[r["node"]].add(r["row"])
    mismatches = []
    for g in nodes:
        for uid, n in nodes[g].items():
            col = n["orig_rows"]
            ids = set(re.findall(r"\b[A-Z]+-\d{3}\b", col))
            if not ids and col != "-":
                # bare numbers and ranges (DEFENSE)
                for a, z in re.findall(r"(\d{3})-(\d{3})", col):
                    ids |= {f"{n['branch']}-{k:03d}" for k in range(int(a), int(z) + 1)}
                ids |= {f"{n['branch']}-{x}" for x in re.findall(r"(?<![\d-])(\d{3})(?![\d-])", col)}
            ids = {i for i in ids}
            main_ids = ids if n["branch"] != "RUNTIME" else {i for i in ids if i in orig_rows[uid]}
            if main_ids != orig_rows[uid]:
                mismatches.append((uid, sorted(main_ids ^ orig_rows[uid])))
    # apply node edits
    for g in nodes:
        for uid, n in nodes[g].items():
            e = NODE_EDITS.get(uid, {})
            if "intent" in e:
                n["intent"] = e["intent"]
            if "epistemic" in e:
                n["epistemic"] = e["epistemic"]
            if "epistemic_replace" in e:
                a, z = e["epistemic_replace"]
                assert a in n["epistemic"], uid
                n["epistemic"] = n["epistemic"].replace(a, z)
    t3_log = []
    for uid in T3_RELABEL:
        g = "D" if is_def(uid) else "P"
        ep = nodes[g][uid]["epistemic"]
        assert ep.startswith("known \\| unvalidated: single T3 source"), (uid, ep)
        nodes[g][uid]["epistemic"] = "risky" + ep[len("known"):]
        t3_log.append(uid)

    # ---------------- claims_ledger.md
    n_claims = sum(len(CID.findall(r["claim_ids"])) for r in ledger_rows)
    n_with_claims = sum(1 for r in ledger_rows if CID.findall(r["claim_ids"]))
    led = ["# Claims ledger (stage 5c)", "",
           "All eight branch ledgers in branch order (SUBSET, CONTRACTS, CONTROL, STRUCTURE, DEFENSE, DEPENDENCIES,",
           "VERIFICATION, RUNTIME), one table, one row per statement. Every claim of the stage-3 tables is placed exactly",
           "once (`python3 build/distill/check_ledger.py`).", "",
           "Conventions kept from the branches: `role` is `decision`, `acceptable-when`, `rejected`, `fact` or `deferred`;",
           "a claim-less `rejected` folklore row carries `-` as claim_ids and names its refuting row in the statement; a node",
           "may hold several decision rows; the row prefix names the branch that wrote it.", "",
           "Integration merges (two rows folded into another, all claim ids kept, nothing dropped):", ""]
    for m in merged_log:
        led.append(f"- `{m['survivor']}` absorbs `{m['absorbed']}` (claims {m['claim_ids']}): {m['why']}.")
    led += ["", f"Rows: {len(ledger_rows)} ({n_with_claims} carry {n_claims} claim ids, {len(ledger_rows) - n_with_claims} are claim-less folklore rows).", ""]
    led += table(LEDGER_COLS, [[r[c] for c in LEDGER_COLS] for r in ledger_rows])
    (DISTILL / "claims_ledger.md").write_text("\n".join(led) + "\n")

    # ---------------- skeleton.md
    sk = ["# Skeleton (stage 5c): js-philosophy and pig-js-defaults", "",
          "Both graphs of the JavaScript guideline, assembled from the eight branch skeletons: the two roots first, then the",
          "eight branch subtrees (each breadth-first, the L1 node first), then the intentlinks, the inter links, the planned",
          "boundary links and the judge records. Node columns: `| uid | name | intent | epistemic_state | ledger rows |`.", "",
          "Conventions:", "",
          "- Epistemic cells write the IG multi-issue separator as `\\|`; the `ledger rows` column is derived from `claims_ledger.md`.",
          "- A node with `-` in `ledger rows` rolls up its children (or is an undecided placeholder).",
          "- Cross-branch links were proposals naming a branch keyword; they are resolved to uids here and their provenance is",
          "  in `5c_integrate/link_resolution.md`. Link ids are plain numbers, restarted per table.",
          "- Links to the web-architecture graphs are planned, not created: those graphs do not exist yet.",
          "- Nodes relabelled `risky` (decision on one T3 source): " + ", ".join(f"`{u}`" for u in t3_log) + ".", ""]

    counts = {"P": defaultdict(int), "D": defaultdict(int)}
    branch_counts = {}

    def emit_nodes(g, uids, root=None):
        rows = []
        for u in uids:
            n = nodes[g][u] if u not in ("ROOT", "PIG-JS.ROOT") else root
            r = n.get("rows") if u in ("ROOT", "PIG-JS.ROOT") else (", ".join(node_rows.get(u, [])) or "-")
            ep = n["epistemic"] if "epistemic" in n else "known"
            rows.append([u, n["name"], n["intent"], esc(ep) if "\\|" not in ep else ep, r])
        return table(["uid", "name", "intent", "epistemic_state", "ledger rows"], rows)

    for g, gname, root in (("P", "js-philosophy", ROOT_P), ("D", "pig-js-defaults", ROOT_D)):
        sk += [f"## Graph {gname}", "", "### Root", ""]
        sk += emit_nodes(g, [root["uid"]], root) + [""]
        for b in ORDER:
            uids = bfs(nodes[g], order[g], b)
            branch_counts[(g, b)] = {d: sum(1 for u in uids if depth(u) == d) for d in range(1, 6)}
            sk += [f"### {('PIG-JS.' if g == 'D' else '') + b}", ""]
            sk += emit_nodes(g, uids) + [""]
            for u in uids:
                counts[g][depth(u)] += 1
        counts[g][0] = 1

        # intentlinks inside branches
        sk += [f"### Intentlinks inside {gname}: within branches", ""]
        rows = []
        for i, (b, frm, to, typ, sent) in enumerate(inner[g], 1):
            for u in (frm, to):
                if u not in nodes[g]:
                    errors.append(f"link endpoint {u} not a node ({b})")
            rows.append([str(i), frm, to, typ, esc(sent)])
        sk += table(["#", "from", "to", "type", "sentence"], rows) + [""]
        inner_n = len(rows)

        sk += [f"### Intentlinks inside {gname}: across branches (resolved from proposals)", ""]
        rows = []
        for i, lk in enumerate([x for x in LINKS if x["graph"] == g], 1):
            sent = lk["sentence"]
            if sent is None:
                first = lk["srcs"][0]
                sent = proposals[(first[0], first[1], first[2])]["sentence"]
            for u in (lk["frm"], lk["to"]):
                if u not in nodes[g]:
                    errors.append(f"resolved link endpoint {u} not a node")
            lk["_sentence"] = sent
            rows.append([str(i), lk["frm"], lk["to"], lk["type"], esc(sent)])
        sk += table(["#", "from", "to", "type", "sentence"], rows) + [""]
        cross_n = len(rows)
        counts[g]["links_inner"], counts[g]["links_cross"] = inner_n, cross_n

        if g == "P":
            sk += ["### Inter links from js-philosophy to python-kb-philosophy", "",
                   "Target file `../python_guidelines/intent_graphs/python_kb_philosophy.yaml`; the uids were read there.", ""]
            rows = []
            for i, (b, frm, to, typ, sent) in enumerate(inter_py, 1):
                if frm not in nodes["P"]:
                    errors.append(f"python link from {frm}")
                rows.append([str(i), frm, to, typ, esc(sent)])
            sk += table(["#", "from", "to", "type", "sentence"], rows) + [""]
            counts["P"]["links_python"] = len(rows)
        else:
            sk += ["### Inter links from pig-js-defaults to js-philosophy", "",
                   "Within a branch (each defaults node to the principle it renders), then across branches.", ""]
            rows = []
            for i, (b, frm, to, typ, sent) in enumerate(inter_dp, 1):
                if frm not in nodes["D"] or to.split(":", 1)[1] not in nodes["P"]:
                    errors.append(f"inter link {frm} -> {to}")
                rows.append([str(i), frm, to, typ, esc(sent)])
            k = len(rows)
            for j, x in enumerate(INTER_EXTRA, k + 1):
                sent = x["sentence"]
                if sent is None:
                    first = x["srcs"][0]
                    sent = proposals[(first[0], first[1], first[2])]["sentence"]
                x["_sentence"] = sent
                if x["frm"] not in nodes["D"] or x["to"].split(":", 1)[1] not in nodes["P"]:
                    errors.append(f"inter extra {x['frm']} -> {x['to']}")
                rows.append([str(j), x["frm"], x["to"], x["type"], esc(sent)])
            sk += table(["#", "from", "to", "type", "sentence"], rows) + [""]
            counts["D"]["links_inter"], counts["D"]["links_inter_within"] = len(rows), k

    # planned boundary links
    sk += ["## Planned boundary links to the web-architecture graphs (planned, not created)", "",
           "The target graphs `web-app-philosophy` and `pig-web-defaults` of `../web_architecture_guidelines/` do not exist yet;",
           "target uids are chosen when they do. Each row is a claim or rule that the web-architecture guideline owns.", ""]
    rows = []
    for b, frm, note in planned:
        tgt = "pig-web-defaults" if is_def(frm) else "web-app-philosophy"
        rows.append([str(len(rows) + 1), frm, tgt, esc(note)])
    for key, (frm, tgt, note) in PLANNED_FROM_PROPOSALS.items():
        rows.append([str(len(rows) + 1), frm, tgt, note])
    for r in rows:
        if r[1] not in nodes["P"] and r[1] not in nodes["D"]:
            errors.append(f"planned link from {r[1]}")
    sk += table(["#", "from", "to graph", "content owned there"], rows) + [""]
    counts["planned"] = len(rows)

    # judge records
    sk += ["## Judge records", "",
           "One record per defaults node holding a decision, as written by the branches (positions, forces, decision, rejected",
           "with the condition under which each would win). Layouts differ by branch and are kept. Integration notes are marked.", ""]
    jr_counts = {}
    for b in ORDER:
        text = (BR / b / "skeleton.md").read_text().splitlines()
        start = next(i for i, l in enumerate(text) if l.startswith("## Judge records"))
        body = text[start + 1:]
        body = [("#" + l if l.startswith("###") else l) for l in body]
        sk += [f"### {b}"] + body + [""]
        if b == "CONTROL":
            sk += ["Integration note (CONTROL): the claims ASYNC-C05 and RUNTIME-C37 sit in one merged row, CONTROL-078, on "
                   "PIG-JS.CONTROL.PROCESS.2; the principle is held by CONTROL.LIFECYCLE.", ""]
        if b == "SUBSET":
            sk += ["Integration note (SUBSET): the claim RUNSEC-C07 sits in the merged row SUBSET-051 on PIG-JS.SUBSET.OBJECTS.6 "
                   "(own-property reads, one rule for all keys); the node PIG-JS.DEFENSE.PROTOTYPE.1 links to it.", ""]
        if b == "DEFENSE":
            sk += ["Integration note (DEFENSE): in the record of PIG-JS.DEFENSE.PROTOTYPE.1 the claim RUNSEC-C07 (Object.hasOwn) "
                   "is held by PIG-JS.SUBSET.OBJECTS.6; the decision text above stays as the branch wrote it.", ""]
        jr_counts[b] = len(re.findall(r"^\*\*PIG-JS|^#### PIG-JS|^\| PIG-JS", "\n".join(body), re.M))
    (DISTILL / "skeleton.md").write_text("\n".join(sk) + "\n")

    # ---------------- link_resolution.md
    lr = ["# Cross-branch link resolution (stage 5c)", "",
          "Every proposal of the eight branch skeletons, with its disposition. `how`: given (kept), flipped (direction reversed to",
          "match the sentence), retargeted (branch keyword resolved to a uid), retyped (type changed), merged (a mirror proposal",
          "folded into another link), dropped (reason), planned (boundary link to the web-architecture graphs).", "",
          "| branch | graph | proposal | proposed from | proposed to | proposed type | disposition |", "|---|---|---|---|---|---|---|"]
    disp = {}
    for li, lk in enumerate(LINKS):
        for (b, g, i, how) in lk["srcs"]:
            disp.setdefault((b, g, i), []).append((how, f"{lk['frm']} {lk['type']} {lk['to']}"))
    for x in INTER_EXTRA:
        for (b, g, i, how) in x["srcs"]:
            disp.setdefault((b, g, i), []).append((how, f"{x['frm']} {x['type']} {x['to']}"))
    for key, (frm, tgt, note) in PLANNED_FROM_PROPOSALS.items():
        disp.setdefault(key, []).append(("planned", f"{frm} -> {tgt}"))
    for key, why in DROPS.items():
        disp.setdefault(key, []).append(("dropped", why))
    unaccounted = [k for k in proposals if k not in disp]
    unknown = [k for k in disp if k not in proposals]
    if unaccounted:
        errors.append(f"proposals not accounted for: {unaccounted}")
    if unknown:
        errors.append(f"dispositions for unknown proposals: {unknown}")
    how_count = defaultdict(int)
    for key in sorted(proposals, key=lambda k: (ORDER.index(k[0]), k[1], int(re.sub(r'\D', '', k[2]) or 0))):
        p = proposals[key]
        ds = disp.get(key, [])
        hows = [h for h, _ in ds]
        main = ("dropped" if "dropped" in hows else "planned" if "planned" in hows else
                "merged" if hows and all(h == "merged" for h in hows) else
                next((h for h in hows if h != "merged"), "?"))
        how_count[main] += 1
        lr.append(f"| {key[0]} | {'defaults' if key[1] == 'D' else 'philosophy'} | {p['idx']} | {p['frm'].replace('PIG-JS.', '')} | {p['to']} | {p['type']} | "
                  + "; ".join(f"{h}: {t}" for h, t in ds) + " |")
    lr += ["", "Links added at integration, not proposed by a branch: "
           + "; ".join(f"{lk['frm']} {lk['type']} {lk['to']}" for lk in LINKS if not lk["srcs"])
           + "; " + "; ".join(f"{x['frm']} {x['type']} {x['to']}" for x in INTER_EXTRA if not x["srcs"]) + ".", ""]
    notes = [lk for lk in LINKS if lk["note"]] + [x for x in INTER_EXTRA if x["note"]]
    lr += ["Notes on individual resolutions:", ""]
    for lk in notes:
        frm = lk["frm"]
        lr.append(f"- `{frm}` {lk['type']} `{lk['to']}`: {lk['note']}")
    (HERE / "link_resolution.md").write_text("\n".join(lr) + "\n")

    # ---------------- decisions_for_review.md
    def demote(lines, prefix, by=2):
        out = []
        for l in lines:
            m = re.match(r"^(#+)\s+(.*)$", l)
            if m:
                out.append("#" * (len(m.group(1)) + by) + " " + prefix + ": " + m.group(2))
            else:
                out.append(l)
        return out

    dec_by, und_by = {}, {}
    for b in ORDER:
        lines = (BR / b / "decisions.md").read_text().splitlines()
        lines = [l for i, l in enumerate(lines) if not (i == 0 and l.startswith("# "))]
        und_start = next((i for i, l in enumerate(lines) if re.match(r"^## (C\. )?Undecided", l)), None)
        if und_start is None:
            dec_by[b], und_by[b] = lines, []
            continue
        und_end = next((i for i in range(und_start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        und_by[b] = lines[und_start:und_end]
        dec_by[b] = lines[:und_start] + lines[und_end:]
    dr = ["# Decisions for review (stage 5c)", "",
          "The maintainer can overrule any of these; each states the decision, the rejected positions with the condition under",
          "which each would win, and the grounds. Order: decisions made at integration, then the eight branches' decisions in",
          "branch order, then the undecided nodes with the evidence that would settle each. The branch texts are unchanged except",
          "that headings are prefixed with the branch keyword (the branches reuse `D1`, `D2`).", "",
          "## Decisions made at integration", ""]
    dr += open(HERE / "integration_decisions.md").read().splitlines() if (HERE / "integration_decisions.md").exists() else ["(none)"]
    dr += ["", "## Decisions by branch", ""]
    for b in ORDER:
        dr += [f"### {b}", ""] + demote(dec_by[b], b) + [""]
    dr += ["## Undecided nodes", "",
           "Every node whose epistemic state is `undecided`, with the evidence that would settle it (copied from the branch).", ""]
    und_nodes = sorted(u for g in nodes for u, n in nodes[g].items() if n["epistemic"].startswith("undecided"))
    dr += ["Undecided nodes in the skeleton: " + ", ".join(f"`{u}`" for u in und_nodes) + f" ({len(und_nodes)}).", ""]
    for b in ORDER:
        body = und_by[b]
        dr += [f"### {b}", ""] + (demote(body, b)[1:] if body else ["None."]) + [""]
    (DISTILL / "decisions_for_review.md").write_text("\n".join(dr) + "\n")

    # ---------------- stats
    stats = dict(
        claims=n_claims, rows_in=n_in_rows, rows_out=len(ledger_rows), rows_with_claims=n_with_claims,
        rows_claimless=len(ledger_rows) - n_with_claims, merged=[(m["survivor"], m["absorbed"]) for m in merged_log],
        nodes={g: {k: v for k, v in counts[g].items() if isinstance(k, int)} for g in ("P", "D")},
        links={g: {k: v for k, v in counts[g].items() if isinstance(k, str)} for g in ("P", "D")},
        planned=counts["planned"], how=dict(how_count), proposals=len(proposals),
        branch_counts={f"{g}:{b}": v for (g, b), v in branch_counts.items()},
        undecided=und_nodes, t3=t3_log, mismatches=mismatches, errors=errors,
        roles={r: sum(1 for x in ledger_rows if x["role"] == r) for r in ("decision", "fact", "acceptable-when", "rejected", "deferred")},
        graphs={g: sum(1 for x in ledger_rows if x["graph"] == g) for g in ("js-philosophy", "pig-js-defaults")},
        jr=jr_counts,
    )
    (HERE / "stats.json").write_text(json.dumps(stats, indent=1, default=str))
    print(json.dumps({k: stats[k] for k in ("claims", "rows_in", "rows_out", "nodes", "links", "planned", "how", "errors")}, default=str))
    if mismatches:
        print("ledger-row column mismatches vs branch skeletons:", mismatches)
    return 1 if errors else 0


if __name__ == "__main__":
    # The stage-7 review fixes edited the integrated files directly; re-running this script
    # would rebuild them from the branch folders and undo those fixes. See build/patch/brief_patch.md.
    import sys as _sys
    if "--undo-review-fixes" not in _sys.argv:
        _sys.exit("refusing to run: this would undo the stage-7 review fixes (pass --undo-review-fixes to force)")
    sys.exit(main())
