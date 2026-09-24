"""View state: V-shaped context, expand/collapse, serialization.

The graph is fact (what the code is). The view is perspective (what the
agent sees right now). Agents can create multiple views on the same graph.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import yaml

from codemap.errors import NodeNotFoundError
from codemap.graph import CodeGraph, CodeNode, EdgeKind


class DetailLevel(Enum):
    """How much detail to show for a node in the view."""

    NAMES_ONLY = "names_only"
    SIGNATURE = "signature"
    FULL = "full"


@dataclass
class ViewState:
    """A mutable selection on top of an immutable graph.

    Tracks which nodes are visible and at what detail level.
    """

    graph: CodeGraph
    visible: set[str] = field(default_factory=set)
    detail_level: dict[str, DetailLevel] = field(default_factory=dict)


# -- V-shape context builder -----------------------------------------------


def build_context(graph: CodeGraph, focus_qname: str) -> ViewState:
    """Build a V-shaped context view centered on a focus node.

    Three axes:
      - Wide brim: all top-level nodes (names only)
      - Vertical spine: ancestors from root to focus (signatures)
      - Ground bar: focus node (full) + immediate neighbors (signatures)
    """
    if focus_qname not in graph.nodes:
        msg = f"Node not found: {focus_qname!r}"
        raise NodeNotFoundError(msg)

    view = ViewState(graph=graph)

    # Wide brim: top-level nodes + their direct children.
    # When a single root package exists, its children are the real
    # orientation layer (the subpackages/modules the developer knows).
    for node in graph.top_level_nodes():
        view.visible.add(node.qualified_name)
        view.detail_level[node.qualified_name] = DetailLevel.NAMES_ONLY
        for child in graph.children_of(node.qualified_name):
            view.visible.add(child.qualified_name)
            if child.qualified_name not in view.detail_level:
                view.detail_level[child.qualified_name] = DetailLevel.NAMES_ONLY

    # Vertical spine: ancestors of the focus node
    for ancestor in graph.ancestors_of(focus_qname):
        view.visible.add(ancestor.qualified_name)
        view.detail_level[ancestor.qualified_name] = DetailLevel.SIGNATURE

    # Ground bar: focus node at full detail
    view.visible.add(focus_qname)
    view.detail_level[focus_qname] = DetailLevel.FULL

    # Ground bar: immediate neighbors at signature level
    for edge in graph.edges_from(focus_qname):
        if edge.kind != EdgeKind.CONTAINS and edge.target in graph.nodes:
            view.visible.add(edge.target)
            # Don't downgrade if already at higher detail
            if edge.target not in view.detail_level:
                view.detail_level[edge.target] = DetailLevel.SIGNATURE

    for edge in graph.edges_to(focus_qname):
        if edge.kind != EdgeKind.CONTAINS and edge.source in graph.nodes:
            view.visible.add(edge.source)
            if edge.source not in view.detail_level:
                view.detail_level[edge.source] = DetailLevel.SIGNATURE

    return view


# -- View manipulation -----------------------------------------------------


def expand(view: ViewState, qname: str) -> None:
    """Show children of a node, each at NAMES_ONLY detail."""
    if qname not in view.graph.nodes:
        msg = f"Node not found: {qname!r}"
        raise NodeNotFoundError(msg)

    for child in view.graph.children_of(qname):
        view.visible.add(child.qualified_name)
        if child.qualified_name not in view.detail_level:
            view.detail_level[child.qualified_name] = DetailLevel.NAMES_ONLY


def collapse(view: ViewState, qname: str) -> None:
    """Hide all descendants of a node. The node itself stays visible.

    Protects the current focus node (FULL detail) from removal — collapsing
    an ancestor of the focus doesn't lose orientation.
    """
    if qname not in view.graph.nodes:
        msg = f"Node not found: {qname!r}"
        raise NodeNotFoundError(msg)

    descendants = _collect_descendants(view.graph, qname)
    for desc in descendants:
        if view.detail_level.get(desc) == DetailLevel.FULL:
            continue  # never collapse the focus node
        view.visible.discard(desc)
        view.detail_level.pop(desc, None)


def include(view: ViewState, qname: str) -> None:
    """Add a node to the view at FULL detail."""
    if qname not in view.graph.nodes:
        msg = f"Node not found: {qname!r}"
        raise NodeNotFoundError(msg)

    view.visible.add(qname)
    view.detail_level[qname] = DetailLevel.FULL


def exclude(view: ViewState, qname: str) -> None:
    """Remove a node and all its descendants from the view."""
    if qname not in view.graph.nodes:
        msg = f"Node not found: {qname!r}"
        raise NodeNotFoundError(msg)

    to_remove = {qname} | _collect_descendants(view.graph, qname)
    for name in to_remove:
        view.visible.discard(name)
        view.detail_level.pop(name, None)


# -- YAML serialization ----------------------------------------------------


def render_overview(graph: CodeGraph) -> str:
    """Render the full project skeleton: names and nesting only."""
    top_nodes = graph.top_level_nodes()

    def _build_tree(node: CodeNode) -> dict[str, Any]:
        children = graph.children_of(node.qualified_name)
        entry: dict[str, Any] = {"name": node.qualified_name, "kind": node.kind.value}
        if children:
            entry["children"] = [_build_tree(c) for c in children]
        return entry

    structure = [_build_tree(n) for n in top_nodes]
    data = {"project": graph.root, "structure": structure}
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def render_context(view: ViewState, focus_qname: str) -> str:
    """Render a V-shaped context view as YAML.

    Output format matches the contract defined in IMPLEMENTATION_PLAN.md.
    """
    graph = view.graph
    focus_node = graph.nodes[focus_qname]

    # Wide brim: top-level nodes + their direct children
    brim_qnames: list[str] = []
    for n in graph.top_level_nodes():
        if n.qualified_name in view.visible:
            brim_qnames.append(n.qualified_name)
        for child in graph.children_of(n.qualified_name):
            if child.qualified_name in view.visible:
                brim_qnames.append(child.qualified_name)
    top_level = brim_qnames

    # Vertical spine: ancestors
    lineage = []
    for ancestor in graph.ancestors_of(focus_qname):
        if ancestor.qualified_name in view.visible:
            lineage.append(_render_node(ancestor, view))

    # Focus node: full detail
    focus_rendered = _render_node(focus_node, view)

    # Neighbors: grouped by edge kind.
    # For container nodes (packages/modules), also scan edges of descendants
    # since those carry the real cross-cutting relationships.
    neighbors: dict[str, list[dict[str, Any]]] = {
        "calls": [],
        "imports": [],
        "inherits": [],
        "called_by": [],
    }

    frontier = {focus_qname} | _collect_descendants(graph, focus_qname)
    seen_outgoing: set[str] = set()
    seen_incoming: set[str] = set()

    for source_qname in frontier:
        for edge in graph.edges_from(source_qname):
            if edge.kind == EdgeKind.CONTAINS:
                continue
            if edge.target in frontier:
                continue  # internal edge within the focus subtree
            if edge.target in graph.nodes and edge.target in view.visible:
                if edge.target not in seen_outgoing:
                    seen_outgoing.add(edge.target)
                    target_node = graph.nodes[edge.target]
                    entry = _render_node(target_node, view)
                    neighbors[edge.kind.value].append(entry)

        for edge in graph.edges_to(source_qname):
            if edge.kind == EdgeKind.CONTAINS:
                continue
            if edge.source in frontier:
                continue  # internal edge within the focus subtree
            if edge.source in graph.nodes and edge.source in view.visible:
                if edge.source not in seen_incoming:
                    seen_incoming.add(edge.source)
                    source_node = graph.nodes[edge.source]
                    entry = _render_node(source_node, view)
                    neighbors["called_by"].append(entry)

    # Remove empty neighbor groups
    neighbors = {k: v for k, v in neighbors.items() if v}

    data: dict[str, Any] = {
        "focus": focus_qname,
        "top_level": top_level,
        "lineage": lineage,
        "focus_node": focus_rendered,
    }
    if neighbors:
        data["neighbors"] = neighbors

    return yaml.dump(data, default_flow_style=False, sort_keys=False)


# -- Tree serialization (agent-facing) ------------------------------------

# Reserved YAML keys for edge relations (prefixed with ~ to avoid
# collision with any valid Python identifier — ~ cannot start a
# Python name but is a legal YAML plain scalar start character).
_EDGE_KEYS = frozenset(
    {"~calls", "~called_by", "~inherits", "~inherited_by", "~columns"}
)

# Mapping from EdgeKind to the outgoing and incoming YAML key names.
_OUTGOING_KEY = {EdgeKind.CALLS: "~calls", EdgeKind.INHERITS: "~inherits"}
_INCOMING_KEY = {EdgeKind.CALLS: "~called_by", EdgeKind.INHERITS: "~inherited_by"}


def render_tree(view: ViewState, focus_qname: str) -> str:
    """Render a valid-YAML tree with ~-prefixed edge keys.

    Format:
      - Containment = YAML nesting (node names are mapping keys)
      - Node metadata = YAML comment after the key
      - Edges = ~calls, ~called_by, ~inherits, ~inherited_by keys
        with list values (full qualified names, copy-pasteable)
      - [FOCUS] marker in the comment of the focus node

    Only 'calls' and 'inherits' edges are shown (no imports/contains).
    DB table nodes can also carry a '~columns' list from metadata.
    Incoming edges (~called_by/~inherited_by) only on focus subtree.
    """
    graph = view.graph
    lines: list[str] = []

    lines.append(f"focus: {focus_qname}")
    lines.append("")

    # Pre-compute the focus subtree: focus node + all its descendants.
    # Only nodes in this set get incoming (~called_by/~inherited_by) edges.
    focus_subtree = {focus_qname} | _collect_descendants(graph, focus_qname)

    # Edge kinds to render (skip contains and imports)
    _RENDER_KINDS = {EdgeKind.CALLS, EdgeKind.INHERITS}

    # Build the visible tree: find roots (visible nodes whose parent
    # is either None or not visible)
    visible_roots = sorted(
        (qn for qn in view.visible
         if qn in graph.nodes
         and (graph.nodes[qn].parent is None
              or graph.nodes[qn].parent not in view.visible)),
        key=str,
    )

    def _render_subtree(qname: str, depth: int) -> None:
        node = graph.nodes[qname]
        level = view.detail_level.get(qname, DetailLevel.NAMES_ONLY)
        indent = "  " * depth

        # Comment parts: [FOCUS]?  kind  sig?  "doc"?  path:start-end
        comment_parts: list[str] = []

        if qname == focus_qname:
            comment_parts.append("[FOCUS]")

        comment_parts.append(node.kind.value)

        if level in (DetailLevel.SIGNATURE, DetailLevel.FULL):
            if node.signature is not None:
                comment_parts.append(node.signature)

        if level == DetailLevel.FULL:
            if node.docstring is not None:
                comment_parts.append(f'"{node.docstring}"')

        comment_parts.append(f"{node.path}:{node.line_start}-{node.line_end}")

        comment = "  ".join(comment_parts)
        lines.append(f"{indent}{node.name}:  # {comment}")

        # 1. Recurse into visible children (containment first)
        visible_children = sorted(
            (c.qualified_name for c in graph.children_of(qname)
             if c.qualified_name in view.visible),
            key=str,
        )
        for child_qn in visible_children:
            _render_subtree(child_qn, depth + 1)

        # 2. Collect edges grouped by ~-key
        child_indent = "  " * (depth + 1)
        edge_groups: dict[str, list[str]] = defaultdict(list)
        seen: set[tuple[str, str, str]] = set()

        # Outgoing edges (all visible nodes)
        for edge in graph.edges_from(qname):
            if edge.kind not in _RENDER_KINDS:
                continue
            if edge.target not in view.visible:
                continue
            key = (edge.source, edge.target, edge.kind.value)
            if key in seen:
                continue
            seen.add(key)
            yaml_key = _OUTGOING_KEY[edge.kind]
            edge_groups[yaml_key].append(edge.target)

        # Incoming edges (focus subtree only)
        if qname in focus_subtree:
            for edge in graph.edges_to(qname):
                if edge.kind not in _RENDER_KINDS:
                    continue
                if edge.source not in view.visible:
                    continue
                key = (edge.source, edge.target, edge.kind.value)
                if key in seen:
                    continue
                seen.add(key)
                yaml_key = _INCOMING_KEY[edge.kind]
                edge_groups[yaml_key].append(edge.source)

        # Render edge groups (sorted keys, sorted targets)
        for yaml_key in sorted(edge_groups):
            lines.append(f"{child_indent}{yaml_key}:")
            for target in sorted(edge_groups[yaml_key]):
                lines.append(f"{child_indent}  - {target}")

        # 3. Render db table columns if present.
        if node.kind.value == "db_table" and node.metadata is not None:
            raw_columns = node.metadata.get("columns")
            if isinstance(raw_columns, list) and raw_columns:
                lines.append(f"{child_indent}~columns:")
                for column in raw_columns:
                    lines.append(f"{child_indent}  - {column}")

    for root_qn in visible_roots:
        _render_subtree(root_qn, 0)

    lines.append("")
    return "\n".join(lines)


# -- Internal helpers ------------------------------------------------------


def _render_node(node: CodeNode, view: ViewState) -> dict[str, Any]:
    """Render a node according to its detail level in the view."""
    level = view.detail_level.get(node.qualified_name, DetailLevel.NAMES_ONLY)

    if level == DetailLevel.NAMES_ONLY:
        return {"name": node.name, "qualified_name": node.qualified_name}

    result: dict[str, Any] = {
        "name": node.name,
        "qualified_name": node.qualified_name,
        "kind": node.kind.value,
    }

    if level in (DetailLevel.SIGNATURE, DetailLevel.FULL):
        if node.signature is not None:
            result["signature"] = node.signature

    if level == DetailLevel.FULL:
        if node.docstring is not None:
            result["docstring"] = node.docstring
        result["path"] = node.path
        result["lines"] = [node.line_start, node.line_end]

    return result


def _collect_descendants(graph: CodeGraph, qname: str) -> set[str]:
    """Recursively collect all descendants of a node."""
    descendants: set[str] = set()
    stack = [c.qualified_name for c in graph.children_of(qname)]
    while stack:
        current = stack.pop()
        descendants.add(current)
        stack.extend(c.qualified_name for c in graph.children_of(current))
    return descendants
