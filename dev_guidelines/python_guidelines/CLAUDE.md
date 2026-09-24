# LLM Navigation Guide

> Instructions for Claude (and other LLMs) on navigating this knowledge base efficiently.

**When to use the dedicated agent:** For answering questions or applying these guidelines across all aspects of Python projects (design, requirements, implementation, testing, documentation, packaging, deployment, debugging, evolution), use the **[Python KB Agent](../../.claude/agents/python-kb-agent.md)**. Invoke it via the Task tool with description `"Python guidelines: answer or apply KB"`. The agent follows this navigation protocol and adds workflows for applying the KB to code.

## Table of Contents

1. [Core Principle: Rough-to-Fine](#core-principle-rough-to-fine) _(Lines 39-39)_
   1. [First: Grep the Manifest, Then Read Index Files](#first-grep-the-manifest-then-read-index-files) _(Lines 42-79)_
   1. [The Token Budget](#the-token-budget) _(Lines 82-89)_
   1. [What Rough-to-Fine Means](#what-rough-to-fine-means) _(Lines 92-111)_
1. [Navigation Protocol](#navigation-protocol) _(Lines 114-114)_
   1. [Step 1: Identify the Task](#step-1-identify-the-task) _(Lines 117-129)_
   1. [Step 2: Start at LOD_1 (Stages)](#step-2-start-at-lod_1-stages) _(Lines 132-145)_
   1. [Step 3: Drill Down Only When Needed](#step-3-drill-down-only-when-needed) _(Lines 148-169)_
   1. [Step 4: Use Line Numbers](#step-4-use-line-numbers) _(Lines 172-195)_
1. [Example Sessions](#example-sessions) _(Lines 198-198)_
   1. [Example 1: User asks "Help me write tests for my function"](#example-1-user-asks-help-me-write-tests-for-my-function) _(Lines 201-226)_
   1. [Example 2: User asks "Set up a new Python project"](#example-2-user-asks-set-up-a-new-python-project) _(Lines 229-252)_
   1. [Example 3: User asks "How should I handle this exception?"](#example-3-user-asks-how-should-i-handle-this-exception) _(Lines 255-281)_
1. [Anti-Patterns](#anti-patterns) _(Lines 284-298)_
1. [Quick Reference](#quick-reference) _(Lines 301-301)_
   1. [Knowledge Tree Manifest](#knowledge-tree-manifest) _(Lines 304-311)_
   1. [LOD Directory Mapping](#lod-directory-mapping) _(Lines 314-323)_
   1. [Stage to LOD_2 Mapping](#stage-to-lod_2-mapping) _(Lines 326-339)_








---

## Core Principle: Rough-to-Fine
<!-- Lines 39-39 -->

### First: Grep the Manifest, Then Read Index Files
<!-- Lines 42-79 -->

**Step 0 — generate the manifest if absent.** The manifest files are regenerated on demand, not committed (they are gitignored). If `doc_manifest_sections.yaml` is not present, generate both manifest files first, from the repo root:

```bash
md-doc-tree-full dev_guidelines/python_guidelines/ -o dev_guidelines/python_guidelines/doc_manifest --heading-depth 3
```

**Step 0b — Grep the manifest** to locate which files and sections cover the topic:

```bash
# Find files/sections relevant to your query
Grep(pattern="testing|pytest", path="python_guidelines/doc_manifest_sections.yaml")
```

The manifest (`doc_manifest_sections.yaml`, ~4k lines) maps every file, heading, and line number in the KB. A single grep gives you the exact files and line ranges to read — no blind tree-walking needed.

For tracing cross-references between files, grep the companion file:
```bash
Grep(pattern="2.4_testing", path="python_guidelines/doc_manifest_cross_refs.yaml")
```

**Regenerate** after adding/removing files or restructuring headings, using the same command as Step 0 above.

**Step 1 — Read the index files** (still mandatory for grounding):

1. **`LOD_0_philosophy/0_index.md`** (~150 lines):
   - Lists all 8 foundational principles with one-sentence summaries
   - Shows interdependencies between principles
   - Maps philosophy to stages (which principles apply where)

2. **`LOD_1_stages/0_index.md`** (~170 lines):
   - Shows the development pipeline flow diagram
   - Stage transitions and triggers
   - Quick reference: "I need to... → Go to stage X"
   - Maps stages to LOD_2 phases

Together these two files (~320 lines total) give you the complete map of the knowledge base. The manifest grep tells you *where to look*; the index files tell you *how it all connects*.

### The Token Budget
<!-- Lines 82-89 -->

You have limited context. This knowledge base has about 300 files. **Never load everything.**

The goal is surgical precision:
- Read **only** what the task requires
- At the **level of detail** the task requires
- Stop drilling down **as soon as** you have enough information

### What Rough-to-Fine Means
<!-- Lines 92-111 -->

```text
LOD_0_philosophy/0_index.md  ─┬─► ALWAYS READ FIRST (the maps)
LOD_1_stages/0_index.md      ─┘
       ↓
LOD_0 (Philosophy)  → Read specific files if you need the "why" behind a decision
       ↓
LOD_1 (Stages)      → Find the right stage for the task
       ↓
LOD_2 (Phases)      → Read if you need phase-level guidance
       ↓
LOD_3 (Domains)     → Read if you need topic-specific rules
       ↓
LOD_4 (Practices)   → Read if you need pattern guidance
       ↓
LOD_5 (Details)     → Read ONLY if you need edge cases or deep specifics
```

---

## Navigation Protocol
<!-- Lines 114-114 -->

### Step 1: Identify the Task
<!-- Lines 117-129 -->

Map the user's request to a development stage:

| User Request About | Stage |
|-------------------|-------|
| Understanding requirements, design | Stage 1: Understand |
| Project setup, environment, structure | Stage 2: Setup |
| Writing code, testing, docs | Stage 3: Build |
| Packaging, CI/CD, deployment | Stage 4: Ship |
| Performance, security, debugging | Stage 5: Operate |
| Refactoring, collaboration | Stage 6: Evolve |
| CLI, web apps, APIs, data pipelines | Stage 7: Specialize |

### Step 2: Start at LOD_1 (Stages)
<!-- Lines 132-145 -->

Read the stage file **first**. It gives you:
- An overview of what the stage covers
- Links to relevant LOD_2 phases
- Cross-references to related stages

```
# Example: User asks about testing
Read: LOD_1_stages/3_build.md

Look at TOC → Find "Testing" section
Read that section → Get phase link to LOD_2_phases/2.4_testing.md
```

### Step 3: Drill Down Only When Needed
<!-- Lines 148-169 -->

**Stop condition:** You have enough information to answer the user's question.

| Need | Read Level |
|------|------------|
| General guidance | LOD_1 stage file only |
| Phase-specific guidance | LOD_1 → LOD_2 phase file |
| Topic-specific rules | LOD_1 → LOD_2 → LOD_3 domain file |
| Specific pattern | LOD_1 → LOD_2 → LOD_3 → LOD_4 practice file |
| Edge cases, deep detail | Full drill-down to LOD_5 |

**Example decision tree:**

```
User: "How do I test my code?"
→ LOD_1: Stage 3 mentions testing, links to LOD_2
→ Is the overview enough? If YES, stop. If NO...
→ LOD_2: Testing phase gives test types and strategies
→ Is this enough? If YES, stop. If NO...
→ LOD_3: Specific domain (unit tests, integration, etc.)
```

### Step 4: Use Line Numbers
<!-- Lines 172-195 -->

Every file has a Table of Contents with **line numbers**:

```text
  Table of Contents

  1. [Section Name](#section-name) _(Lines 30-45)_
  2. [Another Section](#another-section) _(Lines 48-62)_
```

**Use these to read surgically:**

```python
# Instead of reading the whole file:
Read(file_path="LOD_3_domains/3.1_implementation.md")

# Read only the section you need:
Read(file_path="LOD_3_domains/3.1_implementation.md", offset=30, limit=15)
```

This saves tokens and keeps your context focused.

---

## Example Sessions
<!-- Lines 198-198 -->

### Example 1: User asks "Help me write tests for my function"
<!-- Lines 201-226 -->

**Navigation path:**

1. **Identify stage:** Testing → Stage 3 (Build)
2. **Read LOD_1:**
   ```
   Read: LOD_1_stages/3_build.md
   Find: Testing section → Links to LOD_2_phases/2.4_testing.md
   ```
3. **Decide:** Do I need more detail?
   - If user wants general "how to test": LOD_2 is enough
   - If user wants pytest specifics: drill to LOD_3

**What NOT to do:**
- Don't read LOD_0 (philosophy) - not needed for "how to write tests"
- Don't read all of LOD_3 - only the testing domain
- Don't read LOD_5 unless there's a specific edge case

**Token-efficient approach:**
```
Read LOD_1_stages/3_build.md (scan TOC for testing)
Read LOD_2_phases/2.4_testing.md (get testing guidance)
STOP - unless user needs pytest specifics, then:
Read LOD_3_domains/3.4_testing/ relevant file
```

### Example 2: User asks "Set up a new Python project"
<!-- Lines 229-252 -->

**Navigation path:**

1. **Identify stage:** Setup → Stage 2 (Setup)
2. **Read LOD_1:**
   ```
   Read: LOD_1_stages/2_setup.md
   Contains: Environment setup, project structure guidance
   ```
3. **Decide:** What specific aspect?
   - Environment: drill to LOD_2_phases/2.2_environment.md
   - Structure: drill to LOD_2_phases/2.3_project_structure.md

**Efficient read pattern:**
```
Read LOD_1_stages/2_setup.md
↓ User wants pyproject.toml specifics?
Read LOD_2_phases/2.2_environment.md (section on dependencies)
↓ User wants src layout details?
Read LOD_3_domains/3.2_environment/ relevant file
```

**Stop early:** If the LOD_1 stage file answers the question, don't drill deeper.

### Example 3: User asks "How should I handle this exception?"
<!-- Lines 255-281 -->

**Navigation path:**

1. **Identify stage:** Exception handling → Stage 3 (Build) or Stage 5 (Operate)
   - Writing exception handling code → Stage 3
   - Debugging production errors → Stage 5
2. **Read LOD_1:** Based on context, choose the right stage
3. **Drill to domain:**
   ```
   LOD_3_domains/3.1_implementation.md (for writing code)
   OR
   LOD_3_domains/3.5_debugging/ (for debugging issues)
   ```

**Use line numbers:**
```
# TOC shows: 1. [Error Handling](#error-handling) _(Lines 120-145)_
# Read just that section:
Read(file_path="...", offset=120, limit=25)
```

**When to go to LOD_5:**
- User asks: "What exceptions should I use for validation errors?" → LOD_5 details
- User asks: "How do I handle errors?" → LOD_3 is enough

---

## Anti-Patterns
<!-- Lines 284-298 -->

**Never do these:**

| Anti-Pattern | Why It's Bad | Do This Instead |
|--------------|--------------|-----------------|
| Skip the manifest grep | Blind navigation wastes tokens | Grep `doc_manifest_sections.yaml` first |
| Load all LOD_3 files | Wastes tokens | Identify the specific domain first |
| Start at LOD_0 | Unnecessary for most tasks | Start at LOD_1 |
| Read full files | Wastes tokens | Use line numbers to read sections |
| Skip LOD_1 | Miss the map | Always start at LOD_1 |
| Load LOD_5 first | Too much detail | Drill down only when needed |
| Read sibling files "just in case" | Token waste | Follow cross-refs only when relevant |

---

## Quick Reference
<!-- Lines 301-301 -->

### Knowledge Tree Manifest
<!-- Lines 304-311 -->

| File | Lines | Content |
|------|-------|---------|
| `doc_manifest_sections.yaml` | ~4k | Every file + headings + line numbers — grep this first (generated, not in repo) |
| `doc_manifest_cross_refs.yaml` | ~1k | Outgoing links per file — trace dependencies (generated, not in repo) |

Generate if absent, or regenerate after structural changes: `md-doc-tree-full dev_guidelines/python_guidelines/ -o dev_guidelines/python_guidelines/doc_manifest --heading-depth 3` (from the repo root)

### LOD Directory Mapping
<!-- Lines 314-323 -->

| LOD | Directory | When to Read |
|-----|-----------|--------------|
| LOD_0 | `LOD_0_philosophy/` | Understanding "why" behind decisions |
| LOD_1 | `LOD_1_stages/` | **Always start here** |
| LOD_2 | `LOD_2_phases/` | Phase-level guidance |
| LOD_3 | [`LOD_3_domains/`](LOD_3_domains/0_index.md) | Topic-specific rules |
| LOD_4 | [`LOD_4_practices/`](LOD_4_practices/0_index.md) | Pattern guidance |
| LOD_5 | [`LOD_5_details/`](LOD_5_details/0_index.md) | Edge cases only |

### Stage to LOD_2 Mapping
<!-- Lines 326-339 -->

| Stage | Primary LOD_2 Phases |
|-------|---------------------|
| 1 Understand | 2.1_requirements, 2.0_design |
| 2 Setup | 2.2_environment, 2.3_project_structure |
| 3 Build | 2.4_testing, 2.5_documentation, 2.6_implementation |
| 4 Ship | 2.7_packaging, 2.8_quality, 2.9_deployment |
| 5 Operate | 2.10_performance, 2.11_security, 2.12_debugging |
| 6 Evolve | 2.13_iteration, 2.14_collaboration |
| 7 Specialize | 2.15_cli, 2.16_web, 2.17_api, 2.18_data |

---

**Remember:** The goal is to read the **minimum** required to give a **complete** answer. Rough-to-Fine means starting broad and drilling down only when necessary.
