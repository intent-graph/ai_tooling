"""Tests for YAML manifest generation."""

import pytest
from pathlib import Path

from md_structure_viz.doc_tree import build_doc_tree, extract_metadata, _detect_toc
from md_structure_viz.manifest_generator import (
    generate_sections_yaml,
    generate_cross_refs_yaml,
    _get_adaptive_headings,
    _build_collapsed_folders,
    _yaml_escape,
    _FolderNode,
)


@pytest.fixture
def sample_docs_dir():
    """Get path to sample documentation directory."""
    return Path(__file__).parent / "fixtures" / "sample_docs"


@pytest.fixture
def sample_tree(sample_docs_dir):
    """Build doc tree from sample docs."""
    return build_doc_tree(sample_docs_dir)


# ---------------------------------------------------------------------------
# Enhanced extract_metadata tests
# ---------------------------------------------------------------------------


class TestExtractMetadataEnhanced:
    """Tests for the enhanced metadata extraction (headings, word count, etc.)."""

    def test_headings_include_line_numbers(self, sample_docs_dir):
        """Headings should include accurate line numbers."""
        readme = sample_docs_dir / "README.md"
        metadata = extract_metadata(readme)

        headings = metadata["headings"]
        assert len(headings) > 0
        assert headings[0]["line"] == 1
        assert headings[0]["level"] == 1
        assert headings[0]["text"] == "Project Documentation"

    def test_headings_capture_all_levels(self, sample_docs_dir):
        """Should capture headings from h1 through h6."""
        endpoints = sample_docs_dir / "api" / "endpoints.md"
        metadata = extract_metadata(endpoints)

        headings = metadata["headings"]
        levels = {h["level"] for h in headings}
        assert 1 in levels
        assert 2 in levels
        assert 3 in levels  # endpoints.md has ### headings

    def test_word_count_is_positive(self, sample_docs_dir):
        """Word count should be a positive integer."""
        readme = sample_docs_dir / "README.md"
        metadata = extract_metadata(readme)

        assert metadata["word_count"] > 0

    def test_line_count_matches_file(self, sample_docs_dir):
        """Line count should match actual file lines."""
        readme = sample_docs_dir / "README.md"
        metadata = extract_metadata(readme)

        actual_lines = len(readme.read_text().split("\n"))
        assert metadata["line_count"] == actual_lines

    def test_toc_range_is_none_for_files_without_toc(self, sample_docs_dir):
        """Files without a Table of Contents should have toc_range=None."""
        readme = sample_docs_dir / "README.md"
        metadata = extract_metadata(readme)

        assert metadata["toc_range"] is None

    def test_error_metadata_includes_new_fields(self, tmp_path):
        """Error metadata should include all new fields with defaults."""
        metadata = extract_metadata(tmp_path / "missing.md")

        assert metadata["headings"] == []
        assert metadata["word_count"] == 0
        assert metadata["line_count"] == 0
        assert metadata["toc_range"] is None


# ---------------------------------------------------------------------------
# TOC detection tests
# ---------------------------------------------------------------------------


class TestTocDetection:
    """Tests for TOC block detection."""

    def test_detect_toc_with_numbered_list(self):
        """Should detect TOC with numbered list items."""
        lines = [
            "# Title",
            "",
            "## Table of Contents",
            "",
            "1. [Section One](#section-one) _(Lines 10-25)_",
            "2. [Section Two](#section-two) _(Lines 26-50)_",
            "3. [Section Three](#section-three) _(Lines 51-80)_",
            "",
            "## Section One",
        ]
        result = _detect_toc(lines)
        assert result is not None
        assert result[0] == 3  # line number of ## Table of Contents
        assert result[1] == 7  # line number of last TOC item

    def test_detect_toc_with_bullet_list(self):
        """Should detect TOC with bullet list items."""
        lines = [
            "# Title",
            "## Table of Contents",
            "- [Intro](#intro)",
            "- [Details](#details)",
            "",
            "## Intro",
        ]
        result = _detect_toc(lines)
        assert result is not None
        assert result[0] == 2
        assert result[1] == 4

    def test_no_toc_detected_without_heading(self):
        """Should return None when no TOC heading present."""
        lines = [
            "# Title",
            "",
            "1. [Item](#item)",
            "2. [Item2](#item2)",
        ]
        result = _detect_toc(lines)
        assert result is None

    def test_no_toc_detected_without_list_items(self):
        """Should return None when TOC heading has no list items."""
        lines = [
            "## Table of Contents",
            "",
            "This is just regular text.",
            "No list items here.",
            "More text.",
        ]
        result = _detect_toc(lines)
        assert result is None


