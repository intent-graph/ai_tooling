# J6_change_flow build result

## L1 headline

The batch for J6_change_flow is written and passes the dry-run check with 0 errors and 0 warnings. Each claim is marked grounded, inferred or open.

- Nodes in the batch: 42 `node.create` (8 L2: INTEGRATION, REVIEW, BUILD, RELEASE, DEPLOY, ROLLBACK, DATA_CHANGE, MEASURE; 34 L3), breadth-first, each L2 under `CHANGE_FLOW` and each L3 under its L2 (grounded: counted in the file and by the tool).
- Intra-unit links: 28 `link.create`, all type `related`, one per node pair (grounded).
- Cross links listed in `cross_links.md`: 48 (13 `realizes`, 35 `related`), not in the batch (grounded: counted).
- Dry-run validate line: `ig-tool validate`: nodes 154, links 90, errors 0, warnings 0; the apply reported 70 operations, all success (grounded: I ran it on a copy of the real graph, deleted afterwards).
- Open: the link type `related` is the judge and skeleton vocabulary; the tool accepted it, but no existing graph uses it (the web graph uses only realizes, requires, refines, conflicts, constrains, dataflow), and one cross-unit note (X7) says "see" for the same relation; the coordinator decides the final type word.
- Files: `batch.yaml`, `cross_links.md`, `result.md` in the slot folder.

## L2 claims

