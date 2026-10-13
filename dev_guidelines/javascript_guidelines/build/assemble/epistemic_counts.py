"""Count epistemic_state classes per graph: known alone, known with unvalidated or conflict (or any other issue),
risky, undecided, deferred, other. Run from the guideline root: python3 build/assemble/epistemic_counts.py"""
import collections
import json
import yaml

FILES = {"js-philosophy": "intent_graphs/js_philosophy.ig.yaml", "pig-js-defaults": "intent_graphs/js_defaults.ig.yaml"}


def klass(state):
    base, *issues = [x.strip() for x in (state or "").split("|")]
    head = base.split()[0].rstrip(":,;").lower() if base else ""
    if head == "known":
        if not issues:
            return "known alone"
        if any(i.startswith(("unvalidated", "conflict")) for i in issues):
            return "known with unvalidated or conflict"
        return "known with other issues (gap, missing, rolls up)"
    if head in ("risky", "undecided", "deferred"):
        return head
    return "other"


if __name__ == "__main__":
    out = {}
    for gid, f in FILES.items():
        g = yaml.safe_load(open(f))
        c = collections.Counter(klass(n.get("epistemic_state")) for n in g["nodes"])
        iss = collections.Counter()
        for n in g["nodes"]:
            for x in (n.get("epistemic_state") or "").split("|")[1:]:
                iss[x.strip().split(":")[0]] += 1
        out[gid] = dict(total=sum(c.values()), **c, issue_types=dict(iss))
    print(json.dumps(out, indent=1))
