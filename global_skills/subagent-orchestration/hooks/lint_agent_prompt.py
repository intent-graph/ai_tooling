#!/usr/bin/env python3
"""PreToolUse hook: lint every sub-agent brief before it is sent.

Blocks an Agent call, with a reason the model sees and can act on, when the brief breaks one
of the mechanical rules of the subagent-orchestration skill:

    model     no explicit `model`
    size      the prompt is longer than MAX_PROMPT_CHARS: something on disk was pasted or
              restated instead of pointed to
    levels    the prompt does not ask for the three-level return (L1 and L2 never named)

Anything unexpected (unparsable input, another tool) lets the call through: a lint must never
stop work because of its own failure.

Wire it in ~/.claude/settings.json:
    "hooks": {"PreToolUse": [{"matcher": "Agent", "hooks": [{"type": "command",
      "command": "python3 ~/.claude/skills/subagent-orchestration/hooks/lint_agent_prompt.py"}]}]}

Requires Python 3.10 or later. Self-test: python3 lint_agent_prompt.py --self-test
"""
import json
import re
import sys

MAX_PROMPT_CHARS = 6000
AGENT_TOOLS = {"Agent", "Task"}
# subagent_type values whose own definition fixes the output format; add names here to skip
EXEMPT_SUBAGENT_TYPES: set[str] = set()

FIX = {
    "model": "Set `model` explicitly: haiku for mechanical work, sonnet for analysis, judgment "
             "or code, opus only after the user confirms.",
    "size": "The brief is {n} characters (limit {limit}). Something on disk is pasted or "
            "restated: point to it instead (absolute path plus the part to read). Write the "
            "session-only context once to <run_dir>/brief_shared.md and point to that.",
    "levels": "Ask for the result at three levels in <run_dir>/<slot>/result.md: L1 headline, "
              "L2 claims, L3 full, each readable alone; name the facts to pin; say which levels "
              "come back inline (L3 stays in the file).",
}


def violations(tool_input: dict) -> list[str]:
    if tool_input.get("subagent_type") in EXEMPT_SUBAGENT_TYPES:
        return []
    prompt = tool_input.get("prompt") or ""
    found = []
    if not tool_input.get("model"):
        found.append(FIX["model"])
    if len(prompt) > MAX_PROMPT_CHARS:
        found.append(FIX["size"].format(n=len(prompt), limit=MAX_PROMPT_CHARS))
    if not (re.search(r"\bL1\b", prompt) and re.search(r"\bL2\b", prompt)):
        found.append(FIX["levels"])
    return found


def decision(event: dict) -> dict | None:
    if event.get("tool_name") not in AGENT_TOOLS:
        return None
    found = violations(event.get("tool_input") or {})
    if not found:
        return None
    reason = ("Sub-agent brief rejected by the subagent-orchestration lint. Fix and resend:\n- "
              + "\n- ".join(found)
              + "\nRules: skill subagent-orchestration, sections 2 to 4.")
    return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                   "permissionDecision": "deny",
                                   "permissionDecisionReason": reason}}


def self_test() -> None:
    good = {"tool_name": "Agent", "tool_input": {
        "model": "sonnet", "subagent_type": "Explore",
        "prompt": "Goal: x.\nOutput: /abs/run/01_x/result.md with L1 headline, L2 claims, L3 full."}}
    cases = [
        ("good brief passes", good, 0),
        ("other tool ignored", {"tool_name": "Read", "tool_input": {}}, 0),
        ("no model", {**good, "tool_input": {**good["tool_input"], "model": None}}, 1),
        ("no levels", {**good, "tool_input": {**good["tool_input"], "prompt": "Goal: x."}}, 1),
        ("too long", {**good, "tool_input": {**good["tool_input"],
                      "prompt": good["tool_input"]["prompt"] + "x" * MAX_PROMPT_CHARS}}, 1),
        ("all three", {"tool_name": "Agent", "tool_input": {"prompt": "y" * 7000}}, 3),
    ]
    failed = 0
    for name, event, expected in cases:
        out = decision(event)
        got = 0 if out is None else out["hookSpecificOutput"]["permissionDecisionReason"].count("\n- ")
        status = "ok  " if got == expected else "FAIL"
        failed += got != expected
        print(f"{status} {name}: {got} violation(s), expected {expected}")
    sys.exit(1 if failed else 0)


def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
    try:
        out = decision(json.load(sys.stdin))
    except Exception:
        sys.exit(0)
    if out:
        print(json.dumps(out))
    sys.exit(0)


if __name__ == "__main__":
    main()
