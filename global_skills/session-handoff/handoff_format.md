# The handoff file

Read this when writing a handoff, or when checking one. [SKILL.md](SKILL.md) section 4 has the
rules in short; this file holds the one template.

## Contents
<!-- Lines 8-18 -->

1. [Template](#template)
2. [The five sections](#the-five-sections)
3. [The three levels](#the-three-levels)
4. [Worked example](#worked-example)
5. [Light form](#light-form)
6. [Self-contained form](#self-contained-form)
7. [Failures this format prevents](#failures-this-format-prevents)

---

## Template
<!-- Lines 21-67 -->

```markdown
# Handoff: <slug>
Status: open | taken over <YYYY-MM-DD> | superseded by <path>
Written: <YYYY-MM-DD>, session in <cwd>. Work: <dir>, branch <name> at <short sha> | not under git
Use: read L1, L2 and the Intent section of L3 (stop at L3's next section); open the rest only as your next step needs; re-check State before acting on it; the user has not read this file.

## L1 headline
<One sentence: what the user wants, where the work stands, what the receiver owns.> <certainty>
Pinned:
- <a prohibition or "ask me before X" the user set, in their words> (<date>)

## L2 claims
### Intent
- explicit: <claim>. "<short quote>" (<date>). grounded
- ruled out: <direction>, because <reason>. "<short quote>" (<date>). grounded
- preference: <how to work on this task>. "<short quote>" (<date>). grounded
- implicit: <claim>. Evidence: "<short quote>" (<date>). inferred

### State
- done: <claim> → <pointer: path, commit, command>. grounded, checked <when, how>
- in progress: <claim> → <pointer>. <certainty>
- not checked: <claim>, because <why> → <pointer>. open

### Map
- <absolute path or URL>[, <section | symbol | lines>]: <what it is>; matters for <item>

### Next
- Goal: <the user's words> (<date>) | implicit: <goal>, evidence <quote> | not set by the user
- Constraints: <scope, approvals needed, files others share>
- Stop and ask the user if: <decisions reserved to them>

### Open
- <question>. Decides: <user | receiver>. Changes: <what>. Recommendation: <what>. If unanswered: <work that does not depend on it, or a reversible choice marked provisional; never the user's decision>.

Not passed: <what is left out on purpose, and where it lives>

## L3 full
### Intent
<every Intent item in full: the user's words verbatim with dates, the corrections in order, the
reasoning the user agreed to; carried-forward items keep their original date>

### State | Map | Next | Open
<only what the conversation holds: why an attempt failed, in the user's words; the grounds and
trade-offs of each Open question. Material the receiver will use lives in a draft file instead.>
```

## The five sections
<!-- Lines 70-85 -->

A line belongs to exactly one section. When a line seems to need two, split it.

| Section | Holds | Never holds | Test |
|---|---|---|---|
| **Intent** | the user's goals, rulings, rejections, preferences, and what their behaviour implies | facts about files; your own plan; your unratified proposals | Would this line change if the user changed their mind? |
| **State** | what is true now, each with its pointer and when it was checked | the content behind the pointer; wishes; "assumed" | Can the receiver verify it by opening the pointer? |
| **Map** | where to look, the part that matters, and what it matters for | depth or order of reading; files the receiver opens anyway (project instructions, root README) | Would the receiver miss this place without the line? |
| **Next** | the goal, constraints, exits: the instruction | steps the user did not dictate; standing rules; background | Is it an instruction the receiver can obey or break? |
| **Open** | what nobody knows or has decided yet, each with a default that never takes the user's decision | settled questions; rhetorical worries | Does an answer change what the receiver does? |

Intent tags, in order of authority: **explicit** (the user said it) and **ruled out** bind the
receiver; **preference** binds for this task; **implicit** is the writer's inference, a hypothesis
the receiver confirms when an action hinges on it. Tags, headings and certainty words stay in
English; the content follows the project's language.

## The three levels
<!-- Lines 88-106 -->

The same outline at three heights, as in a sub-agent's three-level return, with one difference:
a sub-agent's levels are read instead of each other, a handoff's are read as prefixes. The
default prefix is L1, L2 and L3's Intent; other L3 sections are read by need. Each prefix stands
alone; pins appear once, in L1, which every prefix includes.
- **L1** rolls up everything: one sentence, a claim, not a topic. "The user wants the export
  to run nightly without touching the invoice tables; the job is written but untested", not
  "Worked on the export".
- **L2** rolls up each item to one line, with its certainty and pointer. Heights differ: a
  single ruling beside a line that rolls up a week of attempts.
- **L3** opens with the user's own words where the wording matters: implicit intent hinges on
  it, and a paraphrase loses it. It adds what L2's short quotes cannot hold, the full sentence and
  the order of corrections, and never repeats an L2 quote. The other L3 sections hold only what
  was said, never material to work from.

No level points at another ("see L3", "as above"): the structure tells the receiver where to
drill. Every name a reader without the conversation would not know is introduced where it first
appears. The user is "the user", never a pronoun.

## Worked example
<!-- Lines 109-170 -->

A handoff for a data-export task. Note what moved down: L2 says the SQL rewrite failed on
rounding; L3 says how, in the user's words.

```markdown
# Handoff: billing_export_nightly
Status: open
Written: 2026-03-14, session in /abs/repo/billing. Work: /abs/repo/billing, branch export-nightly at 4f2a9c1
Use: read L1, L2 and the Intent section of L3 (stop at L3's next section); open the rest only as your next step needs; re-check State before acting on it; the user has not read this file.

## L1 headline
The user wants the billing export moved from a manual script to a nightly job that never
writes to the invoice tables; the job is written and passes unit tests, but has not run
against staging. grounded
Pinned:
- "don't touch invoices. not even a status column" (03-14)

## L2 claims
### Intent
- explicit: nightly, unattended, alerting on failure only. "I don't want to babysit it" (03-13). grounded
- ruled out: a status column on invoices to track exports; finance owns that schema (03-14). grounded
- ruled out: rewriting the export in SQL; the currency rounding differed. "drop it" (03-13). grounded
- preference: one small PR per step, each reviewed before the next. "small diffs" (03-14). grounded
- implicit: correctness over speed; two faster drafts were rejected for rounding, none for
  slowness. Evidence: "slow is fine, wrong is not" (03-13). inferred

### State
- done: job and unit tests → /abs/repo/billing/jobs/nightly_export.py. grounded, tests run 03-14
- not done: staging run; credentials pending from ops → ticket OPS-1182. grounded, checked 03-14
- uncommitted: none. grounded, `git status` 03-14

### Map
- /abs/repo/billing/docs/export_rounding.md: why the SQL rewrite failed; matters for the ruled-out SQL path.
- /abs/repo/infra/cron/README.md, "Registering a job": how nightly jobs are added here; matters for Next.

### Next
- Goal: "it runs every night, and I only hear from it when it fails" (03-13).
- Constraints: read-only on invoice tables; one PR per step.
- Stop and ask the user if: the job needs any write outside the export bucket.

### Open
- Alert channel: on-call pager or team chat? Decides: user. Changes: the alert step only.
  Recommendation: team chat. If unanswered: build the job with the alert target as a setting,
  ask before the first deploy.

Not passed: the review comments on the first PR; they are on the PR itself.

## L3 full
### Intent
- 03-13, on the first draft: "I don't want to babysit it. If it fails, tell me; if it
  works, I never want to hear about it."
- 03-13, after the SQL rewrite: "the totals are off by cents on EUR invoices. slow is fine,
  wrong is not. drop it." Two faster drafts were rejected the same day, both on rounding.
- 03-14, on the PR plan: "small diffs. one step, I review, next step."
- 03-14, on tracking exports: "don't touch invoices. not even a status column, finance owns
  that schema."

### Open
- Alert channel: the user mentioned both the pager and the team channel in passing (03-13)
  and did not choose. An overnight failure delays a report by a day, nothing more.
```

## Light form
<!-- Lines 173-177 -->

For a small handoff, or when the user asks for a few lines: the same header and levels, one line
per section, "none" where a section is empty, and an L3 Intent of one to three quotes. About
fifteen lines. The checker treats it like any other handoff.

## Self-contained form
<!-- Lines 180-196 -->

Only when the user asks for one, or names a receiver that cannot read files: an assistant in a
browser chat, a model that reads only its prompt. Such a receiver usually does one task and
returns its result to the user: it does not take over the conversation. Write for that.
- **Header** gains `Receiver: self-contained (<receiver>)`; `Use:` says the whole file is the
  prompt.
- **L1** is the task in one sentence. **Pins** are constraints on that task, in the user's
  words; an instruction the user gave an earlier session is not one.
- **L2 opens with Next**: the task, the shape of the deliverable, the constraints. Then
  **Intent**, keeping only what shapes the task (audience, criteria, rejected directions);
  **State**, what is already known; **Map**, each source named so the user can check it;
  **Open**, only what the receiver decides itself. Questions for the user stay out.
- **L3** holds the excerpts the task needs, each under `### Map` with its source and date, and the
  user's words that shape the task. History the receiver cannot use stays out.
Everything else holds: three levels, five typed sections, no step plan beyond the deliverable's
shape.

## Failures this format prevents
<!-- Lines 199-213 -->

Each was observed in past handoffs or in the replays; the build notes give the counts.
- **The content dump.** Files summarized into the prompt, so the receiver reads a stale
  paraphrase. Prevented by: State and Map hold pointers only.
- **The dictated reading.** "Read in full, in this order". Prevented by: a pointer names what a
  place is for, never how deep or in what order to read it.
- **The pre-made plan.** Numbered steps the receiver should have derived. Prevented by: Next
  holds goal, constraints, exits.
- **The lost intent.** Rulings and rejections missing, so the receiver re-proposes what the user
  refused; or lost along a chain of handoffs. Prevented by: Intent first, tagged, carried forward.
- **The mixed prompt.** Background, instructions and state interleaved. Prevented by: one line,
  one section.
- **The unchecked state.** "Done (assumed)". Prevented by: State says what was checked and when.
- **The stalled receiver.** Open questions with no default. Prevented by: "If unanswered".
- **The unreachable handoff.** Chat only, or the scratchpad. Prevented by: a file in the project.
