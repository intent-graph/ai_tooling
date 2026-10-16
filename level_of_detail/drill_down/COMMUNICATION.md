# Communication — set the view from purpose, receiver, channel

Read this when producing anything a person or another agent will read: an answer, a question, a status line, a message, a ticket, a document, a slide, a brief, a comment in code. Assumes `LOD_CORE.md`.

## Table of Contents

1. [The three determinants, in order](#the-three-determinants-in-order) _(Lines 21-42)_
1. [Procedure](#procedure) _(Lines 45-52)_
1. [Questions you ask a human](#questions-you-ask-a-human) _(Lines 55-61)_
1. [Status and hand-off](#status-and-hand-off) _(Lines 64-67)_
1. [Records: tickets, wiki pages, long documents](#records-tickets-wiki-pages-long-documents) _(Lines 70-74)_
1. [Presentations](#presentations) _(Lines 77-82)_
1. [Briefs to another agent](#briefs-to-another-agent) _(Lines 85-88)_
1. [Code, comments, docstrings](#code-comments-docstrings) _(Lines 91-94)_
1. [Worked examples](#worked-examples) _(Lines 97-113)_

---

## The three determinants, in order
<!-- Lines 21-42 -->

**1. Purpose**, stated as a capability the receiver gains. After reading, they can decide X, do Y, trust Z, find W, or resume the work. Write that line before anything else. It tells you where detail goes. Illustrations, not a menu:
- decide → options and trade-offs in full, your recommendation first; mechanism at claim.
- do → the steps they will execute in full; rationale at claim.
- trust or verify → the grounds in full (what you ran, where, when); the story at label.
- find or orient → the map at claim across the whole; nothing in full.
- resume or hand off → the requester's intent in full; the state as claims plus pointers; open in full; next as goal and constraints.
Name the actual capability; do not pick from this list.

**2. Receiver**, modelled as an outline.
- Depth: how far down this tree do they already hold? Everything below their depth is introduced the first time it appears (name it and say what it is in a few words) or left out. A name you cannot afford to introduce should not appear.
- Next action: what will they do with this? Detail that does not change their action is volume.
- Capacity: time, attention, and whether they can open the source themselves.
- Standing: peer, senior, external, first contact. Terseness reads as efficiency downward and as curtness upward or outward. Roll up the content, not the courtesy.
- The requester in a live session is a receiver too. When they ask at claim, answer at claim and offer the drill, unless criticality says otherwise.

**3. Channel**, what it carries and what it costs.
- Structure support: headings, nesting, tables, or flat text only.
- Persistence: a record read later by unknown people, or a live turn read once.
- Length norms of the place, and what the receiver can see next to your text: the diff, the file, the thread, the previous message.
Spend where the channel cannot show by itself; starve what sits one click away.

## Procedure
<!-- Lines 45-52 -->

1. One line: the purpose as a capability. One line: receiver depth and next action. One word: the channel.
2. Sketch the outline of everything you could say, at claim. Mark heights and certainty.
3. Set the view: focus where purpose and criticality demand; roll up the rest to claim or label; drop what the receiver cannot act on. The budget falls out of this step. Never pick a word count first.
4. Roll up branch by branch (`ROLL_UP.md`). Heights will differ; that is right.
5. Order: conclusion or ask first, then grounds in decreasing relevance; introduce before use.
6. Self-check: heights vary; focus justified; every line grounded or marked; the receiver can act without opening your sources.

## Questions you ask a human
<!-- Lines 55-61 -->

The most frequent view you set, and the costliest for the receiver.
- Shape: the ask, your recommendation, and what happens if they do nothing, first, at claim (what you need decided, what you would do, why in one clause). Then the grounds, drilled only as far as the decision needs, visibly separated so they can skip them.
- Batch questions that share context; state the shared context once.
- Never ask what you can find; when finding it is slow or uncertain, ask rather than assume. Never ask for a decision you can safely make and report (`HUMAN_CONTROL.md`).
- Say what changes with the answer. If nothing material changes, do not ask.

## Status and hand-off
<!-- Lines 64-67 -->

- Progress: what changed since last time, at claim; what is next, one line; open branches named. Nothing about how the work felt.
- Hand-off or recap: the requester's intent first, in full: what they asked, what they ruled out, what their corrections imply, each with its evidence, inferences marked inferred. It is the one branch that exists only in the conversation. Then done (claim plus pointer), open (full), next (goal and constraints; steps only where the requester dictated them). Point to what is on disk; never restate it, and never say how to read it: the receiver sets its own view. A reader with none of your context must be able to resume from it.

## Records: tickets, wiki pages, long documents
<!-- Lines 70-74 -->

- Read later, by people with less context than the thread. Introduce more, assume less.
- Rationale before mechanism. Name what was ruled out and why; it stops re-litigation.
- Funnel: the wide area, then the part, then the exact thing. Each section sits one rung below the previous, answers its own question once, and stops. Repeating the section above means you are in the wrong one.

## Presentations
<!-- Lines 77-82 -->

- One claim per slide title. The slide body is that claim's children at claim; the grounds go to notes or appendix.
- The deck's outline is the talk's outline. Heights differ across slides on purpose: one slide a single number, the next a whole mechanism.
- A deck outline is itself a view at claim: one line per slide, the argument inside the slide, never in the outline. If your outline reads like a memo, you drilled where the receiver asked for labels.
- Example, a leadership quarter review in five titles: "Revenue +8%, but a 6% churn in the last week: run-rate roughly flat" · "The churn: one customer, pricing cited; two flat regions as context; whether it generalises is open" · "Self-service portal: tickets down 20%" · "New line shipped to 40 pilots; conversion open" · "Decide: hiring plan 3 roles behind, and the engineering-lead search". Slide 1 carries an arithmetic the facts did not state; slide 3 is a single fact; both are right at their height.

## Briefs to another agent
<!-- Lines 85-88 -->

- The brief is a view: the target in full (what to produce, constraints, exits), the surroundings at claim (where this sits, what not to touch), the rest absent.
- Ask for the return as a rolled-up claim with grounds on disk. A return that inlines everything defeats the delegation.

## Code, comments, docstrings
<!-- Lines 91-94 -->

- Comment at the height the code cannot show: why, what was ruled out, the invariant. Never restate the line below.
- A module docstring is the module's claim; a function docstring is its claim plus its contract; the code is the full.

## Worked examples
<!-- Lines 97-113 -->

**A question to the requester.**
Before: fourteen lines describing everything found in three files, then "what do you want me to do?"
After:
> Keep the retry loop, or replace it with the queue's redelivery? I would replace it: the loop duplicates redelivery and hides the failure count.
> Grounds, skip unless wanted: the loop at `worker.py::run` retries three times with a sleep; the queue already redelivers five times with backoff; two of last week's incidents show double-processing consistent with both being active.

**A status line.**
> Venue signed; caterer on budget after dropping dessert. Next: chase the AV vendor by Friday, else switch to the backup (10% more). Open: banner reprint cost, waiting on the printer.

**A brief to a helper.**
> Target: audit every claim marked "observed" under branch AUTH of `graph.yaml` against the current code. Per claim return holds / drifted / missing, with the file you opened. Do not edit anything.
> Surroundings: the graph is the source of truth for an intent tool; AUTH is one of six top branches.
> Return: at most 80 words here, full report in `review/auth_audit.md`.

**A wiki section that started at the wrong height.**
Before: "Fixed the cutoff." After, funnelled: monthly invoicing → the statement a customer receives → the cutoff that decides which month a payment lands in; today a payment made at 23:59 local time lands in the next month for customers east of UTC.
