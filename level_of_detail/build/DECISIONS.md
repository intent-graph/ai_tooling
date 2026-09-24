# Decisions — what was decided, why, and what was ruled out

Purpose: the durable record of every design decision behind the agent-facing files. A future session improves the artifact by revisiting these, not by guessing. Each entry: decision, why, ruled out, source. Sources "Q<n>" refer to `ELICITATION_ROUND_1.md`.

## Shape of the deliverable
<!-- Lines 7-37 -->

**D1 — A folder, not a file.** Compiled agent-facing core (`LOD_CORE.md`) plus on-demand satellites (`drill_down/`), plus the builder-facing source (`build/`), plus reviews (`review/`). Why: the user wants the "compiled binary", the "source code", and the intent behind the source, so a future session can redo and improve. Ruled out: a single flat file. Source: Q1.

**D2 — The core is about one hundred lines, mostly self-sufficient, and points to satellites only for edge cases and depth.** Why: the output is itself an exercise in level of detail; a short file that points further when required. Ruled out: a long flat file; a core that depends on satellites to be actionable. Source: Q2, Q14.

**D3 — Two audiences, two kinds of artifact.** Agent-facing files are optimized for an agent under extreme space constraint and are task-agnostic (the agent may be preparing a deck or a message, not building software). Builder-facing files are human-readable and keep the why and the ruled-out options. Why: content for the agent must be geared for the agent; the recipe must be understandable by a human or a high-context session. Ruled out: one voice for both. Source: Q4, Q11.

**D4 — No fixed budgets or word counts anywhere in agent-facing files.** The budget is an output of the view decision (purpose, criticality, certainty, receiver, channel), derived every time. What the files do fix is the *procedure* for deriving it. Why: the target is a strategic choice that depends on context; a table of numbers denies the framework. Ruled out: a media-by-budget table; per-channel word targets. Source: Q12.

**D5 — Vocabulary designed for priming, recorded in `VOCABULARY.md`.** Why: a fresh agent must be put in the right state of mind by the words alone; wanted connections (SADT, OLAP roll-up, graphics LOD, Toulmin) and avoided ones (anatomy, git, summarization-as-trimming) are managed explicitly. Ruled out: re-using the existing tool's terms (skeleton, lean, lens, frontier) for convenience. Source: Q5.

**D6 — Certainty rule: a rolled-up claim gets its own certainty, which may be higher or lower than its members'.** Kept in the core as one line with the election example. Why: aggregation changes the fact; certainty attaches to a claim at its height. The earlier draft rule "compression never raises certainty" is wrong in theory and in practice. Ruled out: that earlier rule. Risk accepted: the nuance may be too subtle for one line; the reviewer round tests it. Source: Q6.

**D7 — Relations between claims stay informal: one invariant, no link formalism.** "If a depends on b and a rolls up into A, A still depends on b's branch; bring related branches to at least claim when their partner is in focus." Why: an agent has no formal links; the existing graph tool was a means to understand the concept, not a thing to re-implement. Ruled out: typed links, lifting rules, identifiers. Source: Q7.

**D8 — Human visibility and control are proportional to criticality, assessed on two axes, with three modes.** Not a fixed default. Why: showing the view or handing over the choice is a strategic decision that depends on the criticality of the fact, absolute and in context. Ruled out: "silent by default"; "always one shape line per step". Source: Q8.

**D9 — The long-task outline is a satellite, not a core rule, and its relation to the harness is an open experiment.** Why: the harness already has mechanisms (summarization, to-do lists, plan mode, memory) whose behaviour is not known precisely; a heavy default instruction would be too much. Ruled out: a core rule such as "keep an explicit tree above five steps". Source: Q9.

**D10 — Enactment covers input, thinking, action, and communication, all in the core.** Why: the philosophy must be enacted in every aspect of an agent's work, including what to read, how to read it, which action to take and how. Ruled out: a communication-only core. Source: Q10.

