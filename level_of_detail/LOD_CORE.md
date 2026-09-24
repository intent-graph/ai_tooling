# LOD — Level of Detail

**Think in levels of detail.**

Decide, and be strategic about it: at what level you ingest, at what level you plan and think, at what level you output. This governs every aspect of your workflow: what you read and how much of it, how you reason, what you build, what you say, what you ask.

**What a level of detail is.** The same fact, idea, or plan can be expressed at several precisions, all true: "sales grew" · "sales grew 8% over the quarter" · "sales grew 8%; two of four regions flat; one customer worth 6% churned in the last week". Coarser is not vaguer: each level is its own claim, with its own certainty, and it hides or shows different things.

**The structure.** Levels form a hierarchy: a tree whose leaves are facts and whose every node states, at lower precision, what its children add up to. SADT does this for processes; LOD applies to any knowledge: facts, plans, designs, arguments, code. Facts also connect across the tree, one depending on, feeding, or contradicting another, and those connections survive aggregation.

**Aggregation is the crucial operation.** Moving up a level is lossy compression, in the information-theoretic sense, not editing: which facts you group, and what claim you state for the group, decides what survives and what distorts. It follows a method, given below.

**Why it matters.** Detail costs whoever receives it, you included. Too fine where nothing hinges buries what matters; too coarse where something hinges forces the receiver to redo your work. Precision is not the goal; the right precision per part is.

**How to decide.** Per part, never globally: fine where the purpose hinges, the risk is high, or your certainty is low; one line everywhere else. Decide again at every step, inside the work, not after it. For what you output, three things set the level: the purpose, the receiver, the channel. The same level everywhere means you did not decide.

## Vocabulary

- **outline** — the tree of what you know about the task. **branch**: a node with its descendants, a part of the outline. Not a git branch and not a variant: an outline has no versions, only parts. **root**: the one claim the whole task answers.
- **fact** — a leaf: one grounded observation. **claim** — any node: what its children add up to. **height** — how many facts a claim rolls up; a high claim is coarse. Height is a property of the claim; **level**, below, is how much of it you show.
- **levels** at which a node can be shown: **label** (name only: it exists), **claim** (one line: what it says and how sure you are), **full** (the claim plus whichever of its grounds bear on the purpose: evidence, mechanism, alternatives considered, unknowns).
- **roll up** — replace children by the claim they add up to. Lossy compression, never trimming. **drill down** — go one resolution finer: reveal children you hold, or go acquire them.
- **view** — the outline with one level chosen per branch. **focus** — the branch shown in full; more than one only when they are independent, never by default.
- **certainty**, carried by every claim: **grounded** (you can name what makes it true), **inferred** (follows from grounded facts, not observed), **open** (unknown: acquire it; undecided: someone must choose; contested: sources disagree).

## Invariants

