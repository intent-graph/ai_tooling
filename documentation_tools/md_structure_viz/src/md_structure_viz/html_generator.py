"""Generate interactive HTML visualization from DocTree."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from .doc_tree import DocTree


class HTMLGenerator:
    """Generate standalone HTML visualization from documentation tree."""

    def __init__(self, tree: DocTree):
        """Initialize HTML generator.

        Args:
            tree: DocTree instance to visualize
        """
        self.tree = tree
        self.html_template = self._load_template()

    def generate(self, output_path: Path) -> None:
        """Generate HTML file.

        Args:
            output_path: Path to write HTML file
        """
        data = self._prepare_data()
        data_json = json.dumps(data, indent=2)
        html = self.html_template.replace(
            "// __TREE_DATA_PLACEHOLDER__",
            f"const treeData = {data_json};"
        )
        output_path.write_text(html, encoding="utf-8")

    def _prepare_data(self) -> Dict[str, Any]:
        """Convert DocTree to JSON-serializable format.

        Returns:
            Dictionary matching the treeData schema
        """
        nodes: List[Dict[str, Any]] = []
        node_id_map: Dict[str, str] = {}  # Path -> ID mapping

        # Build node list with IDs
        for i, (path, node) in enumerate(self.tree.nodes.items()):
            node_id = f"node_{i}"
            node_id_map[str(path)] = node_id

            try:
                rel_path = path.relative_to(self.tree.root)
            except ValueError:
                rel_path = path

            folder = str(rel_path.parent) if rel_path.parent != Path(".") else ""

            nodes.append({
                "id": node_id,
                "path": str(rel_path),
                "name": path.name,
                "title": node.title,
                "sections": node.section_count,
                "folder": folder,
                "depth": len(rel_path.parts) - 1,
                "incomingRefs": len(node.incoming_refs),
                "outgoingRefs": len(node.outgoing_refs)
            })

        # Build edges
        edges: List[Dict[str, Any]] = []
        for path, node in self.tree.nodes.items():
            source_id = node_id_map[str(path)]
            for target_path in node.outgoing_refs:
                target_id = node_id_map.get(str(target_path))
                if target_id:
                    edges.append({
                        "from": source_id,
                        "to": target_id,
                        "weight": 1
                    })

        # Build folder hierarchy - collect all folders including parent directories
        all_folder_paths: set = set()

        # Add root
        all_folder_paths.add(self.tree.root)

        # Collect all folders from tree.folders
        for path in self.tree.folders.keys():
            all_folder_paths.add(path)

            # Also add all parent folders up to root
            current = path
            while current != current.parent:
                current = current.parent
                if current != self.tree.root.parent:
                    all_folder_paths.add(current)

        # Build folder entries
        folders: List[Dict[str, Any]] = []

        for path in sorted(all_folder_paths):
            try:
                rel_path = path.relative_to(self.tree.root)
            except ValueError:
                # Skip if not under root
                continue

            path_str = str(rel_path) if str(rel_path) != "." else ""

            # Determine parent: root has no parent (null), others have their parent path
            if rel_path == Path("."):
                # Root folder has no parent
                parent_path: Any = None
            else:
                parent_path = str(rel_path.parent) if rel_path.parent != Path(".") else ""
                if parent_path == ".":
                    parent_path = ""

            files_in_folder = self.tree.folders.get(path, [])
            total_sections = sum(
                self.tree.nodes[f].section_count
                for f in files_in_folder
                if f in self.tree.nodes
            )

            # Find immediate subfolders (exclude self-references)
            children: List[str] = []
            for sub_path in all_folder_paths:
                try:
                    sub_rel = sub_path.relative_to(self.tree.root)
                    # Only add as child if parent matches and it's not self
                    if sub_rel.parent == rel_path and sub_rel != rel_path:
                        children.append(str(sub_rel))
                except ValueError:
                    pass

            folders.append({
                "path": path_str,
                "name": rel_path.name if rel_path.name else "root",
                "parent": parent_path,
                "children": sorted(children),
                "fileCount": len(files_in_folder),
                "totalSections": total_sections
            })

        return {
            "root": str(self.tree.root),
            "metadata": {
                "totalFiles": len(self.tree.nodes),
                "totalSections": self.tree.total_sections,
                "totalRefs": self.tree.total_refs,
                "maxDepth": max(len(p.relative_to(self.tree.root).parts)
                               for p in self.tree.nodes.keys()) if self.tree.nodes else 0,
                "generated": datetime.now().isoformat() + "Z"
            },
            "nodes": nodes,
            "edges": edges,
            "folders": folders
        }

    def _load_template(self) -> str:
        """Load HTML template from file.

        Returns:
            HTML template string with placeholder for data
        """
        template_path = Path(__file__).parent / "html_template.html"
        return template_path.read_text(encoding="utf-8")
