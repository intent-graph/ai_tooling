# CodeMap V0 — Implementation Plan

## Derivation Pipeline Position
<!-- Lines 5-7 -->

This plan follows the rough-to-fine derivation pipeline. Steps 1-2 (Usage, Data Flow) are captured in the [README](README.md). This document covers steps 3-6: Schema, System Design, Implementation Strategy, and Tactical Coding.

## 1. Data Architecture (The Schema)
<!-- Lines 10-12 -->

Data model first. If these types are right, even mediocre code produces a maintainable system.

### 1.1 Node Types
<!-- Lines 15-28 -->

Nodes represent units of code at any level. The hierarchy is open — not locked to a 5-tier OOP taxonomy. Functions can contain functions; modules can contain bare functions without classes.

```python
class NodeKind(Enum):
    PACKAGE = "package"       # directory with __init__.py
    MODULE = "module"         # .py file
    CLASS = "class"
    FUNCTION = "function"     # top-level or nested
    METHOD = "method"         # inside a class
```

Future: `VARIABLE`, `CONSTANT`, `BASH_FUNCTION` can be added without breaking anything.

### 1.2 Node Schema
<!-- Lines 31-49 -->

```python
@dataclass(frozen=True)
class CodeNode:
    qualified_name: str         # unique ID: "mypackage.module.MyClass.method"
    name: str                   # short name: "method"
    kind: NodeKind
    path: str                   # file path relative to project root
    line_start: int
    line_end: int
    signature: str | None       # "def method(self, x: int) -> bool" or None
    docstring: str | None       # first line only, for compactness
    parent: str | None          # qualified_name of containing node (None for root)
```

- `frozen=True` — nodes are immutable data, not mutable state
- `qualified_name` is the primary key — no UUIDs, no artificial IDs
- `parent` encodes the containment tree directly in the node

### 1.3 Edge Types
<!-- Lines 52-60 -->

```python
class EdgeKind(Enum):
    CONTAINS = "contains"       # structural: module contains class, class contains method
    CALLS = "calls"             # method/function calls another
    IMPORTS = "imports"         # module imports from another module
    INHERITS = "inherits"       # class inherits from another class
```

### 1.4 Edge Schema
<!-- Lines 63-73 -->

```python
@dataclass(frozen=True)
class CodeEdge:
    source: str                 # qualified_name of source node
    target: str                 # qualified_name of target node
    kind: EdgeKind
```

No edge UIDs. An edge is identified by its (source, target, kind) triple.

### 1.5 Graph Schema
<!-- Lines 76-91 -->

```python
@dataclass
class CodeGraph:
    root: str                               # project root path
    nodes: dict[str, CodeNode]              # keyed by qualified_name
    edges: list[CodeEdge]

    # Derived indexes (built once after parsing, not serialized)
    _children: dict[str, list[str]]         # parent -> [child qualified_names]
    _edges_from: dict[str, list[CodeEdge]]  # source -> [edges]
    _edges_to: dict[str, list[CodeEdge]]    # target -> [edges]
```

Indexes are derived from the primary data, never stored separately. Rebuilt on construction.

### 1.6 View State
<!-- Lines 94-111 -->

The view is a mutable selection on top of an immutable graph. Separate concerns: the graph is fact; the view is perspective.

```python
@dataclass
class ViewState:
    graph: CodeGraph                        # reference to the underlying graph
    visible: set[str]                       # qualified_names currently in view
    detail_level: dict[str, DetailLevel]    # per-node: NAMES_ONLY, SIGNATURE, FULL
```

```python
class DetailLevel(Enum):
    NAMES_ONLY = "names_only"     # just the name, no signature or docstring
    SIGNATURE = "signature"       # name + signature
    FULL = "full"                 # name + signature + docstring + line range + edges
```

## 2. System Design
<!-- Lines 114-114 -->

### 2.1 Module Boundaries
<!-- Lines 117-143 -->

Four modules. Dependency flows one direction: right depends on left, never the reverse.

```
graph.py  ←  parser.py
   ↑
   |
view.py  ←  api.py
   |             ↑
   +--  export_yed.py
```

| Module | Responsibility | Depends on |
| --- | --- | --- |
| `graph.py` | Data model: CodeNode, CodeEdge, CodeGraph, NodeKind, EdgeKind | Nothing |
| `parser.py` | Jedi-based extraction: project path → CodeGraph | `graph` |
| `view.py` | View state: V-shape context, expand, collapse, include, exclude, YAML serialization | `graph` |
| `export_yed.py` | yEd-compatible GraphML export with visual styling | `graph` |
| `api.py` | Public API: the 11 functions agents call. Thin orchestration layer. | `graph`, `parser`, `view`, `export_yed` |

Plus:

| Module | Responsibility |
| --- | --- |
| `errors.py` | Domain exceptions |
| `__init__.py` | Public re-exports, `__all__`, `__version__` |

