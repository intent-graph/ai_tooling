# J5_construction: graph batch

## L1 headline

J5_construction batch built and dry-run checked: 47 nodes (10 L2, 37 L3), 39 intra-unit links, 61 cross links listed for the linker; validate on the dry-run copy: 0 errors, 0 warnings (grounded: ran it).

Pinned:
- Nodes in the batch: 47 `node.create` (breadth-first: 10 L2 under CONSTRUCTION, then 37 L3). The L1 record CONSTRUCTION is skipped (TOP batch).
- Intra-unit links: 39 `link.create`.
- Cross links listed: 61 rows in `cross_links.md` (6 of them from the L1 node CONSTRUCTION, built by TOP).
- Dry-run validate line: `nodes: 89, links: 55, errors: 0, warnings: 0` (apply: 86 operations, status ok).

Files: batch.yaml, cross_links.md, result.md in this folder.

## L2 claims

Pinned: 47 nodes; 39 intra links; 61 cross links; validate 0 errors, 0 warnings.

- Source of the content: the final judge records `03_judge/J5_construction/judged.md` as they stand after review and final pass (R17 to R25, X7, X9, X12 already applied there); nothing re-judged. (grounded: read in full)
- Overrides: MD-01 to MD-07 and `cross_unit_fixes.md` read; no J5 point is marked for the maintainer, so no `unvalidated` annotation is set. X9 (token acceptance) is carried by BOUNDARY.2 and X12 by PARADIGM.2 (link to OPERATION.TELEMETRY.8, listed in cross_links). (grounded)
- Field mapping: `name` and `parent` from the skeleton; `intent` hand-written (1 to 3 sentences, stack-neutral, self-sufficient); `epistemic_state` from the record's certainty (`known | gap: ...` where a grounded decision has inferred or open parts, `inferred: <why>` where the decision itself is inferred, none undecided); `constraints` = the record's MUST lines (45 entries on 36 L3 nodes, none on L2); `design_notes` = the full Decision text plus Grounds, Positions, Rejected, Context, Certainty, Note and ledger rows; `impl_pointers` = judge record plus one per original claim of the attached ledger rows (134 pointers in all, every file and anchor checked to exist). (grounded)
- Judgment calls (inferred): (a) `examples` left unset, the records give no labelled examples; (b) no node is an index node under MD-03, so all carry full design_notes; (c) JS-origin rows point to the package node uid only, not to the JavaScript research claim ids; (d) link `shape.type` uses the record's own verbs (`related`, `requires`, `refines`, `realizes`), accepted by validate; symmetric "related" pairs are stored once, in the first direction, and NAMING to BOUNDARY.5 "related" is dropped because BOUNDARY.5 refines NAMING.
- Environment finding (grounded): the real graph already held CONSTRUCTION and 42 other nodes when I ran the check (other batches applied), so the placeholder step of the brief was unnecessary: `node create CONSTRUCTION` failed with "already exists", the batch applied cleanly on the copy anyway. The scratch copy was deleted.
- Open: nothing blocking. The linker must apply cross links only after the other units' batches exist (targets in ASSURANCE, OWNERSHIP, OPERATION, CHANGE_FLOW, EVOLUTION, TRANSVERSE).

## L3 full

### Tree built (uids unchanged from the skeleton)
- DESIGN: .1 Derivation Order, .2 Effort and Timing on Costly Decisions, .3 Properties First Then Constraints, .4 Growth Horizon
- SYSTEM_SHAPE: .1 to .4; HIDING: .1 to .4; BOUNDARY: .1 to .6; STATE: .1 to .5; DEPENDENCY_DIRECTION: .1, .2; NAMING: .1 to .3; PARADIGM: .1, .2; DATA_NOT_CODE: .1 to .4; PROCESS: .1 to .3.

### Certainty per node (grounded / inferred / open, as set in epistemic_state)
- inferred (decision itself): DESIGN, DESIGN.1, DESIGN.4, SYSTEM_SHAPE, HIDING, HIDING.2, BOUNDARY.4, BOUNDARY.5, STATE, STATE.5, DEPENDENCY_DIRECTION and .1, .2, NAMING, NAMING.2, NAMING.3, PARADIGM and .1, .2, DATA_NOT_CODE (roll-up of grounded children), PROCESS, PROCESS.2: 22 nodes.
- known with a stated gap (22 nodes): DESIGN.2, DESIGN.3, SYSTEM_SHAPE.1 to .4, HIDING.1, .3, BOUNDARY, .2, .3, .6, STATE.1 to .4, NAMING.1, DATA_NOT_CODE.1, .3, .4, PROCESS.1, .3.
- known without gap (3 nodes): HIDING.4, BOUNDARY.1, DATA_NOT_CODE.2.
- open: STATE.4 (preference between immutability and restriction), BOUNDARY.3 (checklist reading of the data-engineering contract format), DATA_NOT_CODE.3 (the no-race clause); each carried inside a `gap:` annotation.
- Undecided nodes: none. `unvalidated` annotations: none (no J5 point awaits the maintainer).

### Intra-unit links (39)
Types: related (33), requires (3: PARADIGM.1 to HIDING.1, DATA_NOT_CODE to BOUNDARY.1, DATA_NOT_CODE.4 to DATA_NOT_CODE.1), refines (3: DATA_NOT_CODE to BOUNDARY.2, BOUNDARY.5 to NAMING, STATE.5 to DEPENDENCY_DIRECTION.1). Full list at the end of `batch.yaml` (operations of kind `link.create`), each with its intent sentence.

### Cross links
`cross_links.md`: source uid, target uid, type, intent. Targets outside the unit: ASSURANCE.CONTRACTS(.1,.2,.3), ASSURANCE.DATA_INTEGRITY.1 and .4, ASSURANCE.RULES.3, ASSURANCE.SECURITY(.2,.6), ASSURANCE.BEHAVIOUR.7, OWNERSHIP.STANCE(.4), OWNERSHIP.CONTAINMENT(.2,.4), OWNERSHIP.SERVICES.2, OWNERSHIP.SELECTION.2, EVOLUTION.INCREMENTAL, EVOLUTION.DECOMMISSION, OPERATION.CAPACITY, OPERATION.RELIABILITY, OPERATION.INCIDENTS, OPERATION.TELEMETRY.8 (cross-unit fix X12, created by J7), CHANGE_FLOW.DEPLOY, TRANSVERSE.SECURITY, TRANSVERSE.CONFIG, TRANSVERSE.DOCS. The row L196 (semantic conventions, another branch) named in the NAMING record has no node uid and is not listed.

### Check run
- `ig-tool apply --batch` on a copy of the real graph file: 86 operations, status ok.
- `ig-tool validate`: nodes 89, links 55, errors 0, warnings 0 (the copy already held 42 nodes and 16 links from other batches).
- Scratch copy deleted. No real file touched; no commit.