# ---------------------------------------------------------------------------
# Adaptive heading tests
# ---------------------------------------------------------------------------


class TestAdaptiveHeadings:
    """Tests for adaptive heading depth logic."""

    def test_no_collapse_under_threshold(self, sample_tree):
        """Files under max_sections should show all headings at requested depth."""
        readme_node = next(
            n for n in sample_tree.nodes.values() if n.path.name == "README.md"
        )
        headings, note = _get_adaptive_headings(readme_node, heading_depth=2, max_sections=20)

        # README has 4 headings at h1+h2 — well under 20
        assert len(headings) == 4
        assert note is None

    def test_collapse_when_exceeding_threshold(self, sample_tree):
        """Files over max_sections should collapse to shallower depth."""
        schemas_node = next(
            n for n in sample_tree.nodes.values() if n.path.name == "schemas.md"
        )
        # schemas.md has 9 h1+h2 headings; set threshold to 5
        headings, note = _get_adaptive_headings(schemas_node, heading_depth=2, max_sections=5)

        # Should collapse to h1 only (1 heading)
        assert len(headings) == 1
        assert headings[0]["level"] == 1
        assert note is not None
        assert "showing h1 only" in note
        assert "exceeded 5" in note

    def test_empty_headings(self, sample_tree):
        """Nodes with no headings should return empty list."""
        # Create a fake node with no headings
        from md_structure_viz.doc_tree import DocNode
        empty_node = DocNode(path=Path("/fake.md"), title="Fake", section_count=0)
        headings, note = _get_adaptive_headings(empty_node, heading_depth=2, max_sections=20)

        assert headings == []
        assert note is None


# ---------------------------------------------------------------------------
# Folder collapsing tests
# ---------------------------------------------------------------------------


class TestFolderCollapsing:
    """Tests for folder path collapsing in manifest output."""

    def test_root_files_under_dot_slash(self, sample_tree):
        """Root-level files should appear under './' node."""
        root_node = _build_collapsed_folders(sample_tree)

        assert root_node.display_name == "./"
        root_names = [n.path.name for n in root_node.files]
        assert "README.md" in root_names

    def test_subfolder_names_end_with_slash(self, sample_tree):
        """Subfolder display names should end with '/'."""
        root_node = _build_collapsed_folders(sample_tree)

        def check_names(node: _FolderNode):
            assert node.display_name.endswith("/"), (
                f"Folder '{node.display_name}' should end with /"
            )
            for child in node.children.values():
                check_names(child)

        check_names(root_node)

    def test_files_sorted_within_folders(self, sample_tree):
        """Files within each folder should be sorted by name."""
        root_node = _build_collapsed_folders(sample_tree)

        def check_sorted(node: _FolderNode):
            names = [n.path.name for n in node.files]
            assert names == sorted(names), f"Files not sorted: {names}"
            for child in node.children.values():
                check_sorted(child)

        check_sorted(root_node)

    def test_children_are_nested(self, sample_tree):
        """Subfolders should be nested as children, not at root level."""
        root_node = _build_collapsed_folders(sample_tree)

        # api/ and guides/ should be children of root, not siblings
        child_names = set(root_node.children.keys())
        assert "api/" in child_names
        assert "guides/" in child_names


# ---------------------------------------------------------------------------
# Sections YAML tests
# ---------------------------------------------------------------------------


