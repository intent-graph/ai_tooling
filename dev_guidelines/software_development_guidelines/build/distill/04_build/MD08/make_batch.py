"""Build batch.yaml for MD-08 from the current graph (exact-substring edits, asserted)."""
import subprocess, yaml, sys
G = "intent_graphs/software_development_philosophy.ig.yaml"
def node(uid):
    out = subprocess.run(["ig-tool", "query", "-g", G, "--node", uid], capture_output=True, text=True, check=True).stdout
    return yaml.safe_load(out)
def rep(s, old, new):
    assert s.count(old) == 1, (old[:60], s.count(old))
    return s.replace(old, new)
UNVAL_Q = "unvalidated: awaiting maintainer, can an automated reviewer be the independent check"
ops = []
def op(uid, **f):
    ops.append({"op": "node.set", "uid": uid, **f})

# ROOT
n = node("ROOT"); es = n["epistemic_state"]; dn = n["design_notes"]
es = rep(es, "41 open items", "40 open items")
es = rep(es, "and two points still open, the reviewer kind at ASSURANCE.RULES.4 and the single-store rule at EVOLUTION.TECHNOLOGY.4)", "and one point still open, the single-store rule at EVOLUTION.TECHNOLOGY.4)")
es = rep(es, " | " + UNVAL_Q + " (ASSURANCE.RULES.4, default applied)", "")
dn = rep(dn, "The 41 open items", "The 40 open items")
dn = rep(dn, "one-source minority views and two flags;", "one-source minority views and one flag;")
dn = rep(dn, "the two flags still open sit on ASSURANCE.RULES.4 and EVOLUTION.TECHNOLOGY.4.", "the one flag still open sits on EVOLUTION.TECHNOLOGY.4.")
op("ROOT", epistemic_state=es, design_notes=dn)

# ASSURANCE
n = node("ASSURANCE"); es = n["epistemic_state"]; dn = n["design_notes"]
es = rep(es, " | unvalidated: awaiting maintainer, can an automated reviewer in its own context be the independent check (RULES.4, default applied: different-kind reviewer for high-risk changes)", "")
dn = rep(dn, "The maintainer point on RULES.4 (can an automated reviewer be the independent check; default applied) is open; see \"Still open\". The earlier flag", "The reviewer question at RULES.4 is decided (MD-08). The earlier flag")
op("ASSURANCE", epistemic_state=es, design_notes=dn)

# plain unvalidated-tail removals
for uid, tail in [("CHANGE_FLOW", " (ASSURANCE.RULES.4, default applied)"), ("ASSURANCE.RULES", " (RULES.4, default applied)"),
                  ("CHANGE_FLOW.REVIEW", " (ASSURANCE.RULES.4, default applied)"), ("CHANGE_FLOW.REVIEW.1", " (ASSURANCE.RULES.4, default applied)")]:
    n = node(uid); es = rep(n["epistemic_state"], " | " + UNVAL_Q + tail, "")
    op(uid, epistemic_state=es)

# RULES.4
n = node("ASSURANCE.RULES.4"); dn = n["design_notes"]
intent = ("Every change to mainline is checked before integration by a party other than whoever authored, pushed or requested it, "
 "working from its own context, and the check is recorded on the development platform. That party is a person other than the author "
 "by default; an automated reviewer working from its own context is the independent check only for a tier of low-risk changes the team "
 "declares in advance. A named person stays accountable for each change, approves it and is able to defend it, and an approval binds the "
 "exact final content, so a new commit that changes the diff voids earlier approvals. Only a tier the team defines in advance, in a team "
 "whose mainline is kept releasable by automated gates and fast revert, may be checked after merge; per-change approval by an external board is not used.")
es = ("known: maintainer decision MD-08 | gap: the reason for rejecting review of uncertain changes only is inferred; "
      "whether a given regulation still requires an external board was not read")
