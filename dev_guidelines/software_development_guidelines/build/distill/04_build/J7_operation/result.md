# Result: build of unit J7_operation

## L1 headline

- Built `batch.yaml` for unit J7_operation: 40 `node.create` (9 L2, 31 L3, breadth-first, TELEMETRY.7 and .8 included) and 26 intra-unit `link.create`. The L1 node OPERATION is not in it (TOP batch). Grounded: counts read from the file.
- Dry run (clean copy: ROOT plus an OPERATION placeholder, then the batch): `validate`: nodes 42, links 26, errors 0, warnings 0. Same batch on a copy of the current real graph (which already holds OPERATION and other branches): nodes 82, links 42, errors 0, warnings 0. Grounded: I ran both.
- 49 cross links (other endpoint outside the unit) are listed in `cross_links.md` for the linker. Open for the linker: whether each target uid exists in its own batch.
- One name departs from the skeleton: TELEMETRY.1 is "What Is Measured: Service and Resource Signals" (the judge record's name after the X12 split). Inferred: the final pass overrides the skeleton name; a coordinator who wants the skeleton name must rename it.

## L2 claims

Files (all in this slot): `batch.yaml`, `cross_links.md`, `result.md`. Scratch graph deleted.

Nodes (grounded: counted and validated)
- 9 L2: RELIABILITY, ALERTING, TELEMETRY, INCIDENTS, CAPACITY, READINESS, RUNBOOKS, RECOVERY, FEEDBACK (FEEDBACK is a leaf L2).
- 31 L3: RELIABILITY.1-4, ALERTING.1-2, TELEMETRY.1-8, INCIDENTS.1-3, CAPACITY.1-3, READINESS.1-3, RUNBOOKS.1-2, RECOVERY.1-6.
- Row split for X12 (grounded): TELEMETRY.1 keeps L190, L191, L192, L1172, L1180, L1177; TELEMETRY.7 takes L189, L1176, L453, L454; TELEMETRY.8 takes L313.

Field mapping (grounded: by construction)
- `design_notes` of each node is the judge record's grounds, positions, rejected (with the best-when conditions), context, certainty and links lines, copied from `judged.md` (final: it already holds the "Review applied" and "Final pass applied" changes), plus a "Maintainer decisions" line where the record cites MD-01, MD-02, MD-03 or X8, X11, X12.
- `intent` is a one-to-three-sentence stack-neutral restatement of the record's Decision; tool and standard names moved to `design_notes` and `examples`. Inferred: my compression keeps the decision; every MUST is kept verbatim in `constraints`.
- `epistemic_state`: `known` for grounded records; `inferred: ...` for the nine roll-ups and READINESS.2; pipe annotations `| inferred:` and `| gap:` for open parts. No node is `undecided`. No `unvalidated` annotation: the one maintainer point (ASSURANCE.RULES.4) is J2's, and `maintainer_points.md` names no J7 node.
- `impl_pointers`: the judge record plus every original claim behind the node's rows (36 pointers to slot 05, 26 to slot 11, 30 to slot 14, 2 to slot 07, 1 to slot 15, 17 web claims), resolved through the three ledgers' `merges` column. L2 nodes carry the judge pointer only.
- Final-pass edits R-08 to R-18 and X8, X11, X12 are already in the judge record and appear in the batch (for example the immutable-retention alternative in RECOVERY.3, the fallback rule in RECOVERY.4, the SHOULD in TELEMETRY.6).

Links
- Intra-unit (26, grounded in the records' Links lines): requires chain RELIABILITY.1 <- .2 <- .3 <- .4; ALERTING.2 requires RELIABILITY.2 and .3; RECOVERY.4 requires RECOVERY.1; RECOVERY.6 requires TELEMETRY.8; RELIABILITY.3 refines INCIDENTS.2 and INCIDENTS.2 requires RELIABILITY.3; the rest are `related`. Link type goes in `shape.type`; direction: the source depends on or relates to the target.
- Cross (49, in `cross_links.md`): includes the X8, X11 and X12 pointers owned by J3, J4, J5 and J8 (DATA_INTEGRITY.4 and PARADIGM.2 to TELEMETRY.8; PERFORMANCE.1 to RELIABILITY.1 and .2; DATA_INTEGRITY.3 and DECOMMISSION.6 to RECOVERY.2).

Points for the coordinator
- Inferred: RELIABILITY.1's record says it is "required by ALERTING.2", but ALERTING.2's own Links line names only RELIABILITY.2 and .3. I followed ALERTING.2's line (no direct link); the indicator is reached through RELIABILITY.2.
- Inferred: both "RELIABILITY.3 refines INCIDENTS.2" and "INCIDENTS.2 requires RELIABILITY.3" are stated in the records; both kept (two directed links, no validator complaint).
- Not applied (not in my slot, listed in `cross_links.md`): the pointer edits inside J3, J4, J5 and J8 nodes.
- Open: the L1 node OPERATION and its two `realizes` links belong to the TOP batch.

## L3 full

Procedure (grounded: I ran it)
1. Read `brief_build.md`, `maintainer_decisions.md`, `cross_unit_fixes.md`, the J7 section of `final_pass/resolutions.md`, the whole `judged.md` of J7, the skeleton `OPERATION/branch.md`, the batch section of the graph-edit skill, and the ledger `merges` columns.
2. Generated the batch with a script kept outside the repository (scratchpad): parses `judged.md` per uid for design notes, takes rows from the skeleton (with the X12 split), resolves claims through the ledgers, dumps YAML.
3. Dry run, clean copy: `ig-tool init --root`, placeholder `node create` for OPERATION under ROOT, then `ig-tool apply --batch ... --role builder -m "dry build J7_operation"` (66 operations, status success), then `ig-tool validate`: `nodes: 42, links: 26, errors: 0, warnings: 0`.
4. Dry run, copy of the current real graph: it already held OPERATION (placeholder create refused: "already exists"), the batch applied (66 operations), `validate`: `nodes: 82, links: 42, errors: 0, warnings: 0`.
5. Deleted both scratch graphs; no real file touched.

Pinned lines
- Nodes in the batch: 40. Intra-unit links: 26. Cross links listed: 49.
- Dry-run validate: `errors: 0, warnings: 0` (clean copy: 42 nodes, 26 links).

Per-node certainty carried (state field), by node
- known: RELIABILITY.1, .2, ALERTING.1, TELEMETRY.8, READINESS.1, RUNBOOKS.1.
- known with annotation: RELIABILITY.3 (gap: no-budget view unsourced), RELIABILITY.4 (gap: culture condition), ALERTING.2 (gap: single authority; inferred: imminent-failure reconciliation), TELEMETRY.1 to .7, INCIDENTS.1 to .3, CAPACITY.1 to .3, READINESS.3, RUNBOOKS.2, RECOVERY.1 to .6, FEEDBACK.
- inferred: the nine roll-ups other than FEEDBACK (eight) and READINESS.2 (no effectiveness evidence for independent versus self-service review).
- open parts kept visible: TELEMETRY.6 (no normative source for a governed telemetry budget), RECOVERY.5 (hardening default rests on one T3 source; opposite side unsourced), CAPACITY.2 (no numeric headroom), READINESS.3 (no cadence), RUNBOOKS.2 (cost of automating a wrong runbook), FEEDBACK (contrary view unsourced).

Rules check (grounded)
- Names contain none of the forbidden characters. No absolute or home paths in any file (grep count 0). No product or tool name in any `intent` (grep for common names returned nothing); product names appear in `design_notes` and `examples` only.
- Real graph, judge records, skeleton and ledger untouched; nothing committed or pushed.
