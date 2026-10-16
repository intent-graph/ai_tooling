#!/usr/bin/env python3
"""Check the shape of a handoff file without reading it into your context.

    check_handoff.py HANDOFF_MD [--allow-tmp]
    check_handoff.py --self-test

Checks, one line each (FAIL exits 1, warn does not):
    location    not in a scratchpad or temp directory (--allow-tmp skips this)
    header      Status, Written and Use lines before L1; a Work location; no Predecessor line.
                An optional "Receiver: self-contained (<receiver>)" line skips the pointer and
                pasting checks
    levels      L1, L2, L3 in order, and L3 opens with ### Intent (the default read stops at
                L3's next section). Without levels, the content checks still run on the whole file
    certainty   L1 states its certainty; State lines state theirs; no "assumed" state
    pins        a "Pinned:" list in L1, each pin dated
    sections    L2 has the five typed sections: Intent, State, Map, Next, Open
    intent      each Intent line is tagged explicit / ruled out / preference / implicit;
                implicit lines cite evidence and say inferred
    claim size  no L2 line over 40 words, paths not counted, prose lines included
    next/open   Next has a Goal line; every Open item has an "If unanswered"
    pointers    absolute paths in L1 and L2 exist on disk; every Map line has one; none points
                to another handoff (a successor stands alone)
    dictation   no reading orders ("read in full", "in this order"), quoted user words excepted
    leftovers   nothing marked as existing "only in the conversation"
    pasting     no long code block in L1 or L2; L1 plus L2 within 60 lines and 6,000 characters,
                paths and URLs not counted
    references  no level points at another level ("see L3", "details below")

Headings, Intent tags and certainty words are structural keys in English; content may be in any
language. Requires Python 3.10 or later.
"""
import re
import sys
from pathlib import Path

CERTAINTY = re.compile(r"\b(grounded|inferred|open|verified)\b", re.I)
CROSS_REF = re.compile(r"\b(see|details in|cf\.?|voir)\s+(L[123]|below|above)\b|\bas\s+(above|below)\b"
                       r"|\b(in|as in|per)\s+(L[123]|below|above)(?=\s*[.,;:)]|\s*$)", re.I | re.M)
HEADER = re.compile(r"^##[ \t]*L([123])\b.*$", re.M)
SECTIONS = ("Intent", "State", "Map", "Next", "Open")
SECTION = re.compile(r"^###[ \t]*(\w+)", re.M)
TAG = re.compile(r"^[-*]\s*\**(explicit|ruled out|preference|implicit)\b", re.I)
DICTATION = re.compile(
    r"(read\W+(?:it\W+|them\W+|this\W+|these\W+|all\W+|everything\W+)?(?:in full|fully|entirely|first)"
    r"|in this order|start by reading|begin by reading|lis(?:ez)?\W+(?:en entier|intégralement|d'abord)"
    r"|commence[rz]? par lire|dans cet ordre)", re.I)
QUOTED = re.compile(r'"[^"\n]*"|“[^”\n]*”|«[^»\n]*»')
LEFTOVER = re.compile(r"\b(conversation|chat) only\b|\bonly in (the )?(conversation|chat)\b"
                      r"|\b(uniquement|seulement) dans (la conversation|le chat)\b", re.I)
ASSUMED = re.compile(r"\b(assumed|supposée?s?)\b", re.I)
DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b|\(\d{2}[-/]\d{2}\)|\b\d{2}[-/]\d{2}\b")
ABS_PATH = re.compile(r"(?<![\w.])(/(?:Users|home|opt|srv|var|private|tmp|mnt|Volumes|abs)/[^\s`'\")\]>,;]+)")
URL = re.compile(r"https?://\S+")
TMP_DIR = re.compile(r"(/scratchpad/|^/tmp/|^/private/tmp/|^/var/folders/)")
L3_NONE = re.compile(r"L3:?\s*none", re.I)
MAX_CODE_LINES = 8
MAX_L2_LINE_WORDS = 40
MAX_L1_L2_LINES = 60
MAX_L1_L2_CHARS = 6000


def split(text: str, pattern: re.Pattern) -> dict[str, str]:
    marks = list(pattern.finditer(text))
    parts = {}
    for i, m in enumerate(marks):
        stop = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        key = m.group(1).capitalize() if pattern is SECTION else f"L{m.group(1)}"
        parts.setdefault(key, text[m.end():stop].strip())
    return parts