cons = ["The approver MUST differ from the author",
        "An automated reviewer MUST NOT be the independent check outside the declared low-risk tier",
        "An approval MUST lapse when the diff changes",
        "A named person MUST be accountable and MUST approve every change"]
dn = rep(dn, "Decision as judged, with the maintainer default (R27) merged with the tier sentence (R16): every change gets an independent check before or after merge;",
 "Decision as judged, with the maintainer decision MD-08 (replacing the earlier default, R27) merged with the tier sentence (R16): every change gets an independent check before or after merge, and that check is a person other than the author by default, an automated reviewer working from its own context only for a tier of low-risk changes the team declares in advance;")
a = dn.index("MAINTAINER POINT (open, F2, R27)")
b = dn.index("\n", a)
dn = dn[:a] + ("MAINTAINER DECISION (MD-08, answered; was F2, R27): the research row says 'independent human check' (L136) while MD-02 says who does the work is not a principle. "
 "Decided: a person other than the author is the independent check by default; an automated reviewer working from its own context is the independent check only for a tier of "
 "low-risk changes the team declares in advance; a named person stays accountable and approves every change. Accepted cost: the team keeps a declared list of low-risk change "
 "classes, and a team of one cannot meet the rule for its own higher-risk changes.") + dn[b:]
dn = rep(dn, "P5 approval binds to the final content.", "P5 approval binds to the final content; P6 a person is the independent check by default, an automated reviewer only for a declared low-risk tier.")
dn = rep(dn, "Rejected, with the condition under which each would be best: ",
 "Rejected, with the condition under which each would be best: an automated reviewer as the independent check for every change (independence by context alone): the author and the reviewer may be models of the same kind with overlapping blind spots; best never as the general rule under MD-08, admitted for the declared low-risk tier. A person only, with no low-risk tier: a team of one could never meet the rule; best where no change class can be declared low-risk. ")
op("ASSURANCE.RULES.4", intent=intent, epistemic_state=es, constraints=cons, design_notes=dn)

# REVIEW.4
n = node("CHANGE_FLOW.REVIEW.4"); dn = n["design_notes"]
intent = ("Format, lint, tests and build run before the human reviewer so attention goes to design and logic. A second automated reviewer may be added as an extra layer "
 "and never as the approving party: a named person approves every change. It is the independent check only for the tier of low-risk changes the team declares in advance "
 "(ASSURANCE.RULES.4); every other change is checked by a person other than its author.")
es = ("known | gap: no study read on the accuracy of an automated second reviewer; inferred, the second automated reviewer as an extra layer (vendor statements only)")
cons = ["Automated checks MUST run before the reviewer is asked",
        "An automated reviewer MUST NOT be the approving party",
        "An automated reviewer MUST NOT be the independent check outside the declared low-risk tier"]
dn = rep(dn, "A second model reviewing in a fresh context may be added as an extra layer, never as the approver: the accountable approval stays with an independent responsible party, and the extra layer substitutes for no part of it at high risk.",
 "A second model reviewing in a fresh context may be added as an extra layer, never as the approver: a named person approves every change. It is the independent check only for the low-risk tier the team declares in advance (RULES.4, MD-08); every other change is checked by a person other than its author, and the extra layer substitutes for no part of that check.")
dn = rep(dn, "P2 as a replacement for part of the human review: best when volume exceeds human capacity and risk is low, and only as a layer (the human review stays in force); where risk is high P3 alone governs approval.",
 "P2 as a replacement for part of the human review: best for the declared low-risk tier (MD-08), where it can be the independent check while a named person still approves; outside that tier the person's check stays in force and P3 alone governs approval.")
op("CHANGE_FLOW.REVIEW.4", intent=intent, epistemic_state=es, constraints=cons, design_notes=dn)

yaml.safe_dump({"operations": ops}, open(sys.argv[1], "w"), allow_unicode=True, width=100, sort_keys=False)
