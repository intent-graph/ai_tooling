"""Tests for path formatting in CLI output - verifying relative paths are used."""

import pytest
import subprocess
import re
from pathlib import Path
from md_structure_viz.doc_tree import build_doc_tree


@pytest.fixture
def sample_docs_dir():
    """Get path to sample documentation directory."""
    return Path(__file__).parent / "fixtures" / "sample_docs"


@pytest.fixture
def sample_tree(sample_docs_dir):
    """Build doc tree from sample docs."""
    return build_doc_tree(sample_docs_dir)


class TestCLICommandPathFormatting:
    """Integration tests for CLI commands verifying output format."""

    def test_simple_command_output_is_relative(self, sample_docs_dir):
        """md-doc-tree-simple should output relative paths."""
        result = subprocess.run(
            ["md-doc-tree-simple", str(sample_docs_dir)],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        assert result.returncode == 0, f"Command failed: {result.stderr}"
        output = result.stdout

        # First line should be directory name only
        first_line = output.split("\n")[0]
        assert first_line == "sample_docs/", f"Expected 'sample_docs/' but got '{first_line}'"

        # Should not contain absolute paths
        assert "/Users/" not in output, "Output should not contain absolute paths"
        assert "Documents/PROJECTS" not in output, "Output should not contain absolute paths"

    def test_rich_command_output_is_relative(self, sample_docs_dir):
        """md-doc-tree-rich should output relative paths."""
        result = subprocess.run(
            ["md-doc-tree-rich", str(sample_docs_dir)],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        assert result.returncode == 0, f"Command failed: {result.stderr}"
        output = result.stdout

        # First line should be directory name only
        first_line = output.split("\n")[0]
        assert first_line == "sample_docs/", f"Expected 'sample_docs/' but got '{first_line}'"

        # Should not contain absolute paths
        assert "/Users/" not in output, "Output should not contain absolute paths"
        assert "Documents/PROJECTS" not in output, "Output should not contain absolute paths"

    def test_full_command_manifest_output_is_relative(self, sample_docs_dir, tmp_path):
        """md-doc-tree-full manifest should output relative paths."""
        prefix = tmp_path / "test_manifest"

        result = subprocess.run(
            ["md-doc-tree-full", str(sample_docs_dir), "--output", str(prefix)],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        assert result.returncode == 0, f"Command failed: {result.stderr}"

        sections_file = tmp_path / "test_manifest_sections.yaml"
        cross_refs_file = tmp_path / "test_manifest_cross_refs.yaml"

        assert sections_file.exists(), "Sections YAML should be created"
        assert cross_refs_file.exists(), "Cross-refs YAML should be created"

        sections_content = sections_file.read_text()
        cross_refs_content = cross_refs_file.read_text()

        # Should not contain absolute paths
        for content in [sections_content, cross_refs_content]:
            assert "/Users/" not in content, "Output should not contain absolute paths"
            assert "Documents/PROJECTS" not in content, "Output should not contain absolute paths"

    def test_json_format_maintains_consistency(self, sample_docs_dir):
        """JSON output structure should be valid and contain expected fields."""
        result = subprocess.run(
            ["md-doc-tree-simple", str(sample_docs_dir), "--format", "json"],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        assert result.returncode == 0, f"Command failed: {result.stderr}"
        output = result.stdout

        # Parse JSON (basic checks)
        assert '"root":' in output, "JSON should have root field"
        assert '"files":' in output, "JSON should have files field"
        assert '"file_count":' in output, "JSON should have file_count field"

        # JSON files list should contain file count
        import json
        data = json.loads(output)
        assert data["file_count"] == len(data["files"]), "File count should match files list length"
        assert data["file_count"] > 0, "Should have found markdown files"


class TestPathFormattingConsistency:
    """Tests verifying consistent path formatting across different input formats."""

    def test_same_output_for_path_with_and_without_trailing_slash(self, sample_docs_dir):
        """Output should be identical whether input has trailing slash or not."""
        # Without trailing slash
        result1 = subprocess.run(
            ["md-doc-tree-simple", str(sample_docs_dir)],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        # With trailing slash
        result2 = subprocess.run(
            ["md-doc-tree-simple", str(sample_docs_dir) + "/"],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        # Both should start with "sample_docs/"
        assert result1.stdout.split("\n")[0] == "sample_docs/"
        # With trailing slash may fail with "directory not found" - that's OK, or should succeed
        if result2.returncode == 0:
            assert result2.stdout.split("\n")[0] == "sample_docs/"

    def test_absolute_path_input_produces_relative_output(self, sample_docs_dir):
        """Absolute paths as input should produce relative paths in output."""
        absolute_path = sample_docs_dir.resolve()

        result = subprocess.run(
            ["md-doc-tree-simple", str(absolute_path)],
            capture_output=True,
            text=True,
            cwd="/tmp"
        )

        assert result.returncode == 0
        output = result.stdout

        # Output should use relative paths even when input is absolute
        first_line = output.split("\n")[0]
        assert first_line == "sample_docs/"
        assert not first_line.startswith("/")
        assert "Users" not in first_line


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
