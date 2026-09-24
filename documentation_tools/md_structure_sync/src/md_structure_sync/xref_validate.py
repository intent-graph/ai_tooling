"""Cross-reference validation for markdown files."""

from pathlib import Path
from typing import Literal

from md_structure_sync.anchors import make_unique_anchors
from md_structure_sync.cross_refs import (
    get_unique_target_paths,
    parse_cross_refs,
    resolve_target_path,
)
from md_structure_sync.fuzzy import find_best_match
from md_structure_sync.models import (
    Config,
    CrossRef,
    CrossRefResult,
    TocSyncState,
    ValidationResult,
)
from md_structure_sync.parse import gather_info
from md_structure_sync.sync import sync_file


def get_file_anchors(path: Path, config: Config) -> list[str]:
    """Extract all valid anchors from a markdown file.

    Returns unique anchors accounting for duplicate titles.
    """
    if not path.exists():
        return []

    try:
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines(keepends=True)
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
    except Exception:
        return []

    info = gather_info(lines, config)

    # Get unique anchors from headers
    titles = [h.title for h in info.headers]
    anchors = make_unique_anchors(titles)

    return anchors


def validate_ref(
    ref: CrossRef,
    source_file: Path,
    target_anchors_cache: dict[Path, list[str]],
    config: Config,
    auto_fix_fuzzy: bool = True,
) -> ValidationResult:
    """Validate a single cross-reference.

    Args:
        ref: The cross-reference to validate
        source_file: Path to the file containing the reference
        target_anchors_cache: Cache of target_path -> list of valid anchors
        config: Configuration
        auto_fix_fuzzy: Whether to suggest fuzzy matches

    Returns:
        ValidationResult with status and optional suggestion
    """
    # Resolve target file path
    if ref.target_path:
        target_path = resolve_target_path(source_file, ref.target_path)
    else:
        # Self-reference
        target_path = source_file.resolve()

    # Check if target file exists
    if not target_path.exists():
        return ValidationResult(
            ref=ref,
            status="file_missing",
        )

    # If no anchor specified, file-only reference is valid
    if not ref.target_anchor:
        return ValidationResult(
            ref=ref,
            status="valid",
        )

    # Get anchors from target file (use cache)
    if target_path not in target_anchors_cache:
        target_anchors_cache[target_path] = get_file_anchors(target_path, config)

    available_anchors = target_anchors_cache[target_path]

    # Exact match
    if ref.target_anchor in available_anchors:
        return ValidationResult(
            ref=ref,
            status="valid",
        )

    # Try fuzzy match
    if auto_fix_fuzzy and available_anchors:
        best_match, score = find_best_match(ref.target_anchor, available_anchors)
        if best_match:
            return ValidationResult(
                ref=ref,
                status="anchor_fuzzy",
                suggested_anchor=best_match,
                similarity_score=score,
            )

    # No match found
    return ValidationResult(
        ref=ref,
        status="anchor_missing",
    )


def _remove_ref_from_line(line: str, ref: CrossRef) -> str:
    """Remove a cross-reference from a line."""
    return line[: ref.col_start] + line[ref.col_end :]


def _add_warning_to_line(line: str, ref: CrossRef, result: ValidationResult) -> str:
    """Add inline warning comment after a reference."""
    if result.status == "file_missing":
        warning = f" <!-- INVALID: file '{ref.target_path}' not found -->"
    elif result.status == "anchor_missing":
        warning = f" <!-- INVALID: anchor '#{ref.target_anchor}' not found -->"
    elif result.status == "anchor_fuzzy":
        warning = (
            f" <!-- INVALID: anchor '#{ref.target_anchor}' not found, "
            f"did you mean '#{result.suggested_anchor}'? -->"
        )
    else:
        return line

    # Insert after the reference
    return line[: ref.col_end] + warning + line[ref.col_end :]


def _fix_fuzzy_ref_in_line(line: str, ref: CrossRef, new_anchor: str) -> str:
    """Replace a fuzzy-matched anchor with the correct one."""
    old_link = ref.full_link
    new_link = f"[{ref.display_text}]({ref.target_path}#{new_anchor})"
    return line.replace(old_link, new_link)


