# Agent contract (CLAUDE.md) — level_of_detail/

You are in the folder that ships the level-of-detail practice. Read [`README.md`](README.md) for the map.

## What is what

- `LOD_CORE.md` and `drill_down/` are **compiled, agent-facing** artifacts: about one hundred lines for the core, task-agnostic, optimized for an agent under a tight context budget, self-contained.
- `build/` is the **source**: decisions, vocabulary, ingredients, recipe, the user's words. Human-readable.

## Rules

- Improving the artifact starts at `build/NEXT_SESSION.md`. Do not patch the core from intuition.
- Never grow the core past about one hundred lines without removing something. Depth goes to `drill_down/`.
- Never add fixed budgets, word counts, or per-channel targets to agent-facing files. The derivation procedure is the rule.
- Change a term in `build/VOCABULARY.md` first, then everywhere. Search the agent-facing files for the "Terms not to use" list before finishing.
- Log every decision in `build/DECISIONS.md` with the ruled-out alternative.
- Do not import the formalism of any single tool into agent-facing files; they must stand alone.
- Review with a model other than the author's; log its findings in `build/DECISIONS.md` and do not keep the report.
- To load the core in every session, add one `@import` of `LOD_CORE.md` to your global instructions (D50); do not add a second loading mechanism without a logged decision in `build/DECISIONS.md`.
- Run `md-structure-sync` on `build/` and `drill_down/` after edits; not on the core.
