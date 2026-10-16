---
name: session-handoff
description: |
  MANDATORY before writing any prompt, brief, or file meant to start or resume work in a new
  session ("prompt for a new session", "hand off", "we are out of context", "next session",
  "nouvelle session", "passer la main"), and when a session starts from such a handoff. The
  handoff is a file in the project at three levels of detail (L1 headline, L2 claims, L3 full),
  with typed sections that never mix: Intent, State, Map, Next, Open. Its payload is what
  exists only in the conversation, the user's explicit and implicit intent; everything on disk
  is passed as a pointer, so the receiving session decides what to read and how deep.
---

# session-handoff: pass the intent and the map, not the content

A handoff is a sub-agent brief whose receiver takes over: the whole task, and the conversation
with the user. The `subagent-orchestration` skill's pointer rule and certainty marks hold; its
levels are adapted (section 4). What changes is the payload: a sub-agent brief carries a few
lines of session-only delta; a handoff's session-only delta is most of what it carries, because
the receiver has the whole disk and none of the conversation.

The one thing only you can pass is what the user wants: what they said, what they ruled out,
what their corrections reveal. Everything else the receiver can read for itself, at the level
its own next step needs. **Your job is to pass the intent and the map. Doing the next session's
job (planning its steps, summarizing files for it) is the failure.**

**Precedence.** The user's explicit request about this handoff (in chat, a few lines, with the
facts inline) and their standing instructions outrank every rule here. Honor the request; still
write the file; apply their corrections of the Intent to it.

## Contents

