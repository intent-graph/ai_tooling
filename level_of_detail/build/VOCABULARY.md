# Vocabulary — the terms this practice uses, and the terms it avoids

Purpose: a quick reference for anyone editing the agent-facing files. Use the terms below with the
meaning given, consistent with `LOD_CORE.md`'s own Vocabulary section; do not reach for a synonym
mid-file. Change a term here first; then in `LOD_CORE.md` and `drill_down/`.

## Table of Contents
<!-- Lines 9-11 -->

1. [Terms to use](#terms-to-use) _(Lines 15-39)_
1. [Terms not to use](#terms-not-to-use) _(Lines 42-54)_

## Terms to use
<!-- Lines 15-39 -->

| Term | Meaning here |
|---|---|
| **Level of Detail, LOD** | several representations of the same thing at different resolutions, chosen per branch, under a budget that is an output of the decision, not an input to it |
| **outline** | the tree of what you know about a task: facts and claims at various resolutions, connected across branches |
| **branch** | a node with its descendants, a part of the outline — not a git branch and not a variant: an outline has no versions, only parts |
| **root** | the one claim the whole task answers |
| **fact** | a leaf: one grounded observation |
| **claim** | any node: what its children add up to, at lower precision |
| **height** | how many facts a claim rolls up; a property of the claim, not of how much of it you show |
| **level** | how much of a claim you show — label, claim, or full (below); distinct from height, which is a property of the claim itself, not of how much you reveal |
| **label / claim / full** | the three levels at which a node can be shown: name only; one line with its certainty; the claim plus whichever grounds bear on the purpose |
| **roll up** | replace children by the claim they add up to — lossy compression, never trimming |
| **drill down** | go one resolution finer, by revealing children you hold or by acquiring them |
| **view** | the outline with one level chosen per branch |
| **focus** | one branch shown in full; more than one only when they are independent, never by default |
| **grounded / inferred / open** | the certainty a claim carries: grounded (you can name what makes it true), inferred (follows from grounded facts, not observed), open (unknown, undecided, or contested — say which) |
| **thin end-to-end version** | the smallest version of the whole that runs or reads start to finish, built before any one part goes to full detail |
| **SADT** | named twice, as the process instance of the same general idea: a parent box and its child diagram share a boundary |

**Intended connections.** Beyond SADT (above), the practice deliberately evokes: OLAP roll-up and
drill-down (the operation names); real-time graphics level of detail (resolution traded for
purpose, not quality lost); Toulmin's model of argument (claim, grounds, warrant, behind "claim"
and "grounded"). See `SOURCES.md` for the full source list.

## Terms not to use
<!-- Lines 42-54 -->

These were considered and rejected for the agent-facing files (`LOD_CORE.md`, `drill_down/*.md`).
If one appears there, it is a regression — replace it with the table above.

- **intentnode, intentlink** — vocabulary of one specific tool (IntentGraph); this practice must stand alone.
- **lens** — same reason, and "lens" also collides with the optics and functional-programming senses.
- **frontier** — tied to that tool's exploration model, not a general LOD concept.
- **skeleton, lean, walking skeleton** — "skeleton" primes anatomy and unfinished "skeleton code"; a label-level node is complete at its resolution, not unfinished.
- **epistemic state** — academic register where "certainty" (grounded / inferred / open) says the same thing plainly.
- **projection, ProjectionIG** — another tool's formalism, not a general concept.
- **summarize** — primes summarization as models perform it: trimming. Roll-up is grouping into a new, lower-resolution claim, not shortening.
- **compress (as the primary verb)** — primes lossless compression (gzip); used at two places as a clarifier ("lossy compression, never trimming"), never as the main verb for the operation.
- **abstraction level** — primes object-oriented abstraction, which removes properties; LOD keeps meaning and drops resolution instead.
