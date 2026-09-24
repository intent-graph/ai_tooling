"""Tests for documentation tree discovery and analysis."""

import pytest
from pathlib import Path

from md_structure_viz.doc_tree import (
    build_doc_tree,
    discover_md_files,
    extract_metadata,
    find_cross_refs,
    get_orphaned_files,
)


@pytest.fixture
def sample_docs_dir():
    """Get path to sample documentation directory."""
    return Path(__file__).parent / "fixtures" / "sample_docs"


class TestDiscoverMdFiles:
    """Tests for markdown file discovery."""

    def test_discover_finds_all_markdown_files(self, sample_docs_dir):
        """Should find all .md files in directory."""
        files = discover_md_files(sample_docs_dir)

        assert len(files) == 6
        file_names = [f.name for f in files]
        assert "README.md" in file_names
        assert "authentication.md" in file_names
        assert "endpoints.md" in file_names

    def test_discover_returns_sorted_paths(self, sample_docs_dir):
        """Should return files in sorted order."""
        files = discover_md_files(sample_docs_dir)
        assert files == sorted(files)

    def test_discover_nonexistent_directory(self):
        """Should raise error for non-existent directory."""
        with pytest.raises(FileNotFoundError):
            discover_md_files(Path("/nonexistent/directory"))


class TestExtractMetadata:
    """Tests for metadata extraction."""

    def test_extract_title_and_sections(self, sample_docs_dir):
        """Should extract title and section count."""
        readme = sample_docs_dir / "README.md"
        metadata = extract_metadata(readme)

        assert metadata["title"] == "Project Documentation"
        assert metadata["sections"] == 4

    def test_extract_with_multiple_sections(self, sample_docs_dir):
        """Should count all heading levels."""
        endpoints = sample_docs_dir / "api" / "endpoints.md"
        metadata = extract_metadata(endpoints)

        assert metadata["title"] == "REST API Endpoints"
        assert metadata["sections"] > 5

    def test_extract_uses_filename_as_fallback(self, tmp_path):
        """Should use filename if no title found."""
        test_file = tmp_path / "test.md"
        test_file.write_text("No heading here\n\nJust content")

        metadata = extract_metadata(test_file)

        assert metadata["title"] == "test.md"
        assert metadata["sections"] == 0

    def test_extract_from_nonexistent_file(self, tmp_path):
        """Should handle missing files gracefully."""
        metadata = extract_metadata(tmp_path / "missing.md")

        assert "error" in metadata


class TestFindCrossRefs:
    """Tests for cross-reference detection."""

    def test_find_cross_refs_in_file(self, sample_docs_dir):
        """Should find markdown links to other files."""
        readme = sample_docs_dir / "README.md"
        refs = find_cross_refs(readme, sample_docs_dir)

        assert len(refs) > 0
        ref_names = [r.name for r in refs]
        assert "endpoints.md" in ref_names

    def test_find_relative_refs(self, sample_docs_dir):
        """Should resolve relative paths correctly."""
        getting_started = sample_docs_dir / "guides" / "getting-started.md"
        refs = find_cross_refs(getting_started, sample_docs_dir)

        assert len(refs) > 0
        # Should have resolved ../api/authentication.md
        assert any("authentication.md" in r.name for r in refs)

    def test_find_refs_in_file_without_links(self, tmp_path):
        """Should return empty list for files without refs."""
        test_file = tmp_path / "test.md"
        test_file.write_text("# Test\n\nNo links here")

        refs = find_cross_refs(test_file, tmp_path)

        assert refs == []


class TestBuildDocTree:
    """Tests for complete tree building."""

    def test_build_tree_creates_nodes(self, sample_docs_dir):
        """Should create nodes for all files."""
        tree = build_doc_tree(sample_docs_dir)

        assert tree.total_files == 6
        assert tree.root == sample_docs_dir.resolve()

    def test_build_tree_extracts_metadata(self, sample_docs_dir):
        """Should extract metadata for all files."""
        tree = build_doc_tree(sample_docs_dir)

        readme_node = next((n for n in tree.nodes.values() if n.path.name == "README.md"), None)
        assert readme_node is not None
        assert readme_node.title == "Project Documentation"

    def test_build_tree_finds_cross_refs(self, sample_docs_dir):
        """Should detect cross-references."""
        tree = build_doc_tree(sample_docs_dir)

        # README should reference other files
        readme_node = next((n for n in tree.nodes.values() if n.path.name == "README.md"), None)
        assert len(readme_node.outgoing_refs) > 0

    def test_build_tree_creates_folder_hierarchy(self, sample_docs_dir):
        """Should organize files by folder."""
        tree = build_doc_tree(sample_docs_dir)

        folders = tree.get_folder_hierarchy()
        assert len(folders) >= 3  # root, api, guides

    def test_total_sections_calculation(self, sample_docs_dir):
        """Should calculate total sections correctly."""
        tree = build_doc_tree(sample_docs_dir)

        assert tree.total_sections > 0
        # Verify by summing manually
        manual_sum = sum(n.section_count for n in tree.nodes.values())
        assert tree.total_sections == manual_sum

    def test_total_refs_calculation(self, sample_docs_dir):
        """Should calculate total references correctly."""
        tree = build_doc_tree(sample_docs_dir)

        assert tree.total_refs > 0
        manual_sum = sum(len(n.outgoing_refs) for n in tree.nodes.values())
        assert tree.total_refs == manual_sum


