# Render brief — project the IntentGraph into the human-readable guideline

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/software_development_guidelines/`;
your task message gives the absolute root and the file(s) you write.

## Purpose and readers

The graph `intent_graphs/software_development_philosophy.ig.yaml` is the source of truth. The
markdown files are a projection of it for two readers:

- an engineer or tech lead deciding how a team sources, verifies, builds, ships, runs and evolves
  software, whatever the stack, who must be able to act on each line: what the practice is, what
  it guarantees, and when another practice would be the best;
- an AI agent doing the same, which reads the README first and drills into one file.

Stack mechanisms are out of scope: the Python, JavaScript and web architecture guidelines hold
them (`../python_guidelines/`, `../javascript_guidelines/`, `../web_architecture_guidelines/`).

## Files (in the guideline folder, lowercase names)

- One body file per L1 branch: `ownership.md`, `assurance.md`, `construction.md`,
  `change_flow.md`, `operation.md`, `evolution.md`, `transverse.md`. Documentation standard:
  200 to 300 lines per file, 500 at most, split on semantic boundaries. If a branch exceeds 500
  lines, split it by L2 groups into `<branch>_<group>.md` files and make `<branch>.md` the
  branch intro and index.
- `README.md` and `CLAUDE.md`: written last, by the README writer (its own task message).

## How to render a node (level of detail)

- The L1 node opens its file: its intent as a two-to-four-line thesis, then a short map of its
  L2 nodes (one line each).
- An L2 node becomes a section: its intent as a one-to-three-line intro, then its L3 nodes.
- An L3 node becomes a subsection or a bold lead, at claim level: the decided practice in one to
  three lines (from `intent`), then the rules a reader acts on (from `constraints`, grouped, not
  copied when they repeat), then "Best instead when" lines from `design_notes` where the record
  names the condition under which another practice would be the best.
- An open maintainer point (an `epistemic_state` with "awaiting maintainer") is shown inline,
  visibly, with the default applied. An open gap that changes what a reader does (a missing
  number, an unproven effect) is shown in one short line; the rest stays in the graph.
- Each node ends with its uid as `` `UID` `` so a reader can query the graph for the grounds,
  positions considered and sources. Do not copy design_notes wholesale; do not cite ledger ids,
  register ids or research claim ids.
- Index nodes (one location per fact, MD-03) become a line pointing to the section that holds
  the content, as a relative link.
- Links: where a node `realizes` or `requires` a node in another file, say so in one phrase with
  a relative link to that section; other link types only where they change what the reader does.
- Stack-neutral throughout: no product, tool or language names except where the graph's intent
  itself names a standard (for example a published framework).

## Format rules

- Documentation standard: `../../documentation_tools/DOCUMENTATION_STANDARD.md`. Every file with
  a TOC uses line-number TOCs; run `md-structure-sync <file>` after writing each file.
- At most one Mermaid diagram per file, only where it carries structure better than prose.
- No dates or version numbers. Relative links only. Public repository: no absolute or home
  paths, no private names, no mention of the maintainer's private practice or its sources.
- Plain, precise English; full sentences only where a connective carries logic; lists and
  tables otherwise.

## How to read the graph

Use `ig-tool` (see `../../../intent_graph/agents/PRIMER_TOOLS.md`): `ig-tool tree -g <graph>
--root <UID>` for a branch's structure, `ig-tool query -g <graph> --node <UID>` per node,
`ig-tool query -g <graph> --links <UID>` for its links. A script that iterates `query --node`
over a branch is fine; never load the graph file whole into your context.