**D11 — The purpose of a communication is named as a capability the receiver gains; typical purposes are illustrated, not enumerated.** Why: an enumerated taxonomy (decide, inform, hand off, record, review, teach) would be another fixed list denying context, and the question about it was unclear to the user. Confirmed by the user after the round-1 recap ("ok proceed"). Ruled out: a fixed intent taxonomy. Source: Q12, Q13.

**D12 — The roll-up algorithm is written for any receiver and any medium.** It spends detail "where the receiver cannot see for themselves" and keeps its edge cases (independent causes do not group, telegraphic style hurts reasoning, caps versus targets, jointly unsatisfiable rules, fabrication under budget pressure). Why: those edge cases recur whatever the medium. Source: Q14.

**D13 — Loading mechanism and overlap with existing rules are deferred to experiment.** No edit to the global instructions file now. Once the core exists, a fresh agent gets it loaded and a task, and we inspect what it used, and where it conflicted with the harness rules, the global instructions, or the user's personal communication instructions. Why: repercussions should be measured, not guessed. Ruled out: rewriting the global Interaction Protocol now; picking `@import` versus skill now. Source: Q1, Q3.

**D14 — Analysing past session logs for the failures that motivated this is a separate project.** Why: the user asked not to do it in this context. Source: Q15.

**D15 — Review by a separate reviewer model (Opus), not by the authoring model. Formal experimental evaluation is tabled.** Why: good practice; a proper experiment needs a judge that does not involve the user, which is not designed yet. Source: Q16.

## Naming and housekeeping
<!-- Lines 40-46 -->

**D16 — Folder `level_of_detail/`, core `LOD_CORE.md`, satellites in `drill_down/`, source in `build/`, reviews in `review/`.** Why: the folder name is self-explanatory to a human browsing the tooling repo; the satellite folder name uses the practice's own verb. Alternatives: `lod_management/`, `lod/`. Reversible by renaming.

**D17 — No dates in file names or bodies; rounds instead** (`ELICITATION_ROUND_1.md`, `ROUND_1_OPUS_REVIEW.md`). Why: the repository's documentation standard; git carries dates.

**D18 — One entry each in the tooling repo's `README.md` and `CLAUDE.md` pointing at this folder.** Why: every sub-part of that repo is indexed there; this is housekeeping, not the always-on wiring (D13).

## Content decisions inside the core
<!-- Lines 49-57 -->

**D19 — The core opens with a five-line statement of the idea before any rule.** Why: the vocabulary primes, but the mental model must be stated once in prose for the rules to be applied with judgment rather than mechanically.

