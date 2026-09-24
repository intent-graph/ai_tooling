# Roll up — lossy compression, never trimming

Read this when you must reduce a branch (a pile of facts, a long section, a finished piece of work) to fewer lines without losing what the receiver needs. Assumes `LOD_CORE.md`.

## Table of Contents

1. [What rolling up is](#what-rolling-up-is) _(Lines 21-26)_
1. [The three moves, in order](#the-three-moves-in-order) _(Lines 29-33)_
1. [Density and opacity](#density-and-opacity) _(Lines 36-40)_
1. [Two tests on every line](#two-tests-on-every-line) _(Lines 43-46)_
1. [Certainty after roll-up (invariant 2)](#certainty-after-roll-up-invariant-2) _(Lines 49-54)_
1. [Form: structure is cheap, prose is expensive](#form-structure-is-cheap-prose-is-expensive) _(Lines 57-65)_
1. [Grounding pass, last](#grounding-pass-last) _(Lines 68-74)_
1. [Edge cases](#edge-cases) _(Lines 77-85)_
1. [Worked examples](#worked-examples) _(Lines 88-103)_

---

## What rolling up is
<!-- Lines 21-26 -->

- You start with a pile of facts, more than fit.
- Each time you group facts into one claim you lose some information and save some volume. A good group saves a lot and loses little; that happens when the facts are alike. Grouping unrelated facts also saves words, but the claim that comes out either says nothing or misstates them: the loss exceeds the saving.
- The work is finding the few groups that carry the most with the least distortion. It is not shortening every line a little.
- Trimming (shorten everything uniformly) leaves a signature: uniform middle height, bare identifiers strung together, dropped verbs, lines the receiver must decode by opening the source.

## The three moves, in order
<!-- Lines 29-33 -->

1. **Prune.** Drop what the receiver would never act on: the incidental, the hyper-specific, anything the artifact next to your text shows plainly. Cheapest saving; do it first; it shrinks what you have to group.
2. **Group** into one to four claims per branch. That ceiling is about what you *show* a receiver in one place; the outline underneath may hold more children (typically two to six, see `DRILL_DOWN.md`), rolled up further for this view. Like with like; a group can itself be a group of groups. State the group's claim, not its members. Members appear only where the receiver would act differently knowing them, and then as names in parentheses under a claim that already said what class of thing they are. One to four is a ceiling on the outcome, not a quota: four genuine groups stay four; one stays one; never force unrelated facts together to hit a number.
3. **Preserve raw, rarely.** A single fact stands unrolled beside the groups only when the branch cannot be understood without it *and* rolling it up would break that understanding. Both must hold. Most branches have none.

## Density and opacity
<!-- Lines 36-40 -->

- **Volume** is how much there is to read. Every fact, group, and word adds to it.
- **Opacity** is how much a line costs to decode: identifiers to hold at once, knowledge assumed, causal steps the receiver must supply.
- Density is the aim; opacity is the failure. Good compression raises meaning per word and keeps the meaning reachable. Bad compression saves the same words by making the receiver reconstruct what was dropped. That moves the cost from you to them; it does not remove it.

## Two tests on every line
<!-- Lines 43-46 -->

- **Actionable at this height?** A coarse line is right where the view is meant to be coarse ("authentication changed in three services" in an overview) and wrong where the receiver came for the members (the same words where they expected to learn which three and what changed). The failure is not vagueness; it is a line the receiver has to open the source to use.
- **Reachable by this receiver?** If the line needs three identifiers held at once, or a step they must supply, either spend the words that make it reachable or cut the line.

## Certainty after roll-up (invariant 2)
<!-- Lines 49-54 -->

- Re-derive it. The rolled-up claim's certainty comes from what grounds *that claim*, not from its most confident child.
- It may go up: the aggregate is grounded while members stay open. Who won is grounded; each vote is open. "The suite passes" is grounded while the cause of one flaky test is open.
- It may go down: members grounded one by one, the claim about their combination only inferred. Each step tested, the end-to-end path never run.
- Language follows: inference words survive roll-up. A shorter line must not sound surer than the long one did.

## Form: structure is cheap, prose is expensive
<!-- Lines 57-65 -->

- The same content costs roughly three times more as sentences than as labelled bullets.
- Nested bullets state belonging, containment, dependency, and cause for free: a child bullet says "part of", "inside", "because of" without a word. One level of nesting freely; a second only where the relation is the point.
- Arrows for causal chains, bullets for lists, a label and a colon for a group.
- Full sentences only where a connective carries the logic: a requirement with an exception, a trade-off, an argument. Keep "because", "so", and the conclusion; drop the padding.
- Verbs first, present tense. No throat-clearing ("note that", "it is worth", "in order to").
- Cheap form is free only while the claim stays reachable. A label-and-colon line that drops the verb stating the relation has bought volume with opacity.
- Compression never changes a claim and never creates one.

## Grounding pass, last
<!-- Lines 68-74 -->

- For each line, name what makes it true: a place in the artifact, a thing you read, a source you can cite with its date.
- A group is grounded only when every member holds, not when one does. "The four that read X are fixed" means you checked all four.
- A claim about what you did *not* change, or what is *not* there, cannot be found in a diff or a listing. Cite what you inspected instead.
- Re-check first the lines you shortened last. Budget pressure produces confident short clauses, which is the exact shape an invented fact takes. Observed: in a controlled trial, fabrications appeared only under the tightest budget, and only in the last-compressed lines; the writer's own final pass caught them.
- A line you cannot ground is cut, or marked as inference ("appears to", "presumably").

## Edge cases
<!-- Lines 77-85 -->

- **Independent causes do not group.** Grouping works on enumerations of like things. A failure with three unrelated causes is three claims, not one "several causes".
- **Reasoning resists telegraphic form.** Requirements, trade-offs, and arguments keep their connectives; compress the padding, not the logic. Telegraphic style suits causal chains and lists, not the argument that justifies them.
- **Caps versus targets.** A hard cap you can only meet by dropping a fact is the wrong constraint. Treat a budget as a target, and when you overrun, say by how much and which fact you kept.
- **Jointly unsatisfiable rules.** "Mostly section X" and "no section over a third" cannot both hold on a small piece. When rules collide, keep the one that serves the receiver's purpose and name the one you dropped.
- **Names versus syntax.** A name, once introduced, can be carried by the receiver. Syntax cannot be rolled up: no before/after lines, no expressions, no query paraphrase. Name the thing and say in words what changed about it.
- **Rolling up finished work.** Claim plus pointer to where the grounds live (file, command, test name, log), never the grounds inline.
- **The receiver already knows this material.** They are not the receiver to write for. Write for the competent reader one step removed; the insider skims for free.

## Worked examples
<!-- Lines 88-103 -->

**Seven facts to three claims.** Raw: three legacy formatters removed · `ExportOptions` renamed · the scheduler entry point takes a spec · the runner entry point takes a spec · four `open()` call sites moved to the storage layer · `python-dateutil` added · `TZ` env var dropped.
Rolled up: "Breaks callers: 3 legacy formatters removed, `ExportOptions` renamed. Entry points (scheduler, runner) take the new spec. Runtime: all file access via the storage layer; `python-dateutil` added, `TZ` env var dropped."
Three groups at three heights: two facts, two facts, three facts. Members named only where a caller would act differently.

**A causal chain, 46 words to 13.** "When the nightly job encounters a row whose parent record has already been archived, it currently raises an exception, which causes the entire batch to be retried from the beginning on the next run and produces duplicate notifications for every row that had already been processed successfully."
Rolled up: "Archived parent → job raises → whole batch retried → duplicate notifications for every processed row."

**An argument, 51 words to 21.** "The two checks together are sufficient because the first one rejects any row whose country code is absent from the reference table, and the second one rejects any row whose date range overlaps an existing range, so a row that passes both cannot be either unmatched or double-counted."
Rolled up: "Two checks partition the failure space: unknown country, and overlapping range. A row passing both cannot be unmatched or double-counted." The connectives and the conclusion survived; only padding went.

**Eleven facts about an event, for a manager reading on a phone.** Raw: venue confirmed · caterer 20% over budget, can cut dessert to land on it · AV vendor silent for 6 days, backup vendor costs 10% more · two speakers confirmed, one pending a week · registration at 60% with 3 weeks left · marketing wants a second email blast, last year's lifted registration 15% · sponsor wants a logo change on the banner · banner already at the printer.
Rolled up, decisions first, heights differing: "Needs you: the banner is at the printer and the sponsor wants a logo change; reprint cost unknown; I hold the print until you say go or no. Registration 60% with 3 weeks left; a second blast lifted 15% last year, so about 69%, still short: I would send it and add a speaker-referral push. Handled: caterer on budget by dropping dessert; backup AV engaged if the vendor stays silent past Friday (10% more); venue and two speakers confirmed, the third chased."
The irreversible item leads and gets four clauses; the venue gets two words. "Reprint cost unknown" is a fact left open rather than invented.

**A verified branch of your own work.** Before: nine lines listing every command run and its output. After: "Migration applied on DEV; 3 checks green (row counts, FK integrity, sample query); log at `scratch/mig_check.txt`." Grounded, because the log exists and you read it.
