"""Tests for Pass 3: filling line numbers."""

import pytest

from md_structure_sync.models import Config
from md_structure_sync.fill import fill_numbers
from md_structure_sync.parse import gather_info
from md_structure_sync.structure import fix_structure

# Config that adds TOC when there are headers (for full_sync tests expecting TOC)
ADD_TOC_CONFIG = Config(toc_policy="add_always")


def lines(text: str) -> list[str]:
    """Convert text to lines with newlines."""
    return [line + "\n" for line in text.strip().split("\n")]


def to_text(lines_list: list[str]) -> str:
    """Convert lines back to text."""
    return "".join(lines_list)


def full_sync(content: list[str], config: Config = None) -> list[str]:
    """Run all three passes."""
    config = config or Config()
    info = gather_info(content, config)
    result = fix_structure(content, info, config)
    result = fill_numbers(result, config)
    return result


class TestRangeComputation:
    """Tests for line range computation."""

    def test_single_section_to_eof(self):
        content = lines("""## Section
<!-- Lines ???-??? -->

Content line 1.
Content line 2.
Content line 3.
""")
        result = fill_numbers(content, Config())
        text = to_text(result)

        # Section content starts at line 3 (after header + comment)
        # Ends at line 6 (last line)
        assert "<!-- Lines 3-6 -->" in text

    def test_two_sections(self):
        content = lines("""## First
<!-- Lines ???-??? -->

Content.

## Second
<!-- Lines ???-??? -->

More content.
""")
        result = fill_numbers(content, Config())
        text = to_text(result)

        # First: lines 3-5 (before "## Second" on line 6)
        # Second: lines 8-9 (9 lines total after strip)
        assert "<!-- Lines 3-5 -->" in text
        assert "<!-- Lines 8-9 -->" in text

    def test_consecutive_headers_empty_section(self):
        content = lines("""## First
<!-- Lines ???-??? -->

## Second
<!-- Lines ???-??? -->

Content.
""")
        result = fill_numbers(content, Config())
        text = to_text(result)

        # First section has no content (line 3, but Second starts at line 4)
        # So first is 3-3
        assert "<!-- Lines 3-3 -->" in text
        assert "<!-- Lines 6-7 -->" in text

    def test_nested_sections(self):
        content = lines("""## Parent
<!-- Lines ???-??? -->

Parent content.

### Child
<!-- Lines ???-??? -->

Child content.

## Sibling
<!-- Lines ???-??? -->

Sibling content.
""")
        result = fill_numbers(content, Config())
        text = to_text(result)

        # Parent: 3-5 (up to Child header - 1)
        # Child: 8-10
        # Sibling: 13-14 (14 lines after strip)
        assert "<!-- Lines 3-5 -->" in text
        assert "<!-- Lines 8-10 -->" in text
        assert "<!-- Lines 13-14 -->" in text


class TestTocFilling:
    """Tests for TOC line number filling."""

    def test_fill_toc_entries(self):
        content = lines("""## Table of Contents

1. [Section One](#section-one) _(Lines ???-???)_
2. [Section Two](#section-two) _(Lines ???-???)_

---

## Section One
<!-- Lines ???-??? -->

Content one.

## Section Two
<!-- Lines ???-??? -->

Content two.
""")
        result = fill_numbers(content, Config())
        text = to_text(result)

        # TOC should have real line numbers
        assert "_(Lines 10-12)_" in text  # Section One
        assert "_(Lines 15-16)_" in text  # Section Two (16 lines after strip)

    def test_toc_matches_header_comments(self):
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines ???-???)_

---

## Section
<!-- Lines ???-??? -->

Content.
""")
        result = fill_numbers(content, Config())
        text = to_text(result)

        # Both should show same range
        assert text.count("9-10") == 2  # In TOC and in comment


class TestFullPipeline:
    """Integration tests running all three passes."""

    def test_file_with_nothing(self):
        content = lines("""# Title

## Section One

Some content here.

## Section Two

### Subsection

Nested content.

## Section Three

