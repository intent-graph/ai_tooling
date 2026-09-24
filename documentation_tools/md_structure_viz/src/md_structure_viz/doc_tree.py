"""Document tree discovery and analysis."""

import re
import subprocess
from dataclasses import dataclass, field
from fnmatch import fnmatch
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Patterns to exclude from documentation discovery
DEFAULT_IGNORE_PATTERNS = [
    # Python virtual environments
    "*venv*/lib/python*",
    "*/.venv/*",
    "*/virtualenv/*",
    "*/site-packages/*",
    "*/__pycache__/*",
    "*/.pytest_cache/*",
    "*/.tox/*",
    "*/eggs/*",
    "*/.eggs/*",
    # Node.js
    "*/node_modules/*",
    # Git
    "*/.git/*",
    # Build artifacts
    "*/dist/*",
    "*/build/*",
    "*/.build/*",
    # IDE
    "*/.idea/*",
    "*/.vscode/*",
    # OS
    "*/.DS_Store",
]


@dataclass
class DocNode:
    """Represents a markdown document."""

    path: Path
    title: str
    section_count: int
    headings: List[dict] = field(default_factory=list)
    word_count: int = 0
    line_count: int = 0
    toc_range: Optional[Tuple[int, int]] = None
    outgoing_refs: List[Path] = field(default_factory=list)
    incoming_refs: List[Path] = field(default_factory=list)

    @property
    def relative_path(self) -> str:
        """Get relative path from root."""
        return str(self.path)

    def __hash__(self):
        return hash(self.path)

    def __eq__(self, other):
        if not isinstance(other, DocNode):
            return False
        return self.path == other.path


@dataclass
class DocTree:
    """Represents the complete documentation tree."""

    root: Path
    nodes: Dict[Path, DocNode] = field(default_factory=dict)
    folders: Dict[Path, List[Path]] = field(default_factory=dict)

    @property
    def total_files(self) -> int:
        """Total number of files."""
        return len(self.nodes)

    @property
    def total_sections(self) -> int:
        """Total number of sections."""
        return sum(n.section_count for n in self.nodes.values())

    @property
    def total_refs(self) -> int:
        """Total number of cross-references."""
        return sum(len(n.outgoing_refs) for n in self.nodes.values())

    def get_files_by_folder(self, folder: Path) -> List[DocNode]:
        """Get files in a specific folder."""
        if folder in self.folders:
            return [self.nodes[f] for f in self.folders[folder] if f in self.nodes]
        return []

    def get_folder_hierarchy(self) -> Dict[Path, List[Path]]:
        """Get folder hierarchy."""
        return self.folders.copy()


def should_exclude_path(path: Path, root: Path, ignore_default: bool = True) -> bool:
    """Check if path should be excluded based on ignore patterns.

    Args:
        path: Path to check
        root: Root directory for relative path calculation
        ignore_default: If True, apply DEFAULT_IGNORE_PATTERNS

    Returns:
        True if path should be excluded, False otherwise
    """
    try:
        rel_path = str(path.relative_to(root))
    except ValueError:
        # Path is not relative to root
        return True

    if ignore_default:
        for pattern in DEFAULT_IGNORE_PATTERNS:
            if fnmatch(rel_path, pattern):
                return True

    return False


def is_git_ignored(path: Path, root: Path) -> bool:
    """Check if path is ignored by git.

    Args:
        path: Path to check
        root: Git repository root (should contain .git directory)

    Returns:
        True if path is git-ignored, False otherwise
    """
    try:
        rel_path = path.relative_to(root)
        result = subprocess.run(
            ["git", "check-ignore", "-q", str(rel_path)],
            cwd=str(root),
            capture_output=True,
            timeout=5,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, ValueError):
        # If git is not available, not a git repo, or path calculation fails
        return False


def discover_md_files(
    root: Path, ignore_default: bool = True, respect_gitignore: bool = False
) -> List[Path]:
    """Find all markdown files recursively, optionally excluding ignored patterns.

    Args:
        root: Root directory to search
        ignore_default: If True, apply DEFAULT_IGNORE_PATTERNS (default: True)
        respect_gitignore: If True, additionally respect .gitignore patterns (default: False)

    Returns:
        Sorted list of markdown file paths

    Raises:
        FileNotFoundError: If root directory does not exist
    """
    if not root.exists():
        raise FileNotFoundError(f"Root path does not exist: {root}")

    root = root.resolve()
    md_files = []
    for md_file in root.rglob("*.md"):
        # Check default ignore patterns
        if ignore_default and should_exclude_path(md_file, root, ignore_default=True):
            continue

        # Check git ignore patterns
        if respect_gitignore and is_git_ignored(md_file, root):
            continue

        md_files.append(md_file)

    return sorted(md_files)


def _detect_toc(lines: List[str]) -> Optional[Tuple[int, int]]:
    """Detect Table of Contents block and return its line range.

    Looks for '## Table of Contents' heading followed by numbered or bulleted
    list items with markdown links (e.g., managed TOCs from md-structure-sync).

    Args:
        lines: First N lines of the file to scan

    Returns:
        Tuple of (start_line, end_line) 1-indexed, or None if no TOC found
    """
    toc_start = None
    toc_end = None

    for i, line in enumerate(lines):
        line_num = i + 1

        if re.match(r"^##\s+Table of Contents", line, re.IGNORECASE):
            toc_start = line_num
            continue

        if toc_start is not None:
            # TOC items: numbered or bulleted list with markdown links
            if re.match(r"^\d+\.\s+\[", line) or re.match(r"^[-*]\s+\[", line):
                toc_end = line_num
            elif line.strip() == "":
                continue  # blank lines within TOC are OK
            elif toc_end is not None:
                break  # Non-empty non-TOC line after TOC content → done
            elif line_num > toc_start + 3 and toc_end is None:
                toc_start = None  # No TOC items found — false positive

    if toc_start is not None and toc_end is not None:
        return (toc_start, toc_end)
    return None


