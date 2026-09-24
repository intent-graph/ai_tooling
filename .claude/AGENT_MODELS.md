# Agent Model Profiles

Source of truth for which model each agent uses under each cost profile.

When invoking an agent via the Task tool, pass the `model` parameter from the active profile column. The `model:` field in each agent's frontmatter matches the `regular` profile — it is the default when no profile is specified.

## Profiles

| Profile | Rule | When to use |
| ------- | ---- | ----------- |
| **regular** | Default assignments: opus for judgment, sonnet for balanced, haiku for mechanical | Normal work — quality matters, cost is secondary |
| **cheap** | Downshift one tier: opus→sonnet, sonnet→haiku, haiku→haiku | Iteration, drafts, bulk runs — acceptable quality at lower cost |

## Model Assignments

| Agent | regular | cheap |
| ----- | ------- | ----- |
| python-kb-agent | sonnet | haiku |
| doc-manifest-agent | haiku | haiku |
| diagram-agent | haiku | haiku |

IntentGraph's `ig-*` agents live in the sibling `intent_graph` repository; see
`../intent_graph/.claude/AGENT_MODELS.md` for their model assignments.


## Adding a Profile

Add a new column to the table above. Example:

| Agent | regular | cheap | turbo |
| ----- | ------- | ----- | ----- |
| ig-steward-agent | opus | sonnet | opus |
| ig-critic-agent | sonnet | haiku | opus |
| ... | ... | ... | ... |

Then reference the new profile name when invoking agents.

## Usage

When the user says **"cheap mode"** (or specifies a profile), read the model from the corresponding column and pass it as the `model` parameter in the Task tool call:

```
Task(
  subagent_type="ig-critic-agent",
  model="haiku",  ← from the 'cheap' column
  ...
)
```

When no profile is specified, use the `regular` column (which matches each agent's frontmatter `model:` field).
