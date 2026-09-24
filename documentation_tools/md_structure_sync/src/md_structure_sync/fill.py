"""Pass 3: Fill line numbers (bottom-to-top)."""

import re

from md_structure_sync.models import Config, FileInfo, SectionRange
from md_structure_sync.parse import gather_info

# Pattern to match placeholder or existing range in comment
RANGE_IN_COMMENT = re.compile(r"(\d+|\?{3})\s*[-–—]\s*(\d+|\?{3})")

# Pattern to match placeholder or existing range in TOC entry
RANGE_IN_TOC = re.compile(r"_\(Lines?\s+(\d+|\?{3})\s*[-–—]\s*(\d+|\?{3})\)_")


def fill_numbers(lines: list[str], config: Config) -> list[str]:
    """Pass 3: Fill all line numbers.

    1. Re-parse to get stable structure
    2. Compute ranges bottom-to-top
    3. Fill header comments
    4. Fill TOC entries
    """
    result = lines.copy()

    # Re-parse to get current structure
    info = gather_info(result, config)

    if not info.headers:
        return result

    # Compute ranges for all sections
    ranges = _compute_ranges(info)

    # Fill header comments (bottom-to-top for safety, though structure is stable)
    result = _fill_header_comments(result, info, ranges)

    # Re-parse to get updated TOC positions
    info = gather_info(result, config)

    # Fill TOC entries
    if info.toc:
        result = _fill_toc_entries(result, info, ranges)

    return result


def _compute_ranges(info: FileInfo) -> list[SectionRange]:
    """Compute actual line ranges for each section.

    For header at line L with comment at L+1:
    - content_start = L + 2
    - content_end = (next_header - 1) or EOF
    """
    ranges = []
    headers = info.headers
    total_lines = len(info.lines)

    for i, header in enumerate(headers):
        # Content starts after header and comment
        content_start = header.line + 2  # header + comment

        # Content ends before next header (or at EOF)
        if i + 1 < len(headers):
            next_header = headers[i + 1]
            content_end = next_header.line - 1
        else:
            content_end = total_lines

        ranges.append(
            SectionRange(
                title=header.title,
                anchor=header.anchor,
                level=header.level,
                line_start=content_start,
                line_end=content_end,
            )
        )

    return ranges


def _fill_header_comments(
    lines: list[str], info: FileInfo, ranges: list[SectionRange]
) -> list[str]:
    """Fill line numbers in header comments."""
    result = lines.copy()

    for header, section_range in zip(info.headers, ranges):
        if not header.has_range_comment:
            continue

        comment_idx = header.range_comment_line - 1  # 0-indexed
        old_line = result[comment_idx]

        # Replace the range
        new_line = RANGE_IN_COMMENT.sub(
            f"{section_range.line_start}-{section_range.line_end}",
            old_line,
        )
        result[comment_idx] = new_line

    return result


def _fill_toc_entries(
    lines: list[str], info: FileInfo, ranges: list[SectionRange]
) -> list[str]:
    """Fill line numbers in TOC entries.

    Match by index (position), not by anchor - this handles duplicate titles
    correctly since TOC entries and headers are in the same order.
    """
    result = lines.copy()
    toc = info.toc

    if not toc or not toc.entries:
        return result

    # Match TOC entries to ranges by index (both are in document order)
    for i, entry in enumerate(toc.entries):
        if i >= len(ranges):
            # More TOC entries than headers (shouldn't happen after Pass 2)
            continue

        section_range = ranges[i]
        entry_idx = entry.line - 1  # 0-indexed
        old_line = result[entry_idx]

        # Replace the range in TOC entry
        new_range = f"_(Lines {section_range.line_start}-{section_range.line_end})_"
        new_line = RANGE_IN_TOC.sub(new_range, old_line)
        result[entry_idx] = new_line

    return result
