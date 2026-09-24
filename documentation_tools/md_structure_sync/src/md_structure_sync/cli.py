"""Command-line interface."""

import argparse
import sys
from pathlib import Path

from md_structure_sync.models import Config
from md_structure_sync.sync import sync_directory, sync_file
from md_structure_sync.xref_validate import (
    validate_cross_refs,
    validate_directory_cross_refs,
)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Synchronize markdown TOC and section line ranges",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  md-structure-sync file.md              # Sync single file (toc_sync)
  md-structure-sync docs/ --pattern "*.md"  # Sync directory
  md-structure-sync file.md --dry-run    # Show changes without writing
  md-structure-sync file.md --cross-refs # Validate cross-references
  md-structure-sync docs/ --cross-refs --on-invalid=warn  # Warn mode
""",
    )

    parser.add_argument(
        "path",
        type=Path,
        help="File or directory to sync",
    )
    parser.add_argument(
        "--pattern",
        default="*.md",
        help="Glob pattern for directory mode (default: *.md)",
    )
    parser.add_argument(
        "--min-level",
        type=int,
        default=2,
        help="Minimum header level to track (default: 2)",
    )
    parser.add_argument(
        "--max-level",
        type=int,
        default=4,
        help="Maximum header level to track (default: 4)",
    )
    parser.add_argument(
        "--no-line-comments",
        action="store_true",
        help="Don't add <!-- Lines --> comments after headers",
    )
    # TOC policy: when to add / maintain / remove TOC
    parser.add_argument(
        "--toc",
        choices=["maintain-only", "add-above", "remove", "add-always"],
        default="maintain-only",
        help="TOC policy: maintain-only (default), add-above (add TOC only when header count >= --toc-min-headers), remove (strip TOC + separator), add-always (add TOC whenever there are headers)",
    )
    parser.add_argument(
        "--toc-min-headers",
        type=int,
        default=3,
        metavar="N",
        help="When --toc add-above: only add TOC if file has at least N headers (default: 3)",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Show what would change without writing files",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Only output errors",
    )

    # Cross-reference validation options
    parser.add_argument(
        "--cross-refs",
        action="store_true",
        help="Validate cross-references between markdown files",
    )
    parser.add_argument(
        "--on-invalid",
        choices=["remove", "warn"],
        default="remove",
        help="Action for invalid cross-refs: remove (default) or warn",
    )
    parser.add_argument(
        "--no-auto-fix",
        action="store_true",
        help="Don't auto-fix fuzzy anchor matches",
    )

    args = parser.parse_args()

    toc_policy_map = {
        "maintain-only": "maintain_only",
        "add-above": "add_above_size",
        "remove": "remove",
        "add-always": "add_always",
    }
    config = Config(
        min_level=args.min_level,
        max_level=args.max_level,
        include_line_comments=not args.no_line_comments,
        dry_run=args.dry_run,
        toc_policy=toc_policy_map[args.toc],
        toc_min_headers=args.toc_min_headers,
    )

    path = args.path

    if not path.exists():
        print(f"Error: {path} does not exist", file=sys.stderr)
        return 1

    # Cross-reference validation mode
    if args.cross_refs:
        return _run_xref_validate(path, args, config)

    # Default: toc_sync mode
    return _run_toc_sync(path, args, config)


def _run_toc_sync(path: Path, args, config: Config) -> int:
    """Run toc_sync on file(s)."""
    if path.is_file():
        results = [sync_file(path, config)]
    else:
        results = sync_directory(path, args.pattern, config)

    # Report results
    errors = 0
    changed = 0

    for result in results:
        if result.error:
            print(f"ERROR: {result.path}: {result.error}", file=sys.stderr)
            errors += 1
        elif result.changed:
            changed += 1
            if not args.quiet:
                prefix = "[dry-run] " if args.dry_run else ""
                print(f"{prefix}Updated: {result.path}")
        elif not args.quiet:
            print(f"Unchanged: {result.path}")

    # Summary
    if not args.quiet:
        total = len(results)
        print(f"\n{changed}/{total} files {'would be ' if args.dry_run else ''}updated")
        if errors:
            print(f"{errors} errors")

    return 1 if errors else 0


def _run_xref_validate(path: Path, args, config: Config) -> int:
    """Run cross-reference validation on file(s)."""
    mode = args.on_invalid
    auto_fix = not args.no_auto_fix

    if path.is_file():
        results = [
            validate_cross_refs(
                path,
                mode=mode,
                auto_fix_fuzzy=auto_fix,
                dry_run=args.dry_run,
                config=config,
            )
        ]
    else:
        results = validate_directory_cross_refs(
            path,
            mode=mode,
            auto_fix_fuzzy=auto_fix,
            dry_run=args.dry_run,
            recursive=True,
            pattern=args.pattern,
            config=config,
        )

    # Report results
    errors = 0
    total_refs = 0
    total_valid = 0
    total_invalid = 0
    total_fixed = 0
    files_changed = 0

    for result in results:
        if result.error:
            print(f"ERROR: {result.path}: {result.error}", file=sys.stderr)
            errors += 1
            continue

        total_refs += result.refs_found
        total_valid += result.refs_valid
        total_invalid += result.refs_invalid
        total_fixed += result.refs_fixed

        if result.changed:
            files_changed += 1

        if not args.quiet and result.refs_found > 0:
            prefix = "[dry-run] " if args.dry_run else ""
            status = "changed" if result.changed else "ok"
            print(
                f"{prefix}{result.path}: {result.refs_found} refs, "
                f"{result.refs_valid} valid, {result.refs_invalid} invalid, "
                f"{result.refs_fixed} fixed [{status}]"
            )

            # Show invalid refs details
            for v in result.validations:
                if v.status != "valid":
                    if v.status == "file_missing":
                        detail = f"file not found: {v.ref.target_path}"
                    elif v.status == "anchor_missing":
                        detail = f"anchor not found: #{v.ref.target_anchor}"
                    elif v.status == "anchor_fuzzy":
                        detail = (
                            f"anchor fuzzy match: #{v.ref.target_anchor} "
                            f"-> #{v.suggested_anchor} ({v.similarity_score:.0%})"
                        )
                    else:
                        detail = v.status
                    print(f"  L{v.ref.line}: {v.ref.display_text} - {detail}")

    # Summary
    if not args.quiet:
        dry_prefix = "would be " if args.dry_run else ""
        print(f"\nCross-reference validation:")
        print(f"  Files processed: {len(results)}")
        print(f"  Files {dry_prefix}changed: {files_changed}")
        print(f"  Total refs: {total_refs}")
        print(f"  Valid: {total_valid}")
        print(f"  Invalid: {total_invalid}")
        print(f"  Fixed: {total_fixed}")
        if errors:
            print(f"  Errors: {errors}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