def items(body: str) -> list[str]:
    """Bullets with their continuation lines, and prose paragraphs, each as one item."""
    out: list[str] = []
    prose = False
    for line in body.splitlines():
        if not line.strip() or line.lstrip().startswith(("#", "```", "<!--")):
            prose = False
            continue
        if re.match(r"\s*[-*]\s", line):
            out.append(line.strip())
            prose = False
        elif out and (line.startswith("  ") or prose):
            out[-1] += " " + line.strip()
        else:
            out.append(line.strip())
            prose = True
    return out


def bullets(body: str) -> list[str]:
    return [i for i in items(body) if re.match(r"[-*]\s", i)]


def exists(p: str) -> bool:
    p = re.sub(r":\d+(-\d+)?$", "", p.split("#")[0].rstrip(".:"))
    return Path(p).exists()


def resolve_path(m: re.Match, text: str) -> str:
    """The longest existing path starting at the match, so paths with spaces resolve."""
    rest = re.split(r"[`'\")\]>]", text[m.start(1):].split("\n")[0])[0]
    cuts = [i for i, ch in enumerate(rest) if ch in " ,;:"] + [len(rest)]
    for i in reversed(cuts):
        if i >= len(m.group(1)) and exists(rest[:i].strip()):
            return rest[:i].strip()
    return m.group(1).rstrip(".:")


def pinned_facts(l1: str) -> list[str]:
    m = re.search(r"Pinned:?\**:?\s*\n\s*((?:\s*[-*].*\n?(?:\s{2,}\S.*\n?)*)+)", l1)
    if not m:
        return []
    return [i.strip() for i in re.split(r"\n\s*[-*]\s+", "\n" + m.group(1)) if i.strip()]


