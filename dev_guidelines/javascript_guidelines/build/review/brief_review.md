# Review brief: stage 7 (independent review)

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`
unless stated. Your task message gives the absolute root. You built none of this: review it
as a skeptical reader whose job is to find what is wrong, not to approve.

## Read first

- `build/plan.md`, all of it: goal, boundary, admission policy, maintainer decisions.
- `build/distill/target_hierarchy.md`: the tree, the **max** selection rule ("I dont want you to
  bring me the internet average, aka avg(all sources). I want you to do max(all sources). It's
  ok to make choices and pick the best."), the judge record.
- `intent_graphs/README.md`, then the two graphs through `ig-tool` (never read a graph file
  whole): `ig-tool tree -g <graph> --show-intent`, `ig-tool query -g <graph> --node <UID>`.
  Command reference: `../../../intent_graph/agents/compressed/PRIMER_TOOLS.md`.
- IntentGraph rules: `../../../intent_graph/agents/compressed/PRIMER_00_PHILOSOPHY.md`,
  `PRIMER_01_SEMANTICS.md`, `PRIMER_03A_EDITING.md`.
- Evidence, as needed: `build/distill/decisions_for_review.md`, `build/distill/claims_ledger.md`,
  the claim tables in `build/research/<slot>/result.md`, `build/audit/source_register.md`.

## What to check, in order of weight

1. **Max, not average.** For each decision in `decisions_for_review.md` and a sample of other
   decision nodes across all eight branches: is it the most demanding practice an admitted
   source supports for the branch's purpose, or a compromise? Name every decision that settles
   for the middle when a stricter grounded position exists.
2. **Grounding.** For a sample of at least 40 decision nodes spread over the branches, follow
   `impl_pointers` to the claims and their sources: does the claim say what the node says? Is
   a restricted source used beyond its restriction? Is anything invented (a rule no claim
   states)? Default to refuted when you cannot confirm.
3. **Quote check.** For the 15 highest-criticality decisions (security in DEFENSE and
   DEPENDENCIES first), fetch the cited T1 source and confirm the decisive passage exists in
   it. Ask your fetch tool for the verbatim passage; record which you confirmed, which you
   could not, and which the source contradicts.
4. **Security completeness.** Would a team following these graphs still ship an obvious hole?
   Name it, with the admitted source that covers it if one exists in the register.
5. **IntentGraph quality.** P2 (children refine, never extend), P4 (language-specific content
   only in the defaults graph), P5 (no duplication across peers), intent states WHY not HOW,
   epistemic states honest (a single-source decision marked `known` without `unvalidated` is a
   finding), `ig-tool validate` clean.
6. **Usability.** Could an engineer apply a branch's rules without reading the build? Name the
   nodes whose intent or constraints are unclear.
7. **Public-repository hygiene.** No absolute or home paths, no private names, anywhere under
   the guideline folder.

## Result file

Write `build/review/result.md` with `## L1 headline` (verdict in one sentence and its
certainty, then `Pinned:`), `## L2 claims` (one line per finding: severity `blocking` |
`major` | `minor`, the node uid or file, what is wrong, the fix; marked grounded, inferred or
open), `## L3 full` (every finding with its evidence, the sample you checked, the quotes
confirmed and not confirmed).

Pin, word for word at every level: counts of findings by severity; the number of decisions
found to settle for the average; quotes confirmed, not confirmed, contradicted; any invented
rule.

Write only in `build/review/`. Do not edit the graphs or the build. Never commit, never
`git push`.
