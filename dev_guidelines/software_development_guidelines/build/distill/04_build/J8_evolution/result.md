# J8_evolution build result

## L1 headline

The J8_evolution batch is built and passes its dry run: `<root>/build/distill/04_build/J8_evolution/batch.yaml` creates 32 nodes (5 L2, 27 L3, breadth-first) and 22 intra-unit links; 63 cross links are listed for the linker in `cross_links.md`.

- Dry-run check (apply on a scratch copy, then validate): 54 operations succeeded; `validate`: nodes 74, links 38, errors 0, warnings 0. The scratch copy is deleted.
- Certainty: grounded for the transcription of the final judge records; one node (TECHNOLOGY.4) carries an open gap (judge flag F8, awaiting no maintainer answer, no resolution addressed it).
- Stopping point: nothing was applied to the real graph; the coordinator applies this batch after TOP, then the linker adds `cross_links.md`.

## L2 claims

1. **Nodes (grounded).** 32 `node.create` ops: DECISIONS, INCREMENTAL, DEBT, DECOMMISSION, TECHNOLOGY (parent `EVOLUTION`), then their L3 children (6, 6, 5, 6, 4), uids and names unchanged from the skeleton. The L1 record EVOLUTION is skipped (TOP batch).
2. **Sources of truth applied (grounded).** `judged.md` of J8 already carries the final-pass fixes R14 to R26 and X7 and X8 (its "Final pass applied" section lists them); I transcribed it and re-checked each resolution in `resolutions.md` against the node text. MD-01 to MD-05 respected: intents are stack-neutral, product and stack names stay in `design_notes`.
3. **Field mapping (grounded).**
   - `intent` from the record's Decision plus Outcome (the "so that" part), one to three sentences.
   - `constraints` split from the record's Constraints.
   - `epistemic_state` from the record certainty (`known`, `inferred: why`, pipe annotations).
   - `design_notes` is the compressed record: positions with ledger and source ids, forces, grounds, rejected positions with the condition under which each is best, context, certainty, maintainer decisions.
   - `impl_pointers` holds the judge pointer plus each original claim of the attached ledger rows. Slot prefixes used: EVOL 12, MAINT 07, TRANS 06, ADOPT 02, SRC 01; web claims ARCH 07_architecture_styles, OPS 06_operations. All pointed claim ids were found in their result files.
   - `examples`: none (the records give none). `history` not set.
4. **Epistemic states (grounded transcription, certainty as in the record).**
   - `inferred`: DECISIONS.2, DECISIONS.6, DEBT.2, DEBT.3, DEBT.5, TECHNOLOGY.3, TECHNOLOGY.4.
   - `known` with an inferred part named: the other 20 L3 nodes and the five L2 nodes.
   - Open: TECHNOLOGY.4 `| gap:` (contested row on one-project or commercially interested sources, limits of the store not verified from primary sources, flag F8).
   - DECOMMISSION.4 `| gap:` the concrete window durations are one project's and not adopted.
   - No `unvalidated: awaiting maintainer` annotation: J8 has no node awaiting the maintainer. Point 18 of `maintainer_points.md` (INCREMENTAL.6) restates R15, already applied; it is cited in that node's design_notes as a deviation listed for the maintainer.
5. **Intra-unit links (inferred from the judge records' Links lines).** 22 links, all type `see` (the record's links inside the branch are all "see"); the shape type is the link type and the intent sentence says why. Includes pairs both ways where the record points both ways (DECISIONS.4 and DECOMMISSION.2). The skeleton's "Conflicts" link on DEBT.5 became "See" because flag F2 was closed by CHANGE_FLOW.REVIEW.2.
6. **Cross links (inferred).** 63 listed in `cross_links.md`, all from EVOLUTION nodes to OWNERSHIP, ASSURANCE, CHANGE_FLOW, OPERATION and TRANSVERSE nodes (types `realizes` and `see`). Targets were checked to exist as skeleton uids. X7 applied: DECOMMISSION.3 to .5 point to OWNERSHIP.SERVICES.2 as "see"; DECOMMISSION.3 and .4 realize ASSURANCE.CONTRACTS.1. Not listed because the record gives no link: INCREMENTAL.6 to ASSURANCE.CONTRACTS.1 (cited in its grounds only).
7. **Environment fact (grounded).** The real graph already held an `EVOLUTION` node, so no placeholder was needed and the dry run used the real graph's current content as the base.
8. **Open (for the coordinator).** Link uids are auto-generated (`SRC_DST`); a double-pointing pair gives two distinct links. No error, no ambiguity found in the brief.

## L3 full

### Files

- Batch: `build/distill/04_build/J8_evolution/batch.yaml` (paths relative to the guideline folder).
- Cross links: `build/distill/04_build/J8_evolution/cross_links.md`.
- Generator and node data lived in the session scratchpad only; nothing else was written.

### Dry-run, verbatim lines

```
ig-tool apply ... --role builder -m "dry build J8_evolution"   -> status: ok, operations: 54, dry_run: false (on scratch copy)
ig-tool validate -g scratch.ig.yaml  -> status: ok  nodes: 74  links: 38  errors: 0  warnings: 0
```

