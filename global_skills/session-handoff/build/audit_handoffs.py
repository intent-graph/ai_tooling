#!/usr/bin/env python3
"""Measure how sessions write handoffs to a new session, from Claude Code transcripts.

Reads every main-session *.jsonl transcript under the projects directory, finds each user
message asking for a new-session prompt or handoff, and reports over all of them:

    adoption   share of requests answered after loading the session-handoff skill
    delivery   share answered with a file written in the project, in a scratchpad or temp
               directory, or in chat only
    size       characters of the reply plus any handoff file written
    shape      share of handoff files with the three levels and the five typed sections
    reaction   the user's next message, truncated, for reading by eye (--show)

Usage: audit_handoffs.py [--projects-dir DIR] [--since YYYY-MM-DD] [--until YYYY-MM-DD] [--show] [--json OUT]
"""
import argparse
import json
import re
import statistics
from pathlib import Path

REQUEST = re.compile(
    r"(new session|next session|fresh session|nouvelle session|prochaine session|hand ?off|"
    r"handover|passer la main|prompt (to|for) (start|resume|continue|a new)|"
    r"(out|court) (of|de) context)", re.I)
SKIP = ("<command-name>", "<task-notification>", "<system-reminder>", "Caveat:", "<local-command",
        "Another Claude session sent a message")
SKILL = "session-handoff"
TMP = re.compile(r"(/scratchpad/|^/tmp/|^/private/tmp/|^/var/folders/)")
SHAPE = (re.compile(r"^## L1", re.M), re.compile(r"^## L2", re.M), re.compile(r"^## L3|L3: none", re.M),
         *(re.compile(rf"^### {s}", re.M) for s in ("Intent", "State", "Map", "Next", "Open")))


def text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")
    return ""


def is_tool_result(content) -> bool:
    return isinstance(content, list) and any(isinstance(c, dict) and c.get("type") == "tool_result" for c in content)


def audit_session(path: Path, since: str, until: str) -> list[dict]:
    evs = []
    for raw in path.read_text(errors="ignore").splitlines():
        try:
            ev = json.loads(raw)
        except ValueError:
            continue
        if ev.get("type") in ("user", "assistant") and not ev.get("isSidechain") \
                and since <= (ev.get("timestamp") or "") < (until or "~"):
            evs.append(ev)
    found, skill_loaded = [], False
    for i, ev in enumerate(evs):
        content = (ev.get("message") or {}).get("content")
        if ev["type"] == "assistant" and isinstance(content, list):
            skill_loaded |= any(c.get("type") == "tool_use" and c.get("name") == "Skill"
                                and SKILL in json.dumps(c.get("input", {})) for c in content if isinstance(c, dict))
        txt = text_of(content) if ev["type"] == "user" and not is_tool_result(content) else ""
        if not txt or txt.startswith(SKIP) or not REQUEST.search(txt[:4000]):
            continue
        reply, writes, reaction, loaded = 0, [], "", skill_loaded
        for ev2 in evs[i + 1:]:
            c2 = (ev2.get("message") or {}).get("content")
            if ev2["type"] == "user":
                t2 = text_of(c2)
                if t2 and not is_tool_result(c2) and not t2.startswith(SKIP):
                    reaction = t2
                    break
                continue
            for x in c2 if isinstance(c2, list) else []:
                if not isinstance(x, dict):
                    continue
                if x.get("type") == "text":
                    reply += len(x["text"])
                elif x.get("type") == "tool_use" and x.get("name") == "Skill" and SKILL in json.dumps(x.get("input", {})):
                    loaded = True
                elif x.get("type") == "tool_use" and x.get("name") == "Write":
                    inp = x.get("input", {})
                    writes.append((inp.get("file_path") or "", inp.get("content") or ""))
        handoffs = [(p, c) for p, c in writes if re.search(r"handoff|next_session|session|prompt|reprise", p, re.I)]
        found.append({
            "session": path.stem, "ts": ev.get("timestamp", "")[:16], "skill": loaded,
            "delivery": "chat" if not handoffs else "tmp" if all(TMP.search(p) for p, _ in handoffs) else "project",
            "chars": reply + sum(len(c) for _, c in handoffs),
            "shape": max((sum(bool(s.search(c)) for s in SHAPE) for _, c in handoffs), default=0),
            "request": txt[:200], "reaction": reaction[:300],
        })
    return found


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--projects-dir", default=str(Path.home() / ".claude/projects"))
    ap.add_argument("--since", default="")
    ap.add_argument("--until", default="", help="exclusive")
    ap.add_argument("--show", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()
    rows = [r for p in sorted(Path(a.projects_dir).glob("*/*.jsonl")) for r in audit_session(p, a.since, a.until)]
    if not rows:
        print("no handoff requests found")
        return
    n = len(rows)
    pct = lambda k: f"{100 * k / n:.0f}%"
    print(f"handoff requests: {n} in {len({r['session'] for r in rows})} sessions")
    print(f"adoption: {pct(sum(r['skill'] for r in rows))} after loading {SKILL}")
    for d in ("project", "tmp", "chat"):
        print(f"delivery {d:8}: {pct(sum(r['delivery'] == d for r in rows))}")
    print(f"size: median {statistics.median(r['chars'] for r in rows):.0f} chars, max {max(r['chars'] for r in rows)}")
    files = [r for r in rows if r["delivery"] != "chat"]
    if files:
        print(f"shape: {sum(r['shape'] == len(SHAPE) for r in files)}/{len(files)} handoff files with 3 levels and 5 sections")
    if a.show:
        for r in rows:
            print(f"\n{r['ts']} skill={r['skill']} {r['delivery']} {r['chars']} chars\n  ask: {r['request']!r}\n  then: {r['reaction']!r}")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