1. Sources applied (grounded). Order followed: maintainer decisions, final-pass resolutions and cross-unit fixes, the judge record `judged.md` (already carrying "Review applied" and "Final pass applied"), the skeleton branch, the three ledger parts. The J6 section of the final pass has no point marked for the maintainer, so no `unvalidated: awaiting maintainer` annotation was needed. Cross-unit X6 and X14 were already applied in the record; X1 to X5 and X7 to X13 name no J6 node.
2. Field mapping (grounded, faithful transcription; the intent is mine, see claim 3).
   - `name` and uid: the skeleton, unchanged (names checked against the judge record headers).
   - `epistemic_state`: from the record's Certainty. L3 nodes read `known | inferred: ...` or `known | gap: ...` or `inferred: ...`; L2 roll-ups read `inferred: roll-up ...`. No node is `undecided` (the record states none).
   - `constraints`: the record's MUST lines, one per entry (L2 roll-ups carry none).
   - `design_notes`: decision (full judge text), grounds with ledger and register ids, positions, each rejected position with its winning condition, context conditions, certainty, maintainer decisions cited (MD-01 everywhere, MD-02 or MD-03 where the node's subject is author neutrality or the procedure/guarantee split), final-pass notes (FL1 to FL4, FL6 to FL9, F5, F10, X6, X14), and the record's links and stack-pointer line.
   - `examples`: 5 nodes only, where the record gives concrete figures or an instance (INTEGRATION.2, REVIEW.2, DEPLOY.2, DATA_CHANGE.7, DATA_CHANGE.8).
   - `impl_pointers`: the judge record plus one pointer per original research claim behind the node's attached ledger rows, slot by claim prefix; web claims point into the web guideline's research slots (OPS 06, ARCH 07, SEC 05, THIN 14, DCON 17). No JavaScript-guideline principle is attached to a J6 row.
3. Intent is condensed by me (inferred): one to three sentences per node, stack-neutral (no product, tool or language names; "Conventional Commits", "Semantic Versioning", the research programme and tool names stay in `design_notes`). The full decision text is kept in `design_notes`, so nothing of the judge record is lost, but the one-to-three-sentence statements are my roll-up of it.
4. Links (grounded for existence, inferred for the choice of one direction per pair).
   - Intra-unit: taken from the judge record's Links lines, one per unordered pair (several pairs are stated from both sides). The three skeleton `Conflicts` (DEPLOY.1 and DEPLOY.3 against DATA_CHANGE.3, ROLLBACK.1 against ROLLBACK.3) are not links: the judge record resolves each (a gate inside one pipeline, undo decided per class) and says "conflicts none".
   - Cross: the eight L2 `realizes` links to the ASSURANCE nodes the record names, plus related pointers (SECURITY.6, RULES.4 and RULES.5, ARTIFACT.1 and ARTIFACT.2, CONTRACTS.1, OWNERSHIP.LIFECYCLE, TRANSVERSE.CONFIG, ENVIRONMENTS and PRIVACY, OPERATION.TELEMETRY, INCIDENTS, RUNBOOKS, RELIABILITY and FEEDBACK, EVOLUTION.DECOMMISSION, CONSTRUCTION.HIDING). Targets are not checked for existence in this build (the dry run was on the real graph's current state, and no cross link is in the batch).
5. Check (grounded). The real graph already holds `CHANGE_FLOW` and 111 other nodes (other units, applied), so the brief's placeholder step was unnecessary and skipped (`node create` failed with "already exists"). The batch applied to the copy of the whole current graph: 70 operations, status ok; validate: errors 0, warnings 0. `scratch.ig.yaml` deleted. The real graph, judge records, skeleton and ledger are untouched; nothing committed or pushed.
6. Public-repository rule (grounded): `grep` for absolute or home paths in the written files finds none; all pointers are relative to the guideline folder.
7. Open points for the coordinator.
   - Link type word `related` (see L1).
   - `OPERATION.TELEMETRY` is the target the record names for DATA_CHANGE.8; after cross-unit X12 the linker may prefer `OPERATION.TELEMETRY.1`.
   - ROLLBACK.3 and DEPLOY.3 notes mention settled-against-the-maintainer items; they are recorded in `design_notes`, not in `epistemic_state` (the final pass lists them, not marks them unvalidated).

## L3 full

### Run

- Generator: a script written for this build (kept in the session scratchpad, not in the repository); it parses `judged.md` and the skeleton `branch.md`, reads `merges` from the three ledger parts, and writes the batch with the intents and `epistemic_state` strings I wrote by hand. Re-running it reproduces `batch.yaml` and `cross_links.md`.
- Check commands (as in the brief): copy of `intent_graphs/software_development_philosophy.ig.yaml`, `ig-tool apply --batch ... --role builder -m "dry build J6_change_flow"`, `ig-tool validate`. Results: apply `operations: 70`, `status: ok`; validate `nodes: 154`, `links: 90`, `errors: 0`, `warnings: 0`.

### Nodes in the batch (42)

L2: CHANGE_FLOW.INTEGRATION, .REVIEW, .BUILD, .RELEASE, .DEPLOY, .ROLLBACK, .DATA_CHANGE, .MEASURE.

L3 (34): INTEGRATION.1 to .6; REVIEW.1 to .4; BUILD.1, .2; RELEASE.1 to .5; DEPLOY.1 to .4; ROLLBACK.1 to .3; DATA_CHANGE.1 to .8; MEASURE.1, .2.

Certainty per node (epistemic_state lead), as in the batch:
- inferred (roll-ups, 8): INTEGRATION, REVIEW, BUILD, RELEASE, DEPLOY, ROLLBACK, DATA_CHANGE, MEASURE.
- inferred (L3, 2): RELEASE.5 (one practitioner source plus the respond-to-failure argument), DATA_CHANGE.8 (maintainer practice, single source; gap on public counterparts L412, L413).
- known with an inferred part (L3, 28): INTEGRATION.1 to .6, REVIEW.1 to .4, BUILD.2, RELEASE.1 to .4, DEPLOY.1 to .3, ROLLBACK.1, .3, DATA_CHANGE.1 to .7, MEASURE.2.
- with an open part (gap), 8 nodes: INTEGRATION.1 (layout winner), INTEGRATION.4 (merge-method winner), REVIEW.4 (no study on second automated reviewer), RELEASE.2 (calendar versioning not read), DEPLOY.4 (pull versus push, known with only a gap), DATA_CHANGE.3 (configuration-like content, L411), DATA_CHANGE.8 (L412, L413), MEASURE.1 (net effect of automation contested, known with only a gap).
- known without annotation: BUILD.1, ROLLBACK.2.
- undecided: none.

### Intra-unit links (28, type related; source to target)

INTEGRATION.2 to RELEASE.3; INTEGRATION.3 to RELEASE.1, ROLLBACK.1; INTEGRATION.4 to INTEGRATION.5; INTEGRATION.5 to REVIEW.2, ROLLBACK.2; INTEGRATION.6 to REVIEW.1; REVIEW.1 to DATA_CHANGE.3, DATA_CHANGE.8; REVIEW.4 to BUILD.1; BUILD.2 to RELEASE.2; RELEASE.1 to MEASURE.1; RELEASE.4 to DATA_CHANGE.3, DEPLOY.1; DEPLOY.1 to DATA_CHANGE.1, DATA_CHANGE.3; DEPLOY.2 to ROLLBACK.1; DEPLOY.3 to DATA_CHANGE.3, DATA_CHANGE.7; ROLLBACK.2 to DATA_CHANGE.4; ROLLBACK.3 to DATA_CHANGE.4; DATA_CHANGE.1 to DATA_CHANGE.2; DATA_CHANGE.5 to DATA_CHANGE.6; DATA_CHANGE.6 to DATA_CHANGE.8; DATA_CHANGE.7 to DATA_CHANGE.3; DATA_CHANGE.8 to DATA_CHANGE.3; MEASURE.2 to MEASURE.1, RELEASE.1. (Link uids are tool-generated as `SRC_DST`.)

### Cross links

48 rows in `cross_links.md` (13 realizes: the eight L2 nodes, ROLLBACK.3, DATA_CHANGE.3 and .4, BUILD.2, DEPLOY.2 to the ASSURANCE nodes the record names; 35 related). Targets outside the unit: ASSURANCE (RULES and .2, .4, .5; ARTIFACT, .1, .2; BEHAVIOUR.1, .7, .8; SECURITY.6; CONTRACTS and .1; AVAILABILITY and .3; DATA_INTEGRITY, .2, .3), OWNERSHIP.LIFECYCLE, TRANSVERSE (CONFIG, ENVIRONMENTS, PRIVACY), OPERATION (INCIDENTS, RUNBOOKS, TELEMETRY, RELIABILITY, FEEDBACK), EVOLUTION.DECOMMISSION, CONSTRUCTION.HIDING.

### Judgement calls

- Skeleton `Conflicts` links dropped (see L2 claim 4); judge record overrides the skeleton.
- Decision text is not in `intent` (too long for one to three sentences, for example DATA_CHANGE.8); it is in `design_notes` under "Decision (judge record, final)".
- `epistemic_state` writes inferred parts as pipe annotations on `known` where the lead decision is grounded; the roll-up and the two fully maintainer-based or single-source nodes lead with `inferred:`.
- Placeholder `CHANGE_FLOW` node not added: it already exists in the real graph.
