"""Jedi-based extraction: Python source → CodeGraph.

Strategy:
  1. Walk project directory to find .py files
  2. For each file, use Jedi's get_names() to extract structure (classes, functions, methods)
  3. Use parso tree to extract imports and inheritance
  4. Use Jedi's goto() on references to resolve cross-file calls
  5. Assemble all nodes and edges into a CodeGraph
"""

from __future__ import annotations

import sqlite3
import warnings
from pathlib import Path
from typing import Any, NamedTuple

import jedi
import parso

from codemap.errors import ParseError
from codemap.graph import CodeEdge, CodeGraph, CodeNode, EdgeKind, NodeKind

# Jedi name.type values we extract as graph nodes
_STRUCTURAL_TYPES = {"class", "function"}

# Directories to skip during project walk
_SKIP_DIRS = {
    "venv", ".venv", "env", ".env",
    "node_modules", ".git", "__pycache__",
    ".tox", ".nox", ".mypy_cache", ".pytest_cache",
}

_SQLITE_EXTENSIONS = {".db", ".db3", ".sqlite", ".sqlite3"}


class PendingCall(NamedTuple):
    """An unresolved cross-file call edge.

    Emitted during per-file parsing when goto() resolves to a target
    outside the current file. Resolved after all files are parsed.
    """

    caller_qname: str
    target_module_path: Path  # absolute path of the target's .py file
    target_full_name: str  # Jedi's full_name for the target


def parse_file(
    file_path: Path,
    project_root: Path,
    jedi_project: Any,
) -> tuple[list[CodeNode], list[CodeEdge], list[PendingCall]]:
    """Extract nodes and edges from a single Python file.

    Returns (nodes, edges, pending_calls) relative to the project root.
    Pending calls are cross-file references that need the full node set
    to resolve — handled by parse_project() after all files are parsed.
    Raises ParseError if the file cannot be read or parsed.
    """
    try:
        source = file_path.read_text(encoding="utf-8")
    except OSError as e:
        msg = f"Cannot read {file_path}: {e}"
        raise ParseError(msg) from e

    rel_path = str(file_path.relative_to(project_root))
    module_qname = _path_to_qualified_name(file_path, project_root)

    nodes: list[CodeNode] = []
    edges: list[CodeEdge] = []

    # -- Module node --------------------------------------------------------
    line_count = source.count("\n") + 1
    module_doc = _extract_module_docstring(source)
    module_node = CodeNode(
        qualified_name=module_qname,
        name=file_path.stem,
        kind=NodeKind.MODULE,
        path=rel_path,
        line_start=1,
        line_end=line_count,
        docstring=module_doc,
        parent=_parent_package_qname(module_qname),
    )
    nodes.append(module_node)

    # -- Structural names (classes, functions/methods) ----------------------
    try:
        script = jedi.Script(source, path=str(file_path), project=jedi_project)
    except Exception as e:
        msg = f"Jedi failed to parse {file_path}: {e}"
        raise ParseError(msg) from e

    jedi_names = script.get_names(all_scopes=True, definitions=True, references=False)

    for name in jedi_names:
        if name.type not in _STRUCTURAL_TYPES:
            continue

        # Skip imported symbols: top-level names whose definition lives elsewhere
        if _is_imported_name(name, script, file_path):
            continue

        qname = _build_qualified_name(name, module_qname)
        parent_qname = _build_parent_qname(name, module_qname)
        kind = _classify_node(name)
        line_start: int = name.line
        line_end = _get_end_line(name, line_count)
        signature = _extract_signature(name, kind)
        docstring = _extract_docstring(name)

        node = CodeNode(
            qualified_name=qname,
            name=name.name,
            kind=kind,
            path=rel_path,
            line_start=line_start,
            line_end=line_end,
            signature=signature,
            docstring=docstring,
            parent=parent_qname,
        )
        nodes.append(node)

        # CONTAINS edge from parent
        edges.append(CodeEdge(parent_qname, qname, EdgeKind.CONTAINS))

    # -- Build a set of known qnames for this file -------------------------
    known_qnames = {n.qualified_name for n in nodes}

    # -- Inheritance edges (from parso tree) --------------------------------
    edges.extend(_extract_inheritance(source, module_qname, known_qnames))

    # -- Import edges (from parso tree) ------------------------------------
    edges.extend(_extract_imports(source, module_qname))

    # -- Call edges (from Jedi reference resolution) -----------------------
    local_calls, pending_calls = _extract_calls(
        script, source, module_qname, known_qnames, nodes, file_path, project_root
    )
    edges.extend(local_calls)

    return nodes, edges, pending_calls