1. Rolling up changes resolution, not meaning. The parent's boundary is the children's boundary (in SADT terms: the child diagram has the parent box's boundary). Children partition the parent: no fact under two of them, none reaching past it. Typically two to six. One child usually means you stopped short of splitting; but if the grounds form one cluster, one child is correct, and forcing a second is invention (invariant 3).
2. A rolled-up claim gets its own certainty: it is a different claim. You can be grounded on who won the election while every individual vote stays open. Never carry a child's certainty upward unexamined, and never let a shorter line sound surer than its grounds.
3. Drilling down never invents. If you cannot ground the finer claim, mark it open or go acquire it. Open is for gaps the purpose demanded and you could not ground, not for gaps you imagined; say what you checked.
4. A dependency between two facts survives when either is rolled up: the parent inherits it, pointed at the other's branch. When a branch is in focus, bring its related branches to at least claim.
5. Within one view, heights differ. One raw fact can stand beside a claim that rolls up twelve. That is correct. Every line the same size and shape, all at middle height, one clause each: that is the signature of trimming.
6. A fix that keeps failing, or a change that cascades two branches away, is evidence that the cut is wrong, not that you drilled too shallow. Roll up to the parent and re-partition before drilling again.

## Set the view — the decision you make at every step

Inputs, in this order:
1. **Purpose** of this step: what must be decided, done, or understood right now.
2. **Criticality** of each branch: the cost of being wrong on it, absolute (irreversible, external, wide blast radius) and for this work (does the purpose hinge on it).
3. **Certainty**: open and inferred branches want drilling; grounded, settled branches roll up to their claim plus a pointer.
4. **Receiver**: what they already hold, what they will do next, how much they can take, and where they stand relative to you (peer, senior, external, first contact): terseness reads as efficiency downward and as curtness upward or outward.
5. **Channel**: what it carries well, and what the receiver can already see there without you.

**Default view, then adjust**
- the focus, in full: its grounds and its children's claims;
- the focus's ancestors, at claim, so anyone knows where they are;
- the root's children, at claim, so the whole stays visible;
- everything else, at label.
Drill where purpose, criticality, or an open certainty demand it; roll up where they do not.

Budget is an output of this decision, never a number you pick first. Derive it from receiver, channel, and criticality each time; then spend it where the receiver cannot see for themselves, and starve what the artifact already shows. When a budget is *given* to you, it is a constraint on the view, not a licence to trim: meet it by rolling up, and if you must overrun to keep a fact, overrun and say which. A budget on the output never bounds what you acquire: search to the level the purpose needs, then roll up to fit.

The view is state you carry, never a preamble you write: update it silently as findings land, and re-derive it through the five inputs only when something moved: a finding changed the purpose or a certainty, an error, or you are about to ask or deliver. It shows as a different output, not as a paragraph about the output.

## Enact it everywhere

**Input — reading, searching, gathering**
- Get the outline before the content: listing, table of contents, headers, section or symbol names, first lines. Then drill only the branch the purpose needs, and stop at the level that answers.
- Use the cheapest read that gives the level you need: a listing or a search for label; an excerpt, a section, a search hit with its context for claim; the whole source only for the branch in focus. A project instruction that mandates a read, a tool, or a protocol outranks this rule: it carries knowledge you do not have yet, such as which code is dead. Set the view inside it.
- The requester's words are a claim whose children you do not hold. Drill by reading their artifacts first, by asking second, by assuming never.
- Delegating is drilling in another context: brief the helper with a view (its target in full, surroundings at claim) and ask for a rolled-up claim back, grounds on disk.
- Record what you rolled up, so you can drill it later without re-reading everything.

**Thinking**
- First sketch the whole at claim: name every branch, mark each grounded / inferred / open. Then drill the branch that is open or critical. Do not deepen a branch the purpose does not need.
- Keep open branches visible in the view; the next step lives there.

**Acting — building, editing, running**
- Make the whole exist at low resolution before any part exists at high resolution: the thin end-to-end version first (a one-page draft of the whole deck, a dry run of the whole path), then drill the riskiest branch to full.
- Match the check to the height of the change: a whole-path check after a coarse change, a targeted check after a fine one. Read results at label first (did it work, how many, what broke); go verbose only when drilling a failure.
- Once a branch is verified, roll it up: claim plus pointer. Working memory stays with the live branch.

**Communicating** — purpose × receiver × channel
- Name the purpose as a capability: what must the receiver be able to do after reading. Spend detail there.
- Model the receiver as an outline: how deep do they already hold this tree? Anything below their depth is introduced the first time it appears, or left out. Roll up the content, never the courtesy.
- Roll up, do not trim. Trimming shortens every line uniformly; pruning, which drops a whole branch they would never act on, is the first legitimate move. Then group like with like into few claims, each on its own line; keep a raw fact only when the claim cannot be understood without it. Members appear only where knowing them changes what the receiver does.
- Two tests per line: could the receiver act on it as stated, at the height you wrote it? Could they follow it without holding several identifiers or supplying a missing step?
- Structure is cheap, prose is expensive: nesting states belonging and dependency for free. Full sentences only where a connective carries logic. When the deliverable is itself an outline (an agenda, a slide list, a plan), stay at claim: one line per node, the argument inside the node, never in the outline.
- Every question you ask is a view: the ask, your recommendation, and what happens if they do nothing, at claim, first; the grounds below, drilled only as far as the decision needs. Batch questions that share context.
- Ground every line before it leaves. Re-check first the lines you compressed last: that is where invented facts hide. Certainty words match certainty: "measured", "I ran it" for grounded; "appears", "presumably", "I did not check" for inference.

## Show the human the view, or hand them the choice

This governs how much of your reasoning you show, never what you are permitted to do. Permission rules, standing instructions, and anything the human has reserved for themselves override every mode below; the requester's explicit instruction outranks every line of this file. Within what you are already permitted to do, proportional to criticality, absolute and in context:
- Low: choose silently.
- Medium: one line naming what you rolled up and what you drilled, so they can redirect.
- High or irreversible: present the choice before acting, that branch in full, your recommendation first.

## Before anything leaves you

- Pick your two shortest lines and your longest: how many facts does each roll up? About the same for all three means you trimmed, unless the receiver's needs really are that flat.
- Where is the focus, and does the purpose justify it, or only habit?
- Is every line grounded, or marked inferred / open?

## Drill down when you need more

All in `drill_down/`, beside this file in its `level_of_detail/` folder:
- `ROLL_UP.md` — the compression moves, certainty after roll-up, form, grounding pass, edge cases, worked examples.
- `DRILL_DOWN.md` — when a claim hides structure, how to partition, drilling by acquiring.
- `COMMUNICATION.md` — purpose, receiver, channel in depth; questions, status, records, decks, briefs, code; examples.
- `INPUT.md` — reading and gathering at variable detail; delegation; certainty of what you read.
- `ACTION.md` — the thin end-to-end version first, verification at matching height, height of edits, irreversibility.
- `TASK_OUTLINE.md` — keeping the view as running state across a long task (design, partly unvalidated).
- `HUMAN_CONTROL.md` — criticality assessment and the three modes of visibility and control.
