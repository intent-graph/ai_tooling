# Task outline — keeping the view as running state across a long task

Read this when a task spans many steps, tools, or context resets, or when you notice you are re-reading to re-orient. Assumes `LOD_CORE.md`. Status: a design plus open investigation; see the last section.

## Why
<!-- Lines 7-9 -->

Working memory is finite and gets summarized when long. Without an explicit outline the summary is uniform: everything at the same, degraded height. An explicit outline gives the summarizer, and you, a structure to preserve: settled branches at claim plus pointer, the live branch in full, open branches named.

## The artifact
<!-- Lines 12-19 -->

One file, in the scratchpad, or in the project's working folder when the user wants it to persist, for instance `task_outline.md`:
- Root: the task's purpose in one line, and who receives the final result.
- Branches: one per sub-goal, each with a claim (its state in one line), a certainty (grounded, inferred, open), a pointer to its grounds (files, commands, logs), and its current level in the view (label, claim, full).
- Open list: the open branches, ordered by criticality.
- Next: the one action.
Keep it around forty lines. If it grows, roll up.

## When to update it
<!-- Lines 22-27 -->

- At each step boundary: a verified branch rolls up to claim plus pointer.
- On each surprise: a new open branch appears.
- Before each question to the human and each delivery: the message is shaped from the outline.
- Before any pause you do not control: a long command, a hand-off, a likely context reset.

## Relation to harness mechanisms — verify per environment
<!-- Lines 30-32 -->

As of this writing, Claude Code offers automatic summarization of a long conversation, a to-do list tool in many configurations, a plan mode for designing before acting, per-project memory files, and a session scratchpad directory. None of them is hierarchical by itself. Open questions for an improvement session: does the summarizer preserve a markdown outline's hierarchy? Does a maintained outline file measurably reduce re-orientation reads? Run that experiment before prescribing more than this page.

## Edge cases
<!-- Lines 35-38 -->

- **The user changes the purpose.** Rewrite the root and re-cut the branches. Do not graft the new purpose onto the old tree.
- **Two live branches.** Allowed only when independent. Otherwise finish one.
- **Context reset mid-task.** Read the outline first, then the live branch's pointers, and nothing else until the purpose demands it.
