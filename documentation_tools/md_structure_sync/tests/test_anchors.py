"""Tests for anchor generation.

`slugify` implements GitHub's heading-anchor algorithm: strip inline markdown
(code spans literal, links reduced to display text, `*`/`~~` emphasis always
removed, `_` emphasis removed only when it forms a matched non-intraword
pair), lowercase, drop every remaining character that is not a Unicode
letter/number, `-`, `_` or space (no hyphen substituted for the removed
character), then turn each remaining space into a hyphen. See `anchors.py`
module docstring for the full rule and rationale.
"""

import pytest

from md_structure_sync.anchors import make_unique_anchors, slugify


class TestSlugify:
    """Tests for slugify function (GitHub-compatible heading slugs)."""

    def test_simple_title(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_characters(self):
        # Punctuation is removed, not replaced by a hyphen: adjacent spaces
        # left behind by removed characters become adjacent hyphens.
        assert slugify("Code & Examples") == "code--examples"
        assert slugify("Version (v2)") == "version-v2"
        assert slugify("What's New?") == "whats-new"

    def test_numbers(self):
        assert slugify("Section 1") == "section-1"
        # Dots between digits are removed (not hyphenated): "3.1.4" -> "314".
        assert slugify("3.1.4 Details") == "314-details"

    def test_slice_style_heading(self):
        # Report case: "Slice 3.1: UNDERSTAND" -> "slice-31-understand"
        assert slugify("Slice 3.1: UNDERSTAND") == "slice-31-understand"

    def test_filename_style_heading(self):
        # Report case: "CONTRIBUTING.md" -> "contributingmd" (dot dropped,
        # no hyphen inserted, no space to convert).
        assert slugify("CONTRIBUTING.md") == "contributingmd"

    def test_em_dash_heading(self):
        # Report case: em dash is removed; the spaces around it survive and
        # each becomes its own hyphen.
        assert slugify("Agent Primers — Start Here") == "agent-primers--start-here"

    def test_multiple_spaces(self):
        # GitHub does not collapse runs of spaces: each becomes its own hyphen.
        assert slugify("Too   Many    Spaces") == "too---many----spaces"

    def test_leading_trailing_special(self):
        # GitHub does not strip leading/trailing hyphens.
        assert slugify("---Leading") == "---leading"
        assert slugify("Trailing---") == "trailing---"
        assert slugify("---Both---") == "---both---"

    def test_all_special_chars(self):
        assert slugify("@#$%^&*()") == ""

    def test_unicode(self):
        # GitHub keeps Unicode letters; only punctuation/symbols are dropped.
        assert slugify("Café") == "café"
        assert slugify("Hypothèse de départ") == "hypothèse-de-départ"
        assert slugify("日本語") == "日本語"

    def test_empty_string(self):
        assert slugify("") == ""

    def test_strips_inline_code(self):
        assert slugify("The `foo` function") == "the-foo-function"

    def test_strips_emphasis_markers(self):
        assert slugify("**Bold** and *italic*") == "bold-and-italic"

    def test_strips_markdown_links(self):
        # [text](url) reduces to its display text before slugifying.
        assert slugify("See [the guide](https://example.com/guide)") == "see-the-guide"

    def test_intraword_underscores_survive(self):
        # Underscores inside a word are not emphasis in GFM: they stay,
        # unlike the old (buggy) unconditional-strip behavior.
        assert slugify("line_profiler") == "line_profiler"
        assert slugify("memory_profiler") == "memory_profiler"

    def test_intraword_underscore_in_longer_heading(self):
        assert slugify("Comparison to STEP_IO_PROTOCOL") == "comparison-to-step_io_protocol"

    def test_dunder_name_is_real_emphasis(self):
        # "__main__" is a matched, non-intraword underscore-emphasis pair
        # (GitHub renders it bold), so the underscores ARE stripped here.
        assert slugify("__main__.py") == "mainpy"

    def test_dunder_name_inside_code_span_survives(self):
        # Same text, but inside a code span: GFM code-span content is
        # literal, so the underscores are never treated as emphasis.
        assert slugify("`__init__.py`") == "__init__py"

    def test_unpaired_leading_underscore_survives(self):
        # A single leading underscore with no matching closer is not
        # emphasis; GitHub keeps it.
        assert slugify("_private helper") == "_private-helper"

    def test_star_emphasis_stripped_underscore_in_code_span_kept(self):
        assert slugify("**Bold** and `snake_case`") == "bold-and-snake_case"


class TestMakeUniqueAnchors:
    """Tests for duplicate anchor handling."""

    def test_no_duplicates(self):
        titles = ["First", "Second", "Third"]
        assert make_unique_anchors(titles) == ["first", "second", "third"]

    def test_simple_duplicate(self):
        titles = ["Section", "Section"]
        assert make_unique_anchors(titles) == ["section", "section-1"]

    def test_triple_duplicate(self):
        titles = ["Section", "Section", "Section"]
        assert make_unique_anchors(titles) == ["section", "section-1", "section-2"]

    def test_mixed_duplicates(self):
        titles = ["Intro", "Details", "Intro", "Summary", "Details"]
        assert make_unique_anchors(titles) == [
            "intro",
            "details",
            "intro-1",
            "summary",
            "details-1",
        ]

    def test_empty_list(self):
        assert make_unique_anchors([]) == []

    def test_single_item(self):
        assert make_unique_anchors(["Only One"]) == ["only-one"]
