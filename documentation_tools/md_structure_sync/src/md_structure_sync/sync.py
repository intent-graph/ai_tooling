"""Orchestrator: sync_file and sync_directory."""

from pathlib import Path

from md_structure_sync.fill import fill_numbers
from md_structure_sync.models import Config, SyncResult
from md_structure_sync.parse import gather_info
from md_structure_sync.structure import fix_structure


def sync_file(path: Path | str, config: Config | None = None) -> SyncResult:
    """Synchronize TOC and line ranges in a markdown file.

    Three-pass algorithm:
    1. Gather: Parse file structure (read-only)
    2. Structure: Insert placeholders for missing TOC/comments
    3. Fill: Compute and fill actual line numbers

    Args:
        path: Path to markdown file
        config: Configuration options (uses defaults if None)

    Returns:
        SyncResult with changed status and any errors
    """
    path = Path(path)
    config = config or Config()

    try:
        # Read file
        content = path.read_text()
        lines = content.splitlines(keepends=True)

        # Ensure last line has newline
        if lines and not lines[-1].endswith("\n"):
            lines[-1] = lines[-1] + "\n"

        # Pass 1: Gather information
        info = gather_info(lines, config)

        # Pass 2: Fix structure with placeholders
        lines = fix_structure(lines, info, config)

        # Pass 3: Fill line numbers
        lines = fill_numbers(lines, config)

        # Check if changed
        new_content = "".join(lines)
        changed = new_content != content

        # Write if changed and not dry run
        if changed and not config.dry_run:
            path.write_text(new_content)

        return SyncResult(path=path, changed=changed)

    except Exception as e:
        return SyncResult(path=path, changed=False, error=str(e))


def sync_directory(
    directory: Path | str,
    pattern: str = "*.md",
    config: Config | None = None,
    recursive: bool = True,
) -> list[SyncResult]:
    """Synchronize all markdown files in a directory.

    Args:
        directory: Directory to scan
        pattern: Glob pattern for files (default: *.md)
        config: Configuration options
        recursive: Whether to scan subdirectories

    Returns:
        List of SyncResult for each file
    """
    directory = Path(directory)
    config = config or Config()

    if recursive:
        files = directory.rglob(pattern)
    else:
        files = directory.glob(pattern)

    results = []
    for file_path in sorted(files):
        result = sync_file(file_path, config)
        results.append(result)

    return results