### 2.2 Data Flow
<!-- Lines 146-170 -->

```
Project path (str)
    ↓
parser.parse_project(path)
    ↓  walks directories, calls Jedi per file
CodeGraph (nodes + edges + indexes)
    ↓
view.build_context(graph, focus_node)
    ↓  computes V-shape: wide brim + spine + ground bar
ViewState (visible set + detail levels)
    ↓
view.render_yaml(view_state)
    ↓
YAML string → agent
```

Source retrieval is a bypass — reads lines directly from files using node's path + line range:

```
agent calls codemap.source(node)
    → reads node.path lines[node.line_start:node.line_end]
    → returns raw source string
```

### 2.3 Error Strategy
<!-- Lines 173-186 -->

```python
class CodeMapError(Exception):
    """Base exception for all CodeMap operations."""

class ParseError(CodeMapError):
    """Raised when a file cannot be parsed."""

class NodeNotFoundError(CodeMapError):
    """Raised when a qualified_name doesn't exist in the graph."""
```

Fail fast at boundaries (bad path, missing file, unparseable syntax). Never silently swallow errors. Error messages include what went wrong, where, and what to do.

### 2.4 YAML Serialization Design
<!-- Lines 189-243 -->

The YAML output is the product. It must be immediately graspable by an agent. Design it as carefully as the data model.

**Overview output** (names and nesting only):

```yaml
project: my_project
modules:
  - my_project.main
  - my_project.utils
  - my_project.models
    classes:
      - my_project.models.User
      - my_project.models.Order
```

**Context output** (V-shaped):

```yaml
focus: my_project.models.User.validate
# --- wide brim: top-level orientation ---
top_level:
  - my_project.main
  - my_project.utils
  - my_project.models
# --- vertical spine: lineage to focus ---
lineage:
  - name: my_project.models
    kind: module
    signature: null
  - name: my_project.models.User
    kind: class
    signature: "class User"
# --- ground bar: focus + neighbors ---
focus_node:
  name: validate
  kind: method
  qualified_name: my_project.models.User.validate
  signature: "def validate(self, data: dict) -> bool"
  docstring: "Validate user data against schema."
  path: src/my_project/models.py
  lines: [45, 67]
neighbors:
  calls:
    - name: check_email
      qualified_name: my_project.utils.check_email
      signature: "def check_email(email: str) -> bool"
  imports:
    - name: Schema
      qualified_name: my_project.models.Schema
  inherits: []
```

This format is the contract between CodeMap and the agents. Design it, test it on a real example, iterate before hardcoding.

## 3. Implementation Strategy
<!-- Lines 246-246 -->

### 3.1 Implementation Order
<!-- Lines 249-264 -->

Build bottom-up through the dependency chain. Each step has its own tests before moving to the next.

| Step | Module | What to build | Test with |
| --- | --- | --- | --- |
| **S1** | `errors.py` | Exception hierarchy | Trivial — just class definitions |
| **S2** | `graph.py` | CodeNode, CodeEdge, CodeGraph, enums, index builder | Unit: create nodes/edges, verify indexes, query children/edges |
| **S3** | `parser.py` | Jedi-based extraction for a single file | Parse a small `.py` fixture, assert expected nodes and edges |
| **S4** | `parser.py` | Extend to multi-file project (walk directories) | Parse a test project with 3-4 files, verify cross-file edges |
| **S5** | `view.py` | V-shape context builder | Given a graph + focus node, verify correct wide brim, spine, ground bar |
| **S6** | `view.py` | expand / collapse / include / exclude | Mutate view state, verify visible set changes correctly |
| **S7** | `view.py` | YAML serialization | Render a view to YAML, verify format matches spec |
| **S8** | `api.py` | Wire all 10 public functions | Integration: build → overview → search → context → expand → source |
| **S9** | Polish | Docstrings, `__init__.py`, `__all__`, edge cases | Full test suite passes, mypy strict passes, ruff clean |
| **S10** | `export_yed.py` | yEd GraphML export: flat/grouped modes, color-coded nodes/edges, depth/kind/qname metadata | Export a graph, open in yEd, verify visual styling and layout |

### 3.2 Test Fixtures
<!-- Lines 267-279 -->

Create a small Python project as a test fixture:

```
tests/fixtures/sample_project/
├── __init__.py
├── main.py          # imports from models, calls functions
├── models.py        # classes with methods, inheritance
└── utils.py         # standalone functions, called by models
```

This fixture exercises: packages, modules, classes, methods, functions, imports, calls, inheritance.

### 3.3 Development Rhythm
<!-- Lines 282-292 -->

Per the guidelines:

1. Pick a step from the table above
2. Write a failing test for the step's capability
3. Implement until test passes
4. Write/update docstrings
5. Run `ruff check . && ruff format . && mypy src/ && pytest`
6. Commit
7. Next step

