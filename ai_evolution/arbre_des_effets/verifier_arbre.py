"""Arbre des effets : vérification et diagrammes.

Lit un dossier d'arbre (README.md puis les fichiers de branche ; boîtes `## INT.n · …` et `- **INT.n.m · …**`, lignes `Causes :` et
`Faits :`), vérifie les règles du README, puis réécrit un diagramme par niveau entre les
marqueurs `<!-- GENERE:<id>:debut -->` et `<!-- GENERE:<id>:fin -->`.

Usage : python3 verifier_arbre.py [dossier] [--check] [--elagues]   (défaut : internet/)
  --check    vérifier sans réécrire
  --elagues  lister les faits du choc qu'aucune feuille ne cite
Bibliothèque standard seulement.
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOSSIER = HERE.parent
WEIGHTS = ("fort", "moyen", "faible")

BOX_H2 = re.compile(r"^## ((?:INT|CLD)\.\d+(?:\.\d+)*) · (.+)$")
BOX_LI = re.compile(r"^\s*- \*\*((?:INT|CLD)\.\d+(?:\.\d+)*) · (.+?)\*\*")
CAUSES = re.compile(r"^\s*(?:- )?Causes : (.+)$")
FACTS = re.compile(r"^\s*(?:- )?Faits : (.+)$")
ITEM = re.compile(r"^\s*((?:X\.)?(?:INT|CLD)[\w.]*?)\s*\(([^)]*)\)\s*$")


def parent_of(box):
    parts = box.split(".")
    return None if parts[1] == "0" else ".".join(parts[:-1]) if len(parts) > 2 else parts[0] + ".0"


def ancestors(box):
    out, p = [], parent_of(box)
    while p:
        out.append(p)
        p = parent_of(p)
    return out


def tree_files(folder):
    return [folder / "README.md"] + sorted(f for f in folder.glob("*.md") if f.name != "README.md")


def parse(folder):
    boxes, current = {}, None
    lines = [l for f in tree_files(folder) for l in f.read_text().splitlines()]
    for line in lines:
        m = BOX_H2.match(line) or BOX_LI.match(line)
        if m:
            current = m.group(1)
            boxes[current] = {"title": m.group(2).strip(), "causes": [], "facts": [], "amont": False}
            continue
        if current is None:
            continue
        if m := CAUSES.match(line):
            for raw in re.split(r";(?![^()]*\))", m.group(1)):
                if raw.strip().startswith("amont"):
                    boxes[current]["amont"] = True
                elif im := ITEM.match(raw):
                    flags = {f.strip() for f in im.group(2).split(",")}
                    boxes[current]["causes"].append({"src": im.group(1), "flags": flags})
                elif raw.strip():
                    boxes[current]["causes"].append({"src": raw.strip(), "flags": {"?"}})
        elif m := FACTS.match(line):
            boxes[current]["facts"] += [f.strip() for f in m.group(1).split(",") if f.strip()]
    return boxes


def register():
    text = (DOSSIER / "04_confondants.md").read_text()
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"^\| (X\.(?:INT|CLD)\.\d\d) \| [^|]+ \| ([^|]+) \|", text, re.M)}


def dossier_ids(shock):
    ids = set()
    for sub in ("par_dimension", "par_annee"):
        for p in (DOSSIER / sub).rglob("*.md"):
            ids.update(re.findall(rf"^\| ([FJ]\.{shock}\.[\w.]+) \|", p.read_text(), re.M))
    return ids


def check(boxes, xs, ids):
    errors, children = [], {b: [] for b in boxes}
    for b in boxes:
        p = parent_of(b)
        if p:
            if p not in boxes:
                errors.append(f"{b} : parent {p} absent")
            else:
                children[p].append(b)
    seen = {}
    for b, d in boxes.items():
        kids = children[b]
        if kids and not 2 <= len(kids) <= 6:
            errors.append(f"{b} : {len(kids)} enfant(s), attendu 2 à 6")
        if not kids and not d["facts"]:
            errors.append(f"{b} : feuille sans faits")
        if kids and d["facts"]:
            errors.append(f"{b} : faits sur une boîte non feuille")
        for f in d["facts"]:
            if f not in ids:
                errors.append(f"{b} : fait introuvable {f}")
            if f in seen:
                errors.append(f"{f} cité sous {seen[f]} et {b}")
            seen[f] = b
        mains = [c for c in d["causes"] if "principale" in c["flags"]]
        if b.split(".")[1] != "0" and not d["amont"] and len(mains) != 1:
            errors.append(f"{b} : {len(mains)} cause(s) principale(s), attendu 1")
        for c in d["causes"]:
            if c["src"] not in boxes and c["src"] not in xs:
                errors.append(f"{b} : cause inconnue {c['src']}")
            if not (c["flags"] & set(WEIGHTS)) and "boucle" not in c["flags"]:
                errors.append(f"{b} : cause {c['src']} sans poids")
    # invariant 4 : une cause qui atteint un descendant apparaît sur chaque ancêtre traversé
    for d, dd in boxes.items():
        for c in dd["causes"]:
            src = c["src"]
            src_chain = {src, *ancestors(src)} if src in boxes else {src}
            for a in ancestors(d):
                inside = src == a or a in (ancestors(src) if src in boxes else [])
                if inside or a in src_chain:
                    break
                if not any(e["src"] in src_chain for e in boxes[a]["causes"]):
                    errors.append(f"invariant 4 : {src} → {d} absent de {a}")
    # cycles parmi les causes comptées, déclarées sous le niveau 1
    edges = [(c["src"], b) for b, d in boxes.items() if b.count(".") >= 2
             for c in d["causes"] if "boucle" not in c["flags"]]
    graph = {}
    for s, t in edges:
        graph.setdefault(s, []).append(t)
    state = {}

    def visit(n, stack):
        state[n] = 1
        for m in graph.get(n, []):
            if state.get(m) == 1:
                errors.append("cycle : " + " → ".join(stack + [n, m]))
            elif not state.get(m):
                visit(m, stack + [n])
        state[n] = 2
    for n in list(graph):
        if not state.get(n):
            visit(n, [])
    return errors, children, seen


def main_chain_end(box, boxes):
    """Où mène la chaîne des causes principales : une boîte d'amont ou un confondant."""
    seen = set()
    while box in boxes and box not in seen:
        seen.add(box)
        mains = [c["src"] for c in boxes[box]["causes"] if "principale" in c["flags"]]
        if not mains:
            return box
        box = mains[0]
    return box


