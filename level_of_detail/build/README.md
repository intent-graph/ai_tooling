# build/ — the authoring record behind the LOD practice

This folder is not the product. Agents load `../LOD_CORE.md` and `../drill_down/*.md`.
This folder records how that product was made, why it says what it says, and what to
read before changing it. To use the practice, read `../README.md` instead.

## Start here
<!-- Lines 9-13 -->

To improve `LOD_CORE.md` or `drill_down/`, start at `NEXT_SESSION.md`: what to read,
in what order, what is open, and which experiment comes next. Read the decision log
before editing the core.

## What each file is for
<!-- Lines 16-26 -->

- `NEXT_SESSION.md` — entry point for an improvement session: what may change, what
  must be preserved, reading order, open questions, next experiments.
- `DECISIONS.md` — every choice behind the agent-facing files, why, and what was ruled out.
- `ELICITATION_ROUND_1.md` — the original brief in the requester's words, and the
  questions that shaped the first version.
- `VOCABULARY.md` — the terms this practice uses, with their one-line meaning, and the
  terms it deliberately avoids.
- `SOURCES.md` — every source that fed the practice, what was taken from each, what was left out.
- `RECIPE.md` — the procedure that produced the core and its satellites, so it can be redone.

## Relation to the rest of the folder
<!-- Lines 29-32 -->

- `../LOD_CORE.md`, `../drill_down/` — compiled, agent-facing, self-contained.
- `build/` — the human-readable source behind them.

## Rules for improvers
<!-- Lines 35-39 -->

- Do not grow the core past its length budget without removing something; depth goes to a satellite.
- Log every change in `DECISIONS.md`, with the alternative ruled out.
- Keep agent-facing files task-agnostic.
- Review changes with a model other than the author's; log its findings in `DECISIONS.md` and do not keep the report.
