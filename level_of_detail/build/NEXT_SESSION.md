# Next session — how to improve this artifact

Purpose: the entry point for a session (or a human) whose job is to make the agent-facing files better. Read this first; it tells you what to read, what is open, and which experiment comes next.

## Table of Contents

1. [What you are improving, and what you must preserve](#what-you-are-improving-and-what-you-must-preserve) _(Lines 18-21)_
1. [Read in this order](#read-in-this-order) _(Lines 24-33)_
1. [Open questions](#open-questions) _(Lines 36-45)_
1. [Experiments, in order](#experiments-in-order) _(Lines 48-54)_
1. [Reviewer protocol (used in round 1, reuse it)](#reviewer-protocol-used-in-round-1-reuse-it) _(Lines 57-62)_
1. [When you finish a round](#when-you-finish-a-round) _(Lines 65-69)_

---

## What you are improving, and what you must preserve
<!-- Lines 18-21 -->

- Improve: `../LOD_CORE.md` and `../drill_down/*.md` — clarity, priming, actionability, coverage of edge cases, and their effect on a fresh agent's behaviour.
- Preserve: the decisions in `DECISIONS.md` unless you log a new decision that supersedes one, with its reason and the ruled-out alternative. The core's length budget. The absence of fixed budgets. Task-agnosticism. Self-containment.

## Read in this order
<!-- Lines 24-33 -->

1. `../README.md` — the folder at label.
2. `../LOD_CORE.md` — the artifact you are improving, in full.
3. This file.
4. `DECISIONS.md` — why the artifact is the way it is.
5. `VOCABULARY.md` — the words to use, and the words not to use.
6. `ELICITATION_ROUND_1.md` — the user's intent in their own words.
7. `RECIPE.md` — the procedure, when you are about to rebuild rather than patch.
8. `SOURCES.md` and the sources themselves — only for the branch you are drilling.

## Open questions
<!-- Lines 36-45 -->

- **Loading mechanism: wired (D50).** One `@import` of `LOD_CORE.md` in your global instructions loads the core in every session of every project; satellites stay behind the core's pointer section. Now due: repeat the overlap experiment through the real import rather than an inlined block, on a task with a human-facing output and a question to the human, and check whether the two fixes it produced (D43, D44) hold. Watch for cost complaints on short sessions; reversal is deleting that one `@import` line.
- **"branch" after naming git.** Two reviewers confirmed the git pull; the core now names and dismisses it (D37). Re-test on a coding task in round 3; if it still interferes, the fallback is renaming to a term without a version-control meaning.
- **Over-production on outline-shaped deliverables.** A counterweight was added (D41). Verify on a deck or agenda task that outputs stay one line per node.
- **Open-branch invention.** Bounded in invariant 3 (D40). Verify that agents still surface genuine gaps and no longer manufacture plausible ones.
- **Height as an executable test.** The first self-check now counts facts behind three lines (D39). Verify it takes under a minute and does not invite padding.
- **Hand-off, intent first (D53).** Verify on a live hand-off that the receiver resumes without asking what the user wants, and that the writer no longer plans the receiver's steps.
- **Task outline versus harness.** How the harness summarizes long contexts, whether it preserves an outline's hierarchy, and whether a maintained outline file reduces re-orientation. See `../drill_down/TASK_OUTLINE.md`.
- **Reviewer caveats to carry.** Both behavioural tests were n=2 and self-graded; round 2's "normal" outputs were written after one read of the files, so its deltas may understate the effect. The substantive catches (an irreversible item surfaced; a rename that would break references dropped; a headline number cancelled by a churn) are traceable to specific lines; stylistic deltas less so.

## Experiments, in order
<!-- Lines 48-54 -->

0. **Round 3 review**, now unblocked (the mechanism is wired, D50): same protocol, fresh Opus, on the current core. Before anything else, have it read only the first paragraph and write what it would now do differently; that is the test of the opening. Then ask whether N-1…N-9 from round 2 are resolved, and include one coding task with a literal git branch and one outline-shaped deliverable.
1. **Overlap and conflict (from Q3): repeat now that it is wired.** An earlier experiment inlined the core as standing instructions over a real read-only task; findings folded into D43–D46 (transcript not retained). Repeat through the real `@import` (D50), with a task that includes a question to the human, and check the user's personal communication instructions for overlap, which that experiment did not exercise.
2. **Priming audit (from Q5).** Ask several fresh models, one term at a time and then in the sentences where each appears, what the term evokes. Compare with `VOCABULARY.md`; adjust.
3. **Failure analysis of past sessions (from Q15).** A separate project: a session reads past transcripts, finds where detail was uniform, questions were unshaped, or settled branches were over-explained, and produces examples. Those examples become worked examples in `drill_down/` and test cases for experiment 4.
4. **Evaluation without the human (from Q16).** Paired tasks; one agent with the core loaded, one without; an Opus judge with a rubric derived from the core's self-check (heights vary, focus justified, lines grounded, receiver can act). Measure before prescribing. Design needs: tasks with a known receiver, a judge that does not see which arm is which, and a check that the judge itself is not trimming.

## Reviewer protocol (used in round 1, reuse it)
<!-- Lines 57-62 -->

- Model: Opus, fresh context, no access to this conversation.
- Inputs: the agent-facing files only, plus the brief. Not `build/`.
- Brief asks for: self-sufficiency for a non-software task; per-term associations evoked; contradictions or ambiguities; rules that are not actionable; what a fresh agent would do differently on two sample tasks (a question to a requester; a status message); anything in the core that belongs in a satellite or the reverse; length.
- Output: a report outside the repository, findings ranked by severity, each with a quote and a proposed rewrite. Return to the caller under eighty words.

## When you finish a round
<!-- Lines 65-69 -->

- Log changes in `DECISIONS.md`.
- Log the reviewer's findings in `DECISIONS.md`; do not keep the report.
- Update this file's open questions and experiment list.
- Run `md-structure-sync` on `build/` and `drill_down/` (not on the core, which carries no table of contents).
