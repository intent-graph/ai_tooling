"""The zoom judge in shadow: schema migration with a backup, places and their crops, the candidate aligned by the
structure map's warp, the closed-question contract, and the command on stored attempts."""

from __future__ import annotations

import io
import json
import sqlite3
from dataclasses import replace
from importlib import resources
from pathlib import Path
from typing import Any

import numpy as np
import pytest
from PIL import Image
from test_loop1 import api_run

from virtual_unstaging import config, zoomjudge, zooms
from virtual_unstaging.cli import _adapters, main
from virtual_unstaging.domain import JudgeRequestOptions, ModelRef
from virtual_unstaging.judge import ContractError
from virtual_unstaging.loop1.zoomrun import ask_zooms
from virtual_unstaging.store.db import SCHEMA_VERSION, connect, create_schema
from virtual_unstaging.zooms import INSIDE, OUTSIDE, Place


def test_a_version_1_database_is_migrated_after_a_copy(tmp_path: Path) -> None:
    path = tmp_path / "project.sqlite"
    conn = connect(path)
    v1 = resources.files("virtual_unstaging.store").joinpath("schema.sql").read_text(encoding="utf-8")
    conn.executescript("BEGIN;\n" + v1 + "\nPRAGMA user_version = 1;\nCOMMIT;")
    conn.execute("INSERT INTO model (role, name, revision) VALUES ('judge', 'j', '1')")
    create_schema(conn, backup=path)
    assert conn.execute("PRAGMA user_version").fetchone()[0] == SCHEMA_VERSION == 2
    assert conn.execute("SELECT COUNT(*) FROM zoom_answer").fetchone()[0] == 0
    copy = sqlite3.connect(tmp_path / "project.sqlite.v1.bak")
    assert copy.execute("PRAGMA user_version").fetchone()[0] == 1
    assert copy.execute("SELECT name FROM model").fetchone()[0] == "j"
    create_schema(conn, backup=path)  # already current: nothing happens


def test_places_are_the_changed_regions_then_the_removal_areas_parts() -> None:
    region = np.zeros((200, 300), dtype=bool)
    region[20:120, 20:120] = True  # the larger part
    region[150:180, 200:260] = True
    measures = {"regions": [{"box": [0.8, 0.1, 0.9, 0.2], "share": 0.01}] * 6}
    found = zooms.places(measures, region)
    assert [p.where for p in found] == [OUTSIDE] * 4 + [INSIDE] * 2
    x0, y0, x1, y1 = found[4].box
    assert (x0, y0) == pytest.approx((20 / 300, 20 / 200), abs=0.01) and (x1, y1) == pytest.approx((0.4, 0.6), abs=0.01)


def test_an_outside_crop_is_grown_by_the_places_size_and_square() -> None:
    assert zooms.crop_box(Place(OUTSIDE, (0.3, 0.4, 0.5, 0.45)), (1000, 1000)) == (100, 125, 700, 725)
    assert zooms.crop_box(Place(OUTSIDE, (0.0, 0.0, 0.01, 0.01)), (1000, 800)) == (0, 0, 185, 184)  # MIN_SIDE grown, clipped


