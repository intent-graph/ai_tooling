# CodeMap

**A structural map of codebases, purpose-built as the substrate for AI agent reasoning.**

## The Problem
<!-- Lines 7-14 -->

AI agents that modify code need a "world model" of the codebase. The two obvious representations fail in opposite directions:

- **Raw source / full ASTs**: Semantically complete but overwhelmingly verbose. Syntactic noise (punctuation, boilerplate, formatting) floods the context window and leaves no room for reasoning.
- **Flat-text RAG**: Treats a repository as a bag of text chunks. Structural relationships — call graphs, containment, data dependencies — are invisible. The agent sees *words* but not *architecture*.

Agents either drown in detail or navigate blind. We need something in between.

## What CodeMap Does
<!-- Lines 17-28 -->

CodeMap parses a Python project into a **structural graph** — a representation that captures the skeleton of a codebase (what exists, where, and how things relate) while discarding syntactic noise. Agents query this graph through an 11-method API to understand the code before touching it.

**Properties:**

- **Hierarchical**: mirrors code nesting (package → module → class → method/function)
- **Pointer-based**: nodes store signatures and locations, not source code. Code is retrieved on demand.
- **Relational**: edges capture containment, calls, inheritance, and imports
- **Agent-friendly**: YAML serialization with V-shaped context generation
- **Parsed via Jedi + parso**: extracts structure and resolves cross-file symbols without executing the target code
- **Best-effort SQLite mapping**: detects `.db`/`.sqlite` files, adds table structure, and continues with warnings on introspection failures

## Installation
<!-- Lines 31-40 -->

```bash
cd documentation_tools/codemap
uv tool install -e .
# tests
uv run --extra dev pytest
```

**Runtime dependencies:** `jedi`, `pyyaml` — nothing else.

## Quick Start
<!-- Lines 43-75 -->

```python
from codemap import CodeMap

# Parse a project
cm = CodeMap.build("path/to/your/python/project")

# Disable SQLite introspection if needed
cm_no_db = CodeMap.build("path/to/your/python/project", include_sqlite=False)

# Orient: see the full skeleton
print(cm.overview())

# Locate: find nodes by name
results = cm.search("User")

# Focus: get V-shaped context for a specific node
print(cm.context("mypackage.models.User.validate"))

# Navigate: see what a node connects to
neighbors = cm.neighbors("mypackage.models.User", edge_type="inherits")

# Adjust: drill into or hide parts of the view
cm.expand("mypackage.models")   # show children
cm.collapse("mypackage.models") # hide children

# Read: get actual source when ready to modify
print(cm.source("mypackage.models.User.validate"))

# Export: visualize the graph in yEd
cm.export_yed("/tmp/my_graph.graphml", flat=True)
```

## The V-Shape: Context Generation
<!-- Lines 78-101 -->

The primary job of CodeMap is to produce **focused context** for an agent working on a specific node. The shape of that context follows the V-shape principle:

> The farther from the focus, the less detail — but always keep orientation.

```
  ___              ___       ← wide brim: all top-level packages (names only)
      \     |     /             orientation — "where am I in the whole?"
       \    |    /
        \   |   /            ← the V: detail gradient (coarse → focused)
         \  |  /
          \ | /              ← center vertical: lineage from root to focus
           \|/
          _____              ← ground bar: focus node + immediate neighbors
```

| Axis | What | Detail level |
| --- | --- | --- |
| **Wide brim** | Root package + its direct children (subpackages, modules) | Names only |
| **Vertical spine** | Direct ancestors from root to focus | Names + signatures |
| **Ground bar** | Focus node + immediate neighbors (calls, imports, inheritance — both directions) | Full detail for focus; signatures for neighbors |

Everything else is absent. The agent sees where it is, how it got there, and what it's touching — nothing more.

## API Reference
<!-- Lines 104-106 -->

All 11 methods are on the `CodeMap` object returned by `CodeMap.build()`.

### Build
<!-- Lines 109-113 -->

| Method | Purpose | Returns |
| --- | --- | --- |
| `CodeMap.build(path, include_sqlite=True)` | Parse a Python project into a map | `CodeMap` object |

### Orient & Locate
<!-- Lines 116-121 -->

| Method | Purpose | Returns |
| --- | --- | --- |
| `cm.overview()` | Full project skeleton — names and nesting only | YAML string |
| `cm.search(query)` | Find nodes by name (case-insensitive substring) | List of dicts |

