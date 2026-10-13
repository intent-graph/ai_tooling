# CLAUDE.md — ai_tooling

Agent entry point for this repository. See [README.md](README.md) for what each folder is and
how to install the CLIs.

## Before working on a subpart

Read that subpart's `README.md` (and `CLAUDE.md` where present) first — each tool and knowledge
base here documents itself:

- `documentation_tools/{codemap,md_structure_sync,md_structure_viz}/`
- `dev_guidelines/{python_guidelines,cli_guidelines,web_architecture_guidelines}/`
- `level_of_detail/` — read `README.md` and `CLAUDE.md` before touching `LOD_CORE.md`,
  `drill_down/`, or `build/`.
- `global_skills/` — user-wide skills; read its `CLAUDE.md` (self-contained folders, no
  links leaving a skill folder).
- `diagrams_for_humans/`, `howto/`, `ai_evolution/`

## Agents and skills (`.claude/`)

- **doc-manifest-agent** — generates doc manifests via `md-doc-tree-{simple,rich,full}`.
- **diagram-agent** — generates yEd `.graphml` from a structured graph description.
- **python-kb-agent** — answers Python questions from `dev_guidelines/python_guidelines/`.
- Skills: `md-doc-tools` (reference for the `md-doc-tree-*` and `md-structure-sync` CLIs),
  `codemap` (reference for the `codemap` CLI).

## Documentation standard

- Target 200-300 lines per file, max 500.
- Line-number TOC in every doc that has one: `[Section](#anchor) _(Lines X-Y)_`.
- Run `md-structure-sync` on a file after editing it, if it carries a line-number TOC.
- No version numbers or dates in docs — git tracks this.
- Full standard: `documentation_tools/DOCUMENTATION_STANDARD.md`.

## Public/private invariant

This repository is public. It must never reference private material: no links or paths
outside the public repos, no absolute or home paths, no names of private projects, folders,
employers or clients. Cross-repo links to the sibling
public `intent_graph` repository are fine as relative links (`../intent_graph/...`), since both
repos sit side by side on a checkout.
