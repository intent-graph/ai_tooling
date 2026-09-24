"""Cross-reference parsing from markdown files."""

import re
from pathlib import Path

from md_structure_sync.models import CrossRef

# Pattern to match markdown links to .md files
# Captures: [display text](path/to/file.md) or [display text](path/to/file.md#anchor)
XREF_PATTERN = re.compile(
    r"\[([^\]]+)\]"  # [display text]
    r"\("
    r"([^)#]+\.md)"  # path/to/file.md (must end in .md)
    r"(?:#([^)]+))?"  # optional #anchor
    r"\)"
)

# Pattern for self-references (same-file anchors)
SELF_REF_PATTERN = re.compile(
    r"\[([^\]]+)\]"  # [display text]
    r"\(#([^)]+)\)"  # (#anchor)
)


def parse_cross_refs(lines: list[str], include_self_refs: bool = False) -> list[CrossRef]:
    """Extract all cross-references from markdown lines.

    Args:
        lines: List of lines (with newlines)
        include_self_refs: If True, also include same-file #anchor references

    Returns:
        List of CrossRef objects, sorted by line number then column
    """
    refs = []

    for line_num, line in enumerate(lines, start=1):
        # Find .md file references
        for match in XREF_PATTERN.finditer(line):
            display_text = match.group(1)
            target_path = match.group(2)
            target_anchor = match.group(3)  # May be None

            refs.append(
                CrossRef(
                    line=line_num,
                    col_start=match.start(),
                    col_end=match.end(),
                    display_text=display_text,
                    target_path=target_path,
                    target_anchor=target_anchor,
                )
            )

        # Find self-references if requested
        if include_self_refs:
            for match in SELF_REF_PATTERN.finditer(line):
                # Skip if this position was already matched as a file ref
                already_matched = any(
                    r.line == line_num
                    and r.col_start <= match.start() < r.col_end
                    for r in refs
                )
                if already_matched:
                    continue

                display_text = match.group(1)
                anchor = match.group(2)

                refs.append(
                    CrossRef(
                        line=line_num,
                        col_start=match.start(),
                        col_end=match.end(),
                        display_text=display_text,
                        target_path="",  # Empty string = self-reference
                        target_anchor=anchor,
                    )
                )

    # Sort by line, then column
    refs.sort(key=lambda r: (r.line, r.col_start))
    return refs


def resolve_target_path(source_file: Path, target_path: str) -> Path:
    """Resolve a relative target path against the source file's location.

    Args:
        source_file: Path to the file containing the reference
        target_path: Relative path from the source file

    Returns:
        Resolved absolute path to the target file
    """
    if not target_path:
        # Self-reference
        return source_file.resolve()

    source_dir = source_file.parent
    return (source_dir / target_path).resolve()


def get_unique_target_paths(
    source_file: Path, refs: list[CrossRef]
) -> set[Path]:
    """Get unique resolved target file paths from cross-references.

    Args:
        source_file: Path to the file containing the references
        refs: List of cross-references

    Returns:
        Set of unique resolved paths (excluding self-references)
    """
    targets = set()
    source_resolved = source_file.resolve()

    for ref in refs:
        if not ref.target_path:
            # Self-reference, skip
            continue

        target = resolve_target_path(source_file, ref.target_path)
        if target != source_resolved:
            targets.add(target)

    return targets
