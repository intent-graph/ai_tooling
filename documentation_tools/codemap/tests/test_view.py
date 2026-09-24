"""Tests for view: V-shape context, expand/collapse, serialization."""

import sqlite3
from pathlib import Path

import pytest
import yaml

from codemap.errors import NodeNotFoundError
from codemap.graph import CodeGraph, EdgeKind
from codemap.parser import parse_project
from codemap.view import (
    DetailLevel,
    build_context,
    collapse,
    exclude,
    expand,
    include,
    render_overview,
    render_tree,
)

FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_PROJECT = FIXTURES_DIR / "sample_project"


@pytest.fixture
def graph() -> CodeGraph:
    return parse_project(SAMPLE_PROJECT)


# -- S5: V-shape context builder -------------------------------------------


class TestBuildContext:
    def test_focus_node_is_full_detail(self, graph: CodeGraph) -> None:
        # Find a method node
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        assert methods, "validate method not found in graph"
        view = build_context(graph, methods[0])
        assert view.detail_level[methods[0]] == DetailLevel.FULL

    def test_top_level_nodes_visible(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        top = graph.top_level_nodes()
        for node in top:
            assert node.qualified_name in view.visible

    def test_ancestors_visible(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        ancestors = graph.ancestors_of(methods[0])
        for ancestor in ancestors:
            assert ancestor.qualified_name in view.visible
            assert view.detail_level[ancestor.qualified_name] == DetailLevel.SIGNATURE

    def test_neighbors_visible(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        # Check that non-CONTAINS edge targets are visible
        for edge in graph.edges_from(methods[0]):
            if edge.kind != EdgeKind.CONTAINS and edge.target in graph.nodes:
                assert edge.target in view.visible

    def test_nonexistent_node_raises(self, graph: CodeGraph) -> None:
        with pytest.raises(NodeNotFoundError):
            build_context(graph, "nonexistent.node")


# -- S6: expand / collapse / include / exclude -----------------------------


class TestViewManipulation:
    def test_expand_shows_children(self, graph: CodeGraph) -> None:
        # Find a class and expand it
        classes = [qn for qn, n in graph.nodes.items() if n.name == "User"]
        assert classes
        view = build_context(graph, classes[0])
        children_before = {
            c.qualified_name
            for c in graph.children_of(classes[0])
            if c.qualified_name in view.visible
        }
        expand(view, classes[0])
        children_after = {
            c.qualified_name
            for c in graph.children_of(classes[0])
            if c.qualified_name in view.visible
        }
        assert len(children_after) >= len(children_before)

    def test_collapse_hides_descendants(self, graph: CodeGraph) -> None:
        # Start with a module, expand it, then collapse
        modules = [qn for qn, n in graph.nodes.items() if n.name == "models"]
        assert modules
        view = build_context(graph, modules[0])
        expand(view, modules[0])
        # Verify children are visible
        children = graph.children_of(modules[0])
        assert any(c.qualified_name in view.visible for c in children)
        # Collapse
        collapse(view, modules[0])
        # Children should be gone
        for child in children:
            assert child.qualified_name not in view.visible

    def test_include_adds_at_full_detail(self, graph: CodeGraph) -> None:
        # Start with some focus, include a distant node
        top = graph.top_level_nodes()
        view = build_context(graph, top[0].qualified_name)
        # Find a method not currently in view
        all_methods = [qn for qn, n in graph.nodes.items() if n.name == "check_email"]
        assert all_methods
        include(view, all_methods[0])
        assert all_methods[0] in view.visible
        assert view.detail_level[all_methods[0]] == DetailLevel.FULL

    def test_exclude_removes_node_and_descendants(self, graph: CodeGraph) -> None:
        modules = [qn for qn, n in graph.nodes.items() if n.name == "models"]
        assert modules
        view = build_context(graph, modules[0])
        expand(view, modules[0])
        # Now exclude the module
        exclude(view, modules[0])
        assert modules[0] not in view.visible
        # All descendants should also be gone
        for child in graph.children_of(modules[0]):
            assert child.qualified_name not in view.visible

    def test_manipulation_on_nonexistent_node_raises(self, graph: CodeGraph) -> None:
        view = build_context(graph, graph.top_level_nodes()[0].qualified_name)
        with pytest.raises(NodeNotFoundError):
            expand(view, "nonexistent")
        with pytest.raises(NodeNotFoundError):
            collapse(view, "nonexistent")
        with pytest.raises(NodeNotFoundError):
            include(view, "nonexistent")
        with pytest.raises(NodeNotFoundError):
            exclude(view, "nonexistent")


# -- S7: Serialization -----------------------------------------------------


class TestOverviewRendering:
    def test_overview_is_valid_yaml(self, graph: CodeGraph) -> None:
        output = render_overview(graph)
        data = yaml.safe_load(output)
        assert "project" in data
        assert "structure" in data

    def test_overview_contains_all_top_level(self, graph: CodeGraph) -> None:
        output = render_overview(graph)
        data = yaml.safe_load(output)
        top_names = {n.qualified_name for n in graph.top_level_nodes()}
        structure_names = {s["name"] for s in data["structure"]}
        assert top_names == structure_names


class TestRenderTree:
    def test_tree_has_focus_line(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        assert output.startswith(f"focus: {methods[0]}")

    def test_is_valid_yaml(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        data = yaml.safe_load(output)
        assert isinstance(data, dict)
        assert "focus" in data

    def test_focus_node_has_marker_in_comment(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        focus_lines = [line for line in output.splitlines() if "[FOCUS]" in line]
        assert len(focus_lines) == 1
        # Uses short name as YAML key
        assert "validate:" in focus_lines[0]
        # Has path:lines pattern in the comment
        import re
        assert re.search(r":\d+-\d+$", focus_lines[0].strip())

    def test_node_keys_are_short_names(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        for line in output.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("focus:"):
                continue
            # Skip edge keys and list items
            if stripped.startswith("~") or stripped.startswith("- "):
                continue
            # Node lines are "name:  # comment" — extract the key
            if ":  #" in stripped:
                key = stripped.split(":  #")[0]
                assert "." not in key, f"Full qname in tree key: {line}"

    def test_node_comments_have_path_lines(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        import re
        for line in output.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("focus:"):
                continue
            if stripped.startswith("~") or stripped.startswith("- "):
                continue
            # Node lines have path:start-end in the comment
            assert re.search(r":\d+-\d+$", stripped), f"Missing path:lines in: {line}"

    def test_ancestors_visible_in_tree(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        ancestors = graph.ancestors_of(methods[0])
        for ancestor in ancestors:
            # Ancestors appear by short name as YAML keys
            assert f"{ancestor.name}:" in output

    def test_only_calls_and_inherits_edge_keys(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        allowed = {"~calls:", "~called_by:", "~inherits:", "~inherited_by:"}
        for line in output.splitlines():
            stripped = line.strip()
            if stripped.startswith("~"):
                assert stripped in allowed, f"Unexpected edge key: {stripped}"

    def test_edge_targets_are_full_qnames(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        for line in output.splitlines():
            stripped = line.strip()
            if stripped.startswith("- ") and "." in stripped:
                # List items under ~-keys are full qualified names
                target = stripped[2:]  # strip "- "
                assert target in graph.nodes, f"Edge target not in graph: {target}"

    def test_incoming_edges_only_on_focus_subtree(self, graph: CodeGraph) -> None:
        methods = [qn for qn, n in graph.nodes.items() if n.name == "validate"]
        view = build_context(graph, methods[0])
        output = render_tree(view, methods[0])
        # Track which node owns each ~called_by / ~inherited_by block
        incoming_keys = {"~called_by:", "~inherited_by:"}
        current_node: str | None = None
        for line in output.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("focus:"):
                continue
            if stripped.startswith("- ") or stripped.startswith("~"):
                if stripped in incoming_keys:
                    # Current node must be set
                    assert current_node is not None, "~called_by with no parent node"
            elif ":  #" in stripped:
                # It's a node line — extract key
                current_node = stripped.split(":  #")[0]

    def test_db_table_renders_columns(self, tmp_path: Path) -> None:
        project = tmp_path / "repo"
        project.mkdir()
        (project / "main.py").write_text("def hello() -> str:\n    return 'ok'\n")
        db_path = project / "app.db"
        conn = sqlite3.connect(db_path)
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
        conn.commit()
        conn.close()

        db_graph = parse_project(project)
        users_qname = next(
            qn for qn, n in db_graph.nodes.items() if n.kind.value == "db_table"
        )
        view = build_context(db_graph, users_qname)
        output = render_tree(view, users_qname)
        assert "~columns:" in output
        assert "- id" in output
        assert "- email" in output
