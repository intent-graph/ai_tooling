"""Tests for Pass 2: structure fixing."""

import pytest

from md_structure_sync.models import Config
from md_structure_sync.parse import gather_info
from md_structure_sync.structure import fix_structure

# Config that adds TOC when there are headers (for tests expecting TOC insertion)
ADD_TOC_CONFIG = Config(toc_policy="add_always")


def lines(text: str) -> list[str]:
    """Convert text to lines with newlines."""
    return [line + "\n" for line in text.strip().split("\n")]


def to_text(lines: list[str]) -> str:
    """Convert lines back to text."""
    return "".join(lines)


class TestHeaderCommentInsertion:
    """Tests for inserting missing line range comments."""

    def test_insert_single_comment(self):
        content = lines("""# Title

## Section

Content here.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())

        assert "<!-- Lines ???-??? -->" in to_text(result)

    def test_insert_multiple_comments(self):
        content = lines("""## First

Content.

## Second

More content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())
        text = to_text(result)

        # Should have two placeholder comments
        assert text.count("<!-- Lines ???-??? -->") == 2

    def test_preserve_existing_comment(self):
        content = lines("""## Section
<!-- Lines 5-20 -->

Content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())

        # Original comment should be preserved (numbers will be fixed in Pass 3)
        assert "<!-- Lines 5-20 -->" in to_text(result)

    def test_mixed_present_missing_comments(self):
        content = lines("""## First
<!-- Lines 10-20 -->

Content.

## Second

More content.

## Third
<!-- Lines 50-60 -->

Even more.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())
        text = to_text(result)

        # First and third have comments, second needs one
        assert "<!-- Lines 10-20 -->" in text
        assert "<!-- Lines 50-60 -->" in text
        assert "<!-- Lines ???-??? -->" in text

    def test_no_comments_when_disabled(self):
        config = Config(include_line_comments=False)
        content = lines("""## Section

Content.
""")
        info = gather_info(content, config)
        result = fix_structure(content, info, config)

        assert "<!-- Lines" not in to_text(result)