def parse_project(
    project_path: str | Path,
    *,
    include_sqlite: bool = True,
) -> CodeGraph:
    """Parse a Python project into a CodeGraph.

    Walks the directory, finds .py files, extracts structure and
    relationships. Returns a complete graph with all indexes built.
    """
    root = Path(project_path).resolve()
    if not root.is_dir():
        msg = f"Project path is not a directory: {root}"
        raise ParseError(msg)

    jedi_project = jedi.Project(path=str(root))

    all_nodes: dict[str, CodeNode] = {}
    all_edges: list[CodeEdge] = []
    all_pending: list[PendingCall] = []

    # Package nodes for directories with __init__.py
    _add_package_nodes(root, all_nodes)

    # Parse each .py file (skip venv / hidden directories)
    py_files = sorted(
        f for f in root.rglob("*.py")
        if not any(p in _SKIP_DIRS for p in f.relative_to(root).parts)
    )
    for py_file in py_files:
        if py_file.name == "__init__.py":
            continue  # Package structure already handled
        try:
            nodes, edges, pending = parse_file(py_file, root, jedi_project)
            for node in nodes:
                all_nodes[node.qualified_name] = node
            all_edges.extend(edges)
            all_pending.extend(pending)
        except ParseError:
            # Skip unparseable files but continue with the rest
            continue

    # Create directory nodes for subdirs that have .py files but no __init__.py
    _add_directory_nodes(root, all_nodes)

    # Add CONTAINS edges from packages/directories to their direct children
    _add_package_containment(all_nodes, all_edges)

    if include_sqlite:
        _add_sqlite_nodes(root, all_nodes, all_edges)

    # Resolve cross-file call edges now that all nodes are known
    all_edges.extend(_resolve_pending_calls(all_pending, all_nodes, root))

    project_qname = root.name
    return CodeGraph(root=project_qname, nodes=all_nodes, edges=all_edges)


# -- Internal helpers ------------------------------------------------------


def _is_imported_name(name: Any, script: Any, file_path: Path) -> bool:
    """Return True if a Jedi name is an imported symbol, not a local definition.

    For top-level names (parent is module), resolves the definition via goto().
    If the definition lives in a different file, it's an import.
    Names nested inside classes/functions are always local.
    """
    parent = name.parent()
    if parent is None or parent.type != "module":
        return False  # nested name — always local to this file

    try:
        targets = script.goto(line=name.line, column=name.column)
        for target in targets:
            if target.module_path is None:
                return True  # C extension or built-in — not local
            return Path(target.module_path).resolve() != file_path.resolve()
    except Exception:
        pass
    return False


def _path_to_qualified_name(file_path: Path, project_root: Path) -> str:
    """Convert a file path to a dotted qualified name.

    If the project root is itself a package (has __init__.py), the root
    directory name is prepended: sample_project/models.py → sample_project.models

    If the project root is not a package, paths are relative:
    my_project/models.py → models
    """
    rel = file_path.relative_to(project_root)
    parts = list(rel.parts)
    # Strip .py extension from the last part
    if parts[-1].endswith(".py"):
        parts[-1] = parts[-1][:-3]

    # If root is a package, prefix with the root directory name
    if (project_root / "__init__.py").exists():
        parts = [project_root.name, *parts]

    return ".".join(parts)


def _parent_package_qname(module_qname: str) -> str | None:
    """Get the parent package qualified name, or None for top-level."""
    parts = module_qname.rsplit(".", maxsplit=1)
    if len(parts) > 1:
        return parts[0]
    return None


