"""Tests for cross-reference validation."""

import pytest
from pathlib import Path
import tempfile

from md_structure_sync.models import Config, TocSyncState
from md_structure_sync.xref_validate import (
    get_file_anchors,
    validate_ref,
    validate_cross_refs,
    validate_directory_cross_refs,
)
from md_structure_sync.cross_refs import parse_cross_refs


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


def create_file(path: Path, content: str) -> None:
    """Create a file with given content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


class TestGetFileAnchors:
    """Tests for get_file_anchors function."""

    def test_simple_headers(self, temp_dir):
        file_path = temp_dir / "test.md"
        create_file(file_path, """# Title

## Section One

Content.

## Section Two

More content.
""")
        anchors = get_file_anchors(file_path, Config())

        assert "section-one" in anchors
        assert "section-two" in anchors

    def test_duplicate_headers(self, temp_dir):
        file_path = temp_dir / "test.md"
        create_file(file_path, """## Section

First.

## Section

Second.

## Section

Third.
""")
        anchors = get_file_anchors(file_path, Config())

        assert "section" in anchors
        assert "section-1" in anchors
        assert "section-2" in anchors

    def test_nonexistent_file(self, temp_dir):
        file_path = temp_dir / "nonexistent.md"
        anchors = get_file_anchors(file_path, Config())
        assert anchors == []

    def test_empty_file(self, temp_dir):
        file_path = temp_dir / "empty.md"
        create_file(file_path, "")
        anchors = get_file_anchors(file_path, Config())
        assert anchors == []


class TestValidateRef:
    """Tests for validate_ref function."""

    def test_valid_file_only(self, temp_dir):
        source = temp_dir / "source.md"
        target = temp_dir / "target.md"
        create_file(source, "")
        create_file(target, "## Section\n\nContent.\n")

        from md_structure_sync.models import CrossRef
        ref = CrossRef(
            line=1, col_start=0, col_end=20,
            display_text="Target",
            target_path="target.md",
            target_anchor=None,
        )

        result = validate_ref(ref, source, {}, Config())
        assert result.status == "valid"

    def test_missing_file(self, temp_dir):
        source = temp_dir / "source.md"
        create_file(source, "")

        from md_structure_sync.models import CrossRef
        ref = CrossRef(
            line=1, col_start=0, col_end=20,
            display_text="Missing",
            target_path="missing.md",
            target_anchor=None,
        )

        result = validate_ref(ref, source, {}, Config())
        assert result.status == "file_missing"

    def test_valid_anchor(self, temp_dir):
        source = temp_dir / "source.md"
        target = temp_dir / "target.md"
        create_file(source, "")
        create_file(target, "## Section One\n\nContent.\n")

        from md_structure_sync.models import CrossRef
        ref = CrossRef(
            line=1, col_start=0, col_end=30,
            display_text="Section One",
            target_path="target.md",
            target_anchor="section-one",
        )

        result = validate_ref(ref, source, {}, Config())
        assert result.status == "valid"

    def test_missing_anchor(self, temp_dir):
        source = temp_dir / "source.md"
        target = temp_dir / "target.md"
        create_file(source, "")
        create_file(target, "## Section One\n\nContent.\n")

        from md_structure_sync.models import CrossRef
        ref = CrossRef(
            line=1, col_start=0, col_end=30,
            display_text="Wrong Section",
            target_path="target.md",
            target_anchor="wrong-section",
        )

        result = validate_ref(ref, source, {}, Config())
        assert result.status == "anchor_missing"

    def test_fuzzy_anchor_match(self, temp_dir):
        source = temp_dir / "source.md"
        target = temp_dir / "target.md"
        create_file(source, "")
        create_file(target, "## Section One\n\nContent.\n")

        from md_structure_sync.models import CrossRef
        ref = CrossRef(
            line=1, col_start=0, col_end=30,
            display_text="Section One",
            target_path="target.md",
            target_anchor="secton-one",  # Typo
        )

        result = validate_ref(ref, source, {}, Config(), auto_fix_fuzzy=True)
        assert result.status == "anchor_fuzzy"
        assert result.suggested_anchor == "section-one"
        assert result.similarity_score is not None
        assert result.similarity_score >= 0.8


class TestValidateCrossRefs:
    """Tests for validate_cross_refs function."""

    def test_all_valid(self, temp_dir):
        source = temp_dir / "source.md"
        target = temp_dir / "target.md"

        create_file(target, """## Section One