Operations: 32 `node.create` + 22 `link.create` = 54.

### Node table (uid, certainty, rows)

| uid | epistemic_state lead | ledger rows |
|---|---|---|
| EVOLUTION.DECISIONS | known (roll-up) | none |
| EVOLUTION.INCREMENTAL | known (roll-up) | none |
| EVOLUTION.DEBT | known (roll-up) | none |
| EVOLUTION.DECOMMISSION | known (roll-up) | none |
| EVOLUTION.TECHNOLOGY | known (roll-up) | none |
| DECISIONS.1 Content of a Record | known | L1001 L1002 L1009 L1233 L324 |
| DECISIONS.2 Significance Threshold | inferred | L1004 |
| DECISIONS.3 Form and Storage | known | L1003 |
| DECISIONS.4 Changing an Accepted Record | known | L232 L1005 |
| DECISIONS.5 Status, Ownership and Use in Review | known | L1006 L1007 |
| DECISIONS.6 Proposal Versus Record | inferred | L1008 |
| INCREMENTAL.1 Step Size and Feedback | known | L1010 L1236 |
| INCREMENTAL.2 Expand, Migrate, Contract | known | L1011 L1012 |
| INCREMENTAL.3 Replacement Versus Rewrite | known | L039 L1017 |
| INCREMENTAL.4 Mass Change and Migration Ownership | known | L1013 L1014 |
| INCREMENTAL.5 Lifespan, Consumers and Cost of Change | known | L1015 L1016 |
| INCREMENTAL.6 Conventions Applied Forward Only | known | L296 |
| DEBT.1 What Counts as Debt | known | L1018 L1021 |
| DEBT.2 Taking Debt Versus Investing in Quality | inferred | L1020 L1207 L1237 L1231 |
| DEBT.3 Finding and Inventorying Debt | inferred | L1022 L1023 L1027 |
| DEBT.4 Refactoring Step Size | known | L1024 |
| DEBT.5 Timing and Responsibility of Repayment | inferred | L1019 L1025 L1026 |
| DECOMMISSION.1 Why Remove | known | L1028 L1029 L1041 |
| DECOMMISSION.2 Grounds to Retire | known | L1037 |
| DECOMMISSION.3 Announcing Retirement | known | L1030 L1032 |
| DECOMMISSION.4 Support Window Before Removal | known, gap | L1031 |
| DECOMMISSION.5 Advisory or Compulsory Deprecation | known | L1033 |
| DECOMMISSION.6 Carrying Out the Retirement | known | L1034 L1035 L1036 |
| TECHNOLOGY.1 Adding as Replacing | known | L026 L1038 L1229 |
| TECHNOLOGY.2 Standing Position per Technology | known | L1039 |
| TECHNOLOGY.3 How Firmly the Stack Is Held | inferred | L1040 |
| TECHNOLOGY.4 One General-Purpose Store for Several Roles | inferred, gap F8 | L1232 |

(In the table, bare L3 uids are prefixed `EVOLUTION.`.)

### Intra-unit links (22, type `see`)

DECISIONS.4 to DECOMMISSION.2; DECOMMISSION.2 to DECISIONS.4 and DECISIONS.3; DECISIONS.6 to DECISIONS.1 and DECISIONS.5; INCREMENTAL.2 to DEBT.1; INCREMENTAL.3 to INCREMENTAL.1 and DECOMMISSION; INCREMENTAL.4 to DECOMMISSION.5; INCREMENTAL.6 to DECOMMISSION.3; DEBT.1 to INCREMENTAL.2; DEBT.2 to DEBT.3, DECOMMISSION.1 and INCREMENTAL.1; DEBT.5 to INCREMENTAL.4; DECOMMISSION.5 to INCREMENTAL.4 and DECOMMISSION.3; TECHNOLOGY.1 to TECHNOLOGY.3 and DECOMMISSION.2; TECHNOLOGY.2 to DECISIONS.3; TECHNOLOGY.3 to TECHNOLOGY.1; TECHNOLOGY.4 to TECHNOLOGY.1.

### Transcription decisions worth checking

- DECISIONS.2 follows R14 (combined test); DECISIONS.4 states "a record is superseded, only corrections edit it" and sends living documents to TRANSVERSE.DOCS.
- INCREMENTAL.6 follows R15 (mark in metadata; name only where no consumer breaks); its design_notes cite the maintainer's practice as the base rule that won and name the two refinements as listed for the maintainer.
- DEBT.3 follows R20 and R21 (no undecided paragraph; inventory kept where the team plans its work).
- TECHNOLOGY.3 follows R26, including the consequent constraint edit the judge noted.
- Owner-and-capacity principle lives only in DECOMMISSION.1's decision (R18); INCREMENTAL.2, INCREMENTAL.4, DECOMMISSION.5 and .6 carry "(owner and capacity: DECOMMISSION.1)" in their constraints, DECOMMISSION.1's own constraint carries no suffix.
- In the INCREMENTAL.2 and DECOMMISSION.6 intents the "(owner and capacity)" pointer is in constraints only, to keep intents self-sufficient.
- Public repository rule: no absolute or home paths in `batch.yaml` or `cross_links.md` (checked by search).
