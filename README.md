# ai_tooling

Generic, reusable tooling and knowledge bases for working with AI coding agents: CLIs for
navigating and documenting codebases, a transverse level-of-detail practice, and guideline
knowledge bases an agent can consult mid-task.

This repository is designed to sit beside the sibling `intent_graph` repository on disk; relative
links from here assume a checkout layout of `../intent_graph`.

## Layout
<!-- Lines 12-29 -->

- `documentation_tools/` — `md_structure_sync` (TOC/line-range sync CLI), `md_structure_viz`
  (doc-tree visualization CLI), `codemap` (structural code-graph CLI for Python), and
  `DOCUMENTATION_STANDARD.md` (the doc format these tools maintain).
- `dev_guidelines/` — `python_guidelines` (a Python knowledge base, LOD-organized),
  `cli_guidelines` (CLI interface-design consensus: clig.dev/12-Factor/POSIX/GNU) and
  `web_architecture_guidelines` (architecture of a JavaScript + Python + Postgres web
  application: who does what across tiers, held as two IntentGraphs).
- `diagrams_for_humans/` — reference for generating yEd `.graphml` diagrams.
- `level_of_detail/` — the level-of-detail practice: an agent-facing core plus satellites, and
  the authoring record behind them.
- `howto/` — short how-tos (exposing a Python tool system-wide, writing a structured subagent).
- `global_skills/` — Claude Code skills meant for every project, installed user-wide by symlink
  (`subagent-orchestration`: brief sub-agents by pointer, fixed I/O, three-level returns).
- `ai_evolution/` — notes on AI evolution and method (in French).
- `.claude/` — agents (`doc-manifest-agent`, `diagram-agent`, `python-kb-agent`) and skills
  (`md-doc-tools`, `codemap`) that wrap the CLIs above for agent use.

## Installing the CLIs
<!-- Lines 32-44 -->

Each CLI is a standalone Python project installed system-wide with `uv`:

```bash
uv tool install -e documentation_tools/codemap
uv tool install -e documentation_tools/md_structure_sync
uv tool install -e documentation_tools/md_structure_viz
```

This puts `codemap`, `md-structure-sync`, `md-doc-tree-simple`, `md-doc-tree-rich`, and
`md-doc-tree-full` on `PATH`, callable from any directory. Check each tool's own README for
test setup and alternative install methods.

## License
<!-- Lines 47-55 -->

- **CC BY 4.0** — `level_of_detail/`, `ai_evolution/`, `dev_guidelines/`, `howto/`,
  `documentation_tools/DOCUMENTATION_STANDARD.md` (intellectual/creative work).
- **MIT** — everything else: `documentation_tools/` code, `diagrams_for_humans/`, `.claude/`,
  `global_skills/`.
- Code files inside the CC BY folders (`*.py`, `*.sh`) are MIT.

Copyright 2026 Rémi Cura. Texts: [`LICENSE`](LICENSE) (MIT) and
[`LICENSE-CC-BY-4.0.txt`](LICENSE-CC-BY-4.0.txt); each CC BY folder also carries a short `LICENSE.md`.
