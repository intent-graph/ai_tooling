# JavaScript Guidelines

Solid, maintainable, secure JavaScript in the browser and in Node, at the language level. JavaScript
is the most misused language, yet with strong principles it is made useful and safe: the guideline
narrows it to a checked subset rather than avoiding it. It is held as two IntentGraphs, distilled
from audited authoritative sources only.

## Table of Contents

1. [What This Is](#what-this-is) _(Lines 21-31)_
1. [How to Read](#how-to-read) _(Lines 34-46)_
1. [The Two Graphs](#the-two-graphs) _(Lines 49-61)_
1. [How It Was Built](#how-it-was-built) _(Lines 64-82)_
1. [Maintainer Decisions](#maintainer-decisions) _(Lines 85-95)_
1. [Related Guidelines](#related-guidelines) _(Lines 98-104)_

---

## What This Is
<!-- Lines 21-31 -->

- **Is**: a set of decisions, each the best practice an admitted source supports for its purpose
  ("max, not average": the best of the sources, never their average; best is not most demanding), with every rejected alternative kept with the condition under
  which it would win, and every rule traced to claims and sources.
- **Is not**: a survey of what the web says, a framework manual, or a project life-cycle guide
  (sourcing, application architecture, UX validation, deploy, operations and development process
  belong to the software development guideline).
- **Honest about evidence**: a rule resting on a single source, on inference, or on a summarized
  quote carries `unvalidated: <why>` in its epistemic state; ten rules stay `undecided` because no
  admitted source states one.

## How to Read
<!-- Lines 34-46 -->

- **In Obsidian**: run `intent_graphs/export_to_obsidian.sh`, open `intent_graphs/obsidian_export/`
  as a vault, start at `js_defaults/viz/__FT_ROOT.canvas`. See
  [intent_graphs/obsidian_export/README.md](intent_graphs/obsidian_export/README.md).
- **With `ig-tool`**: `ig-tool tree -g intent_graphs/js_defaults.ig.yaml --show-intent` for the
  tree, `ig-tool query -g intent_graphs/js_defaults.ig.yaml --node <UID>` for one rule with its
  constraints, judge record and evidence pointers.
- **The graphs' own guide**: [intent_graphs/README.md](intent_graphs/README.md): what each graph
  holds, what is not covered, the planned links to sibling guidelines.
- **What the build decided, and why**:
  [build/distill/decisions_for_review.md](build/distill/decisions_for_review.md), one entry per
  weighty decision with its rejected positions; the maintainer may overrule any line.

## The Two Graphs
<!-- Lines 49-61 -->

| Graph | File | Holds |
|---|---|---|
| `js-philosophy` (product) | [intent_graphs/js_philosophy.ig.yaml](intent_graphs/js_philosophy.ig.yaml) | 56 principles that follow from what JavaScript is, or matter especially in it |
| `pig-js-defaults` (projection, `PIG-JS.*`) | [intent_graphs/js_defaults.ig.yaml](intent_graphs/js_defaults.ig.yaml) | 287 concrete rules |

Both share eight branches, in dependency order: **SUBSET** (which parts of the language to use),
**CONTRACTS** (types at build time, parsing at trust boundaries), **CONTROL** (time, failure and
resources made explicit), **STRUCTURE** (modules and their dependencies), **DEFENSE** (every input
hostile, every sink dangerous), **DEPENDENCIES** (third-party code runs with your privileges, and
the framework short list), **VERIFICATION** (machines check what people forget), **RUNTIME**
(measured behaviour). Language-general principles were sent to the software development guideline.

## How It Was Built
<!-- Lines 64-82 -->

The full record is [build/plan.md](build/plan.md); each stage keeps its brief and its results in
`build/`.

1. **Discover** candidate sources per research area; **audit** each by an independent agent
   against six gates (authority, currency, grounds, primary source, conflict of interest,
   consistency with the spec); no community source admitted. 443 documents audited, 412 admitted
   (261 for restricted uses only), 31 rejected with the gate they failed:
   [build/audit/source_register.md](build/audit/source_register.md),
   [build/audit/rejections.md](build/audit/rejections.md).
2. **Extract** 700 claims from admitted sources only, checked by script.
3. **Check coverage and dissent**, including a folklore audit: popular beliefs confirmed,
   restricted or refuted against primary sources.
4. **Consolidate** under the max rule, **assemble** with `ig-tool`, **review** independently, fix.
   Two security gap rounds followed the first review.

Rebuilding: edit the integrated files in `build/distill/`, then run the steps in
[build/patch/brief_patch.md](build/patch/brief_patch.md) (never `build/distill/5c_integrate/integrate.py`).

## Maintainer Decisions
<!-- Lines 85-95 -->

Recorded verbatim in [build/plan.md](build/plan.md), section Maintainer decisions. In short:

- Only authoritative sources; max, not average; the build may choose and record why.
- TypeScript in scope as a decision (the build chose strict TypeScript); browser and Node; a short
  list of framework candidates rather than framework rules.
- Scope stays at the language level; language-general principles go to the software development
  guideline, what is specific to or especially important in JavaScript stays here.
- No readable guideline document for now; quotes stay marked tool-extracted; the ten undecided
  rules stay undecided.

## Related Guidelines
<!-- Lines 98-104 -->

- [../web_architecture_guidelines/](../web_architecture_guidelines/README.md): who does what across
  database, backend and browser; rendering strategy; session architecture.
- [../software_development_guidelines/](../software_development_guidelines/): sourcing, application
  architecture, verification and validation, delivery, operation, for any language.
- [../python_guidelines/](../python_guidelines/README.md): Python code; its philosophy graph is
  linked from `js-philosophy`.
