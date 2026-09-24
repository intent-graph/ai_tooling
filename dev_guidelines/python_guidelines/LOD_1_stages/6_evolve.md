# 6 Evolve

> Iterate on code, collaborate with others.

## Table of Contents

1. [Stage Overview](#stage-overview) _(Lines 39-41)_
   1. [Why Evolution Matters](#why-evolution-matters) _(Lines 44-46)_
   1. [What Happens Here](#what-happens-here) _(Lines 49-54)_
   1. [Entry Criteria](#entry-criteria) _(Lines 57-64)_
   1. [Exit Criteria](#exit-criteria) _(Lines 67-80)_
1. [Iteration Phase](#iteration-phase) _(Lines 83-85)_
   1. [Refactoring](#refactoring) _(Lines 88-139)_
   1. [Technical Debt](#technical-debt) _(Lines 142-166)_
   1. [Deprecation](#deprecation) _(Lines 169-190)_
   1. [Breaking Changes](#breaking-changes) _(Lines 193-210)_
1. [Collaboration Phase](#collaboration-phase) _(Lines 213-215)_
   1. [Code Review](#code-review) _(Lines 218-261)_
   1. [Version Control](#version-control) _(Lines 264-295)_
   1. [Team Conventions](#team-conventions) _(Lines 298-339)_
1. [Stage Checklist](#stage-checklist) _(Lines 342-344)_
   1. [Iteration Checklist](#iteration-checklist) _(Lines 347-354)_
   1. [Collaboration Checklist](#collaboration-checklist) _(Lines 357-364)_
   1. [Quick Verification](#quick-verification) _(Lines 367-378)_
   1. [Red Flags](#red-flags) _(Lines 381-390)_
1. [Navigation](#navigation) _(Lines 393-399)_








---

## Stage Overview
<!-- Lines 39-41 -->

The Evolve stage addresses **sustainable software growth**. Code isn't static—it changes, improves, accumulates debt, and involves multiple people. This stage provides the practices that make evolution manageable rather than chaotic.

### Why Evolution Matters
<!-- Lines 44-46 -->

Most software spending is maintenance, not initial development. The decisions you make about how code evolves determine whether a codebase becomes easier or harder to work with over time.

### What Happens Here
<!-- Lines 49-54 -->

This stage has two phases:

1. **Iteration (6.1):** Improving existing code systematically
2. **Collaboration (6.2):** Working effectively with others

### Entry Criteria
<!-- Lines 57-64 -->

You enter this stage when:
- Code is in production and needs changes
- Technical debt needs addressing
- Team is growing or changing
- Breaking changes are necessary
- Refactoring is needed

### Exit Criteria
<!-- Lines 67-80 -->

This stage is ongoing—you never truly "exit." Success means:
- Refactoring happens continuously
- Technical debt is tracked and managed
- Code reviews are productive
- Version control practices are consistent
- Team conventions are documented

**Philosophy connections:**
- [0.3 Rough-to-Fine](../LOD_0_philosophy/0.3_rough_to_fine.md) — Iteration as refinement
- [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md) — Traceability through version control

---

## Iteration Phase
<!-- Lines 83-85 -->

Iteration is the **continuous improvement of existing code**. It encompasses refactoring, managing technical debt, handling deprecation, and making breaking changes responsibly.

### Refactoring
<!-- Lines 88-139 -->

Refactoring is **changing code structure without changing behavior**. It's not rewriting; it's improving.

**When to refactor:**
- Before adding a feature (make the change easy)
- After adding a feature (clean up)
- When patterns emerge (DRY violations)
- When code is hard to understand

**Refactoring discipline:**
```
1. Have tests that pass
2. Make small structural change
3. Run tests
4. Commit
5. Repeat
```

Never refactor and change behavior in the same commit. If tests fail during refactoring, you changed behavior—undo and try again.

**Common refactorings:**
- **Extract function:** Pull repeated code into a named function
- **Rename:** Give something a better name
- **Extract class:** Group related data and functions
- **Inline:** Remove unnecessary indirection
- **Move:** Put code where it belongs

```python
# Before: Duplicated logic
def process_order(order):
    if order.total > 100:
        discount = order.total * 0.1
    else:
        discount = 0
    # ...

def calculate_invoice(order):
    if order.total > 100:
        discount = order.total * 0.1
    else:
        discount = 0
    # ...

# After: Extracted function
def calculate_discount(total: Decimal) -> Decimal:
    return total * Decimal("0.1") if total > 100 else Decimal("0")

def process_order(order):
    discount = calculate_discount(order.total)
    # ...
```

### Technical Debt
<!-- Lines 142-166 -->

Technical debt is **the cost of shortcuts taken**. Like financial debt, it accrues interest—future work becomes harder.

**Types of debt:**
- **Deliberate:** Known shortcuts for speed
- **Accidental:** Discovered through learning
- **Bit rot:** Code that aged poorly

**Managing debt:**
1. **Track it:** Maintain a debt register
2. **Quantify it:** Estimate cost to fix
3. **Prioritize:** Fix what blocks progress
4. **Budget time:** Allocate capacity for debt reduction

```markdown
## Technical Debt Register
<!-- Lines 168-175 -->

| ID | Description | Impact | Estimated Fix | Priority |
|----|-------------|--------|---------------|----------|
| TD-001 | User service has no tests | High risk of regression | 2 days | High |
| TD-002 | Config is hardcoded | Blocks multi-env deploy | 4 hours | Medium |
| TD-003 | Auth uses deprecated library | Security risk | 1 day | High |
```

### Deprecation
<!-- Lines 169-190 -->

Deprecation is **signaling that something will be removed**.

```python
import warnings

def old_function():
    """Deprecated: Use new_function instead."""
    warnings.warn(
        "old_function is deprecated, use new_function instead",
        DeprecationWarning,
        stacklevel=2
    )
    return new_function()
```

**Deprecation protocol:**
1. Add deprecation warning with migration path
2. Document in changelog
3. Maintain for at least one version cycle
4. Remove with a major version bump

### Breaking Changes
<!-- Lines 193-210 -->

Breaking changes **require users to update their code**. Handle them carefully:

**When breaking changes are necessary:**
- Fixing fundamental design mistakes
- Removing security vulnerabilities
- Major version upgrades

**Breaking change protocol:**
1. **Announce early:** Give users time
2. **Provide migration path:** How do they update?
3. **Version appropriately:** Major version bump (semver)
4. **Document thoroughly:** What changed, why, how to adapt

**Cross-ref:** → [6.1 Iteration](../LOD_2_phases/6.1_iteration.md) for detailed guidance

---

## Collaboration Phase
<!-- Lines 213-215 -->

Collaboration is how **multiple people work on the same codebase** without chaos.

### Code Review
<!-- Lines 218-261 -->

Code review serves multiple purposes:
- **Catch bugs:** Fresh eyes spot problems
- **Share knowledge:** Reviewers learn the code
- **Enforce standards:** Consistency through oversight
- **Improve design:** Discussion improves solutions

**Reviewing effectively:**

```markdown
## Code Review Checklist
<!-- Lines 239-239 -->

### Correctness
<!-- Lines 242-245 -->
- [ ] Does the code do what it claims?
- [ ] Are edge cases handled?
- [ ] Are there obvious bugs?

### Design
<!-- Lines 248-251 -->
- [ ] Is this the right approach?
- [ ] Is it appropriately simple?
- [ ] Does it follow project patterns?

### Maintainability
<!-- Lines 254-257 -->
- [ ] Is it readable?
- [ ] Are names clear?
- [ ] Would I understand this in 6 months?

### Testing
<!-- Lines 260-270 -->
- [ ] Are there tests?
- [ ] Do tests cover the changes?
- [ ] Are tests readable?
```

**Giving feedback:**
- Be specific: "This could be clearer" → "Consider renaming `x` to `user_count`"
- Explain why: Not just "change this" but why it matters
- Distinguish: "Must fix" vs "Consider" vs "Nitpick"
- Be kind: Critique code, not people

### Version Control
<!-- Lines 264-295 -->

Version control is the **foundation of collaboration**. Use it well.

**Commit discipline:**
- **Atomic commits:** One logical change per commit
- **Meaningful messages:** Explain why, not just what
- **Clean history:** Readable sequence of changes

```bash
# Good commit message
git commit -m "Add rate limiting to API endpoints

Prevents abuse by limiting requests to 100/minute per user.
Implements token bucket algorithm with Redis backend.

Closes #123"

# Bad commit message
git commit -m "fixed stuff"
```

**Branching strategy:**
- **Main/Master:** Always deployable
- **Feature branches:** One feature per branch
- **Short-lived:** Merge frequently

```
main ─────────────────────────────
       \                   /
        feature-x ────────
```

### Team Conventions
<!-- Lines 298-339 -->

Conventions reduce friction by making decisions automatic.

**Document conventions:**
- Code style (handled by formatter)
- Commit message format
- Branch naming
- PR/review process
- Testing requirements

```markdown
## Team Conventions
<!-- Lines 320-320 -->

### Branches
<!-- Lines 323-326 -->
- Feature: `feature/short-description`
- Bugfix: `fix/issue-number-description`
- Release: `release/version`

### Commits
<!-- Lines 329-331 -->
- Imperative mood: "Add feature" not "Added feature"
- Reference issues: "Closes #123"

### Pull Requests
<!-- Lines 334-348 -->
- Require one approval
- Must pass CI
- Squash merge to main
```

**Enforce automatically where possible:**
- Linters for style
- Pre-commit hooks for formatting
- CI for tests
- Branch protection rules

**Cross-ref:** → [6.2 Collaboration](../LOD_2_phases/6.2_collaboration.md) for detailed guidance

---

## Stage Checklist
<!-- Lines 342-344 -->

The Evolve stage is ongoing, but verify these foundations:

### Iteration Checklist
<!-- Lines 347-354 -->

- [ ] Refactoring happens regularly
- [ ] Tests exist to support refactoring
- [ ] Technical debt is tracked
- [ ] Debt reduction is scheduled
- [ ] Deprecation process is defined
- [ ] Breaking change policy exists

### Collaboration Checklist
<!-- Lines 357-364 -->

- [ ] Code review process is defined
- [ ] Reviews happen before merge
- [ ] Commit conventions are documented
- [ ] Branch strategy is defined
- [ ] CI runs on all PRs
- [ ] Team conventions are documented

### Quick Verification
<!-- Lines 367-378 -->

```bash
# Check for deprecation warnings
python -W default script.py

# View git log for commit discipline
git log --oneline -20

# Check branch protection
gh repo view --json branchProtectionRules
```

### Red Flags
<!-- Lines 381-390 -->

Stop and address if:
- **"We'll clean it up later"** — Technical debt accumulating untracked
- **"Just merge it"** — Skipping review
- **"I'll remember"** — Conventions not documented
- **Large PRs** — Review fatigue, merge conflicts
- **Long-lived branches** — Integration pain

---

## Navigation
<!-- Lines 393-399 -->

**Cross-refs:**
- ↑ Parent: [LOD_1 Stages Index](0_index.md)
- ↑ Philosophy: [0.3 Rough-to-Fine](../LOD_0_philosophy/0.3_rough_to_fine.md), [0.6 Reproducibility](../LOD_0_philosophy/0.6_reproducibility.md)
- ← Previous Stage: [5 Operate](5_operate.md)
- → Next Stage: [7 Specialize](7_specialize.md)
- ↓ Child Phases: [6.1 Iteration](../LOD_2_phases/6.1_iteration.md), [6.2 Collaboration](../LOD_2_phases/6.2_collaboration.md)
