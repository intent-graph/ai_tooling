# How to Program Subagents: Standardized Prompt I/O

When an orchestrator invokes a subagent, the prompt **is** the function call. This document defines a canonical structure for that prompt — typed inputs, explicit instructions, and a contracted output — so orchestrators never have to reverse-engineer what an agent needs.

## Table of Contents

1. [The Problem](#the-problem) _(Lines 50-65)_
1. [The Metaphor: Agents as Functions](#the-metaphor-agents-as-functions) _(Lines 68-94)_
1. [Canonical Prompt Template](#canonical-prompt-template) _(Lines 97-197)_
1. [Section Breakdown](#section-breakdown) _(Lines 200-200)_
   1. [Section 1: INPUT](#section-1-input) _(Lines 203-205)_
      1. [1.1 Context (immutable orientation)](#11-context-immutable-orientation) _(Lines 208-217)_
      1. [1.2 Working Material (the stuff to act on)](#12-working-material-the-stuff-to-act-on) _(Lines 220-253)_
      1. [1.3 Environment (execution configuration)](#13-environment-execution-configuration) _(Lines 256-264)_
      1. [1.4 Execution State (memory across invocations)](#14-execution-state-memory-across-invocations) _(Lines 267-276)_
   1. [Section 2: INSTRUCTIONS](#section-2-instructions) _(Lines 279-281)_
      1. [2.1 Primary Objective](#21-primary-objective) _(Lines 284-288)_
      1. [2.2 Initialization](#22-initialization) _(Lines 291-293)_
      1. [2.3 Algorithm / Execution Path](#23-algorithm--execution-path) _(Lines 296-298)_
      1. [2.4 Examples](#24-examples) _(Lines 301-303)_
      1. [2.5 Constraints, Exits & Escalations](#25-constraints-exits--escalations) _(Lines 306-316)_
   1. [Section 3: OUTPUT CONTRACT](#section-3-output-contract) _(Lines 319-321)_
      1. [3.1 Artifacts — the produced work product. Files written, inline results returned, handles created. Output handles use the same six-field structure as input handles (§1.2) so the orchestrator can pass them forward to the next agent without rewriting the contract.](#31-artifacts--the-produced-work-product-files-written-inline-results-returned-handles-created-output-handles-use-the-same-six-field-structure-as-input-handles-12-so-the-orchestrator-can-pass-them-forward-to-the-next-agent-without-rewriting-the-contract) _(Lines 324-324)_
      1. [3.2 State Mutation — scratchpad updates for the next invocation or handoff to another agent.](#32-state-mutation--scratchpad-updates-for-the-next-invocation-or-handoff-to-another-agent) _(Lines 327-327)_
      1. [3.3 Epistemology — the agent's self-assessment. Confidence score (how sure it is), and identified unknowns (what it couldn't determine). This prevents the orchestrator from treating uncertain output as ground truth.](#33-epistemology--the-agents-self-assessment-confidence-score-how-sure-it-is-and-identified-unknowns-what-it-couldnt-determine-this-prevents-the-orchestrator-from-treating-uncertain-output-as-ground-truth) _(Lines 330-330)_
      1. [3.4 Control Flow & Telemetry — routing signal for the orchestrator. The `Task Status` field drives the workflow state machine:](#34-control-flow--telemetry--routing-signal-for-the-orchestrator-the-task-status-field-drives-the-workflow-state-machine) _(Lines 333-340)_
      1. [3.5 Escalation Payload — populated **only** when status is `YIELD_FOR_INPUT`. This is the agent's structured request for help. It must contain:](#35-escalation-payload--populated-only-when-status-is-yield_for_input-this-is-the-agents-structured-request-for-help-it-must-contain) _(Lines 343-353)_
1. [Parameter Conventions](#parameter-conventions) _(Lines 356-356)_
   1. [Naming](#naming) _(Lines 359-372)_
   1. [Nullability](#nullability) _(Lines 375-377)_
   1. [Template vs. Instance](#template-vs-instance) _(Lines 380-391)_
1. [Orchestrator Workflow](#orchestrator-workflow) _(Lines 394-396)_
   1. [Step 1: Determine parameters from step definition](#step-1-determine-parameters-from-step-definition) _(Lines 399-401)_
   1. [Step 2: Assemble the INPUT section](#step-2-assemble-the-input-section) _(Lines 404-421)_
   1. [Step 3: Attach the INSTRUCTIONS section](#step-3-attach-the-instructions-section) _(Lines 424-426)_
   1. [Step 4: Attach the OUTPUT CONTRACT](#step-4-attach-the-output-contract) _(Lines 429-431)_
   1. [Step 5: Produce the instance](#step-5-produce-the-instance) _(Lines 434-436)_
   1. [Step 6: Invoke](#step-6-invoke) _(Lines 439-456)_
   1. [Step 7: Validate output and route](#step-7-validate-output-and-route) _(Lines 459-471)_
1. [Comparison to STEP_IO_PROTOCOL](#comparison-to-step_io_protocol) _(Lines 474-487)_
   1. [What stays the same](#what-stays-the-same) _(Lines 490-495)_




---

## The Problem
<!-- Lines 50-65 -->

Current orchestrator → agent communication is ad-hoc:

1. **Parameter discovery overhead.** The orchestrator reads each prompt template, scans for `{placeholders}`, and builds substitution logic per step. Every template has a different shape. Adding a parameter means editing both the template and the orchestrator.

2. **No I/O formalism.** Agent prompts mix context, instructions, and output expectations into one prose blob. There's no boundary between "what the agent receives" and "what the agent must do" and "what the agent must return." This means:
   - The orchestrator doesn't know which inputs are required vs optional without reading the full template.
   - The agent doesn't know its output contract until it parses prose mid-prompt.
   - Testing an agent invocation requires running it — there's no way to validate the call signature statically.

3. **Responsibility confusion.** Should the orchestrator assemble frontier context, or should the agent pull it? Should code files be inlined or pointed-to? These decisions are re-made per template instead of once.

The root cause: prompts are treated as documents, not as function calls.

---

## The Metaphor: Agents as Functions
<!-- Lines 68-94 -->

Think of the orchestrator as a **caller** and each agent as a **function**. The prompt is the function's **call signature**.

```
orchestrator                          agent (= function)
     │                                     │
     ├─ assembles arguments ──────────────▶ receives typed input
     │   (context, material, flags)        │
     │                                     ├─ reads instructions (= function body)
     │                                     │
     │                                     ├─ produces output (= return value)
     │◀──────────────── returns ───────────┤
     │   (artifacts, state, telemetry)     │
```

Three categories of data flow through this call:

| Category | Direction | What it contains | Mutability |
|----------|-----------|-----------------|------------|
| **Context** | In | Background knowledge the agent needs to orient. Graph state, primer docs, environment flags. | Immutable — agent reads, never writes. |
| **Working Material** | In | The stuff the agent acts on. Frontier YAML, source files, issue lists. May be inline or pointer-referenced. | Agent transforms this into output. |
| **Output** | Out | Produced artifacts (files, edits), state mutations (scratchpad, queue updates), and telemetry (status, confidence, resource usage). | Agent writes, orchestrator reads. |

This separation is the entire point. Once you know which slot each piece of data goes into, the prompt writes itself.

---

## Canonical Prompt Template
<!-- Lines 97-197 -->

Every agent invocation prompt follows this three-section structure. Parameters use `{{double_braces}}` to distinguish from literal text.

```markdown
# AGENT TASK PAYLOAD: {{task_id}}

## 1. INPUT

### 1.1 Context
- Inline: {{inline_context_text}}
- External (read if needed): {{external_context_uris}}

### 1.2 Working Material
- Inline Payload: `{{small_inline_data}}`
- Pointers: {{target_file_uris}}
- Stateful Handles:
  {{#each handles}}
  - Handle: `{{handle_id}}`
    - Invocation: `{{invocation_syntax}}`
    - Input Format: {{input_format_description}}
    - Output Format: {{output_format_description}}
    - Side Effects: {{side_effects_or_none}}
    - Example: `{{example_call}}` → `{{example_response}}`
  {{/each}}

### 1.3 Environment
- Execution Flags: `dry_run: {{is_dry_run}}`, `verbosity: {{verbosity_level}}`
- Effort Hint: {{effort_hint}}

### 1.4 Execution State
- Scratchpad / Memory: > {{previous_agent_notes}}
- Error Context (if retry): > {{reason_for_previous_failure}}

---

## 2. INSTRUCTIONS

### 2.1 Primary Objective
> {{main_goal_statement}}

### 2.2 Initialization
- Setup Steps: {{pre_execution_setup_instructions}}

### 2.3 Algorithm / Execution Path
- {{step_by_step_logic_or_decision_tree}}

### 2.4 Examples
- Input Example: `{{mock_input}}`
- Thought Example: `{{mock_reasoning_steps}}`
- Output Example: `{{mock_expected_output}}`

### 2.5 Constraints, Exits & Escalations
- Constraints: {{strict_negative_boundaries_what_not_to_do}}
- Exit Conditions: {{when_to_fail_fast_without_asking}}
- Escalation Rules: Yield and request input if confidence is below {{threshold}} on a destructive action, or if encountering a 50/50 technical split.
- Default Escalation Target: [HUMAN | ORCHESTRATOR]

---

## 3. OUTPUT CONTRACT
(The agent must return a payload matching this exact structure)

### 3.1 Artifacts
- Inline Return: {{expected_json_or_text_format}}
- Generated Pointers: {{uris_of_new_or_modified_files}}
- Stateful Handles (same structure as input handles — pass forward to next agent):
  {{#each output_handles}}
  - Handle: `{{handle_id}}`
    - Invocation: `{{invocation_syntax}}`
    - Input Format: {{input_format_description}}
    - Output Format: {{output_format_description}}
    - Side Effects: {{side_effects_or_none}}
    - Example: `{{example_call}}` → `{{example_response}}`
  {{/each}}

### 3.2 State Mutation
- Updated Scratchpad: {{notes_for_next_iteration_or_handoff}}

### 3.3 Epistemology
- Confidence Score: {{0.0_to_1.0}}
- Unknowns / Assumptions: {{identified_blind_spots_during_execution}}

### 3.4 Control Flow & Telemetry
- Task Status: [SUCCESS | PARTIAL | FAILURE | YIELD_FOR_INPUT]
- Summary: {{brief_summary_of_actions}}
- Resource Usage: `tokens: {{token_count}}, time: {{execution_time}}, tool_calls: {{tool_call_count}}`

### 3.5 Escalation Payload (Populate ONLY if Status is YIELD_FOR_INPUT)
- Target: [HUMAN | ORCHESTRATOR]
- Blockage Summary: {{clear_description_of_the_ambiguity_or_missing_data}}
- Impact Assessment: {{risk_of_guessing_wrong}}
- Proposed Options / Specific Question:
  - Option A: {{path_1_and_tradeoffs}}
  - Option B: {{path_2_and_tradeoffs}}
- Agent Recommendation: {{leaning_if_any}}
```

Not every section applies to every agent. Omit subsections that don't apply — but keep the three top-level sections and their numbering stable. The orchestrator always knows where to find what.

---

## Section Breakdown
<!-- Lines 200-200 -->

### Section 1: INPUT
<!-- Lines 203-205 -->

Everything the agent receives. Split into four subsections by role, not by format.

#### 1.1 Context (immutable orientation)
<!-- Lines 208-217 -->

What the agent needs to understand its situation. The agent reads this but never modifies it.

| Slot | Purpose | Example |
|------|---------|---------|
| `inline_context_text` | Small, critical context inlined for reliability. Agent primer summary, target UID, workflow step name. | `"Step: DISTILL.CHALLENGE, Target: PARSER, Workflow: distill"` |
| `external_context_uris` | Pointers to larger context the agent may read on demand. Reference docs, vocabulary files, tool registries. | `["AGENT_PRIMER.md", "VOCABULARY_AND_FORMALISM.md"]` |

**Design rule:** If it's < 200 tokens and critical for orientation, inline it. If it's reference material the agent may or may not need, point to it.

#### 1.2 Working Material (the stuff to act on)
<!-- Lines 220-253 -->

The actual payload the agent transforms. This is the functional "argument" in the programming metaphor.

| Slot | Purpose | Example |
|------|---------|---------|
| `small_inline_data` | Data small enough to inline (< 500 tokens). Critic issue list, short frontier excerpt. | `"issues: [{type: vagueness, node: D, severity: major}]"` |
| `target_file_uris` | Paths to files the agent must read and act on. Frontier YAML, source code, documentation. | `["{step_folder}/input_frontier.yaml", "{step_folder}/input_source/"]` |
| `handles` | Stateful resources the agent can invoke — tool endpoints, database cursors, streaming interfaces. Each handle carries its own mini-contract (see below). | See handle structure below |

**Handle structure.** A bare endpoint is useless — the agent doesn't know the calling convention, the expected input/output shapes, or whether it has side effects. Each handle entry provides six fields:

| Field | Purpose |
|-------|---------|
| `handle_id` | Short name the agent uses to refer to this handle in its output. |
| `invocation_syntax` | Exact command or API call to use. Copy-pasteable. |
| `input_format_description` | What arguments the handle accepts, and in what shape. |
| `output_format_description` | What the handle returns — shape, encoding, key fields. |
| `side_effects_or_none` | Whether calling this mutates state (`"none"` for read-only, or describe the mutation). |
| `example_call` → `example_response` | Concrete round-trip showing a realistic invocation and its output. |

Example handle entry:

```yaml
- handle_id: graph_query
  invocation: "ig-tool query -g {step_folder}/input_graph.json --node {uid} --depth 1"
  input_format: "uid = IntentNode UID string (e.g., 'PARSER'). depth = integer >= 0."
  output_format: "YAML to stdout: node fields + children list. Empty output if node not found."
  side_effects: none
  example: "ig-tool query -g graph.json --node D --depth 1"
    # → { uid: D, intent: "Parse input files", children: [D.1, D.2] }
```

**Design rule:** The orchestrator decides what's working material and what's context. The litmus test: *does the agent's output depend on transforming this specific data?* If yes → working material. If it's background knowledge → context.

#### 1.3 Environment (execution configuration)
<!-- Lines 256-264 -->

Flags that control how the agent runs, not what it does.

| Slot | Purpose | Example |
|------|---------|---------|
| `is_dry_run` | If true, agent proposes but doesn't write. | `false` |
| `verbosity_level` | Controls output detail. `quiet` / `normal` / `verbose`. | `"normal"` |
| `effort_hint` | Free-form guidance on how much time, thoroughness, and token budget the agent should spend. The orchestrator describes the depth-vs-speed tradeoff in natural language — no fixed enum. | `"Quick pass — flag obvious issues only, skip optional reads"` or `"Thorough — this is a retry after PARTIAL, cross-check everything"` |

#### 1.4 Execution State (memory across invocations)
<!-- Lines 267-276 -->

Carries state between retries or sequential invocations of the same agent.

| Slot | Purpose | Example |
|------|---------|---------|
| `previous_agent_notes` | Scratchpad from a prior invocation. The agent can use this to avoid repeating work. | `"Reviewed nodes D, D.1, D.2. D.3 was missing source."` |
| `reason_for_previous_failure` | If this is a retry, why the last attempt failed. | `"output_edits.yaml was malformed YAML — missing closing bracket on line 47"` |

**Design rule:** First invocation → these are empty/null. The orchestrator populates them only on retry or continuation.

### Section 2: INSTRUCTIONS
<!-- Lines 279-281 -->

What the agent must do. This is the function body — the algorithm, not the data.

#### 2.1 Primary Objective
<!-- Lines 284-288 -->

One sentence stating the goal. This is the function's docstring.

> "Review the product frontier and ProjectionIG observations for quality issues."

#### 2.2 Initialization
<!-- Lines 291-293 -->

Setup the agent should perform before the main work. Reading agent definition files, loading mode modules, validating inputs.

#### 2.3 Algorithm / Execution Path
<!-- Lines 296-298 -->

The step-by-step procedure or decision tree. This is where domain-specific logic lives. Can be a numbered list, a flowchart description, or a conditional tree.

#### 2.4 Examples
<!-- Lines 301-303 -->

Concrete input → reasoning → output examples. These ground the instruction in specifics and prevent drift. The three-part structure (input, thought, output) mirrors chain-of-thought prompting.

#### 2.5 Constraints, Exits & Escalations
<!-- Lines 306-316 -->

Three distinct concepts:

- **Constraints** are negative boundaries — what the agent must NOT do. Anti-foraging rules, scope limits, prohibited side effects.
- **Exit conditions** define when the agent should **fail fast without asking** — unrecoverable errors, budget exhaustion, hard invariant violations. These produce `FAILURE` status.
- **Escalation rules** define when the agent should **yield and ask for input** instead of guessing. Two canonical triggers:
  1. Confidence on a destructive action drops below `{{threshold}}` (e.g., applying edits that delete constraints, restructuring a graph region).
  2. A 50/50 technical split where both paths have real tradeoffs and the agent has no basis to prefer one.

  The agent sets `Default Escalation Target` to `HUMAN` (needs domain judgment) or `ORCHESTRATOR` (needs more context/data). On yield, the agent populates Section 3.5 and stops — it does not guess and continue.

### Section 3: OUTPUT CONTRACT
<!-- Lines 319-321 -->

What the agent must return. This is the function's return type — the orchestrator validates against this.

#### 3.1 Artifacts — the produced work product. Files written, inline results returned, handles created. Output handles use the same six-field structure as input handles (§1.2) so the orchestrator can pass them forward to the next agent without rewriting the contract.
<!-- Lines 324-324 -->

#### 3.2 State Mutation — scratchpad updates for the next invocation or handoff to another agent.
<!-- Lines 327-327 -->

#### 3.3 Epistemology — the agent's self-assessment. Confidence score (how sure it is), and identified unknowns (what it couldn't determine). This prevents the orchestrator from treating uncertain output as ground truth.
<!-- Lines 330-330 -->

#### 3.4 Control Flow & Telemetry — routing signal for the orchestrator. The `Task Status` field drives the workflow state machine:
<!-- Lines 333-340 -->

| Status | Meaning | Orchestrator action |
|--------|---------|-------------------|
| `SUCCESS` | Task completed fully | Proceed to next step |
| `PARTIAL` | Task completed with gaps | Human decides: accept partial or retry with more context |
| `FAILURE` | Unrecoverable error | Retry with different inputs, or escalate to human |
| `YIELD_FOR_INPUT` | Agent hit a decision it cannot make alone | Route escalation payload (§3.5) to target, then resume agent |

#### 3.5 Escalation Payload — populated **only** when status is `YIELD_FOR_INPUT`. This is the agent's structured request for help. It must contain:
<!-- Lines 343-353 -->

- **Target** — who should answer: `HUMAN` (domain judgment needed) or `ORCHESTRATOR` (more data/context needed).
- **Blockage Summary** — what specifically is ambiguous or missing.
- **Impact Assessment** — what goes wrong if the agent guesses. This lets the recipient triage urgency.
- **Proposed Options** — concrete alternatives with tradeoffs. The agent does the analysis work; the recipient only needs to pick.
- **Agent Recommendation** — the agent's leaning, if any. "I'd go with A because X, but B is defensible because Y." This is optional — if the agent truly has no preference, it says so.

The escalation payload turns yield from a vague "I'm stuck" into a structured decision request. The recipient can respond with a single line ("Option A") and the agent resumes.

---

## Parameter Conventions
<!-- Lines 356-356 -->

### Naming
<!-- Lines 359-372 -->

Parameters use `{{snake_case}}`. Names should be self-documenting:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `{{*_text}}` | Inline string content | `{{inline_context_text}}` |
| `{{*_uris}}` | List of file paths or URIs | `{{target_file_uris}}` |
| `{{*_data}}` | Structured data (JSON/YAML) | `{{small_inline_data}}` |
| `{{is_*}}` | Boolean flag | `{{is_dry_run}}` |
| `{{*_level}}` | Enum / graduated value | `{{verbosity_level}}` |
| `{{*_hint}}` | Free-form natural language guidance | `{{effort_hint}}` |
| `{{*_count}}` | Numeric metric | `{{token_count}}` |
| `{{handles}}` | List of stateful handle entries (each with 6 fields) | `{{handles}}` |

### Nullability
<!-- Lines 375-377 -->

If a parameter doesn't apply, omit the entire subsection — don't leave `{{param}}` as a placeholder. The orchestrator knows which subsections to include based on the step definition.

### Template vs. Instance
<!-- Lines 380-391 -->

A **template** is the canonical prompt structure with `{{params}}`. An **instance** is a filled template ready to send. The orchestrator:

1. Loads the template
2. Resolves parameters from the step definition + runtime state
3. Strips unused subsections
4. Produces the instance

The template is version-controlled. The instance is ephemeral (saved to `_prompt.md` in the step folder for observability).

---

## Orchestrator Workflow
<!-- Lines 394-396 -->

How the orchestrator uses this template to invoke an agent:

### Step 1: Determine parameters from step definition
<!-- Lines 399-401 -->

The dispatch table (e.g., `dispatch_distill.md`) declares which agent, which inputs, and which mode modules each step uses. The orchestrator reads this once per workflow, not per invocation.

### Step 2: Assemble the INPUT section
<!-- Lines 404-421 -->

```
Context:
  inline  ← step metadata (step UID, target, workflow type)
  external ← reference doc paths from dispatch table

Working Material:
  inline  ← small data (< 500 tokens) from previous step output
  pointers ← file paths assembled by ig-tool step create

Environment:
  flags ← workflow configuration (dry_run, verbosity)

Execution State:
  scratchpad ← from workflow_state.json (if continuation)
  error ← from previous invocation trace (if retry)
```

### Step 3: Attach the INSTRUCTIONS section
<!-- Lines 424-426 -->

Copy from the canonical template for this step. Instructions are step-specific and version-controlled — the orchestrator does not compose them at runtime.

### Step 4: Attach the OUTPUT CONTRACT
<!-- Lines 429-431 -->

Also from the canonical template. The output contract is the same every time the step runs.

### Step 5: Produce the instance
<!-- Lines 434-436 -->

Combine sections 1-3, strip empty subsections, write to `{step_folder}/_prompt.md`.

### Step 6: Invoke
<!-- Lines 439-456 -->

Two modes:

**Full-prompt mode** — send the entire instance as the Task prompt. Simple, works for small prompts.

**Pointer mode** — send a minimal prompt that points to the instance on disk. Keeps orchestrator context lean.

```text
Execute the task described in:
  {{step_folder}}/_prompt.md

Template parameter values:
  {{step_folder}}: /abs/path/to/steps/006_DISTILL.CHALLENGE
  {{target_uid}}: PARSER

All other content is literal text from the template.
```

### Step 7: Validate output and route
<!-- Lines 459-471 -->

The orchestrator checks the returned payload against section 3's contract:
- Required artifacts present?
- Task status is a valid enum value?
- If `PARTIAL` or `FAILURE`, are gaps reported?
- If `YIELD_FOR_INPUT`, is section 3.5 populated with a valid target, blockage summary, and at least one proposed option?

On `YIELD_FOR_INPUT`, the orchestrator routes the escalation payload to the specified target (human or orchestrator-level logic), collects the response, injects it into section 1.4 (Execution State), and re-invokes the agent. The agent resumes from where it stopped.

This validation is mechanical — no LLM needed.

---

## Comparison to STEP_IO_PROTOCOL
<!-- Lines 474-487 -->

This template formalizes what [`STEP_IO_PROTOCOL.md`](../../intent_graph/agents_runtime/orchestrator/STEP_IO_PROTOCOL.md) already does, with three key improvements:

| Aspect | STEP_IO_PROTOCOL (current) | This template |
|--------|---------------------------|---------------|
| **Parameter discovery** | Orchestrator reads template, scans for `{placeholders}` | Parameters are declared in the INPUT section with typed slots |
| **I/O boundary** | Input files, task, output, constraints — four sections with mixed concerns | Three clean sections: INPUT (data in), INSTRUCTIONS (logic), OUTPUT (data out) |
| **Output contract** | Prose description + file naming convention | Structured contract with status enum, confidence, telemetry |
| **Retry/continuation** | Not formalized — orchestrator re-invokes from scratch | Section 1.4 carries execution state across retries |
| **Self-assessment** | Agent reports gaps as YAML in output file | Section 3.3 (Epistemology) is a first-class part of every return |
| **Yield/escalation** | Not formalized — agent either completes or fails | `YIELD_FOR_INPUT` status + structured escalation payload (§3.5) with options, impact, and recommendation |

**Migration path:** Existing templates in `agent_invocation_prompt_templates/` can be refactored one-by-one. The three-section structure is backward-compatible — existing agents don't need to change, only the prompt shape does.

### What stays the same
<!-- Lines 490-495 -->

- Step folders and the manifest pattern
- Filesystem for bulk data, inline for orientation
- Anti-foraging rule
- Write-to-disk, summarize-to-orchestrator output pattern
- `ig-tool` for step creation, trace recording, edit application