def _build_qualified_name(name: Any, module_qname: str) -> str:
    """Build a project-relative qualified name from a Jedi Name object."""
    chain = [name.name]
    current = name.parent()
    while current is not None and current.type != "module":
        chain.append(current.name)
        current = current.parent()
    chain.reverse()
    return f"{module_qname}.{'.'.join(chain)}"


def _build_parent_qname(name: Any, module_qname: str) -> str:
    """Build the qualified name of the parent container."""
    parent = name.parent()
    if parent is None or parent.type == "module":
        return module_qname
    chain = [parent.name]
    current = parent.parent()
    while current is not None and current.type != "module":
        chain.append(current.name)
        current = current.parent()
    chain.reverse()
    return f"{module_qname}.{'.'.join(chain)}"


def _classify_node(name: Any) -> NodeKind:
    """Determine if a function-type name is a METHOD or a FUNCTION."""
    if name.type == "class":
        return NodeKind.CLASS
    parent = name.parent()
    if parent is not None and parent.type == "class":
        return NodeKind.METHOD
    return NodeKind.FUNCTION


def _get_end_line(name: Any, file_line_count: int) -> int:
    """Extract end line from the parso tree node, with fallback."""
    try:
        tree_name = name._name  # noqa: SLF001
        if hasattr(tree_name, "tree_name"):
            parent_node = tree_name.tree_name.parent
            if hasattr(parent_node, "end_pos"):
                end_line: int = parent_node.end_pos[0]
                # parso end_pos can point to the line after the block
                # when the block ends with a newline
                if parent_node.end_pos[1] == 0 and end_line > 1:
                    return end_line - 1
                return end_line
    except (AttributeError, TypeError):
        pass
    return file_line_count


def _extract_signature(name: Any, kind: NodeKind) -> str | None:
    """Build a readable signature string."""
    desc: str = name.description
    if kind == NodeKind.CLASS:
        return desc
    try:
        sigs = name.get_signatures()
        if sigs:
            sig_str: str = sigs[0].to_string()
            return f"def {sig_str}"
    except Exception:
        pass
    return desc


def _extract_docstring(name: Any) -> str | None:
    """Extract first line of docstring, or None."""
    try:
        doc: str = name.docstring(raw=True)
        if doc:
            first_line: str = doc.split("\n")[0].strip()
            return first_line
    except (AttributeError, TypeError):
        pass
    return None


def _extract_module_docstring(source: str) -> str | None:
    """Extract module-level docstring from source."""
    tree: Any = parso.parse(source)
    for child in tree.children:
        if child.type == "simple_stmt":
            for sub in child.children:
                if sub.type == "expr_stmt":
                    first = sub.children[0] if sub.children else None
                    if first is not None and first.type == "string":
                        raw: str = first.value.strip("\"'").strip()
                        return raw.split("\n")[0] if raw else None
        # Only check the first statement
        break
    return None


def _extract_inheritance(
    source: str,
    module_qname: str,
    known_qnames: set[str],
) -> list[CodeEdge]:
    """Extract INHERITS edges from class definitions via parso."""
    edges: list[CodeEdge] = []
    tree: Any = parso.parse(source)

    for node in _walk_tree(tree):
        if node.type != "classdef":
            continue
        class_name: str | None = None
        superclasses: list[str] = []
        in_arglist = False
        for child in node.children:
            if hasattr(child, "type") and child.type == "name" and class_name is None:
                class_name = child.value
            elif hasattr(child, "value") and child.value == "(":
                in_arglist = True
            elif hasattr(child, "value") and child.value == ")":
                in_arglist = False
            elif in_arglist and hasattr(child, "type"):
                if child.type == "name":
                    superclasses.append(child.value)
                elif child.type == "arglist":
                    for arg_child in child.children:
                        if hasattr(arg_child, "type") and arg_child.type == "name":
                            superclasses.append(arg_child.value)

        if class_name and superclasses:
            class_qname = f"{module_qname}.{class_name}"
            for super_name in superclasses:
                super_qname = f"{module_qname}.{super_name}"
                if super_qname in known_qnames:
                    edges.append(CodeEdge(class_qname, super_qname, EdgeKind.INHERITS))

    return edges