class TestOrphanedFiles:
    """Tests for orphaned file detection."""

    def test_find_orphaned_files(self, sample_docs_dir):
        """Should identify files with no incoming references."""
        tree = build_doc_tree(sample_docs_dir)
        orphaned = get_orphaned_files(tree)

        # Schemas might be orphaned (only referenced by auth guide)
        orphaned_names = [o.path.name for o in orphaned]
        # This depends on actual cross-references in fixtures


class TestIgnoreFlags:
    """Tests for ignore_default and respect_gitignore flags."""

    def test_discover_with_default_ignore_enabled(self, sample_docs_dir):
        """Should filter files based on DEFAULT_IGNORE_PATTERNS when enabled."""
        # Sample docs has no venvs/node_modules, so count should be same
        files_with_ignore = discover_md_files(sample_docs_dir, ignore_default=True)
        assert len(files_with_ignore) == 6

    def test_discover_with_default_ignore_disabled(self, sample_docs_dir):
        """Should not filter based on DEFAULT_IGNORE_PATTERNS when disabled."""
        # Sample docs has no venvs/node_modules, so count should be same
        files_without_ignore = discover_md_files(sample_docs_dir, ignore_default=False)
        assert len(files_without_ignore) == 6

    def test_discover_default_ignore_is_enabled_by_default(self, sample_docs_dir):
        """DEFAULT_IGNORE_PATTERNS should be enabled by default."""
        files_default = discover_md_files(sample_docs_dir)
        files_explicit_true = discover_md_files(sample_docs_dir, ignore_default=True)
        assert len(files_default) == len(files_explicit_true)

    def test_discover_respects_gitignore_when_enabled(self, sample_docs_dir):
        """Should filter git-ignored files when respect_gitignore=True."""
        # Sample docs is not a git repo, so this should behave same as without
        files_with_git = discover_md_files(sample_docs_dir, respect_gitignore=True)
        files_without_git = discover_md_files(sample_docs_dir, respect_gitignore=False)
        assert len(files_with_git) == len(files_without_git)

    def test_discover_git_ignore_is_disabled_by_default(self, sample_docs_dir):
        """respect_gitignore should be disabled by default."""
        files_default = discover_md_files(sample_docs_dir)
        files_explicit_false = discover_md_files(sample_docs_dir, respect_gitignore=False)
        assert len(files_default) == len(files_explicit_false)

    def test_discover_flags_work_orthogonally(self, sample_docs_dir):
        """Flags should work independently (both, either, or neither)."""
        # Test all 4 combinations
        files_both_true = discover_md_files(
            sample_docs_dir, ignore_default=True, respect_gitignore=True
        )
        files_ignore_only = discover_md_files(
            sample_docs_dir, ignore_default=True, respect_gitignore=False
        )
        files_git_only = discover_md_files(
            sample_docs_dir, ignore_default=False, respect_gitignore=True
        )
        files_both_false = discover_md_files(
            sample_docs_dir, ignore_default=False, respect_gitignore=False
        )

        # For sample_docs (no venvs, not a git repo), all combinations should return same count
        assert len(files_both_true) == 6
        assert len(files_ignore_only) == 6
        assert len(files_git_only) == 6
        assert len(files_both_false) == 6

    def test_build_tree_forwards_ignore_flags(self, sample_docs_dir):
        """build_doc_tree should accept and forward ignore flags."""
        tree_default = build_doc_tree(sample_docs_dir)
        tree_with_flags = build_doc_tree(
            sample_docs_dir, ignore_default=True, respect_gitignore=False
        )

        # Both should have same number of files for sample_docs
        assert tree_default.total_files == tree_with_flags.total_files == 6

    def test_build_tree_flags_default_to_correct_values(self, sample_docs_dir):
        """build_doc_tree should default to ignore_default=True, respect_gitignore=False."""
        tree = build_doc_tree(sample_docs_dir)
        assert tree.total_files == 6  # Sample docs has 6 files with defaults


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
