"""Mermaid diagram generation for documentation trees."""

from pathlib import Path
from typing import Dict, List, Set

from .doc_tree import DocNode, DocTree


def sanitize_id(path: Path, root: Path) -> str:
    """Convert file path to valid Mermaid ID."""
    try:
        rel_path = path.relative_to(root)
    except ValueError:
        rel_path = path

    # Create ID: replace path separators and special chars
    id_str = str(rel_path).replace("/", "_").replace(".", "_").replace("-", "_")
    # Ensure starts with letter
    if id_str[0].isdigit():
        id_str = f"f_{id_str}"
    return id_str


def escape_label(text: str) -> str:
    """Escape special characters for Mermaid labels."""
    # Remove quotes and angle brackets
    text = text.replace('"', "'").replace("<", "[").replace(">", "]")
    return text


def generate_tree_graph(tree: DocTree) -> str:
    """Generate tree-based Mermaid diagram with folder hierarchy and cross-refs."""
    lines = ["graph TB"]
    lines.append("")

    # Phase 1: Create nodes for folders and files
    created_folders: Set[Path] = set()
    node_id_map: Dict[Path, str] = {}

    # Sort to ensure consistent ordering
    sorted_files = sorted(tree.nodes.values(), key=lambda n: n.path)

    # Create folder nodes
    for node in sorted_files:
        folder = node.path.parent
        if folder not in created_folders and folder != tree.root:
            folder_id = sanitize_id(folder, tree.root)
            folder_name = folder.name
            lines.append(f'    {folder_id}["{folder_name}/"]')
            created_folders.add(folder)

    lines.append("")

    # Create file nodes
    for node in sorted_files:
        node_id = sanitize_id(node.path, tree.root)
        node_id_map[node.path] = node_id

        # Create label with title and section count
        filename = node.path.name
        label = f"{filename}<br/>{node.section_count} sections"
        label = escape_label(label)

        lines.append(f'    {node_id}["{label}"]')

    lines.append("")

    # Phase 2: Create folder hierarchy edges (solid lines)
    root_id = sanitize_id(tree.root, tree.root)
    lines.append(f'    ROOT["{tree.root.name}/"]')

    for folder in created_folders:
        folder_id = sanitize_id(folder, tree.root)
        parent_folder = folder.parent

        if parent_folder == tree.root:
            lines.append(f"    ROOT --> {folder_id}")
        else:
            parent_id = sanitize_id(parent_folder, tree.root)
            lines.append(f"    {parent_id} --> {folder_id}")

    # Connect files to folders
    for node in sorted_files:
        folder = node.path.parent
        node_id = node_id_map[node.path]

        if folder == tree.root:
            lines.append(f"    ROOT --> {node_id}")
        else:
            folder_id = sanitize_id(folder, tree.root)
            lines.append(f"    {folder_id} --> {node_id}")

    lines.append("")

    # Phase 3: Create cross-reference edges (dotted lines)
    ref_count = 0
    for node in sorted_files:
        if not node.outgoing_refs:
            continue

        source_id = node_id_map[node.path]

        for target_path in node.outgoing_refs:
            if target_path in node_id_map:
                target_id = node_id_map[target_path]
                lines.append(f"    {source_id} -.->|refs| {target_id}")
                ref_count += 1

    if ref_count > 0:
        lines.append("")

    # Phase 4: Apply styling
    lines.append("    classDef folder fill:#f9f,stroke:#333,stroke-width:2px")
    lines.append("    classDef file fill:#bbf,stroke:#333,stroke-width:1px")

    # Mark folders
    folder_list = " ".join([sanitize_id(f, tree.root) for f in created_folders])
    if folder_list:
        lines.append(f"    class ROOT,{folder_list} folder")

    # Mark files
    file_list = " ".join(node_id_map.values())
    if file_list:
        lines.append(f"    class {file_list} file")

    return "\n".join(lines)


def generate_simple_flowchart(tree: DocTree) -> str:
    """Generate simple flowchart showing only cross-references."""
    lines = ["graph TD"]
    lines.append("")

    node_id_map: Dict[Path, str] = {}
    sorted_files = sorted(tree.nodes.values(), key=lambda n: n.path)

    # Create nodes
    for node in sorted_files:
        node_id = sanitize_id(node.path, tree.root)
        node_id_map[node.path] = node_id

        filename = node.path.name
        label = f"{filename}<br/>{node.section_count} sections"
        label = escape_label(label)

        lines.append(f'    {node_id}["{label}"]')

    lines.append("")

    # Create reference edges
    for node in sorted_files:
        if not node.outgoing_refs:
            continue

        source_id = node_id_map[node.path]

        for target_path in node.outgoing_refs:
            if target_path in node_id_map:
                target_id = node_id_map[target_path]
                lines.append(f"    {source_id} --> {target_id}")

    return "\n".join(lines)


def generate_stats(tree: DocTree) -> str:
    """Generate statistics about the documentation tree."""
    lines = []
    lines.append(f"**Documentation Statistics**")
    lines.append("")
    lines.append(f"- Root: {tree.root}")
    lines.append(f"- Total files: {tree.total_files}")
    lines.append(f"- Total sections: {tree.total_sections}")
    lines.append(f"- Total cross-references: {tree.total_refs}")
    lines.append(f"- Average sections per file: {tree.total_sections / tree.total_files:.1f}")

    return "\n".join(lines)