def _extract_imports(
    source: str,
    module_qname: str,
) -> list[CodeEdge]:
    """Extract IMPORTS edges from import statements via parso."""
    edges: list[CodeEdge] = []
    tree: Any = parso.parse(source)

    for child in tree.children:
        if child.type != "simple_stmt":
            continue
        for sub in child.children:
            if sub.type != "import_from":
                continue
            module_name: str | None = None
            for part in sub.children:
                if hasattr(part, "type"):
                    if part.type == "dotted_name":
                        module_name = part.get_code().strip()
                        break
                    if (
                        part.type == "name"
                        and module_name is None
                        and hasattr(part, "value")
                        and part.value not in ("from", "import")
                    ):
                        module_name = part.value
                        break
            if module_name:
                edges.append(CodeEdge(module_qname, module_name, EdgeKind.IMPORTS))
    return edges


def _extract_calls(
    script: Any,
    source: str,
    module_qname: str,
    known_qnames: set[str],
    nodes: list[CodeNode],
    file_path: Path,
    project_root: Path,
) -> tuple[list[CodeEdge], list[PendingCall]]:
    """Extract CALLS edges by resolving references via Jedi goto().

    For each function/method node, scan its body for references that
    resolve to other known functions/methods.

    Returns (resolved_edges, pending_calls). Pending calls are cross-file
    references whose targets aren't in this file's known_qnames — they
    carry enough info for parse_project() to resolve them later.
    """
    edges: list[CodeEdge] = []
    pending: list[PendingCall] = []
    seen: set[tuple[str, str]] = set()
    seen_pending: set[tuple[str, str]] = set()

    func_nodes = [n for n in nodes if n.kind in (NodeKind.FUNCTION, NodeKind.METHOD)]

    refs = script.get_names(all_scopes=True, definitions=False, references=True)

    for ref in refs:
        if ref.type == "param":
            continue

        caller = _find_containing_function(ref.line, func_nodes)
        if caller is None:
            continue

        try:
            targets = script.goto(line=ref.line, column=ref.column)
        except Exception:
            continue

        for target in targets:
            if target.full_name is None:
                continue
            if target.module_path is None:
                continue
            target_full: str = target.full_name
            if target_full.startswith("builtins."):
                continue

            # Try local resolution first (same file)
            target_qname = _resolve_target_qname(
                target_full, module_qname, known_qnames
            )
            if target_qname and target_qname != caller.qualified_name:
                pair = (caller.qualified_name, target_qname)
                if pair not in seen:
                    seen.add(pair)
                    edges.append(
                        CodeEdge(
                            caller.qualified_name,
                            target_qname,
                            EdgeKind.CALLS,
                        )
                    )
            elif target_qname is None:
                # Unresolved locally — defer for cross-file resolution
                target_path = Path(target.module_path).resolve()
                if _is_within_project(target_path, project_root):
                    pending_key = (caller.qualified_name, target_full)
                    if pending_key not in seen_pending:
                        seen_pending.add(pending_key)
                        pending.append(
                            PendingCall(caller.qualified_name, target_path, target_full)
                        )

    return edges, pending


def _find_containing_function(line: int, func_nodes: list[CodeNode]) -> CodeNode | None:
    """Find the innermost function/method containing a given line."""
    best: CodeNode | None = None
    for node in func_nodes:
        if node.line_start <= line <= node.line_end:
            if best is None or (node.line_end - node.line_start) < (
                best.line_end - best.line_start
            ):
                best = node
    return best


def _resolve_target_qname(
    jedi_full_name: str,
    module_qname: str,
    known_qnames: set[str],
) -> str | None:
    """Try to match a Jedi-resolved name to a known node in our graph."""
    if jedi_full_name in known_qnames:
        return jedi_full_name

    parts = jedi_full_name.split(".")
    for i in range(len(parts)):
        candidate = ".".join(parts[i:])
        if candidate in known_qnames:
            return candidate

    return None


