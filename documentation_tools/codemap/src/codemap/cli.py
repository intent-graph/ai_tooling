"""Command-line interface for CodeMap — structural code graph for AI agents."""

from __future__ import annotations

import argparse
import json
import sys

from codemap.api import CodeMap
from codemap.errors import CodeMapError, NodeNotFoundError


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codemap",
        description="Structural code graph for AI agent reasoning",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- overview ---
    p_overview = sub.add_parser(
        "overview",
        help="Print project skeleton (names and nesting only)",
    )
    p_overview.add_argument("path", help="Root of the Python project to parse")
    p_overview.add_argument(
        "--no-sqlite-introspection",
        action="store_true",
        help="Disable SQLite file introspection",
    )

    # --- search ---
    p_search = sub.add_parser(
        "search",
        help="Find nodes by name pattern (case-insensitive substring)",
    )
    p_search.add_argument("path", help="Root of the Python project to parse")
    p_search.add_argument("query", help="Substring to match against node names")
    p_search.add_argument(
        "--no-sqlite-introspection",
        action="store_true",
        help="Disable SQLite file introspection",
    )

    # --- context ---
    p_context = sub.add_parser(
        "context",
        help="V-shaped context for a focus node (ancestors + children + edges)",
    )
    p_context.add_argument("path", help="Root of the Python project to parse")
    p_context.add_argument("qualified_name", help="Fully qualified node name")
    p_context.add_argument(
        "--no-sqlite-introspection",
        action="store_true",
        help="Disable SQLite file introspection",
    )

    # --- neighbors ---
    p_neighbors = sub.add_parser(
        "neighbors",
        help="Immediate connections of a node",
    )
    p_neighbors.add_argument("path", help="Root of the Python project to parse")
    p_neighbors.add_argument("qualified_name", help="Fully qualified node name")
    p_neighbors.add_argument(
        "--edge-type", help="Filter by edge type (e.g. calls, imports)"
    )
    p_neighbors.add_argument(
        "--no-sqlite-introspection",
        action="store_true",
        help="Disable SQLite file introspection",
    )

    # --- source ---
    p_source = sub.add_parser(
        "source",
        help="Print source code lines for a node",
    )
    p_source.add_argument("path", help="Root of the Python project to parse")
    p_source.add_argument("qualified_name", help="Fully qualified node name")
    p_source.add_argument(
        "--no-sqlite-introspection",
        action="store_true",
        help="Disable SQLite file introspection",
    )

    # --- export-yed ---
    p_export = sub.add_parser(
        "export-yed",
        help="Export graph to yEd-compatible GraphML",
    )
    p_export.add_argument("path", help="Root of the Python project to parse")
    p_export.add_argument("--output", "-o", help="Output .graphml file path")
    p_export.add_argument(
        "--flat",
        action="store_true",
        default=True,
        help="Emit all nodes at top level (no nested groups) [default: True]",
    )
    p_export.add_argument(
        "--grouped",
        action="store_false",
        dest="flat",
        help="Use nested folder groups (original behavior)",
    )
    p_export.add_argument(
        "--no-sqlite-introspection",
        action="store_true",
        help="Disable SQLite file introspection",
    )

    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    try:
        cm = CodeMap.build(
            args.path,
            include_sqlite=not getattr(args, "no_sqlite_introspection", False),
        )
    except Exception as exc:
        print(f"Error parsing project: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        if args.command == "overview":
            print(cm.overview())

        elif args.command == "search":
            results = cm.search(args.query)
            if not results:
                print("No matches found.", file=sys.stderr)
                sys.exit(1)
            print(json.dumps(results, indent=2))

        elif args.command == "context":
            print(cm.context(args.qualified_name))

        elif args.command == "neighbors":
            results = cm.neighbors(args.qualified_name, edge_type=args.edge_type)
            if not results:
                print("No neighbors found.", file=sys.stderr)
            print(json.dumps(results, indent=2))

        elif args.command == "source":
            print(cm.source(args.qualified_name))

        elif args.command == "export-yed":
            out = cm.export_yed(
                output_path=args.output if args.output else None,
                flat=args.flat,
            )
            print(f"GraphML written to {out}")

    except NodeNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    except CodeMapError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
