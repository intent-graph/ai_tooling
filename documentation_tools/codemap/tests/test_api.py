"""Integration tests for the public API."""

import sqlite3
from pathlib import Path

import pytest
import yaml

from codemap.api import CodeMap
from codemap.errors import CodeMapError, NodeNotFoundError

FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_PROJECT = FIXTURES_DIR / "sample_project"


@pytest.fixture
def cm() -> CodeMap:
    return CodeMap.build(SAMPLE_PROJECT)


# -- Build -----------------------------------------------------------------


class TestBuild:
    def test_build_returns_codemap(self) -> None:
        cm = CodeMap.build(SAMPLE_PROJECT)
        assert isinstance(cm, CodeMap)

    def test_build_nonexistent_raises(self) -> None:
        with pytest.raises(CodeMapError):
            CodeMap.build("/nonexistent")

    def test_build_can_disable_sqlite_introspection(self, tmp_path: Path) -> None:
        project = tmp_path / "repo"
        project.mkdir()
        (project / "main.py").write_text("def hello() -> str:\n    return 'ok'\n")
        db_path = project / "app.db"
        conn = sqlite3.connect(db_path)
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
        conn.commit()
        conn.close()

        cm = CodeMap.build(project, include_sqlite=False)
        results = cm.search("app.db")
        assert results == []


# -- Overview --------------------------------------------------------------


class TestOverview:
    def test_overview_is_yaml(self, cm: CodeMap) -> None:
        output = cm.overview()
        data = yaml.safe_load(output)
        assert "project" in data
        assert "structure" in data

    def test_overview_contains_project_name(self, cm: CodeMap) -> None:
        output = cm.overview()
        data = yaml.safe_load(output)
        assert data["project"] == "sample_project"


# -- Search ----------------------------------------------------------------


class TestSearch:
    def test_search_by_name(self, cm: CodeMap) -> None:
        results = cm.search("User")
        assert len(results) >= 1
        assert any(r["name"] == "User" for r in results)

    def test_search_case_insensitive(self, cm: CodeMap) -> None:
        results = cm.search("user")
        assert any(r["name"] == "User" for r in results)

    def test_search_no_results(self, cm: CodeMap) -> None:
        results = cm.search("zzz_nonexistent_zzz")
        assert results == []

    def test_search_by_qualified_name(self, cm: CodeMap) -> None:
        results = cm.search("models.User")
        assert len(results) >= 1


# -- Context ---------------------------------------------------------------


class TestContext:
    def test_context_returns_tree(self, cm: CodeMap) -> None:
        results = cm.search("validate")
        validate_qn = [r for r in results if r["kind"] == "method"][0]["qualified_name"]
        output = cm.context(validate_qn)
        assert output.startswith(f"focus: {validate_qn}")
        assert "[FOCUS]" in output

    def test_context_nonexistent_raises(self, cm: CodeMap) -> None:
        with pytest.raises(NodeNotFoundError):
            cm.context("nonexistent.node")


# -- Neighbors -------------------------------------------------------------


class TestNeighbors:
    def test_neighbors_returns_list(self, cm: CodeMap) -> None:
        results = cm.search("User")
        user_qn = [r for r in results if r["kind"] == "class"][0]["qualified_name"]
        neighbors = cm.neighbors(user_qn)
        assert isinstance(neighbors, list)
        assert len(neighbors) >= 1

    def test_neighbors_filtered_by_edge_type(self, cm: CodeMap) -> None:
        results = cm.search("User")
        user_qn = [r for r in results if r["kind"] == "class"][0]["qualified_name"]
        inherits = cm.neighbors(user_qn, edge_type="inherits")
        for n in inherits:
            assert n["edge"] == "inherits"

    def test_neighbors_nonexistent_raises(self, cm: CodeMap) -> None:
        with pytest.raises(NodeNotFoundError):
            cm.neighbors("nonexistent.node")


# -- Expand / Collapse / Include / Exclude ---------------------------------


class TestViewManipulation:
    def test_expand_after_context(self, cm: CodeMap) -> None:
        results = cm.search("models")
        module_qn = [r for r in results if r["kind"] == "module"][0]["qualified_name"]
        cm.context(module_qn)
        output = cm.expand(module_qn)
        assert "[FOCUS]" in output

    def test_collapse_after_expand(self, cm: CodeMap) -> None:
        results = cm.search("models")
        module_qn = [r for r in results if r["kind"] == "module"][0]["qualified_name"]
        cm.context(module_qn)
        cm.expand(module_qn)
        output = cm.collapse(module_qn)
        assert "[FOCUS]" in output

    def test_include_distant_node(self, cm: CodeMap) -> None:
        results = cm.search("models")
        module_qn = [r for r in results if r["kind"] == "module"][0]["qualified_name"]
        cm.context(module_qn)

        check_results = cm.search("check_email")
        check_qn = check_results[0]["qualified_name"]
        output = cm.include(check_qn)
        # Short name should appear in tree
        assert "check_email" in output

    def test_exclude_node(self, cm: CodeMap) -> None:
        results = cm.search("models")
        module_qn = [r for r in results if r["kind"] == "module"][0]["qualified_name"]
        cm.context(module_qn)
        output = cm.exclude(module_qn)
        # Short name "models" should not appear as a YAML node key
        node_keys = [
            line.strip().split(":  #")[0]
            for line in output.splitlines()
            if line.strip() and ":  #" in line
        ]
        assert "models" not in node_keys

    def test_expand_without_context_raises(self, cm: CodeMap) -> None:
        with pytest.raises(CodeMapError, match="Call context"):
            cm.expand("anything")


# -- Source ----------------------------------------------------------------


class TestSource:
    def test_source_returns_code(self, cm: CodeMap) -> None:
        results = cm.search("check_email")
        func_qn = [r for r in results if r["kind"] == "function"][0]["qualified_name"]
        source = cm.source(func_qn)
        assert "def check_email" in source
        assert "@" in source

    def test_source_nonexistent_raises(self, cm: CodeMap) -> None:
        with pytest.raises(NodeNotFoundError):
            cm.source("nonexistent.node")


# -- End-to-end workflow ---------------------------------------------------


class TestEndToEnd:
    def test_full_workflow(self, cm: CodeMap) -> None:
        """Exercise the typical agent workflow: overview → search → context → expand → source."""
        # 1. Overview
        overview = cm.overview()
        assert "sample_project" in overview

        # 2. Search
        results = cm.search("validate")
        assert len(results) >= 1
        validate_qn = [r for r in results if r["kind"] == "method"][0]["qualified_name"]

        # 3. Context
        context_output = cm.context(validate_qn)
        assert context_output.startswith(f"focus: {validate_qn}")
        assert "[FOCUS]" in context_output

        # 4. Neighbors
        neighbors = cm.neighbors(validate_qn)
        assert isinstance(neighbors, list)

        # 5. Source
        source = cm.source(validate_qn)
        assert "validate" in source
