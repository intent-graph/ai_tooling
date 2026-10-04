# global_skills

Claude Code skills meant for every project, not only this repository. Each one is installed
user-wide by symlinking its folder into `~/.claude/skills/`; Claude Code then lists its
description in every session.

Unlike `.claude/skills/` (skills that apply only while working in this repository), nothing
here is discovered automatically. This avoids the same skill appearing twice when working
inside `ai_tooling/`.

## Skills
<!-- Lines 13-17 -->

| Skill | What it does |
|---|---|
| [`subagent-orchestration/`](subagent-orchestration/SKILL.md) | Mandatory before every sub-agent call. Briefs point to files instead of pasting or restating them; each agent writes to a fixed slot in a run directory; agents are chained through files; every result comes back at three self-contained levels (L1 headline, L2 claims, L3 full on disk) with salient facts pinned verbatim. Optional lint hook in `hooks/`; measurements and decisions in `build/`. Long-form rationale for the typed payload: [`../howto/programming_subagents.md`](../howto/programming_subagents.md). |

## Install
<!-- Lines 20-32 -->

From the root of this repository:

```bash
ln -s "$PWD/global_skills/subagent-orchestration" ~/.claude/skills/subagent-orchestration
```

A skill that must run before a given action also needs one line in the user's global
instructions (`~/.claude/CLAUDE.md`) naming it as mandatory; the description alone makes it
known, not binding.

A project can add its own rules on top (its guideline paths, a stricter model policy) with a
small project skill that says "load `subagent-orchestration` first, then apply these".