**D20 — The "starting shape" (focus in full, ancestors at claim, root's children at claim, rest at label) is given as a default to adjust from, not a rule.** Why: a default reduces the cost of the decision without removing it.

**D21 — Every question to a human is framed as a view** (ask plus recommendation at claim first, grounds below). Why: questions are the most frequent and costliest view an agent sets; the user's own observation.

**D22 — The self-check is four questions, the first being "do heights vary".** Why: uniform height is the single most reliable symptom of trimming.

## Review round 1 — changes applied and declined
<!-- Lines 60-92 -->

Source: round-1 review (fresh Opus reader, report not retained; 4 blocking, 8 major, 9 minor). All blocking and major findings applied; minors applied where one clause sufficed.

**D23 — Precedence sentence added to the human-visibility section and to `HUMAN_CONTROL.md`.** "This governs how much of your reasoning you show, never what you are permitted to do; permission rules, standing instructions, and the requester's explicit instruction override every mode." Why: "Low: choose silently" read as self-granted authorization (B-3), the one dangerous failure found. Also closes m-9 (no file said the user outranks the practice). Ruled out: cutting the three modes to fund other lines; the user asked for this decision to be explicit (Q8).

**D24 — The children count is reconciled across files.** Core: "typically two to six; one child means you did not split, and a forced split is invention". `ROLL_UP.md`'s one-to-four is now stated as what you *show* a receiver in one place; `DRILL_DOWN.md`'s two-to-six as the outline's structure, each pointing at the other. Why: three ranges for one apparent operation (B-1); the two are distinct operations and nothing said so.

**D25 — "branch" kept; defused at first use with "(a part of the outline, never a version of it)".** Why: the git pull was confirmed strong and repeated (M-1), but the term is correct for a tree and the rename churn across eight files is real. Ruled out: renaming to subtree, limb, or section.

**D26 — Height and level distinguished in the vocabulary; the first self-check rewritten as a texture test.** "Does granularity vary, one line a bare fact, another rolling up a dozen? Same size and shape everywhere means you trimmed." Why: heights as counts never repeat exactly, so the old check passed everything (B-2). The trimming signature from `ROLL_UP.md` was promoted.

**D27 — The re-set rule rewritten: update silently as findings land; re-derive deliberately only when something moved; never narrate.** Why: five universal triggers invited per-step meta-commentary, which is the throat-clearing the practice bans (B-4).

**D28 — "Default view, then adjust" promoted to its own block, with the focus's children at claim stated explicitly.** Why: the only executable default was buried mid-paragraph and omitted the most common case (M-2).

**D29 — Focus defined singular, with the independence exception.** Why: plural definition, singular use everywhere else, and a rule in `TASK_OUTLINE.md` against two live branches (M-3).

**D30 — Given budgets handled in the core.** "When a budget is given to you, it is a constraint on the view, not a licence to trim: meet it by rolling up; if you must overrun to keep a fact, overrun and say which." Why: the core said budgets are never fixed while agents receive fixed budgets daily (M-4); consistent with D4, which forbids the *files* from fixing budgets, not the world.

**D31 — Software tilt removed from the core's input and action bullets; one non-software worked example added to `ROLL_UP.md`.** Shell words (head, grep, file, pass/fail) replaced with generic reads and results; the thin path illustrated with a deck draft and a dry run. Why: three of four action bullets used a software frame and every worked example was code (M-5).

**D32 — Prune and trim distinguished in the core.** Why: the slogan "do not trim" was followed two lines later by "prune", near-synonyms in ordinary English (M-6).

**D33 — "Uniform detail is never right" softened to "usually means you did not choose", with the flat-list exception.** Why: a list of equally important, equally certain items is legitimately uniform; the absolute invited spurious variation (M-7).

**D34 — Invariant 6 added: repeated local failure or a cascade is evidence the cut is wrong; roll up and re-partition.** Why: the practice's best recovery move lived only in satellites, which are not open when an agent is grinding on a leaf (M-8).

**D35 — Standing of the receiver added** to the receiver input and to the communication bullet ("roll up the content, never the courtesy"), and to `COMMUNICATION.md`. Why: both with-core sample outputs were better and shorter but brusquer; the receiver model had depth and next action, not relationship.

**D36 — Minor changes applied:** map simile first, SADT as a parenthetical (m-1); "full" scoped to grounds that bear on the purpose (m-2); "open" split into unknown / undecided / contested with next steps (m-3); the relation invariant rewritten in words without single-letter variables (m-4); "ask rather than assume when finding is slow" in `COMMUNICATION.md` (m-5); "I did not check" added to the inference register (m-7); the task-outline pointer marked "design, partly unvalidated" (m-8); "what happens if they do nothing" added to the question shape.

**Declined from the review, with reasons.** Cutting line 7 ("that choice is strategic, it is yours…"): it is the user's central insight, kept as priming. Cutting the three visibility modes: see D23. Making "stop at the level that answers" a standalone imperative (m-6): no line to spare. Reviewer caveats carried to `NEXT_SESSION.md`: behavioural test was n=2 and self-graded; satellite reachability depends on the undecided loading mechanism.

## Review round 2 — changes applied and declined
<!-- Lines 95-111 -->

Source: round-2 review (second fresh Opus reader, report not retained). Of the twelve round-1 findings it judged 9 resolved, 2 partly (B-2 check, M-5 examples), 1 not (M-1 "branch"). New: 0 blocking, 3 major, 6 minor. Its behavioural test caught a substantive error on the non-software task (a headline +8% cancelled by a 6% churn) and found the core over-produces when the deliverable is itself an outline.

**D37 — "branch" now names git explicitly.** "Not a git branch and not a variant: an outline has no versions, only parts." Why: the abstract denial did not fire; the reviewer measured interference on a task containing a literal git branch (N-1). Naming the active association and dismissing it is the move that worked for height/level.

**D38 — "standing" defined where it is used.** The receiver input now reads "where they stand relative to you (peer, senior, external, first contact): terseness reads as efficiency downward and as curtness upward or outward"; the duplicate clause was removed from the communication bullet. Why: the only undefined term in the core, colliding with "standing instructions" 40 lines later (N-2).

**D39 — The first self-check is now executable.** "Pick your two shortest lines and your longest: how many facts does each roll up? About the same for all three means you trimmed, unless the receiver's needs really are that flat." Why: the previous clause hung the verdict on visual size and shape, unfalsifiable and wrong for a deck outline (N-3). The fourth check, a duplicate of the communicating section's first test, was cut (N-6).

**D40 — Open branches are bounded.** Invariant 3 gains: "Open is for gaps the purpose demanded and you could not ground, not for gaps you imagined; say what you checked." Why: the reviewer observed itself generating a plausible open question from domain knowledge rather than from the material; nothing in the core bounded the sanctioned escape hatch.

**D41 — Counterweight for outline-shaped deliverables.** Core: "When the deliverable is itself an outline (an agenda, a deck skeleton, a plan), stay at claim: one line per node, the argument inside the node, never in the outline." `COMMUNICATION.md` Presentations gains the same rule and a five-title example. Why: on the deck task the core's pressures all added words and only one line pushed back; output grew from a five-line outline to a memo.

**D42 — Minor edits applied:** re-derivation paragraph condensed, "a step boundary" dropped as subsumed (N-5); one-child wording carries its own exception (N-9); the action pointer says "the thin end-to-end version first" rather than the never-introduced "thin path" (N-8); the software status example in `COMMUNICATION.md` swapped for the event one, since `ROLL_UP.md` already carries the migration example (N-4).

**Declined, with reasons.** Removing the SADT reference from the opening (N-7): the user asked for that association (Q5); the defect was the word "formally", which demoted the map simile, so the parenthetical now reads "or, if you know SADT". Cutting the Input and Thinking blocks to three bullets: the user named input as essential to the practice (Q10, D10); the reviewer itself rated the case for keeping them as "not zero". `ACTION.md` staying software-voiced: accepted by the reviewer as defensible; left as is.

## Overlap experiment 1 — what it changed
<!-- Lines 114-124 -->

Source: an overlap experiment (transcript not retained). A fresh Opus agent received the core inlined as standing instructions, above a read-only code question. It saw nine instruction sources, applied twenty-seven rules, found five overlaps and five conflicts, read two files in full (both forced by a project gate), nine at excerpt level, and ran fifteen searches; its counterfactual estimate without the core was about 1,800 lines read instead of about 200, and a reply ordered by architectural interest rather than by what the requester could act on.

**D43 — Project-mandated input protocols outrank the cheapest-read rule.** Added to the Input block: "A project instruction that mandates a read, a tool, or a protocol outranks this rule: it carries knowledge you do not have yet, such as which code is dead. Set the view inside it." Why: the agent skipped the repository's mandatory context-gathering protocol in favour of a direct search and nearly reported eight dead functions as live callers; the protocol it had skipped was partly rescued by the one it had obeyed. The precedence paragraph covered permissions and the human's instructions, not project input protocols.

**D44 — An output budget never bounds acquisition.** Added to the budget paragraph: "search to the level the purpose needs, then roll up to fit." Why: the agent reported that an 80-word cap on its return made it stop looking for a sixth caller; budget leaking upstream into acquisition is exactly what the input ordering exists to prevent, and nothing said so.

**D45 — Pointer line names the folder.** "beside this file in the tooling repo's `level_of_detail/` folder", so the satellites remain findable when the core is inlined from elsewhere. Why: an import inlines text; "next to this file" then has no referent.

**D46 — Loading mechanism: recommendation recorded, wiring left to the user.** Recommendation: one `@import` line in the user's global instructions pointing at `LOD_CORE.md`; satellites stay on disk, reached through the core's pointer section; no skill needed for the always-on part. Grounds: inlined as standing instructions the core coexisted with nine sources; project gate rules (blocking full reads) were obeyed over it; all five overlaps resolved toward the more operational wording, mostly the core's; none of the five conflicts was dangerous, and the two that were defects in the core are fixed (D43, D44). A skill would load only on trigger, which a transverse practice cannot rely on; a skill remains an option for deliberately invoking the satellites. Ruled out for now: editing the global instructions from this session without the user's go.

## Opening paragraph — rewritten on the user's judgment
<!-- Lines 127-138 -->

**D47 — The opening rewritten as a root claim plus one unfolding paragraph.** "Level of detail is a decision, never a default." then the four insights in the user's order: outline, depth per branch, remade inside every step, purpose × receiver × channel for what you say; closing on "Detail that is flat everywhere means you never chose." Why: the user judged the previous opening not great and the most impactful part of the project; its defects (four ideas at one height, undefined terms, no why, hedged ending, SADT clutter) were weighed against the alternatives (candidates not retained). SADT moved to invariant 1, where it qualifies the boundary rule; the uniform-detail hedge stays in invariant 5. Ruled out: a bulleted opening (reads as rules); a problem-first opening (the user leads with conclusions). Source: user feedback after the round-2 recap; both reviewers had rated the earlier prose opening highly, which shows a fresh reader's approval is not the test of an opening.

**D48 — Opening rewritten again, imperative and generic, in the user's structure.** "Think in levels of detail." then: decide at what level to ingest, plan and think, output; it governs every aspect of the workflow; what a level of detail is, with a one-line example in three precisions; why it matters; how to decide. Why: the user judged candidate A "not generic enough, not sharp enough" and dictated the structure. Metaphors (map, outline, branches) removed from the opening; they start in the vocabulary. Ruled out: keeping the prose-unfolding form. Source: user feedback (candidates not retained).

**D49 — Opening extended with a structure block and an aggregation block.** Structure: hierarchy, tree, leaves are facts, every node states what its children add up to at lower precision; SADT named without explanation as the process instance of a more general idea; facts connect across the tree and connections survive aggregation. Aggregation: moving up a level is lossy compression in the information-theoretic sense, not editing; grouping and the group's claim decide what survives and what distorts; it follows the method given below. Why: the user found D much better but missing the aggregation sentence, the connectedness of facts, the keywords hierarchy and tree, and SADT as an example that LOD exceeds. Source: user feedback; a base Haiku model knows SADT, so naming it costs nothing and primes the decomposition frame.

**D50 — Wired: one `@import` of `LOD_CORE.md` in the user's global instructions, on the user's go.** Reversible by deleting that line. Source: D46's recommendation plus the user's explicit go.

**D51 — Reviewer reports are not kept; `review/` removed.** A review round logs its findings here, each with the change made or the reason it was declined; the report itself stays outside the repository. Why: the user prefers less surface over process records before publishing. Supersedes the `review/` part of D1 and D16. Source: user ruling.

**D52 — Provenance limited to public and self-owned sources.** Mentions of earlier internal documents and their trial records were removed from this folder; the algorithm and its edge cases stand on their own. Source: user ruling.
