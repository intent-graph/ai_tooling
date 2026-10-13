# Assembly brief: stage 6 (build the IntentGraphs)

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/javascript_guidelines/`
unless stated. Your task message gives the absolute root.

## Read first

- IntentGraph rules, compressed primers in `../../../intent_graph/agents/compressed/`:
  `PRIMER_00_PHILOSOPHY.md`, `PRIMER_01_SEMANTICS.md`, `PRIMER_03A_EDITING.md`,
  `PRIMER_TOOLS.md`, `PRIMER_05_INTENT_RESOURCES.md`.
- Exact `ig-tool` syntax: `../../../intent_graph/.claude/skills/ig-tool-graph-edit/SKILL.md`
  (batch format: read before authoring any batch) and
  `../../../intent_graph/.claude/skills/ig-tool-query/SKILL.md` (init, validate, query).
- Precedent, for shape only: `../python_guidelines/intent_graphs/` (`README.md`,
  `intent_resources.yaml`, and the first 120 lines of `python_defaults.ig.yaml`).
- What to build: `build/distill/skeleton.md` (node tables, intentlinks, inter links, judge
  records), `build/distill/claims_ledger.md` (rows per node), `build/distill/result.md`
  (`## L2 claims`). Read `build/distill/decisions_for_review.md` for the decisions' wording.

## What you build, in `intent_graphs/`

- `js_philosophy.ig.yaml`: graph `js-philosophy`, product graph, root uid `ROOT`.
- `js_defaults.ig.yaml`: graph `pig-js-defaults`, projection graph, root uid `PIG-JS.ROOT`,
  every uid prefixed `PIG-JS.` (as `PIG-PY.` in the Python defaults graph).
- `intent_resources.yaml`: product `js-philosophy`; projection target `javascript`:
  `pig-js-defaults`; also list `python-kb-philosophy` (relative path to the Python philosophy
  file) so the inter links resolve.
- `README.md`: what each graph holds, how to read it, the mapping to the build, in the shape of
  the Python `intent_graphs/README.md`.

## Field mapping, per node

- `name`, `intent`, `epistemic_state`: from the skeleton, unchanged in meaning. Philosophy
  intents state WHY; defaults intents state the rule as intent (what and why, not code).
- `constraints`: the node's `decision` ledger rows, each as one MUST or MUST NOT sentence;
  then its `acceptable-when` rows as "Acceptable only when <condition>: <practice>".
- `design_notes`: the judge record (positions, forces, decision, rejected with the condition
  under which each would win), the source ids the rows cite, and a "Rejected beliefs" line for
  every `rejected` folklore row.
- `impl_pointers`: one entry per claim of the node's ledger rows, in the form
  `build/research/<slot>/result.md::<CLAIM-ID>` (list of strings).
- `examples`: only where the skeleton or the claims give a concrete case.
- Intentlinks and inter links: exactly those of the skeleton, with their sentences; inter
  endpoints qualified `graph_id:node_uid`. Planned links to the web-architecture graphs are not
  created; list them in `README.md` as planned.

## How

- Build with `ig-tool` only (init, then batch apply), never by hand-writing YAML; pass
  `--role assembler` and `-m "<why>"` on every mutating command.
- Run `ig-tool validate` on each graph after each batch; 0 errors is the gate.
- Check completeness by script: every skeleton node exists in its graph, every ledger row's
  claims appear in its node's `impl_pointers`, every skeleton link exists.
- Public repository: no absolute or home paths, no private names, in anything you write.

## Result file

Write `build/assemble/result.md` with `## L1 headline`, `## L2 claims`, `## L3 full`, each
readable alone, findings marked grounded, inferred or open. Pin, word for word at every level:
node and link counts per graph, the validate summary line of each graph, any skeleton element
not built and why.

Write only in `intent_graphs/` and `build/assemble/`. Never commit, never `git push`.
