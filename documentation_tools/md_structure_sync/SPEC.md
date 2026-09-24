# Specification: md-structure-sync

> Technical specification for the markdown structure synchronization tool.

## 1. Core Algorithm: Three-Pass Approach
<!-- Lines 7-17 -->

The algorithm prioritizes **robustness over efficiency**. Parsing 3 times is cheap; correctness is not.

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   PASS 1     │ ──► │   PASS 2     │ ──► │   PASS 3     │
│   GATHER     │     │   STRUCTURE  │     │   FILL       │
│  Info only   │     │  Placeholders│     │  Numbers     │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Pass 1: Information Gathering (Read-Only)
<!-- Lines 20-33 -->

**Goal:** Understand current file state without modifications.

Collect:
- Does TOC exist? If yes: start line, end line, line count
- Header tree: for each header (H2+), record:
  - Line number
  - Level (2, 3, 4...)
  - Title text
  - Does it have a line-range comment on next line? (yes/no/malformed)
- Any structural anomalies (duplicate anchors, orphan TOC entries, etc.)

**Output:** `FileInfo` struct with all gathered data.

### Pass 2: Structure Fixing (Normalize with Placeholders)
<!-- Lines 36-51 -->

**Goal:** Ensure correct structure exists, using placeholders for unknown values.

Actions:
1. **TOC normalization:**
   - If TOC missing and sections exist → insert TOC skeleton with placeholder entries
   - If TOC exists but entries wrong → remove bad entries, insert placeholder entries
   - Placeholder format: `1. [Section Name](#anchor) _(Lines ???-???)_`

2. **Header comment normalization:**
   - If line-range comment missing → insert `<!-- Lines ???-??? -->`
   - If line-range comment malformed → replace with placeholder
   - If line-range comment exists and well-formed → leave as-is (will be updated in Pass 3)

**Output:** File with correct structure, `???` placeholders where numbers will go.

### Pass 3: Fill Numbers (Bottom-to-Top)
<!-- Lines 54-72 -->

**Goal:** Replace all placeholders with computed line numbers.

Process:
1. Parse file again (structure is now stable)
2. Walk headers **bottom-to-top**
3. For each header:
   - Compute `line_start` = header_line + 2 (after comment)
   - Compute `line_end` = (next_header_line - 1) or EOF
   - Replace `???-???` in its comment with actual range
   - Store (title, anchor, start, end) in list
4. When reaching TOC:
   - Replace each placeholder entry with stored data
   - Process top-to-bottom (natural reading order)

**Output:** Final file with all line numbers filled.

---

## 2. Data Model
<!-- Lines 75-75 -->

### 2.1 FileInfo (Pass 1 Output)
<!-- Lines 78-89 -->

```python
@dataclass
class FileInfo:
    lines: list[str]                    # Original file content
    title: str | None                   # H1 content
    title_line: int | None              # H1 line number (1-indexed)

    toc: TocInfo | None                 # None if no TOC found
    headers: list[HeaderInfo]           # All H2+ headers in order
```

### 2.2 TocInfo
<!-- Lines 92-102 -->

```python
@dataclass
class TocInfo:
    header_line: int                    # Line of "## Table of Contents"
    first_entry_line: int               # First numbered entry
    last_entry_line: int                # Last entry (before --- or next section)
    entry_count: int                    # Number of entry lines
    entries: list[TocEntryInfo]         # Parsed entries (may be incomplete)
```

### 2.3 TocEntryInfo
<!-- Lines 105-116 -->

```python
@dataclass
class TocEntryInfo:
    line: int
    indent_level: int                   # 0 = top-level, 1 = indented, etc.
    title: str
    anchor: str
    range_start: int | None             # None if missing or malformed
    range_end: int | None
```

### 2.4 HeaderInfo
<!-- Lines 119-133 -->

```python
@dataclass
class HeaderInfo:
    line: int                           # Line number of header
    level: int                          # 2 for ##, 3 for ###
    title: str                          # Header text
    anchor: str                         # Computed slug

    has_range_comment: bool             # Is there a <!-- Lines --> on next line?
    range_comment_line: int | None      # Line number of comment (if exists)
    range_start: int | None             # Parsed start (None if missing/malformed)
    range_end: int | None               # Parsed end
```

### 2.5 SectionRange (Pass 3 Computation)
<!-- Lines 136-148 -->

```python
@dataclass
class SectionRange:
    title: str
    anchor: str
    level: int
    line_start: int                     # Content start (after header + comment)
    line_end: int                       # Last line before next section or EOF
```

---

## 3. Parsing Rules
<!-- Lines 151-151 -->

### 3.1 Header Detection
<!-- Lines 154-160 -->