class TestGenerateSectionsYaml:
    """Tests for sections YAML output."""

    def test_header_comment(self, sample_tree):
        """Output should start with header comment containing stats."""
        yaml = generate_sections_yaml(sample_tree)
        first_line = yaml.split("\n")[0]

        assert first_line.startswith("# doc_sections")
        assert "6 files" in first_line
        assert "sections" in first_line

    def test_contains_all_files(self, sample_tree):
        """Output should contain all 6 markdown files."""
        yaml = generate_sections_yaml(sample_tree)

        assert "README.md:" in yaml
        assert "authentication.md:" in yaml
        assert "endpoints.md:" in yaml
        assert "schemas.md:" in yaml
        assert "deployment.md:" in yaml
        assert "getting-started.md:" in yaml

    def test_heading_entries_format(self, sample_tree):
        """Heading entries should be quoted strings with line number and # markers."""
        yaml = generate_sections_yaml(sample_tree)

        # Check format: "LINE: # Heading Text"
        assert '"1: # Project Documentation"' in yaml
        assert '"5: ## Overview"' in yaml

    def test_metadata_includes_lines_and_words(self, sample_tree):
        """File metadata comments should include line and word counts."""
        yaml = generate_sections_yaml(sample_tree)

        # Should contain "N lines, M words" pattern
        import re
        assert re.search(r"\d+ lines, \d+ words", yaml), "Missing lines/words metadata"

    def test_folder_grouping(self, sample_tree):
        """Files should be grouped under nested folder keys."""
        yaml = generate_sections_yaml(sample_tree)

        assert "./:\n" in yaml
        # api/ and guides/ should be indented (nested under root)
        assert "  api/:" in yaml
        assert "  guides/:" in yaml

    def test_subfolders_are_indented(self, sample_tree):
        """Subfolder files should be more deeply indented than root files."""
        yaml = generate_sections_yaml(sample_tree)
        lines = yaml.split("\n")

        # Root files at indent 2 (under "./:")
        root_file_lines = [l for l in lines if "README.md:" in l and "api/" not in l]
        assert any(l.startswith("  README.md:") for l in root_file_lines)

        # api/ files at indent 4 (under "  api/:")
        api_file_lines = [l for l in lines if "endpoints.md:" in l]
        assert any(l.startswith("    endpoints.md:") for l in api_file_lines)

    def test_no_absolute_paths(self, sample_tree):
        """Output should not contain absolute paths."""
        yaml = generate_sections_yaml(sample_tree)

        assert "/Users/" not in yaml
        assert "/home/" not in yaml

    def test_adaptive_depth_with_low_threshold(self, sample_tree):
        """Files exceeding threshold should show collapse annotation."""
        yaml = generate_sections_yaml(sample_tree, heading_depth=2, max_sections=5)

        # schemas.md has 9 h1+h2 headings — should be collapsed
        assert "showing h1 only" in yaml
        assert "exceeded 5" in yaml


# ---------------------------------------------------------------------------
# Cross-refs YAML tests
# ---------------------------------------------------------------------------


class TestGenerateCrossRefsYaml:
    """Tests for cross-references YAML output."""

    def test_header_comment(self, sample_tree):
        """Output should start with header comment containing stats."""
        yaml = generate_cross_refs_yaml(sample_tree)
        first_line = yaml.split("\n")[0]

        assert first_line.startswith("# doc_cross_refs")
        assert "6 files" in first_line
        assert "references" in first_line

    def test_outgoing_refs_listed(self, sample_tree):
        """Files with outgoing refs should list their targets."""
        yaml = generate_cross_refs_yaml(sample_tree)

        # README links to endpoints and getting-started
        assert "api/endpoints.md" in yaml
        assert "guides/getting-started.md" in yaml

    def test_leaf_files_show_empty_list(self, sample_tree):
        """Files with no outgoing refs should show [] with metadata."""
        yaml = generate_cross_refs_yaml(sample_tree)

        # schemas.md has no outgoing refs
        assert "schemas.md: []" in yaml

    def test_targets_are_relative_paths(self, sample_tree):
        """Cross-reference targets should be relative paths from root."""
        yaml = generate_cross_refs_yaml(sample_tree)

        # Targets should be like "api/authentication.md", not absolute
        assert "/Users/" not in yaml
        lines = yaml.split("\n")
        ref_lines = [l for l in lines if l.strip().startswith("- ")]
        for line in ref_lines:
            target = line.strip().lstrip("- ").strip()
            assert not target.startswith("/"), f"Target '{target}' should be relative"

    def test_folder_grouping(self, sample_tree):
        """Files should be grouped under nested folder keys."""
        yaml = generate_cross_refs_yaml(sample_tree)

        assert "./:\n" in yaml
        assert "  api/:" in yaml
        assert "  guides/:" in yaml


# ---------------------------------------------------------------------------
# YAML escaping tests
# ---------------------------------------------------------------------------


class TestYamlEscaping:
    """Tests for YAML string escaping."""

    def test_escape_double_quotes(self):
        """Double quotes in text should be escaped."""
        assert _yaml_escape('The "Best" Practice') == 'The \\"Best\\" Practice'

    def test_escape_backslashes(self):
        """Backslashes should be escaped."""
        assert _yaml_escape("path\\to\\file") == "path\\\\to\\\\file"

    def test_no_change_for_simple_text(self):
        """Simple text without special chars should pass through unchanged."""
        assert _yaml_escape("Simple heading") == "Simple heading"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
