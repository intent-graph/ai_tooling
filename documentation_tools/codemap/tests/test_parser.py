"""Tests for Jedi-based parser: single file and multi-file project."""

import sqlite3
from pathlib import Path

import pytest

from codemap.errors import ParseError
from codemap.graph import EdgeKind, NodeKind
from codemap.parser import parse_file, parse_project

FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAMPLE_PROJECT = FIXTURES_DIR / "sample_project"


# -- S3: Single file parsing -----------------------------------------------


class TestParseSingleFile:
    """Parse a single .py file and verify extracted nodes and edges."""

    def _parse_models(self) -> tuple[list, list]:
        import jedi

        project = jedi.Project(path=str(SAMPLE_PROJECT))
        nodes, edges, _pending = parse_file(
            SAMPLE_PROJECT / "models.py", SAMPLE_PROJECT, project
        )
        return nodes, edges

    def test_module_node_exists(self) -> None:
        nodes, _ = self._parse_models()
        module = [n for n in nodes if n.kind == NodeKind.MODULE]
        assert len(module) == 1
        assert module[0].qualified_name == "sample_project.models"
        assert module[0].path == "models.py"

    def test_classes_extracted(self) -> None:
        nodes, _ = self._parse_models()
        classes = [n for n in nodes if n.kind == NodeKind.CLASS]
        class_names = {c.name for c in classes}
        assert "BaseModel" in class_names
        assert "User" in class_names
        assert "Order" in class_names

    def test_methods_extracted(self) -> None:
        nodes, _ = self._parse_models()
        methods = [n for n in nodes if n.kind == NodeKind.METHOD]
        method_names = {m.name for m in methods}
        assert "save" in method_names
        assert "__init__" in method_names
        assert "validate" in method_names

    def test_method_has_signature(self) -> None:
        nodes, _ = self._parse_models()
        validate = [n for n in nodes if n.name == "validate"][0]
        assert validate.signature is not None
        assert "validate" in validate.signature
        assert "bool" in validate.signature

    def test_class_has_docstring(self) -> None:
        nodes, _ = self._parse_models()
        user = [n for n in nodes if n.name == "User" and n.kind == NodeKind.CLASS][0]
        assert user.docstring is not None
        assert "user" in user.docstring.lower()

    def test_containment_edges(self) -> None:
        _, edges = self._parse_models()
        contains = [e for e in edges if e.kind == EdgeKind.CONTAINS]
        # Module contains classes
        module_to_class = [
            e
            for e in contains
            if e.source.endswith("models") and "BaseModel" in e.target
        ]
        assert len(module_to_class) == 1

    def test_inheritance_edges(self) -> None:
        _, edges = self._parse_models()
        inherits = [e for e in edges if e.kind == EdgeKind.INHERITS]
        # User inherits BaseModel
        user_inherits = [
            e for e in inherits if "User" in e.source and "BaseModel" in e.target
        ]
        assert len(user_inherits) == 1

    def test_import_edges(self) -> None:
        _, edges = self._parse_models()
        imports = [e for e in edges if e.kind == EdgeKind.IMPORTS]
        # models imports from sample_project.utils
        assert any("utils" in e.target for e in imports)

    def test_line_ranges_valid(self) -> None:
        nodes, _ = self._parse_models()
        for node in nodes:
            assert node.line_start >= 1
            assert node.line_end >= node.line_start

    def test_parent_references_valid(self) -> None:
        nodes, _ = self._parse_models()
        qnames = {n.qualified_name for n in nodes}
        for node in nodes:
            if node.parent is not None:
                # Parent should exist in nodes or be a package-level name
                assert node.parent in qnames or "." not in node.parent, (
                    f"Orphaned parent: {node.parent} for {node.qualified_name}"
                )


# -- S3: Edge cases --------------------------------------------------------


class TestParseEdgeCases:
    def test_nonexistent_file_raises(self) -> None:
        import jedi

        project = jedi.Project(path=str(SAMPLE_PROJECT))
        with pytest.raises(ParseError, match="Cannot read"):
            parse_file(SAMPLE_PROJECT / "nonexistent.py", SAMPLE_PROJECT, project)


# -- S4: Multi-file project parsing ----------------------------------------


