# Python Development Guidelines

> A first-principles, hierarchical knowledge base for Python development — from empty folder to production-ready, maintained application. About 300 files across 6 levels of detail.

## Table of Contents

1. [How to Use This KB](#how-to-use-this-kb) _(Lines 24-26)_
   1. [1. Use the Python KB Agent (recommended)](#1-use-the-python-kb-agent-recommended) _(Lines 29-31)_
   1. [2. Grep the Manifest (quick shortcut)](#2-grep-the-manifest-quick-shortcut) _(Lines 34-66)_
   1. [3. Navigate the Tree Manually](#3-navigate-the-tree-manually) _(Lines 69-73)_
   1. [For Human Developers](#for-human-developers) _(Lines 76-85)_
1. [What's Inside](#whats-inside) _(Lines 88-88)_
   1. [Levels of Detail](#levels-of-detail) _(Lines 91-104)_
   1. [Stages](#stages) _(Lines 107-120)_
   1. [Philosophy Foundations](#philosophy-foundations) _(Lines 123-138)_
1. [Notation and Related Files](#notation-and-related-files) _(Lines 141-147)_



---

## How to Use This KB
<!-- Lines 24-26 -->

Three methods, in order of preference:

### 1. Use the Python KB Agent (recommended)
<!-- Lines 29-31 -->

For any question about Python development, invoke the **[Python KB Agent](../../.claude/agents/python-kb-agent.md)** via the Task tool with `subagent_type="python-kb-agent"`. The agent greps the manifest, navigates the tree, prunes irrelevant branches, and returns a shaped answer with vertical context. This is the preferred path — it handles everything below automatically.

### 2. Grep the Manifest (quick shortcut)
<!-- Lines 34-66 -->

For a quick, targeted lookup when you already know what keyword to search for. The manifest is a YAML file that maps every file, heading, and line number in the KB. **It is ~4k lines — never read it, only grep it.**

**Step 0 — generate the manifest if absent.** The manifest files are regenerated on demand, not committed (they are gitignored). If `doc_manifest_sections.yaml` is not present, generate both manifest files first, from the repo root:

```bash
md-doc-tree-full dev_guidelines/python_guidelines/ -o dev_guidelines/python_guidelines/doc_manifest --heading-depth 3
```

Then:

```
Grep(pattern="testing|pytest", path="python_guidelines/doc_manifest_sections.yaml")
```

This returns the exact files and line ranges that cover your topic. Then read only those sections:

```
Read(path="python_guidelines/LOD_2_phases/2.4_testing.md", offset=30, limit=20)
```

For tracing which files link to each other:
```
Grep(pattern="2.4_testing", path="python_guidelines/doc_manifest_cross_refs.yaml")
```

| File | Lines | Content | Access |
|------|-------|---------|--------|
| `doc_manifest_sections.yaml` | ~4k | Every file + headings + line numbers + word counts | **Grep only** (generated, not in repo) |
| `doc_manifest_cross_refs.yaml` | ~1k | Outgoing links per file | **Grep only** (generated, not in repo) |

**Regenerate** after adding/removing files or restructuring headings, using the same command as Step 0 above.

### 3. Navigate the Tree Manually
<!-- Lines 69-73 -->

Follow the **rough-to-fine** method described in [CLAUDE.md](CLAUDE.md): start at LOD_1 (stages), identify the right stage for your task, drill into LOD_2 phases only if the stage-level answer isn't enough, then into LOD_3/4/5 only when you need specifics. Use each file's TOC line numbers for surgical reads. Stop as soon as you have enough information.

The two index files provide the map: [LOD_0_philosophy/0_index.md](LOD_0_philosophy/0_index.md) (principles) and [LOD_1_stages/0_index.md](LOD_1_stages/0_index.md) (stages and transitions).

### For Human Developers
<!-- Lines 76-85 -->

1. Start at LOD_1 — find your current stage
2. Drill down via links to LOD_2 phases, then LOD_3 domains
3. Return to LOD_0 when decisions feel arbitrary
4. Use TOCs — every file has a Table of Contents with `_(Lines X-Y)_` ranges

**Line navigation:** VS Code `Cmd+G`, Vim `:42`, or click the line number gutter.

---

## What's Inside
<!-- Lines 88-88 -->

### Levels of Detail
<!-- Lines 91-104 -->

The KB is organized as a tree with 6 levels. Start at LOD_1, drill down only as needed. Go deeper for specifics, go up (LOD_0) when decisions feel arbitrary.

| LOD | Name | Depth | Purpose |
|-----|------|-------|---------|
| **LOD_0** | [Philosophy](LOD_0_philosophy/0_index.md) | Full prose | First principles — the "why" behind decisions |
| **LOD_1** | [Stages](LOD_1_stages/0_index.md) | Full prose | Development pipeline — where you are in the process |
| **LOD_2** | [Phases](LOD_2_phases/0_index.md) | Full prose | Lifecycle phases within each stage |
| **LOD_3** | [Domains](LOD_3_domains/0_index.md) | Expanded outlines | Topic-specific rules (e.g. testing, packaging) |
| **LOD_4** | [Practices](LOD_4_practices/0_index.md) | Short | Patterns and how-to |
| **LOD_5** | [Details](LOD_5_details/0_index.md) | Minimal | Edge cases and deep specifics |

About 300 files total.

### Stages
<!-- Lines 107-120 -->

Each stage maps to a development goal. Find your goal, go to the stage.

| Goal | Stage | Phases |
|------|-------|--------|
| Understand the philosophy | [LOD_0: Philosophy](LOD_0_philosophy/0_index.md) | First principles, axioms |
| Define the problem before solving it | [1 Understand](LOD_1_stages/1_understand.md) | Requirements, Design |
| Prepare environment and structure | [2 Setup](LOD_1_stages/2_setup.md) | Environment, Project Structure |
| Write code, test it, document it | [3 Build](LOD_1_stages/3_build.md) | Implementation, Testing, Documentation |
| Package, validate, deploy | [4 Ship](LOD_1_stages/4_ship.md) | Packaging, Quality, Deployment |
| Optimize, secure, debug | [5 Operate](LOD_1_stages/5_operate.md) | Performance, Security, Debugging |
| Iterate and collaborate | [6 Evolve](LOD_1_stages/6_evolve.md) | Iteration, Collaboration |
| Build specific app type (CLI, web, API, data) | [7 Specialize](LOD_1_stages/7_specialize.md) | Application-specific guidance |

### Philosophy Foundations
<!-- Lines 123-138 -->

Each stage traces back to foundational principles in [LOD_0](LOD_0_philosophy/0_index.md):

| Philosophy | Primary Impact |
|------------|----------------|
| [0.1 Intentionality](LOD_0_philosophy/0.1_intentionality.md) | Stages 1, 3 |
| [0.2 Structure Primacy](LOD_0_philosophy/0.2_structure_primacy.md) | Stages 1, 2 |
| [0.3 Rough-to-Fine](LOD_0_philosophy/0.3_rough_to_fine.md) | Stages 1, 6 |
| [0.4 Data-Centricity](LOD_0_philosophy/0.4_data_centricity.md) | Stages 1, 3 |
| [0.5 Communication as UX](LOD_0_philosophy/0.5_communication_ux.md) | Stage 3 |
| [0.6 Reproducibility](LOD_0_philosophy/0.6_reproducibility.md) | Stages 2, 4, 6 |
| [0.7 Polyglot Pragmatism](LOD_0_philosophy/0.7_polyglot_pragmatism.md) | Stages 1, 3 |
| [0.8 Defensive Design](LOD_0_philosophy/0.8_defensive_design.md) | Stages 1, 5 |

---

## Notation and Related Files
<!-- Lines 141-147 -->

Cross-references in KB files use: `↑` parent, `↓` child, `→` sibling/forward, `←` back.

- [CLAUDE.md](CLAUDE.md) — LLM navigation protocol (rough-to-fine, token budget, anti-patterns)
- [intent_graphs/](intent_graphs/README.md) — IntentGraph representation (philosophy + guidelines/style)
- [../software_development_guidelines/](../software_development_guidelines/README.md) — stack-neutral principles (ownership, assurance, change flow, operation, evolution); this KB keeps only the Python realization
- [../](../README.md) — index of all development guidelines
