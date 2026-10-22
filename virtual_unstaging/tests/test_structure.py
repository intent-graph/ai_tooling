"""The structure map: alignment of a small reframing, structural change robust to small shifts and tone, regions only
outside the removal region, and the judge reading it in place of the colour change map."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pytest
from fastapi.testclient import TestClient
from PIL import Image
from test_loop1 import api_run
from test_serve import AUTH, make_app, mask_png, png, put, run_tool

from virtual_unstaging.clients.fakes import FakeChat
from virtual_unstaging.serve.tools.structure import (
    TranslationBackend,
    box_mean,
    describe_alignment,
    measure_structure,
    regions,
    summarize,
)

SIZE = 128


def textured(seed: int = 0) -> np.ndarray:
    """A room-like picture with structure everywhere: blocks of random grey with edges."""
    rng = np.random.default_rng(seed)
    blocks = rng.integers(40, 220, size=(16, 16, 1)).astype(np.uint8)
    pixels = np.kron(blocks, np.ones((8, 8, 1), dtype=np.uint8)).repeat(3, axis=2)
    return np.asarray(pixels, dtype=np.uint8)


def region() -> np.ndarray:
    mask = np.zeros((SIZE, SIZE), dtype=bool)
    mask[40:88, 40:88] = True
    return mask


def structure(first: np.ndarray, second: np.ndarray, **kw: float) -> Any:
    params = {"margin": 0.03, "threshold": 0.45, "search": 0.02} | kw
    return measure_structure(Image.fromarray(first), Image.fromarray(second), region(), params["margin"],
                             params["threshold"], params["search"], TranslationBackend()).measures


def test_the_same_picture_has_no_change() -> None:
    measures = structure(textured(), textured())
    assert measures["regions"] == [] and measures["outside_changed_share"] == 0.0
    assert measures["alignment"] == {"scale": 1.0, "shift_pct": 0.0, "rotation_deg": 0.0, "applied": True}


def test_a_change_outside_the_region_is_one_region_with_its_box() -> None:
    changed = textured()
    changed[0:24, 96:128] = textured(seed=7)[0:24, 96:128]  # new structure in the top right corner
    measures = structure(textured(), changed)
    assert len(measures["regions"]) == 1
    x0, y0, x1, y1 = measures["regions"][0]["box"]
    assert x0 >= 0.7 and y1 <= 0.25 and x1 == 1.0 and y0 == 0.0
    assert "the structure changed in 1 place" in summarize(measures)


def test_tone_and_a_small_shift_are_not_changes() -> None:
    lighter = np.clip(textured().astype(int) + 18, 0, 255).astype(np.uint8)
    assert structure(textured(), lighter)["regions"] == []
    shifted = np.roll(textured(), 2, axis=1)
    measures = structure(textured(), shifted, search=0.0)  # no local search: the alignment absorbs the shift
    assert measures["regions"] == [] and measures["alignment"]["applied"] is True
    assert measures["alignment"]["shift_pct"] == pytest.approx(100 * 2 / SIZE, abs=0.01)


def test_a_change_inside_the_region_is_not_reported() -> None:
    emptied = textured()
    emptied[44:84, 44:84] = 128
    assert structure(textured(), emptied)["regions"] == []


def test_a_large_reframing_is_reported_and_not_corrected() -> None:
    moved = np.roll(textured(), 20, axis=1)  # 15% of the long side
    measures = structure(textured(), moved)
    assert measures["alignment"]["applied"] is False and measures["regions"]
    assert summarize(measures).startswith("framing differs")


def test_helpers() -> None:
    assert box_mean(np.ones((5, 7), dtype=np.float32), 2).tolist() == np.ones((5, 7)).tolist()
    cells = np.zeros((6, 6), dtype=bool)
    cells[0:2, 0:2] = True
    cells[4, 4] = True
    assert [len(g) for g in regions(cells, 1)] == [4, 1] and [len(g) for g in regions(cells, 2)] == [4]
    warp = np.array([[1.02, 0.0, 5.12], [0.0, 1.02, 0.0]], dtype=np.float32)
    assert describe_alignment(warp, 512) == {"scale": 1.02, "shift_pct": 1.0, "rotation_deg": 0.0, "applied": True}


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    return TestClient(make_app(tmp_path), headers=AUTH)


def test_structure_map_on_the_tool_server(client: TestClient) -> None:
    changed = textured()
    changed[0:24, 96:128] = textured(seed=7)[0:24, 96:128]
    shas = [put(client, png(textured())), put(client, png(changed)), put(client, mask_png(SIZE, SIZE, slice(40, 88), slice(40, 88)))]
    reply = run_tool(client, "structure_map", shas)
    assert reply.status_code == 200, reply.text
    body = reply.json()
    assert set(body["outputs"]) == {"changes"} and len(body["measures"]["regions"]) == 1
    assert body["measures"]["compared_at"] == [SIZE, SIZE] and body["measures"]["candidate_resized"] is False
    for params in ({"threshold": 2}, {"search": -1}, {"unknown": 1}):
        assert run_tool(client, "structure_map", shas, params).status_code == 400


def test_the_judge_reads_the_structure_map_unless_the_project_turns_it_off(project: Path) -> None:
    sent: list[Any] = []
    fake = FakeChat()

    def chat(messages: list[dict[str, object]], schema: dict[str, object]) -> str:
        sent.append(messages)
        return fake(messages, schema)

    api_run(project, "single", chat=chat)
    texts = [p["text"] for p in sent[0][1]["content"] if p["type"] == "text"]
    assert "- structure_map: framing" in texts[-1] and any("outlined in red" in t for t in texts)
    text = (project / "project.toml").read_text(encoding="utf-8").replace("structure_map = true", "structure_map = false")
    (project / "project.toml").write_text(text, encoding="utf-8")
    sent.clear()
    api_run(project, "single", chat=chat)
    texts = [p["text"] for p in sent[0][1]["content"] if p["type"] == "text"]
    assert "- change_map: outside the removal region" in texts[-1]
