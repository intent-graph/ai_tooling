"""YAML manifest generation for documentation trees.

Generates two YAML files from a DocTree:
- sections YAML: folder-nested hierarchy with headings, line numbers, word counts, TOC refs
- cross-refs YAML: folder-nested hierarchy with outgoing document links

Both files use folder paths as nested YAML keys, reflecting the actual directory tree.
Intermediate empty folders are collapsed (e.g., ``doc/generated_doc/gen_ai_doc/``).
Designed for LLM consumption: compact, grep-friendly, actionable line numbers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .doc_tree import DocNode, DocTree


# ---------------------------------------------------------------------------
# Internal tree structure
# ---------------------------------------------------------------------------


@dataclass
class _FolderNode:
    """Internal tree node representing a folder in the hierarchy."""

    display_name: str  # e.g. "api/" or "doc/generated_doc/" (when collapsed)
    path: Path
    files: List[DocNode] = field(default_factory=list)
    children: Dict[str, "_FolderNode"] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _yaml_escape(s: str) -> str:
    """Escape a string for use inside YAML double quotes."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def _get_adaptive_headings(
    node: DocNode, heading_depth: int, max_sections: int
) -> Tuple[List[dict], Optional[str]]:
    """Get headings for a node, adapting depth if section count exceeds threshold.

    Tries the requested depth first. If the heading count exceeds *max_sections*,
    falls back one level at a time until h1 (which is always shown regardless).

    Returns:
        (filtered_headings, collapse_note_or_None)
    """
    if not node.headings:
        return [], None

    for depth in range(heading_depth, 0, -1):
        filtered = [h for h in node.headings if h["level"] <= depth]
        if len(filtered) <= max_sections or depth == 1:
            if depth < heading_depth:
                total = len([h for h in node.headings if h["level"] <= heading_depth])
                note = (
                    f"{total} sections (showing h{depth} only, "
                    f"h{depth + 1} exceeded {max_sections})"
                )
                return filtered, note
            return filtered, None

    # Fallback: return all (shouldn't reach here)
    return node.headings, None


def _format_file_meta(node: DocNode, collapse_note: Optional[str] = None) -> str:
    """Format the YAML comment with file metadata.

    Examples:
        ``# 120 lines, 850 words``
        ``# 120 lines, 850 words, TOC@3-25``
        ``# 2000 lines, 15000 words, 45 sections (showing h1 only, h2 exceeded 20)``
    """
    parts = [f"{node.line_count} lines", f"{node.word_count} words"]

    if node.toc_range:
        parts.append(f"TOC@{node.toc_range[0]}-{node.toc_range[1]}")

    if collapse_note:
        parts.append(collapse_note)

    return "# " + ", ".join(parts)


# ---------------------------------------------------------------------------
# Tree building and collapsing
# ---------------------------------------------------------------------------


def _build_folder_tree(tree: DocTree) -> _FolderNode:
    """Build a nested folder tree from the flat DocTree.folders dict.

    Creates intermediate folder nodes as needed so that the tree is fully
    connected from root to every file-bearing folder.
    """
    root = tree.root
    all_folders: Dict[Path, _FolderNode] = {}

    # Create nodes for folders that have files
    for folder_path, file_paths in tree.folders.items():
        files = sorted(
            [tree.nodes[f] for f in file_paths if f in tree.nodes],
            key=lambda n: n.path.name,
        )
        name = "./" if folder_path == root else folder_path.name + "/"
        all_folders[folder_path] = _FolderNode(
            display_name=name, path=folder_path, files=files
        )

    # Create intermediate folder nodes (needed for hierarchy wiring)
    for folder_path in list(all_folders.keys()):
        current = folder_path.parent
        while current != root and current not in all_folders:
            all_folders[current] = _FolderNode(
                display_name=current.name + "/",
                path=current,
            )
            current = current.parent

    # Ensure root exists
    if root not in all_folders:
        all_folders[root] = _FolderNode(display_name="./", path=root)

    # Wire parent -> child relationships
    for folder_path, node in all_folders.items():
        if folder_path == root:
            continue
        parent_path = folder_path.parent
        if parent_path in all_folders:
            all_folders[parent_path].children[folder_path.name] = node

    return all_folders[root]


def _collapse_folder_tree(node: _FolderNode) -> _FolderNode:
    """Collapse intermediate folders that have no files and exactly one child.

    E.g., ``doc/`` -> ``generated_doc/`` -> ``gen_ai_doc/`` (files here)
    becomes a single node with display_name ``doc/generated_doc/gen_ai_doc/``.
    """
    # Recursively collapse children first
    collapsed_children: Dict[str, _FolderNode] = {}
    for name in sorted(node.children):
        child = _collapse_folder_tree(node.children[name])

        # Merge single-child empty intermediates
        while not child.files and len(child.children) == 1:
            grandchild = next(iter(child.children.values()))
            child = _FolderNode(
                display_name=child.display_name + grandchild.display_name,
                path=grandchild.path,
                files=grandchild.files,
                children=grandchild.children,
            )

        collapsed_children[child.display_name] = child

    return _FolderNode(
        display_name=node.display_name,
        path=node.path,
        files=node.files,
        children=collapsed_children,
    )