def textured(size: tuple[int, int] = (256, 192), seed: int = 0) -> Image.Image:
    rng = np.random.default_rng(seed)
    blocks = rng.integers(30, 230, size=(size[1] // 8, size[0] // 8, 3)).astype(np.uint8)
    return Image.fromarray(np.kron(blocks, np.ones((8, 8, 1), dtype=np.uint8)))


def test_the_candidate_is_aligned_by_the_warp_at_full_resolution() -> None:
    original = textured()
    shifted = Image.fromarray(np.roll(np.asarray(original), 8, axis=1))  # the candidate: moved 8 px right
    measures = {"alignment": {"applied": True}, "compared_at": [128, 96], "warp": [[1, 0, 4], [0, 1, 0]]}  # 4 px at half
    aligned = np.asarray(zooms.aligned_candidate(original, shifted, measures), dtype=int)
    assert np.abs(aligned[:, 16:-16] - np.asarray(original, dtype=int)[:, 16:-16]).mean() < 1
    unapplied = zooms.aligned_candidate(original, shifted, {**measures, "alignment": {"applied": False}})
    assert np.array_equal(np.asarray(unapplied), np.asarray(shifted))


def test_a_zoom_is_the_two_crops_side_by_side() -> None:
    original = textured()
    region = np.zeros((192, 256), dtype=bool)
    region[40:100, 40:120] = True
    image = Image.open(io.BytesIO(zooms.render(original, original, region, Place(INSIDE, (40 / 256, 40 / 192, 120 / 256, 100 / 192)))))
    assert image.width == 2 * max(image.size[1], (image.width - zooms.GAP) // 2) + zooms.GAP
    assert max(image.size) == 2 * zooms.CROP_SIDE + zooms.GAP or image.height == zooms.CROP_SIDE
    pixels = np.asarray(image.convert("RGB"))
    assert ((pixels == (255, 0, 255)).all(axis=-1)).any()  # the removal area outlined


PLACES = (Place(OUTSIDE, (0.1, 0.1, 0.2, 0.2)), Place(INSIDE, (0.3, 0.3, 0.7, 0.8)))


def answer(*items: dict[str, Any]) -> str:
    return json.dumps({f"zoom_{n}": item for n, item in enumerate(items, start=1)})


def item(answers: list[str], severity: str = "none", comment: str = "") -> dict[str, Any]:
    return {"answers": answers, "severity": severity, "comment": comment}


def test_the_contract_takes_each_zoom_with_answers_of_its_kind() -> None:
    parsed = zoomjudge.parse(answer(item(["added", "changed_shape", "added"], "minor", "a bin"), item(["continues"])), PLACES)
    assert [(a.n, a.answers, a.severity) for a in parsed] == [(1, ("added", "changed_shape"), "minor"), (2, ("continues",), "none")]
    for bad in (answer(item(["continues"]), item(["continues"])),  # an inside answer to an outside zoom
                answer(item(["same"])),  # zoom 2 missing
                answer(item([]), item(["continues"])),  # no answer
                "not json"):
        with pytest.raises(ContractError):
            zoomjudge.parse(bad, PLACES)
    schema = zoomjudge.output_schema(PLACES)
    properties: Any = schema["properties"]
    assert schema["required"] == ["zoom_1", "zoom_2"]
    assert properties["zoom_1"]["properties"]["answers"]["items"]["enum"] == list(zoomjudge.ANSWERS[OUTSIDE])
    assert "uniqueItems" not in json.dumps(schema)  # refused by the judge server's grammar backend


def test_the_request_names_each_zoom_and_its_kind() -> None:
    request = zoomjudge.build(ModelRef("j", "1"), [(p, textured_png()) for p in PLACES],
                              lambda data, kind: {"type": "image", "bytes": len(data)}, lambda t: {"type": "text", "text": t},
                              JudgeRequestOptions())
    texts = [part["text"] for part in request.messages[1]["content"] if part["type"] == "text"]  # type: ignore[index, union-attr]
    assert texts[:2] == ["Zoom 1 (outside): original left, edited right.", "Zoom 2 (inside): original left, edited right."]
    assert "inside" in str(request.messages[0]["content"])


def textured_png() -> bytes:
    buffer = io.BytesIO()
    textured().save(buffer, format="PNG")
    return buffer.getvalue()


def zoom_chat(messages: list[dict[str, object]], schema: dict[str, object]) -> str:
    """A judge that answers every zoom as unchanged."""
    texts = [p["text"] for p in messages[1]["content"] if p["type"] == "text"]  # type: ignore[index, union-attr, attr-defined]
    kinds = [t.split("(")[1].split(")")[0] for t in texts if t.startswith("Zoom ")]
    return answer(*(item(["same" if k == OUTSIDE else "continues"]) for k in kinds))


def test_the_command_asks_once_per_picture_and_reuses_an_answered_request(project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    run, _ = api_run(project, "single")
    adapters = replace(_adapters(project, config.load(project)), chat=zoom_chat)
    conn = connect(project / "project.sqlite")
    done = ask_zooms(adapters, conn, [run], say=lambda _: None)
    pictures = conn.execute("SELECT COUNT(DISTINCT attempt_id) FROM zoom_judgment").fetchone()[0]
    assert len(done) == pictures > 0 and all(d["zooms"] >= 1 and d["error"] is None for d in done)
    assert conn.execute("SELECT COUNT(*) FROM zoom_answer WHERE answer = 'continues'").fetchone()[0] >= pictures
    again = ask_zooms(adapters, conn, [run], say=lambda _: None)
    assert all(d.get("reused") for d in again)
    assert main(["--project", str(project), "zooms", str(run), "--limit", "1"]) == 0
    assert "1 pictures" in capsys.readouterr().out


def test_the_command_needs_no_generator(project: Path, monkeypatch: pytest.MonkeyPatch,
                                         capsys: pytest.CaptureFixture[str]) -> None:
    run, _ = api_run(project, "single")

    def no_generator(cfg: object) -> object:
        raise config.ConfigError("the tool server serves no generator")

    monkeypatch.setattr("virtual_unstaging.cli._generator", no_generator)
    assert main(["--project", str(project), "zooms", str(run), "--limit", "1"]) == 0
    assert "1 pictures" in capsys.readouterr().out