def validate_cross_refs(
    path: Path,
    mode: Literal["remove", "warn"] = "remove",
    auto_fix_fuzzy: bool = True,
    dry_run: bool = False,
    config: Config = None,
    sync_state: TocSyncState = None,
) -> CrossRefResult:
    """Validate cross-references in a markdown file.

    Args:
        path: Path to the markdown file
        mode: "remove" to delete invalid refs, "warn" to add inline comments
        auto_fix_fuzzy: Whether to auto-fix fuzzy anchor matches
        dry_run: If True, don't write changes
        config: Configuration (uses defaults if None)
        sync_state: Shared state for tracking toc_sync status

    Returns:
        CrossRefResult with validation details
    """
    config = config or Config()
    sync_state = sync_state or TocSyncState()

    # Create a config for toc_sync that respects dry_run
    toc_sync_config = Config(
        min_level=config.min_level,
        max_level=config.max_level,
        include_line_comments=config.include_line_comments,
        toc_title=config.toc_title,
        placeholder=config.placeholder,
        dry_run=dry_run,  # Use the xref dry_run setting
    )

    result = CrossRefResult(
        path=path,
        refs_found=0,
        refs_valid=0,
        refs_invalid=0,
        refs_fixed=0,
        changed=False,
    )

    # Check file exists
    if not path.exists():
        result.error = f"File not found: {path}"
        return result

    # Step 1: Ensure source file is toc_synced
    if not sync_state.is_toc_synced(path):
        sync_result = sync_file(path, toc_sync_config)
        sync_state.mark_toc_synced(path)
        if sync_result.error:
            result.error = f"toc_sync failed: {sync_result.error}"
            return result

    # Read current content
    try:
        content = path.read_text(encoding="utf-8")
        lines = content.splitlines(keepends=True)
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
    except Exception as e:
        result.error = str(e)
        return result

    # Step 2: Parse cross-references
    refs = parse_cross_refs(lines, include_self_refs=True)
    result.refs_found = len(refs)

    if not refs:
        return result

    # Step 3: Ensure target files are toc_synced
    target_paths = get_unique_target_paths(path, refs)
    for target_path in target_paths:
        if target_path.exists() and not sync_state.is_toc_synced(target_path):
            sync_file(target_path, toc_sync_config)
            sync_state.mark_toc_synced(target_path)

    # Step 4: Validate each reference
    target_anchors_cache: dict[Path, list[str]] = {}
    validations: list[ValidationResult] = []

    for ref in refs:
        validation = validate_ref(
            ref, path, target_anchors_cache, config, auto_fix_fuzzy
        )
        validations.append(validation)

        if validation.status == "valid":
            result.refs_valid += 1
        else:
            result.refs_invalid += 1

    result.validations = validations

    # Step 5: Apply fixes based on mode
    if result.refs_invalid == 0:
        return result

    # Process invalid refs (bottom-to-top to preserve line numbers)
    modified_lines = lines.copy()
    invalid_validations = [v for v in validations if v.status != "valid"]
    invalid_validations.sort(key=lambda v: (v.ref.line, v.ref.col_start), reverse=True)

    for validation in invalid_validations:
        line_idx = validation.ref.line - 1  # 0-indexed
        old_line = modified_lines[line_idx]

        if mode == "remove":
            if validation.status == "anchor_fuzzy" and auto_fix_fuzzy:
                # Auto-fix fuzzy match
                new_line = _fix_fuzzy_ref_in_line(
                    old_line, validation.ref, validation.suggested_anchor
                )
                result.refs_fixed += 1
            else:
                # Remove the reference
                new_line = _remove_ref_from_line(old_line, validation.ref)
        else:  # warn mode
            if validation.status == "anchor_fuzzy" and auto_fix_fuzzy:
                # Auto-fix fuzzy match (no warning needed)
                new_line = _fix_fuzzy_ref_in_line(
                    old_line, validation.ref, validation.suggested_anchor
                )
                result.refs_fixed += 1
            else:
                # Add warning comment
                new_line = _add_warning_to_line(old_line, validation.ref, validation)

        modified_lines[line_idx] = new_line

    # Check if content changed
    new_content = "".join(modified_lines)
    if new_content != content:
        result.changed = True

        if not dry_run:
            path.write_text(new_content, encoding="utf-8")

            # Mark file as dirty if we removed refs (structure may need re-sync)
            if mode == "remove":
                sync_state.mark_dirty(path)

    return result


def validate_directory_cross_refs(
    directory: Path,
    mode: Literal["remove", "warn"] = "remove",
    auto_fix_fuzzy: bool = True,
    dry_run: bool = False,
    recursive: bool = True,
    pattern: str = "*.md",
    config: Config = None,
) -> list[CrossRefResult]:
    """Validate cross-references in all markdown files in a directory.

    Uses two-phase approach for efficiency:
    1. Phase 1: toc_sync all files
    2. Phase 2: xref_validate all files (skip_toc_sync=True)

    Args:
        directory: Directory to process
        mode: "remove" or "warn"
        auto_fix_fuzzy: Whether to auto-fix fuzzy matches
        dry_run: If True, don't write changes
        recursive: If True, process subdirectories
        pattern: Glob pattern for markdown files
        config: Configuration

    Returns:
        List of CrossRefResult for each file
    """
    config = config or Config()

    # Create a config for toc_sync that respects dry_run
    toc_sync_config = Config(
        min_level=config.min_level,
        max_level=config.max_level,
        include_line_comments=config.include_line_comments,
        toc_title=config.toc_title,
        placeholder=config.placeholder,
        dry_run=dry_run,  # Use the xref dry_run setting
    )

    # Find all markdown files
    if recursive:
        files = list(directory.rglob(pattern))
    else:
        files = list(directory.glob(pattern))

    if not files:
        return []

    # Phase 1: toc_sync all files
    sync_state = TocSyncState()
    for file_path in files:
        sync_file(file_path, toc_sync_config)
        sync_state.mark_toc_synced(file_path)

    # Phase 2: xref_validate all files
    results = []
    for file_path in files:
        result = validate_cross_refs(
            file_path,
            mode=mode,
            auto_fix_fuzzy=auto_fix_fuzzy,
            dry_run=dry_run,
            config=config,
            sync_state=sync_state,
        )
        results.append(result)

    # Phase 3: Re-sync dirty files (if in remove mode)
    if mode == "remove" and not dry_run:
        for dirty_path in list(sync_state.dirty):
            sync_file(dirty_path, toc_sync_config)
            sync_state.clear_dirty(dirty_path)

    return results
