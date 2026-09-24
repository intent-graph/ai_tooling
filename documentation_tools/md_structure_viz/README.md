# md_structure_viz

Visualize documentation structure in software repositories with three complementary tools.

## Quick Start
<!-- Lines 7-16 -->

```bash
# Generate YAML manifests for LLM/AI consumption (default)
md-doc-tree-full /path/to/docs -o doc_manifest

# Produces:
#   doc_manifest_sections.yaml  — folder-nested headings with line numbers
#   doc_manifest_cross_refs.yaml — folder-nested cross-reference map
```

## Three Tools
<!-- Lines 19-19 -->

### 1. md-doc-tree-simple
<!-- Lines 22-33 -->

Ultra-fast, machine-readable list of markdown files.

```bash
md-doc-tree-simple docs/
md-doc-tree-simple docs/ --format json
```

**Output:** Tree structure or JSON with file list
**Performance:** < 1s for 1000 files
**Dependencies:** None (pure zsh)

### 2. md-doc-tree-rich
<!-- Lines 36-46 -->

Enhanced tree with file metadata and titles.

```bash
md-doc-tree-rich docs/
```

**Output:** Tree with per-file stats (lines, words, H1/H2 section count, TOC detection) and title
**Performance:** < 5s for 1000 files
**Dependencies:** grep, sed (standard tools)

### 3. md-doc-tree-full
<!-- Lines 49-79 -->

Complete analysis producing **YAML manifests** (default), with optional **Mermaid flowchart** or **interactive HTML** output.

```bash
# YAML manifests (default) — requires -o
md-doc-tree-full docs/ -o doc_manifest
md-doc-tree-full docs/ -o doc_manifest --heading-depth 3 --max-sections 30

# Mermaid cross-reference flowchart
md-doc-tree-full docs/ --format flow
md-doc-tree-full docs/ --format flow -o refs.md

# Interactive HTML visualization
md-doc-tree-full docs/ --format html -o visualization.html
```

**Default output (manifest):** Two YAML files designed for LLM consumption:
- `<prefix>_sections.yaml` — nested folder hierarchy with headings, line numbers, word counts, TOC detection
- `<prefix>_cross_refs.yaml` — nested folder hierarchy with outgoing document links

**Performance:** < 5s for 100+ files
**Dependencies:** Python 3.10+

**Manifest features:**
- Folder-as-key nested YAML reflecting actual directory tree
- Intermediate empty folders collapsed (e.g., `doc/generated_doc/gen_ai_doc/`)
- Heading entries as `"LINE: ## Heading Text"` — compact, grep-friendly, actionable
- Per-file metadata: line count, word count, TOC detection (`TOC@start-end`)
- Adaptive heading depth: auto-collapses to shallower level if a file exceeds threshold
- Cross-reference deduplication

## Installation
<!-- Lines 82-93 -->

Requires Python >= 3.11.

```bash
# From the tool folder
cd documentation_tools/md_structure_viz
uv tool install -e .

# Or from the repo root
uv tool install -e documentation_tools/md_structure_viz
```

## Examples
<!-- Lines 96-96 -->

### Simple Mode
<!-- Lines 99-112 -->

```bash
$ md-doc-tree-simple docs/
docs/
├── README.md
├── api/
│   ├── authentication.md
│   ├── endpoints.md
│   └── schemas.md
└── guides/
    ├── getting-started.md
    └── deployment.md
```

### Rich Mode
<!-- Lines 115-130 -->

```bash
$ md-doc-tree-rich docs/
docs/
├── README.md  `[120L, 850W, 3S]`  : "Project Documentation"
├── api/
│   ├── authentication.md  `[100L, 700W, 5S]`  : "API Authentication"
│   ├── endpoints.md  `[250L, 2100W, 12S]`  : "REST Endpoints"
│   └── schemas.md  `[180L, 1400W, 8S]`  : "Data Schemas"
└── guides/
    ├── getting-started.md  `[85L, 600W, 4S]`  : "Getting Started"
    └── deployment.md  `[130L, 950W, 6S]`  : "Deployment"

Total: 7 files | 765 lines | 6600 words | 38 sections
```

### Full Mode - YAML Manifest (default)
<!-- Lines 133-189 -->

