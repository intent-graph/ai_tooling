# CLAUDE.md — software development guidelines

Agent navigation card.

- Read [README.md](README.md) first: the thesis, the file per question, the maintainer decisions
  (they override any source).
- Then open one branch index (`ownership.md`, `assurance.md`, `construction.md`,
  `change_flow.md`, `operation.md`, `evolution.md`, `transverse.md`) and drill into one body file.
- For the grounds of a decision, query its node id (shown in backquotes at the end of each
  section): `ig-tool query -g intent_graphs/software_development_philosophy.ig.yaml --node <UID>`.
  Never load the graph file whole.
- The graph is the source of truth; the markdown files are its projection. To change a decision,
  change the graph (with `ig-tool`, `--role` and `-m`), then re-render the affected file and run
  `python3 build/distill/07_render/check_links.py` and `md-structure-sync <file>`.
- Stack mechanisms live in the stack guidelines (`../python_guidelines/`,
  `../javascript_guidelines/`, `../web_architecture_guidelines/`), not here.
- Public repository: no absolute or home paths, no private names.