class TestTocInsertion:
    """Tests for inserting missing TOC."""

    def test_insert_toc_after_h1(self):
        content = lines("""# Title

## Section One

Content.

## Section Two

More content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, ADD_TOC_CONFIG)
        text = to_text(result)

        assert "## Table of Contents" in text
        assert "[Section One](#section-one)" in text
        assert "[Section Two](#section-two)" in text
        assert "---" in text

    def test_insert_toc_at_start_no_h1(self):
        content = lines("""## Section One

Content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, ADD_TOC_CONFIG)
        text = to_text(result)

        # TOC should be at the very start
        assert text.startswith("## Table of Contents")

    def test_no_toc_for_empty_file(self):
        content = lines("""# Just a Title
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())

        assert "Table of Contents" not in to_text(result)

    def test_toc_entries_have_placeholders(self):
        content = lines("""## Section

Content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, ADD_TOC_CONFIG)
        text = to_text(result)

        assert "_(Lines ???-???)_" in text

    def test_nested_toc_entries(self):
        content = lines("""## Section

### Subsection

Content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, ADD_TOC_CONFIG)
        text = to_text(result)

        # Subsection should be indented
        assert "   1. [Subsection]" in text


class TestTocRebuild:
    """Tests for rebuilding corrupted/mismatched TOC."""

    def test_rebuild_toc_missing_entries(self):
        # TOC has fewer entries than actual sections
        content = lines("""## Table of Contents

1. [Section One](#section-one) _(Lines 10-20)_

---

## Section One

Content.

## Section Two

More content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())  # maintain_only still rebuilds existing TOC
        text = to_text(result)

        # Should now have both entries
        assert "[Section One]" in text
        assert "[Section Two]" in text

    def test_rebuild_toc_extra_entries(self):
        # TOC has more entries than actual sections
        content = lines("""## Table of Contents

1. [Section One](#section-one) _(Lines 10-20)_
2. [Deleted Section](#deleted-section) _(Lines 21-30)_
3. [Section Two](#section-two) _(Lines 31-40)_

---

## Section One

Content.

## Section Two

More content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())
        text = to_text(result)

        # Should only have actual sections
        assert "[Section One]" in text
        assert "[Section Two]" in text
        assert "[Deleted Section]" not in text

    def test_rebuild_toc_wrong_order(self):
        # TOC entries in wrong order
        content = lines("""## Table of Contents

1. [Section Two](#section-two) _(Lines 20-30)_
2. [Section One](#section-one) _(Lines 10-19)_

---

## Section One

First content.

## Section Two

Second content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())
        text = to_text(result)

        # Order should match actual headers
        one_pos = text.find("[Section One]")
        two_pos = text.find("[Section Two]")
        assert one_pos < two_pos

    def test_rebuild_toc_duplicate_entries(self):
        # TOC has duplicate entries
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines 10-20)_
2. [Section](#section) _(Lines 10-20)_

---

## Section

Content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())
        text = to_text(result)

        # Should have exactly one entry
        assert text.count("[Section](#section)") == 1

    def test_preserve_correct_toc(self):
        # TOC is already correct (right entries, right order)
        content = lines("""## Table of Contents

1. [Section One](#section-one) _(Lines 10-20)_
2. [Section Two](#section-two) _(Lines 21-30)_

---

## Section One
<!-- Lines 10-20 -->

Content.

## Section Two
<!-- Lines 21-30 -->

More content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())

        # Structure should be mostly preserved
        # (exact line numbers may differ after Pass 3)
        assert "[Section One]" in to_text(result)
        assert "[Section Two]" in to_text(result)

    def test_toc_with_wrong_anchors(self):
        # TOC anchors don't match header anchors
        content = lines("""## Table of Contents

1. [Section One](#wrong-anchor) _(Lines 10-20)_

---

## Section One

Content.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, Config())
        text = to_text(result)

        # Should have correct anchor
        assert "[Section One](#section-one)" in text


class TestComplexCases:
    """Tests for complex scenarios."""

    def test_toc_insert_and_comments_together(self):
        # No TOC, no comments
        content = lines("""# My Document

## Introduction

Welcome.

## Details

### Subdetail

Info.

## Conclusion

The end.
""")
        info = gather_info(content, Config())
        result = fix_structure(content, info, ADD_TOC_CONFIG)
        text = to_text(result)

        # Should have TOC with all entries
        assert "## Table of Contents" in text
        assert "[Introduction]" in text
        assert "[Details]" in text
        assert "[Subdetail]" in text
        assert "[Conclusion]" in text

        # Should have comments after each header
        assert text.count("<!-- Lines ???-??? -->") >= 4

    def test_deeply_nested_structure(self):
        config = Config(min_level=2, max_level=4, toc_policy="add_always")
        content = lines("""## Level 2

### Level 3

#### Level 4

Content.
""")
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        text = to_text(result)

        # Check indentation in TOC
        assert "1. [Level 2]" in text
        assert "   1. [Level 3]" in text
        assert "      1. [Level 4]" in text


class TestTocPolicy:
    """Tests for TOC policy options: maintain_only, add_above_size, remove."""

    def test_maintain_only_does_not_add_toc(self):
        content = lines("""# Doc

## Section One

Content.

## Section Two

More.
""")
        config = Config(toc_policy="maintain_only")
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        text = to_text(result)
        assert "Table of Contents" not in text

    def test_maintain_only_keeps_existing_toc(self):
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines ???-???)_

---

## Section

Content.
""")
        config = Config(toc_policy="maintain_only")
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        text = to_text(result)
        assert "## Table of Contents" in text
        assert "[Section]" in text

    def test_add_above_size_adds_when_at_least_n_headers(self):
        content = lines("""# Doc

## One

## Two

## Three

Content.
""")
        config = Config(toc_policy="add_above_size", toc_min_headers=3)
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        text = to_text(result)
        assert "## Table of Contents" in text
        assert "[One]" in text
        assert "[Two]" in text
        assert "[Three]" in text

    def test_add_above_size_does_not_add_below_threshold(self):
        content = lines("""# Doc

## One

## Two

Content.
""")
        config = Config(toc_policy="add_above_size", toc_min_headers=3)
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        text = to_text(result)
        assert "Table of Contents" not in text

    def test_remove_strips_toc_block(self):
        content = lines("""# Doc

## Table of Contents

1. [Section](#section) _(Lines 10-20)_

---

## Section

Content.
""")
        config = Config(toc_policy="remove")
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        text = to_text(result)
        assert "Table of Contents" not in text
        assert "## Section" in text
        assert "Content." in text

    def test_remove_no_toc_is_noop(self):
        content = lines("""## Section

Content.
""")
        config = Config(toc_policy="remove")
        info = gather_info(content, config)
        result = fix_structure(content, info, config)
        assert to_text(result) == to_text(content)
