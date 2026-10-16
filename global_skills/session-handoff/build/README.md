# build: why session-handoff is shaped this way

Maintainer-facing. The skill itself is [../SKILL.md](../SKILL.md); nothing here is loaded when the
skill runs. Change the skill only against a measurement: re-run the audit below before and after,
and replay at least one past session through the changed skill.

## Table of Contents

1. [Diagnosis](#diagnosis) _(Lines 22-36)_
2. [Baseline over past sessions](#baseline-over-past-sessions) _(Lines 39-68)_
3. [Experiment: default, v0, v1, v2, v3](#experiment-default-v0-v1-v2-v3) _(Lines 71-121)_
4. [Decisions](#decisions) _(Lines 124-205)_
5. [Review round 1](#review-round-1) _(Lines 208-229)_
6. [Install and enforce](#install-and-enforce) _(Lines 232-244)_
7. [Re-measure](#re-measure) _(Lines 247-257)_
8. [Open](#open) _(Lines 260-264)_

---

## Diagnosis
<!-- Lines 22-36 -->

No skill covered the hand-off to a new session; each session improvised. The user's verdict,
given in several projects over three months, in their words: "Your job is to pass the intent +
pointers, not the details"; "mes intentions + des pointeurs, pas des faits"; "privilégie le
passage de logique, d'intentions et de pointeurs plutôt que de contenu"; "if the file is in the
scratchpad, how can I share it with new session?" (sarcastic); "do not assume I read your
prompt". Five failures, named by the user:
1. **Content instead of pointers.** Files restated in the prompt, so the receiver reads a
   stale paraphrase and is not in control of what and how to read.
2. **No strict format.** Background, state, intent and instructions interleaved.
3. **Intent missing.** The one thing only the writer holds, the user's explicit and implicit
   intent from the conversation, is thin or absent.
4. **No level of detail.** One flat block; the receiver cannot stop early.
5. **Not treated as what it is:** a sub-agent brief whose receiver takes over.

## Baseline over past sessions
<!-- Lines 39-68 -->

Two measurements over every transcript on the authoring machine, before the skill existed.

`audit_handoffs.py --until <install date>` (mechanical): 37 hand-off requests in 28 sessions;
answered in chat only 81%, with a file in a scratchpad or temp directory 8%, with a file in the
project 11%; median reply plus file 5.5k characters; 0 of 7 files with levels and typed sections.

A sonnet agent then scored 38 hand-offs by hand (single-pass coding, not reviewed), and collected
43 distinct statements by the user about how hand-offs or briefs should be written:

| Measure | Value |
|---|---|
| Size | median 6.5k characters, 92 lines |
| Restate on-disk facts instead of pointing, at mid or high level | 24 of 34 |
| Dictate the reading ("in this order", "in full") | 22 of 38 |
| Typed sections for intent, state, instructions and context | 6 of 38; no two share a schema |
| Level-of-detail scheme, or pinned facts | 0 of 38 |
| Rejected directions with their why, in full | 4 of 38 |
| Implicit intent with its evidence | 1 of 38 |
| Standing rules copied in (never push, shell discipline) | 15 of 38 |
| Recorded user reaction negative or a correction | 9 of 15 |

What the user said, rolled up: "pass intent and pointers, not details" in 13 statements over
three months, twice right after a hand-off that restated details; short (7); strict structure
and self-contained levels (7); a hand-off is the same problem as briefing a sub-agent (5);
deliver a file in a reachable folder (5); gate before handing over: milestone, docs up to date
(3); do not assume the user read the prompt (4). And a distinction: the user's own rulings and
failed directions, not the assistant's: "ne donne pas les mauvaises solutions que tu as
proposé"; "pas ce que tu as décidé, ce que je t'ai transmis comme intention et info".

## Experiment: default, v0, v1, v2, v3
<!-- Lines 71-121 -->

Three past sessions, replayed up to the user's request for a hand-off: a UI-design session
where the user had rejected the real hand-off ("you are doing a bad job"), a prompt-refactoring
session ending in a milestone, and a document-preparation session in French. Each replay was
written by a fresh sonnet agent holding the conversation rendering, without the skill
(default) and with each version of it. A fresh sonnet judge per session first wrote the ground
truth of the user's intent from the whole session, including what happened after the
request, then scored the candidates blind on the same rubric; later versions were scored
against the same ground truth.

Per arm, summed over the three sessions. Recall counts the ground-truth intent items present
(60 in all); restated, dictated and planned count lines (fewer is better); size is what the
receiver reads before its first action.

| Arm | Intent recall | Restated | Dictated reading | Planned steps | Read before acting | Judge verdict |
|---|---|---|---|---|---|---|
| default | 51 | 16 | 13 | 18 | 1k to 7k, flat; two of three in chat only | 1 reject, 2 accept with fixes |
| v0 | 56 | 12 | 4 | 1 | L1+L2 6.5k to 10.3k | 3 accept with fixes; preferred 3 of 3, blind |
| v1 | not scored | | | | L1+L2 8.7k on two sessions: heavier | |
| v2 | 57, plus 3 partial | 8 | 7 | 1 | L1+L2 6.1k to 6.7k | 3 accept with fixes |
| v3 | 59, plus 1 partial | 10 | 7 | 2 | L1+L2 6.5k to 8.5k; default read with L3 Intent 7.9k to 12.0k | 3 accept with fixes |

- v0 to v1: pins once, a `Use:` line, "L2 at claim" in prose, no facts from files. L2 grew
  (mean line 156 to 200 characters) and two writers took the "L3: none" exit, one dropping a
  draft text that existed only in the conversation. Prose guidance alone did not move behaviour.
- v1 to v2: the checker fails an L2 line over forty words, L3 is never empty, the worked example
  shows an L3, and conversation-only material goes to a draft file during consolidation. L1+L2
  fell 27% from v0, recall held, and two writers saved chat-only drafts beside the work.
- v2 to v3 (review round 1 applied): recall rose to 59 of 60, intent errors fell (invented
  constraints and widened rejections gone), State says "not checked" instead of "assumed", every
  Open item carries a default. Cost: L1+L2 grew 6% to 27%, and the default read, now including
  L3's Intent, reached 12k characters. Two scorers found that L3 Intent mostly repeated L2's
  quotes, and that defaults on Open items let a receiver start building the user's undecided
  design choices. One v3 writer dropped a conversation-only draft that its v2 counterpart had
  saved: writer variance at n=1 is as large as the version effect.
- Self-contained case (a research brief for a session without file access, first replayed in
  v3): against the brief the real session had produced in chat, recall 10 of 13 against 8,
  planned elements 5 against 14, verdict accept with fixes against reject (the user had answered
  "write in a md not here"). Its defect: written as a takeover, it buried the task in L3, kept
  history and questions for the user, and pinned an instruction meant for an earlier session.
- After v3, not replayed: L3 never repeats L2; an Open default never takes the user's decision
  (work around it, or a reversible choice marked provisional); a successor never points to an
  older handoff, even for rules; the size check ignores path length (one session's Map was
  1.6k characters of absolute paths).
- The v2 "dictated" count includes the file's own `Use:` line and the bootstrap's "load the
  skill" line, two per file; without these protocol lines it is about one per file.
- Caveats: n=3, sonnet writers and sonnet judges; v2 was scored by different judge instances
  than v0 and default, against the same ground truth and rubric; the judge could see that one
  candidate followed a format, not which arm it was; replay writers could read project files
  that had changed since the session, which caused two invented constraints.

## Decisions
<!-- Lines 124-205 -->

Each with the alternative ruled out.

1. **A separate skill, sibling of `subagent-orchestration`.** Same pointer rule, same levels and
   certainty; different trigger (a hand-off, not an Agent call), different receiver (it takes
   over the task and the conversation with the user), different payload. Ruled out: a section
   of `subagent-orchestration`, whose description and lint hook are about Agent calls.
2. **The payload is the user's intent; everything on disk is a pointer.** Ruled out: a summary
   of the session, the default, which restates files and goes stale.
3. **Five typed sections, one line in one section: Intent, State, Map, Next, Open.** Ruled out:
   the CONTRACT payload (INPUT / INSTRUCTIONS / OUTPUT), since a receiving session returns no
   output contract; and a free "Context" section, which is where mixing happens.
4. **Intent tags with an order of authority:** explicit and ruled out bind, preference binds
   for the task, implicit is a hypothesis and always cites evidence. Explicit is what the user
   said, no wider. Ruled out: one "the user wants" list, which merged what was said with what
   was guessed (judges found invented preferences and widened rejections).
5. **Levels are self-contained prefixes; pins once, in L1.** The default read is L1, L2 and L3's
   Intent; each prefix stands alone, which is the user's "self-contained levels" applied to a
   reader who always starts at the top. Diverges from `subagent-orchestration`, whose levels are
   read instead of each other and repeat the pins. Ruled out: copying pins into every level
   (judges flagged the triple repeat as weight).
6. **A file in the project and a three-line bootstrap prompt.** Ruled out: the chat-only prompt
   (most of the baseline), which cannot be re-read, superseded or pointed at; and the
   scratchpad, which dies with the session.
7. **Check, then consolidate, before writing.** State says what was checked and when, never
   "assumed" ("you can not commit and pass over if you don't check"). Durable facts go to their
   project documents; material the receiver will use that exists only in the conversation
   (drafts, proposed edits, tables, measurements, fetched data with its source) goes to a draft
   file beside the work; both are pointed at.
   Ruled out: carrying them in the hand-off (a second source of truth), or leaving them out
   (a v1 writer dropped an approved draft text "on purpose").
8. **Next holds goal, constraints and exits; no step plan unless the user dictated it.** Ruled
   out: numbered next steps, the default's most frequent failure.
9. **Pointers say what a place is for, never how to read it.** Ruled out: "read in full, in
   this order".
10. **L2 lines are claims, enforced by the checker (FAIL over forty words, paths not counted);
    L3 is never empty.** v1 asked for "L2 at claim" in prose and L2 grew; two writers took the
    "L3: none" exit and piled detail into L2. Ruled out: prose guidance alone.
11. **The file carries a `Use:` line**, so it works in a session that lacks the skill. Ruled
    out: a bootstrap that depends on the skill being installed.
12. **Delivery: the path, the bootstrap, and the Intent lines for the user to correct.** The
    user owns the intent; this is their check. Ruled out: pasting the hand-off into chat.
13. **Receiver rules:** re-check State before acting, treat implicit intent as a hypothesis,
    never assume the user read the hand-off ("do not assume I read your prompt").
14. **Section headings stay in English as structural keys; content follows the project's
    language.** Ruled out: translated headings, which the checker and receivers cannot rely on.
15. **No lint hook yet.** A hand-off is a `Write` to a free path; a hook would need a path
    heuristic. Re-measure adoption first.
16. **Self-contained only on request, and then always honored.** User ruling: self-contained is
    asked for when the receiver cannot read files (an assistant in a browser chat, a model that
    reads only its prompt); "these are exceptions, they are well identified, the skill should
    honor them when asked". The file then carries `Receiver: self-contained (<receiver>)`,
    excerpts with their sources in L3, and the checker skips its pointer and pasting checks.
    Ruled out: the writer deciding on its own when to inline.
17. **A successor stands alone.** It carries forward every Intent item and pin of the handoff it
    started from that still holds, with the original quote and date, and does not mention the old
    file, whose Status points forward. Grounds: the user's rule for document versions, "la
    nouvelle version n'est pas un document incrémental sur l'ancienne version, c'est une version
    self contained", applied to a chain of handoffs. Ruled out: pointing to the predecessor as
    history, which drops the intent of every session but the last.
18. **The user's explicit request about a handoff outranks the skill.** In chat, a few lines, facts
    inline: honored, and the file is still written. Ruled out: rules that override the requester,
    against the level-of-detail practice ("the requester's explicit instruction outranks every
    line").
19. **Every Open item has a default ("If unanswered"); the receiver proceeds on what does not
    hinge on it and batches its questions.** Ruled out: a receiver that stops on any open
    decision (the cold receiver test held four user-owned items, none with a default).
20. **The header names where the work lives** (directory, branch, commit), not only where the
    writer ran; **pins are the user's dated words**, never a standing rule or a file fact; **the
    goal is the user's, or marked implicit or "not set"**. Ruled out: a goal that is the writer's
    unratified proposal.
21. **Placement: the repository's working-notes place, never a public repository.** A handoff
    carries absolute paths and private intent. Ruled out: "beside the work" alone, one
    `git add -A` from a leak in a public repository.
22. **One template, in `handoff_format.md`; SKILL.md keeps a skeleton.** The two copies had
    already drifted. A light form (about fifteen lines) serves "a few lines" requests.
23. **The self-contained form is task-first.** Its receiver does one task and returns, like a
    sub-agent: L1 is the task, Next opens L2, Intent keeps only what shapes the task, Open holds
    only what the receiver decides, L3 holds the sourced excerpts. Ruled out: the takeover shape,
    which buried the task and kept history the receiver could not use (replay of a research
    brief).

## Review round 1
<!-- Lines 208-229 -->

A fresh Opus agent, given the skill, the user's 51 statements and the replay outputs, ran a cold
receiver test first (a fresh session resuming from a v2 handoff), then reviewed. 20 findings: 1
blocker, 5 major, 14 minor; all applied on the user's go, with one adjustment (the blocker's
grounds are the user's rule for document versions, not a statement about handoffs).

- Blocker: a chain of handoffs dropped earlier sessions' intent → decision 17.
- Major: the user's words sat outside the default read → default prefix includes L3 Intent
  (decision 5); no self-check gate → decision 7; conversation-only material still lost →
  decision 7; the user's explicit request had no precedence → decision 18; Open items carried no
  default → decision 19.
- Minor: goal could be an unratified proposal, pins mixed with standing rules, header missing the
  work location (decision 20); names left undefined; English keys unstated; pointer parts
  forbidden unlike the sibling skill (now allowed, never depth or order); two template copies
  drifting, no light form (decision 22); placement in public repositories (decision 21); checker
  false negatives (prose lines, "Read, in full, first", bare Map paths), false positives ("in L2
  regularization", quoted user words), no diagnosis on files without levels, size numbers
  disagreeing with SKILL.md. Each checker fix has a case in `--self-test`.
- The cold receiver oriented from L1 and L2 alone; it could not act on proposed edits that
  existed "only in the conversation", a missing branch name, and undefined terms: each now has a
  rule and a check.

## Install and enforce
<!-- Lines 232-244 -->

From the repository root:

```bash
ln -s "$PWD/global_skills/session-handoff" ~/.claude/skills/session-handoff
```

Then one line in the global instructions (`~/.claude/CLAUDE.md`): "Before writing any prompt or
file meant to start or resume work in a new session, and when a session starts from one, load the
skill `session-handoff` and follow it." Both done on the authoring machine on the install date.

Check the checker itself after any change: `python3 scripts/check_handoff.py --self-test`.

## Re-measure
<!-- Lines 247-257 -->

```bash
python3 build/audit_handoffs.py --since <install date, YYYY-MM-DD>
```

Read first: adoption (share of hand-off requests answered after loading the skill), delivery
(file in the project versus chat or scratchpad), then the share of files with the full shape.
Against the baseline above, these show whether the skill is used, and whether using it changes
the hand-offs. Then replay one past session (`--show` lists candidates) through the current
skill and score it against a ground truth written before reading the candidate.

## Open
<!-- Lines 260-264 -->

- **A live receiver test.** No real session has yet resumed from a handoff written with the
  skill; the cold receiver test in review round 1 is a proxy.
- **Adoption.** Re-run the audit after a few weeks of use: share of hand-off requests answered
  after loading the skill, and share of files with the full shape.
