# Render brief — project the two IntentGraphs into the human-readable guideline

Paths are relative to the guideline folder `ai_tooling/dev_guidelines/web_architecture_guidelines/`.

## Purpose and readers

The graphs in `intent_graphs/` are the source of truth. The markdown files are a projection
of them for two readers:

- an engineer or architect designing or reviewing a web application on this stack, who must be
  able to act on each line: decide where a responsibility goes, choose the default, know when
  the default does not apply;
- an AI agent doing the same, which reads the README first and drills into one file.

Code-level conventions are out of scope (Python: `../python_guidelines/`; JavaScript: a
separate guideline).

## Files to produce (in the guideline folder, lowercase names)

- `README.md` — what this is and is not; the one-paragraph thesis (L0 and the allocation in
  three lines); how to read (which file for which question); the open maintainer questions,
  each in one self-contained paragraph with its recorded default; the two graphs and how to
  query them; provenance (`build/` and `build/RECIPE.md`); related guidelines.
- `CLAUDE.md` — short agent navigation card: read README first; drill one file; query a node
  with `ig-tool query -g intent_graphs/<file> --node <UID>`; never load a whole graph file.
- The guideline body, split by the documentation standard (200 to 300 lines per file, 500 at
  most, split on semantic boundaries). Expected split, adjust if a file would exceed 500 lines:
  - `allocation.md` — the ALLOCATION branch of both graphs: forces and how they combine,
    context, rules, the allocation matrix (one line per responsibility: authority, copies,
    forbidden, what moves it), then the stack placements.
  - `philosophy.md` — the four tier branches of the philosophy graph (DATA, LOGIC,
    INTERACTION, TRANSVERSE).
  - `stack_defaults_<branch>.md` — the projection graph per tier branch (data, logic,
    interaction, transverse), or fewer files if they fit.

## How to render a node (level of detail)

- Per node, at claim level: its name as a heading or bold lead, the decided practice in one to
  three lines (from `intent`), then the rules a reader acts on (from `constraints`, grouped,
  not all copied if they repeat), then "Acceptable when" or "Changes when" lines from
  `design_notes` where the record names them.
- Open maintainer clauses are shown inline, visibly, with the recorded default.
- Each node ends with its uid in the form `` `UID` `` so a reader can query the graph for the
  full grounds, positions considered, evidence and sources. Do not copy design_notes
  wholesale; do not cite ledger ids.
- Roll-up nodes become section intros of one to three lines.
- Philosophy files stay stack-neutral; stack files name the stack.
- Where a projection node refines a philosophy node, say so in one phrase with a relative link
  to the section in the other file.

## Format rules

- Documentation standard: `../../documentation_tools/DOCUMENTATION_STANDARD.md`. Every file
  that has a TOC uses line-number TOCs; run `md-structure-sync <file>` after writing each file.
- One Mermaid diagram in `allocation.md` (the three tiers and what each is authority for) and
  at most one per other file where it carries structure better than prose.
- No dates or version numbers. Relative links only. Public repository: no absolute or home
  paths, no private names.
- Plain, precise English; full sentences only where a connective carries logic; lists and
  tables otherwise.

## How to read the graphs

Use `ig-tool` (see `../../../intent_graph/agents/PRIMER_TOOLS.md`): `ig-tool tree -g <graph>`
for structure, `ig-tool query -g <graph> --node <UID>` or `--children <UID>` per node. A
script that iterates `query --node` over the tree is fine; never load a graph file whole into
your context.