def extract_metadata(file: Path) -> Dict:
    """Extract title, headings, word count, line count, and TOC info from markdown file.

    Returns dict with keys:
        title (str): First # heading or filename
        sections (int): Total heading count (all levels)
        headings (list[dict]): Each heading with keys: level, text, line
        word_count (int): Total word count
        line_count (int): Total line count
        toc_range (tuple[int,int] | None): Line range of TOC block if detected
    """
    try:
        content = file.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        return {
            "title": file.name,
            "sections": 0,
            "headings": [],
            "word_count": 0,
            "line_count": 0,
            "toc_range": None,
            "error": str(e),
        }

    file_lines = content.split("\n")
    line_count = len(file_lines)
    word_count = len(content.split())

    # Extract first heading as title
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else file.name

    # Extract all headings with line numbers
    headings = []
    for i, line in enumerate(file_lines, 1):
        heading_match = re.match(r"^(#{1,6}) (.+)$", line)
        if heading_match:
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            headings.append({"level": level, "text": text, "line": i})

    sections = len(headings)

    # Detect TOC in first 100 lines
    toc_range = _detect_toc(file_lines[:100])

    return {
        "title": title,
        "sections": sections,
        "headings": headings,
        "word_count": word_count,
        "line_count": line_count,
        "toc_range": toc_range,
    }


def find_cross_refs(file: Path, root: Path) -> List[Path]:
    """Find markdown cross-references in a file."""
    try:
        content = file.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []

    # Find all markdown links with .md files
    # Pattern: [text](path/to/file.md)
    ref_pattern = r"\[([^\]]+)\]\(([^)]+\.md)\)"
    refs = re.findall(ref_pattern, content)

    seen = set()
    resolved_refs = []
    for _, ref_path in refs:
        # Resolve relative path
        target = file.parent / ref_path
        target = target.resolve()

        # Deduplicate
        if target in seen:
            continue
        seen.add(target)

        # Only include if target exists and is under root
        if target.exists() and target.is_file():
            try:
                # Check if target is under root
                target.relative_to(root)
                resolved_refs.append(target)
            except ValueError:
                # File is outside root, skip
                pass

    return resolved_refs


def build_doc_tree(
    root: Path, ignore_default: bool = True, respect_gitignore: bool = False
) -> DocTree:
    """Build complete documentation tree with cross-references.

    Args:
        root: Root documentation directory
        ignore_default: If True, apply DEFAULT_IGNORE_PATTERNS (default: True)
        respect_gitignore: If True, additionally respect .gitignore patterns (default: False)

    Returns:
        DocTree instance representing the documentation structure
    """
    root = root.resolve()

    # Phase 1: Discover files and extract metadata
    md_files = discover_md_files(root, ignore_default=ignore_default, respect_gitignore=respect_gitignore)
    nodes: Dict[Path, DocNode] = {}

    for md_file in md_files:
        md_file = md_file.resolve()
        metadata = extract_metadata(md_file)

        nodes[md_file] = DocNode(
            path=md_file,
            title=metadata.get("title", md_file.name),
            section_count=metadata.get("sections", 0),
            headings=metadata.get("headings", []),
            word_count=metadata.get("word_count", 0),
            line_count=metadata.get("line_count", 0),
            toc_range=metadata.get("toc_range"),
        )

    # Phase 2: Find cross-references
    for md_file, node in nodes.items():
        refs = find_cross_refs(md_file, root)
        node.outgoing_refs = [r for r in refs if r in nodes]

    # Phase 3: Build incoming references
    for node in nodes.values():
        for target in node.outgoing_refs:
            if target in nodes:
                nodes[target].incoming_refs.append(node.path)

    # Phase 4: Build folder hierarchy
    folders: Dict[Path, List[Path]] = {}
    for md_file in nodes.keys():
        folder = md_file.parent
        if folder not in folders:
            folders[folder] = []
        folders[folder].append(md_file)

    return DocTree(root=root, nodes=nodes, folders=folders)


def get_orphaned_files(tree: DocTree) -> List[DocNode]:
    """Get files with no incoming references."""
    orphaned = []
    for node in tree.nodes.values():
        # Root README is not orphaned even if no refs
        if node.path.name == "README.md" and node.path.parent == tree.root:
            continue
        if len(node.incoming_refs) == 0:
            orphaned.append(node)
    return orphaned


def get_circular_refs(tree: DocTree) -> List[tuple[Path, Path]]:
    """Detect circular references in documentation."""
    visited: Set[Path] = set()
    cycles: List[tuple[Path, Path]] = []

    def dfs(node_path: Path, path: List[Path]) -> bool:
        if node_path in path:
            # Found a cycle
            start_idx = path.index(node_path)
            cycles.append((path[start_idx], node_path))
            return True

        if node_path in visited:
            return False

        visited.add(node_path)
        if node_path not in tree.nodes:
            return False

        node = tree.nodes[node_path]
        for ref in node.outgoing_refs:
            dfs(ref, path + [node_path])

        return False

    for start_file in tree.nodes.keys():
        visited.clear()
        dfs(start_file, [])

    return cycles
