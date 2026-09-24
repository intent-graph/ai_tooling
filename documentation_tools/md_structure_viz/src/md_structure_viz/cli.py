"""Command-line interface for documentation tree visualization."""

import argparse
import subprocess
import sys
from pathlib import Path

from .doc_tree import build_doc_tree
from .manifest_generator import generate_sections_yaml, generate_cross_refs_yaml
from .mermaid import generate_simple_flowchart, generate_stats
from .html_generator import HTMLGenerator


def main():
    """Main CLI entry point for md-doc-tree-full."""
    parser = argparse.ArgumentParser(
        description="Visualize documentation structure with cross-references"
    )
    parser.add_argument("path", nargs="?", default=".", help="Root documentation directory")
    parser.add_argument(
        "--output", "-o",
        help=(
            "Output prefix (manifest) or file path (flow/html). "
            "For manifest format: produces <prefix>_sections.yaml and <prefix>_cross_refs.yaml"
        ),
    )
    parser.add_argument(
        "--format", "-f",
        choices=["manifest", "flow", "html"],
        default="manifest",
        help="Output format (default: manifest)",
    )
    parser.add_argument(
        "--heading-depth",
        type=int,
        default=2,
        help="Max heading level to include in sections manifest (default: 2 = # and ##)",
    )
    parser.add_argument(
        "--max-sections",
        type=int,
        default=20,
        help="Per-file section threshold before falling back to shallower headings (default: 20)",
    )
    parser.add_argument("--stats", "-s", action="store_true", help="Show statistics only")
    parser.add_argument(
        "--ignore-default",
        dest="ignore_default",
        default=True,
        action=argparse.BooleanOptionalAction,
        help="Apply default ignore patterns for venv, node_modules, etc. (default: True)",
    )
    parser.add_argument(
        "--respect-gitignore",
        action="store_true",
        default=False,
        help="Additionally filter files ignored by .gitignore",
    )

    args = parser.parse_args()

    # Validate: manifest format requires -o
    if args.format == "manifest" and not args.output:
        parser.error(
            "--output (-o) is required for manifest format.\n"
            "  Example: md-doc-tree-full ./docs -o doc_manifest\n"
            "  This produces: doc_manifest_sections.yaml and doc_manifest_cross_refs.yaml"
        )

    root = Path(args.path).resolve()

    try:
        tree = build_doc_tree(
            root,
            ignore_default=args.ignore_default,
            respect_gitignore=args.respect_gitignore,
        )
    except Exception as e:
        print(f"Error: Failed to analyze directory: {e}", file=sys.stderr)
        sys.exit(1)

    if args.stats:
        print(generate_stats(tree))
        return

    if args.format == "html":
        output_path = Path(args.output) if args.output else Path("doc_manifest.html")
        html_gen = HTMLGenerator(tree)
        html_gen.generate(output_path)
        print(f"HTML visualization generated: {output_path}")
        return

    if args.format == "flow":
        mermaid_content = generate_simple_flowchart(tree)
        if args.output:
            output_path = Path(args.output)
            with open(output_path, "w") as f:
                f.write("```mermaid\n")
                f.write(mermaid_content)
                f.write("\n```\n")
            print(f"Mermaid diagram saved to {output_path}")
        else:
            print("```mermaid")
            print(mermaid_content)
            print("```")
        return

    # --- manifest format (default) ---
    sections_content = generate_sections_yaml(
        tree,
        heading_depth=args.heading_depth,
        max_sections=args.max_sections,
    )
    cross_refs_content = generate_cross_refs_yaml(tree)

    prefix = Path(args.output)
    sections_path = prefix.parent / f"{prefix.name}_sections.yaml"
    cross_refs_path = prefix.parent / f"{prefix.name}_cross_refs.yaml"

    sections_path.write_text(sections_content, encoding="utf-8")
    cross_refs_path.write_text(cross_refs_content, encoding="utf-8")

    print(f"Manifest generated:")
    print(f"  {sections_path}")
    print(f"  {cross_refs_path}")


def run_simple():
    """Entry point for md-doc-tree-simple wrapper."""
    script_dir = Path(__file__).parent.parent.parent
    script_path = script_dir / "bin" / "md-doc-tree-simple"

    if not script_path.exists():
        print(f"Error: Script not found: {script_path}", file=sys.stderr)
        sys.exit(1)

    result = subprocess.run([str(script_path)] + sys.argv[1:])
    sys.exit(result.returncode)


def run_rich():
    """Entry point for md-doc-tree-rich wrapper."""
    script_dir = Path(__file__).parent.parent.parent
    script_path = script_dir / "bin" / "md-doc-tree-rich"

    if not script_path.exists():
        print(f"Error: Script not found: {script_path}", file=sys.stderr)
        sys.exit(1)

    result = subprocess.run([str(script_path)] + sys.argv[1:])
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
