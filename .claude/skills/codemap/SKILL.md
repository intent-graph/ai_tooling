---
name: codemap
description: >
  Reference for the codemap CLI — structural code graph for Python codebases.
  Use when navigating, searching, or visualizing Python code structure.
user-invocable: false
---

# codemap — Structural Code Graph

System-wide CLI. Installed via `uv tool install -e .` from `documentation_tools/codemap/`.
Parses a Python codebase into a navigable graph: modules, classes, functions, edges (calls, imports, inheritance).

## Commands

### overview — Project skeleton

```bash
codemap overview /path/to/project
```

Names and nesting only. Use for quick orientation before drilling in.

### search — Find nodes by name

```bash
codemap search /path/to/project "ClassName"
codemap search /path/to/project "parse"
```

Case-insensitive substring match. Returns matching node paths.

### context — V-shaped context for a focus node

```bash
codemap context /path/to/project pkg.module.ClassName
codemap context /path/to/project pkg.module.function_name
```

Shows ancestors (for orientation) + children (for detail) + edges (calls, imports).
The **V-shape**: go up to see where the node sits, go down to see what it contains.

Node paths use dot notation matching the Python module structure: `package.module.Class.method`.

### neighbors — Immediate connections

```bash
codemap neighbors /path/to/project pkg.module.ClassName
```

Direct connections only (no ancestor/descendant context).

### source — Print source code

```bash
codemap source /path/to/project pkg.module.ClassName
```

Prints the actual source code lines for a node.

### export-yed — yEd GraphML export

```bash
codemap export-yed /path/to/project
codemap export-yed /path/to/project -o output.graphml
```

Generates a yEd-compatible `.graphml` file for visual inspection.

---

## Common Mistakes

1. **Wrong path argument order**: The project path is always the **first** positional argument, pattern/node is **second**.
2. **Wrong node path format**: Use dot notation (`pkg.module.Class`), not file paths (`pkg/module.py:Class`).
3. **Missing project path**: Every command requires the project root as the first argument.
