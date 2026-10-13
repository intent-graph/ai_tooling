# Result: critique of the software development philosophy IntentGraph

## L1 headline

The graph validates, keeps the target hierarchy and is faithful to the binding rules in structure; its defects are local and none re-judges a decision. A coordinator batch of 93 operations settles 26 of them; 23 subtle ones go to the final Opus pass.

Main defects, in order of weight:
- Parents that do not cover or do not honestly roll up their children: five L1 or L2 intents omit children (CHANGE_FLOW, CONSTRUCTION, OPERATION, AVAILABILITY, TRANSVERSE.DOCS); eight L2 parents overstate certainty over `inferred` children (seven say `known`); the question awaiting the maintainer (automated reviewer as independent check) is missing at ROOT and at ASSURANCE.RULES, and not carried to its dependent CHANGE_FLOW.REVIEW.4.
- Build residue in graph text: ledger and record ids in 20 epistemic states, 2 constraints and 4 examples; certainty written inside 7 intents or constraints; two nodes keep normative sub-decisions in `examples` under labels no node defines.
- The same fact stated in two nodes (MD-03) in about a dozen pairs (durable test data, placement of logic, type derivation, base structures, tested restore, expand-migrate-contract, delivery metrics, sync plan).
- Links: direction not uniform (about 13 put the governing node first), 4 reversed against their sentence, 11 sentences with a "requires" prefix, 1 target too coarse, 6 leaves with no link although their text names one.
- MD-02: one rule (ASSURANCE.SECURITY.6) applies only to an automated author; one node name and one parent intent say "second model".

Pinned:
- Nodes examined: 292 of 292 (intent, constraints, examples, epistemic state of every node; design_notes of 9; all 403 links).
- Findings fix: 26 (`findings.md` ids X01 to X26; 25 in `fix_batch.yaml`, X26 as one `ig-tool node reorder` command).
- Findings flag: 23 (`findings.md` ids Y01 to Y23).
- Dry-run validate line of `fix_batch.yaml`: after 93 operations on a scratch copy, `ig-tool validate`: nodes 292, links 407, errors 0, warnings 0 (same after the reorder command); scratch copy deleted.

## L2 claims

Pinned:
- Nodes examined: 292 of 292; links read: 403 of 403; design_notes read: 9 nodes.
- Findings fix: 26. Findings flag: 23.
- Dry-run validate of `fix_batch.yaml`: 93 operations applied on a scratch copy, nodes 292, links 407, errors 0, warnings 0; scratch copy deleted.

What holds (mechanical or read in full):
- Validation and shape (grounded): `ig-tool validate` on the original gives 0 errors and 0 warnings; three levels, 232 leaves; all names free of the unsafe characters; no duplicate name; no link joins a node to its own ancestor or descendant; no duplicate link pair; no absolute or home path and no private name in any node.
- Hierarchy (grounded): the seven L1 branches are in the target order of `target_hierarchy.md`; the "roll-up of N records" counts in the states equal the real child counts (compared by eye for every L1 and L2 parent).
- Language swap (grounded): no product name in any intent or constraint; tool leaks are 4 (fixed) and 7 borderline (flagged).
- MD-02 (grounded for the scan, inferred for the verdict): "whoever does the work" is the stated outcome at ROOT, ASSURANCE.RULES.3, SECURITY.3, INTEGRATION.5; one rule depends on the author's kind (SECURITY.6, flagged).
- MD-03 split (inferred): the decision/practice split is kept everywhere it was declared; the failures are restatements, not a missing split.