def _is_within_project(path: Path, project_root: Path) -> bool:
    """Check if a resolved path falls inside the project root."""
    try:
        path.relative_to(project_root)
        return True
    except ValueError:
        return False


def _resolve_pending_calls(
    pending: list[PendingCall],
    all_nodes: dict[str, CodeNode],
    project_root: Path,
) -> list[CodeEdge]:
    """Resolve cross-file pending calls against the complete node set.

    Converts each PendingCall's module_path to our qualified name space,
    then tries suffix-matching against all_nodes to find the target.
    """
    edges: list[CodeEdge] = []
    seen: set[tuple[str, str]] = set()
    all_qnames = set(all_nodes.keys())

    for pc in pending:
        # Convert the target's file path to our module qname
        target_module_qname = _path_to_qualified_name(pc.target_module_path, project_root)

        # Try to build the target qname from module qname + name suffix.
        # Jedi full_name might be "src.discovery.FunctionDiscovery.discover_all"
        # Our module qname is "discovery". We need "discovery.FunctionDiscovery.discover_all".
        # Strategy: take the part of full_name after the module-level component.
        target_qname = _resolve_cross_file_qname(
            pc.target_full_name, target_module_qname, all_qnames
        )

        if target_qname and target_qname != pc.caller_qname:
            pair = (pc.caller_qname, target_qname)
            if pair not in seen:
                seen.add(pair)
                edges.append(CodeEdge(pc.caller_qname, target_qname, EdgeKind.CALLS))

    return edges


def _resolve_cross_file_qname(
    jedi_full_name: str,
    target_module_qname: str,
    all_qnames: set[str],
) -> str | None:
    """Match a Jedi full_name to a node in the graph using the target's module qname.

    Jedi returns e.g. "src.discovery.FunctionDiscovery.discover_all".
    We know the target module is "discovery" (from path conversion).
    We try: target_module_qname + suffix portions of full_name until we hit a match.
    """
    # Direct match (unlikely but cheap)
    if jedi_full_name in all_qnames:
        return jedi_full_name

    # Suffix matching: try all suffixes of full_name, prefixed with our module qname
    parts = jedi_full_name.split(".")
    for i in range(len(parts)):
        suffix = ".".join(parts[i:])
        # Try module_qname.suffix (e.g. "discovery" + "FunctionDiscovery.discover_all")
        candidate = f"{target_module_qname}.{suffix}"
        if candidate in all_qnames:
            return candidate
        # Also try the bare suffix (handles package-prefixed qnames)
        if suffix in all_qnames:
            return suffix

    return None


def _add_package_nodes(
    project_root: Path,
    nodes: dict[str, CodeNode],
) -> None:
    """Add PACKAGE nodes for directories containing __init__.py."""
    for init_file in sorted(
        f for f in project_root.rglob("__init__.py")
        if not any(p in _SKIP_DIRS for p in f.relative_to(project_root).parts)
    ):
        pkg_dir = init_file.parent
        if pkg_dir == project_root:
            qname = project_root.name
        else:
            rel = pkg_dir.relative_to(project_root)
            qname = ".".join(rel.parts)

        parent = _parent_package_qname(qname)

        try:
            init_source = init_file.read_text(encoding="utf-8")
            docstring = _extract_module_docstring(init_source)
        except OSError:
            docstring = None

        rel_path = str(pkg_dir.relative_to(project_root))
        if rel_path == ".":
            rel_path = project_root.name

        nodes[qname] = CodeNode(
            qualified_name=qname,
            name=pkg_dir.name,
            kind=NodeKind.PACKAGE,
            path=rel_path,
            line_start=1,
            line_end=1,
            docstring=docstring,
            parent=parent,
        )


