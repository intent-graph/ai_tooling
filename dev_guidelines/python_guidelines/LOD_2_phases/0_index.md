# 0 Phases Index

> All lifecycle phases organized by stage.

## Table of Contents

1. [Overview](#overview) _(Lines 28-43)_
1. [Phase Index by Stage](#phase-index-by-stage) _(Lines 46-46)_
   1. [Stage 1: Understand](#stage-1-understand) _(Lines 49-54)_
   1. [Stage 2: Setup](#stage-2-setup) _(Lines 57-62)_
   1. [Stage 3: Build](#stage-3-build) _(Lines 65-71)_
   1. [Stage 4: Ship](#stage-4-ship) _(Lines 74-80)_
   1. [Stage 5: Operate](#stage-5-operate) _(Lines 83-89)_
   1. [Stage 6: Evolve](#stage-6-evolve) _(Lines 92-97)_
   1. [Stage 7: Specialize](#stage-7-specialize) _(Lines 100-106)_
1. [Quick Reference](#quick-reference) _(Lines 109-109)_
   1. [By Task](#by-task) _(Lines 112-132)_
   1. [By Content Type](#by-content-type) _(Lines 135-146)_
1. [Navigation](#navigation) _(Lines 149-149)_
   1. [Upward: To Stages](#upward-to-stages) _(Lines 152-162)_
   1. [Downward: To Domains](#downward-to-domains) _(Lines 165-177)_


---

## Overview
<!-- Lines 28-43 -->

LOD_2 contains **17 lifecycle phases**, each providing detailed treatment of a specific aspect of development. Phases are organized under their parent stage.

**Key Characteristics:**
- **Full prose:** Complete guidance for each phase
- **Self-contained:** Each phase file can be read independently
- **Cross-linked:** References to related phases and LOD_3 domains
- **Actionable:** Provides concrete guidance, not just principles

**When to Use LOD_2:**
- You know which stage you're in and need detailed guidance
- You need to understand a specific lifecycle phase
- You want to drill down to specific topics (LOD_3)

---

## Phase Index by Stage
<!-- Lines 46-46 -->

### Stage 1: Understand
<!-- Lines 49-54 -->

| Phase | File | Purpose |
|-------|------|---------|
| 1.1 | [1.1_requirements.md](1.1_requirements.md) | Requirements gathering, decomposition, scope |
| 1.2 | [1.2_design.md](1.2_design.md) | Data modeling, architecture, interfaces |

### Stage 2: Setup
<!-- Lines 57-62 -->

| Phase | File | Purpose |
|-------|------|---------|
| 2.1 | [2.1_environment.md](2.1_environment.md) | Python installation, virtualenvs, tools |
| 2.2 | [2.2_project_structure.md](2.2_project_structure.md) | Directory layout, modules, config files |

### Stage 3: Build
<!-- Lines 65-71 -->

| Phase | File | Purpose |
|-------|------|---------|
| 3.1 | [3.1_implementation.md](3.1_implementation.md) | Naming, typing, functions, classes, idioms |
| 3.2 | [3.2_testing.md](3.2_testing.md) | Unit, integration, fixtures, coverage |
| 3.3 | [3.3_documentation.md](3.3_documentation.md) | Docstrings, README, API docs, guides |

### Stage 4: Ship
<!-- Lines 74-80 -->

| Phase | File | Purpose |
|-------|------|---------|
| 4.1 | [4.1_packaging.md](4.1_packaging.md) | pyproject.toml, dependencies, publishing |
| 4.2 | [4.2_quality.md](4.2_quality.md) | Linting, formatting, type checking, CI |
| 4.3 | [4.3_deployment.md](4.3_deployment.md) | Containers, monitoring, health checks |

### Stage 5: Operate
<!-- Lines 83-89 -->

| Phase | File | Purpose |
|-------|------|---------|
| 5.1 | [5.1_performance.md](5.1_performance.md) | Profiling, optimization, concurrency, async |
| 5.2 | [5.2_security.md](5.2_security.md) | Secrets, validation, auditing, secure coding |
| 5.3 | [5.3_debugging.md](5.3_debugging.md) | Debugging strategies, logging, tracing |

### Stage 6: Evolve
<!-- Lines 92-97 -->

| Phase | File | Purpose |
|-------|------|---------|
| 6.1 | [6.1_iteration.md](6.1_iteration.md) | Refactoring, tech debt, deprecation |
| 6.2 | [6.2_collaboration.md](6.2_collaboration.md) | Code review, version control, conventions |

### Stage 7: Specialize
<!-- Lines 100-106 -->

| Phase | File | Purpose |
|-------|------|---------|
| 7.1 | [7.1_scenarios.md](7.1_scenarios.md) | CLI, web, API, data pipelines, libraries |

---

## Quick Reference
<!-- Lines 109-109 -->

### By Task
<!-- Lines 112-132 -->

| I need to... | Go to |
|--------------|-------|
| Write a problem statement | [1.1 Requirements](1.1_requirements.md) |
| Design data models | [1.2 Design](1.2_design.md) |
| Set up pyenv/venv | [2.1 Environment](2.1_environment.md) |
| Choose project layout | [2.2 Project Structure](2.2_project_structure.md) |
| Name variables/functions | [3.1 Implementation](3.1_implementation.md) |
| Add type hints | [3.1 Implementation](3.1_implementation.md) |
| Write pytest tests | [3.2 Testing](3.2_testing.md) |
| Write docstrings | [3.3 Documentation](3.3_documentation.md) |
| Configure pyproject.toml | [4.1 Packaging](4.1_packaging.md) |
| Set up ruff/black | [4.2 Quality](4.2_quality.md) |
| Create Dockerfile | [4.3 Deployment](4.3_deployment.md) |
| Profile slow code | [5.1 Performance](5.1_performance.md) |
| Handle secrets | [5.2 Security](5.2_security.md) |
| Configure logging | [5.3 Debugging](5.3_debugging.md) |
| Refactor safely | [6.1 Iteration](6.1_iteration.md) |
| Review PRs | [6.2 Collaboration](6.2_collaboration.md) |
| Build a CLI | [7.1 Scenarios](7.1_scenarios.md) |

### By Content Type
<!-- Lines 135-146 -->

| Content | Phases |
|---------|--------|
| Code patterns | 3.1, 5.1, 5.2 |
| Configuration | 2.1, 2.2, 4.1, 4.2 |
| Testing | 3.2 |
| Documentation | 3.3 |
| DevOps/CI | 4.2, 4.3 |
| Process/Workflow | 6.1, 6.2 |

---

## Navigation
<!-- Lines 149-149 -->

### Upward: To Stages
<!-- Lines 152-162 -->

| Phase | Parent Stage |
|-------|--------------|
| 1.1, 1.2 | [1 Understand](../LOD_1_stages/1_understand.md) |
| 2.1, 2.2 | [2 Setup](../LOD_1_stages/2_setup.md) |
| 3.1, 3.2, 3.3 | [3 Build](../LOD_1_stages/3_build.md) |
| 4.1, 4.2, 4.3 | [4 Ship](../LOD_1_stages/4_ship.md) |
| 5.1, 5.2, 5.3 | [5 Operate](../LOD_1_stages/5_operate.md) |
| 6.1, 6.2 | [6 Evolve](../LOD_1_stages/6_evolve.md) |
| 7.1 | [7 Specialize](../LOD_1_stages/7_specialize.md) |

### Downward: To Domains
<!-- Lines 165-177 -->

Each phase expands into multiple LOD_3 domain files. See the [LOD_3 Domains Index](../LOD_3_domains/0_index.md) for the full listing, or individual phase files for specific domain links.

**Example:** 3.1 Implementation → LOD_3 domains:
- 3.1.1 Naming
- 3.1.2 Typing
- 3.1.3 Functions
- ... (9 total)

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages](../LOD_1_stages/0_index.md)
- ↓ Children: [LOD_3 Domains](../LOD_3_domains/0_index.md) (78 files)
- → Related: [../README.md](../README.md)
