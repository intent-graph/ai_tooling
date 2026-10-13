# Render result: CONSTRUCTION

## L1 headline

- Files: `construction.md`, 478 lines, no split (under the 500 limit).
- Nodes rendered: 48 of 48 in the branch (1 L1, 10 L2, 37 L3); every section ends with its uid.
- Open maintainer points shown inline: 0 "awaiting maintainer" in this branch; 4 open gaps shown, each as one "Open point" line (BOUNDARY.3, STATE.4, DEPENDENCY_DIRECTION.2, DATA_NOT_CODE.3).
- md-structure-sync: run on the file (line-number TOC to level 2, line comments to level 2), status ok.

## L2 claims

- Structure: L1 thesis and four branch-wide MUST rules, a map table, then ten L2 sections in graph order, each with its L3 subsections. Grounded (counted against the tree).
- Each L3: decided practice, MUST/MUST NOT constraints, "Best instead when" from the rejected-position records, links, certainty note, uid. Grounded.
- Cross-file links point to sibling sections by slug of the node name (ownership, assurance, change_flow, evolution, operation, transverse). Names were read from the graph; the sibling files did not exist when written, so anchor existence is inferred.
- One link label differs from the target node's name: the link for CHANGE_FLOW.DATA_CHANGE.4 uses its real name, "Order and Compatibility With Running Code", with the phrase "relies on it" (the graph link says database access sits behind a layer in code). Grounded.
- Open points shown (the gap stated in the graph, nothing invented): BOUNDARY.3 checklist reading of the contract format; STATE.4 no source on immutability versus restriction; DEPENDENCY_DIRECTION.2 open as a standalone principle; DATA_NOT_CODE.3 "checked after resolution without a race". Grounded.
- Dropped by design: ledger, register and research-claim ids, the P1/P2 position labels, grounds prose in design_notes. No product, tool or language names; no dates, absolute paths or private names (grep checked). Grounded.
- Judgment: sibling-parallel run shared the scratchpad directory; my dump file may have been overwritten by another agent, but I had read it fully before. Not material.

## L3 full

Method: `ig-tool tree --root CONSTRUCTION` for the structure; a script iterated `ig-tool query --node` and `--links` over the 48 uids (intent, epistemic_state, constraints, design_notes sections Rejected, Context, Flags, plus links). Names of linked sibling nodes were fetched per uid.

Files written:
- `construction.md`: 478 lines, sections Thesis, Map, ten L2 sections.
- This file.

Rendering decisions:
- Thesis: node intent as 3 sentences plus the four L1 constraints as a list.
- "Best instead when": taken from the Rejected record where it names a condition ("best only where ..."); "never best" cases stated as such in one clause. Conditions marked inferred in the record stay marked inferred.
- Links: realizes/requires/refines links to other branches become a phrase with a relative link; intra-file links use heading slugs. Links within the branch that change what a reader does were kept (derivation order and naming, cycles and hiding, layering and gates, state and caches).
- Index nodes: none in the branch (no node is a pure pointer); BOUNDARY.1's deferred web-architecture half was left out (not judged in the graph).
- TOC: level 2 only, to keep the file under 500 lines (a level-3 TOC took it to 507).

Pins:
- Nodes rendered 48/48. Open maintainer points: 0 awaiting maintainer; 4 open gaps shown.
- Inferred items in the text: sibling anchors exist; every "inferred" tag is copied from the node's own certainty record.
- Not done: no check that sibling files contain the linked sections (they are written in parallel).