def mid(n):
    return n.replace(".", "_")


def diagram(p, boxes, children, xs):
    kids = children[p]
    lines, nodes, arrows = ["```mermaid", "flowchart LR"], {}, {}
    for k in kids:
        nodes[k] = f'  {mid(k)}["{k}<br/>{short(boxes[k]["title"])}"]'
    for k in kids:
        for c in boxes[k]["causes"]:
            src = c["src"]
            owner = next((s for s in kids if src == s or s in ancestors(src)), None) \
                if src in boxes else None
            if owner is None and src in boxes:
                owner = next((a for a in [src, *ancestors(src)] if parent_of(a) == "INT.0"
                              or parent_of(a) == "CLD.0"), src)
                if owner in (p, *ancestors(p)):
                    continue
                nodes.setdefault(owner, f'  {mid(owner)}["{owner}<br/>{short(boxes[owner]["title"])}"]:::autre')
            elif owner is None:
                owner = src
                nodes.setdefault(src, f'  {mid(src)}["{src}<br/>{short(re.split(r"[:;,(]", xs.get(src, ""))[0], 30)}"]:::conf')
            if owner == k:
                continue
            weight = next((w for w in WEIGHTS if w in c["flags"]), "")
            if weight == "faible" and "principale" not in c["flags"]:
                continue  # vue : les causes faibles restent dans le texte
            style = "-.->" if "boucle" in c["flags"] else "==>" if "principale" in c["flags"] else "-->"
            label = "boucle" if "boucle" in c["flags"] else weight
            key = (owner, k)
            if key not in arrows or style == "==>":
                arrows[key] = f"  {mid(owner)} {style}|{label}| {mid(k)}"
    used = set(kids) | {end for key in arrows for end in key}
    lines += [v for n, v in nodes.items() if n in used] + list(arrows.values())
    lines += ["  classDef conf fill:#eee,stroke:#999,color:#555",
              "  classDef autre fill:#e8f0fb,stroke:#6b8fc7", "```"]
    return "\n".join(lines)


def short(text, n=42):
    text = text.replace('"', "'")
    return text.strip() if len(text) <= n else text[:n].rsplit(" ", 1)[0].rstrip() + "…"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    folder = Path(args[0]) if args else HERE / "internet"
    boxes = parse(folder)
    shock = next(iter(boxes)).split(".")[0]
    xs, ids = register(), dossier_ids(shock)
    errors, children, seen = check(boxes, xs, ids)
    for e in errors:
        print("erreur :", e)
    leaves = [b for b in boxes if not children[b]]
    depth = {}
    for b in leaves:
        depth[b.count(".")] = depth.get(b.count("."), 0) + 1
    print(f"{len(boxes)} boîtes, {len(leaves)} feuilles, profondeur des feuilles {dict(sorted(depth.items()))}, "
          f"{len(seen)} faits cités sur {len([i for i in ids if i.startswith('F.')])} faits du choc.")
    ends = {}
    for b in leaves:
        ends.setdefault(main_chain_end(b, boxes), []).append(b)
    print("chaînes principales des feuilles, par point d'arrivée :")
    for end, bs in sorted(ends.items(), key=lambda kv: -len(kv[1])):
        print(f"  {end} ← {len(bs)} : {', '.join(bs)}")
    if "--elagues" in sys.argv:
        pruned = sorted(i for i in ids if i.startswith("F.") and i not in seen)
        print(f"faits non cités ({len(pruned)}) : {', '.join(pruned)}")
    if errors:
        sys.exit(1)
    if "--check" in sys.argv:
        return
    for path in tree_files(folder):
        text = path.read_text()
        for p in boxes:
            start, end = f"<!-- GENERE:{p}:debut -->", f"<!-- GENERE:{p}:fin -->"
            if start in text:
                head, rest = text.split(start, 1)
                text = f"{head}{start}\n{diagram(p, boxes, children, xs)}\n{end}{rest.split(end, 1)[1]}"
        path.write_text(text)
    print("diagrammes réécrits.")


if __name__ == "__main__":
    main()
