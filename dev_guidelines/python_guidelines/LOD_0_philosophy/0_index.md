# 0 Philosophy Index

> Immutable axioms governing all Python development decisions.

## Table of Contents

1. [Overview](#overview) _(Lines 27-43)_
1. [Philosophy Files](#philosophy-files) _(Lines 46-57)_
   1. [Reading Order](#reading-order) _(Lines 60-67)_
   1. [Interdependencies](#interdependencies) _(Lines 70-88)_
1. [How to Use LOD_0](#how-to-use-lod_0) _(Lines 91-91)_
   1. [For Decision Making](#for-decision-making) _(Lines 94-101)_
   1. [For Code Review](#for-code-review) _(Lines 104-112)_
   1. [For Onboarding](#for-onboarding) _(Lines 115-123)_
1. [Cross-Reference Map](#cross-reference-map) _(Lines 126-126)_
   1. [Philosophy → Stage Impact](#philosophy--stage-impact) _(Lines 129-140)_
   1. [Navigation](#navigation) _(Lines 143-149)_
1. [Summary](#summary) _(Lines 152-153)_




---

## Overview
<!-- Lines 27-43 -->

LOD_0 contains the **first principles** that govern all downstream decisions. These are not arbitrary rules but derived axioms that answer the question: *Why do we do things this way?*

**Key Characteristics:**
- **Immutable:** These principles rarely change
- **Universal:** Apply across all Python development contexts
- **Foundational:** All other LOD levels trace back here
- **Articulable:** Each principle can be explained in one sentence

**When to Consult LOD_0:**
- When a decision feels arbitrary
- When two "best practices" conflict
- When explaining *why* to a skeptical colleague
- When onboarding to this guideline system

---

## Philosophy Files
<!-- Lines 46-57 -->

| File | Title | Core Axiom |
|------|-------|------------|
| [0.1](0.1_intentionality.md) | Intentionality | Every artifact exists for a reason that can be articulated |
| [0.2](0.2_structure_primacy.md) | Structure Primacy | Structure precedes implementation |
| [0.3](0.3_rough_to_fine.md) | Rough-to-Fine | Derive solutions top-down, abstract to concrete |
| [0.4](0.4_data_centricity.md) | Data-Centric Thinking | Data is the enduring artifact; code is transient |
| [0.5](0.5_communication_ux.md) | Communication as UX | Every name, docstring, and interface is UX |
| [0.6](0.6_reproducibility.md) | Reproducibility | Same inputs, same process, same outputs |
| [0.7](0.7_polyglot_pragmatism.md) | Polyglot Pragmatism | Right paradigm for the right problem |
| [0.8](0.8_defensive_design.md) | Defensive Design | Assume failure, design for clarity |

### Reading Order
<!-- Lines 60-67 -->

**First time:** Read in numerical order (0.1 → 0.8)

**Quick refresh:** Focus on these three:
1. [0.1 Intentionality](0.1_intentionality.md) - The meta-principle
2. [0.2 Structure Primacy](0.2_structure_primacy.md) - Design before code
3. [0.3 Rough-to-Fine](0.3_rough_to_fine.md) - The derivation process

### Interdependencies
<!-- Lines 70-88 -->

```
0.1 Intentionality ──────────────────────────────────┐
       │                                              │
       ▼                                              │
0.2 Structure Primacy ◄──► 0.4 Data-Centricity       │
       │                         │                    │
       ▼                         ▼                    │
0.3 Rough-to-Fine ◄────► 0.7 Polyglot Pragmatism     │
       │                         │                    │
       ▼                         ▼                    │
0.5 Communication ◄────► 0.8 Defensive Design        │
       │                         │                    │
       ▼                         ▼                    │
0.6 Reproducibility ◄────────────┴────────────────────┘
```

---

## How to Use LOD_0
<!-- Lines 91-91 -->

### For Decision Making
<!-- Lines 94-101 -->

When facing a design decision:

1. **Identify the tension:** What are the competing options?
2. **Trace to philosophy:** Which LOD_0 principles apply?
3. **Apply the axiom:** What does the principle recommend?
4. **Document the reasoning:** "We chose X because of [principle]"

### For Code Review
<!-- Lines 104-112 -->

Use philosophy as a review lens:

- **0.1 Intentionality:** "Why does this exist?"
- **0.2 Structure:** "Is the structure clear before code?"
- **0.4 Data-Centricity:** "Is data stable, code transient?"
- **0.5 Communication:** "Is naming obvious to the reader?"
- **0.8 Defensive:** "Does this fail fast and clearly?"

### For Onboarding
<!-- Lines 115-123 -->

New team members should:
1. Read all 8 philosophy files (2-3 hours)
2. Identify 2-3 that resonate most
3. Watch for their application in code review
4. Reference philosophy in PR discussions

---

## Cross-Reference Map
<!-- Lines 126-126 -->

### Philosophy → Stage Impact
<!-- Lines 129-140 -->

| Philosophy | Primary Stages | Why |
|------------|----------------|-----|
| 0.1 Intentionality | 1 Understand, 3 Build | Drives requirements and naming |
| 0.2 Structure Primacy | 1 Understand, 2 Setup | Drives design and project structure |
| 0.3 Rough-to-Fine | 1 Understand, 6 Evolve | Drives derivation and iteration |
| 0.4 Data-Centricity | 1 Understand, 3 Build | Drives data modeling and typing |
| 0.5 Communication | 3 Build | Drives naming and documentation |
| 0.6 Reproducibility | 2 Setup, 4 Ship, 6 Evolve | Drives environments and versioning |
| 0.7 Polyglot | 1 Understand, 3 Build | Drives paradigm selection |
| 0.8 Defensive | 1 Understand, 5 Operate | Drives error strategy and security |

### Navigation
<!-- Lines 143-149 -->

**Cross-refs:**
- ↓ Children: All [LOD_1 Stages](../LOD_1_stages/0_index.md) reference LOD_0 principles
- → Related: [../README.md](../README.md) for navigation overview

---

## Summary
<!-- Lines 152-153 -->

LOD_0 is the **foundation**. Every guideline, pattern, and practice in this knowledge base traces back to one or more of these 8 principles. When in doubt, return here.