def _build_collapsed_folders(tree: DocTree) -> _FolderNode:
    """Build and collapse the folder tree. Public helper for testing."""
    raw_tree = _build_folder_tree(tree)
    return _collapse_folder_tree(raw_tree)


# ---------------------------------------------------------------------------
# YAML rendering (recursive)
# ---------------------------------------------------------------------------


def _render_sections_folder(
    node: _FolderNode,
    indent: int,
    lines: List[str],
    heading_depth: int,
    max_sections: int,
) -> None:
    """Recursively render a folder node as sections YAML."""
    prefix = "  " * indent
    lines.append(f"{prefix}{node.display_name}:")

    # Render files
    file_prefix = "  " * (indent + 1)
    heading_prefix = "  " * (indent + 2)
    for file_node in node.files:
        headings, collapse_note = _get_adaptive_headings(
            file_node, heading_depth, max_sections
        )
        meta = _format_file_meta(file_node, collapse_note)
        filename = file_node.path.name

        if headings:
            lines.append(f"{file_prefix}{filename}: {meta}")
            for h in headings:
                escaped = _yaml_escape(h["text"])
                hashes = "#" * h["level"]
                lines.append(f'{heading_prefix}- "{h["line"]}: {hashes} {escaped}"')
        else:
            lines.append(f"{file_prefix}{filename}: [] {meta}")

    # Render subfolders
    for child_name in sorted(node.children):
        _render_sections_folder(
            node.children[child_name], indent + 1, lines, heading_depth, max_sections
        )


def _render_cross_refs_folder(
    node: _FolderNode,
    indent: int,
    lines: List[str],
    root: Path,
) -> None:
    """Recursively render a folder node as cross-refs YAML."""
    prefix = "  " * indent
    lines.append(f"{prefix}{node.display_name}:")

    file_prefix = "  " * (indent + 1)
    ref_prefix = "  " * (indent + 2)
    for file_node in node.files:
        filename = file_node.path.name
        meta = f"# {file_node.line_count} lines, {file_node.word_count} words"

        refs = file_node.outgoing_refs
        if refs:
            lines.append(f"{file_prefix}{filename}: {meta}")
            for ref_path in sorted(refs):
                try:
                    rel_ref = str(ref_path.relative_to(root))
                except ValueError:
                    rel_ref = str(ref_path)
                lines.append(f"{ref_prefix}- {rel_ref}")
        else:
            lines.append(f"{file_prefix}{filename}: [] {meta}")

    # Render subfolders
    for child_name in sorted(node.children):
        _render_cross_refs_folder(
            node.children[child_name], indent + 1, lines, root
        )


# ---------------------------------------------------------------------------
# Public generators
# ---------------------------------------------------------------------------


def generate_sections_yaml(
    tree: DocTree, heading_depth: int = 2, max_sections: int = 20
) -> str:
    """Generate the sections YAML manifest.

    Args:
        tree: Analysed documentation tree.
        heading_depth: Maximum heading level to include (default 2 = ``#`` + ``##``).
        max_sections: Per-file threshold; files exceeding this fall back one level
                      (default 20).

    Returns:
        YAML content as a string (no library dependency — hand-formatted).
    """
    lines: List[str] = []

    # Header comment
    root_name = tree.root.name
    lines.append(
        f"# doc_sections  |  root: {root_name}  "
        f"|  {tree.total_files} files, {tree.total_sections} sections"
    )
    lines.append("")

    folder_tree = _build_collapsed_folders(tree)
    _render_sections_folder(folder_tree, 0, lines, heading_depth, max_sections)

    lines.append("")  # trailing newline
    return "\n".join(lines)


def generate_cross_refs_yaml(tree: DocTree) -> str:
    """Generate the cross-references YAML manifest.

    Args:
        tree: Analysed documentation tree.

    Returns:
        YAML content as a string.
    """
    lines: List[str] = []

    root_name = tree.root.name
    lines.append(
        f"# doc_cross_refs  |  root: {root_name}  "
        f"|  {tree.total_files} files, {tree.total_refs} references"
    )
    lines.append("")

    folder_tree = _build_collapsed_folders(tree)
    _render_cross_refs_folder(folder_tree, 0, lines, tree.root)

    lines.append("")
    return "\n".join(lines)
