"""Public API: the 11 methods agents call.

Thin orchestration over graph, parser, view, and export. This is
the only module agents import directly.
"""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

from codemap.errors import CodeMapError, NodeNotFoundError
from codemap.export_yed import export_graphml
from codemap.graph import CodeGraph, CodeNode
from codemap.parser import parse_project
from codemap.view import (
    ViewState,
    build_context,
    render_overview,
    render_tree,
)
from codemap.view import (
    collapse as _collapse,
)
from codemap.view import (
    exclude as _exclude,
)
from codemap.view import (
    expand as _expand,
)
from codemap.view import (
    include as _include,
)


class CodeMap:
    """Agent-facing interface to a parsed codebase.

    Usage:
        cm = CodeMap.build("path/to/project")
        print(cm.overview())
        print(cm.context("pkg.module.Class.method"))
    """

    def __init__(self, graph: CodeGraph, project_root: Path) -> None:
        self._graph = graph
        self._project_root = project_root
        self._view: ViewState | None = None

    # -- Build -------------------------------------------------------------

    @staticmethod
    def build(
        path: str | Path,
        *,
        include_sqlite: bool = True,
    ) -> CodeMap:
        """Parse a Python project into a navigable code map."""
        root = Path(path).resolve()
        graph = parse_project(path, include_sqlite=include_sqlite)
        return CodeMap(graph, root)

    # -- Orient & Locate ---------------------------------------------------

    def overview(self) -> str:
        """Full project skeleton — names and nesting only. Returns YAML."""
        return render_overview(self._graph)

    def search(self, query: str) -> list[dict[str, Any]]:
        """Find nodes by name pattern. Case-insensitive substring match."""
        query_lower = query.lower()
        results: list[dict[str, Any]] = []
        for node in self._graph.nodes.values():
            if (
                query_lower in node.name.lower()
                or query_lower in node.qualified_name.lower()
            ):
                results.append(
                    {
                        "name": node.name,
                        "qualified_name": node.qualified_name,
                        "kind": node.kind.value,
                        "path": node.path,
                    }
                )
        return results

    # -- Focus & Navigate --------------------------------------------------

    def context(self, qualified_name: str) -> str:
        """V-shaped context for a focus node.

        Returns an indented node tree + edge list. Also sets the internal
        view state for subsequent expand/collapse/include/exclude calls.
        """
        self._view = build_context(self._graph, qualified_name)
        return render_tree(self._view, qualified_name)

    def neighbors(
        self, qualified_name: str, edge_type: str | None = None
    ) -> list[dict[str, Any]]:
        """Immediate connections of a node, optionally filtered by edge type."""
        if qualified_name not in self._graph.nodes:
            msg = f"Node not found: {qualified_name!r}"
            raise NodeNotFoundError(msg)

        results: list[dict[str, Any]] = []

        for edge in self._graph.edges_from(qualified_name):
            if edge_type is not None and edge.kind.value != edge_type:
                continue
            if edge.target in self._graph.nodes:
                target = self._graph.nodes[edge.target]
                results.append(
                    {
                        "name": target.name,
                        "qualified_name": target.qualified_name,
                        "kind": target.kind.value,
                        "edge": edge.kind.value,
                        "direction": "outgoing",
                    }
                )

        for edge in self._graph.edges_to(qualified_name):
            if edge_type is not None and edge.kind.value != edge_type:
                continue
            if edge.source in self._graph.nodes:
                source = self._graph.nodes[edge.source]
                results.append(
                    {
                        "name": source.name,
                        "qualified_name": source.qualified_name,
                        "kind": source.kind.value,
                        "edge": edge.kind.value,
                        "direction": "incoming",
                    }
                )

        return results

    # -- Adjust Detail -----------------------------------------------------

    def expand(self, qualified_name: str) -> str:
        """Show children of a collapsed node. Returns updated view."""
        view = self._require_view()
        _expand(view, qualified_name)
        return render_tree(view, self._focus_qname(view))

    def collapse(self, qualified_name: str) -> str:
        """Hide descendants of a node. Returns updated view."""
        view = self._require_view()
        _collapse(view, qualified_name)
        return render_tree(view, self._focus_qname(view))

    def include(self, qualified_name: str) -> str:
        """Add a node at full detail. Returns updated view."""
        view = self._require_view()
        _include(view, qualified_name)
        return render_tree(view, self._focus_qname(view))

    def exclude(self, qualified_name: str) -> str:
        """Remove a node and descendants from view. Returns updated view."""
        view = self._require_view()
        _exclude(view, qualified_name)
        return render_tree(view, self._focus_qname(view))

    # -- Read Source --------------------------------------------------------

    def source(self, qualified_name: str) -> str:
        """Retrieve the actual source code lines for a node."""
        if qualified_name not in self._graph.nodes:
            msg = f"Node not found: {qualified_name!r}"
            raise NodeNotFoundError(msg)

        node = self._graph.nodes[qualified_name]
        file_path = self._resolve_path(node)

        try:
            all_lines = file_path.read_text(encoding="utf-8").splitlines()
        except OSError as e:
            msg = f"Cannot read source file {file_path}: {e}"
            raise CodeMapError(msg) from e

        # line_start and line_end are 1-indexed
        selected = all_lines[node.line_start - 1 : node.line_end]
        return "\n".join(selected)

    # -- Export ------------------------------------------------------------

    def export_yed(
        self,
        output_path: str | Path | None = None,
        *,
        flat: bool = False,
    ) -> Path:
        """Export the graph to yEd-compatible GraphML.

        If output_path is not given, writes to
        {tempfile.gettempdir()}/codemap__{project_name}.graphml.

        Set flat=True to emit all nodes at the top level (no nested groups).
        This works better with most yEd layout algorithms.

        Open the result in yEd, then:
          Layout > Hierarchical  (auto-arrange)
          Tools  > Fit Node to Label  (auto-size)
        """
        if output_path is None:
            output_path = (
                Path(tempfile.gettempdir()) / f"codemap__{self._project_root.name}.graphml"
            )
        return export_graphml(self._graph, output_path, flat=flat)

    # -- Internal helpers --------------------------------------------------

    def _require_view(self) -> ViewState:
        """Ensure a view exists (context() must be called first)."""
        if self._view is None:
            msg = "Call context() before expand/collapse/include/exclude"
            raise CodeMapError(msg)
        return self._view

    def _focus_qname(self, view: ViewState) -> str:
        """Find the current focus node (the one at FULL detail)."""
        from codemap.view import DetailLevel

        for qn, level in view.detail_level.items():
            if level == DetailLevel.FULL:
                return qn
        # Fallback: first visible node
        return next(iter(view.visible))

    def _resolve_path(self, node: CodeNode) -> Path:
        """Resolve a node's relative path to an absolute file path."""
        resolved = self._project_root / node.path
        if resolved.exists():
            return resolved
        msg = f"Cannot resolve source path: {node.path} (tried {resolved})"
        raise CodeMapError(msg)

    @property
    def graph(self) -> CodeGraph:
        """Access the underlying graph (for advanced use)."""
        return self._graph
