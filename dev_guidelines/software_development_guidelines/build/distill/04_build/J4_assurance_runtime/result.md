# Result: build of unit J4_assurance_runtime

## L1 headline

Batch built and dry-run checked: 15 nodes (3 L2, 12 L3 under ASSURANCE) and 8 intra-unit links, validate 0 errors and 0 warnings; 37 cross links are listed for the linker. Certainty: grounded for the transcription (every field comes from the final judge record, final pass and cross-unit lines X5, X11, X13 already applied in it); inferred for the three roll-up nodes. Open: none for J4.

Pinned:
- Nodes in the batch: 15 (ASSURANCE.PERFORMANCE and .1 to .5; ASSURANCE.AVAILABILITY and .1 to .5; ASSURANCE.ARTIFACT and .1, .2).
- Intra-unit links: 8 (requires 3, see 5).
- Cross links listed: 37, in cross_links.md.
- Dry-run validate: `nodes: 17, links: 8, errors: 0, warnings: 0` (17 = 15 plus ROOT plus the ASSURANCE placeholder, scratch copy deleted).

## L2 claims

- Batch: 15 node.create in breadth-first order (3 L2 nodes, then 12 L3), then 8 link.create; the 7 L1 nodes and the ROOT update are not here (TOP batch). Grounded (dry run applied 23 operations, all success).
- Fields: name and uid from the skeleton; intent written stack-neutral (no product, tool, language names); constraints are the judge record's MUSTs split one per entry (L3 nodes only, roll-up nodes carry none); design_notes carry the judge record's grounds, positions, rejected, context, certainty and links verbatim, plus maintainer-decision and final-pass notes; impl_pointers carry the judge record and every original claim behind the attached ledger rows. Grounded.
- Epistemic states: 12 L3 nodes `known`, with `| gap:` annotations where the record marks inferred or open parts (PERFORMANCE.2 and .5, AVAILABILITY.1 to .5, ARTIFACT.1); 3 roll-ups `inferred: roll-up ...`. None undecided, none `unvalidated` (no maintainer point for J4). Grounded.
- Intra-unit links: PERFORMANCE.2 requires .1; .3 requires .5; PERFORMANCE.4 requires AVAILABILITY.3; PERFORMANCE.2 see .4; AVAILABILITY.1 see .2 and .3; AVAILABILITY.3 see .5; AVAILABILITY.4 see .5. Symmetric "related" statements in the record (.5 to .3, .5 to .4, .2 to .1) are kept once, in one direction. Grounded for the content, inferred for the direction chosen (source depends on target).
- Cross links: 37 rows in cross_links.md, to OPERATION, CHANGE_FLOW, OWNERSHIP, CONSTRUCTION and the other ASSURANCE units (BEHAVIOUR, RULES, SECURITY, DATA_INTEGRITY). Two targets do not exist yet: OPERATION.TELEMETRY.7 (created by X12) and a CONSTRUCTION node for degraded-mode design (record names only the branch). Inferred where the record says "realized by" (written as `realizes` from the realizing node).
- Not done, by design: X2 (ASSURANCE L1 re-roll, wave 3). Link shape types (`requires`, `see`) are free text and accepted by the tool; `see` is not in the primer's four patterns. Open: none.
- Judge-record corrections: none needed; no contradiction found between judged.md, resolutions and cross-unit fixes. Grounded.

## L3 full

Files written (slot `build/distill/04_build/J4_assurance_runtime/`): batch.yaml, cross_links.md, result.md. Nothing else touched; scratch graph deleted; nothing committed or pushed.

Sources read, in order: brief_build.md; maintainer_decisions.md (MD-01 to MD-07); resolutions.md (J4 section, flag-1 to flag-7); cross_unit_fixes.md (X2, X5, X11, X13 name J4; X12 supplies the telemetry target); J4 judged.md (already carries the final pass; apply_result.md confirms); skeleton branch.md for ASSURANCE (uids, names, rows); the three ledger parts (merges column); the batch section of the graph-edit skill.

