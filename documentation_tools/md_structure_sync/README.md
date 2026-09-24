# md-structure-sync

> Synchronize markdown table of contents and section line ranges.

## Problem
<!-- Lines 7-13 -->

Markdown files with manual TOCs and line-range annotations drift out of sync as content changes. This tool detects and fixes:

- Missing or outdated Table of Contents
- Wrong line-range annotations in TOC entries: `_(Lines X-Y)_`
- Wrong line-range comments after headers: `<!-- Lines X-Y -->`

## Usage
<!-- Lines 16-30 -->

```bash
# Single file
md-structure-sync path/to/file.md

# Directory (recursive)
md-structure-sync path/to/docs/ --pattern "*.md"

# Dry run (show changes without writing)
md-structure-sync path/to/file.md --dry-run

# Adjust header depth (default: H2-H4)
md-structure-sync path/to/file.md --min-level 2 --max-level 3
```

## Design
<!-- Lines 33-33 -->

### The Line-Shift Problem
<!-- Lines 36-49 -->

Inserting a TOC or line comment shifts all subsequent line numbers. Naive approaches break:

```
1. Parse file → sections at lines 10, 25, 40
2. Insert TOC (5 lines) at line 3
3. Sections are now at lines 15, 30, 45 ← original parse is wrong
```

**Solution:** Two-pass approach:

1. **Pass 1 (Parse):** Read file, identify sections and existing annotations
2. **Pass 2 (Compute + Patch):** Calculate final line numbers *including* planned insertions, generate all edits, apply bottom-to-top

### Processing Pipeline
<!-- Lines 52-59 -->

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  PARSE   │ ──► │  PLAN    │ ──► │ COMPUTE  │ ──► │  APPLY   │
│ Raw→AST  │     │ Edits    │     │ Final #s │     │ Bottom↑  │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```

### Idempotency
<!-- Lines 62-64 -->

Running twice produces identical output. Safe to use in CI/pre-commit hooks.

## File Format Assumptions
<!-- Lines 67-67 -->

### H1 Title (optional)
<!-- Lines 70-76 -->

```markdown
# Document Title
```

Single H1 at top, not included in TOC.

### Table of Contents
<!-- Lines 79-91 -->

```markdown
## Table of Contents

1. [Section Name](#section-name) _(Lines 30-75)_
2. [Another Section](#another-section) _(Lines 76-120)_
   1. [Subsection](#subsection) _(Lines 80-100)_
```

- Located after H1 (or at top if no H1)
- Followed by `---` separator
- Nested numbering for H3+ under H2

### Section Headers
<!-- Lines 94-104 -->

```markdown
## Section Name
<!-- Lines 30-75 -->

Content here...
```

- Line comment immediately after header (optional, inserted if missing)
- Range spans from header to next header (or EOF)

## Fenced Code Blocks
<!-- Lines 107-115 -->

Everything inside a fenced code block (a line of three or more backticks or tildes,
optionally indented, with an optional info string) is ignored: headings, TOC-header lookalikes, TOC entries, and
`<!-- Lines X-Y -->` comments inside a fence are never parsed as real structure, and the
tool never inserts or rewrites a `<!-- Lines -->` comment inside one. A fence closes only
on a line using the same marker character and at least the same length as the opener
(per CommonMark), so a shorter or differently-charactered marker nested inside stays
part of the fenced content.

## Anchor Generation
<!-- Lines 118-130 -->

Anchors match GitHub's heading-slug algorithm: strip inline markdown first — code span
contents are literal (only the backticks go, e.g. `` `snake_case` `` keeps its
underscore), `[text](url)` links reduce to `text`, `*`/`**`/`***`/`~~` emphasis markers are
always removed, and `_`/`__`/`___` are removed only when they form a matched,
non-intraword emphasis pair (so `line_profiler` and `STEP_IO_PROTOCOL` keep their
underscores, but `__main__` does not, matching GitHub's own renderer). Then lowercase,
remove every remaining character that is not a Unicode letter/number, `-`, `_` or space
(no hyphen inserted for the removed character), and turn each remaining space into a
hyphen. Runs of spaces are not collapsed, so removed punctuation next to a space can
produce a double hyphen (e.g. "Code & Examples" → `code--examples`). Duplicate headings
get `-1`, `-2`, ... suffixes in document order.

## Installation
<!-- Lines 133-140 -->

```bash
cd documentation_tools/md_structure_sync
uv tool install -e .

# tests
uv run --extra dev pytest
```
