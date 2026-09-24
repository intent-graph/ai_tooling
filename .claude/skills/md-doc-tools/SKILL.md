---
name: md-doc-tools
description: >
  Reference for md-structure-sync and md-doc-tree-{simple,rich,full} CLIs.
  Use when syncing markdown TOCs, visualizing doc trees, or generating doc manifests.
user-invocable: false
---

# md-doc-tools — Markdown Structure Maintenance & Visualization

Two tool families, both system-wide. Installed via `uv tool install -e .` from their respective directories.

---

## md-structure-sync — TOC and Line-Range Sync

Detects and fixes out-of-sync TOCs and line-range annotations in markdown files. Idempotent — safe to run repeatedly or in CI/pre-commit.

### Basic Usage

```bash
# Single file
md-structure-sync path/to/file.md

# Directory (recursive)
md-structure-sync path/to/docs/ --pattern "*.md"

# Dry run (show what would change)
md-structure-sync path/to/file.md --dry-run
```

### Key Flags

| Flag | Default | Notes |
|------|---------|-------|
| `--pattern` | `*.md` | Glob for directory mode |
| `--min-level` | 2 | Minimum header level to track |
| `--max-level` | 4 | Maximum header level to track |
| `--no-line-comments` | off | Skip `<!-- Lines -->` comments after headers |
| `--toc` | `maintain-only` | Policy: `maintain-only`, `add-above`, `remove`, `add-always` |
| `--toc-min-headers` | 3 | For `--toc add-above`: only add TOC if >= N headers |
| `--dry-run` / `-n` | off | Preview without writing |
| `--quiet` / `-q` | off | Only output errors |

### What It Fixes

- TOC entries: `[Section](#anchor) _(Lines X-Y)_`
- Line comments after headers: `<!-- Lines X-Y -->`
- Both are updated to reflect actual line numbers after edits

### When to Run

Run after editing any markdown doc that has TOC or line-range annotations. The CLAUDE.md standard requires it.

---

## md-doc-tree — Documentation Structure Visualization

Three tools with progressive complexity, all installed together from `md_structure_viz/`.

### md-doc-tree-simple — File tree only

```bash
md-doc-tree-simple /path/to/docs/
```

Plain file tree. Fastest (< 1s). Good for scripting and quick listing.

### md-doc-tree-rich — Tree + metadata

```bash
md-doc-tree-rich /path/to/docs/
```

Adds `[lines, words, sections]` and title per file. Good for structure overview.

### md-doc-tree-full — Interactive visualization

```bash
# HTML (recommended for large doc trees)
md-doc-tree-full /path/to/docs/ --format html -o viz.html
open viz.html

# YAML manifest (for programmatic use)
md-doc-tree-full /path/to/docs/ --format manifest -o manifest

# Mermaid flow diagram
md-doc-tree-full /path/to/docs/ --format flow -o graph.md
```

| Format | Output | Best for |
|--------|--------|----------|
| `html` | Single self-contained HTML file | Exploring 50+ file doc trees interactively |
| `manifest` | `_sections.yaml` + `_cross_refs.yaml` | Programmatic analysis, agent input |
| `flow` | Mermaid markdown | Embedding in docs |

Key flags: `--heading-depth N`, `--max-sections N`, `--stats`, `--respect-gitignore`.

### Common Mistakes

1. **md-doc-tree-full default format is `manifest`**, not `html`. Always pass `--format html` if you want the interactive visualization.
2. **md-doc-tree-full `--stats` alone fails**: the default `manifest` format requires `--output`. Pair it with `--format flow`, e.g. `--stats --format flow`.
3. **Manifest format produces TWO files**: `<prefix>_sections.yaml` and `<prefix>_cross_refs.yaml`. The `-o` flag is a prefix, not a single file path.
