"""Core data model: nodes, edges, and the code graph.

The graph is immutable after construction. Indexes are derived from
primary data and rebuilt on init — never stored separately.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

# -- Enums -----------------------------------------------------------------


class NodeKind(Enum):
    """Classification of code units at any nesting level."""

    PACKAGE = "package"
    MODULE = "module"
    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"
    DATABASE = "database"
    DB_SCHEMA = "db_schema"
    DB_TABLE = "db_table"


class EdgeKind(Enum):
    """Structural and semantic relationships between code units."""

    CONTAINS = "contains"
    CALLS = "calls"
    IMPORTS = "imports"
    INHERITS = "inherits"


# -- Data: Nodes & Edges ---------------------------------------------------


@dataclass(frozen=True)
class CodeNode:
    """A unit of code at any hierarchical level.

    Identified by qualified_name (the primary key). Stores pointers
    to source (path + line range), not source code itself.
    """

    qualified_name: str
    name: str
    kind: NodeKind
    path: str
    line_start: int
    line_end: int
    signature: str | None = None
    docstring: str | None = None
    parent: str | None = None
    metadata: dict[str, Any] | None = None


@dataclass(frozen=True)
class CodeEdge:
    """A directed relationship between two code nodes.

    Identified by the (source, target, kind) triple — no artificial IDs.
    """

    source: str
    target: str
    kind: EdgeKind


# -- Graph -----------------------------------------------------------------


@dataclass
class CodeGraph:
    """The complete structural map of a codebase.

    Primary data: nodes dict + edges list.
    Derived indexes: children, edges_from, edges_to — rebuilt on construction.
    """

    root: str
    nodes: dict[str, CodeNode] = field(default_factory=dict)
    edges: list[CodeEdge] = field(default_factory=list)

    # Derived indexes (not part of __init__, built by rebuild_indexes)
    _children: dict[str, list[str]] = field(
        default_factory=lambda: defaultdict(list), init=False, repr=False
    )
    _edges_from: dict[str, list[CodeEdge]] = field(
        default_factory=lambda: defaultdict(list), init=False, repr=False
    )
    _edges_to: dict[str, list[CodeEdge]] = field(
        default_factory=lambda: defaultdict(list), init=False, repr=False
    )

    def __post_init__(self) -> None:
        self.rebuild_indexes()

    def rebuild_indexes(self) -> None:
        """Derive children and edge indexes from primary data."""
        self._children = defaultdict(list)
        self._edges_from = defaultdict(list)
        self._edges_to = defaultdict(list)

        for node in self.nodes.values():
            if node.parent is not None:
                self._children[node.parent].append(node.qualified_name)

        for edge in self.edges:
            self._edges_from[edge.source].append(edge)
            self._edges_to[edge.target].append(edge)

    # -- Query methods -----------------------------------------------------

    def children_of(self, qualified_name: str) -> list[CodeNode]:
        """Direct children of a node in the containment hierarchy."""
        return [self.nodes[qn] for qn in self._children.get(qualified_name, [])]

    def edges_from(self, qualified_name: str) -> list[CodeEdge]:
        """All outgoing edges from a node."""
        return self._edges_from.get(qualified_name, [])

    def edges_to(self, qualified_name: str) -> list[CodeEdge]:
        """All incoming edges to a node."""
        return self._edges_to.get(qualified_name, [])

    def ancestors_of(self, qualified_name: str) -> list[CodeNode]:
        """Lineage from root to the node's parent (inclusive), top-down."""
        ancestors: list[CodeNode] = []
        current = self.nodes.get(qualified_name)
        if current is None:
            return ancestors
        while current.parent is not None:
            parent = self.nodes.get(current.parent)
            if parent is None:
                break
            ancestors.append(parent)
            current = parent
        ancestors.reverse()
        return ancestors

    def top_level_nodes(self) -> list[CodeNode]:
        """All nodes with no parent — the root-level modules/packages."""
        return [n for n in self.nodes.values() if n.parent is None]