def check(path: Path, text: str, allow_tmp: bool) -> list[tuple[str, str, str]]:
    out = []
    if not allow_tmp:
        bad = TMP_DIR.search(str(path.resolve()))
        out.append(("FAIL" if bad else "ok", "location",
                    "in a scratchpad or temp dir: the next session cannot rely on it" if bad
                    else "in the project tree"))

    head = text.split("## L1")[0]
    self_contained = bool(re.search(r"^Receiver:\s*self-contained", head, re.M | re.I))
    missing = [k for k in ("Status:", "Written:", "Use:") if k not in head]
    notes = []
    if "Work:" not in head:
        notes.append("no Work location (dir, branch, commit)")
    if re.search(r"Predecessor:\s*(?!none)\S", head, re.I):
        notes.append("names a predecessor: a successor stands alone, the old file points forward")
    status = "FAIL" if "Status:" in missing else "warn" if missing or notes else "ok"
    detail = "; ".join(([f"missing {', '.join(missing)}"] if missing else []) + notes)
    out.append((status, "header", detail or "Status, Written, Use and Work lines"))
    if self_contained:
        out.append(("ok", "receiver", "self-contained on request: pointer and pasting checks skipped"))

    lv = split(text, HEADER)
    if [k for k in ("L1", "L2", "L3") if k in lv] != ["L1", "L2", "L3"]:
        out.append(("FAIL", "levels", f"found {list(lv) or 'none'}; want '## L1 ...', '## L2 ...', '## L3 ...'; "
                                      "content checks below run on the whole file"))
        l1, l2, l3 = lv.get("L1", ""), lv.get("L2", text), lv.get("L3", "")
    else:
        l1, l2, l3 = lv["L1"], lv["L2"], lv["L3"]
        first = SECTION.search(l3)
        if L3_NONE.search(l3) or not first or first.group(1).capitalize() != "Intent":
            out.append(("FAIL", "levels", "L3 must open with ### Intent: the user's words, part of the default read"))
        else:
            out.append(("ok", "levels", f"L1, L2, L3; L3 opens with Intent ({len(split(l3, SECTION)['Intent'])} chars)"))

    pins = pinned_facts(l1) if l1 else []
    if l1:
        headline = l1.split("Pinned")[0]
        out.append(("ok" if CERTAINTY.search(headline) else "warn", "certainty",
                    "L1 states its certainty" if CERTAINTY.search(headline) else "L1 states no certainty"))
        undated = [p for p in pins if not DATE.search(p)]
        out.append(("warn" if not pins or undated else "ok", "pins",
                    "no 'Pinned:' list in L1: did the user set no prohibition and no 'ask me before'?" if not pins
                    else f"{len(undated)}/{len(pins)} pins without a date: a pin is the user's words, dated" if undated
                    else f"{len(pins)} pinned fact(s) in L1, dated"))

    secs = split(l2, SECTION)
    absent = [s for s in SECTIONS if s not in secs]
    out.append(("FAIL" if absent else "ok", "sections",
                f"L2 lacks ### {', ### '.join(absent)}" if absent else "five typed sections in L2"))

    intent = [b for b in bullets(secs.get("Intent", "")) if b.strip(" -*") not in pins]
    if intent:
        tags = [TAG.match(b) for b in intent]
        untagged = sum(t is None for t in tags)
        kinds = {t.group(1).lower() for t in tags if t}
        implicit = [b for b, t in zip(intent, tags) if t and t.group(1).lower() == "implicit"]
        weak = [b for b in implicit if not (re.search(r"evidence|preuve|\"|«|“", b, re.I)
                                            and re.search(r"inferred", b, re.I))]
        status = "FAIL" if untagged > len(intent) // 4 else "ok"
        detail = f"{len(intent)} lines, tags: {', '.join(sorted(kinds)) or 'none'}"
        if untagged:
            detail += f"; {untagged} untagged"
        if "implicit" not in kinds or "ruled out" not in kinds:
            status = "warn" if status == "ok" else status
            detail += "; no " + " and no ".join(k for k in ("implicit", "ruled out") if k not in kinds) + \
                      " item (did you read the user's corrections?)"
        if weak:
            status = "warn" if status == "ok" else status
            detail += f"; {len(weak)} implicit line(s) without evidence or 'inferred'"
        out.append((status, "intent", detail))
    else:
        out.append(("FAIL", "intent", "no Intent lines: the one thing only the writer can pass"))

    state = items(secs.get("State", ""))
    if state:
        marked = sum(bool(CERTAINTY.search(s)) for s in state)
        assumed = [s for s in state if ASSUMED.search(s)]
        out.append(("warn" if marked < len(state) or assumed else "ok", "certainty",
                    f"{marked}/{len(state)} State lines state their certainty"
                    + (f"; {len(assumed)} say 'assumed': check it, or say 'not checked' and why" if assumed else "")))

    l2_items = [i for s in SECTIONS for i in items(secs.get(s, ""))]
    words = [len(URL.sub("", ABS_PATH.sub("", i)).split()) for i in l2_items]
    if words:
        long_lines = sum(w > MAX_L2_LINE_WORDS for w in words)
        mean = sum(words) / len(words)
        out.append(("FAIL" if long_lines else "warn" if mean > 25 else "ok", "claim size",
                    f"{long_lines} L2 line(s) over {MAX_L2_LINE_WORDS} words, paths not counted; "
                    f"mean {mean:.0f}: move counts, identifiers and reasoning to L3" if long_lines
                    else f"L2 lines average {mean:.0f} words" + (" (claims or paragraphs?)" if mean > 25 else "")))

    if secs:
        problems = []
        if not re.search(r"^\s*[-*]\s*\**Goal\b", secs.get("Next", ""), re.M | re.I):
            problems.append("Next has no Goal line")
        open_items = [b for b in bullets(secs.get("Open", "")) if not re.match(r"[-*]\s*none\b", b, re.I)]
        no_default = [b for b in open_items if not re.search(r"if unanswered", b, re.I)]
        if no_default:
            problems.append(f"{len(no_default)}/{len(open_items)} Open items without 'If unanswered'")
        out.append(("warn" if problems else "ok", "next/open",
                    "; ".join(problems) or "Goal set; every Open item has a default"))

    if not self_contained:
        found = {resolve_path(m, l1 + "\n" + l2) for m in ABS_PATH.finditer(l1 + "\n" + l2)}
        gone = sorted(p for p in found if not p.startswith("/abs/") and not exists(p))
        bare = [b for b in bullets(secs.get("Map", "")) if not ABS_PATH.search(b) and not URL.search(b)
                and not re.match(r"[-*]\s*none\b", b, re.I)]
        problems = []
        if gone:
            problems.append(f"{len(gone)}/{len(found)} paths not on disk: {', '.join(gone[:3])}")
        if bare:
            problems.append(f"{len(bare)} Map line(s) without an absolute path or URL")
        handoffs = sorted(p.rstrip(":") for p in found if re.search(r"handoff|next_session", Path(p).name, re.I)
                          and Path(p).name != path.name)
        if handoffs:
            problems.append(f"points to another handoff ({Path(handoffs[0]).name}): carry its still-valid "
                            "items forward, move its durable rules to their project document")
        if not found and l2_items:
            problems.append("no absolute path in L1 or L2: does the receiver know where to look?")
        out.append(("warn" if problems else "ok", "pointers",
                    "; ".join(problems) or f"{len(found)} absolute paths, all on disk"))

    orders = [m.group(0) for m in DICTATION.finditer(QUOTED.sub('""', l1 + "\n" + l2))]
    out.append(("warn" if orders else "ok", "dictation",
                f"reading orders: {'; '.join(orders[:3])} (quote them if the user dictated them)"
                if orders else "no reading orders"))

    left = [m.group(0) for m in LEFTOVER.finditer(text)]
    out.append(("warn" if left else "ok", "leftovers",
                f"'{left[0]}': material the receiver needs goes to a draft file beside the work" if left
                else "nothing left only in the conversation"))

    if not self_contained:
        blocks = re.findall(r"```.*?\n(.*?)```", l1 + "\n" + l2, re.S)
        long_blocks = [b for b in blocks if b.count("\n") > MAX_CODE_LINES]
        n_lines = len([x for x in (l1 + "\n" + l2).splitlines() if x.strip()])
        n_chars = len(URL.sub("", ABS_PATH.sub("", l1 + l2)))  # paths and URLs are not content
        problems = []
        if long_blocks:
            problems.append(f"{len(long_blocks)} code block(s) over {MAX_CODE_LINES} lines (pasted content?)")
        if n_lines > MAX_L1_L2_LINES or n_chars > MAX_L1_L2_CHARS:
            problems.append(f"L1+L2 is {n_lines} lines, {n_chars} chars (restated content, a plan, or "
                            "detail that belongs in L3?)")
        out.append(("warn" if problems else "ok", "pasting",
                    "; ".join(problems) or f"L1+L2 is {n_lines} lines, {n_chars} chars"))

    bodies = lv if lv else {"file": text}
    refs = [(k, m.group(0)) for k, body in bodies.items() for m in CROSS_REF.finditer(QUOTED.sub('""', body))]
    out.append(("FAIL" if refs else "ok", "references",
                "; ".join(f"{k}: '{r}'" for k, r in refs[:4]) if refs else "each level stands alone"))
    return out


