"""Pass 2: Structure fixing with placeholders."""

from md_structure_sync.anchors import make_unique_anchors, slugify
from md_structure_sync.models import Config, FileInfo, HeaderInfo
from md_structure_sync.parse import HEADER_PATTERN, gather_info


def fix_structure(lines: list[str], info: FileInfo, config: Config) -> list[str]:
    """Pass 2: Ensure correct structure with placeholders.

    - Insert/fix TOC with placeholder entries
    - Insert/fix line range comments with placeholders

    Returns new list of lines (may be different length).
    """
    # remove policy with no existing TOC: nothing to strip, leave the file untouched
    # (remove is a TOC-stripping mode, not general header-comment maintenance).
    if config.toc_policy == "remove" and info.toc is None:
        return lines.copy()

    result = lines.copy()

    # Step 1: Fix header comments (bottom-to-top to preserve line numbers)
    result = _fix_header_comments(result, info, config)

    # Step 2: Re-parse after comment changes
    info = gather_info(result, config)

    # Step 3: Fix TOC
    result = _fix_toc(result, info, config)

    return result


def _fix_header_comments(lines: list[str], info: FileInfo, config: Config) -> list[str]:
    """Insert missing line range comments after headers.

    Process bottom-to-top so insertions don't shift later line numbers.
    """
    if not config.include_line_comments:
        return lines

    result = lines.copy()
    placeholder = config.placeholder

    # Process headers in reverse order (bottom to top)
    for header in reversed(info.headers):
        if header.has_range_comment:
            # Comment exists - will be updated in Pass 3
            continue

        # Insert placeholder comment after header
        # header.line is 1-indexed, so index = header.line - 1
        # Insert at index header.line (which is right after the header)
        insert_idx = header.line  # 0-indexed position after header line
        comment_line = f"<!-- Lines {placeholder}-{placeholder} -->\n"
        result.insert(insert_idx, comment_line)

    return result


def _fix_toc(lines: list[str], info: FileInfo, config: Config) -> list[str]:
    """Fix, insert, or remove TOC according to config.toc_policy."""
    policy = config.toc_policy

    # remove: strip TOC block (header + entries + separator) if present
    if policy == "remove":
        if info.toc is not None:
            return _remove_toc(lines, info.toc)
        return lines.copy()

    # No headers = no TOC needed (for add/maintain)
    if not info.headers:
        return lines.copy()

    result = lines.copy()
    placeholder = config.placeholder
    expected_entries = _build_toc_entries(info.headers, placeholder, config)

    if info.toc is None:
        # No TOC exists - insert only when policy allows
        if policy == "maintain_only":
            return lines.copy()
        if policy == "add_above_size" and len(info.headers) < config.toc_min_headers:
            return lines.copy()
        result = _insert_toc(result, info, expected_entries, config)
    else:
        # TOC exists - maintain: rebuild if entries don't match
        if policy == "maintain_only" or policy == "add_above_size" or policy == "add_always":
            if _toc_needs_rebuild(info.toc, info.headers):
                result = _rebuild_toc_entries(result, info, expected_entries, config)

    return result


def _remove_toc(lines: list[str], toc) -> list[str]:
    """Remove TOC block: header line, blank, entries, blank, separator (and trailing blank)."""
    result = lines.copy()
    # 1-indexed header_line..end_line inclusive → 0-indexed slice [start:end)
    start_0 = toc.header_line - 1
    end_0 = toc.end_line  # exclusive: deletes indices start_0..end_0-1 = lines header_line..end_line
    del result[start_0:end_0]
    return result


def _build_toc_entries(
    headers: list[HeaderInfo], placeholder: str, config: Config
) -> list[str]:
    """Build TOC entry lines from headers."""
    entries = []
    min_level = config.min_level

    # Generate unique anchors for duplicate titles
    titles = [h.title for h in headers]
    unique_anchors = make_unique_anchors(titles)

    for header, anchor in zip(headers, unique_anchors):
        indent_level = header.level - min_level
        indent = "   " * indent_level
        entry = (
            f"{indent}1. [{header.title}](#{anchor}) "
            f"_(Lines {placeholder}-{placeholder})_\n"
        )
        entries.append(entry)

    return entries


def _insert_toc(
    lines: list[str], info: FileInfo, entries: list[str], config: Config
) -> list[str]:
    """Insert a complete TOC at the appropriate location."""
    result = lines.copy()

    # Determine insertion point
    if info.title_line:
        # After H1 and any following blank lines
        insert_idx = info.title_line  # 0-indexed: right after H1
        # Skip blank lines after H1
        while insert_idx < len(result) and result[insert_idx].strip() == "":
            insert_idx += 1
    else:
        # At the very beginning
        insert_idx = 0

    # Build TOC block
    toc_lines = [
        f"## {config.toc_title}\n",
        "\n",
    ]
    toc_lines.extend(entries)
    toc_lines.extend([
        "\n",
        "---\n",
        "\n",
    ])

    # Insert TOC
    for i, line in enumerate(toc_lines):
        result.insert(insert_idx + i, line)

    return result


def _toc_needs_rebuild(toc, headers: list[HeaderInfo]) -> bool:
    """Check if TOC entries need to be rebuilt.

    Returns True if:
    - Entry count doesn't match header count
    - Entry anchors don't match expected unique anchors (in order)
    """
    if len(toc.entries) != len(headers):
        return True

    # Generate expected unique anchors for comparison
    titles = [h.title for h in headers]
    expected_anchors = make_unique_anchors(titles)

    # Check if TOC anchors match expected unique anchors in order
    for entry, expected_anchor in zip(toc.entries, expected_anchors):
        if entry.anchor != expected_anchor:
            return True

    return False


def _rebuild_toc_entries(
    lines: list[str], info: FileInfo, entries: list[str], config: Config
) -> list[str]:
    """Remove old TOC entries and insert new ones."""
    result = lines.copy()
    toc = info.toc

    # Find the range to replace
    # Start: line after TOC header (skip blank line if present)
    start_idx = toc.header_line  # 0-indexed: line after "## Table of Contents"

    # Skip blank lines after TOC header
    while start_idx < len(result) and result[start_idx].strip() == "":
        start_idx += 1

    # End: line before separator (or before next section)
    if toc.separator_line:
        end_idx = toc.separator_line - 1  # 0-indexed: line before ---
    elif toc.last_entry_line:
        end_idx = toc.last_entry_line  # 0-indexed: line after last entry
    else:
        end_idx = start_idx

    # Skip blank lines before separator
    while end_idx > start_idx and result[end_idx - 1].strip() == "":
        end_idx -= 1

    # Remove old entries
    del result[start_idx:end_idx]

    # Insert new entries
    # Add blank line before entries if not present
    insert_lines = []
    if start_idx > 0 and result[start_idx - 1].strip() != "":
        insert_lines.append("\n")

    insert_lines.extend(entries)

    # Add blank line after entries if separator follows
    if toc.separator_line:
        insert_lines.append("\n")

    for i, line in enumerate(insert_lines):
        result.insert(start_idx + i, line)

    return result


def _ensure_newline(line: str) -> str:
    """Ensure line ends with newline."""
    if not line.endswith("\n"):
        return line + "\n"
    return line
