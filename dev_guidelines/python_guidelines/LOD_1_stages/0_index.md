# 0 Stages Index

> High-level development stages from problem to production.

## Table of Contents

1. [Overview](#overview) _(Lines 23-39)_
1. [Stage Flow](#stage-flow) _(Lines 42-42)_
   1. [The Development Pipeline](#the-development-pipeline) _(Lines 45-68)_
   1. [Stage Transitions](#stage-transitions) _(Lines 71-81)_
   1. [Common Entry Points](#common-entry-points) _(Lines 84-95)_
1. [Stage Index](#stage-index) _(Lines 98-108)_
   1. [Quick Reference by Task](#quick-reference-by-task) _(Lines 111-132)_
1. [Navigation Guide](#navigation-guide) _(Lines 135-135)_
   1. [Upward: To Philosophy](#upward-to-philosophy) _(Lines 138-150)_
   1. [Downward: To Phases](#downward-to-phases) _(Lines 153-169)_


---

## Overview
<!-- Lines 23-39 -->

LOD_1 organizes the development lifecycle into **7 intuitive stages**. Each stage represents a distinct phase of work with clear inputs and outputs.

**Key Characteristics:**
- **Non-linear:** Stages can be entered at any point
- **Iterative:** You will revisit stages as the project evolves
- **Entry point:** Most users start navigation here
- **Bridges up and down:** Links to LOD_0 philosophy and LOD_2 phases

**When to Use LOD_1:**
- Finding where you are in the development process
- Understanding what comes next
- Navigating to detailed guidance (LOD_2+)
- Onboarding to a project phase

---

## Stage Flow
<!-- Lines 42-42 -->

### The Development Pipeline
<!-- Lines 45-68 -->

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 1 UNDERSTAND│ ──► │  2 SETUP    │ ──► │  3 BUILD    │
│ Requirements│     │ Environment │     │ Implement   │
│ Design      │     │ Structure   │     │ Test, Doc   │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
       ┌──────────────────────────────────────┘
       ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   4 SHIP    │ ──► │  5 OPERATE  │ ──► │  6 EVOLVE   │
│ Package     │     │ Performance │     │ Iterate     │
│ Quality, CI │     │ Security    │     │ Collaborate │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ 7 SPECIALIZE│
                    │ CLI, Web,   │
                    │ API, etc.   │
                    └─────────────┘
```

### Stage Transitions
<!-- Lines 71-81 -->

| From | To | Trigger |
|------|-----|---------|
| 1 Understand | 2 Setup | Requirements clear, design approved |
| 2 Setup | 3 Build | Environment ready, structure in place |
| 3 Build | 4 Ship | Code complete, tests passing |
| 4 Ship | 5 Operate | Deployed to production |
| 5 Operate | 6 Evolve | Production stable, feedback received |
| 6 Evolve | 1 Understand | New feature/major change |
| Any | 7 Specialize | Need app-type-specific guidance |

### Common Entry Points
<!-- Lines 84-95 -->

| Scenario | Start At |
|----------|----------|
| Greenfield project | Stage 1: Understand |
| Joining existing project | Stage 3: Build (after Stage 2 environment setup) |
| Bug fix | Stage 5: Operate → Stage 3: Build |
| Feature request | Stage 1: Understand |
| Release preparation | Stage 4: Ship |
| Tech debt sprint | Stage 6: Evolve |

---

## Stage Index
<!-- Lines 98-108 -->

| Stage | File | Purpose | Phases |
|-------|------|---------|--------|
| **1** | [1_understand.md](1_understand.md) | Define the problem before solving it | Requirements, Design |
| **2** | [2_setup.md](2_setup.md) | Prepare environment and structure | Environment, Project Structure |
| **3** | [3_build.md](3_build.md) | Write code, test it, document it | Implementation, Testing, Documentation |
| **4** | [4_ship.md](4_ship.md) | Package, validate, deploy | Packaging, Quality, Deployment |
| **5** | [5_operate.md](5_operate.md) | Optimize, secure, debug | Performance, Security, Debugging |
| **6** | [6_evolve.md](6_evolve.md) | Iterate and collaborate | Iteration, Collaboration |
| **7** | [7_specialize.md](7_specialize.md) | Application-specific guidance | CLI, Web, API, Data Pipelines, etc. |

### Quick Reference by Task
<!-- Lines 111-132 -->

| I need to... | Go to |
|--------------|-------|
| Gather requirements | [1 Understand](1_understand.md) |
| Design architecture | [1 Understand](1_understand.md) |
| Set up Python environment | [2 Setup](2_setup.md) |
| Create project structure | [2 Setup](2_setup.md) |
| Write functions/classes | [3 Build](3_build.md) |
| Write tests | [3 Build](3_build.md) |
| Write documentation | [3 Build](3_build.md) |
| Configure pyproject.toml | [4 Ship](4_ship.md) |
| Set up CI/CD | [4 Ship](4_ship.md) |
| Optimize performance | [5 Operate](5_operate.md) |
| Fix security issues | [5 Operate](5_operate.md) |
| Debug production issues | [5 Operate](5_operate.md) |
| Refactor code | [6 Evolve](6_evolve.md) |
| Review pull requests | [6 Evolve](6_evolve.md) |
| Build a CLI app | [7 Specialize](7_specialize.md) |
| Build a web app | [7 Specialize](7_specialize.md) |

---

## Navigation Guide
<!-- Lines 135-135 -->

### Upward: To Philosophy
<!-- Lines 138-150 -->

Each stage connects to foundational principles:

| Stage | Primary Philosophy Links |
|-------|--------------------------|
| 1 Understand | [0.1 Intentionality](../LOD_0_philosophy/0.1_intentionality.md), [0.2 Structure](../LOD_0_philosophy/0.2_structure_primacy.md), [0.3 Rough-to-Fine](../LOD_0_philosophy/0.3_rough_to_fine.md) |
| 2 Setup | [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md), [0.2 Structure](../LOD_0_philosophy/0.2_structure_primacy.md) |
| 3 Build | [0.5 Communication](../LOD_0_philosophy/0.5_communication_ux.md), [0.7 Polyglot](../LOD_0_philosophy/0.7_polyglot_pragmatism.md) |
| 4 Ship | [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md) |
| 5 Operate | [0.8 Defensive](../LOD_0_philosophy/0.8_defensive_design.md) |
| 6 Evolve | [0.3 Rough-to-Fine](../LOD_0_philosophy/0.3_rough_to_fine.md), [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md) |
| 7 Specialize | All (varies by application type) |

### Downward: To Phases
<!-- Lines 153-169 -->

Each stage expands into [LOD_2 Phases](../LOD_2_phases/0_index.md):

| Stage | LOD_2 Phases |
|-------|--------------|
| 1 Understand | 1.1 Requirements, 1.2 Design |
| 2 Setup | 2.1 Environment, 2.2 Project Structure |
| 3 Build | 3.1 Implementation, 3.2 Testing, 3.3 Documentation |
| 4 Ship | 4.1 Packaging, 4.2 Quality, 4.3 Deployment |
| 5 Operate | 5.1 Performance, 5.2 Security, 5.3 Debugging |
| 6 Evolve | 6.1 Iteration, 6.2 Collaboration |
| 7 Specialize | 7.1 Scenarios |

**Cross-refs:**
- ↑ Parent: [LOD_0 Philosophy](../LOD_0_philosophy/0_index.md)
- ↓ Children: [LOD_2 Phases](../LOD_2_phases/0_index.md)
- → Related: [../README.md](../README.md)