def _add_directory_nodes(
    project_root: Path,
    nodes: dict[str, CodeNode],
) -> None:
    """Create nodes for subdirectories that contain .py files but lack __init__.py.

    Without this, modules in non-package subdirs (e.g. src/main.py → "src.main")
    reference a parent "src" that doesn't exist, breaking the hierarchy.
    """
    # Collect parent qnames that modules reference but don't exist yet
    missing_parents: set[str] = set()
    for node in list(nodes.values()):
        parent = node.parent
        while parent is not None and parent not in nodes:
            missing_parents.add(parent)
            parts = parent.rsplit(".", maxsplit=1)
            parent = parts[0] if len(parts) > 1 else None

    for qname in missing_parents:
        parts = qname.split(".")
        rel_path = "/".join(parts)
        dir_path = project_root / rel_path
        if not dir_path.is_dir():
            # qname might map to project root itself for single-part names
            if len(parts) == 1 and (project_root / parts[0]).is_dir():
                rel_path = parts[0]
            else:
                continue

        parent = _parent_package_qname(qname)
        nodes[qname] = CodeNode(
            qualified_name=qname,
            name=parts[-1],
            kind=NodeKind.PACKAGE,
            path=rel_path,
            line_start=1,
            line_end=1,
            parent=parent,
        )


def _add_package_containment(
    nodes: dict[str, CodeNode],
    edges: list[CodeEdge],
) -> None:
    """Add CONTAINS edges from packages to their direct module children."""
    existing_edges = {(e.source, e.target, e.kind) for e in edges}

    for node in nodes.values():
        if node.parent is not None and node.parent in nodes:
            triple = (node.parent, node.qualified_name, EdgeKind.CONTAINS)
            if triple not in existing_edges:
                edges.append(
                    CodeEdge(node.parent, node.qualified_name, EdgeKind.CONTAINS)
                )
                existing_edges.add(triple)


def _walk_tree(node: Any) -> list[Any]:
    """Recursively walk all nodes in a parso tree."""
    result: list[Any] = [node]
    if hasattr(node, "children"):
        for child in node.children:
            result.extend(_walk_tree(child))
    return result


def _add_sqlite_nodes(
    project_root: Path,
    nodes: dict[str, CodeNode],
    edges: list[CodeEdge],
) -> None:
    """Discover SQLite files and add database/schema/table hierarchy nodes."""
    sqlite_files = sorted(
        f for f in project_root.rglob("*")
        if f.is_file()
        and f.suffix.lower() in _SQLITE_EXTENSIONS
        and not any(p in _SKIP_DIRS for p in f.relative_to(project_root).parts)
    )
    if not sqlite_files:
        return

    existing_edges = {(e.source, e.target, e.kind) for e in edges}

    for db_file in sqlite_files:
        try:
            info = _read_sqlite_catalog(db_file)
        except sqlite3.Error as exc:
            rel = db_file.relative_to(project_root)
            warnings.warn(
                f"Skipping SQLite introspection for {rel}: {exc}",
                RuntimeWarning,
                stacklevel=2,
            )
            continue

        rel_parts = db_file.relative_to(project_root).parts
        parent_qname = _ensure_parent_qname_for_file(rel_parts, nodes)
        db_qname = _db_qname_for_file(rel_parts)

        db_node = CodeNode(
            qualified_name=db_qname,
            name=db_file.name,
            kind=NodeKind.DATABASE,
            path=str(db_file.relative_to(project_root)),
            line_start=1,
            line_end=1,
            parent=parent_qname,
        )
        nodes[db_qname] = db_node
        _add_contains_edge(parent_qname, db_qname, edges, existing_edges)

        schema_names = sorted(info.keys())
        show_schema_nodes = len(schema_names) > 1 or any(s != "main" for s in schema_names)

        for schema_name in schema_names:
            tables = info[schema_name]
            if show_schema_nodes:
                schema_qname = f"{db_qname}.{_sanitize_qname_part(schema_name)}"
                schema_node = CodeNode(
                    qualified_name=schema_qname,
                    name=schema_name,
                    kind=NodeKind.DB_SCHEMA,
                    path=str(db_file.relative_to(project_root)),
                    line_start=1,
                    line_end=1,
                    parent=db_qname,
                )
                nodes[schema_qname] = schema_node
                _add_contains_edge(db_qname, schema_qname, edges, existing_edges)
                table_parent = schema_qname
            else:
                table_parent = db_qname

            for table_name, columns in sorted(tables.items(), key=lambda item: item[0]):
                table_qname = (
                    f"{table_parent}.{_sanitize_qname_part(table_name)}"
                )
                table_node = CodeNode(
                    qualified_name=table_qname,
                    name=table_name,
                    kind=NodeKind.DB_TABLE,
                    path=str(db_file.relative_to(project_root)),
                    line_start=1,
                    line_end=1,
                    parent=table_parent,
                    metadata={"columns": columns},
                )
                nodes[table_qname] = table_node
                _add_contains_edge(table_parent, table_qname, edges, existing_edges)


