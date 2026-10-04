#!/usr/bin/env python3
"""Measure how sessions brief their sub-agents, from Claude Code transcripts.

Reads every *.jsonl transcript under the projects directory (main sessions and sub-agents),
finds each Agent / Task call, and reports, over all calls:

    adoption   share of calls preceded, in the same session, by loading the skill
    size       prompt and return size (the return of a background agent is read from its
               task notification, not from the launch receipt)
    pasting    share of prompt text repeated from an earlier prompt in the same session, and
               share copied verbatim from tool results the session had already read
    shape      share of prompts with an explicit model, a typed agent, the three-level return,
               an absolute result path, and the length the lint hook would block

Usage: audit_subagent_calls.py [--projects-dir DIR] [--since YYYY-MM-DD]
"""
import argparse
import json
import re
from pathlib import Path

SKILL_NAMES = ("subagent-orchestration", "subagent-call")
AGENT_TOOLS = {"Agent", "Task"}
HOOK_LIMIT = 6000
LINE_NUMBER = re.compile(r"^\s*\d+[\t→]")


def norm(line: str) -> str:
    return re.sub(r"\s+", " ", LINE_NUMBER.sub("", line)).strip(" -*>#|`")


def text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
    return ""


def audit_session(path: Path, since: str) -> list[dict]:
    calls, receipts, notified = {}, {}, {}
    read_lines, prompt_lines, skill_at = set(), set(), None
    for i, raw in enumerate(path.read_text(errors="ignore").splitlines()):
        try:
            ev = json.loads(raw)
        except ValueError:
            continue
        if since and (ev.get("timestamp") or "") < since:
            continue
        content = (ev.get("message") or {}).get("content")
        if isinstance(content, str) and "<task-notification>" in content:
            tid = re.search(r"<tool-use-id>(\S+?)</tool-use-id>", content)
            res = re.search(r"<result>(.*)</result>", content, re.S)
            if tid and res:
                notified[tid.group(1)] = notified.get(tid.group(1), 0) + len(res.group(1))
            continue
        if not isinstance(content, list):
            continue
        for c in content:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use":
                inp = c.get("input") or {}
                if c.get("name") == "Skill" and any(n in json.dumps(inp) for n in SKILL_NAMES):
                    skill_at = i if skill_at is None else skill_at
                if c.get("name") in AGENT_TOOLS:
                    lines = [norm(l) for l in (inp.get("prompt") or "").splitlines()]
                    lines = [l for l in lines if len(l) >= 40]
                    calls[c["id"]] = dict(
                        at=i, inp=inp,
                        repeated=sum(len(l) for l in lines if l in prompt_lines),
                        copied=sum(len(l) for l in lines if l in read_lines))
                    prompt_lines.update(lines)
            elif c.get("type") == "tool_result":
                t = text_of(c.get("content"))
                if c.get("tool_use_id") in calls:
                    receipts[c["tool_use_id"]] = t
                else:
                    read_lines.update(l for l in map(norm, t.splitlines()) if len(l) >= 40)
    rows = []
    for tid, call in calls.items():
        p, inp, r = call["inp"].get("prompt") or "", call["inp"], receipts.get(tid, "")
        rows.append(dict(
            prompt=len(p),
            # a background result that came back by hand-back message is not in the transcript
            ret=notified.get(tid) if r.startswith("Async agent launched") else len(r),
            repeated=call["repeated"], copied=call["copied"],
            skill=skill_at is not None and skill_at < call["at"],
            model=bool(inp.get("model")),
            general=inp.get("subagent_type") in (None, "general-purpose"),
            levels=bool(re.search(r"\bL1\b", p) and re.search(r"\bL2\b", p)),
            result_path=bool(re.search(r"/[\w./-]+/result\.md", p)),
            over_limit=len(p) > HOOK_LIMIT))
    return rows


def quantiles(values: list[int]) -> str:
    v = sorted(values)
    return f"p50 {v[len(v) // 2]:,} · p90 {v[int(len(v) * .9)]:,} · max {v[-1]:,}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--projects-dir", type=Path, default=Path.home() / ".claude" / "projects")
    ap.add_argument("--since", default="", help="ISO date; ignore events before it")
    args = ap.parse_args()
    sessions = {f: audit_session(f, args.since) for f in args.projects_dir.rglob("*.jsonl")}
    rows = [r for rs in sessions.values() for r in rs]
    if not rows:
        raise SystemExit("no sub-agent calls found")
    n = len(rows)
    share = lambda k: f"{100 * sum(r[k] for r in rows) / n:.0f}%"
    p_total = sum(r["prompt"] for r in rows)
    print(f"calls {n} in {sum(1 for rs in sessions.values() if rs)} sessions"
          + (f" since {args.since}" if args.since else ""))
    print(f"adoption   skill loaded before the call: {share('skill')}")
    print(f"size       prompt chars {quantiles([r['prompt'] for r in rows])}; total {p_total:,}")
    known = [r["ret"] for r in rows if r["ret"] is not None]
    print(f"           return chars {quantiles(known)}; total {sum(known):,} "
          f"({n - len(known)} returns not in the transcript)")
    print(f"pasting    repeated from an earlier prompt: "
          f"{100 * sum(r['repeated'] for r in rows) / p_total:.0f}% of prompt chars; "
          f"copied verbatim from what the session read: "
          f"{100 * sum(r['copied'] for r in rows) / p_total:.0f}%")
    print(f"shape      explicit model {share('model')} · general-purpose {share('general')} · "
          f"three levels {share('levels')} · result.md path {share('result_path')} · "
          f"over {HOOK_LIMIT} chars {share('over_limit')}")


if __name__ == "__main__":
    main()
