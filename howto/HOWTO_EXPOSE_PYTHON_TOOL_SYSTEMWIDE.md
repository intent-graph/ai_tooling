# How to Expose a Python Tool System-Wide (for Humans, Agents, and Subagents)

When you build a Python CLI tool in a project, you need it callable from anywhere — by humans in a terminal, by AI agents in subprocesses. This document captures the pattern we use, why it works, and how to replicate it.

## Table of Contents

1. [The Problem](#the-problem) _(Lines 29-39)_
1. [The Solution: uv tool install -e](#the-solution-uv-tool-install--e) _(Lines 42-59)_
1. [Step-by-Step Recipe](#step-by-step-recipe) _(Lines 62-62)_
   1. [1. Create a pyproject.toml at the project root](#1-create-a-pyprojecttoml-at-the-project-root) _(Lines 65-92)_
   1. [2. Write the CLI module](#2-write-the-cli-module) _(Lines 95-110)_
   1. [3. Install system-wide](#3-install-system-wide) _(Lines 113-123)_
   1. [4. Verify](#4-verify) _(Lines 126-134)_
1. [What Happens When You Change Code](#what-happens-when-you-change-code) _(Lines 137-148)_
1. [Why Not pip install / symlink / wrapper script](#why-not-pip-install--symlink--wrapper-script) _(Lines 151-151)_
   1. [pip install -e (into system Python)](#pip-install--e-into-system-python) _(Lines 154-162)_
   1. [pip install -e (into a venv)](#pip-install--e-into-a-venv) _(Lines 165-167)_
   1. [Symlink to /usr/local/bin](#symlink-to-usrlocalbin) _(Lines 170-176)_
   1. [Wrapper shell script](#wrapper-shell-script) _(Lines 179-190)_
1. [Multiple Source Trees in One Package](#multiple-source-trees-in-one-package) _(Lines 193-223)_
1. [Reference: ig-tool](#reference-ig-tool) _(Lines 226-237)_



---

## The Problem
<!-- Lines 29-39 -->

A Python CLI tool that lives inside a project has three barriers to being "just callable":

1. **PYTHONPATH** — the tool imports from project packages. Without the right `PYTHONPATH`, `import mypackage` fails. Agents get this wrong constantly (11/22 failures in our test).
2. **Venv activation** — if deps are in a venv, you must activate it first. Subagents (Cursor Task tool, Claude Code, etc.) start fresh shells with no venv active.
3. **Path to the script** — the tool lives deep in the project tree (`agents_runtime/src/ig_agents/cli/`). Agents need to know the absolute path.

The result: agents write ad-hoc workarounds, waste tokens on failed imports, and often give up.

---

## The Solution: uv tool install -e
<!-- Lines 42-59 -->

`uv tool install --editable .` from your project root does three things:

1. **Creates a private venv** at `~/.local/share/uv/tools/<package>/` with all dependencies installed.
2. **Symlinks the CLI binary** to `~/.local/bin/<tool-name>`, which is on PATH.
3. **Editable install** — the private venv's package links back to your source tree on disk.

The result:

- **Any shell** (human, agent, subagent, CI) can call `my-tool <args>` without setup.
- **Code changes are live** — edit a `.py` file, the next invocation sees the change.
- **No system pollution** — deps live in the private venv, not in system Python.
- **No venv activation** — the binary is a real executable on PATH, not a script requiring a venv.

This is the same mechanism `pipx` provides, but faster and integrated with `uv`.

---

## Step-by-Step Recipe
<!-- Lines 62-62 -->

### 1. Create a pyproject.toml at the project root
<!-- Lines 65-92 -->

```toml
[project]
name = "my-project-tools"
version = "0.1.0"
dependencies = [
    "pydantic>=2.0,<3",
    "pyyaml>=6.0,<7",
]
requires-python = ">=3.11"

[project.scripts]
my-tool = "my_package.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/my_package"]
```

Key points:

- `[project.scripts]` defines the CLI entry point: `my-tool` calls `my_package.cli:main`.
- `[tool.hatch.build.targets.wheel] packages` tells hatchling where to find the source.
- Use hatchling (not setuptools) — it handles nested/multiple source dirs cleanly.

### 2. Write the CLI module
<!-- Lines 95-110 -->

```python
# src/my_package/cli.py
import argparse
import sys

def main() -> None:
    parser = argparse.ArgumentParser(prog="my-tool")
    # ... define subcommands ...
    args = parser.parse_args()
    # ... dispatch ...

if __name__ == "__main__":
    main()
```

### 3. Install system-wide
<!-- Lines 113-123 -->

```bash
cd my-project && uv tool install -e .
```

Output:

```
Installed 1 executable: my-tool
```

### 4. Verify
<!-- Lines 126-134 -->

```bash
which my-tool          # ~/.local/bin/my-tool
my-tool --help         # works from any directory
cd /tmp && my-tool ... # works from any directory
```

---

## What Happens When You Change Code
<!-- Lines 137-148 -->

| Change | Action needed |
|---|---|
| Edit any `.py` file | **Nothing.** Live immediately. |
| Add/remove a dependency in pyproject.toml | Re-run `uv tool install -e .` |
| Add a new `[project.scripts]` entry point | Re-run `uv tool install -e .` |
| Rename the `main()` function | Re-run `uv tool install -e .` |

The rule: **code changes are free. Metadata changes cost one re-install (~2 seconds).**

---

## Why Not pip install / symlink / wrapper script
<!-- Lines 151-151 -->

### pip install -e (into system Python)
<!-- Lines 154-162 -->

Modern macOS/Homebrew Python enforces PEP 668 ("externally managed environment"). `pip install` into system Python fails:

```
error: externally-managed-environment
```

You'd need `--break-system-packages` (ugly) or a dedicated venv (then not "system-wide").

### pip install -e (into a venv)
<!-- Lines 165-167 -->

Works, but the tool is only available when the venv is active. Subagents don't activate your venv.

### Symlink to /usr/local/bin
<!-- Lines 170-176 -->

```bash
ln -s /path/to/my-tool /usr/local/bin/my-tool
```

Works if the script handles PYTHONPATH internally. But it's a system-level side effect, not portable, and requires a wrapper script to resolve paths. Fragile.

### Wrapper shell script
<!-- Lines 179-190 -->

```bash
#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR/../../src"
exec python3 "$SCRIPT_DIR/cli.py" "$@"
```

Works but: requires system Python to have all deps installed, requires knowing the path to the script, and adds a layer of indirection. `uv tool install` does this automatically and better.

---

## Multiple Source Trees in One Package
<!-- Lines 193-223 -->

If your project has multiple packages (e.g., a core library and an agent layer), hatchling can point to all of them:

```toml
[tool.hatch.build.targets.wheel]
packages = [
    "lib/core/src/mycore",
    "lib/agents/src/myagents",
]
```

This creates a single installable package that includes both `mycore` and `myagents`. The CLI can import from either.

**Naming collision warning:** If an inner package already has its own `pyproject.toml` with the same `[project] name`, the root package must use a different name. The pip/metadata name and the importable Python module name are independent:

```toml
# Root pyproject.toml
[project]
name = "myproject-tools"  # pip name (must be unique)

[tool.hatch.build.targets.wheel]
packages = [
    "lib/core/src/mycore",     # import mycore  (unchanged)
    "lib/agents/src/myagents", # import myagents (unchanged)
]
```

The individual `pyproject.toml` files still work for local dev/testing. The root one is only for the system-wide install.

---

## Reference: ig-tool
<!-- Lines 226-237 -->

This is the pattern used by the IntentGraph project's `ig-tool` CLI:

- **Root pyproject.toml:** `intent_graph/pyproject.toml` (package name: `intentgraph-tools`)
- **Two source trees:** `src/src/intentgraph` + `agents_runtime/src/ig_agents`
- **Entry point:** `ig-tool = "ig_agents.cli:main"`
- **Install:** `cd intent_graph && uv tool install -e .`
- **Result:** `~/.local/bin/ig-tool` — callable from anywhere by humans, agents, and subagents

Tool catalog: `intent_graph/agents_runtime/TOOL_REGISTRY.md`

The full test showed: 6 subcommands, 20+ flags, all working from `/tmp` with zero configuration. Agent failure rate for tool invocation dropped from 50% (PYTHONPATH-based) to 0% (system-wide binary).