class TestParseProject:
    """Parse the full sample project and verify cross-file relationships."""

    def _parse(self) -> "codemap.graph.CodeGraph":  # type: ignore[name-defined]  # noqa: F821
        return parse_project(SAMPLE_PROJECT)

    def test_all_modules_found(self) -> None:
        graph = self._parse()
        modules = [n for n in graph.nodes.values() if n.kind == NodeKind.MODULE]
        module_names = {m.name for m in modules}
        assert "models" in module_names
        assert "utils" in module_names
        assert "main" in module_names

    def test_package_node_exists(self) -> None:
        graph = self._parse()
        packages = [n for n in graph.nodes.values() if n.kind == NodeKind.PACKAGE]
        assert len(packages) >= 1
        assert any(p.name == "sample_project" for p in packages)

    def test_total_node_count(self) -> None:
        """Should have: 1 package + 3 modules + 3 classes + several methods/functions."""
        graph = self._parse()
        assert len(graph.nodes) >= 10

    def test_cross_file_import_edges(self) -> None:
        graph = self._parse()
        imports = [e for e in graph.edges if e.kind == EdgeKind.IMPORTS]
        # models imports utils, main imports models and utils
        import_targets = {e.target for e in imports}
        assert any("utils" in t for t in import_targets)
        assert any("models" in t for t in import_targets)

    def test_package_contains_modules(self) -> None:
        graph = self._parse()
        pkg = [n for n in graph.nodes.values() if n.kind == NodeKind.PACKAGE][0]
        children = graph.children_of(pkg.qualified_name)
        child_names = {c.name for c in children}
        assert "models" in child_names
        assert "utils" in child_names
        assert "main" in child_names

    def test_nonexistent_project_raises(self) -> None:
        with pytest.raises(ParseError, match="not a directory"):
            parse_project("/nonexistent/path")

    def test_indexes_populated(self) -> None:
        graph = self._parse()
        # edges_from and edges_to should be populated
        has_outgoing = any(
            len(graph.edges_from(n.qualified_name)) > 0 for n in graph.nodes.values()
        )
        assert has_outgoing

    def test_functions_in_utils(self) -> None:
        graph = self._parse()
        funcs = [
            n
            for n in graph.nodes.values()
            if n.kind == NodeKind.FUNCTION and "utils" in n.qualified_name
        ]
        func_names = {f.name for f in funcs}
        assert "check_email" in func_names
        assert "format_name" in func_names


class TestParseProjectWithSqlite:
    def _build_project_with_db(self, tmp_path: Path) -> Path:
        project = tmp_path / "repo"
        project.mkdir()
        (project / "main.py").write_text("def hello() -> str:\n    return 'ok'\n")
        db_path = project / "app.db"
        conn = sqlite3.connect(db_path)
        conn.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, created_at TEXT)"
        )
        conn.execute("CREATE TABLE events (id INTEGER PRIMARY KEY, event_type TEXT)")
        conn.commit()
        conn.close()
        return project

    def test_sqlite_tables_are_added_with_columns(self, tmp_path: Path) -> None:
        project = self._build_project_with_db(tmp_path)
        graph = parse_project(project)

        db_nodes = [n for n in graph.nodes.values() if n.kind == NodeKind.DATABASE]
        assert len(db_nodes) == 1
        db_node = db_nodes[0]
        assert db_node.name == "app.db"

        schema_nodes = [n for n in graph.nodes.values() if n.kind == NodeKind.DB_SCHEMA]
        assert schema_nodes == []

        table_nodes = [n for n in graph.nodes.values() if n.kind == NodeKind.DB_TABLE]
        table_names = {n.name for n in table_nodes}
        assert {"users", "events"} <= table_names

        users_node = next(n for n in table_nodes if n.name == "users")
        assert users_node.metadata is not None
        assert users_node.metadata["columns"] == ["id", "email", "created_at"]
        assert users_node.parent == db_node.qualified_name

    def test_sqlite_introspection_can_be_disabled(self, tmp_path: Path) -> None:
        project = self._build_project_with_db(tmp_path)
        graph = parse_project(project, include_sqlite=False)
        assert all(n.kind != NodeKind.DATABASE for n in graph.nodes.values())
        assert all(n.kind != NodeKind.DB_TABLE for n in graph.nodes.values())

    def test_invalid_sqlite_file_warns_and_continues(self, tmp_path: Path) -> None:
        project = tmp_path / "repo"
        project.mkdir()
        (project / "main.py").write_text("def hello() -> str:\n    return 'ok'\n")
        (project / "broken.db").write_text("not a sqlite database")

        with pytest.warns(RuntimeWarning, match="Skipping SQLite introspection"):
            graph = parse_project(project)

        assert "main" in {n.name for n in graph.nodes.values()}
