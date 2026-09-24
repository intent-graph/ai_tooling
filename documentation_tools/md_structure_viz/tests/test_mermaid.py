"""Tests for Mermaid diagram generation."""

import pytest
from pathlib import Path

from md_structure_viz.doc_tree import build_doc_tree
from md_structure_viz.mermaid import (
    generate_tree_graph,
    generate_simple_flowchart,
    generate_stats,
    sanitize_id,
    escape_label,
)


@pytest.fixture
def sample_docs_dir():
    """Get path to sample documentation directory."""
    return Path(__file__).parent / "fixtures" / "sample_docs"


@pytest.fixture
def doc_tree(sample_docs_dir):
    """Build documentation tree from sample docs."""
    return build_doc_tree(sample_docs_dir)


class TestSanitizeId:
    """Tests for ID sanitization."""

    def test_sanitize_path_separators(self):
        """Should replace path separators with underscores."""
        path = Path("api/endpoints.md")
        root = Path(".")
        result = sanitize_id(path, root)

        assert "/" not in result
        assert "_" in result

    def test_sanitize_dots(self):
        """Should handle dots in filenames."""
        path = Path("api/endpoints.md")
        root = Path(".")
        result = sanitize_id(path, root)

        assert "." not in result


class TestEscapeLabel:
    """Tests for label escaping."""

    def test_escape_quotes(self):
        """Should replace quotes with single quotes."""
        label = 'Test "quoted" text'
        result = escape_label(label)

        assert '"' not in result
        assert "'" in result

    def test_escape_angle_brackets(self):
        """Should replace angle brackets."""
        label = "Test <angle> brackets"
        result = escape_label(label)

        assert "<" not in result
        assert ">" not in result


class TestGenerateTreeGraph:
    """Tests for tree graph generation."""

    def test_generate_creates_valid_mermaid(self, doc_tree):
        """Should generate valid Mermaid syntax."""
        result = generate_tree_graph(doc_tree)

        assert "graph TB" in result
        assert "classDef" in result
        assert "class" in result

    def test_generate_includes_folders(self, doc_tree):
        """Should create nodes for folders."""
        result = generate_tree_graph(doc_tree)

        # Should mention folder structure
        assert "/" in result  # Folder references

    def test_generate_includes_files(self, doc_tree):
        """Should create nodes for files."""
        result = generate_tree_graph(doc_tree)

        # Should include files from fixture
        assert "sections" in result

    def test_generate_includes_cross_refs(self, doc_tree):
        """Should show cross-references as dotted lines."""
        result = generate_tree_graph(doc_tree)

        # Dotted lines indicate cross-refs
        assert "-.->" in result or "refs" in result

    def test_generate_applies_styling(self, doc_tree):
        """Should apply Mermaid styling classes."""
        result = generate_tree_graph(doc_tree)

        assert "classDef folder" in result
        assert "classDef file" in result

    def test_generate_returns_string(self, doc_tree):
        """Should return a string."""
        result = generate_tree_graph(doc_tree)

        assert isinstance(result, str)
        assert len(result) > 0


class TestGenerateSimpleFlowchart:
    """Tests for simple flowchart generation."""

    def test_generate_creates_valid_mermaid(self, doc_tree):
        """Should generate valid Mermaid syntax."""
        result = generate_simple_flowchart(doc_tree)

        assert "graph TD" in result or "graph LR" in result

    def test_generate_shows_only_refs(self, doc_tree):
        """Should only show cross-references, not folder hierarchy."""
        result = generate_simple_flowchart(doc_tree)

        # Should have file connections
        assert "-->" in result

    def test_generate_returns_string(self, doc_tree):
        """Should return a string."""
        result = generate_simple_flowchart(doc_tree)

        assert isinstance(result, str)
        assert len(result) > 0


class TestGenerateStats:
    """Tests for statistics generation."""

    def test_generate_includes_file_count(self, doc_tree):
        """Should include total file count."""
        result = generate_stats(doc_tree)

        assert "Total files:" in result
        assert "7" in result  # 7 files in fixture

    def test_generate_includes_section_count(self, doc_tree):
        """Should include total section count."""
        result = generate_stats(doc_tree)

        assert "Total sections:" in result

    def test_generate_includes_ref_count(self, doc_tree):
        """Should include total cross-reference count."""
        result = generate_stats(doc_tree)

        assert "Total cross-references:" in result

    def test_generate_includes_average_sections(self, doc_tree):
        """Should calculate average sections per file."""
        result = generate_stats(doc_tree)

        assert "Average sections per file:" in result

    def test_generate_returns_string(self, doc_tree):
        """Should return a string."""
        result = generate_stats(doc_tree)

        assert isinstance(result, str)
        assert len(result) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
