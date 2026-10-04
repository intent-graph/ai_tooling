---
name: subagent-orchestration
description: |
  MANDATORY before every sub-agent call (Agent tool, Workflow agent() prompts, SendMessage
  continuations), including one-line Explore calls, and before planning any fan-out. Keeps the
  orchestrator's context small: point to files instead of pasting or restating them, give each
  agent a fixed output path in a run directory, chain agents through files, and get every
  result back at three self-contained levels of detail (L1 headline, L2 claims, L3 full on
  disk) with the salient facts pinned verbatim at every level.
---

# subagent-orchestration: brief by pointer, get results back at three levels

Your context is the scarce resource; a sub-agent's is disposable. Every character you write
into a brief stays in your context for the rest of the session, and a fan-out multiplies it.
Every character a sub-agent returns inline does the same. So send pointers, not content;
receive a short result and a path, not the whole result; open the path only when the purpose
needs it.

This skill exists to stop three failures, measured over 500 past calls ([build/](build/README.md)):
1. **Pasting.** Guidelines, specs, file contents, earlier results copied or restated into briefs.
2. **Loose I/O.** No fixed place to write; results routed through the orchestrator's context.
3. **One-size returns.** A single block of text, too long to keep and too flat to act on.

## Contents

0. [Delegate at all?](#0-delegate-at-all)
1. [The run directory: fixed I/O](#1-the-run-directory-fixed-io)
2. [The brief: point, do not paste](#2-the-brief-point-do-not-paste)
3. [The return: three levels, pinned facts](#3-the-return-three-levels-pinned-facts)
4. [Brief skeleton and example](#4-brief-skeleton-and-example)
5. [Fan-out and chaining](#5-fan-out-and-chaining)
6. [CONTRACT mode](#6-contract-mode)
7. [After the return](#7-after-the-return)
8. [Before you send](#8-before-you-send)

---

## 0. Delegate at all?

- One search, one file read, or one command answers it: do it yourself.
- Delegate when the branch is wide (many files, many hits) and you need its claim, not its
  members; when isolation protects your context; when independent work can run in parallel.
- You are ready to delegate only when you can state the goal in one sentence and name the file
  the result will be written to.

## 1. The run directory: fixed I/O

Before the first call, choose one run directory for the orchestration, and one slot per call:

```text
<run_dir>/                    session scratchpad for working results; the project for durable ones
├── brief_shared.md           optional, written once by you: session-only context all agents need
├── 01_<slug>/
│   ├── result.md             written by the agent: L1, L2, L3 (section 3)
│   └── ...                   any other artifact it produces
└── 02_<slug>/
```

- **You choose every output path before the call.** You never search for what an agent wrote,
  and a later agent can be pointed at an earlier one's `result.md`.
- **Absolute paths everywhere.** A sub-agent's `cd` does not persist between its commands.
- **Write scope** is its slot, plus exactly the project paths it must change. State it.

## 2. The brief: point, do not paste

1. **Point to what is on disk:** the path, the part to read (section, symbol, line range), and
   why it matters. The agent reading ten files is the purpose of delegating, not a cost to
   save. Never paste a file, a guideline, a spec, or another agent's output. Never restate one
   in your own words either: a restatement is a paste that has drifted.
2. **Do not read in order to brief.** If you have not read a file, point to it. Reading it only
   to describe it costs your context twice.
3. **Inline only the session-only delta:** decisions made in this conversation, options ruled
   out and why, preferences the user stated, and an exact excerpt that must not be misread (an
   error message, an identifier) when it exists nowhere on disk. If the delta runs past about
   ten lines, or goes to more than one agent, write it once to `brief_shared.md` and point.
4. **Chain through files.** Agent B gets the path of agent A's `result.md` and the level to
   read, never A's content passed through your prompt.
5. **Point to the rules it must follow.** A typed agent may not load the project's
   instructions: name the instruction files to read first, and restate any standing
   prohibition its tools could break (for example, never `git push`).
6. **Explicit `model` and a typed `subagent_type`.** Mechanical (fetch, split, reformat, bulk
   grep) → haiku. Analysis, judgment, code → sonnet; a lookup that must interpret what it reads
   is judgment. Hard synthesis or high-stakes reasoning →
   opus, after the user confirms. `general-purpose` only when no typed agent fits: it loads
   about ten times more context. User and project instructions override these defaults.

**Size check.** A brief that points runs 10 to 30 lines. Past about 40, look for what you
pasted or restated.

## 3. The return: three levels, pinned facts

The agent writes its result at three levels of detail: the same content three times, each level
**self-contained**, readable with no other level in hand, every name introduced where it
appears, no "see below".

| Level | What it holds | Where |
|---|---|---|
| **L1 headline** | The one-sentence answer to the goal, with its certainty; then the pinned facts. | file, inline |
| **L2 claims** | One line per finding or branch: its claim, its certainty, its pointer (file:line, command). Then what was not checked. | file, inline by default |
| **L3 full** | Every branch in full: grounds, evidence, alternatives considered, raw lists, what was not checked and why. | file only |

- **Levels are set by height, not by word count.** L1 rolls up everything; L2 rolls up each
  branch; L3 rolls up nothing. Each level is a roll-up of the one below (facts grouped into
  fewer claims), never a trim, and each claim carries its own certainty: **grounded** (names
  what makes it true), **inferred** (follows from grounded facts, not observed), **open**
  (unknown, undecided, or contested; say which).
- **Pinned facts are never rolled up.** Every level opens with the same `Pinned:` block, copied
  from L1, never rewritten (agents reword pins otherwise: measured 0 of 4). Pin: the facts you name in the brief; any effect outside its slot (files changed, commands
  with side effects, anything irreversible); failures, blockers, contradictions with the brief;
  a decision it needs from someone, phrased as a question; a number or identifier the goal
  hinges on. More than about five pins means the cut was wrong or something broke: L1 says so.
- **You choose what comes back inline; the file always holds all three.** Default: L1, L2, and
  the path. Fan-out or chaining: L1 and the path. A small task where L3 would repeat L2: the
  agent writes "L3: none, L2 is complete".
- **An agent that cannot write files** (some read-only types): ask for L1 and L2 inline. Its
  own context holds L3 while it lives: continue it with `SendMessage` for one branch in full.

Template for `result.md`, reading rules, and a worked example: [return_levels.md](return_levels.md).

## 4. Brief skeleton and example

Drop a line that has nothing to say, never Output, Return, or the closing line.

```text
Goal:    <one sentence: what to produce, and what I will do with it>
Read:    <absolute paths, each with the part to read and why>
Context: <session-only delta, one line each, or "read <run_dir>/brief_shared.md">
Scope:   <read-only | may write only <slot> and <paths>>; never <standing prohibitions>
Output:  write <run_dir>/<NN_slug>/result.md with sections L1 headline, L2 claims, L3 full,
         each readable alone; mark each claim grounded / inferred / open.
Pin:     <facts that must appear word for word at every level, or "defaults only">
Return:  after writing, run `sed '/^## L3/,$d' <path>` (L1 only: `/^## L2/`) and reply
         with its output unchanged, then the path. L3 stays in the file.
If anything here is ambiguous, missing, or contradicts what you find, stop and return the
question with your recommendation instead of guessing.
```

**Add-ons**, each triggered by one thing:

| Trigger | Add |
|---|---|
| It may hit a decision it should not make alone | **Stop if:** <the decision>. Return the question, two or three options with one-clause trade-offs, a recommendation, and what happens if nobody answers. |
| It uses a tool it may not know | **Tool:** exact command, one example call and what it returns, side effects. |
| This is a retry | **Previous attempt:** what came back and why it was not usable. |
| Parallel siblings exist | **Siblings:** what the others cover, so it does not overlap. |

**Example**, read-only exploration, tier non-trivial → sonnet, typed `Explore`:

```text
Goal:    find every place the CLI reads its --config value, so I can choose one place to
         add validation.
Read:    /abs/repo/CLAUDE.md first (project rules); then /abs/repo/src/tool/, start at
         cli.py (argparse) and settings.py (env fallback).
Context: tests and plugins/ are out of scope; the user wants one validation point, not two.
Scope:   read-only.
Output:  write /abs/run/01_config_flag/result.md with sections L1 headline, L2 claims,
         L3 full, each readable alone; mark each claim grounded / inferred / open.
Pin:     any path where a bad config is silently ignored.
Return:  after writing, run `sed '/^## L3/,$d' /abs/run/01_config_flag/result.md` and reply
         with its output unchanged, then the path. L3 stays in the file.
If anything here is ambiguous, missing, or contradicts what you find, stop and return the
question with your recommendation instead of guessing.
```

## 5. Fan-out and chaining

- **Write the shared part once.** `brief_shared.md`, or a CONTRACT template; each call carries
  only its slot values: "Execute the task in /abs/run/brief_shared.md. Slot 03_auth, target
  /abs/repo/src/auth/. Write /abs/run/03_auth/result.md, then reply with the output of
  `sed '/^## L2/,$d' /abs/run/03_auth/result.md` and the path."
- **Ask for L1 inline.** Merge by reading the L2 sections from the files, or give the merge to
  one more agent that reads every `result.md` and writes its own result at three levels.
- **Chain.** Agent B's Read line is A's `result.md` and the level it needs.

## 6. CONTRACT mode

Use the typed payload in [contract_mode.md](contract_mode.md) (INPUT / INSTRUCTIONS / OUTPUT
CONTRACT with a `task_status`) when any one holds: the return is parsed by code; the prompt is
stored as a reusable workflow step; the agent can cause irreversible, shared, or external
effects (DB or remote writes, deletes, sends); you expect to resume it more than once. A fan-out
inside one session is not a reason: use section 5. The run directory, pointer rules, and three
levels still apply. In a
Workflow script, put them in the `agent()` schema: `l1`, `l2`, `result_path`, `pinned`,
`task_status`.

## 7. After the return

1. **Read at the level you need.** Act on L1 when it is enough. Use L2 to choose between
   branches. Open L3, one section of it, only for the branch in focus.
2. **Verify the artifact, not the report.** Open one file it wrote, run the gate, check one claim
   marked grounded. A result is a proposal until you have checked it.
3. **Check the shape** without reading the file: `python3 <this skill>/scripts/check_result.py
   <result.md> [--inline <file with the inline return>]` checks levels, certainty, pins word
   for word, cross-level references, and the inline copy. A malformed return goes back once,
   naming what failed.
4. **Pass results on by path, not by content.** To the user: quote L1, which is written to stand
   alone. To another agent: the path and the level.
5. **Continue or respawn.** The agent built context worth keeping → `SendMessage` with only the
   delta, and ask it to update `result.md` and return L1. The brief was wrong → respawn with a
   corrected brief. Two unusable returns from one brief mean the task was cut wrong: re-split it.
6. **Questions it returns** go to the user as the agent framed them when they are the user's to
   decide. Answer them yourself only when the answer is already settled in your context.

## 8. Before you send

- [ ] Nothing on disk is pasted or restated; the brief points, with the part to read.
- [ ] The session-only delta is inline, or written once to `brief_shared.md`.
- [ ] Every path is absolute; the output path is chosen by you, inside the run directory.
- [ ] Write scope and standing prohibitions are stated.
- [ ] Three levels requested, pins named, inline levels chosen.
- [ ] `model` and `subagent_type` set; the tier is stated in your message to the user.
- [ ] The closing line: stop and ask instead of guessing.