Defects by check:
- T4 refinement coherence (grounded): children not covered by the parent intent in five nodes (X05 to X09); one L1 constraint exceeds its parent's intent (Y07); one leaf with no constraint (X19); parent says "measured" where the child says "stated" (X20). No parent was found that contradicts a child.
- Parents unreadable alone (grounded): OPERATION constraint 4 names a child by label (X07); five EVOLUTION parents carry a meta line instead of a condition (X10).
- Intent states HOW or names a tool (grounded for four, inferred for seven): X16 fixes `require-hashes`, "merge request", "re-raises", a licence directory layout; Y19 lists seven borderline mechanisms.
- Restated content (grounded that both nodes state it, inferred that one should be an index): Y01 to Y06; one fixed (X18).
- Author rules (MD-02): X17 (second model), Y09 (SECURITY.6).
- Epistemic states (grounded): eight L2 parents carry a child's certainty up (X03); ROOT and ASSURANCE.RULES hide an open question (X04); ASSURANCE.ARTIFACT hides a child gap (X02); ledger ids in 20 states (X14, X15); six leaves say `known` over an inferred core (Y14); one-source figures stated as requirements (Y15).
- Links (grounded): format artifact in 11 sentences (X21); reversed in 4 (X22); coarse target (X23); redundancy (X24, Y11); mismatch between sentence and nodes (Y12); direction convention not uniform (Y10); missing (X25) and orphan (Y13).
- Open (not decided here): whether the 76 parent/child link coincidences are all redundant (Y11); whether the PRIVACY family of links should be reversed (Y10); the scope of TRANSVERSE.DOCS.5 (Y18).

Fix batch:
- `fix_batch.yaml`: 93 operations (64 `node.set`, 11 `link.set`, 7 `link.remove`, 11 `link.create`); each keeps the meaning of the node and changes only the defect (grounded: old text read from the graph, not retyped).
- Left out on purpose: the 23 flags; the order of ASSURANCE children is a CLI command because the batch format has no reorder operation.

## L3 full

Pinned:
- Nodes examined: 292 of 292 (every intent, every constraint list, every epistemic_state and every example; design_notes read in full for ASSURANCE.RULES.1, ASSURANCE.RULES.4, ASSURANCE.AVAILABILITY.3, ASSURANCE.BEHAVIOUR.7, CHANGE_FLOW.REVIEW.4, TRANSVERSE.DOCS.5, CONSTRUCTION.BOUNDARY.2, OPERATION.FEEDBACK, EVOLUTION.DEBT); links read: 403 of 403.
- Findings fix: 26. Findings flag: 23.
- Dry-run validate of `fix_batch.yaml`: `ig-tool apply --batch` on a scratch copy, 93 operations, then `ig-tool validate`: nodes 292, links 407, errors 0, warnings 0; `--dry-run` also reports 93 operations; scratch copies deleted.

Method (grounded):
- Roles and checks: `ig-critic-agent.md` and `ig-critic-review-arch.md` read; binding rules `maintainer_decisions.md` (MD-01 to MD-07) and `target_hierarchy.md` read. The graph was read only through `ig-tool query` (`--structure`, `--overview`, `--node` for all 292 nodes, `--children`, `--links`); the outputs were parsed by script for the mechanical checks and read by branch for the judgement checks. `ig-tool lens` was not needed. The graph file was not edited; the only copies were scratch copies, deleted.
- Format model: `web_architecture_guidelines/build/distill/05_critique/result.md` (L1 and L2 read).
- Not done: the judge records were not re-opened (decisions are out of scope); research ledgers were not consulted, so a claim in a node was not re-grounded against its source; design_notes of the other 283 nodes were searched only for the ids and the maintainer question, not read.

Mechanical results (grounded, counts from the script):
- Structure: 292 nodes = 1 root + 7 L1 + 53 L2 (52 with children, OPERATION.FEEDBACK a leaf) + 231 L3; 403 links, 0 inter links.
- Process ids: in intents 0; in constraints 2 nodes (DATA_INTEGRITY.5, PERFORMANCE.3); in examples 4 nodes (BEHAVIOUR.4, .7, .8, CONTRACTS.1); in epistemic states 20 nodes plus 2 with decision numbers (ROOT, PRIVACY).
- Certainty written inside intent or constraint: DATA_INTEGRITY.1, DATA_INTEGRITY.5, CAPACITY.3, RUNBOOKS.2, TELEMETRY.6, CONTAINMENT.2, DEPLOY.4.
- Base states: 214 `known`, 78 `inferred`; 15 L2 parents have base `known`, 7 of them over at least one child with base `inferred` (the eighth parent of X03, ASSURANCE.SECURITY, is `inferred` but says "components grounded").
- Constraint forms: 384 begin with MUST (96 inverted), 94 carry MUST mid-sentence, 25 "no ..." forms, 54 other.
- Links: 0 ancestor links, 0 duplicate pairs, 76 parent/child coincidences, 20 leaves with no link.

