"""Tests for Pass 1: parsing."""

import pytest

from md_structure_sync.models import Config
from md_structure_sync.parse import gather_info


def lines(text: str) -> list[str]:
    """Convert text to lines with newlines."""
    return [line + "\n" for line in text.strip().split("\n")]


class TestFindTitle:
    """Tests for H1 title detection."""

    def test_h1_at_start(self):
        content = lines("""# My Document

Some content here.
""")
        info = gather_info(content, Config())
        assert info.title == "My Document"
        assert info.title_line == 1

    def test_no_h1(self):
        content = lines("""## First Section

Content.
""")
        info = gather_info(content, Config())
        assert info.title is None
        assert info.title_line is None

    def test_h1_with_extra_spaces(self):
        content = lines("""#   Spaced Title

Content.
""")
        info = gather_info(content, Config())
        assert info.title == "Spaced Title"

    def test_h1_not_first_line(self):
        # H1 should still be found even if not on line 1
        # Note: lines() strips, so we build manually
        content = ["\n", "# Document Title\n", "\n", "Content.\n"]
        info = gather_info(content, Config())
        assert info.title == "Document Title"
        assert info.title_line == 2


class TestFindToc:
    """Tests for TOC detection."""

    def test_no_toc(self):
        content = lines("""# Title

## Section One

Content.
""")
        info = gather_info(content, Config())
        assert info.toc is None

    def test_toc_with_entries(self):
        content = lines("""# Title

## Table of Contents

1. [Section One](#section-one) _(Lines 10-20)_
2. [Section Two](#section-two) _(Lines 21-30)_

---

## Section One

Content.
""")
        info = gather_info(content, Config())
        assert info.toc is not None
        assert info.toc.header_line == 3
        assert info.toc.entry_count == 2
        assert info.toc.separator_line == 8

        # Check first entry
        entry1 = info.toc.entries[0]
        assert entry1.title == "Section One"
        assert entry1.anchor == "section-one"
        assert entry1.range_start == 10
        assert entry1.range_end == 20

    def test_toc_with_placeholders(self):
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines ???-???)_

---
""")
        info = gather_info(content, Config())
        assert info.toc is not None
        assert info.toc.entries[0].range_start is None
        assert info.toc.entries[0].range_end is None

    def test_toc_nested_entries(self):
        content = lines("""## Table of Contents

