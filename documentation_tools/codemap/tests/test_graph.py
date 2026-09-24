"""Tests for the core graph data model."""

from codemap.graph import CodeEdge, CodeGraph, CodeNode, EdgeKind, NodeKind


def _make_sample_graph() -> CodeGraph:
    """Build a small graph exercising all node/edge types.

    Structure:
        pkg (package)
        ├── pkg.models (module)
        │   ├── pkg.models.User (class)
        │   │   ├── pkg.models.User.__init__ (method)
        │   │   └── pkg.models.User.validate (method)
        │   └── pkg.models.BaseModel (class)
        └── pkg.utils (module)
            └── pkg.utils.check_email (function)
    """
    nodes = {
        "pkg": CodeNode(
            qualified_name="pkg",
            name="pkg",
            kind=NodeKind.PACKAGE,
            path="pkg",
            line_start=1,
            line_end=1,
        ),
        "pkg.models": CodeNode(
            qualified_name="pkg.models",
            name="models",
            kind=NodeKind.MODULE,
            path="pkg/models.py",
            line_start=1,
            line_end=50,
            parent="pkg",
        ),
        "pkg.utils": CodeNode(
            qualified_name="pkg.utils",
            name="utils",
            kind=NodeKind.MODULE,
            path="pkg/utils.py",
            line_start=1,
            line_end=20,
            parent="pkg",
        ),
        "pkg.models.BaseModel": CodeNode(
            qualified_name="pkg.models.BaseModel",
            name="BaseModel",
            kind=NodeKind.CLASS,
            path="pkg/models.py",
            line_start=5,
            line_end=15,
            signature="class BaseModel",
            parent="pkg.models",
        ),
        "pkg.models.User": CodeNode(
            qualified_name="pkg.models.User",
            name="User",
            kind=NodeKind.CLASS,
            path="pkg/models.py",
            line_start=18,
            line_end=45,
            signature="class User(BaseModel)",
            parent="pkg.models",
        ),
        "pkg.models.User.__init__": CodeNode(
            qualified_name="pkg.models.User.__init__",
            name="__init__",
            kind=NodeKind.METHOD,
            path="pkg/models.py",
            line_start=19,
            line_end=25,
            signature="def __init__(self, name: str, email: str)",
            parent="pkg.models.User",
        ),
        "pkg.models.User.validate": CodeNode(
            qualified_name="pkg.models.User.validate",
            name="validate",
            kind=NodeKind.METHOD,
            path="pkg/models.py",
            line_start=27,
            line_end=40,
            signature="def validate(self) -> bool",
            docstring="Validate user data.",
            parent="pkg.models.User",
        ),
        "pkg.utils.check_email": CodeNode(
            qualified_name="pkg.utils.check_email",
            name="check_email",
            kind=NodeKind.FUNCTION,
            path="pkg/utils.py",
            line_start=5,
            line_end=15,
            signature="def check_email(email: str) -> bool",
            parent="pkg.utils",
        ),
    }

    edges = [
        # Containment
        CodeEdge("pkg", "pkg.models", EdgeKind.CONTAINS),
        CodeEdge("pkg", "pkg.utils", EdgeKind.CONTAINS),
        CodeEdge("pkg.models", "pkg.models.BaseModel", EdgeKind.CONTAINS),
        CodeEdge("pkg.models", "pkg.models.User", EdgeKind.CONTAINS),
        CodeEdge("pkg.models.User", "pkg.models.User.__init__", EdgeKind.CONTAINS),
        CodeEdge("pkg.models.User", "pkg.models.User.validate", EdgeKind.CONTAINS),
        CodeEdge("pkg.utils", "pkg.utils.check_email", EdgeKind.CONTAINS),
        # Inheritance
        CodeEdge("pkg.models.User", "pkg.models.BaseModel", EdgeKind.INHERITS),
        # Calls
        CodeEdge("pkg.models.User.validate", "pkg.utils.check_email", EdgeKind.CALLS),
        # Imports
        CodeEdge("pkg.models", "pkg.utils", EdgeKind.IMPORTS),
    ]

    return CodeGraph(root="pkg", nodes=nodes, edges=edges)


