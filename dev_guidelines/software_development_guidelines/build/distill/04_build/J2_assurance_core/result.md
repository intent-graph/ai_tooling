# J2_assurance_core: graph build result

## L1 headline

Pinned:
- Batch: `build/distill/04_build/J2_assurance_core/batch.yaml`, 38 operations: 19 `node.create` (3 L2 nodes ASSURANCE.RULES, ASSURANCE.BEHAVIOUR, ASSURANCE.CONTRACTS, then 16 L3 nodes: RULES.1 to .5, BEHAVIOUR.1 to .8, CONTRACTS.1 to .3) and 19 `link.create` (all intra-unit). The L1 node ASSURANCE is not in the batch (separate TOP batch).
- Cross links: 29, listed in `cross_links.md` for the linker.
- Dry-run validate line: `errors: 0, warnings: 0` (apply: `operations: 38`, `issues: 0`; scratch copy deleted).
- ASSURANCE.RULES.4 `epistemic_state` ends with `| unvalidated: awaiting maintainer, can an automated reviewer be the independent check`.

The unit's 19 nodes transcribe the final judge records with the final-pass resolutions and cross-unit fixes X1, X4, X5, X7, X13, X14 applied. The check passed against the current real graph, which already holds ASSURANCE and the other units, so no placeholder node was needed. One open maintainer point (RULES.4); everything else is as judged.

## L2 claims

Certainty marks are mine for this build: grounded = I ran it or read it in the named file; inferred = follows from grounded facts; open = not settled.

- Source of truth order followed: maintainer decisions, then `final_pass/resolutions.md` section J2 and `cross_unit_fixes.md`, then `judged.md` (grounded: read in full).
- RULES.4 (R27): the judge's default is kept (independence of the reviewer's context, not of its kind; a named person stays accountable) and the epistemic state carries the unvalidated annotation; the open regulatory question (external board) is carried as a gap (grounded for the transcription; the question itself is open).
- Applied overrides, all from the resolution lines and visible in the node text (grounded):
  - RULES.1 P8 and the platform-undo wording (R15, R26); the block-or-advise rule held there (X4).
  - BEHAVIOUR.2 split block/advise (X4).
  - BEHAVIOUR.4 holds d5, d6, d8 moved from BEHAVIOUR.7 (R22), with their ledger rows and pointers (L269, L270, L272); BEHAVIOUR.7 keeps d1, d2, d3, d7, d9 and d4 as a stack pointer.
  - BEHAVIOUR.5 carries "a gap found becomes a test" (X13); BEHAVIOUR.6 decides the coverage floor and rejects the 80% floor of SECURITY.3 row L1126 (X1, R21); BEHAVIOUR.7 d1 per X5.
  - CONTRACTS.1 holds the evolution policy by consumer reach and artifact kind, with L353 as a row (X7); RULES.4 holds the reason review is not reserved for uncertain changes (X14).
- Stack neutrality: intent, constraints and epistemic states name no product or language; products and sources (Google, DORA, NIST, OpenAPI and similar) appear only in design_notes and examples that quote a stack pointer (grounded: scanned by eye; no automated check).
- Links: 19 intra-unit links (types requires, refines, dataflow, conflicts, see). Types come from the judge records' wording (Requires, Conflicts, dataflow, "shared with", "refined by"); the validator accepted all of them (grounded). Two links are my reading of statements in the decision text rather than of a record's Links line: BEHAVIOUR.2 requires RULES.1 (X4 text) and BEHAVIOUR.3 requires RULES.2 ("the mix follows from RULES.2"); inferred.
- Traceability: each L3 node carries the judge pointer plus one pointer per original research claim behind its attached ledger rows (slot folder by prefix; web claims to the web guideline slots OPS 06_operations, ARCH 07_architecture_styles, DCON 17_data_contracts; JS principles to the package uid, all uids found in the package, grounded). L2 nodes hold the judge pointer only (no rows).
- Gap in traceability (inferred, not an error): ledger rows that merge JS-guideline research ids (QUALITY-, LANG-, SUPPLY- claims, 19 ids) have no slot in the brief's prefix list; they are reached through the JS package pointer of the same row and are not given a second pointer.
- Open: whether the linker should keep the three J4-owned pairings in `cross_links.md` (PERFORMANCE.4, AVAILABILITY.3 and .5 lines); listed with an origin column so they can be dropped if J4 emits them.

## L3 full

### What was read (grounded)

Brief `brief_build.md`; `maintainer_decisions.md` (MD-01 to MD-07); `03_judge/final_pass/resolutions.md` section J2 (R15 to R32); `03_judge/cross_unit_fixes.md` (X1 to X14, those naming J2); `03_judge/J2_assurance_core/judged.md` in full including "Review applied" and "Final pass applied"; `02_skeleton/branches/ASSURANCE/branch.md` for the rows attached per node and the tree; the three ledger parts for the `merges` column; the batch format in the graph-edit skill; the JS package for uids.

### Nodes in the batch, breadth-first

