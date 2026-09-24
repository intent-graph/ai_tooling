# CLI Guidelines

Interface-design guidance for any command-line tool in this repo (`ig-tool`, `codemap`,
`md-doc-tree-*`, `md-structure-sync`, or a new CLI). Governs the **interface contract** —
flags, output modes, exit codes, help text — as distinct from internal code structure.

## Start here
<!-- Lines 9-12 -->

[cli_guidelines.md](cli_guidelines.md) — the full
guideline set, grounded in the clig.dev / 12-Factor / POSIX / GNU consensus.

## When to use this
<!-- Lines 15-22 -->

- Designing a new CLI or a new subcommand's flags/output shape.
- Reviewing an existing CLI for interface-contract gaps (missing `--version`, flat exit
  codes, inconsistent `--dry-run`/`--force`, etc.).
- Any refactor that touches argument parsing, output formatting, or exit-code semantics.

Not for internal code structure (module layout, function decomposition) — that's the
Python Development Guidelines KB (`dev_guidelines/python_guidelines/`) instead.