# -- Node & Edge construction ---------------------------------------------


class TestDataclasses:
    def test_node_is_frozen(self) -> None:
        node = CodeNode(
            qualified_name="a.b",
            name="b",
            kind=NodeKind.MODULE,
            path="a/b.py",
            line_start=1,
            line_end=10,
        )
        try:
            node.name = "c"  # type: ignore[misc]
            raise AssertionError("Should have raised FrozenInstanceError")
        except AttributeError:
            pass

    def test_edge_is_frozen(self) -> None:
        edge = CodeEdge("a", "b", EdgeKind.CALLS)
        try:
            edge.source = "c"  # type: ignore[misc]
            raise AssertionError("Should have raised FrozenInstanceError")
        except AttributeError:
            pass

    def test_node_optional_fields_default_none(self) -> None:
        node = CodeNode(
            qualified_name="a",
            name="a",
            kind=NodeKind.PACKAGE,
            path="a",
            line_start=1,
            line_end=1,
        )
        assert node.signature is None
        assert node.docstring is None
        assert node.parent is None


# -- Index construction ----------------------------------------------------


class TestIndexes:
    def test_children_index(self) -> None:
        g = _make_sample_graph()
        children = g.children_of("pkg")
        names = {c.qualified_name for c in children}
        assert names == {"pkg.models", "pkg.utils"}

    def test_children_of_leaf_is_empty(self) -> None:
        g = _make_sample_graph()
        assert g.children_of("pkg.utils.check_email") == []

    def test_edges_from(self) -> None:
        g = _make_sample_graph()
        edges = g.edges_from("pkg.models.User.validate")
        targets = {e.target for e in edges}
        assert "pkg.utils.check_email" in targets

    def test_edges_to(self) -> None:
        g = _make_sample_graph()
        edges = g.edges_to("pkg.utils.check_email")
        sources = {e.source for e in edges}
        assert "pkg.models.User.validate" in sources

    def test_edges_from_unknown_node_empty(self) -> None:
        g = _make_sample_graph()
        assert g.edges_from("nonexistent") == []


# -- Traversal methods -----------------------------------------------------


class TestTraversal:
    def test_ancestors_of_deep_node(self) -> None:
        g = _make_sample_graph()
        ancestors = g.ancestors_of("pkg.models.User.validate")
        names = [a.qualified_name for a in ancestors]
        assert names == ["pkg", "pkg.models", "pkg.models.User"]

    def test_ancestors_of_root_is_empty(self) -> None:
        g = _make_sample_graph()
        assert g.ancestors_of("pkg") == []

    def test_ancestors_of_unknown_node_empty(self) -> None:
        g = _make_sample_graph()
        assert g.ancestors_of("nonexistent") == []

    def test_top_level_nodes(self) -> None:
        g = _make_sample_graph()
        top = g.top_level_nodes()
        assert len(top) == 1
        assert top[0].qualified_name == "pkg"


# -- Rebuild indexes -------------------------------------------------------


class TestRebuild:
    def test_rebuild_after_mutation(self) -> None:
        """Adding a node and rebuilding produces correct indexes."""
        g = _make_sample_graph()
        new_node = CodeNode(
            qualified_name="pkg.utils.format_name",
            name="format_name",
            kind=NodeKind.FUNCTION,
            path="pkg/utils.py",
            line_start=17,
            line_end=20,
            signature="def format_name(name: str) -> str",
            parent="pkg.utils",
        )
        g.nodes[new_node.qualified_name] = new_node
        g.edges.append(
            CodeEdge("pkg.utils", "pkg.utils.format_name", EdgeKind.CONTAINS)
        )
        g.rebuild_indexes()

        children = g.children_of("pkg.utils")
        names = {c.qualified_name for c in children}
        assert "pkg.utils.format_name" in names