def self_test() -> None:
    cases = [
        (CROSS_REF, "weight decay moved in L2 regularization", False),
        (CROSS_REF, "as in L1 norm terms", False),
        (CROSS_REF, "in below_basic cases", False),
        (CROSS_REF, "details are in L3.", True),
        (CROSS_REF, "see L3", True),
        (CROSS_REF, "as above", True),
        (CROSS_REF, "voir L3", True),
        (DICTATION, "Read, in full, first: /abs/x", True),
        (DICTATION, "start by reading the QA note", True),
        (DICTATION, "Read these, in this order:", True),
        (DICTATION, "commence par lire le README", True),
        (DICTATION, QUOTED.sub('""', '"careful, read first, I changed it" (09-15)'), False),
        (DICTATION, "the reader decides what to open", False),
        (LEFTOVER, "edits agreed in conversation only", True),
        (LEFTOVER, "the user said in the conversation that", False),
        (ASSUMED, "done (assumed): tests pass", True),
        (DATE, '"don\'t touch invoices" (03-14)', True),
    ]
    failed = 0
    for pattern, sample, expected in cases:
        got = bool(pattern.search(sample))
        failed += got != expected
        print(f"{'ok  ' if got == expected else 'FAIL'} {sample!r} -> {got}")
    sample = "intro\n- a bullet\n  continued\nprose line one\nprose line two\n\n- next"
    got = items(sample)
    ok = got == ["intro", "- a bullet continued", "prose line one prose line two", "- next"]
    failed += not ok
    print(f"{'ok  ' if ok else 'FAIL'} items() -> {got}")
    sys.exit(1 if failed else 0)


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    if "--self-test" in args:
        self_test()
    files = [a for a in args if not a.startswith("--")]
    if len(files) != 1:
        print("FAIL usage      give exactly one handoff file")
        sys.exit(1)
    path = Path(files[0])
    if not path.is_file():
        print(f"FAIL file       nothing at {path}")
        sys.exit(1)
    results = check(path, path.read_text(), "--allow-tmp" in args)
    for status, name, detail in results:
        print(f"{status:4} {name:10} {detail}")
    sys.exit(1 if any(s == "FAIL" for s, _, _ in results) else 0)


if __name__ == "__main__":
    main()
