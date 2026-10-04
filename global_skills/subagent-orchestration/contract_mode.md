# CONTRACT mode — the typed sub-agent payload

Read this when [SKILL.md](SKILL.md) section 6 picked CONTRACT: the return is parsed by code,
the prompt is a stored workflow step, the agent can cause risky effects, or it will be resumed. Everything in
SKILL.md still applies (pointers, run directory, three levels); this file adds the structure.

## Contents
<!-- Lines 9-17 -->

1. [Template](#template)
2. [What each slot is for](#what-each-slot-is-for)
3. [Parameter conventions](#parameter-conventions)
4. [Pointer mode, for fan-out](#pointer-mode-for-fan-out)
5. [Validate the return](#validate-the-return)

---

## Template
<!-- Lines 20-111 -->

Strip subsections that do not apply; keep the three sections and their numbering, so the agent
and any script always know where to find what. Never leave a `{{placeholder}}` in an instance.

```markdown
# AGENT TASK: {{task_id}}

## 1. INPUT

### 1.1 Context (read, do not modify)
- Read first: {{context_uris}}               # absolute paths, each with the part to read and why
- Session-only delta: {{session_delta_text}} # decisions, ruled-out options, user preferences; not on disk

### 1.2 Working material (transform this)
- Pointers: {{target_file_uris}}
- Inline payload, only if it exists nowhere on disk (< 500 tokens): {{small_inline_data}}
- Handles:
  - handle_id: {{handle_id}}
    invocation: {{invocation_syntax}}
    input_format: {{input_format_description}}
    output_format: {{output_format_description}}
    side_effects: {{side_effects_or_none}}
    example: {{example_call}} → {{example_response}}

### 1.3 Environment
- is_dry_run: {{is_dry_run}}
- run_dir: {{run_dir_uri}}                   # absolute; this agent's slot is {{slot_uri}}
- write_scope: {{write_scope_text}}          # its slot, plus exact project paths, or read-only
- effort_hint: {{effort_hint}}

### 1.4 Execution state (retry or continuation only)
- previous_agent_notes: {{previous_agent_notes}}
- reason_for_previous_failure: {{reason_for_previous_failure}}

---

## 2. INSTRUCTIONS

### 2.1 Objective
{{main_goal_statement}}                      # one sentence, plus what the result is used for

### 2.2 Initialization
{{pre_execution_setup_instructions}}         # what to read first, what to check exists

### 2.3 Algorithm
{{step_by_step_logic_or_decision_tree}}

### 2.4 Example
- Input: {{mock_input}}
- Output: {{mock_expected_output}}

### 2.5 Constraints, exits, escalations
- Must not: {{strict_negative_boundaries}}
- Fail fast (→ FAILURE) when: {{when_to_fail_fast}}
- Yield (→ YIELD_FOR_INPUT) when: a destructive action you are not sure is intended; a choice
  between paths with real trade-offs and no objective tiebreak; {{task_specific_yield_triggers}}
- Escalation target: HUMAN | ORCHESTRATOR

---

## 3. OUTPUT CONTRACT
Return exactly this shape. The caller validates it mechanically.

### 3.1 Artifacts
- Result file: {{result_uri}} with sections L1 headline, L2 claims, L3 full, each readable
  alone (format: return_levels.md, beside this file)
- Inline return: {{inline_levels_level}}, copied from the result file, and its path  # L1 | L1+L2
- Files written: {{uris_of_new_or_modified_files}}
- Output handles (same six fields as 1.2): {{output_handles}}

### 3.2 State
- Notes for the next invocation or hand-off: {{notes_for_next_iteration}}

### 3.3 Certainty and pins
- Per claim: grounded | inferred | open
- Not checked: {{what_was_not_checked}}
- Pinned, word for word at every level: {{pinned_facts_text}}, plus every effect outside the
  slot, every failure or contradiction with this contract, every decision needed

### 3.4 Control
- task_status: SUCCESS | PARTIAL | FAILURE | YIELD_FOR_INPUT
- summary: {{one_to_three_lines}}

### 3.5 Escalation (only if YIELD_FOR_INPUT)
- target: HUMAN | ORCHESTRATOR
- blockage: {{what_is_ambiguous_or_missing}}
- impact: {{what_goes_wrong_if_guessed}}
- options: A — {{path_and_trade_off}}; B — {{path_and_trade_off}}
- recommendation: {{leaning_and_why, or "no preference"}}
- if nobody answers: {{default_outcome}}
```

## What each slot is for
<!-- Lines 114-130 -->

- **Context vs working material.** Does the output depend on transforming this data? Then it
  is working material (1.2). Background it only needs to read is context (1.1).
- **Inline vs pointer.** Anything on disk is a path, even if you have already read it: pasting
  or restating it costs your context again, and N times in a fan-out. Inline only the
  session-only delta, and short excerpts that exist nowhere on disk.
- **Handles.** A bare command is not enough: give the exact invocation, the input and output
  shapes, side effects, and one real round-trip.
- **Execution state (1.4).** Empty on a first call. On a retry, say what came back and why it
  was unusable; on a continuation, the prior notes.
- **Exits vs yields.** An exit is unrecoverable (missing input, invariant broken): report
  FAILURE and stop. A yield is a decision the agent should not make alone: fill 3.5 and stop.
  Neither guesses and continues.
- **Certainty (3.3).** Per claim, not one score for the whole return: the caller needs to know
  which lines it can build on without re-checking. Pinned facts are what the caller must see
  even if it reads only L1.

## Parameter conventions
<!-- Lines 133-149 -->

`{{snake_case}}`, with a suffix that states the type:

| Suffix | Type | Example |
|---|---|---|
| `*_text` | inline string | `inline_context_text` |
| `*_uris` | list of paths or URIs | `target_file_uris` |
| `*_data` | structured JSON / YAML | `small_inline_data` |
| `is_*` | boolean | `is_dry_run` |
| `*_level` | enum | `verbosity_level` |
| `*_hint` | free-form guidance | `effort_hint` |
| `*_count` | number | `retry_count` |

A **template** has the `{{params}}`; an **instance** is the filled copy that is sent. Keep the
template under version control and save instances next to the run for traceability when the
call is part of a workflow.

## Pointer mode, for fan-out
<!-- Lines 152-162 -->

Write the instance (or the template) to disk once and send each agent a short prompt:

```text
Execute the task described in /abs/path/run_042/_prompt.md.
Parameter values: {{output_file_path}} = /abs/path/src/fn_a.sql; {{design_section}} = 5.2.
All other content is literal text from that file.
```

The caller's context stays small, and every agent reads the same contract.

## Validate the return
<!-- Lines 165-182 -->

Mechanical first, then the artifact itself (SKILL.md section 7).

1. Required artifacts present, files exist where 3.1 says; the result file has L1, L2, L3, and
   the pinned facts appear word for word in L1.
2. `task_status` is one of the four values.
3. PARTIAL or FAILURE → gaps listed in 3.3.
4. YIELD_FOR_INPUT → 3.5 has target, blockage, impact, at least two options, recommendation.

| Status | Caller action |
|---|---|
| SUCCESS | Verify the artifact, then proceed. |
| PARTIAL | Accept the gap, or re-invoke with tighter input and 1.4 filled. |
| FAILURE | Re-invoke with corrected input, or bring it to the user. |
| YIELD_FOR_INPUT | Route 3.5 to its target. HUMAN → present the options as the agent framed them, without pre-deciding. ORCHESTRATOR → decide from what you hold. Then continue the same agent with `SendMessage`, sending the answer as 1.4. |

A malformed escalation (missing fields, a prose question) is sent back once with a request to
fill 3.5; it is not answered as-is.
