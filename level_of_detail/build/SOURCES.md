# Sources — the ingredients, and what was taken from each

Purpose: every input that shaped the agent-facing files, with what was extracted and what was deliberately left behind. A future session can re-read a source at the level it needs instead of everything. Paths are relative to the tooling repository root unless absolute.

## Internal material
<!-- Lines 7-23 -->

| Source | What was taken | What was left behind |
|---|---|---|
| the author's own notes on working method and communication | rough-to-fine derivation; functional hierarchy levels; macro/meso/micro zoom; conclusion first; record what was ruled out | domain specifics, voice and style |
| the IntentGraph pitch, `../intent_graph/CLAUDE.md`, `../intent_graph/README.md` | the problem statement: flat artifacts have no zoom; mixed-detail coherence; a lens as a per-node level assignment | product versus projection graphs; agents catalog |
| `../intent_graph/agents/PRIMER_00_PHILOSOPHY.md` | P2 "zooming adds information, never changes meaning" → invariant 1; P5 normalization → partition without overlap; "never invent intent" → invariant 3; "task return ≤ 80 words, detail to disk" → rolled-up returns | axioms about intent as source of truth; UID grammar; tool rules |
| `../intent_graph/agents/PRIMER_01_SEMANTICS.md` | epistemic state vocabulary → certainty (renamed grounded / inferred / open); "parent must be readable without expanding children" → drill-down test; execution order is not structure → naming children as things | field schema; link types; Obsidian safety |
| `../intent_graph/agents/PRIMER_02_NAVIGATION.md` | skeleton / lean / full → label / claim / full; the IV pattern → the starting shape; budget forcing focus; "orient once, spot-check, do not re-read" → INPUT | commands |
| `../intent_graph/agents/PRIMER_03A_EDITING.md` | expansion signals and the atomic-node test → DRILL_DOWN; content migration on split; propagation cascade as a miscut signal; temporary mess allowed if marked | propagation channels table; UID rules |
| `../intent_graph/agents/PRIMER_04_WORKFLOWS.md` | effort hint → purpose drives depth; critique grounding check ("default to refuted") → certainty of acquired knowledge decays | workflows, roles |
| `../intent_graph/agents/PRIMER_DIALOGUE.md` | question file shape: minimal ask first, deepened context second; batch questions; extract, do not re-read → COMMUNICATION questions section | file protocol |
| `../intent_graph/agents/PRIMER_TOOLS.md`, `PRIMER_05_INTENT_RESOURCES.md` | nothing beyond confirming the tooling is out of scope | all |
| `dev_guidelines/python_guidelines/CLAUDE.md`, `dev_guidelines/python_guidelines/README.md` | LOD 0–5 navigation: grep the manifest first, read index files, drill only when needed, stop condition, anti-patterns → INPUT | the Python content |
| `howto/programming_subagents.md` | the brief as a typed call: context at claim, target in full, output contract; effort hint | template text |
| `documentation_tools/DOCUMENTATION_STANDARD.md` | file lengths, line-number TOCs, no dates in docs | — |
| Claude Code harness rules (the system prompt of the authoring session) | confirmation before irreversible actions; "check that evidence supports this specific action" → ACTION; final-message style rules sit below this practice: they are form, LOD is selection | copied nothing verbatim |

## External material
<!-- Lines 26-30 -->

| Source | What was taken |
|---|---|
| `ELICITATION_ROUND_1.md` (this folder) | every decision in `DECISIONS.md` |

## Outside knowledge invoked deliberately
<!-- Lines 33-34 -->

SADT / IDEF0 (parent box and child diagram share a boundary; three to six boxes per diagram). OLAP roll-up and drill-down. Real-time graphics level of detail. Toulmin's model of argument (claim, grounds, warrant). Outliner editors (collapse, expand). Photographic depth of field. The Minto pyramid principle was considered as a priming target and not named.
