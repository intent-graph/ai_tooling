# Build result: unit J9_transverse

## L1 headline

Batch for unit J9_transverse is written and passes the dry run with 0 errors and 0 warnings; nothing needed the maintainer.
- Pin, nodes in the batch: 35 `node.create` (6 L2 roll-ups, 29 L3), breadth-first, parent of each L2 is `TRANSVERSE` (the L1 node is not in this batch).
- Pin, intra-unit links: 25 `link.create` (all type see), both endpoints inside the unit.
- Pin, cross links listed: 55 rows in `cross_links.md` (9 realizes, 4 requires, 42 see); 2 of them start at the L1 node TRANSVERSE, whose record belongs to the TOP batch.
- Pin, dry-run validate line: `status: ok; command: validate; nodes: 43; links: 25; errors: 0; warnings: 0` (43 = ROOT, 7 L1, 35 of this unit; the apply reported 60 operations, all success).
- Claims: batch faithfulness to the final judge records grounded; link vocabulary and the added pointers inferred; nothing open (no node carries an awaiting-maintainer annotation).
- Files: `build/distill/04_build/J9_transverse/batch.yaml`, `cross_links.md`, `result.md`.

## L2 claims

Each claim carries its certainty.

1. Source order was respected (grounded). Maintainer decisions MD-01 to MD-07 first, then the J9 section of the final-pass resolutions and the cross-unit fixes (X8, X9, X10), then `judged.md` (which already holds the "Review applied" and "Final pass applied" texts), then the skeleton branch, then the three ledger parts. No verdict was re-judged. Checked: names equal the skeleton names for all 36 uids (script assertion).
2. Field mapping (grounded):
   - `name` is the skeleton name.
   - `intent` is a hand-written one-to-three-sentence compression of the judge's Decision, with no product or tool names (framework, tool and standard names stay in `design_notes`).
   - `epistemic_state` follows the record's certainty (`known`, `inferred: ...`, pipe annotations `| inferred:`/`| gap:`).
   - `constraints` are the judge's MUST rules, one per entry.
   - `design_notes` carries the judge's Decision, Grounds, Positions, Rejected (with the condition under which each would be best), Context and Certainty verbatim, plus a line for maintainer decisions, review items and final-pass items.
   - `examples` is omitted (the records give no concrete examples as such).
   - `history` is not set.
3. Index nodes (grounded, MD-03): `TRANSVERSE.DOCS` and `TRANSVERSE.SECURITY` carry only the pointer in `design_notes`. The four other L2 nodes carry the judge's roll-up record and certainty.
4. Maintainer-codified rows decided against in part are recorded as such in `design_notes` (grounded): DOCS.2 (L321, hand-kept line-number tables of contents) and DOCS.3 (L318, dated header change log). Both are settled in the final pass, listed for the maintainer's objection, none awaits an answer; so no `| unvalidated: awaiting maintainer` annotation was needed in this unit.
5. Final-pass and cross-unit texts are applied (grounded): T1 (DOCS.3 unchanged), T5 (MON.1 grounded), T6/X8 (PRIVACY.2 backup copies included, PRIVACY.3 erasure in backups), T7/X9 (CONFIG.1 token-acceptance clause removed, see-link to CONSTRUCTION.BOUNDARY.2), T8 (CONFIG.2 channel text), X10 (CONFIG.6 link to OWNERSHIP.LIFECYCLE.3), F11, F12, F13. These were already in `judged.md`; I checked its own "Final pass applied" list against the resolutions.
6. `impl_pointers` (grounded for the pattern, inferred for two choices): each L3 node has the judge pointer plus one pointer per original claim behind its ledger rows, slot from the claim prefix as in the brief; web claims point into the web guideline research slot (OPS 06_operations, SEC 05_identity_security, THIN 14_thin_spots, read from the ledger part 2 section headings); JS principle `DEFENSE.SECRETS` points to the handoff package. Inferred: CONFIG.1 also points to two JavaScript research claims (`RUNSEC-C46`, `SECGAP2-C03`) at `../javascript_guidelines/build/research/06_runsec` and `14_secgap2`, which the brief's slot list does not cover; both targets exist. L2 nodes carry the judge pointer only (no attached rows). The `JS:` and `MAINT-` pointers were not resolved for existence by the tool (the validator does not check paths); I checked the three web ids and the two JS ids with grep.
7. Links (inferred): the judge record's verbs became `shape.type` values `realizes`, `requires`, `see`; the graph tool accepted them (no vocabulary is documented, the primer lists none). Each link intent names the two nodes and carries the judge's parenthetical reason or a short reason I wrote from the Links line. Direction: "Realized by OPERATION and CHANGE_FLOW.DEPLOY" on CONFIG.2 is listed as two cross links from those nodes to CONFIG.2.
8. Dry run (grounded, ran it): scratch copy of the real graph, apply of the batch (status ok, 60 operations), validate 0 errors 0 warnings. The placeholder node step of the brief failed with "Node 'TRANSVERSE' already exists": the real graph already holds ROOT and the seven L1 nodes (8 nodes before this batch), so the check ran against the real L1 skeleton, which is stricter than a placeholder. Scratch file deleted.
9. Open: none for the batch. Open evidence gaps of the judge records stay at their nodes in `epistemic_state` (DOCS.4, SECURITY.1, SECURITY.2, SECURITY.6, MON.4, PRIVACY.2, PRIVACY.3, PRIVACY.4, CONFIG.1).

