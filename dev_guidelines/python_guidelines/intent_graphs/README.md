# Python KB — Two-Graph Representation

This directory holds the **canonical generic guideline IGs** for Python. Other repos reference these files via their `intent_resources.yaml`; they do not keep local copies. Edit the graphs here; consume via manifest paths.

The Python Development Guidelines knowledge base is represented with **two IntentGraphs** in this directory:

1. **Philosophy** — principles and axioms (the "why").
2. **Guidelines / style** — concrete Python rendering defaults (the "what to do" and "how to render").

This split follows the IntentGraph axiom **P4 (Projection is orthogonal)**: product intent (what we believe) is separate from projection intent (how we render). Here, philosophy is product-level; guidelines/style is projection-level for Python code.

---

## 1. Philosophy graph (principles)
<!-- Lines 16-39 -->

**File:** [python_kb_philosophy.yaml](python_kb_philosophy.yaml)

**Source in KB:** [LOD_0_philosophy/](../LOD_0_philosophy/)

**Content:** The 8 foundational principles that govern all downstream decisions:

| UID | Principle | One-line axiom |
|-----|-----------|----------------|
| INTENTIONALITY | Intentionality | Every artifact exists for a reason that can be articulated |
| STRUCTURE | Structure Primacy | Structure precedes implementation |
| ROUGHTOFINE | Rough-to-Fine | Derive solutions top-down, abstract to concrete |
| DATACENTRICITY | Data-Centric Thinking | Data is the enduring artifact; code is transient |
| COMMUNICATION | Communication as UX | Every name, docstring, and interface is UX |
| REPRODUCIBILITY | Reproducibility | Same inputs, same process, same outputs |
| POLYGLOT | Polyglot Pragmatism | Right paradigm for the right problem |
| DEFENSIVE | Defensive Design | Assume failure, design for clarity |

**Intentlinks** encode interdependencies from the KB (e.g. Intentionality → Structure; Structure ↔ Data-Centricity; Rough-to-Fine ↔ Polyglot; Communication ↔ Defensive; Reproducibility → Intentionality).

**Use when:** Explaining *why* a guideline exists, resolving conflicts between practices, onboarding to the guideline system, or tracing a rule back to first principles.

---

## 2. Guidelines / style graph (Python defaults)
<!-- Lines 42-54 -->

**File:** [python_defaults.ig.yaml](python_defaults.ig.yaml)

**Source in KB:** Derived from LOD_1–LOD_5 (stages, phases, domains, practices, details), condensed into projection dimensions.

**Content:** Default rendering decisions for Python code — structure (package layout, module granularity, dependencies), implementation (naming, types, paradigm, errors, API, imports), testing, documentation, tooling, and performance style. Each node provides constraints and conventions (e.g. PEP 8 naming, pytest, Google docstrings, Ruff, pyproject.toml).

**Relationship to philosophy:** The guidelines graph materializes the philosophy in Python-specific form. For example, Defensive Design appears as fail-fast exceptions and boundary validation in `PIG-PY.IMPL.ERR`; Communication as UX appears in `PIG-PY.IMPL.NAME` and `PIG-PY.DOC.STR`.

**Use when:** Generating or reviewing Python code, configuring linters/formatters, setting up project layout, or answering "how should we do X in Python?".

---

## Mapping at a glance
<!-- Lines 57-64 -->

| KB layer | IntentGraph | File |
|----------|-------------|------|
| LOD_0 Philosophy (8 principles) | Philosophy (product) | [python_kb_philosophy.yaml](python_kb_philosophy.yaml) |
| LOD_1–LOD_5 (stages, phases, domains, practices, details) | Guidelines/style (projection) | [python_defaults.ig.yaml](python_defaults.ig.yaml) |

---

## Manifest and Obsidian export
<!-- Lines 67-74 -->

**intent_resources.yaml** (in this directory) lists both graphs and the Obsidian vault root. Paths are relative to the manifest.

**obsidian_export/** is the Obsidian vault root, with one folder per IG (explicit naming):
- **obsidian_export/philosophy/** — export target for `python_kb_philosophy.yaml`
- **obsidian_export/python_defaults/** — export target for `python_defaults.ig.yaml`

**One-liner export to Obsidian:** `./export_to_obsidian.sh` (from repo root or this directory). See [obsidian_export/README.md](obsidian_export/README.md) for details.
