"""Planning: scenes and their clutter specs, sampled into the target cells with the largest shortfall.

A cell's shortfall is its wanted pairs minus the clutter specs that may still become pairs in it (no loop yet, accepted,
or unfinished). Every draw is seeded from the dataset's seed and the scene's ordinal, so planning is reproducible;
nothing already planned is planned again (S2).
"""

from __future__ import annotations

import random
import sqlite3

from clutter_pairs.dataset import Dataset
from clutter_pairs.domain import derive_seed
from clutter_pairs.space import ROOM_TYPE, sample_clutter_specs, sample_values
from clutter_pairs.store import repo

MAX_SCENES_PER_PLAN = 10_000


def plan(conn: sqlite3.Connection, ds: Dataset) -> int:
    """Add scenes until every target's shortfall is covered; returns the number of scenes added. Call in a
    transaction."""
    alive = repo.alive_specs_per_target(conn, ds.target_set_id)
    targets = repo.targets(conn, ds.target_set_id)
    shortfall = {tid: wanted - alive.get(tid, 0) for tid, wanted, _ in targets}
    cells = {tid: dict(cell) for tid, _, cell in targets}
    added = 0
    while any(v > 0 for v in shortfall.values()):
        if added >= MAX_SCENES_PER_PLAN:
            raise RuntimeError("planning does not converge: check the targets")
        tid = max(shortfall, key=lambda t: (shortfall[t], -t))
        cell = cells[tid]
        ordinal = repo.scene_count(conn) + 1
        scene_seed = derive_seed(ds.cfg.seed, "scene", ordinal)
        rng = random.Random(scene_seed)
        room = sample_values(ds.space, "room", cell, rng)
        scene = sample_values(ds.space, "scene", cell, rng)
        specs = sample_clutter_specs(ds.space, room[ROOM_TYPE], scene_seed, ds.cfg.run.variants, cell)
        repo.create_scene(conn, ds.space_version_id, room, scene, scene_seed, specs)
        added += 1
        for other, other_cell in cells.items():
            for _, _, values, _ in specs:
                every = {**room, **scene, **values}
                if all(every.get(axis) == value for axis, value in other_cell.items()):
                    shortfall[other] -= 1
    return added