```python
HEADER_PATTERN = re.compile(r'^(#{1,6})\s+(.+)$')
```

Match at line start only. Capture level (# count) and title.

### 3.2 Line Range Comment Detection
<!-- Lines 163-173 -->

```python
LINE_RANGE_PATTERN = re.compile(
    r'^<!--\s*Lines?\s+(\d+|[\?]+)\s*[-–—]\s*(\d+|[\?]+)\s*-->$'
)
```

- Matches `<!-- Lines 30-75 -->` or `<!-- Lines ???-??? -->`
- Tolerant of Line/Lines, various dash types
- Must be on its own line, no extra content

### 3.3 TOC Header Detection
<!-- Lines 176-180 -->

```python
TOC_HEADER_PATTERN = re.compile(r'^##\s+Table of Contents\s*$', re.IGNORECASE)
```

### 3.4 TOC Entry Detection
<!-- Lines 183-193 -->

```python
TOC_ENTRY_PATTERN = re.compile(
    r'^(\s*)\d+\.\s+'                           # indent + number
    r'\[([^\]]+)\]'                             # [title]
    r'\(#([^)]+)\)'                             # (#anchor)
    r'(?:\s+_\(Lines?\s+(\d+|[\?]+)\s*[-–—]\s*(\d+|[\?]+)\)_)?'  # optional range
    r'\s*$'
)
```

### 3.5 Anchor Generation
<!-- Lines 196-209 -->

GitHub-compatible heading slug algorithm:

```python
def slugify(title: str) -> str:
    s = strip_inline_markdown(title)   # code spans, emphasis, [text](url) -> text
    s = s.strip().lower()
    s = re.sub(r'[^\w\- ]', '', s)     # \w is Unicode-aware; drop punctuation, no hyphen inserted
    s = s.replace(' ', '-')            # each space -> one hyphen, no collapsing
    return s
```

Duplicate headings receive `-1`, `-2`, ... suffixes in document order (`make_unique_anchors`).

### 3.6 Fenced Code Block Detection
<!-- Lines 212-226 -->

```python
FENCE_PATTERN = re.compile(r'^(\s*)(`{3,}|~{3,})')
```

A fence opens on a line matching this pattern (optionally indented, optional info string
after the marker) and closes only on a later line whose marker uses the **same character**
and is **at least as long** (CommonMark semantics). Every line from the opener through the
closer (inclusive) is fenced content. All line scanners — header detection, TOC-header
detection, TOC-entry parsing, and range-comment detection — skip fenced lines entirely:
they are never treated as headings, TOC structure, or `<!-- Lines -->` comments, and the
tool never inserts or rewrites a comment on a fenced line.

---

## 4. Pass 2: Structure Fixing Rules
<!-- Lines 229-229 -->

### 4.1 TOC Handling
<!-- Lines 232-251 -->

| Current State | Action |
|---------------|--------|
| No TOC, no sections | Do nothing |
| No TOC, has sections | Insert full TOC with placeholders |
| TOC exists, correct entry count | Keep structure, placeholders if needed |
| TOC exists, wrong entry count | Regenerate entries with placeholders |

**TOC insertion point:** After H1 + blank line, or line 1 if no H1.

**TOC template:**
```markdown
## Table of Contents

