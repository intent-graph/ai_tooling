# Build result: unit J3_assurance_integrity

## L1 headline

The batch for J3 is written and passes the dry check: 19 node.create (3 L2: DATA_INTEGRITY, DOCS_SYNC, SECURITY; 16 L3) and 8 intra-unit link.create, 27 operations, applied to a scratch copy with a placeholder ASSURANCE node under ROOT (grounded: I ran it). Dry-run validate line: `nodes: 21, links: 8, inter_links: 0, issues: 0, errors: 0, warnings: 0`. Cross links listed for the linker: 49 (grounded). No decision is re-judged; two judgement calls are open for the coordinator (L2). Files: `batch.yaml`, `cross_links.md`, `result.md` in `build/distill/04_build/J3_assurance_integrity/`.

## L2 claims

- Nodes: 19, breadth-first (3 L2, then 16 L3 in tree order), uids and names unchanged from the skeleton (grounded: the batch applied and `validate` passed; names carry no forbidden character). The seven L1 nodes, ROOT and ASSURANCE itself are not in this batch (grounded: brief; ASSURANCE is the placeholder in the scratch copy only).
- Intra-unit links: 8 (grounded: from the "Links" lines of the records). They are DATA_INTEGRITY.3 and .5 see each other; DOCS_SYNC.1 requires .2; DOCS_SYNC.2 sees .4; DOCS_SYNC.4 requires .2; SECURITY.3 sees .1 and .4; SECURITY.4 requires SECURITY.2. Link types are carried as `shape: {type: requires|see}` (inferred that the linker accepts these free-text types; the tool accepted them).
- Cross links: 49 rows in `cross_links.md`, each with source uid, target uid, type, one-line intent (grounded: from judged "Links" lines; every target uid exists in the skeleton or is created by J7 at graph build, TELEMETRY.8, X12). Two targets are inferred: the judge writes "TRANSVERSE (privacy and retention)" and "TRANSVERSE (configuration and secrets)"; I used the L2 uids TRANSVERSE.PRIVACY and TRANSVERSE.CONFIG (inferred).
- Faithfulness: verdicts transcribed, not re-judged. Sources applied in order: maintainer decisions (MD-01 to MD-03 cited in every node's design_notes; the documentation ruling quoted in the three DOCS_SYNC-branch nodes), then final-pass resolutions and cross-unit fixes, which the record's "Final pass applied" section already contains (grounded: `apply_result.md` and the section agree; no maintainer point concerns J3, so no `unvalidated` annotation is needed).
- Open item carried: the penetration-test period (SECURITY.3) stays open, written as `| gap:` in its epistemic_state (grounded).
- Judgement call 1: DATA_INTEGRITY.5's Decision held a garbled fragment ("... removed. with an owner (inferred ..."). I repaired the punctuation only (a comma instead of the full stop and lower-case "with"), no wording; the constraint line already says the same (inferred that this is the intended reading).
- Judgement call 2: the brief wants `intent` in one to three sentences, but several decisions run to a paragraph. `intent` holds a 2-3 sentence stack-neutral summary written by me from the Decision and Outcome; the full Decision text sits first in `design_notes` ("Decision (full)"), so nothing is lost (grounded: both fields in the batch).
- Traceability: 97 impl_pointers in total, all resolved to an existing file and claim id (grounded: scripted check, 0 missing). The slot folder is the full research folder name (for example `build/research/03_verification/result.md::VERIFY-C..`), because the folders are `NN_name`, not the bare `NN` of the brief. Web claims use `../web_architecture_guidelines/build/research/14_thin_spots` and `17_data_contracts` (the two web areas present in J3 rows). No JS claim is behind J3.
- Public-repo check: no absolute or home path in the batch (0 matches); no product name in any `intent` (checked for the stack words of the records: none).

## L3 full

### Method

1. Read the brief, the maintainer decisions, `judged.md` (final, with "Final pass applied"), `apply_result.md`, `cross_unit_fixes.md`, the ASSURANCE skeleton branch (rows per node) and the three ledger parts.
2. A script (kept outside the repository, in the session scratch area) parsed each node section of `judged.md` and generated `batch.yaml`; `intent` and `epistemic_state` are hand-written per node, everything else is transcribed.
3. Check, as in the brief: copy of the real graph file to `scratch.ig.yaml` in the slot, `ig-tool node create` for the ASSURANCE placeholder under ROOT, `ig-tool apply --batch ... --role builder`, `ig-tool validate`; the scratch file was deleted afterwards. The real graph file was not touched.

### Field mapping applied

- `name`, `uid`, `parent`: skeleton (L2 under ASSURANCE, L3 under its L2).
- `intent`: my 2-3 sentence summary of Decision and Outcome (see judgement call 2).
- `epistemic_state`: `known` when the record's Certainty is wholly grounded; `known | inferred part: ...` when only a minor part is inferred; `inferred: ...` when the judge calls the form, synthesis or combination inferred or the roll-up has no source as a whole; `| gap: ...` for the open penetration-test period. Per node: DATA_INTEGRITY inferred (roll-up); .1 inferred (split of the middle zone); .2 known | inferred part; .3 inferred (form); .4 known; .5 known | inferred part (owner); DOCS_SYNC inferred (synthesis); .1 known | inferred part; .2 inferred (combination); .3 known; .4 known | inferred part; SECURITY inferred | gap; .1 known | inferred part; .2 inferred (synthesis); .3 inferred | gap; .4, .5 known; .6 known | inferred part; .7 known. (Judgement: where the judge writes "grounded for the core, inferred for X", I chose by whether X is part of the decision itself, .1 .3 .2 .2 and .3 vs minor parts.)
- `constraints`: the record's MUST list, one entry per rule, wording unchanged (inferred marks kept: DATA_INTEGRITY.1 "MUST name constraints (inferred)"). L2 nodes carry none (the records give none).
- `design_notes`: Binding line (MD-01, MD-02, MD-03), the documentation ruling for DOCS_SYNC nodes, then Decision (full), Grounds, Positions considered, Rejected with best-when conditions, Context conditions, Certainty (judge), Flags, Links (as judged). L2 nodes: rolled-up decision, certainty, links. No node is an index node, so none is reduced to a pointer.
- `examples`: none (no record gives concrete examples).
- `impl_pointers`: the judge record `build/distill/03_judge/J3_assurance_integrity/judged.md::<UID>`, then one pointer per original claim behind the node's attached ledger rows (skeleton "Rows", ledger `merges` column; maintainer claims `MAINT-C..` point to `07_maintainer_doctrine`). L2 nodes have no attached rows: judge record only.
- `history`: not set.

### Pointers per node (judge record plus claims)

DATA_INTEGRITY 1 (roll-up); .1 4; .2 4; .3 7; .4 4; .5 5; DOCS_SYNC 1; .1 5; .2 8; .3 7; .4 6; SECURITY 1; .1 6; .2 5; .3 9; .4 4; .5 4; .6 12; .7 4 (counts include the judge pointer; total 97).

### Links

Intra-unit (in the batch): see "L2 claims". Cross-unit: `cross_links.md`, 49 rows; groups: DATA_INTEGRITY 15, DOCS_SYNC 11, SECURITY 23. Links to J2 and J4 nodes (RULES.1 to .5, BEHAVIOUR.2, .3, .6, .8, CONTRACTS.3, AVAILABILITY.4, ARTIFACT, ARTIFACT.2) state only what J3 needs from them (the J2 and J4 verdicts were not yet written when J3 was judged).

### Observations, not changed

- The header of `judged.md` still says the J2 and J4 verdicts are "not yet written" (stale, noted by the apply step); irrelevant to the batch.
- DATA_INTEGRITY.3 mentions "TRANSVERSE.PRIVACY.2/.3" and "OPERATION.RECOVERY.2" as text pointers inside the Decision (cross-unit fix X8); they depend on those nodes existing after the J7 and J9 batches, which the linker should confirm.
- SECURITY.5's constraint refers to the waiver of SECURITY.2 in words; no intra-unit link is created for it because the record's Links line has none.

### Pinned lines

- Nodes in batch: 19 (3 L2, 16 L3).
- Intra-unit links: 8.
- Cross links listed: 49.
- Dry-run apply: status success, operations 27.
- Dry-run validate: `nodes: 21 / links: 8 / inter_links: 0 / errors: 0 / warnings: 0`.
