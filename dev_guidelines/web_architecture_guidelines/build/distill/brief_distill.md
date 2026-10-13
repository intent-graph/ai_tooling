# Distillation brief — shared by every distillation step

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/web_architecture_guidelines/`
unless stated. Your task message gives the absolute root and your step.

## What exists

- `build/research/brief_shared.md` — what is being built, source tiers, claim format, and the
  round-2 scope decisions (in, light, out). Read it first.
- `build/research/01_…/` to `07_…/` (round 1), `08_coverage_check/` (gaps, overlaps,
  contested topics of round 1), `09_…/` to `14_…/` (round 2, filling those gaps). Each
  `result.md` has L1, L2, L3; L3 holds the source register and every claim.

## Decisions already taken (do not reopen)

- **Two IntentGraphs**, in `intent_graphs/`, mirroring the Python guideline's pair
  (`../python_guidelines/intent_graphs/README.md` explains that pair):
  - `web_app_philosophy.ig.yaml`, graph id `web-app-philosophy`, **product** graph: principles
    for designing a web application as a whole. The maintainer believes this philosophy
    differs from designing a backend alone or a database alone, with large overlaps. Round 2
    (`13_web_principles`) found the distinct core is the web *environment*; most other
    principles are shared. Represent both: web-distinct principles, and shared ones linked
    to their counterpart.
  - `web_defaults.ig.yaml`, graph id `pig-web-defaults`, **projection** graph (UIDs
    `PIG-WEB.*`, same convention as `PIG-PY.*` in the Python defaults graph): the
    stack-specific architecture decisions for JS + Python + Postgres.
- **Overlap with the Python philosophy graph** (`../python_guidelines/intent_graphs/python_kb_philosophy.yaml`,
  graph id `python-kb-philosophy`, 8 principles) is expressed as inter intentlinks, not by
  copying principles.
- **Traceability:** every node points to the claims it rests on, as impl_pointers of the form
  `build/research/<slot>/result.md::<CLAIM-ID>`. Source ids and divergent positions go in
  design_notes. Never cite a source a claim did not cite.
- **Superseded by `target_hierarchy.md` (max rule and judge record):** ~~Epistemic state from agreement~~ —
  the original rule read: consensus → `known`; majority → `known | conflict: <minority position>`
  or `risky`; contested → `undecided` with every position in design_notes. Those undecided
  nodes become questions for the maintainer; do not settle them yourself.
- **Scope out** topics become `deferred` nodes, not omitted.
- Public repository: no absolute or home paths, no private names, in anything written.
- IntentGraph rules: the primers in `../../../intent_graph/agents/` (PRIMER_00, 01, 03A),
  especially P2 (zooming preserves meaning), P4 (projection separation, language-swap test),
  P5 (normalized, no duplication across peers), UID format, node-name character safety.

## Superseded partition

The partition of `01_consolidate/skeleton.md` is superseded by `target_hierarchy.md`
(maintainer decision). `01_consolidate/` stays as the evidence base: its ledger rows and
source register remain valid.
