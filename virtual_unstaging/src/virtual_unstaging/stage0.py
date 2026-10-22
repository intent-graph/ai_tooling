"""Stage 0, preparation: removal and protected masks per photo, from files or from segmentation, with the
measures stage 0 records (mask share, sharpness). Filtering by those measures comes in a later slice."""

from __future__ import annotations

import sqlite3
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import numpy as np

from virtual_unstaging import imaging
from virtual_unstaging.store import repo
from virtual_unstaging.store.blobs import BlobStore
from virtual_unstaging.store.db import transaction
from virtual_unstaging.tools import ToolBox

MASK_SUFFIXES = (".png", ".jpg", ".jpeg")


def sharpness(data: bytes) -> float:
    """Variance of the Laplacian on the image brought to 1024 px: low means blur or darkness."""
    image = imaging.decode(data).convert("L")
    image.thumbnail((1024, 1024))
    a = np.asarray(image, dtype=np.float32)
    lap = -4 * a[1:-1, 1:-1] + a[:-2, 1:-1] + a[2:, 1:-1] + a[1:-1, :-2] + a[1:-1, 2:]
    return float(lap.var())


def store_image(conn: sqlite3.Connection, blobs: BlobStore, data: bytes) -> str:
    sha = blobs.put(data)
    width, height, media_type = imaging.describe(data)
    with transaction(conn):
        repo.ensure_image(conn, sha, width, height, media_type)
    return sha


def import_masks(
    conn: sqlite3.Connection,
    blobs: BlobStore,
    rule_set_id: int,
    removal_dir: Path,
    protected_dir: Path | None = None,
    names: Sequence[str] | None = None,
) -> dict[str, str]:
    """Attach mask files to photos by file stem (`photo.jpg` <- `photo.png`). Returns photo -> outcome."""
    outcomes: dict[str, str] = {}
    for photo in repo.photos(conn, names):
        stem = Path(photo.source_name).stem
        removal = _find(removal_dir, stem)
        if removal is None:
            outcomes[photo.source_name] = "no mask file"
            continue
        removal_run = _import_mask(conn, blobs, removal, (photo.width, photo.height))
        protected_run = None
        if protected_dir is not None:
            protected = _find(protected_dir, stem)
            if protected is not None:
                protected_run = _import_mask(conn, blobs, protected, (photo.width, photo.height))
        measures = _measures(blobs, photo.image_sha256, removal_run)
        decision, reason = ("attempt", None) if measures["mask_share"] > 0.0 else ("skip", "nothing_to_remove")
        with transaction(conn):
            repo.set_eligibility(
                conn, photo.photo_id, rule_set_id, decision, reason, measures, removal_run.tool_run_id,
                protected_run.tool_run_id if protected_run else None,
            )
        outcomes[photo.source_name] = reason or f"mask covers {measures['mask_share']:.1%}"
    return outcomes


def segment(
    conn: sqlite3.Connection,
    blobs: BlobStore,
    tools: ToolBox,
    rule_set_id: int,
    names: Sequence[str] | None = None,
    threshold: float = 0.3,
) -> dict[str, str]:
    """Masks from the tool server's `segment_elements`: movable elements to remove, fixed elements to protect."""
    outcomes: dict[str, str] = {}
    for photo in repo.photos(conn, names):
        fixed, movable = repo.rules_for(conn, rule_set_id, photo.group_id)
        if not movable:
            outcomes[photo.source_name] = "no movable elements in the rules"
            continue
        removal = _tool(conn, blobs, tools, "segment_elements", [photo.image_sha256], {"labels": movable, "threshold": threshold})
        protected = None
        visible: list[str] = []
        if fixed:
            protected = _tool(conn, blobs, tools, "segment_elements", [photo.image_sha256], {"labels": fixed, "threshold": threshold})
            found = protected.measures.get("found", {})
            visible = [label for label in fixed if isinstance(found, dict) and float(found.get(label, 0.0)) > 0.0]
        measures = {**_measures(blobs, photo.image_sha256, removal), "fixed_visible": visible}
        decision, reason = ("attempt", None) if measures["mask_share"] > 0.0 else ("skip", "nothing_to_remove")
        with transaction(conn):
            repo.set_eligibility(
                conn, photo.photo_id, rule_set_id, decision, reason, measures, removal.tool_run_id,
                protected.tool_run_id if protected else None,
            )
        outcomes[photo.source_name] = reason or f"mask covers {measures['mask_share']:.1%}"
    return outcomes


def _find(directory: Path, stem: str) -> Path | None:
    for suffix in MASK_SUFFIXES:
        candidate = directory / f"{stem}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def _import_mask(conn: sqlite3.Connection, blobs: BlobStore, path: Path, size: tuple[int, int]) -> repo.ToolRunRow:
    mask = imaging.mask_array(path.read_bytes(), size)
    sha = store_image(conn, blobs, imaging.mask_png(mask))
    with transaction(conn):
        # the content's hash is in the key: a corrected mask under the same file name is a new tool run
        return repo.insert_tool_run(
            conn, "import", "1", {"file": path.name, "sha256": sha}, [], {"mask": sha}, {"share": float(mask.mean())}, "", 0.0
        )


def _tool(
    conn: sqlite3.Connection, blobs: BlobStore, tools: ToolBox, name: str, inputs: list[str], params: dict[str, Any]
) -> repo.ToolRunRow:
    key = repo.tool_run_key(name, tools.version(name), params, inputs)
    found = repo.find_tool_run(conn, key)
    if found:
        return found
    result = tools.run(name, inputs, params, blobs.get)
    outputs = {out: store_image(conn, blobs, data) for out, data in result.outputs.items()}
    with transaction(conn):
        return repo.insert_tool_run(
            conn, name, result.version, params, inputs, outputs, result.measures, result.summary, result.gpu_seconds
        )


def _measures(blobs: BlobStore, photo_sha: str, removal: repo.ToolRunRow) -> dict[str, Any]:
    mask = imaging.mask_array(blobs.get(removal.outputs["mask"]))
    return {"mask_share": round(float(mask.mean()), 4), "sharpness": round(sharpness(blobs.get(photo_sha)), 1)}
