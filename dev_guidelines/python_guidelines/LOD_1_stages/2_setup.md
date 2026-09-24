# 2 Setup

> Prepare the development environment and project foundation.

## Table of Contents

1. [Stage Overview](#stage-overview) _(Lines 37-39)_
   1. [Why Setup Matters](#why-setup-matters) _(Lines 42-44)_
   1. [What Happens Here](#what-happens-here) _(Lines 47-52)_
   1. [Entry Criteria](#entry-criteria) _(Lines 55-61)_
   1. [Exit Criteria](#exit-criteria) _(Lines 64-77)_
1. [Environment Phase](#environment-phase) _(Lines 80-82)_
   1. [Python Installation](#python-installation) _(Lines 85-107)_
   1. [Virtual Environments](#virtual-environments) _(Lines 110-133)_
   1. [Development Tools](#development-tools) _(Lines 136-155)_
   1. [IDE Configuration](#ide-configuration) _(Lines 158-175)_
   1. [Environment Variables](#environment-variables) _(Lines 178-203)_
1. [Project Structure Phase](#project-structure-phase) _(Lines 206-208)_
   1. [Choosing a Layout](#choosing-a-layout) _(Lines 211-245)_
   1. [Module Organization](#module-organization) _(Lines 248-285)_
   1. [Configuration Files](#configuration-files) _(Lines 288-323)_
   1. [Entry Points](#entry-points) _(Lines 326-343)_
   1. [Standard Files](#standard-files) _(Lines 346-360)_
1. [Stage Checklist](#stage-checklist) _(Lines 363-365)_
   1. [Environment Checklist](#environment-checklist) _(Lines 368-375)_
   1. [Project Structure Checklist](#project-structure-checklist) _(Lines 378-385)_
   1. [Tool Configuration Checklist](#tool-configuration-checklist) _(Lines 388-394)_
   1. [Quick Verification](#quick-verification) _(Lines 397-415)_
   1. [Red Flags](#red-flags) _(Lines 418-427)_
1. [Navigation](#navigation) _(Lines 430-436)_


---

## Stage Overview
<!-- Lines 37-39 -->

The Setup stage establishes the **foundation** on which everything else is built. A well-set-up project makes development smooth; a poorly-set-up project creates friction forever.

### Why Setup Matters
<!-- Lines 42-44 -->

Setup decisions persist. The directory structure you create today, the tools you configure, the conventions you establish—these will be with you for the project's lifetime. Getting them right upfront is far easier than changing them later.

### What Happens Here
<!-- Lines 47-52 -->

This stage has two phases:

1. **Environment (2.1):** Installing Python, creating virtual environments, configuring tools
2. **Project Structure (2.2):** Directory layout, module organization, configuration files

### Entry Criteria
<!-- Lines 55-61 -->

You enter this stage when:
- Starting a new project (after Understand)
- Joining an existing project (environment setup only)
- Upgrading Python version or tooling
- Restructuring an existing project

### Exit Criteria
<!-- Lines 64-77 -->

You exit this stage when:
- Python and dependencies are installed and isolated
- Development tools are configured (linter, formatter, type checker)
- Project structure is created
- You can run `python -c "import myproject"` successfully
- Basic tooling commands work (`pytest`, `ruff check`, etc.)

**Philosophy connections:**
- [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md) — Environment isolation ensures consistency
- [0.2 Structure Primacy](../LOD_0_philosophy/0.2_structure_primacy.md) — Project structure reflects design

---

## Environment Phase
<!-- Lines 80-82 -->

Environment setup ensures **everyone works with the same tools**.

### Python Installation
<!-- Lines 85-107 -->

Use a Python version manager to install and switch between versions:

```bash
# Install pyenv (macOS/Linux)
curl https://pyenv.run | bash

# Install specific Python version
pyenv install 3.11.7

# Set project-local version
cd myproject
pyenv local 3.11.7

# Verify
python --version  # Python 3.11.7
```

**Version selection:**
- Use the latest stable release for new projects
- Match production Python version exactly
- Document the required version in `pyproject.toml`

### Virtual Environments
<!-- Lines 110-133 -->

**Always use virtual environments.** Never install packages globally.

```bash
# Create virtual environment
python -m venv .venv

# Activate (Unix/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Verify isolation
which python  # Should show .venv/bin/python
pip list      # Should show minimal packages
```

**Why virtual environments:**
- Isolate project dependencies
- Avoid version conflicts between projects
- Match production environment
- Enable reproducible builds

### Development Tools
<!-- Lines 136-155 -->

Install and configure essential tools:

```bash
# Install development dependencies
pip install ruff mypy pytest pytest-cov

# Or use a dependency group
pip install -e ".[dev]"
```

**Essential tools:**

| Tool | Purpose | Config File |
|------|---------|-------------|
| ruff | Linting + formatting | `pyproject.toml` |
| mypy | Type checking | `pyproject.toml` |
| pytest | Testing | `pyproject.toml` |
| pre-commit | Git hooks | `.pre-commit-config.yaml` |

### IDE Configuration
<!-- Lines 158-175 -->

Configure your IDE to use the virtual environment:

**VS Code (`.vscode/settings.json`):**
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.analysis.typeCheckingMode": "basic",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff"
    }
}
```

**PyCharm:**
- Settings → Project → Python Interpreter → Add → Existing Environment → Select `.venv/bin/python`

### Environment Variables
<!-- Lines 178-203 -->

Document required environment variables:

```bash
# .env.example (commit this)
DATABASE_URL=postgresql://user:pass@localhost/dbname
SECRET_KEY=your-secret-key-here
DEBUG=true
```

```python
# config.py - Load at startup
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
```

**Cross-ref:** → [2.1 Environment](../LOD_2_phases/2.1_environment.md) for detailed guidance

---

## Project Structure Phase
<!-- Lines 206-208 -->

Project structure determines **how code is organized**.

### Choosing a Layout
<!-- Lines 211-245 -->

Two main options:

**Flat layout** (simple projects):
```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── README.md
```

**Src layout** (recommended for packages):
```
myproject/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── README.md
```

**Src layout benefits:**
- Prevents accidental imports from project root
- Forces you to install the package to test it
- Matches how users will install and import

### Module Organization
<!-- Lines 248-285 -->

Organize modules by **domain** or **layer**:

**By domain (feature-based):**
```
src/myproject/
├── users/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── routes.py
├── orders/
│   ├── __init__.py
│   ├── models.py
│   ├── services.py
│   └── routes.py
└── shared/
    └── database.py
```

**By layer (technical):**
```
src/myproject/
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── order.py
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   └── order_service.py
├── routes/
│   └── ...
└── database.py
```

**Guidance:** Domain-based for large applications; layer-based for smaller projects.

### Configuration Files
<!-- Lines 288-323 -->

Every Python project needs `pyproject.toml`:

```toml
[project]
name = "myproject"
version = "0.1.0"
description = "A short description"
requires-python = ">=3.11"
dependencies = [
    "httpx>=0.24",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1",
    "mypy>=1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 88
select = ["E", "F", "I", "UP"]

[tool.mypy]
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Entry Points
<!-- Lines 326-343 -->

Define how the application is launched:

**CLI entry point:**
```toml
[project.scripts]
myproject = "myproject.cli:main"
```

**`__main__.py` for `python -m myproject`:**
```python
# src/myproject/__main__.py
from myproject.cli import main

if __name__ == "__main__":
    main()
```

### Standard Files
<!-- Lines 346-360 -->

Every project should have:

| File | Purpose |
|------|---------|
| `README.md` | Project overview, installation, usage |
| `pyproject.toml` | Project metadata, dependencies, tool config |
| `.gitignore` | Files to exclude from git |
| `.python-version` | Python version (for pyenv) |
| `LICENSE` | Legal terms |

**Cross-ref:** → [2.2 Project Structure](../LOD_2_phases/2.2_project_structure.md) for detailed guidance

---

## Stage Checklist
<!-- Lines 363-365 -->

Before leaving the Setup stage, verify:

### Environment Checklist
<!-- Lines 368-375 -->

- [ ] Python version is installed and documented
- [ ] Virtual environment is created and activated
- [ ] Development dependencies are installed
- [ ] IDE is configured to use virtual environment
- [ ] Environment variables are documented (`.env.example`)
- [ ] `.gitignore` excludes `.venv/`, `__pycache__/`, `.env`

### Project Structure Checklist
<!-- Lines 378-385 -->

- [ ] Directory layout is chosen (flat or src)
- [ ] `pyproject.toml` is configured
- [ ] Package is installable (`pip install -e .`)
- [ ] Import works (`python -c "import myproject"`)
- [ ] Entry points are configured (if CLI)
- [ ] Test directory exists and pytest runs

### Tool Configuration Checklist
<!-- Lines 388-394 -->

- [ ] Linter is configured and runs cleanly (`ruff check .`)
- [ ] Formatter is configured (`ruff format .`)
- [ ] Type checker is configured (`mypy src/`)
- [ ] Tests run (`pytest`)
- [ ] Pre-commit hooks are configured (optional but recommended)

### Quick Verification
<!-- Lines 397-415 -->

Run these commands—all should succeed:

```bash
# Environment
python --version         # Correct version
pip list                 # Shows project dependencies

# Project
pip install -e ".[dev]"  # Install succeeds
python -c "import myproject"  # Import works

# Tools
ruff check .             # No errors (or expected ones)
ruff format --check .    # Formatted correctly
mypy src/                # No type errors
pytest                   # Tests pass
```

### Red Flags
<!-- Lines 418-427 -->

Stop and fix if:

- **Using system Python** — Create a virtual environment
- **`pip install` without virtualenv** — Activate the venv first
- **Import errors** — Check `__init__.py` and project structure
- **"Works on my machine"** — Environment isn't reproducible

---

## Navigation
<!-- Lines 430-436 -->

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages Index](0_index.md)
- ↑ Philosophy: [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md), [0.2 Structure Primacy](../LOD_0_philosophy/0.2_structure_primacy.md)
- ← Previous Stage: [1 Understand](1_understand.md)
- → Next Stage: [3 Build](3_build.md)
- ↓ Child Phases: [2.1 Environment](../LOD_2_phases/2.1_environment.md), [2.2 Project Structure](../LOD_2_phases/2.2_project_structure.md)
