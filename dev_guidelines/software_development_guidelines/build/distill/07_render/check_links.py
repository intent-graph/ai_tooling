#!/usr/bin/env python3
"""Check (and optionally repair) relative markdown links between the guideline's body files.

A link `file.md#anchor` is broken when the file does not exist or has no heading whose
GitHub-style slug is `anchor`. With --fix, a broken link is repointed to the one body file that
holds a heading with that slug, when exactly one does; ambiguous or unknown anchors are reported.

Usage: python3 check_links.py [--fix]   (run from anywhere; paths resolve from this file)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # the guideline folder
LINK = re.compile(r"\]\(((?!https?:|#)[^)#\s]+\.md)(#[^)\s]+)?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")


def slug(text: str) -> str:
    text = re.sub(r"`", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set:
    found, seen = set(), {}
    in_code = False
    for line in path.read_text().splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        m = HEADING.match(line)
        if m:
            s = slug(m.group(2))
            n = seen.get(s, 0)
            found.add(s if n == 0 else f"{s}-{n}")
            seen[s] = n + 1
    return found


def main(fix: bool) -> int:
    files = sorted(p for p in ROOT.glob("*.md"))
    index = {p.name: anchors(p) for p in files}
    owners = {}
    for name, slugs in index.items():
        for s in slugs:
            owners.setdefault(s, []).append(name)
    broken = repaired = 0
    for p in files:
        text = p.read_text()
        out = text
        for m in LINK.finditer(text):
            target, frag = m.group(1), (m.group(2) or "")[1:]
            tname = Path(target).name
            ok = tname in index and (not frag or frag in index[tname])
            if ok:
                continue
            broken += 1
            cand = owners.get(frag, []) if frag else []
            if fix and len(cand) == 1:
                out = out.replace(m.group(0), f"]({cand[0]}#{frag})", 1)
                repaired += 1
            else:
                print(f"{p.name}: {target}#{frag} -> candidates {cand or 'none'}")
        if fix and out != text:
            p.write_text(out)
    print(f"files {len(files)}; broken {broken}; repaired {repaired}; left {broken - repaired}")
    return 0 if broken == repaired else 1


if __name__ == "__main__":
    sys.exit(main("--fix" in sys.argv))
