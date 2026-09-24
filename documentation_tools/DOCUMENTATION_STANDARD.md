# Documentation Standard

This document defines the organizational structure, formatting standards, and maintenance practices for all markdown documentation in this repository.

## Table of Contents

1. [Principles](#principles) _(Lines 37-56)_
1. [File Length Guidelines](#file-length-guidelines) _(Lines 59-59)_
   1. [Target Lengths by Document Type](#target-lengths-by-document-type) _(Lines 62-70)_
   1. [When to Split](#when-to-split) _(Lines 73-87)_
1. [Document Structure](#document-structure) _(Lines 90-90)_
   1. [Standard Document Header](#standard-document-header) _(Lines 93-125)_
   1. [Required Elements](#required-elements) _(Lines 128-134)_
   1. [Optional Elements (for README/Index files)](#optional-elements-for-readmeindex-files) _(Lines 137-144)_
1. [Line Number TOC Format](#line-number-toc-format) _(Lines 147-147)_
   1. [Format Specification](#format-specification) _(Lines 150-173)_
   1. [Section Comments](#section-comments) _(Lines 176-189)_
1. [Metadata Approach](#metadata-approach) _(Lines 192-192)_
   1. [Minimal Git-Based Metadata](#minimal-git-based-metadata) _(Lines 195-206)_
   1. [How to Reference Documents](#how-to-reference-documents) _(Lines 209-221)_
1. [Semantic Splitting](#semantic-splitting) _(Lines 224-224)_
   1. [Principles](#principles-1) _(Lines 227-232)_
   1. [Splitting Process](#splitting-process) _(Lines 235-245)_
1. [Cross-References](#cross-references) _(Lines 248-248)_
   1. [Link Format](#link-format) _(Lines 251-262)_
   1. [Hub Files](#hub-files) _(Lines 265-280)_
1. [Maintenance Guidelines](#maintenance-guidelines) _(Lines 283-283)_
   1. [When Creating New Documentation](#when-creating-new-documentation) _(Lines 286-292)_
   1. [When Refactoring Existing Documentation](#when-refactoring-existing-documentation) _(Lines 295-304)_
   1. [When Deprecating Documentation](#when-deprecating-documentation) _(Lines 307-315)_


---

## Principles
<!-- Lines 37-56 -->

**Core Values:**

1. **Modular Over Monolithic**: Split large documents into focused, manageable modules
2. **Indexed and Navigable**: Every document has clear line-number based table of contents
3. **Hierarchical Structure**: Use directory structure to show relationships
4. **Content Preservation**: Reorganization does NOT change technical content
5. **Git-Based Metadata**: No manual version numbers or dates - git tracks this
6. **AI and Human Friendly**: Same docs work for both audiences

**Key Rules:**

- **Shorter is better**: Target 200-300 lines per file, max 500 (rare exceptions like main README)
- **Split semantically**: Group by logical boundaries, not arbitrary line counts
- **Preserve exactly**: When refactoring, copy content verbatim - no rewrites
- **Line numbers**: All major sections show start-end line ranges in TOCs
- **Simple metadata**: Filename IS the doc ID, git tracks versions and dates

---
  
## File Length Guidelines
<!-- Lines 59-59 -->

### Target Lengths by Document Type
<!-- Lines 62-70 -->

| Document Type | Target Lines | Max Lines | Notes |
|--------------|--------------|-----------|-------|
| Guideline Module | 200-300 | 500 | Deep dive on one topic |
| README/Index | 150-250 | 400 | Navigation hub |
| Main Repository README | 300-400 | 500 | Needs to point to many things |
| Workflow/Process | 200-300 | 450 | Step-by-step procedures |
| AI Instructions | 500-800 | 1000 | Complex prompts need more context |

### When to Split
<!-- Lines 73-87 -->

**Split if:**
- File exceeds max by 50%+ (e.g., 750+ for guideline)
- Multiple distinct topics that can be separated
- Users commonly reference only specific sections
- Table of contents has 10+ major sections

**Keep together if:**
- Topics are tightly coupled and splitting adds confusion
- Total length under max guideline
- Splitting would create excessive cross-references
- Content follows a narrative flow that shouldn't be broken

---

## Document Structure
<!-- Lines 90-90 -->

### Standard Document Header
<!-- Lines 93-125 -->

Every document should start with this structure:
The Table of content can be skipped if the file is short enough

```markdown
# [Document Title]

[1-3 sentence document purpose]

## Table of Contents

1. [Section One](#section-one) _(Lines 30-120)_
2. [Section Two](#section-two) _(Lines 121-250)_
   - [Subsection 2.1](#subsection-21) _(Lines 130-180)_
   - [Subsection 2.2](#subsection-22) _(Lines 181-250)_
3. [Section Three](#section-three) _(Lines 251-350)_

---

## Section One
<!-- Lines 30-120 -->

[Content...]

## Section Two
<!-- Lines 121-250 -->

### Subsection 2.1
<!-- Lines 130-180 -->

[Content...]
```

### Required Elements
<!-- Lines 128-134 -->

1. **H1 Title**: Single top-level heading with document name
2. **Purpose Statement**: 1-3 sentences immediately after title
3. **Table of Contents**: With line number ranges for all major sections
4. **Horizontal Rule**: `---` separator after TOC
5. **Section Comments**: `<!-- Lines X-Y -->` at start of major sections

### Optional Elements (for README/Index files)
<!-- Lines 137-144 -->

- **Quick Reference**: Most important points up front
- **Decision Trees**: Visual guides for common choices
- **Module Index**: Table with file descriptions and when to read
- **Related Documentation**: Links to connected docs

---

## Line Number TOC Format
<!-- Lines 147-147 -->

### Format Specification
<!-- Lines 150-173 -->

```markdown
## Table of Contents

1. [Major Section](#major-section) _(Lines 80-250)_
   - [Subsection A](#subsection-a) _(Lines 95-150)_
   - [Subsection B](#subsection-b) _(Lines 151-250)_
2. [Another Section](#another-section) _(Lines 251-400)_
```

**Rules:**

- Use `_(Lines X-Y)_` format (underscore italics with "Lines" prefix)
- Line numbers are **approximate** and don't need to be updated constantly
- Only add line numbers to **major sections** (H2), optionally to subsections (H3)
- Don't add line numbers to every H4/H5 (too granular)

**Benefits:**

- AI can jump directly to specific sections
- Code reviewers can navigate large files quickly
- Cross-references can point to exact locations
- Shows relative size of sections at a glance

### Section Comments
<!-- Lines 176-189 -->

Add HTML comments at the start of major sections:

```markdown
## Major Section Name
<!-- Lines 80-250 -->

[Section content...]
```

These comments help readers see where they are when scrolling.

---

## Metadata Approach
<!-- Lines 192-192 -->

### Minimal Git-Based Metadata
<!-- Lines 195-206 -->

**NO:**
- ❌ Version numbers (git tracks this)
- ❌ "Last Updated" dates (use `git log filename`)
- ❌ "Status" fields (archived docs go to `doc/archived/`)
- ❌ Author names (use `git blame` or `git log`)

**YES:**
- ✅ Document ID = filename (simple!)
- ✅ Clear document title (H1 heading)
- ✅ Purpose statement (1-3 sentences)

### How to Reference Documents
<!-- Lines 209-221 -->

**Cross-file references:**
```markdown
See [Function Design Guidelines](../function_design.md#parameter-conventions).
See [Primary Keys](db_schema_design/03_primary_keys.md) for details.
```

**Document ID in discussions:**
- Filename without extension: `db_schema_design/03_primary_keys`
- Or full relative path: `doc/guidelines/db_schema_design/03_primary_keys.md`

---

## Semantic Splitting
<!-- Lines 224-224 -->

### Principles
<!-- Lines 227-232 -->

1. **Split by logical boundaries**: Major topics should be separate files
2. **Preserve cohesion**: Related subsections stay together
3. **Avoid tiny files**: Don't split below ~150 lines unless truly independent
4. **Merge related**: Combine small sections that make sense together
 
### Splitting Process
<!-- Lines 235-245 -->

1. **Identify major sections**: Look at existing H2 headings
2. **Calculate sizes**: Count lines for each section
3. **Group related**: Combine small related sections (<150 lines)
4. **Check targets**: Aim for 200-300 lines per file
5. **Preserve content**: Extract exact text, no rewrites
6. **Add TOCs**: Create line-number TOCs for each new file
7. **Create README**: Build index/hub with links to all modules

---

## Cross-References
<!-- Lines 248-248 -->

### Link Format
<!-- Lines 251-262 -->

**Same repository references (RECOMMENDED):**
```markdown
See [Document Title](relative/path.md#section-anchor).
See [Primary Keys](db_schema_design/03_primary_keys.md#composite-keys).
```

**With line number hints (for AI/precision):**
```markdown
See [Primary Keys](db_schema_design/03_primary_keys.md#composite-keys) @ lines 120-180.
```

### Hub Files
<!-- Lines 265-280 -->

README files should provide comprehensive navigation:

```markdown
## Module Index

| Module | Lines | Topics Covered | When to Read |
|--------|-------|----------------|--------------|
| [01. Principles](01_design_principles.md) | 200 | Core philosophy | Starting new design |
| [02. Naming](02_naming_conventions.md) | 300 | Table/column names | Naming decisions |
```

This shows users exactly where to look and what each module covers.

---

## Maintenance Guidelines
<!-- Lines 283-283 -->

### When Creating New Documentation
<!-- Lines 286-292 -->

1. Use templates from `doc/TEMPLATES/`
2. Follow target line lengths (200-300 for most docs)
3. Add line-number TOC
4. Update relevant README indexes
5. Use relative links for cross-references

### When Refactoring Existing Documentation
<!-- Lines 295-304 -->

1. Analyze semantic boundaries first
2. Preserve content exactly (no rewrites during reorganization)
3. Extract sections verbatim
4. Add line-number TOCs to new files
5. Create README index if splitting into multiple files
6. Deprecate or archive old file with pointer to new location
7. Update cross-references in other docs
8. Update CLAUDE.md if search paths changed

### When Deprecating Documentation
<!-- Lines 307-315 -->

1. Move to `doc/archived/` (don't delete)
2. Add deprecation notice at top pointing to replacement
3. Update all references to point to new location

---

This document is licensed CC BY 4.0 (see the repository root `README.md` and
`LICENSE-CC-BY-4.0.txt`), unlike the rest of `documentation_tools/`, which is MIT.
