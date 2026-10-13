# J1_ownership: graph batch

## L1 headline

`batch.yaml` creates the 35 nodes of unit J1_ownership (6 L2, 29 L3, breadth-first, parent `OWNERSHIP` for the L2) and 21 intra-unit links; 11 cross links are listed in `cross_links.md`. Dry run on a copy of the graph: `ig-tool apply` 56 operations, all success; `ig-tool validate`: nodes 43, links 21, errors 0, warnings 0, status ok.

## L2 claims

- Nodes in the batch (grounded, counted in the batch file): 35 `node.create` (6 L2: STANCE, SELECTION, LIFECYCLE, CONTAINMENT, SERVICES, LICENCE; 29 L3: STANCE 4, SELECTION 6, LIFECYCLE 5, CONTAINMENT 4, SERVICES 6, LICENCE 4). No L1 node: `OWNERSHIP` already exists in the real graph (built by the TOP batch), so no placeholder was added to the scratch copy.
- Intra-unit links: 21 `link.create`, all type related (grounded: the skeleton Links lines plus the judge records' Links lines, listed in L3).
- Cross links: 11 outbound or two-way links plus 2 inbound lines from X7, in `cross_links.md` (grounded: each follows a judge Links line or a cross-unit line).
- Dry-run validate line: `nodes: 43, links: 21, errors: 0, warnings: 0` (grounded: I ran the check; scratch copy deleted afterwards, real graph untouched).
- Source of truth: verdicts transcribed from `judged.md` as final, including its "Review applied" and "Final pass applied" sections (R01 to R19, F1 to F6, X7, X10); no resolution was marked for the maintainer, so no `unvalidated: awaiting maintainer` annotation (grounded: apply_result says none open). MD-01 and MD-02 cited in every `design_notes`; MD-03 on nodes that hold only a pointer to content held elsewhere.
- Name changed (grounded, deviates from "names unchanged"): the skeleton name of `OWNERSHIP.STANCE.3` is "Bringing Code Inside: Copy, Vendor, Upstream", which contains a colon forbidden by the brief. The batch uses "Bringing Code Inside - Copy, Vendor, Upstream". Recommendation: change the skeleton name the same way; no other name was affected.
- Intent, constraints and epistemic_state fields are my compression of the judge record (inferred as a faithful roll-up; the full Decision text, grounds, positions, rejected, context and certainty are copied verbatim into `design_notes`). Constraint lists are my selection of the MUST rules the Decision states; a reviewer should check no rule was added.
- Traceability (grounded): every node carries a pointer to its judge record; L3 nodes also carry one pointer per original research claim behind their ledger rows, plus web-guideline and JavaScript-guideline pointers where rows carry them.
- Open: eight JavaScript-origin claim ids merged into rows L1540 to L1545 (SUPPLY-C13, C17, C24, C27, C36, C39, C41 and QUALITY-C46) have no slot in the brief's prefix list, so they have no pointer; the rows' JS principle pointer stands for them. Not checked whether the three pointer kinds resolve to real files beyond slot folder names (validate does not check).

## L3 full

Batch: `batch.yaml` (this folder), 56 operations: 35 `node.create`, then 21 `link.create`. Fields set per node: `name`, `intent`, `parent`, `epistemic_state`, `constraints`, `design_notes`, `examples` (where the record gives concrete examples: STANCE.1, STANCE.2, STANCE.4, SELECTION.2, LIFECYCLE.5, CONTAINMENT.1, CONTAINMENT.2, LICENCE.2, LICENCE.3), `impl_pointers`. `history` not set.

Generation: nodes were produced by a script from `judged.md` (verbatim sections), the skeleton (names and tree), the ledgers (claim traceability) and my hand-written intents, constraints and epistemic states. Slot folders used: SRC 01_sourcing, ADOPT 02_adoption, TRANS 06_transverse, MAINT 07_maintainer_doctrine, EXT 09_external_services, AUTH 13_change_authors, RECOV 14_recovery; web claims OPS 06_operations, ARCH 07_architecture_styles, SEC 05_identity_security; JavaScript principles by their node uid in the handoff package.

`design_notes` layout per L3 node: ledger rows; Decision in full; Grounds; Positions considered; Rejected with the condition under which each would be best; Context conditions; Certainty; Stack pointers where the record has them; "Applied after judging" (review and final-pass items that touched the node); Binding decisions. L2 nodes hold the rolled-up decision and certainty and state that they hold no fact of their own. No index node (MD-03) exists in this unit: no node is a pure pointer.

Epistemic states (by certainty): `inferred:` for STANCE.4 and SELECTION.6 (the judge's core claim is inferred). `known | gap:` for LICENCE (L2), LICENCE.3, CONTAINMENT.4, SERVICES.2 (also inferred part) and SERVICES.5. All other nodes `known | inferred: ...` naming the inferred part, except LIFECYCLE.1, CONTAINMENT.3, LICENCE.1 and LICENCE.4 (`known`).

Intra-unit links (src to dst, 21):
- STANCE.1 to SELECTION.2, SELECTION.1; STANCE.2 to STANCE.3, SERVICES.3; STANCE.3 to STANCE.2, LIFECYCLE.4
- SELECTION.1 to STANCE.1; SELECTION.2 to STANCE.1; SELECTION.3 to LIFECYCLE.2; SELECTION.5 to LIFECYCLE.4, LIFECYCLE.5
- LIFECYCLE.2 to SELECTION.3; LIFECYCLE.3 to LIFECYCLE.1; LIFECYCLE.4 to SELECTION.5; LIFECYCLE.5 to SELECTION.5
- CONTAINMENT.1 to SERVICES.3, CONTAINMENT.2; CONTAINMENT.2 to CONTAINMENT.1
- SERVICES.3 to CONTAINMENT.1, STANCE.2
- LICENCE.2 to LICENCE.1
STANCE.1 to SELECTION.1, STANCE.2 to SERVICES.3 and STANCE.3 to LIFECYCLE.4 come from the judge records' Links lines (not the skeleton); the rest are skeleton Links lines.

Cross links: see `cross_links.md` (11 rows plus 2 inbound).

Dry-run check, as run: copy of the real graph to `scratch.ig.yaml` in this folder; `ig-tool apply --batch batch.yaml --role builder` on it: status success, 56 operations; `ig-tool validate`: `graph nodes: 43, links: 21, inter_links: 0, issues: 0, errors: 0, warnings: 0, status: ok`. The real graph already holds ROOT and the seven L1 nodes (8 nodes), so the node `OWNERSHIP` needed no placeholder. `scratch.ig.yaml` deleted.

Judgement calls (inferred): (1) epistemic_state wording `known | inferred: ...` for mixed-certainty nodes, as the brief names `known` and pipe annotations but not a mixed form; (2) LICENCE.2 example lists the prohibited classes as the judge record words them; (3) the SERVICES.1 link to `OPERATION` (L1) is listed in cross_links because the judge Links line names "OPERATION" without an L2 uid.