Content.

## Section Two

More content.
""")
        create_file(source, """# Source

See [Section One](target.md#section-one).

Also [Section Two](target.md#section-two).
""")

        result = validate_cross_refs(source, dry_run=True)

        assert result.refs_found == 2
        assert result.refs_valid == 2
        assert result.refs_invalid == 0
        assert result.error is None

    def test_missing_file_remove_mode(self, temp_dir):
        source = temp_dir / "source.md"
        create_file(source, """# Source

See [Missing](missing.md) for details.
""")

        result = validate_cross_refs(source, mode="remove", dry_run=True)

        assert result.refs_found == 1
        assert result.refs_invalid == 1
        assert result.changed is True

    def test_missing_file_warn_mode(self, temp_dir):
        source = temp_dir / "source.md"
        create_file(source, """# Source

See [Missing](missing.md) for details.
""")

        result = validate_cross_refs(source, mode="warn", dry_run=True)

        assert result.refs_found == 1
        assert result.refs_invalid == 1
        assert result.changed is True

    def test_fuzzy_auto_fix(self, temp_dir):
        source = temp_dir / "source.md"
        target = temp_dir / "target.md"

        create_file(target, "## Section One\n\nContent.\n")
        create_file(source, """See [Section](target.md#secton-one).""")  # Typo

        result = validate_cross_refs(source, auto_fix_fuzzy=True, dry_run=True)

        assert result.refs_found == 1
        assert result.refs_fixed == 1
        assert result.changed is True

    def test_remove_actually_removes(self, temp_dir):
        source = temp_dir / "source.md"
        create_file(source, """See [Missing](missing.md) for details.""")

        result = validate_cross_refs(source, mode="remove", dry_run=False)

        assert result.changed is True
        content = source.read_text()
        assert "[Missing]" not in content

    def test_warn_adds_comment(self, temp_dir):
        source = temp_dir / "source.md"
        create_file(source, """See [Missing](missing.md) for details.""")

        result = validate_cross_refs(source, mode="warn", dry_run=False)

        assert result.changed is True
        content = source.read_text()
        assert "<!-- INVALID:" in content
        assert "file" in content and "not found" in content

    def test_dry_run_no_changes(self, temp_dir):
        source = temp_dir / "source.md"
        # Use a pre-synced file to avoid toc_sync changes
        create_file(source, """## Table of Contents

1. [Section](#section) _(Lines 8-9)_

---

## Section
<!-- Lines 8-9 -->

See [Missing](missing.md) for details.
""")
        original = source.read_text()

        result = validate_cross_refs(source, mode="remove", dry_run=True)

        assert result.changed is True
        # File should be unchanged in dry run (only xref changes, not toc_sync)
        assert source.read_text() == original

    def test_nonexistent_source(self, temp_dir):
        source = temp_dir / "nonexistent.md"
        result = validate_cross_refs(source)

        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_self_reference_validation(self, temp_dir):
        source = temp_dir / "source.md"
        # Pre-synced file to avoid TOC entries being counted
        create_file(source, """## Table of Contents

1. [Existing Section](#existing-section) _(Lines 8-10)_

---

## Existing Section
<!-- Lines 8-10 -->

Content.

See [Existing](#existing-section) and [Missing](#missing-section).
""")

        result = validate_cross_refs(source, dry_run=True)

        # Self-refs: TOC entry (valid) + 2 in content (1 valid, 1 invalid)
        # TOC entry is also a self-ref, so we count 3 total
        assert result.refs_found == 3
        assert result.refs_valid == 2  # TOC entry + Existing
        assert result.refs_invalid == 1  # Missing


class TestValidateDirectoryCrossRefs:
    """Tests for validate_directory_cross_refs function."""

    def test_multiple_files(self, temp_dir):
        create_file(temp_dir / "a.md", """# A

See [B](b.md#section).
""")
        create_file(temp_dir / "b.md", """# B

## Section

Content.

See [A](a.md).
""")

        results = validate_directory_cross_refs(temp_dir, dry_run=True)

        assert len(results) == 2
        # File refs should be valid since files exist
        # After toc_sync, there will be TOC entries as self-refs too
        total_invalid = sum(r.refs_invalid for r in results)
        assert total_invalid == 0  # No invalid refs

    def test_recursive(self, temp_dir):
        create_file(temp_dir / "root.md", """See [Nested](sub/nested.md).""")
        create_file(temp_dir / "sub" / "nested.md", """## Section\n\nContent.""")

        results = validate_directory_cross_refs(temp_dir, recursive=True, dry_run=True)

        assert len(results) == 2

    def test_pattern_filter(self, temp_dir):
        create_file(temp_dir / "doc.md", """Content.""")
        create_file(temp_dir / "readme.markdown", """Content.""")

        results = validate_directory_cross_refs(
            temp_dir, pattern="*.markdown", dry_run=True
        )

        assert len(results) == 1

    def test_empty_directory(self, temp_dir):
        results = validate_directory_cross_refs(temp_dir)
        assert len(results) == 0


class TestTocSyncState:
    """Tests for TocSyncState tracking."""

    def test_mark_and_check(self, temp_dir):
        state = TocSyncState()
        file_path = temp_dir / "test.md"

        assert not state.is_toc_synced(file_path)

        state.mark_toc_synced(file_path)
        assert state.is_toc_synced(file_path)

    def test_normalized_paths(self, temp_dir):
        state = TocSyncState()
        file_path = temp_dir / "sub" / ".." / "test.md"
        normalized = temp_dir / "test.md"

        state.mark_toc_synced(file_path)

        # Should match even with different path representation
        assert state.is_toc_synced(normalized)

    def test_dirty_tracking(self, temp_dir):
        state = TocSyncState()
        file_path = temp_dir / "test.md"

        state.mark_dirty(file_path)
        assert file_path.resolve() in state.dirty

        state.clear_dirty(file_path)
        assert file_path.resolve() not in state.dirty

    def test_shared_state_prevents_resync(self, temp_dir):
        """Test that shared state prevents redundant syncs."""
        target = temp_dir / "target.md"
        source1 = temp_dir / "source1.md"
        source2 = temp_dir / "source2.md"

        create_file(target, "## Section\n\nContent.\n")
        create_file(source1, "[Link](target.md#section)")
        create_file(source2, "[Link](target.md#section)")

        state = TocSyncState()

        # First validation syncs target
        validate_cross_refs(source1, sync_state=state, dry_run=True)
        assert state.is_toc_synced(target)

        # Second validation should reuse sync state
        # (we can't easily verify no re-sync, but we verify state is shared)
        validate_cross_refs(source2, sync_state=state, dry_run=True)
        assert state.is_toc_synced(target)


class TestEdgeCases:
    """Edge case tests for xref validation."""

    def test_multiple_refs_same_line(self, temp_dir):
        target = temp_dir / "target.md"
        source = temp_dir / "source.md"

        create_file(target, "## A\n\nContent.\n\n## B\n\nMore.")
        create_file(source, "See [A](target.md#a) and [C](target.md#c).")

        result = validate_cross_refs(source, mode="remove", dry_run=True)

        assert result.refs_found == 2
        assert result.refs_valid == 1  # #a exists
        assert result.refs_invalid == 1  # #c missing

    def test_special_chars_in_path(self, temp_dir):
        # Spaces in filename
        target = temp_dir / "my file.md"
        source = temp_dir / "source.md"

        create_file(target, "## Section\n\nContent.")
        create_file(source, "See [Link](my%20file.md#section).")

        # Note: URL-encoded spaces may not work directly
        # This tests the current behavior
        result = validate_cross_refs(source, dry_run=True)
        # The path "my%20file.md" won't resolve to "my file.md"
        # So this should be file_missing
        assert result.refs_invalid == 1

    def test_circular_references(self, temp_dir):
        a = temp_dir / "a.md"
        b = temp_dir / "b.md"

        create_file(a, "## Section A\n\nSee [B](b.md#section-b).")
        create_file(b, "## Section B\n\nSee [A](a.md#section-a).")

        # Should not infinite loop
        results = validate_directory_cross_refs(temp_dir, dry_run=True)

        assert len(results) == 2
        # File-to-file refs are valid; TOC self-refs are also valid
        total_invalid = sum(r.refs_invalid for r in results)
        assert total_invalid == 0

    def test_deeply_nested_paths(self, temp_dir):
        source = temp_dir / "docs" / "guide" / "source.md"
        target = temp_dir / "api" / "reference" / "target.md"

        create_file(target, "## Endpoint\n\nContent.")
        create_file(source, "See [API](../../api/reference/target.md#endpoint).")

        result = validate_cross_refs(source, dry_run=True)

        assert result.refs_valid == 1
        assert result.refs_invalid == 0
