# Agent contract (CLAUDE.md) — global_skills/

Skills here are installed user-wide by symlink and load in sessions of any project. See
[README.md](README.md).

## Rules

- A skill folder is self-contained: its files link only to files inside the same folder. A
  relative link that leaves the folder breaks once the folder is reached through
  `~/.claude/skills/`. Links from `README.md` files to the rest of the repository are fine.
- Public repository: no absolute or home paths, no private project names. Examples use
  `/abs/path/...`.
- `SKILL.md` stays under about 200 lines; depth goes to a sibling file the skill points to.
- `subagent-orchestration`: the working rules live in its `SKILL.md`, `return_levels.md` and
  `contract_mode.md`; the long-form rationale for the typed payload in
  `../howto/programming_subagents.md`. Change the template here, not there. Before changing the
  skill, read `subagent-orchestration/build/README.md` and re-run its audit before and after.