Final content.
""")
        result = full_sync(content, ADD_TOC_CONFIG)
        text = to_text(result)

        # Should have TOC
        assert "## Table of Contents" in text
        assert "[Section One]" in text
        assert "[Section Two]" in text
        assert "[Subsection]" in text
        assert "[Section Three]" in text

        # Should have separator
        assert "---" in text

        # Should have comments with real line numbers
        assert "<!-- Lines" in text
        assert "???" not in text  # No placeholders remaining

    def test_idempotent(self):
        # Running twice should produce identical output
        content = lines("""# Document

## First

Content.

## Second

More.
""")
        result1 = full_sync(content, ADD_TOC_CONFIG)
        result2 = full_sync(result1, ADD_TOC_CONFIG)

        assert result1 == result2

    def test_fix_wrong_line_numbers(self):
        # File with incorrect line numbers
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines 999-1000)_

---

## Section
<!-- Lines 888-999 -->

Content.
""")
        result = full_sync(content)
        text = to_text(result)

        # Should have correct line numbers
        assert "999" not in text
        assert "888" not in text

    def test_corrupted_toc_recovery(self):
        # TOC is completely wrong
        content = lines("""## Table of Contents

1. [Wrong](#wrong) _(Lines 1-2)_
2. [Also Wrong](#also-wrong)
   1. [Nested Wrong](#nested-wrong) _(Lines 5-10)_

---

## Actual Section

Content here.

## Another Section

More content.
""")
        result = full_sync(content)
        text = to_text(result)

        # Should have correct entries
        assert "[Actual Section](#actual-section)" in text
        assert "[Another Section](#another-section)" in text
        assert "[Wrong]" not in text

    def test_header_without_comment_gets_one(self):
        content = lines("""## Table of Contents

1. [Section](#section) _(Lines 8-10)_

---

## Section

Content without comment initially.
""")
        result = full_sync(content)
        text = to_text(result)

        # Should have comment after header
        lines_list = text.split("\n")
        section_idx = None
        for i, line in enumerate(lines_list):
            if line.strip() == "## Section":
                section_idx = i
                break

        assert section_idx is not None
        # Next line should be a comment
        assert "<!-- Lines" in lines_list[section_idx + 1]


class TestEdgeCases:
    """Edge case tests for the full pipeline."""

    def test_empty_file(self):
        result = full_sync([])
        assert result == []

    def test_only_title(self):
        content = lines("""# Just a Title
""")
        result = full_sync(content)
        # No TOC needed, should be mostly unchanged
        assert "Table of Contents" not in to_text(result)

    def test_special_characters_in_title(self):
        content = lines("""## Code & Examples (v2)

Content.
""")
        result = full_sync(content, ADD_TOC_CONFIG)
        text = to_text(result)

        # GitHub-compatible slug: "&" is dropped (not hyphenated), so the two
        # spaces either side of it become two hyphens: "code--examples-v2".
        assert "[Code & Examples (v2)](#code--examples-v2)" in text

    def test_duplicate_section_titles(self):
        content = lines("""## Section

First content.

## Section

Second content.
""")
        result = full_sync(content, ADD_TOC_CONFIG)
        text = to_text(result)

        # Both should appear in TOC
        # Second one gets -1 suffix
        assert "[Section](#section)" in text
        assert "[Section](#section-1)" in text

    def test_very_long_section(self):
        # Section with many lines
        content_lines = ["## Section\n", "<!-- Lines ???-??? -->\n", "\n"]
        for i in range(100):
            content_lines.append(f"Line {i}\n")

        result = fill_numbers(content_lines, Config())
        text = to_text(result)

        # Should have correct range
        assert "<!-- Lines 3-103 -->" in text

    def test_no_trailing_newline(self):
        content = ["## Section\n", "<!-- Lines ???-??? -->\n", "\n", "Content"]
        # Last line has no newline
        result = fill_numbers(content, Config())

        # Should still work
        assert "<!-- Lines 3-4 -->" in to_text(result)

    def test_windows_line_endings(self):
        content = [
            "## Section\r\n",
            "<!-- Lines ???-??? -->\r\n",
            "\r\n",
            "Content.\r\n",
        ]
        result = fill_numbers(content, Config())
        # Should handle gracefully (though output format may change)
        assert "Lines 3-4" in to_text(result)