| uid | name | epistemic state head | constraints | impl pointers |
|---|---|---|---|---|
| ASSURANCE.RULES | Rules Common to Every Property | known, gap on numeric defaults | 0 | 1 |
| ASSURANCE.BEHAVIOUR | Behaviour | known, gap on .6 effects, .7, .8 | 0 | 1 |
| ASSURANCE.CONTRACTS | Interfaces and Contracts | known, gap on style choices | 0 | 1 |
| ASSURANCE.RULES.1 | Trustworthy Signal | known, gap numeric thresholds | 4 | 11 |
| ASSURANCE.RULES.2 | Placement and Feedback Speed | known, gap layering, ten minutes | 3 | 9 |
| ASSURANCE.RULES.3 | Gates That Cannot Be Skipped | known, gap fitness functions, one platform | 2 | 4 |
| ASSURANCE.RULES.4 | Independent Review That Binds | known, gap, then `unvalidated: awaiting maintainer` | 3 | 6 |
| ASSURANCE.RULES.5 | One Bar and Evidence for Every Change | known, gap P2, P5, single vendor source | 3 | 6 |
| ASSURANCE.BEHAVIOUR.1 | What the Suite Must Promise | known, gap strict/weak split | 3 | 10 |
| ASSURANCE.BEHAVIOUR.2 | Static Layer | known, gap types-as-first-layer | 2 | 9 |
| ASSURANCE.BEHAVIOUR.3 | Test Level Mix | known, gap shape per context | 2 | 8 |
| ASSURANCE.BEHAVIOUR.4 | Test Construction | known, gap d5, d6, d8 | 3 | 14 |
| ASSURANCE.BEHAVIOUR.5 | Tests Driven by Change | known, gap ordering contested | 2 | 5 |
| ASSURANCE.BEHAVIOUR.6 | Measuring Adequacy and Probing for Faults | known, gaps incl. open effect size of mutation testing | 2 | 10 |
| ASSURANCE.BEHAVIOUR.7 | Tests Without Durable Effect on Data | known, gap d2, d3, d7, d9 | 3 | 8 |
| ASSURANCE.BEHAVIOUR.8 | Defect Classes That Survive Review | inferred | 3 | 6 |
| ASSURANCE.CONTRACTS.1 | What Counts as Compatible | known, gap threshold, mapping | 2 | 6 |
| ASSURANCE.CONTRACTS.2 | Contract Tests | known, gap single-team seam | 2 | 10 |
| ASSURANCE.CONTRACTS.3 | One Source of Description | known, gap CI-blocks inferred | 3 | 7 |

Decisions on form (grounded, mine): the judge's `Decision` becomes `intent` rewritten stack-neutral in one to three sentences; the `Constraints:` line of each record becomes the constraint entries, with BEHAVIOUR.1's mixed line split into its three MUSTs and the two L2 roll-ups carrying none; `design_notes` carries positions (ledger ids), grounds, rejected positions with the condition under which each would be best, context, maintainer points, flags and routing notes; `examples` only where the record gives concrete cases (RULES.1, BEHAVIOUR.2, .4, .5, .6, .7, .8, CONTRACTS.1, .2, .3); `history` not set.

### Intra-unit links (19)

- RULES.1 conflicts BEHAVIOUR.7; CONTRACTS.1 conflicts CONTRACTS.2 (both from the records' Conflicts lines, resolved in the nodes).
- BEHAVIOUR.1 requires RULES.3 and RULES.1, refines RULES.5; BEHAVIOUR.2 requires RULES.3 and RULES.1; BEHAVIOUR.3 requires RULES.2; BEHAVIOUR.5 requires BEHAVIOUR.1; BEHAVIOUR.8 requires BEHAVIOUR.2.
- RULES.2 requires BEHAVIOUR.1 and RULES.3; RULES.5 requires RULES.1 and RULES.4; CONTRACTS.3 requires RULES.3.
- BEHAVIOUR.6 dataflow BEHAVIOUR.1; BEHAVIOUR.3 see BEHAVIOUR.4 and see CONTRACTS.2; CONTRACTS.2 see CONTRACTS.3.

### Cross links

29 rows in `cross_links.md` (source, target, type, intent, origin line). Groups: X-line pointers (X1, X4, X5, X7, X13, X14), realization by CHANGE_FLOW, ARTIFACT.2 and CONSTRUCTION, index pointers (RULES.4 to CHANGE_FLOW.REVIEW, TRANSVERSE.PRIVACY, TRANSVERSE.DOCS), the L2 BEHAVIOUR pointers to the four sibling property nodes, and the consumer-side pointers of CONTRACTS.1 and .2 into OWNERSHIP.

### Dry-run check (grounded: I ran it)

```text
cp intent_graphs/software_development_philosophy.ig.yaml <slot>/scratch.ig.yaml
ig-tool apply -g <slot>/scratch.ig.yaml --batch <slot>/batch.yaml -o <slot>/scratch.ig.yaml --role builder -m "dry build J2_assurance_core"
  status: ok / operations: 38 / issues: 0 / errors: 0 / warnings: 0   (graph after: nodes 178, links 120)
ig-tool validate -g <slot>/scratch.ig.yaml
  status: ok / nodes: 178 / links: 120 / errors: 0 / warnings: 0
```

Note on the check: the real graph at check time already held the L1 node ASSURANCE and the other units' nodes (the placeholder step of the brief failed with "Node 'ASSURANCE' already exists", which is the expected condition and needed no workaround). The batch applied cleanly on top of that state, so uid collisions with the already applied units are excluded for the graph as it stood. `scratch.ig.yaml` was deleted afterwards; the real graph, judge records, skeleton and ledger were not touched.

### Public-repository rule (grounded)

`batch.yaml` and `cross_links.md` contain no absolute or home paths (count of `/Users` and `/home`: 0); pointers are relative to the guideline root, as the brief prescribes.