Fix findings (26), one line each; operations are in `fix_batch.yaml`:
- X01 ARTIFACT.1 undefined "L2" in a constraint.
- X02 ARTIFACT roll-up hides ARTIFACT.1 gap.
- X03 eight L2 parents carry child certainty upward (BEHAVIOUR, BOUNDARY, DEBT, DECISIONS, TECHNOLOGY, SELECTION, STANCE, SECURITY).
- X04 awaiting-maintainer token missing at ROOT and ASSURANCE.RULES.
- X05 to X09 parent intents omit children: CHANGE_FLOW (MEASURE, DATA_CHANGE), CONSTRUCTION (NAMING, PARADIGM, PROCESS), OPERATION (TELEMETRY, CAPACITY, RUNBOOKS, FEEDBACK), AVAILABILITY (.3), TRANSVERSE.DOCS (.5).
- X10 meta constraint on five EVOLUTION parents.
- X11 "No ... MUST" grammar on three OWNERSHIP nodes.
- X12 certainty inside intent or constraint (7 nodes).
- X13 ids in constraints and examples (4 nodes).
- X14 sub-decisions in `examples` under undefined labels (BEHAVIOUR.4, .7).
- X15 ids in 18 epistemic states.
- X16 four HOW or tool leaks.
- X17 "second model" wording and node name.
- X18 DECOMMISSION.4 restates a CONTRACTS.1 case.
- X19 SYSTEM_SHAPE.4 has no constraint.
- X20 ASSURANCE "measured budget" against "stated budget".
- X21 eleven link sentences with a "requires" or "related" prefix.
- X22 four links reversed against their sentence.
- X23 RECOVERY.5 link to a whole L1 instead of DEPLOY.4.
- X24 two duplicate links.
- X25 six missing links.
- X26 ASSURANCE child order (RULES last but one), CLI command.

Flag findings (23), one line each; the proposed correction is in `findings.md`:
- Y01 AVAILABILITY.3 restates the BEHAVIOUR.7 data rule and its link says the opposite.
- Y02 PARADIGM.2 and DATA_INTEGRITY.1 both state where a rule lives.
- Y03 type derivation (BOUNDARY.3, CONTRACTS.3) and base structures (BOUNDARY.4, HIDING.4).
- Y04 tested restore, expand-migrate-contract, reviewed script equals deployed script.
- Y05 FEEDBACK and MEASURE.1; REVIEW.1 and RULES.4 and .5; STATE.1 to .3 and DATA_INTEGRITY.4.
- Y06 five further pairs, three with no link.
- Y07 CONSTRUCTION constraint 4 lifts one clause of one leaf.
- Y08 REVIEW.4 and ancestors do not carry the open question; RULES.4 reads settled.
- Y09 SECURITY.6 rule tied to an automated author.
- Y10 link direction convention (about 13 links).
- Y11 parent-level links that double child-level links.
- Y12 five links whose sentence does not match the nodes.
- Y13 14 leaves with no link.
- Y14 `known` over an inferred core; vocabulary differs by branch.
- Y15 one-source figures stated as requirements.
- Y16 PERFORMANCE names .3 as weakest, .3 shows no caveat.
- Y17 open lists omit contested decisions.
- Y18 DOCS.5 and DOCS.2 scope.
- Y19 seven borderline HOW mechanisms.
- Y20 five constraints with a term the intent never mentions.
- Y21 RULES.1 rule held only in `examples`.
- Y22 build vocabulary in states.
- Y23 constraint syntax differs by branch.

Operation counts of `fix_batch.yaml` (grounded): 93 operations: 64 `node.set` (5 of them `unset: [constraints]`), 11 `link.set`, 7 `link.remove`, 11 `link.create`. Every `node.set` replaces whole lists (constraints, examples) with the old content minus the defect; the old text was read from the graph, not retyped.

Questions for the coordinator (open):
- Link direction convention (Y10): the batch assumes "the relying or realizing node is the source" (X22 reverses four links on that reading). If the maintainer reads the other way, X22 should be dropped and Y10 inverted. Recommendation: keep the batch reading, since it holds for about 390 of 403 links; without an answer X22 is the only part affected.
- X14 adds two sentences to intents from each node's design_notes (verdict shape, test location, fixture values; synthetic versus curated records). Recommendation: apply; the content is the judged sub-decision, only its place changes. If refused, the labels still have to leave the examples and states.