1. [Section](#section) _(Lines ???-???)_

---

```

### 4.2 Header Comment Handling
<!-- Lines 254-260 -->

| Current State | Action |
|---------------|--------|
| No comment after header | Insert `<!-- Lines ???-??? -->` |
| Comment exists, well-formed | Leave as-is (numbers may be wrong, fixed in Pass 3) |
| Comment exists, malformed | Replace with `<!-- Lines ???-??? -->` |

### 4.3 Placeholder Format
<!-- Lines 263-271 -->

```
???-???
```

Three question marks each side. Easy to detect, impossible to confuse with real numbers.

---

## 5. Pass 3: Number Filling Rules
<!-- Lines 274-274 -->

### 5.1 Line Range Computation
<!-- Lines 277-293 -->

For header H at line L with comment at line L+1:

```
content_start = L + 2          # First line after comment
content_end = next_header - 1  # Line before next header
            = EOF_line         # If last section
```

**Special case:** If header is immediately followed by another header (no content):
```
content_start = L + 2
content_end = L + 1            # Empty range: start > end, display as "L+2-L+1"
```

Actually, better: `content_end = content_start - 1` signals empty section.

### 5.2 Bottom-to-Top Processing
<!-- Lines 296-329 -->

```python
def fill_numbers(lines: list[str], headers: list[HeaderInfo]) -> list[str]:
    ranges = []

    # Process bottom-to-top
    for i, header in enumerate(reversed(headers)):
        # Next header is previous in reversed list (or EOF)
        if i == 0:
            content_end = len(lines)
        else:
            next_header = headers[-(i)]  # Previous in reversed order
            content_end = next_header.line - 1

        content_start = header.line + 2  # After header + comment

        # Update the comment line
        comment_line_idx = header.line  # 0-indexed: header.line is 1-indexed
        lines[comment_line_idx] = f'<!-- Lines {content_start}-{content_end} -->'

        # Store for TOC
        ranges.append(SectionRange(
            title=header.title,
            anchor=header.anchor,
            level=header.level,
            line_start=content_start,
            line_end=content_end,
        ))

    # Reverse to get top-to-bottom order for TOC
    ranges.reverse()
    return lines, ranges
```

### 5.3 TOC Entry Generation
<!-- Lines 332-342 -->

```python
def format_toc_entry(section: SectionRange, indent: int) -> str:
    spaces = '   ' * indent  # 3 spaces per level
    return f'{spaces}1. [{section.title}](#{section.anchor}) _(Lines {section.line_start}-{section.line_end})_'
```

Numbering is always `1.` — markdown renderers auto-number.

---

## 6. Configuration
<!-- Lines 345-357 -->

```python
@dataclass
class Config:
    min_level: int = 2                      # Track H2+
    max_level: int = 4                      # Up to H4
    include_line_comments: bool = True      # Add <!-- Lines --> after headers
    toc_title: str = "Table of Contents"    # TOC header text
    placeholder: str = "???"                # Placeholder for unknown numbers
```

---

## 7. Module Structure
<!-- Lines 360-374 -->

```
md_structure_sync/
├── __init__.py
├── models.py           # Dataclasses from Section 2
├── parse.py            # Pass 1: gather_info(lines, config) → FileInfo
├── structure.py        # Pass 2: fix_structure(lines, info, config) → list[str]
├── fill.py             # Pass 3: fill_numbers(lines, config) → list[str]
├── sync.py             # Orchestrator: sync_file(path, config) → SyncResult
├── anchors.py          # slugify(), handle duplicates
└── cli.py              # Entry point
```

---

## 8. Sync Orchestrator
<!-- Lines 377-405 -->

```python
def sync_file(path: Path, config: Config) -> SyncResult:
    # Read
    lines = path.read_text().splitlines(keepends=True)

    # Pass 1: Gather
    info = gather_info(lines, config)

    # Pass 2: Structure (may modify lines)
    lines = fix_structure(lines, info, config)

    # Pass 3: Fill numbers
    lines = fill_numbers(lines, config)

    # Write if changed
    new_content = ''.join(lines)
    old_content = path.read_text()

    if new_content != old_content:
        if not config.dry_run:
            path.write_text(new_content)
        return SyncResult(changed=True, path=path)

    return SyncResult(changed=False, path=path)
```

---

## 9. Robustness Matrix
<!-- Lines 408-423 -->

| Input State | Pass 1 Detects | Pass 2 Fixes | Pass 3 Fills |
|-------------|----------------|--------------|--------------|
| Perfect file | All info | No changes | No changes (idempotent) |
| No TOC | toc=None | Insert TOC skeleton | Fill TOC entries |
| TOC with wrong numbers | entries with wrong ranges | Keep structure | Correct numbers |
| TOC missing entries | entry count mismatch | Regenerate entries | Fill entries |
| TOC extra entries | entry count mismatch | Regenerate entries | Fill entries |
| Header missing comment | has_range_comment=False | Insert placeholder | Fill number |
| Header wrong comment | range values wrong | Keep (well-formed) | Correct number |
| Header malformed comment | detected as malformed | Replace with placeholder | Fill number |
| Empty file | No sections | No changes | No changes |
| Only H1 | No H2+ headers | No changes | No changes |

---

## 10. Test Cases
<!-- Lines 426-426 -->

### File States
<!-- Lines 429-441 -->
- [ ] Empty file
- [ ] H1 only
- [ ] H1 + H2 sections, no TOC
- [ ] Complete and correct (idempotent check)
- [ ] TOC numbers all wrong
- [ ] TOC missing some entries
- [ ] TOC has extra/deleted entries
- [ ] Nested sections (H2 → H3 → H4)
- [ ] Header comments all missing
- [ ] Header comments all wrong
- [ ] Header comments partially present
- [ ] Malformed comments (extra text, wrong format)

### Edge Cases
<!-- Lines 444-450 -->
- [ ] Empty section (consecutive headers)
- [ ] Last section to EOF
- [ ] Duplicate section titles
- [ ] Special chars in titles: `Code & "Quotes"`
- [ ] Windows line endings (CRLF)
- [ ] No trailing newline
- [ ] Very long file (1000+ lines)