1. [Section One](#section-one) _(Lines 10-50)_
   1. [Subsection](#subsection) _(Lines 15-30)_
2. [Section Two](#section-two) _(Lines 51-100)_

---
""")
        info = gather_info(content, Config())
        assert info.toc.entry_count == 3
        assert info.toc.entries[0].indent_level == 0
        assert info.toc.entries[1].indent_level == 1
        assert info.toc.entries[2].indent_level == 0

    def test_toc_without_separator(self):
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines 10-20)_

## Section

Content.
""")
        info = gather_info(content, Config())
        assert info.toc is not None
        assert info.toc.separator_line is None
        assert info.toc.entry_count == 1

    def test_toc_case_insensitive(self):
        content = lines("""## table of contents

1. [Section](#section)

---
""")
        info = gather_info(content, Config())
        assert info.toc is not None

    def test_toc_entries_without_line_range(self):
        content = lines("""## Table of Contents

1. [Section One](#section-one)
2. [Section Two](#section-two)

---
""")
        info = gather_info(content, Config())
        assert info.toc.entry_count == 2
        assert info.toc.entries[0].range_start is None

    def test_empty_toc(self):
        content = lines("""## Table of Contents

---
""")
        info = gather_info(content, Config())
        assert info.toc is not None
        assert info.toc.entry_count == 0
        assert info.toc.first_entry_line is None


class TestFindHeaders:
    """Tests for header detection."""

    def test_h2_headers(self):
        content = lines("""# Title

## First Section

Content.

## Second Section

More content.
""")
        info = gather_info(content, Config())
        assert len(info.headers) == 2
        assert info.headers[0].title == "First Section"
        assert info.headers[0].level == 2
        assert info.headers[0].line == 3
        assert info.headers[1].title == "Second Section"
        assert info.headers[1].line == 7

    def test_nested_headers(self):
        content = lines("""## Section

### Subsection

#### Detail
""")
        info = gather_info(content, Config())
        assert len(info.headers) == 3
        assert info.headers[0].level == 2
        assert info.headers[1].level == 3
        assert info.headers[2].level == 4

    def test_header_level_filtering(self):
        config = Config(min_level=2, max_level=3)
        content = lines("""# Title

## Section

### Subsection

#### Too Deep
""")
        info = gather_info(content, config)
        assert len(info.headers) == 2
        assert info.headers[0].level == 2
        assert info.headers[1].level == 3

    def test_skip_toc_header(self):
        content = lines("""## Table of Contents

1. [Section](#section)

---

## Section

Content.
""")
        info = gather_info(content, Config())
        # Should not include TOC header
        assert len(info.headers) == 1
        assert info.headers[0].title == "Section"

    def test_header_with_range_comment(self):
        content = lines("""## Section
<!-- Lines 5-20 -->

Content here.
""")
        info = gather_info(content, Config())
        assert info.headers[0].has_range_comment is True
        assert info.headers[0].range_comment_line == 2
        assert info.headers[0].range_start == 5
        assert info.headers[0].range_end == 20

    def test_header_with_placeholder_comment(self):
        content = lines("""## Section
<!-- Lines ???-??? -->

Content.
""")
        info = gather_info(content, Config())
        assert info.headers[0].has_range_comment is True
        assert info.headers[0].is_placeholder is True
        assert info.headers[0].range_start is None

    def test_header_without_comment(self):
        content = lines("""## Section

Content without comment.
""")
        info = gather_info(content, Config())
        assert info.headers[0].has_range_comment is False
        assert info.headers[0].range_comment_line is None

    def test_anchor_generation(self):
        content = lines("""## My Special Section (v2)

Content.
""")
        info = gather_info(content, Config())
        assert info.headers[0].anchor == "my-special-section-v2"

    def test_various_dash_types_in_comment(self):
        # Test en-dash and em-dash
        content = lines("""## Section One
<!-- Lines 5–20 -->

## Section Two
<!-- Lines 25—40 -->
""")
        info = gather_info(content, Config())
        assert info.headers[0].range_start == 5
        assert info.headers[0].range_end == 20
        assert info.headers[1].range_start == 25
        assert info.headers[1].range_end == 40


class TestFencedCodeBlocks:
    """Headers, TOC entries and line-range comments inside fenced code blocks
    must be ignored, matching CommonMark fence semantics (a fence closes only
    on a line with the same marker character and at least the same length).
    """

    def test_fenced_heading_not_a_header(self):
        content = lines("""# Title

## Real Section

```markdown
## Fenced Heading
```

Content.
""")
        info = gather_info(content, Config())
        titles = [h.title for h in info.headers]
        assert titles == ["Real Section"]

    def test_fenced_heading_not_in_toc_scan(self):
        # A TOC-detection pass must not pick up a "## Table of Contents"
        # look-alike inside a fence, nor treat fenced text as terminating
        # the TOC scan.
        content = lines("""## Table of Contents

1. [Real Section](#real-section) _(Lines 10-20)_

---

## Real Section

```markdown
## Table of Contents

1. [Fake](#fake)
```

Content.
""")
        info = gather_info(content, Config())
        assert info.toc is not None
        assert info.toc.entry_count == 1
        assert info.toc.entries[0].title == "Real Section"

    def test_fenced_line_range_comment_not_detected(self):
        content = lines("""## Real Section

```markdown
## Example
<!-- Lines 1-2 -->
```

Content.
""")
        info = gather_info(content, Config())
        assert len(info.headers) == 1
        assert info.headers[0].title == "Real Section"
        assert info.headers[0].has_range_comment is False

    def test_tilde_fence_ignored(self):
        content = lines("""## Real Section

~~~markdown
## Fenced Heading
~~~

Content.
""")
        info = gather_info(content, Config())
        titles = [h.title for h in info.headers]
        assert titles == ["Real Section"]

    def test_indented_fence_ignored(self):
        content = lines("""## Real Section

   ```markdown
   ## Fenced Heading
   ```

Content.
""")
        info = gather_info(content, Config())
        titles = [h.title for h in info.headers]
        assert titles == ["Real Section"]

    def test_nested_fences_longer_marker_required_to_close(self):
        # A fence of length 4 is not closed by a marker of length 3; the
        # shorter, inner-looking marker is just fenced content.
        content = lines("""## Real Section

````markdown
```
## Still Fenced
```
````

## Second Real Section
""")
        info = gather_info(content, Config())
        titles = [h.title for h in info.headers]
        assert titles == ["Real Section", "Second Real Section"]

    def test_fence_closed_by_same_or_longer_marker(self):
        content = lines("""## Real Section

```markdown
## Fenced Heading
````

## After Fence
""")
        info = gather_info(content, Config())
        titles = [h.title for h in info.headers]
        assert titles == ["Real Section", "After Fence"]

    def test_mismatched_marker_char_does_not_close_fence(self):
        # A ``` fence is not closed by a ~~~ line (different marker char).
        content = lines("""## Real Section

```markdown
## Fenced Heading
~~~
## Still Fenced
```

## After Fence
""")
        info = gather_info(content, Config())
        titles = [h.title for h in info.headers]
        assert titles == ["Real Section", "After Fence"]


class TestEdgeCases:
    """Edge case tests."""

    def test_empty_file(self):
        info = gather_info([], Config())
        assert info.title is None
        assert info.toc is None
        assert info.headers == []

    def test_only_h1(self):
        content = lines("""# Just a Title
""")
        info = gather_info(content, Config())
        assert info.title == "Just a Title"
        assert info.headers == []

    def test_consecutive_headers(self):
        content = lines("""## First

## Second

## Third
""")
        info = gather_info(content, Config())
        assert len(info.headers) == 3

    def test_header_at_eof(self):
        content = ["## Last Section\n"]
        info = gather_info(content, Config())
        assert len(info.headers) == 1
        assert info.headers[0].has_range_comment is False
