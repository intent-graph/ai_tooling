"""The zoom judge on stored attempts, in shadow: per judged picture of some runs, the current structure map, its
places, their zooms and one separate judge call; nothing in the runs changes (design/defect_detectors.md)."""

from __future__ import annotations

import sqlite3
import time
from collections.abc import Callable, Sequence
from typing import Any

from virtual_unstaging import detectors, imaging, zoomjudge, zooms
from virtual_unstaging.judge import ContractError
from virtual_unstaging.loop1.runner import Adapters
from virtual_unstaging.store import repo
from virtual_unstaging.store.db import transaction


def ask_zooms(adapters: Adapters, conn: sqlite3.Connection, run_ids: Sequence[int], limit: int | None = None,
              say: Callable[[str], None] = print) -> list[dict[str, Any]]:
    """One zoom judgment per distinct judged picture of the runs; a request the same judge already answered is reused."""
    judge = adapters.judge_model
    with transaction(conn):
        judge_model_id = repo.ensure_model(conn, "judge", judge.name, judge.revision)
    thresholds = detectors.load_thresholds()
    done: list[dict[str, Any]] = []
    for row in repo.judged_candidates(conn, run_ids)[:limit]:
        inputs = [row["original"], row["candidate"], row["region"]]
        structure = _tool(adapters, conn, "structure_map", inputs)
        found = {d.code: d for d in detectors.detect(structure.measures, thresholds)}
        entry: dict[str, Any] = {"attempt": row["attempt"], "bands": {c: d.band for c, d in found.items()}}
        if found["other_picture"].band == detectors.PRESENT:
            say(f"attempt {row['attempt']}: another picture ({found['other_picture'].reason}): no zooms")
            done.append(entry | {"zooms": 0})
            continue
        original = imaging.decode(adapters.blobs.get(row["original"])).convert("RGB")
        candidate = imaging.decode(adapters.blobs.get(row["candidate"]))
        region = imaging.mask_array(adapters.blobs.get(row["region"]), original.size)
        places = zooms.places(structure.measures, region)
        aligned = zooms.aligned_candidate(original, candidate, structure.measures)
        shown = [(p, zooms.render(original, aligned, region, p)) for p in places]
        stored = [(p.where, p.box, _store_image(adapters, conn, data)) for p, data in shown]
        request = zoomjudge.build(judge, shown, adapters.image_part, adapters.text_part, adapters.judge_request)
        reused = repo.find_zoom_judgment(conn, request.request_sha256, judge_model_id)
        if reused is not None:
            say(f"attempt {row['attempt']}: {len(places)} zooms, answered before (zoom judgment {reused})")
            done.append(entry | {"zooms": len(places), "zoom_judgment": reused, "reused": True})
            continue
        for _ in range(2):  # one retry on a broken answer
            started = time.monotonic()
            raw = adapters.chat(request.messages, request.schema)
            wall = time.monotonic() - started
            try:
                answers, error = zoomjudge.parse(raw, places), None
            except ContractError as broken:
                answers, error = (), str(broken)
            with transaction(conn):
                zoom_judgment_id = repo.insert_zoom_judgment(
                    conn, row["attempt"], judge_model_id, structure.tool_run_id, request.request_sha256, raw, error, wall,
                    stored, [(a.n, a.answers, a.severity, a.comment) for a in answers])
            if error is None:
                break
        said = "; ".join(f"{p.where} {', '.join(a.answers)} ({a.severity})" for p, a in zip(places, answers, strict=False))
        say(f"attempt {row['attempt']}: {len(places)} zooms in {wall:.1f} s: {said or error}")
        done.append(entry | {"zooms": len(places), "zoom_judgment": zoom_judgment_id, "seconds": round(wall, 1),
                             "error": error})
    return done


def _tool(adapters: Adapters, conn: sqlite3.Connection, name: str, inputs: list[str]) -> repo.ToolRunRow:
    key = repo.tool_run_key(name, adapters.tools.version(name), {}, inputs)
    found = repo.find_tool_run(conn, key)
    if found:
        return found
    result = adapters.tools.run(name, inputs, {}, adapters.blobs.get)
    outputs = {out: _store_image(adapters, conn, data) for out, data in result.outputs.items()}
    with transaction(conn):
        return repo.insert_tool_run(conn, name, result.version, {}, inputs, outputs, result.measures, result.summary,
                                    result.gpu_seconds)


def _store_image(adapters: Adapters, conn: sqlite3.Connection, data: bytes) -> str:
    sha = adapters.blobs.put(data)
    width, height, media_type = imaging.describe(data)
    with transaction(conn):
        repo.ensure_image(conn, sha, width, height, media_type)
    return sha