```bash
$ md-doc-tree-full docs/ -o doc_manifest
Manifest generated:
  doc_manifest_sections.yaml
  doc_manifest_cross_refs.yaml
```

**doc_manifest_sections.yaml:**

```yaml
# doc_sections  |  root: docs  |  6 files, 38 sections

./:
  README.md: # 120 lines, 850 words, TOC@3-25
    - "1: # Project Documentation"
    - "15: ## Installation"
    - "42: ## Quick Start"
  api/:
    endpoints.md: # 250 lines, 2100 words
      - "1: # REST API Endpoints"
      - "18: ## Authentication"
      - "95: ## Error Handling"
    authentication.md: # 100 lines, 700 words
      - "1: # Auth Guide"
      - "12: ## OAuth2 Flow"
  guides/:
    getting-started.md: # 85 lines, 600 words
      - "1: # Getting Started"
      - "30: ## Prerequisites"
```

**doc_manifest_cross_refs.yaml:**

```yaml
# doc_cross_refs  |  root: docs  |  6 files, 7 references

./:
  README.md: # 120 lines, 850 words
    - api/endpoints.md
    - guides/getting-started.md
  api/:
    endpoints.md: # 250 lines, 2100 words
      - api/authentication.md
    authentication.md: [] # 100 lines, 700 words
  guides/:
    getting-started.md: # 85 lines, 600 words
      - api/authentication.md
```

**Key features:**
- Nested YAML reflecting actual directory tree
- Heading entries with line numbers for targeted reads
- `TOC@start-end` when a managed Table of Contents is detected
- Adaptive depth: files with too many headings auto-collapse (see `--max-sections`)
- Per-file metadata: lines, words, TOC presence

### Full Mode - Other Formats
<!-- Lines 192-200 -->

```bash
# Mermaid cross-reference flowchart
$ md-doc-tree-full docs/ --format flow

# Interactive HTML visualization
$ md-doc-tree-full docs/ --format html -o visualization.html
```

## CLI Reference
<!-- Lines 203-203 -->

### Shared Flags (all three tools)
<!-- Lines 206-211 -->

| Option | Default | Description |
| --- | --- | --- |
| `--ignore-default` / `--no-ignore-default` | `True` | Filter venv, node_modules, .git, dist, build, etc. |
| `--respect-gitignore` | `False` | Additionally filter files matched by .gitignore |

### md-doc-tree-simple
<!-- Lines 214-222 -->

```
md-doc-tree-simple <path> [options]
```

| Option | Default | Description |
| --- | --- | --- |
| `--format` | `tree` | `tree` or `json` |

### md-doc-tree-rich
<!-- Lines 225-231 -->

```
md-doc-tree-rich <path> [options]
```

No mode-specific flags beyond the shared flags. Outputs a tree with per-file metadata.

### md-doc-tree-full
<!-- Lines 234-248 -->

```
md-doc-tree-full <path> -o <prefix> [options]
```

| Option | Default | Description |
| --- | --- | --- |
| `--output`, `-o` | (required for manifest) | Output prefix or file path |
| `--format`, `-f` | `manifest` | `manifest`, `flow`, or `html` |
| `--heading-depth` | `2` | Max heading level (`2` = `#` + `##`) |
| `--max-sections` | `20` | Per-file threshold for adaptive depth fallback |
| `--stats`, `-s` | | Print statistics only |
| `--ignore-default` / `--no-ignore-default` | `True` | Filter venv, node_modules, etc. |
| `--respect-gitignore` | `False` | Additionally filter .gitignore patterns |

## Architecture
<!-- Lines 251-263 -->

- **Tool 1 (md-doc-tree-simple)**: Pure zsh, filesystem only
- **Tool 2 (md-doc-tree-rich)**: Zsh with grep/sed parsing
- **Tool 3 (md-doc-tree-full)**:
  - Python with full markdown parsing
  - **YAML manifest** (default): Two nested YAML files for LLM/AI consumption
  - **Mermaid flowchart** (`--format flow`): Cross-reference graph
  - **HTML** (`--format html`): Interactive D3.js visualization

Each tool is independent and can be used separately.

For detailed output format specifications, see [OUTPUT_FORMATS.md](OUTPUT_FORMATS.md).

## Testing
<!-- Lines 266-270 -->

```bash
uv run --extra dev pytest
```

## License
<!-- Lines 273-274 -->

MIT
