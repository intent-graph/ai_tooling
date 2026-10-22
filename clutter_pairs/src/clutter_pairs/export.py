"""Export: a named dataset version as plain files (design/README.md, "Stored data").

`exports/<name>/clean/`, `cluttered/` and `mask/` PNGs, and `manifest.jsonl`, one line per pair. Public ids are
content hashes that survive a rebuild of the store; the split is a property of the building (P6), drawn from the
building's public id. A snapshot: pairs accepted later do not join it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from virtual_unstaging.domain import canonical_json, sha256_bytes, sha256_text

from clutter_pairs.dataset import Dataset
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction, utc_now

SPLITS = (("train", 8), ("validation", 1), ("test", 1))  # tenths of the buildings, by their public id


def split_of(building_public_id: str) -> str:
    slot = int(building_public_id[:8], 16) % sum(n for _, n in SPLITS)
    for name, share in SPLITS:
        if slot < share:
            return name
        slot -= share
    raise AssertionError("unreachable")


def export(ds: Dataset, name: str) -> tuple[Path, int]:
    conn = ds.conn
    if not name.replace("_", "").replace("-", "").isalnum():
        raise ValueError("an export name holds letters, digits, '-' and '_' only")
    if repo.export_exists(conn, name):
        raise ValueError(f"export {name} exists: exports are snapshots, choose another name")
    target = ds.folder / "exports" / name
    if target.exists():
        raise ValueError(f"{target} exists")
    pairs = repo.query(conn, "pair")
    scenes: dict[int, str] = {}
    rooms: dict[int, list[str]] = {}
    buildings: dict[int, list[str]] = {}
    for p in pairs:
        scene = repo.scene(conn, int(p["scene_id"]))  # type: ignore[call-overload]
        scenes[scene.id] = sha256_text(canonical_json({"values": sorted(scene.values), "seed": scene.seed}))
        rooms.setdefault(scene.room_id, [])
        if scenes[scene.id] not in rooms[scene.room_id]:
            rooms[scene.room_id].append(scenes[scene.id])
    room_ids = {}
    for p in pairs:
        scene = repo.scene(conn, int(p["scene_id"]))  # type: ignore[call-overload]
        room_values = [v for v in scene.values if v[0] in ds.space.axes_for("room")]
        room_ids[scene.room_id] = sha256_text(canonical_json({"values": sorted(room_values),
                                                              "scenes": sorted(rooms[scene.room_id])}))
        buildings.setdefault(scene.building_id, [])
        if room_ids[scene.room_id] not in buildings[scene.building_id]:
            buildings[scene.building_id].append(room_ids[scene.room_id])
    building_ids = {b: sha256_text(canonical_json({"rooms": sorted(r)})) for b, r in buildings.items()}
    splits = {b: split_of(public) for b, public in building_ids.items()}
    lines: list[str] = []
    for folder in ("clean", "cluttered", "mask"):
        (target / folder).mkdir(parents=True, exist_ok=False)
    for p in pairs:
        line = _manifest_line(conn, ds, p, scenes, room_ids, building_ids, splits)
        for folder, column in (("clean", "clean_image"), ("cluttered", "cluttered_image"), ("mask", "mask_image")):
            (target / folder / f"{line['pair']}.png").write_bytes(ds.blobs.get(str(p[column])))
        lines.append(json.dumps(line, sort_keys=True, ensure_ascii=False))
    manifest = ("\n".join(lines) + "\n").encode("utf-8") if lines else b""
    (target / "manifest.jsonl").write_bytes(manifest)
    with transaction(conn):
        repo.create_export(conn, name, utc_now(), sha256_bytes(manifest), splits, [int(p["pair_id"]) for p in pairs])  # type: ignore[call-overload]
    return target, len(pairs)


def _manifest_line(conn: Any, ds: Dataset, p: dict[str, Any], scenes: dict[int, str], rooms: dict[int, str],
                   buildings: dict[int, str], splits: dict[int, str]) -> dict[str, Any]:
    pair_public = sha256_text(f"{p['clean_image']}:{p['cluttered_image']}")
    spec = repo.clutter_spec(conn, int(p["clutter_spec_id"]))
    clean_model = repo.model_by_id(conn, int(p["clean_model_id"]))
    editor = repo.model_by_id(conn, int(p["editor_model_id"]))
    measures = {m.name: m.value for a in repo.assessments(conn, int(p["pair_id"])) for m in a.measures}
    iterations = len(repo.iterations(conn, int(p["loop_run_id"])))
    return {
        "pair": pair_public, "scene": scenes[int(p["scene_id"])], "room": rooms[int(p["room_id"])],
        "building": buildings[int(p["building_id"])], "split": splits[int(p["building_id"])],
        "clean": f"clean/{pair_public}.png", "cluttered": f"cluttered/{pair_public}.png", "mask": f"mask/{pair_public}.png",
        "values": dict(repo.pair_values(conn, int(p["pair_id"]))),
        "items": [dict(item) for item in spec.items],
        "models": {"clean": {"name": clean_model.name, "revision": clean_model.revision, "family": clean_model.family,
                             "licence": clean_model.licence},
                   "editor": {"name": editor.name, "revision": editor.revision, "family": editor.family,
                              "licence": editor.licence}},
        "checks": {"clutter_iterations": iterations,
                   "mask_share": measures.get("mask_share_min"), "unexplained_share": measures.get("unexplained_share"),
                   "shift_px": measures.get("shift_px"), "global_delta_e": measures.get("global_delta_e")},
    }