## 4. Project Setup
<!-- Lines 295-295 -->

### 4.1 Directory Layout
<!-- Lines 298-336 -->

```
documentation_tools/codemap/
├── src/
│   └── codemap/
│       ├── __init__.py
│       ├── errors.py
│       ├── graph.py
│       ├── parser.py
│       ├── view.py
│       ├── export_yed.py
│       └── api.py
├── tests/
│   ├── conftest.py
│   ├── fixtures/
│   │   └── sample_project/
│   │       ├── __init__.py
│   │       ├── main.py
│   │       ├── models.py
│   │       └── utils.py
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
├── IMPLEMENTATION_PLAN.md
└── .gitignore
```

### 4.2 pyproject.toml
<!-- Lines 339-377 -->

```toml
[project]
name = "codemap"
version = "0.1.0"
description = "Structural code graph for AI agent reasoning"
requires-python = ">=3.11"
dependencies = [
    "jedi>=0.19,<1.0",
    "pyyaml>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov",
    "ruff>=0.1",
    "mypy>=1.0",
    "types-PyYAML",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/codemap"]

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "UP"]

[tool.mypy]
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### 4.3 Dependencies
<!-- Lines 380-387 -->

| Dependency | Why | Range |
| --- | --- | --- |
| `jedi` | Structure extraction + cross-file symbol resolution | `>=0.19,<1.0` |
| `pyyaml` | YAML serialization for agent-readable output | `>=6.0` |

Two runtime dependencies. That's it. Every additional dependency must pass the Articulation Test.

## 5. Key Design Decisions (ADRs)
<!-- Lines 390-390 -->

### ADR-1: qualified_name as primary key (not UUID)
<!-- Lines 393-399 -->

**Decision:** Nodes are identified by their Python qualified name (`package.module.Class.method`), not by generated UUIDs.

**Why:** Qualified names are meaningful, stable across rebuilds, and human-readable. Agents can refer to nodes by name. UUIDs add indirection with no benefit for a read-only graph that rebuilds from scratch.

**Trade-off:** If two symbols share a qualified name (unlikely in Python), this breaks. Acceptable for V0.

### ADR-2: Frozen dataclasses for nodes and edges
<!-- Lines 402-406 -->

**Decision:** `CodeNode` and `CodeEdge` are `frozen=True` dataclasses.

**Why:** Nodes and edges are data, not mutable state. The graph is built once by the parser and then queried. Immutability prevents accidental mutation and makes the data hashable.

### ADR-3: View state is separate from graph
<!-- Lines 409-413 -->

**Decision:** `ViewState` is a mutable object that references an immutable `CodeGraph`.

**Why:** The graph is fact (what the code is). The view is perspective (what the agent sees right now). Mixing them conflates two concerns. Agents can create multiple views on the same graph.

### ADR-4: YAML format is the contract
<!-- Lines 416-420 -->

**Decision:** The YAML output format is designed and tested as a first-class artifact, not an afterthought.

**Why:** The YAML is what agents actually consume. It is the product. The internal data model serves the YAML, not the other way around.

### ADR-5: No incrementality in V0
<!-- Lines 423-427 -->

**Decision:** `build()` always parses the full project from scratch.

**Why:** Jedi is fast enough for medium projects. Adding incremental updates adds complexity (cache invalidation, state management) with no proven need yet. Measure first, optimize if needed.

## 6. Risks and Open Questions
<!-- Lines 430-438 -->

| Risk | Mitigation |
| --- | --- |
| Jedi may be slow on large projects (1000+ files) | V0 targets small-medium projects. Measure. Tree-sitter migration path exists. |
| Jedi's `get_names()` may not surface all relationships we need | Spike S3 early. If Jedi's API is insufficient, consider `ast` module for structure + Jedi only for resolution. |
| YAML format may not be agent-friendly in practice | Test the format with a real agent workflow before committing. Iterate on the YAML spec in S7. |
| `qualified_name` collisions in edge cases | Accept for V0. Add disambiguation if it occurs in practice. |
| Bash function support | Deferred. Jedi doesn't parse bash. Will need a separate parser (probably regex or bash AST). Out of scope for V0 core. |

## 7. Success Criteria
<!-- Lines 441-451 -->

V0 is done when:

1. `codemap.build(path)` parses a real Python project into a graph
2. `codemap.overview()` returns a readable YAML skeleton
3. `codemap.context(node)` returns a V-shaped context that an IntentGraph agent can consume
4. `codemap.source(node)` returns the correct source lines
5. All 11 API functions work end-to-end (including `export_yed`)
6. Test suite passes, mypy strict passes, ruff clean
7. An IntentGraph agent (Generator or Extractor) successfully uses CodeMap in a real task
8. yEd export produces valid GraphML with proper visual styling (nodes color-coded by kind, edges styled by kind)
