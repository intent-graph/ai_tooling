"""Shared steps of the integration tests: open, plan and run a dataset on the fake model server."""

from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image

from clutter_pairs import config, importer, plan, run
from clutter_pairs.dataset import Dataset, open_dataset
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction


def run_dataset(folder: Path, smoke: bool = False, deadline: datetime | None = None) -> tuple[Dataset, run.RunSummary]:
    ds = open_dataset(folder)
    with transaction(ds.conn):
        plan.plan(ds.conn, ds)
    thresholds = config.thresholds(ds.cfg, repo.threshold_decisions(ds.conn))
    options = run.RunOptions(smoke=smoke, deadline=deadline, replan=lambda conn: plan.plan(conn, ds))
    return ds, run.execute(ds, run.connect_models(ds, retries=0), thresholds, options)


def make_import_set(folder: Path, entries: Sequence[tuple[str, str, bool]], size: tuple[int, int] = (400, 300),
                    source: dict[str, str] | None = None, extra: dict[str, dict[str, Any]] | None = None,
                    indices: Sequence[int] | None = None) -> Path:
    """An import set of generated images: (file, room type, whether the stand-in judge accepts it: its marker block).
    Each image is drawn from its index (the entry's rank unless `indices` gives it): two sets share an image by
    sharing an index. `extra` adds keys to a file's manifest line."""
    folder.mkdir(parents=True, exist_ok=True)
    origin = source or {"name": "render-tool", "revision": "1.0", "family": "procedural", "licence": "MIT"}
    lines = []
    for rank, (name, room_type, accepted) in enumerate(entries):
        index = rank if indices is None else indices[rank]
        rng = np.random.default_rng(index)
        pixels = np.clip(rng.uniform(0.3, 0.8, size=3) + rng.normal(0, 0.02, size=(size[1], size[0], 3)), 0, 1)
        out = (pixels * 255).astype(np.uint8)
        if accepted:
            out[:64, :64] = 255  # the stand-in clean judge accepts an image whose corner is white
        Image.fromarray(out).save(folder / name)
        lines.append(json.dumps({"file": name, "room_type": room_type, "source": origin,
                                 "origin": f"seed {index}", **(extra or {}).get(name, {})}))
    (folder / "manifest.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return folder


def run_imports(folder: Path, import_set: Path, smoke: bool = False) -> tuple[Dataset, run.RunSummary]:
    """Open a dataset, import a set, run only what the import made (no top-up of generated scenes)."""
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    thresholds = config.thresholds(ds.cfg, repo.threshold_decisions(ds.conn))
    return ds, run.execute(ds, run.connect_models(ds, retries=0), thresholds, run.RunOptions(smoke=smoke))