Method: batch.yaml is generated from judged.md by a script (not kept in the slot): design_notes and constraints are extracted from the record's numbered fields, intent and epistemic_state are written by hand. This keeps the transcription faithful and the intent stack-neutral.

Nodes (uid, certainty):
- ASSURANCE.PERFORMANCE: inferred roll-up. .1 Targets and Budgets: known. .2 Load Test Design: known, gap: open-loop rule inferred, fidelity contested and settled by criticality. .3 When Tests Run and Baselines: known. .4 Testing in Production for Performance: known. .5 Measurement Before Optimization: known, gap: transfer of methods inferred, warm-up separation a scope.
- ASSURANCE.AVAILABILITY: inferred roll-up. .1 Tolerating a Degraded Dependency: known, gap: degradation detail inferred. .2 Protecting Remote Calls: known, gap: back-pressure signal handling inferred in part, idempotency mechanism left to the interface. .3 Verifying Resilience Under Real Conditions: known, gap: production-first preference inferred (one source). .4 Proving Restore: known, gap: no cadence number. .5 Exercising Recovery: known, gap: no production-drill frequency, game-day ordering inferred.
- ASSURANCE.ARTIFACT: inferred roll-up. .1 Build Provenance and Match to Source: known, gap: second-level floor grounded for one platform, inferred for others; archive content inferred. .2 Protected Mainline Binds Every Actor: known.

Decisions applied from the sources of truth:
- MD-01, MD-02: cited on every node; MD-03: cited on AVAILABILITY (index to OPERATION.RECOVERY) and ARTIFACT (CHANGE_FLOW and SECURITY operate it).
- Final pass: flag-1 to flag-7 and X5, X11, X13 are already in judged.md; notes name them per node. PERFORMANCE.1 reads "never from current performance as a final value" (X11); PERFORMANCE.4 and AVAILABILITY.3 split the production-test guardrails as X5 sets; AVAILABILITY.3 and .5 point to BEHAVIOUR.5 (X13).
- X12 (split of TELEMETRY.1) adds OPERATION.TELEMETRY.7 as the target of the synthetic-monitoring pointer; it is marked (new) in cross_links.md.
- Maintainer point for J4: none, so no `unvalidated` annotation.

Traceability: impl_pointers per node are the judge record plus original claims through the ledger merges: PERF-C01, C03, C04 to C17, C24, C33 (PERFORMANCE and AVAILABILITY rows), VERIFY-C29, C40, C41, SRC-C32, EXT-C01 to C09, C42, OPERATE-C28b, DATA-C12, RECOV-C01, C20 to C23, C25 to C27, ADOPT-C18, DELIVER-C08, C28, C29, MAINT-C21, AUTH-C22, C29; web claims OPS-C19, OPS-C20 (slot 06_operations) and SEC-C58 (slot 05_identity_security), written `../web_architecture_guidelines/build/research/<slot>/result.md::<ID>`; JavaScript principles RUNTIME, RUNTIME.MEASURE, RUNTIME.METHOD on PERFORMANCE.5, written `../javascript_guidelines/build/handoff/to_software_guideline/package.md::<uid>`. The two JavaScript research claim ids in L1564 and L1565 (RUNTIME-C61 to C63) are not pointed to: the brief maps the JS prefix to package uids only. Roll-up nodes carry the judge pointer alone (no rows attached).

Checks: dry run exactly as the brief gives it (placeholder ASSURANCE node under ROOT added to the scratch copy only, apply with role builder, validate): 23 operations success, 17 nodes, 8 links, 0 errors, 0 warnings. `node show` confirmed constraints, design_notes and epistemic_state persist. scratch.ig.yaml deleted. No absolute or home paths in batch.yaml (grepped); cross_links.md and this file carry none.

Open questions for the linker: which CONSTRUCTION L3 node (if any) holds degraded-mode design; whether `see` is an accepted link type in the final graph or should be `refines` or `requires`.
