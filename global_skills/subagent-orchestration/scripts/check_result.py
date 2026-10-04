#!/usr/bin/env python3
"""Check the shape of a three-level result.md without reading it into your context.

    check_result.py RESULT_MD [--inline FILE_WITH_THE_INLINE_RETURN]

Checks, one line each (FAIL exits 1, warn does not):
    levels      L1, L2, L3 sections present, in order
    certainty   L1 states its certainty; share of L2 claims that state theirs
    pins        every fact under "Pinned:" in L1 appears word for word in L2 and in L3
    references  no level points at another level ("see L3", "details below")
    flat L2     L2 lines all of the same length: the signature of trimming, not rolling up
    inline      the inline return matches the file and does not carry L3

Requires Python 3.10 or later.
"""
import re
import statistics
import sys
from pathlib import Path

CERTAINTY = re.compile(r"\b(grounded|inferred|open|verified)\b", re.I)
CROSS_REF = re.compile(r"\b(see|in|as in|details in|per)\s+(L[123]|below|above)\b", re.I)
L3_NONE = re.compile(r"L3:?\s*none", re.I)
# "## L1 headline", "**L1 Headline:**", "## L1: ...", or the inline form "L1 <text>"
HEADER = re.compile(r"^(?:#{1,3}[ \t]*|\*\*)?L([123])\b(?:[ \t]*(?:headline|claims|full)\b)?"
                    r"[ \t]*(?::|\u2014|-)?[ \t]*(?:\*\*)?:?", re.M | re.I)
FILE_LINE = re.compile(r"^\s*(\*\*)?(File|Path|Full report written to)\b.*$", re.M | re.I)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip(" -*`").lower()


def split_levels(text: str) -> dict[str, str]:
    marks = [(m.group(1), m.start(), m.end()) for m in HEADER.finditer(text)]
    levels = {}
    for i, (n, _, end) in enumerate(marks):
        stop = marks[i + 1][1] if i + 1 < len(marks) else len(text)
        levels.setdefault(f"L{n}", text[end:stop].strip())
    return levels


def bullets(body: str) -> list[str]:
    """Bullet items, each joined with its indented continuation lines."""
    items: list[str] = []
    for line in body.splitlines():
        if re.match(r"\s*[-*]\s", line):
            items.append(line.strip())
        elif items and line.startswith("  ") and line.strip():
            items[-1] += " " + line.strip()
        elif not line.strip() or not line.startswith(" "):
            items.append("") if items and items[-1] else None
    return [i for i in items if i]


def pinned_facts(l1: str) -> list[str]:
    m = re.search(r"Pinned:?\**:?\s*\n\s*((?:\s*[-*].*\n?(?:\s{2,}\S.*\n?)*)+)", l1)
    if not m:
        return []
    items = re.split(r"\n\s*[-*]\s+", "\n" + m.group(1))
    return [norm(i) for i in items if norm(i)]


def check(result: str, inline: str | None) -> list[tuple[str, str, str]]:
    out = []
    lv = split_levels(result)
    order = [k for k in ("L1", "L2", "L3") if k in lv]
    l3_none = bool(L3_NONE.search(result))
    if order == ["L1", "L2", "L3"] or (order == ["L1", "L2"] and l3_none):
        out.append(("ok", "levels", "L1, L2, L3" + (" (L3: none)" if l3_none else "")))
    else:
        out.append(("FAIL", "levels", f"found {order or 'none'}"))
        return out
    l1, l2, l3 = lv["L1"], lv["L2"], lv.get("L3", "")

    headline = l1.split("Pinned")[0]
    out.append(("ok" if CERTAINTY.search(headline) else "warn", "certainty",
                "L1 states its certainty" if CERTAINTY.search(headline) else "L1 states no certainty"))
    pins = pinned_facts(l1)
    claims = [c for c in bullets(l2) if norm(c) not in pins]
    marked = sum(bool(CERTAINTY.search(l)) for l in claims)
    if claims:
        out.append(("ok" if marked == len(claims) else "warn", "certainty",
                    f"{marked}/{len(claims)} L2 claims state their certainty"))

    missing = [(p, lvl) for p in pins for lvl, body in (("L2", l2), ("L3", l3))
               if not (lvl == "L3" and l3_none) and p not in norm(body)]
    if not pins:
        out.append(("warn", "pins", "no 'Pinned:' list in L1"))
    elif missing:
        for p, lvl in missing:
            out.append(("FAIL", "pins", f"not word for word in {lvl}: {p[:70]}"))
    else:
        out.append(("ok", "pins", f"{len(pins)} pinned fact(s), identical at every level"))

    refs = [(k, m.group(0)) for k, body in lv.items() for m in CROSS_REF.finditer(body)]
    out.append(("FAIL" if refs else "ok", "references",
                "; ".join(f"{k}: '{r}'" for k, r in refs) if refs else "each level stands alone"))

    lengths = [len(l.strip()) for l in claims]
    if len(lengths) >= 4:
        cv = statistics.pstdev(lengths) / statistics.mean(lengths)
        out.append(("warn" if cv < 0.15 else "ok", "flat L2",
                    f"line-length variation {cv:.2f}" + (" (trimmed?)" if cv < 0.15 else "")))

    if inline is not None:
        ilv = split_levels(FILE_LINE.sub("", inline))
        problems = []
        if "L3" in ilv and not L3_NONE.search(ilv["L3"]):
            problems.append("carries L3")
        if "L1" not in ilv:
            problems.append("no L1")
        for k in ("L1", "L2"):
            if k in ilv and norm(ilv[k]) != norm(lv[k]):
                problems.append(f"{k} differs from the file")
        out.append(("FAIL" if problems else "ok", "inline",
                    ", ".join(problems) if problems else "matches the file, no L3"))
    return out


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    if not Path(args[0]).is_file():
        print(f"FAIL file       nothing at the assigned path {args[0]}")
        sys.exit(1)
    result = Path(args[0]).read_text()
    inline = Path(args[args.index("--inline") + 1]).read_text() if "--inline" in args else None
    results = check(result, inline)
    for status, name, detail in results:
        print(f"{status:4} {name:10} {detail}")
    sys.exit(1 if any(s == "FAIL" for s, _, _ in results) else 0)


if __name__ == "__main__":
    main()