1. [Sub-agent brief vs handoff](#1-sub-agent-brief-vs-handoff)
2. [Before writing: check, then consolidate](#2-before-writing-check-then-consolidate)
3. [Distill the intent](#3-distill-the-intent)
4. [The handoff file](#4-the-handoff-file)
5. [Deliver](#5-deliver)
6. [Receiving a handoff](#6-receiving-a-handoff)
7. [Variants](#7-variants)
8. [Before you hand off](#8-before-you-hand-off)

---

## 1. Sub-agent brief vs handoff

| | Sub-agent brief | Session handoff |
|---|---|---|
| Receiver | does one bounded task, returns to you | owns the task from now on, talks to the user |
| Payload | goal plus a few lines of session-only delta | the session-only delta, mainly the user's intent |
| Levels are read | by you, instead of each other (often L1 alone) | by the receiver, as prefixes that each stand alone |
| Lives in | the prompt and a run directory | a file in the project, plus a short bootstrap prompt |

## 2. Before writing: check, then consolidate

The handoff can point only at what is on disk, and can claim only what was checked.
- **Check what can be checked**: run the tests, `git status` and `git log`, look at the output
  the user judges the work by ("you can not commit and pass over if you don't check"). State
  says what was checked and when; an unchecked claim says "not checked" and why, never "assumed".
- **Durable facts and decisions** (a design choice, a ruling, a finding that outlives the task)
  go to their project document now, following the project's own rules (documentation contract,
  decision log, README registration, language); the handoff points at them. A small edit: do it.
  More: ask the user first.
- **Material the receiver will use that exists only in the conversation** (a draft, proposed
  edits, a table, a measurement, data fetched from a source, with that source) goes to a draft
  file beside the work, marked as a draft. Leaving it out is not an option; L3 holds only what
  was said.
- **Work in progress**: State says what is uncommitted, untested, half-edited. Commit only if
  the user asked for a milestone; never push. Nothing the receiver needs stays in the scratchpad.

## 3. Distill the intent

Sources: the **user's** messages in this conversation, not your own, and the Intent and pins of
the handoff this session started from, if any. **Carry forward** every item from it that still
holds, with its original quote and date; drop only what the user superseded. A successor stands
alone: it never points to an older handoff, not even for rules. A durable project rule found
there (commit conventions, layout) moves to its project document first, and is pointed at there.

Explicit and ruled-out items are what the user said, no wider: "not just debugging" does not rule
debugging out, and a rejection you expect but did not hear is implicit. Tag each item:
- **explicit**: goals, rulings, constraints, a reading order or method the user dictated;
- **ruled out**: directions the user rejected, or saw fail, and why. This stops re-litigation;
- **preference**: how this user wants this task done, beyond their standing instructions;
- **implicit**: what the user wants but did not state, inferred from what they did. Signals: a
  correction ("no", "bad job", sarcasm) implies a rule and names the failed behaviour; a point
  made twice is a priority; what they spent time on or skipped; what they rejected or accepted
  shows the quality bar; their questions show what they care about. Always **inferred**, always
  with its evidence: a short quote and its date.

**Intent is the user's, not yours.** A proposal or decision of yours the user did not ratify is
not intent: it goes to Open, or nowhere. A direction the user rejected is passed as their ruling
in one line, not as your proposal at length ("not what you decided: what I gave you as intent
and information"). Leave out the user's global and project instructions: the receiver loads
them, and restating them is pasting.

## 4. The handoff file

**Where.** In the project, beside the work; in the repository's place for working notes when it
has one (gitignored if it is). Never commit a handoff to a public repository: it carries absolute
paths and private intent. Use the project's naming convention; otherwise
`handoff_<YYYY-MM-DD>_<slug>.md`, lowercase. Never only in chat, never in the scratchpad. A new
handoff for the same work supersedes the old one: set the old one's Status to
"superseded by <new path>"; the new one does not mention it.

**Shape.** The full template, the rules per section, a worked example, and the light and
self-contained forms: [handoff_format.md](handoff_format.md). The skeleton:

```markdown
# Handoff: <slug>
Status: / Written: / Use:              (header: state, date, where the work lives, how to read)
## L1 headline                          (one sentence, its certainty; Pinned: the user's rulings)
## L2 claims                            (### Intent, State, Map, Next, Open: one claim per line)
## L3 full                              (### Intent first: the user's words; then only what the
                                         conversation holds for the other sections)
```

**Levels are self-contained prefixes.** The receiver reads L1, L2 and L3's Intent by default,
then other L3 sections by need; a sub-agent's levels, by contrast, are read instead of each
other. Each prefix stands alone. Pins appear once, in L1, which every prefix includes; L2 never
repeats L1; L3 adds what L2 cannot hold, never repeats it. L3's Intent is the user's full words
where the wording matters and the order of their corrections, not L2's quotes again.

**Rules.**
- **L2 holds claims.** One line: its tag, about twenty words, a pointer, a certainty; a quote is
  a few words. Counts, identifiers, sub-lists and reasoning go to L3, under the same section.
- **Point, never paste or restate** a file, a guideline, a spec. A pointer may name the part that
  matters (section, symbol, line range) and says what it matters for; it never prescribes depth
  or order ("in full", "in this order", "first"). Unless the user dictated it: then quote it.
- **No facts from files.** A figure, date or finding that lives in a file is pointed to, never
  copied, even in State: "the loan terms → <path>", not the terms.
- **Pins are the user's words with their date**: every prohibition and every "ask me before X"
  the user set. Never a standing instruction, never a fact from a file.
- **Next: goal, constraints, exits; no plan.** The goal is the user's words with their date, or
  "implicit:" with its evidence, or "not set by the user", your proposal then going to Open.
  Steps appear only where the user dictated them. Files others share are named as constraints.
- **Open: every item has a default.** The question, who decides, what the answer changes, your
  recommendation, and "If unanswered:" what the receiver can do without the answer: work that
  does not depend on it, or a reversible choice labelled provisional. A decision the user owns is
  never taken by default; the default for it is to ask.
- **Introduce every name** a reader without the conversation would not know, in a few words.
- **Headings, Intent tags and certainty words stay in English**: the checker and receivers read
  them. Content follows the project's language. The user is "the user", never a pronoun.
- **Size.** L1 and L2 usually run 15 to 50 lines; the checker warns past 60 lines or 6,000
  characters, paths not counted. A small handoff takes the light form: one line per section,
  "none" where empty.

## 5. Deliver

1. Run `python3 <this skill>/scripts/check_handoff.py <handoff.md>`; fix every FAIL.
2. In chat, give the user three things, nothing else: the path, as a clickable link; the
   bootstrap prompt in a code block; the Intent lines of L2, under "Intent as I understood it,
   correct me before you paste". The user owns the intent; this is their check.

Bootstrap prompt, the only thing pasted into the new session:

```text
Resume <the goal in a few words>. Start in <project dir>.
Handoff: <absolute path to the handoff file>
Load the skill session-handoff (receiving side) if you have it; the file's Use line says how to read it.
```

## 6. Receiving a handoff

1. Read the default prefix, L1, L2 and L3's Intent:
   `awk '/^## L3/{l3=1} l3 && /^### (State|Map|Next|Open)/{exit} {print}' <path>`, and the
   project instructions as usual. Then decide what to open from the Map, and how deep.
2. **You own the task.** Re-check every State claim before acting on it: state decays. A
   contradiction with the handoff is a finding; tell the user.
3. Explicit intent and pins bind. Implicit intent is a working hypothesis: confirm it only when
   your next action hinges on it. Ruled-out directions stay out unless you have new evidence;
   then say so before trying.
4. **Never assume the user read the handoff.** Every question to them carries its own context.
5. Open items: proceed on what does not hinge on them, using each one's "If unanswered"; ask only
   what your next action hinges on, in one batched question.
6. Set the handoff's Status to "taken over <date>". Tell the user, in two lines, the goal as you
   understand it and your first action; then proceed.

## 7. Variants

- **Self-contained, on request.** When the user asks for a self-contained prompt, or names a
  receiver that cannot read files (an assistant in a browser chat, a model that reads only its
  prompt), honor it: a known exception, not a judgment call. Inline what the receiver needs, each
  excerpt marked with its source; header line `Receiver: self-contained (<receiver>)`. Such a
  receiver does one task and returns: Next comes first, Intent keeps only what shapes the task
  (handoff_format.md). Never self-contained unasked: a receiver with disk access gets pointers.
- **A handoff to a sub-agent** is a brief: use `subagent-orchestration`.
- **Several parallel successors**: one handoff per independent branch, each with its own Next;
  the shared Intent written once, in a file they all point to.
- **Project rules on content** (confidential data, opacity rules, a journal no one may write)
  outrank this skill: point to aggregates, never to the forbidden content.

## 8. Before you hand off

- [ ] What could be checked was checked; State says what and when, never "assumed".
- [ ] Durable facts are in their project documents; conversation-only material is in a draft
      file; both are pointed to.
- [ ] Intent carries forward the predecessor's still-valid items; each item is the user's, tagged,
      with its evidence; none is your unratified proposal.
- [ ] No line restates a file or prescribes how to read; Next plans no step the user did not
      dictate; every Open item has its "If unanswered".
- [ ] Pins are the user's words, once, in L1; L2 lines are claims; L3 starts with the user's words.
- [ ] Every unfamiliar name is introduced; the file is in the project, never in a public repository.
- [ ] `check_handoff.py` passes; the user got the path, the bootstrap, and the Intent lines.
