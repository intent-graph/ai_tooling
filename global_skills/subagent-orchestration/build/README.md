# build: why subagent-orchestration is shaped this way

Maintainer-facing. The skill itself is [../SKILL.md](../SKILL.md); nothing here is loaded when the
skill runs. Change the skill only against a measurement: re-run the audit below before and after.

## Table of Contents

1. [Diagnosis](#diagnosis) _(Lines 20-32)_
2. [Baseline over past sessions](#baseline-over-past-sessions) _(Lines 35-49)_
3. [Experiment: no skill, old skill, new skill](#experiment-no-skill-old-skill-new-skill) _(Lines 52-71)_
4. [Live tests after install](#live-tests-after-install) _(Lines 74-97)_
5. [Decisions](#decisions) _(Lines 100-132)_
6. [Install and enforce](#install-and-enforce) _(Lines 135-151)_
7. [Re-measure](#re-measure) _(Lines 154-161)_

---

## Diagnosis
<!-- Lines 20-32 -->

The predecessor skill, `subagent-call`, was **never used**: it was not linked into
`~/.claude/skills/`, so no session listed it, and no global instruction named it as mandatory.
Zero of 504 recorded sub-agent calls were preceded by loading it.

It was also **incomplete** for the three failures it was meant to stop:
- **Pasting.** "Pointers, not pasted content" was one rule of seven, and its exception ("inline
  only what you already hold") licensed exactly the common case: the orchestrator has read a
  file, so it pastes or restates it. Restating in its own words was not named at all.
- **I/O.** A return shape and size bound, but no fixed output location, and no rule for passing
  one agent's result to the next without routing it through the orchestrator's context.
- **Levels.** One rolled-up return; no multi-level result, no pinned facts.

## Baseline over past sessions
<!-- Lines 35-49 -->

`audit_subagent_calls.py` over every transcript on the authoring machine: 504 calls, 97 sessions.

| Measure | Value |
|---|---|
| Prompt size | median 3.5k chars, p90 10k; 32% of prompts over 6k chars |
| Prompt volume vs return volume | 2.33M chars written into briefs vs about 1.0M returned |
| Prompt text repeated from an earlier prompt of the same session | 30% |
| Prompt text copied verbatim from what the session had read | 5% (the rest of the bloat is restatement) |
| Explicit `model` / `general-purpose` type | 80% / 66% |
| Three-level return requested / fixed `result.md` path | 0% / 0% |

Typical worst case: an 11k-character guideline pasted "in full below" into each prompt of a
fan-out, once per agent.

## Experiment: no skill, old skill, new skill
<!-- Lines 52-71 -->

Six fresh sonnet sub-agents played the orchestrator on one scenario (a documentation audit of
three folders, in parallel, then one agent to apply approved fixes), two per arm. Each had read
the documentation standard and held a chat-only user requirement, then wrote the calls it would
send. Content cost counts brief text plus any shared brief written to disk, with absolute paths
collapsed to one token.

| Arm | Content cost (chars) | Restates the standard (keyword hits) | Three levels | Output path set |
|---|---|---|---|---|
| no skill | 6.5k, 11.8k | 8, 32 | 0 of 8 calls | 5 of 8 |
| old skill | 11.7k, 12.3k | 13, 8 | 0 of 8 | 5 of 8 |
| new skill | 6.6k, 7.4k | 1, 2 | 8 of 8 | 8 of 8 |

Directional, two runs per arm. The old skill cost more than no skill: fan-out triggered its
CONTRACT mode and full templates. All arms handed approved fixes to the last agent as a file.

A first live call made with the new brief (a haiku lookup) wrote three good levels, but also
pasted L3 into its reply and reworded L2 inline. Hence the Return line: "copied from the file,
and its path. L3 stays in the file".

## Live tests after install
<!-- Lines 74-97 -->

Three real tasks, each briefed by the skill and run twice: before and after decisions 9 and 10.
Agents: a read-only `Explore` on haiku returning inline; a `claude` agent on sonnet writing
`result.md`; a documentation lookup on haiku writing `result.md`. Each return was checked with
`scripts/check_result.py` and against a ground truth computed independently.

| Rule | First run | After 9 and 10 |
|---|---|---|
| Content correct against ground truth | 3 of 3 | 2 of 3: the haiku lookup inverted the observation it was given |
| Pinned facts identical at every level | 0 of 3 (4 with the first lookup) | 2 of 3: the haiku lookup wrote no `Pinned:` block |
| Inline reply identical to the file | 0 of 2 | 1 of 1 checked (sonnet) |
| File at the assigned path | 1 of 2: haiku mistyped a long path | 2 of 2 |
| L3 kept out of the inline reply | 2 of 2 (0 of 1 before the Return line was tightened) | 2 of 2 |

Also confirmed live: the lint hook, added to settings mid-session, blocked a brief that
requested no levels before any agent started; the three compliant briefs passed it. Replayed
offline, it passes all 8 briefs written with the skill in the experiment and blocks all 16
written without it; it would have blocked 99% of the 509 past calls, all for missing levels.

The sonnet agent met every rule after the change; the haiku agents met the format partly and
missed judgment twice. Open: whether a SKILL.md edited mid-session reaches a running session
(observed: the older text was served; two haiku lookups of the docs disagreed). Until settled,
start a new session after editing the skill.

## Decisions
<!-- Lines 100-132 -->

Each with the alternative ruled out.

1. **Rename to `subagent-orchestration`.** The scope now spans calls: run directory, chaining,
   fan-out. Ruled out: keeping `subagent-call`, which names a single call.
2. **The file holds all three levels; inline is L1 and L2 by default, L1 for fan-out.** Ruled
   out: all three inline, which puts L3 in the orchestrator's context. Also ruled out: the path
   alone inline, which costs a read for the L1 the orchestrator almost always needs.
3. **Levels defined by height, not word counts.** L1 rolls up everything, L2 each branch, L3
   nothing. Ruled out: fixed budgets per level; the budget is an output of purpose, receiver,
   and channel (level-of-detail practice).
4. **Pinned facts identical at every level.** Identical wording makes softening detectable by
   eye or script. Ruled out: a separate pinned list only, which leaves L2 and L3 free to drift.
5. **Pointer rule without the "already hold" exception; restatement named as pasting.** Ruled
   out: the old exception, which matched the measured failure.
6. **Fan-out uses a shared brief file plus slot values; CONTRACT is reserved for parsed returns,
   risky effects, resumable loops, and stored workflow steps.** Ruled out: CONTRACT for every
   fan-out, which was the costliest arm.
7. **Agents that cannot write files return L1 and L2 inline; L3 stays in the agent's context and
   is reached by continuing it.** Ruled out: forcing read-only types to write.
8. **Enforcement in three layers: link, one binding line, an optional lint hook.** Ruled out:
   the description alone, which makes a skill known, not binding.
9. **Every level opens with the same copied `Pinned:` block.** Measured: asked only for pins
   "word for word", agents reworded them every time (L2 tables, L3 prose). Ruled out: fuzzy
   matching in the checker, which would accept softened pins.
10. **The inline reply is read back from the file with `sed '/^## L3/,$d' <path>`.** Measured:
    retyped replies drifted from the file in every case; the read-back also fails loudly on a
    mistyped path. Ruled out: dropping the identity requirement, which leaves the orchestrator
    quoting text the record does not hold.
11. **A shape checker, `scripts/check_result.py`.** The orchestrator checks a return without
    reading it into its context. Ruled out: checking by eye, which costs the context the skill
    exists to save.

## Install and enforce
<!-- Lines 135-151 -->

From the repository root:

```bash
ln -s "$PWD/global_skills/subagent-orchestration" ~/.claude/skills/subagent-orchestration
```

Then one line in the global instructions (`~/.claude/CLAUDE.md`), in the sub-agent section:
"Before any sub-agent call, load the skill `subagent-orchestration` and follow it." A standing
instruction that tells the orchestrator to inline every constraint, path, and schema contradicts
the pointer rule; reword it to "point to it, inline only what exists nowhere on disk".

Optional, the strongest layer: [../hooks/lint_agent_prompt.py](../hooks/lint_agent_prompt.py), a
`PreToolUse` hook on `Agent` that blocks a brief with no explicit model, over 6,000 characters,
or with no three-level return, and tells the model what to fix. Wiring is in its docstring;
`--self-test` checks it. It does not see Workflow `agent()` prompts.

## Re-measure
<!-- Lines 154-161 -->

```bash
python3 build/audit_subagent_calls.py --since <install date, YYYY-MM-DD>
```

Read first: adoption (share of calls after loading the skill), then the share of prompts over
6,000 characters, repeated prompt text, and three levels requested. Against the baseline above,
these show whether the skill is used, and whether using it changes the briefs.