### Focus & Navigate
<!-- Lines 124-129 -->

| Method | Purpose | Returns |
| --- | --- | --- |
| `cm.context(qname)` | V-shaped context for a focus node (the workhorse) | YAML string |
| `cm.neighbors(qname, edge_type?)` | Immediate connections, optionally filtered | List of dicts |

### Adjust Detail
<!-- Lines 132-139 -->

| Method | Purpose | Returns |
| --- | --- | --- |
| `cm.expand(qname)` | Show children of a node | Updated YAML |
| `cm.collapse(qname)` | Hide a node's descendants | Updated YAML |
| `cm.include(qname)` | Add a specific node at full detail | Updated YAML |
| `cm.exclude(qname)` | Remove a node and all descendants from view | Updated YAML |

### Read Source
<!-- Lines 142-146 -->

| Method | Purpose | Returns |
| --- | --- | --- |
| `cm.source(qname)` | Retrieve actual source code lines for a node | Source string |

### Export
<!-- Lines 149-166 -->

| Method | Purpose | Returns |
| --- | --- | --- |
| `cm.export_yed(path?, flat?)` | Export graph to yEd-compatible GraphML | `Path` of written file |

The yEd export uses yWorks XML extensions for proper visual rendering. Nodes are color-coded by kind (package=indigo, module=blue, class=amber, function=green, method=teal). Edges are styled by kind (calls=blue, imports=purple, inherits=red). Each node carries `depth`, `kind`, and `qualified_name` as GraphML data attributes — usable via yEd's Properties Mapper for color gradients, sizing, and filtering.

Set `flat=True` (recommended) to emit all nodes at the top level — works with most yEd layout algorithms. Default grouped mode uses collapsible nested groups.

**Typical agent workflow:**

1. `overview()` → `search()` — find where to work
2. `context()` — get the V-shaped default view
3. `expand()` / `collapse()` / `include()` / `exclude()` — dial detail up or down
4. `neighbors()` — explore connections from any visible node
5. `source()` — read actual code when ready to modify
6. `export_yed()` — (optional) visualize the graph for human review

## Data Model
<!-- Lines 169-169 -->

### Nodes
<!-- Lines 172-187 -->

Every code unit is a `CodeNode` identified by its **qualified name** (e.g., `mypackage.models.User.validate`).

| Field | Type | Description |
| --- | --- | --- |
| `qualified_name` | `str` | Primary key — dotted path from package root |
| `name` | `str` | Short name (`validate`) |
| `kind` | `NodeKind` | `package`, `module`, `class`, `function`, `method`, `database`, `db_schema`, `db_table` |
| `path` | `str` | File path relative to project root |
| `line_start` | `int` | Start line (1-indexed) |
| `line_end` | `int` | End line (1-indexed) |
| `signature` | `str \| None` | `def validate(self) -> bool` or `class User` |
| `docstring` | `str \| None` | First line of docstring |
| `parent` | `str \| None` | Qualified name of containing node |
| `metadata` | `dict \| None` | Optional extra data (e.g., table columns for `db_table`) |

### Edges
<!-- Lines 190-199 -->

Relationships are `CodeEdge` triples — no artificial IDs.

| Edge Kind | Meaning | Example |
| --- | --- | --- |
| `contains` | Structural nesting | module → class, class → method |
| `calls` | Function/method invocation | `validate` → `check_email` |
| `imports` | Module-level import | models → utils |
| `inherits` | Class inheritance | `User` → `BaseModel` |

### Graph
<!-- Lines 202-204 -->

`CodeGraph` holds the primary data (nodes dict + edges list) plus derived indexes (children, edges_from, edges_to) rebuilt on construction.

## YAML Output Format
<!-- Lines 207-233 -->

The tree output is **valid YAML** — containment as nesting, metadata in comments, edges as `~`-prefixed keys. See **[TREE_FORMAT.md](TREE_FORMAT.md)** for the full specification and real-world examples.

```yaml
focus: sample_project.models.User.validate

sample_project:  # package  sample_project:1-1
  models:  # module  sample_project/models.py:1-50
    User:  # class  class User  sample_project/models.py:10-40
      validate:  # [FOCUS]  method  def validate(self) -> bool  sample_project/models.py:21-23
        ~calls:
          - sample_project.utils.check_email
  utils:  # module  sample_project/utils.py:1-30
check_email:  # function  def check_email(email: str) -> bool  sample_project/utils.py:5-15
  ~called_by:
    - sample_project.models.User.validate
```

