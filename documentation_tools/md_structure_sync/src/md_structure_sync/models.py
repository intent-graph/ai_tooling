"""Data models for md-structure-sync."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

# TOC policy: when to add, maintain, or remove TOC
TocPolicy = Literal["maintain_only", "add_above_size", "remove", "add_always"]


@dataclass
class Config:
    """Configuration for sync operations."""

    min_level: int = 2  # Track H2+
    max_level: int = 4  # Up to H4
    include_line_comments: bool = True  # Add <!-- Lines --> after headers
    toc_title: str = "Table of Contents"
    placeholder: str = "???"
    dry_run: bool = False
    # TOC policy: maintain_only (default), add_above_size, remove, add_always
    toc_policy: TocPolicy = "maintain_only"
    toc_min_headers: int = 3  # Only add TOC when header count >= this (if toc_policy is add_above_size)


@dataclass
class TocEntryInfo:
    """Information about a single TOC entry."""

    line: int  # 1-indexed line number
    indent_level: int  # 0 = top-level, 1 = indented
    title: str
    anchor: str
    range_start: int | None = None  # None if missing or placeholder
    range_end: int | None = None


@dataclass
class TocInfo:
    """Information about an existing TOC."""

    header_line: int  # Line of "## Table of Contents"
    first_entry_line: int | None  # First numbered entry (None if no entries)
    last_entry_line: int | None  # Last entry line
    separator_line: int | None  # Line of --- separator (if exists)
    entries: list[TocEntryInfo] = field(default_factory=list)

    @property
    def entry_count(self) -> int:
        return len(self.entries)

    @property
    def end_line(self) -> int:
        """Last line of TOC block (separator or last entry)."""
        if self.separator_line:
            return self.separator_line
        if self.last_entry_line:
            return self.last_entry_line
        return self.header_line


@dataclass
class HeaderInfo:
    """Information about a section header."""

    line: int  # 1-indexed line number
    level: int  # 2 for ##, 3 for ###
    title: str
    anchor: str

    # Line range comment status
    has_range_comment: bool = False
    range_comment_line: int | None = None
    range_start: int | None = None  # Parsed value (None if missing/malformed/placeholder)
    range_end: int | None = None
    is_placeholder: bool = False  # True if contains ???


@dataclass
class FileInfo:
    """Complete parse result from Pass 1."""

    lines: list[str]  # Original lines (with newlines)
    title: str | None = None  # H1 content
    title_line: int | None = None  # H1 line number

    toc: TocInfo | None = None
    headers: list[HeaderInfo] = field(default_factory=list)


@dataclass
class SectionRange:
    """Computed range for a section (Pass 3 output)."""

    title: str
    anchor: str
    level: int
    line_start: int  # Content start (after header + comment)
    line_end: int  # Last line before next section or EOF


@dataclass
class SyncResult:
    """Result of a sync operation."""

    path: Path
    changed: bool
    error: str | None = None


# =============================================================================
# Cross-Reference Validation Models
# =============================================================================


@dataclass
class TocSyncState:
    """Tracks which files have had toc_sync applied.

    Uses resolved absolute paths for O(1) lookup.
    """

    completed: set[Path] = field(default_factory=set)
    dirty: set[Path] = field(default_factory=set)

    def is_toc_synced(self, path: Path) -> bool:
        """Check if file has been toc_synced."""
        return path.resolve() in self.completed

    def mark_toc_synced(self, path: Path) -> None:
        """Mark file as toc_synced."""
        self.completed.add(path.resolve())

    def mark_dirty(self, path: Path) -> None:
        """Mark file as needing re-sync after xref changes."""
        self.dirty.add(path.resolve())

    def clear_dirty(self, path: Path) -> None:
        """Remove file from dirty set after re-sync."""
        self.dirty.discard(path.resolve())


@dataclass
class CrossRef:
    """A cross-reference link found in a markdown file."""

    line: int  # 1-indexed
    col_start: int  # 0-indexed column start
    col_end: int  # 0-indexed column end (exclusive)
    display_text: str  # Text shown to user
    target_path: str  # Relative path to target file
    target_anchor: str | None  # Anchor within target (None if file-only)

    @property
    def full_link(self) -> str:
        """Reconstruct the full markdown link."""
        if self.target_anchor:
            return f"[{self.display_text}]({self.target_path}#{self.target_anchor})"
        return f"[{self.display_text}]({self.target_path})"


@dataclass
class ValidationResult:
    """Result of validating a single cross-reference."""

    ref: CrossRef
    status: str  # "valid", "file_missing", "anchor_missing", "anchor_fuzzy"
    suggested_anchor: str | None = None  # For fuzzy matches
    similarity_score: float | None = None  # For fuzzy matches


@dataclass
class CrossRefResult:
    """Result of cross-reference validation for a file."""

    path: Path
    refs_found: int
    refs_valid: int
    refs_invalid: int
    refs_fixed: int
    changed: bool
    error: str | None = None
    validations: list[ValidationResult] = field(default_factory=list)