## L3 full

### Pinned facts

- Batch: `build/distill/04_build/J9_transverse/batch.yaml`, `operations:` list; first the 35 `node.create`, then the 25 `link.create`.
- Node order: L2 in tree order (DOCS, SECURITY, SECURITY_MONITORING, PRIVACY, CONFIG, ENVIRONMENTS), then each L2's children by number. Counts: DOCS 5, SECURITY 6, SECURITY_MONITORING 5, PRIVACY 4, CONFIG 6, ENVIRONMENTS 3 (29 L3).
- Dry-run commands as in the brief; apply output: `status: ok`, `command: batch`, `operations: 60`, `dry_run: false` (written to the scratch copy only); validate output: `graph: ...scratch.ig.yaml; nodes: 43; links: 25; inter_links: 0; issues: 0; errors: 0; warnings: 0`.
- Cross links: `cross_links.md`, columns source, target, type, intent. Type counts: realizes 9, requires 4, see 42. Sources outside the unit that point in: none listed (other units' records point to J9 and are theirs to list, for example X8, X10).

### Intra-unit links (25, all see)

- SECURITY.1 to SECURITY.2; SECURITY.2 to SECURITY.1 and to SECURITY_MONITORING.4; SECURITY.5 to SECURITY.6; SECURITY.6 to SECURITY.5.
- SECURITY_MONITORING.3 to PRIVACY.1 and PRIVACY.2; SECURITY_MONITORING.5 to PRIVACY.3.
- PRIVACY.1 to SECURITY_MONITORING.3 and PRIVACY.2; PRIVACY.2 to PRIVACY.1, PRIVACY.3, CONFIG.4; PRIVACY.3 to PRIVACY.2 and SECURITY_MONITORING.5; PRIVACY.4 to SECURITY_MONITORING.2 and PRIVACY.1.
- CONFIG.1 to CONFIG.4; CONFIG.2 to CONFIG.1 and CONFIG.4; CONFIG.4 to SECURITY_MONITORING.2 and PRIVACY.2; CONFIG.5 to CONFIG.4; CONFIG.6 to CONFIG.4 and SECURITY.5.
- Every `TRANSVERSE.` target named on a judge `Links:` line is present; two parenthetical mentions on L2 Links lines (ASSURANCE.SECURITY.7 on SECURITY_MONITORING, ASSURANCE.SECURITY.5 on CONFIG) are covered by the realizes link to ASSURANCE.SECURITY and appear as the reason, not as separate links.

### Choices worth a second look

- Intent text is my compression; the full decision is in `design_notes` unchanged, so a reader can compare.
- `epistemic_state` uses `known | inferred: ...` for nodes the judge marks grounded with inferred parts, and plain `inferred: ...` for roll-ups and for MON.5 and PRIVACY.3, where the judge marks the core decision itself inferred.
- DOCS.5 flags line ("inferred parts noted") and all "Flags: none" lines are not copied; no flag remains open per the judge.
- `design_notes` for CONFIG.1 keeps the line that the earlier JavaScript-guideline verdict on L1535 was re-examined and confirmed only for the two grounded constraints.
- Not in the batch by design: the L1 node TRANSVERSE and the ROOT update (TOP batch); links to nodes in other units (cross_links.md).
