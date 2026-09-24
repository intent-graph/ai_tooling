"""Tests for cross-reference parsing."""

import pytest

from md_structure_sync.cross_refs import (
    parse_cross_refs,
    resolve_target_path,
    get_unique_target_paths,
)
from pathlib import Path


def lines(text: str) -> list[str]:
    """Convert text to lines with newlines."""
    return [line + "\n" for line in text.strip().split("\n")]


class TestParseCrossRefs:
    """Tests for parse_cross_refs function."""

    def test_simple_file_ref(self):
        content = lines("""Some text with a [link](other.md) in it.""")
        refs = parse_cross_refs(content)

        assert len(refs) == 1
        ref = refs[0]
        assert ref.display_text == "link"
        assert ref.target_path == "other.md"
        assert ref.target_anchor is None
        assert ref.line == 1

    def test_file_with_anchor(self):
        content = lines("""See [Section One](docs/guide.md#section-one) for details.""")
        refs = parse_cross_refs(content)

        assert len(refs) == 1
        ref = refs[0]
        assert ref.display_text == "Section One"
        assert ref.target_path == "docs/guide.md"
        assert ref.target_anchor == "section-one"

    def test_multiple_refs_same_line(self):
        content = lines("""See [A](a.md) and [B](b.md#anchor) for info.""")
        refs = parse_cross_refs(content)

        assert len(refs) == 2
        assert refs[0].target_path == "a.md"
        assert refs[1].target_path == "b.md"
        assert refs[1].target_anchor == "anchor"

    def test_multiple_refs_different_lines(self):
        content = lines("""First [link](first.md).

Second [link](second.md#section).""")
        refs = parse_cross_refs(content)

        assert len(refs) == 2
        assert refs[0].line == 1
        assert refs[1].line == 3

    def test_relative_paths(self):
        content = lines("""
[Parent](../parent.md)
[Sibling](./sibling.md)
[Nested](sub/nested.md)
""")
        refs = parse_cross_refs(content)

        assert len(refs) == 3
        assert refs[0].target_path == "../parent.md"
        assert refs[1].target_path == "./sibling.md"
        assert refs[2].target_path == "sub/nested.md"

    def test_ignores_non_md_links(self):
        content = lines("""
[Website](https://example.com)
[Image](image.png)
[PDF](doc.pdf)
[Markdown](readme.md)
""")
        refs = parse_cross_refs(content)

        assert len(refs) == 1
        assert refs[0].target_path == "readme.md"

    def test_self_refs_excluded_by_default(self):
        content = lines("""See [Section](#section) below.""")
        refs = parse_cross_refs(content)

        assert len(refs) == 0

    def test_self_refs_included_when_requested(self):
        content = lines("""See [Section](#section) below.""")
        refs = parse_cross_refs(content, include_self_refs=True)

        assert len(refs) == 1
        assert refs[0].target_path == ""
        assert refs[0].target_anchor == "section"

    def test_column_positions(self):
        content = lines("""Some [link](file.md) here.""")
        refs = parse_cross_refs(content)

        ref = refs[0]
        assert ref.col_start == 5
        assert ref.col_end == 20  # After ")"

    def test_empty_content(self):
        refs = parse_cross_refs([])
        assert refs == []

    def test_no_refs(self):
        content = lines("""Just plain text with no links.""")
        refs = parse_cross_refs(content)
        assert refs == []

    def test_toc_entry_not_parsed_as_xref(self):
        content = lines("""1. [Section](#section) _(Lines 10-20)_""")
        refs = parse_cross_refs(content)
        # This is a self-ref, excluded by default
        assert len(refs) == 0

    def test_complex_display_text(self):
        content = lines("""See [Code & Examples (v2)](guide.md#code-examples).""")
        refs = parse_cross_refs(content)

        assert len(refs) == 1
        assert refs[0].display_text == "Code & Examples (v2)"

    def test_full_link_property(self):
        content = lines("""[Title](file.md#anchor)""")
        refs = parse_cross_refs(content)

        assert refs[0].full_link == "[Title](file.md#anchor)"

    def test_full_link_without_anchor(self):
        content = lines("""[Title](file.md)""")
        refs = parse_cross_refs(content)

        assert refs[0].full_link == "[Title](file.md)"


class TestResolveTargetPath:
    """Tests for resolve_target_path function."""

    def test_simple_relative(self, tmp_path):
        source = tmp_path / "docs" / "source.md"
        source.parent.mkdir(parents=True)
        source.touch()

        result = resolve_target_path(source, "target.md")
        expected = (tmp_path / "docs" / "target.md").resolve()
        assert result == expected

    def test_parent_directory(self, tmp_path):
        source = tmp_path / "docs" / "sub" / "source.md"
        source.parent.mkdir(parents=True)
        source.touch()

        result = resolve_target_path(source, "../target.md")
        expected = (tmp_path / "docs" / "target.md").resolve()
        assert result == expected

    def test_nested_path(self, tmp_path):
        source = tmp_path / "source.md"
        source.touch()

        result = resolve_target_path(source, "docs/guide.md")
        expected = (tmp_path / "docs" / "guide.md").resolve()
        assert result == expected

    def test_self_reference(self, tmp_path):
        source = tmp_path / "source.md"
        source.touch()

        result = resolve_target_path(source, "")
        assert result == source.resolve()


class TestGetUniqueTargetPaths:
    """Tests for get_unique_target_paths function."""

    def test_deduplicates_paths(self, tmp_path):
        source = tmp_path / "source.md"
        source.touch()

        content = lines("""
[First](target.md#section-1)
[Second](target.md#section-2)
[Third](other.md)
""")
        refs = parse_cross_refs(content)
        targets = get_unique_target_paths(source, refs)

        # Should have 2 unique paths, not 3
        assert len(targets) == 2

    def test_excludes_self_refs(self, tmp_path):
        source = tmp_path / "source.md"
        source.touch()

        content = lines("""[Link](other.md)""")
        refs = parse_cross_refs(content, include_self_refs=True)

        # Add a self-ref manually
        from md_structure_sync.models import CrossRef
        refs.append(CrossRef(
            line=2,
            col_start=0,
            col_end=10,
            display_text="Self",
            target_path="",
            target_anchor="self",
        ))

        targets = get_unique_target_paths(source, refs)

        # Self-ref should be excluded
        assert len(targets) == 1
