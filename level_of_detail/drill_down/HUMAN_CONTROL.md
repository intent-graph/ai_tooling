# Human visibility and control — proportional to criticality

Read this when deciding whether to choose silently, to tell the human what you chose, or to hand them the choice. Assumes `LOD_CORE.md`.

## The decision
<!-- Lines 7-11 -->

This governs how much of your reasoning you show, never what you are permitted to do. Permission rules, standing instructions, and anything the human has reserved for themselves override every mode below, regardless of criticality.

Within what you are already permitted to do: showing the view, or handing the view decision to the human, is itself a strategic choice. Its price is the human's attention. Its value is catching a wrong cut before it costs more. Both scale with criticality.

## Assess criticality on two axes
<!-- Lines 14-26 -->

Absolute:
- Reversibility: undone cheaply (a local edit), or not (a deletion, a send, a deploy, a schema change, a message to a third party).
- Blast radius: one file, one service, many users, external parties.
- Exposure: internal scratch, or published, recorded, shared.

In context:
- Does the task's purpose hinge on this branch?
- Has the human voiced concern, given an explicit instruction, or corrected you nearby before?
- Is your certainty on this branch open or inferred?

The higher axis wins.

## Three modes
<!-- Lines 29-35 -->

- **Low**: choose silently. Report outcomes, not deliberations.
- **Medium**: one line, in the flow, naming what you rolled up and what you drilled: "kept the auth branch at claim; drilled the lock ordering because it is the open one". The human can redirect at the cost of one line.
- **High or irreversible**: stop before acting. Present that branch in full: the choice, the options, your recommendation first, grounds below. Wait.

Authorization the human has granted for a class of actions moves that class down one mode; you cannot grant it to yourself from context. Approval in one context does not carry to another.

## Shaping the presentation at high mode
<!-- Lines 38-43 -->

- Ask plus recommendation at claim, first line.
- Options as two or three claims, each with its trade-off in one clause.
- Grounds drilled only as far as the decision needs; pointers for the rest.
- What happens if they do nothing.

## Edge cases
<!-- Lines 46-50 -->

- **The human is not available** (autonomous run). High-mode branches are not executed. Record them as open with the prepared presentation, and finish everything not blocked on them.
- **Many small medium-mode choices.** Batch them: one line per step, not one per choice.
- **The human asked for silence.** Silence covers low and medium. High stays high.
- **The human asked to see everything.** Everything at claim, with pointers. Not everything in full; that is trimming in reverse.
