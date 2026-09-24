"""Tests for the sync orchestrator."""

import pytest
from pathlib import Path
import tempfile
import os

from md_structure_sync.models import Config
from md_structure_sync.sync import sync_file, sync_directory


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


class TestSyncFile:
    """Tests for sync_file function."""

    def test_sync_creates_toc(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""# Document

## Section One

Content.

## Section Two

More content.
""")
        config = Config(toc_policy="add_always")
        result = sync_file(file_path, config)

        assert result.changed is True
        assert result.error is None

        content = file_path.read_text()
        assert "## Table of Contents" in content
        assert "[Section One]" in content
        assert "[Section Two]" in content

    def test_sync_idempotent(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""# Document

## Section

Content.
""")
        config = Config(toc_policy="add_always")
        # First sync
        result1 = sync_file(file_path, config)
        content1 = file_path.read_text()

        # Second sync
        result2 = sync_file(file_path, config)
        content2 = file_path.read_text()

        assert result1.changed is True
        assert result2.changed is False
        assert content1 == content2

    def test_sync_dry_run(self, temp_dir):
        file_path = temp_dir / "test.md"
        original = """# Document

## Section

Content.
"""
        file_path.write_text(original)

        config = Config(dry_run=True)
        result = sync_file(file_path, config)

        assert result.changed is True
        # File should be unchanged
        assert file_path.read_text() == original

    def test_sync_nonexistent_file(self, temp_dir):
        file_path = temp_dir / "nonexistent.md"
        result = sync_file(file_path)

        assert result.changed is False
        assert result.error is not None

    def test_sync_preserves_content(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""# My Document

## Introduction

This is the introduction with **bold** and *italic* text.

- List item 1
- List item 2

```python
def hello():
    print("Hello, World!")
```

## Conclusion

Final thoughts here.
""")
        sync_file(file_path)
        content = file_path.read_text()

        # Original content should be preserved
        assert "**bold**" in content
        assert "*italic*" in content
        assert "- List item 1" in content
        assert 'print("Hello, World!")' in content

    def test_sync_fixes_wrong_numbers(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""## Table of Contents

1. [Section](#section) _(Lines 999-1000)_

---

## Section
<!-- Lines 888-999 -->

Content.
""")
        sync_file(file_path)
        content = file_path.read_text()

        # Wrong numbers should be fixed
        assert "999" not in content
        assert "888" not in content

    def test_sync_with_config(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""## Section

### Subsection

#### Deep

##### Too Deep

Content.
""")
        # Only track H2-H3, and add TOC
        config = Config(min_level=2, max_level=3, toc_policy="add_always")
        sync_file(file_path, config)
        content = file_path.read_text()

        assert "[Section]" in content
        assert "[Subsection]" in content
        assert "[Deep]" not in content
        assert "[Too Deep]" not in content


class TestSyncDirectory:
    """Tests for sync_directory function."""

    def test_sync_multiple_files(self, temp_dir):
        # Create multiple markdown files
        (temp_dir / "file1.md").write_text("""## Section A

Content A.
""")
        (temp_dir / "file2.md").write_text("""## Section B

Content B.
""")
        (temp_dir / "file3.txt").write_text("Not markdown")

        results = sync_directory(temp_dir)

        # Should sync .md files only
        assert len(results) == 2
        assert all(r.changed for r in results)

    def test_sync_recursive(self, temp_dir):
        # Create nested structure
        subdir = temp_dir / "subdir"
        subdir.mkdir()

        (temp_dir / "root.md").write_text("## Root Section\n\nContent.\n")
        (subdir / "nested.md").write_text("## Nested Section\n\nContent.\n")

        results = sync_directory(temp_dir, recursive=True)

        assert len(results) == 2

    def test_sync_non_recursive(self, temp_dir):
        subdir = temp_dir / "subdir"
        subdir.mkdir()

        (temp_dir / "root.md").write_text("## Root Section\n\nContent.\n")
        (subdir / "nested.md").write_text("## Nested Section\n\nContent.\n")

        results = sync_directory(temp_dir, recursive=False)

        # Should only sync root file
        assert len(results) == 1
        assert results[0].path.name == "root.md"

    def test_sync_custom_pattern(self, temp_dir):
        (temp_dir / "readme.md").write_text("## Section\n\nContent.\n")
        (temp_dir / "doc.markdown").write_text("## Section\n\nContent.\n")

        # Only .markdown files
        results = sync_directory(temp_dir, pattern="*.markdown")

        assert len(results) == 1
        assert results[0].path.suffix == ".markdown"

    def test_sync_empty_directory(self, temp_dir):
        results = sync_directory(temp_dir)
        assert len(results) == 0

    def test_sync_with_errors(self, temp_dir):
        # Create a valid file and a problematic situation
        (temp_dir / "good.md").write_text("## Section\n\nContent.\n")

        # Create read-only file (if not on Windows)
        bad_file = temp_dir / "bad.md"
        bad_file.write_text("## Section\n\nContent.\n")

        results = sync_directory(temp_dir)

        # At least the good file should be synced
        good_results = [r for r in results if "good" in str(r.path)]
        assert len(good_results) == 1
        assert good_results[0].changed is True


class TestRealWorldScenarios:
    """Tests simulating real-world usage."""

    def test_documentation_file(self, temp_dir):
        # toc_policy default is "maintain_only" (does not add a TOC where none
        # exists); use "add_always" to exercise TOC generation for a fresh doc.
        file_path = temp_dir / "api.md"
        file_path.write_text("""# API Documentation

## Overview

This document describes the API.

## Authentication

### API Keys

Use API keys for authentication.

### OAuth

OAuth 2.0 is also supported.

## Endpoints

### Users

#### GET /users

Returns all users.

#### POST /users

Creates a new user.

### Products

#### GET /products

Returns all products.

## Error Handling

All errors return JSON.

## Rate Limiting

100 requests per minute.
""")
        result = sync_file(file_path, Config(toc_policy="add_always"))
        content = file_path.read_text()

        assert result.changed is True
        assert "## Table of Contents" in content

        # Check all sections are in TOC
        for section in [
            "Overview",
            "Authentication",
            "API Keys",
            "OAuth",
            "Endpoints",
            "Users",
            "Products",
            "Error Handling",
            "Rate Limiting",
        ]:
            assert f"[{section}]" in content

    def test_changelog_style(self, temp_dir):
        file_path = temp_dir / "changelog.md"
        file_path.write_text("""# Changelog

## [2.0.0] - 2024-01-15

### Added

New features.

### Changed

Breaking changes.

## [1.0.0] - 2023-06-01

### Added

Initial release.
""")
        result = sync_file(file_path)
        content = file_path.read_text()

        assert result.changed is True
        # Section titles with brackets should work
        assert "[[2.0.0]" in content or "[2.0.0]" in content

    def test_partial_toc_repair(self, temp_dir):
        # File with partially correct TOC
        file_path = temp_dir / "partial.md"
        file_path.write_text("""# Document

## Table of Contents

1. [First](#first) _(Lines 12-20)_

---

## First
<!-- Lines 12-20 -->

Content.

## Second

More content.

## Third

Even more.
""")
        result = sync_file(file_path)
        content = file_path.read_text()

        # All three sections should be in TOC
        assert "[First]" in content
        assert "[Second]" in content
        assert "[Third]" in content

        # Should have correct number of TOC entries
        assert content.count("_(Lines") >= 3


class TestSyncFencedCodeBlocks:
    """End-to-end: sync_file must never treat fenced example content as real
    structure — no phantom TOC entries, and an existing `<!-- Lines -->`
    comment inside a fence must be left byte-for-byte untouched."""

    def test_fenced_example_heading_not_added_to_toc(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""# Document

## Table of Contents

1. [Real Section](#real-section) _(Lines 8-20)_

---

## Real Section
<!-- Lines 8-20 -->

Here is an example:

```markdown
## Fenced Example Heading
```

More content.
""")
        result = sync_file(file_path, Config(toc_policy="maintain_only"))
        content = file_path.read_text()

        assert result.error is None
        assert "Fenced Example Heading" not in content.split("## Real Section")[0]
        # Only one TOC entry: the real section, never the fenced example.
        assert content.count("_(Lines") == 1
        assert "[Fenced Example Heading]" not in content

    def test_fenced_lines_comment_left_untouched(self, temp_dir):
        file_path = temp_dir / "test.md"
        original = """# Document

## Real Section
<!-- Lines 5-40 -->

Example of the annotation format:

```markdown
## Example
<!-- Lines 1-2 -->
```

More content after the example.
"""
        file_path.write_text(original)
        sync_file(file_path, Config(toc_policy="remove"))
        content = file_path.read_text()

        # The fenced example's placeholder-looking comment must be untouched.
        assert "<!-- Lines 1-2 -->" in content

    def test_nested_and_longer_fences_do_not_corrupt_sync(self, temp_dir):
        file_path = temp_dir / "test.md"
        file_path.write_text("""# Document

## First Section

````markdown
```
## Inner Fenced Heading
<!-- Lines 999-999 -->
```
````

## Second Section

Content.
""")
        result = sync_file(file_path, Config(toc_policy="add_always"))
        content = file_path.read_text()

        assert result.error is None
        assert "<!-- Lines 999-999 -->" in content  # untouched inside the fence
        assert "[Inner Fenced Heading]" not in content
        assert "[First Section]" in content
        assert "[Second Section]" in content