def _read_sqlite_catalog(db_path: Path) -> dict[str, dict[str, list[str]]]:
    """Return schema->table->columns mapping for user tables only."""
    uri = f"file:{db_path.as_posix()}?mode=ro"
    with sqlite3.connect(uri, uri=True) as conn:
        rows = conn.execute("PRAGMA database_list").fetchall()

        schema_table_columns: dict[str, dict[str, list[str]]] = {}
        for _seq, schema_name, _file in rows:
            schema_ident = _quote_sqlite_identifier(schema_name)
            table_rows = conn.execute(
                f"""
                SELECT name
                FROM {schema_ident}.sqlite_master
                WHERE type = 'table' AND name NOT LIKE 'sqlite_%'
                ORDER BY name
                """
            ).fetchall()

            tables: dict[str, list[str]] = {}
            for (table_name,) in table_rows:
                pragma_ident = _quote_sqlite_identifier(schema_name)
                table_ident = _quote_sqlite_identifier(table_name)
                col_rows = conn.execute(
                    f"PRAGMA {pragma_ident}.table_info({table_ident})"
                ).fetchall()
                columns = [str(col[1]) for col in col_rows]
                tables[str(table_name)] = columns

            if tables:
                schema_table_columns[str(schema_name)] = tables

        return schema_table_columns


def _quote_sqlite_identifier(identifier: str) -> str:
    """Quote an identifier for SQL fragments."""
    escaped = identifier.replace('"', '""')
    return f'"{escaped}"'


def _sanitize_qname_part(raw: str) -> str:
    """Make a stable qname part that avoids separator collisions."""
    return raw.replace(".", "_")


def _db_qname_for_file(rel_parts: tuple[str, ...]) -> str:
    """Build qname for a database file from its relative path."""
    dir_parts = list(rel_parts[:-1])
    file_stem = Path(rel_parts[-1]).stem
    parts = [*dir_parts, file_stem]
    return ".".join(_sanitize_qname_part(p) for p in parts if p)


def _ensure_parent_qname_for_file(
    rel_parts: tuple[str, ...],
    nodes: dict[str, CodeNode],
) -> str | None:
    """Ensure directory nodes exist for file parent and return parent qname."""
    dir_parts = list(rel_parts[:-1])
    if not dir_parts:
        return None

    for idx in range(1, len(dir_parts) + 1):
        raw_parts = dir_parts[:idx]
        qname = ".".join(_sanitize_qname_part(p) for p in raw_parts)
        if qname in nodes:
            continue
        parent = ".".join(_sanitize_qname_part(p) for p in raw_parts[:-1]) or None
        nodes[qname] = CodeNode(
            qualified_name=qname,
            name=raw_parts[-1],
            kind=NodeKind.PACKAGE,
            path="/".join(raw_parts),
            line_start=1,
            line_end=1,
            parent=parent,
        )
    return ".".join(_sanitize_qname_part(p) for p in dir_parts)


def _add_contains_edge(
    source: str | None,
    target: str,
    edges: list[CodeEdge],
    existing_edges: set[tuple[str, str, EdgeKind]],
) -> None:
    """Add a CONTAINS edge if source exists and edge is not duplicated."""
    if source is None:
        return
    triple = (source, target, EdgeKind.CONTAINS)
    if triple in existing_edges:
        return
    edges.append(CodeEdge(source, target, EdgeKind.CONTAINS))
    existing_edges.add(triple)