SQLite-specific snapshot example:

- [`examples/sqlite_minimal/focus_users.yaml`](examples/sqlite_minimal/focus_users.yaml)

Worked example generated from codemap's own source (see [TREE_FORMAT.md](TREE_FORMAT.md#worked-example)):

- [`examples/self/context_codemap_build.yaml`](examples/self/context_codemap_build.yaml)
- [`examples/self/codemap_self.graphml`](examples/self/codemap_self.graphml)

## Project Structure
<!-- Lines 236-268 -->

```text
documentation_tools/codemap/
├── src/codemap/
│   ├── __init__.py      # Public exports
│   ├── errors.py        # CodeMapError, ParseError, NodeNotFoundError
│   ├── graph.py         # CodeNode, CodeEdge, CodeGraph, enums
│   ├── parser.py        # Jedi+parso extraction: project → graph
│   ├── view.py          # V-shape context, expand/collapse, YAML rendering
│   ├── export_yed.py    # yEd-compatible GraphML export with visual styling
│   └── api.py           # CodeMap class — the 11 public methods
├── tests/
│   ├── conftest.py
│   ├── fixtures/sample_project/   # 4-file Python project for testing
│   ├── test_graph.py
│   ├── test_parser.py
│   ├── test_view.py
│   ├── test_api.py
│   └── test_export_yed.py
├── examples/
│   ├── sqlite_minimal/            # SQLite table/column YAML snapshot
│   │   ├── README.md
│   │   └── focus_users.yaml
│   └── self/                      # Worked example: codemap run on its own source
│       ├── context_codemap_build.yaml
│       ├── codemap_self.graphml
│       └── generate.sh
├── pyproject.toml
├── README.md
├── TREE_FORMAT.md                 # YAML tree format spec (for LLM sessions)
└── IMPLEMENTATION_PLAN.md
```

## Development
<!-- Lines 271-285 -->

```bash
# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=codemap --cov-report=term-missing

# Lint and format
ruff check src/ tests/ && ruff format src/ tests/

# Type check
mypy src/
```

## Architecture Decisions
<!-- Lines 288-299 -->

| Decision | Rationale |
| --- | --- |
| `qualified_name` as primary key | Meaningful, stable across rebuilds, human-readable. No UUIDs. |
| Frozen dataclasses for nodes/edges | Nodes and edges are data, not mutable state. Built once, queried many times. |
| View state separate from graph | Graph is fact (what the code is). View is perspective (what the agent sees). |
| YAML as the output contract | The YAML is what agents consume — it is the product, not an afterthought. |
| No incrementality in V0 | `build()` always parses from scratch. Fast enough for small-medium projects. |
| Jedi for V0 parsing | Single dependency covers both structure extraction and cross-file resolution. |
| Custom yEd export (no NetworkX) | yEd requires yWorks-specific XML extensions. Plain GraphML doesn't render colors, shapes, or groups. Hand-crafted XML avoids a heavy dependency. |
| Flat mode recommended for yEd | Nested groups break most yEd layout algorithms. Flat mode with CONTAINS edges preserves structure information while enabling auto-layout. |

## Why This Is a Separate Project
<!-- Lines 302-312 -->

Extracted from [IntentGraph](../../../intent_graph/) during implementation of code-generation agents. The Generator needs to *read* existing code structurally. The Extractor needs to *reverse-engineer* intent from code. Both need a representation that is richer than text, leaner than AST, and independent of intent.

```text
IntentGraph  (what the system should do)
    ↕  agents bridge this gap
CodeMap      (what the code actually is)
    ↕  Jedi (V0) / Tree-sitter (future)
Raw Source   (the bytes on disk)
```

## Next Steps
<!-- Lines 315-319 -->

1. **Integration test with IntentGraph agents** — Generator reads the graph, Extractor writes to IntentGraph via the graph
2. **Tree-sitter migration** — when multi-language support is needed
3. **Incremental updates** — when project size makes full rebuilds too slow

## References
<!-- Lines 322-323 -->

The [implementation plan](IMPLEMENTATION_PLAN.md) documents the schema, system design, and build order.
