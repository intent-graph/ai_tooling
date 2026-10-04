# The three-level return

Read this when writing the Output and Pin lines of a brief, or when checking a return. It is
also what a sub-agent can be pointed at: "format result.md as in /abs/path/return_levels.md".
[SKILL.md](SKILL.md) section 3 has the rules in short.

## Contents
<!-- Lines 9-18 -->

1. [Template for result.md](#template-for-resultmd)
2. [What each level must do](#what-each-level-must-do)
3. [Pinned facts](#pinned-facts)
4. [The inline return](#the-inline-return)
5. [Worked example](#worked-example)
6. [Malformed returns](#malformed-returns)

---

## Template for result.md
<!-- Lines 21-47 -->

```markdown
# <task slug>: result

## L1 headline
<One sentence that answers the goal, with its certainty.>
Pinned:
- <pinned fact, word for word>

## L2 claims
Pinned:
- <the same pinned facts, copied from L1>
- <claim>. <grounded | inferred | open>. <pointer: file:line, command, URL>
- ...
Not checked: <what, and why>.

## L3 full
Pinned:
- <the same pinned facts, copied from L1>
### <branch 1>
<claim, certainty, grounds: what was read or run and what it showed; alternatives considered>
### <branch 2>
...
### Not checked
<what, why, and what it would take to check it>
```

## What each level must do
<!-- Lines 50-70 -->

The three levels are one outline shown at three heights. They hold the same content; they differ
in how much each line rolls up.

- **L1 rolls up everything** into the root claim: the answer to the goal, as a claim, never as a
  topic. "Validation belongs in `settings.load_config()`", not "Investigated config parsing".
  Its certainty is assessed on its own: a grounded conclusion can rest on findings that are
  partly inferred, and a conclusion built only from inferred findings is never grounded.
- **L2 rolls up each branch** to one line: the root's children, each with its own certainty and
  a pointer the reader can open. Lines differ in height. One raw fact may stand beside a line
  that rolls up twelve; when every line has the same size and shape, the agent trimmed instead
  of rolling up.
- **L3 rolls up nothing the purpose needs.** Organized by branch, not by the order of work: a
  log of steps is not L3. Each branch carries its grounds, the alternatives considered, and
  what remains open.

**The self-containment test**, applied to each level alone: could the orchestrator act on it,
quote it to the user, or hand it to another agent with no other level in hand? So: no "see
below", "as in L3", or "the issue above"; every name, file, and abbreviation introduced at its
first use within that level.

## Pinned facts
<!-- Lines 73-89 -->

A pinned fact is never rolled up. Every level opens with the same `Pinned:` block, copied from
L1, not rewritten; L3 also grounds each pin inside its branch. Identical wording lets the
orchestrator, or a script, check that nothing was softened on the way up. Asked only to keep
pins "word for word", agents reworded them in every measured return; a copied block holds.

Pin, and only pin:
- the facts the brief names;
- every effect outside the agent's slot: files changed, commands with side effects, anything
  irreversible or visible to others;
- failures, blockers, and contradictions with the brief;
- a decision someone else must make, phrased as a question with a recommendation;
- a number or identifier the goal hinges on.

When more than about five facts qualify, the task was cut too wide or something went wrong.
L1 says so, and the pins stay.

## The inline return
<!-- Lines 92-105 -->

The brief's Return line chooses what comes back in the tool result. The file always holds all
three levels. The agent does not retype the inline part: after writing the file it prints it
back and replies with that output unchanged, then the path.

```text
sed '/^## L3/,$d' /abs/run/<NN_slug>/result.md      # L1 and L2
sed '/^## L2/,$d' /abs/run/<NN_slug>/result.md      # L1 only
```

Retyped inline returns drifted from their file in every measured case; the read-back also
fails loudly when the file is not at the assigned path. The orchestrator quotes L1, merges
from L2, and opens L3 by section.

## Worked example
<!-- Lines 108-161 -->

Brief: find every place the CLI reads its `--config` value, to choose one place to add
validation. Pin: any path where a bad config is silently ignored.

```markdown
## L1 headline
Add validation in `settings.load_config()` (src/tool/settings.py:60), the only function that
both the --config flag and the APP_CONFIG environment variable reach. Inferred: the call
graph shows no other path, and I did not run the CLI.
Pinned:
- settings.py:88 catches an unreadable config file, ignores it, and starts with defaults.
- No files changed.

## L2 claims
Pinned:
- settings.py:88 catches an unreadable config file, ignores it, and starts with defaults.
- No files changed.
- cli.py:41 defines --config as a plain string; nothing checks that the file exists. Grounded.
- settings.py:72: APP_CONFIG overrides --config when both are set; this precedence is not
  documented. Grounded.
- `load_config()` is the only function both paths reach, so it is the one validation point.
  Inferred from the call graph; the CLI was not run.
- tests/test_settings.py covers environment precedence only, not unreadable files. Grounded.
Not checked: plugins/, which loads its own config; out of scope per the brief.

## L3 full
Pinned:
- settings.py:88 catches an unreadable config file, ignores it, and starts with defaults.
- No files changed.
### Flag path
cli.py:41 `parser.add_argument("--config", type=str)`; the value is passed unchanged to
`settings.load_config(path)` at cli.py:57. No existence or schema check on this path.
### Environment path
settings.py:72 reads APP_CONFIG and, when set, replaces the path argument. README.md describes
the flag only. Alternative considered: validating in cli.py. Rejected, because it would miss
this path.
### Silent fallback
settings.py:88 catches an unreadable config file, ignores it, and starts with defaults.
The handler is `except (OSError, ValueError): return DEFAULTS` with no log line. A typo in the
path therefore starts the tool on defaults with no warning.
### Tests
tests/test_settings.py: three tests, all about environment precedence; none covers an
unreadable or malformed file.
### Effects
No files changed.
### Not checked
plugins/ (out of scope). The claim that no other path reaches the config: found with a call
search for `load_config` and `APP_CONFIG`, not by running the CLI with tracing.
```

Note what changes between levels: L1 holds the decision and the two pins; L2 adds one line
per branch with its pointer; L3 adds the code, the rejected alternative, and the exact way the
"not checked" items were approached. Both pinned facts are identical at all three levels.

## Malformed returns
<!-- Lines 164-172 -->

`scripts/check_result.py` (beside this file) checks all of these but the first mechanically.
Send it back once, naming the defect:
- L1 is a topic, not a claim, or carries no certainty.
- A level refers to another level ("details in L3").
- A level lacks the `Pinned:` block, or a pin is worded differently at different levels.
- L2 lines are all the same size and shape: trimmed, not rolled up.
- L3 is a log of steps instead of branches with their grounds.
- The inline text differs from the file.
