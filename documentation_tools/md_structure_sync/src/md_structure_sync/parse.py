"""Pass 1: Information gathering (read-only parse)."""

import re

from md_structure_sync.anchors import slugify
from md_structure_sync.models import Config, FileInfo, HeaderInfo, TocEntryInfo, TocInfo

# Patterns
HEADER_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

# Fenced code block delimiter: ``` or ~~~, optionally indented, with an optional
# info string after the marker (e.g. ```markdown). Per CommonMark, a fence closes
# only with a line using the *same* marker character and at least the same length.
FENCE_PATTERN = re.compile(r"^(\s*)(`{3,}|~{3,})")


def _line_fence_states(lines: list[str]) -> list[bool]:
    """Return, for each line, whether that line lies inside a fenced code block.

    A fence-opening line itself and a fence-closing line are both considered
    "inside the fence" (they are not headers, TOC entries or line-range
    comments), matching CommonMark's fence semantics: a fence closes only on a
    line with the same marker character and at least the same length as the
    opener.
    """
    in_fence = [False] * len(lines)
    fence_char: str | None = None
    fence_len = 0
    open_now = False

    for i, line in enumerate(lines):
        match = FENCE_PATTERN.match(line)
        if not open_now:
            if match:
                in_fence[i] = True
                open_now = True
                fence_char = match.group(2)[0]
                fence_len = len(match.group(2))
            else:
                in_fence[i] = False
        else:
            in_fence[i] = True
            if match:
                marker = match.group(2)
                if marker[0] == fence_char and len(marker) >= fence_len:
                    open_now = False
                    fence_char = None
                    fence_len = 0

    return in_fence

# Line range comment: <!-- Lines 30-75 --> or <!-- Lines ???-??? -->
# Tolerant of Line/Lines, various dash types, spaces
LINE_RANGE_PATTERN = re.compile(
    r"^<!--\s*Lines?\s+(\d+|\?{3})\s*[-–—]\s*(\d+|\?{3})\s*-->\s*$"
)

# TOC header
TOC_HEADER_PATTERN = re.compile(r"^##\s+Table of Contents\s*$", re.IGNORECASE)

# TOC entry: "1. [Title](#anchor) _(Lines X-Y)_" or without range
# Note: title can contain brackets like [[1.0.0]], so match until ](#
TOC_ENTRY_PATTERN = re.compile(
    r"^(\s*)"  # indent
    r"\d+\.\s+"  # number (ignored, markdown auto-numbers)
    r"\[(.+?)\]\(#"  # [title](#  - non-greedy match for title
    r"([^)]+)\)"  # anchor)
    r"(?:\s+_\(Lines?\s+(\d+|\?{3})\s*[-–—]\s*(\d+|\?{3})\)_)?"  # optional range
    r"\s*$"
)

# Horizontal rule
HR_PATTERN = re.compile(r"^---+\s*$")


def gather_info(lines: list[str], config: Config) -> FileInfo:
    """Pass 1: Gather information about file structure.

    This is read-only - no modifications to lines.
    """
    info = FileInfo(lines=lines)
    in_fence = _line_fence_states(lines)

    # Find H1 title
    _find_title(info, in_fence)

    # Find TOC
    _find_toc(info, config, in_fence)

    # Find all headers (H2+)
    _find_headers(info, config, in_fence)

    return info


def _find_title(info: FileInfo, in_fence: list[bool]) -> None:
    """Find H1 title if present."""
    for i, line in enumerate(info.lines):
        if in_fence[i]:
            continue
        match = HEADER_PATTERN.match(line)
        if match:
            level = len(match.group(1))
            if level == 1:
                info.title = match.group(2).strip()
                info.title_line = i + 1  # 1-indexed
                return
            # If first header is not H1, no title
            return


def _find_toc(info: FileInfo, config: Config, in_fence: list[bool]) -> None:
    """Find existing TOC if present."""
    toc_header_line = None

    # Find TOC header
    for i, line in enumerate(info.lines):
        if in_fence[i]:
            continue
        if TOC_HEADER_PATTERN.match(line):
            toc_header_line = i + 1  # 1-indexed
            break

    if toc_header_line is None:
        return

    # Parse TOC entries
    entries: list[TocEntryInfo] = []
    first_entry_line = None
    last_entry_line = None
    separator_line = None

    # Scan lines after TOC header
    i = toc_header_line  # 0-indexed position after header
    while i < len(info.lines):
        line = info.lines[i]
        line_num = i + 1  # 1-indexed

        if in_fence[i]:
            # Fenced content never counts as TOC structure (separator, next
            # header, or entry); skip over it entirely.
            i += 1
            continue

        # Check for separator (end of TOC)
        if HR_PATTERN.match(line):
            separator_line = line_num
            break

        # Check for next H2 (end of TOC without separator)
        header_match = HEADER_PATTERN.match(line)
        if header_match and len(header_match.group(1)) == 2:
            # Don't include this line as part of TOC
            break

        # Check for TOC entry
        entry_match = TOC_ENTRY_PATTERN.match(line)
        if entry_match:
            indent = entry_match.group(1)
            indent_level = len(indent) // 3  # 3 spaces per level

            title = entry_match.group(2)
            anchor = entry_match.group(3)

            range_start = None
            range_end = None
            if entry_match.group(4) and entry_match.group(5):
                start_str = entry_match.group(4)
                end_str = entry_match.group(5)
                if start_str != "???" and end_str != "???":
                    try:
                        range_start = int(start_str)
                        range_end = int(end_str)
                    except ValueError:
                        pass

            entries.append(
                TocEntryInfo(
                    line=line_num,
                    indent_level=indent_level,
                    title=title,
                    anchor=anchor,
                    range_start=range_start,
                    range_end=range_end,
                )
            )

            if first_entry_line is None:
                first_entry_line = line_num
            last_entry_line = line_num

        i += 1

    info.toc = TocInfo(
        header_line=toc_header_line,
        first_entry_line=first_entry_line,
        last_entry_line=last_entry_line,
        separator_line=separator_line,
        entries=entries,
    )


def _find_headers(info: FileInfo, config: Config, in_fence: list[bool]) -> None:
    """Find all headers in configured range (H2-H4 by default)."""
    # Skip TOC header itself
    toc_header_line = info.toc.header_line if info.toc else None

    for i, line in enumerate(info.lines):
        line_num = i + 1  # 1-indexed

        if in_fence[i]:
            continue

        match = HEADER_PATTERN.match(line)
        if not match:
            continue

        level = len(match.group(1))

        # Skip if outside configured range
        if level < config.min_level or level > config.max_level:
            continue

        # Skip TOC header
        if line_num == toc_header_line:
            continue

        title = match.group(2).strip()
        anchor = slugify(title)

        header = HeaderInfo(
            line=line_num,
            level=level,
            title=title,
            anchor=anchor,
        )

        # Check next line for range comment
        if i + 1 < len(info.lines):
            next_line = info.lines[i + 1]
            range_match = LINE_RANGE_PATTERN.match(next_line)
            if range_match:
                header.has_range_comment = True
                header.range_comment_line = line_num + 1

                start_str = range_match.group(1)
                end_str = range_match.group(2)

                if start_str == "???" or end_str == "???":
                    header.is_placeholder = True
                else:
                    try:
                        header.range_start = int(start_str)
                        header.range_end = int(end_str)
                    except ValueError:
                        header.is_placeholder = True

        info.headers.append(header)
