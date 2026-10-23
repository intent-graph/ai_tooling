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
    FeatureBackend,
    Fit,
    TranslationBackend,
    box_mean,
    describe_alignment,
    lab,
    measure_structure,
    measure_tone,
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
    assert measures["alignment"] == {"scale": 1.0, "shift_pct": 0.0, "rotation_deg": 0.0, "applied": True,
                                     "method": "translation", "features": None, "matched": None}
    assert measures["tone"] == {"shift_de": 0.0, "shift_lab": [0.0, 0.0, 0.0], "uneven_de": 0.0}


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
    assert summarize(measures).startswith("framing: the best fit is a shift of 15.6%")
    assert "sign" not in summarize(measures)  # a measure, not a reading of it


def test_helpers() -> None:
    assert box_mean(np.ones((5, 7), dtype=np.float32), 2).tolist() == np.ones((5, 7)).tolist()
    cells = np.zeros((6, 6), dtype=bool)
    cells[0:2, 0:2] = True
    cells[4, 4] = True
    assert [len(g) for g in regions(cells, 1)] == [4, 1] and [len(g) for g in regions(cells, 2)] == [4]
    warp = np.array([[1.02, 0.0, 5.12], [0.0, 1.02, 0.0]], dtype=np.float32)
    assert describe_alignment(Fit(warp, "ecc"), 512) == {"scale": 1.02, "shift_pct": 1.0, "rotation_deg": 0.0,
                                                         "applied": True, "method": "ecc", "features": None, "matched": None}
    assert lab(np.array([[[255, 255, 255]]], dtype=np.uint8))[0, 0].round(1).tolist() == [100.0, 0.0, 0.0]


def test_a_failed_fit_is_said_as_such_not_as_no_motion() -> None:
    alignment = describe_alignment(Fit(np.eye(2, 3, dtype=np.float32), "none", 600, 0), 512)
    assert alignment["applied"] is False and alignment["scale"] == 1.0
    measures = {"alignment": alignment, "outside_changed_share": 0.7, "regions": [], "tone": None}
    assert summarize(measures).startswith("framing: no fit found between the two pictures (0 of 600 features")


def test_tone_separates_a_uniform_shift_from_an_uneven_one() -> None:
    keep = ~region()
    base = textured()
    lighter = np.clip(base.astype(int) + 20, 0, 255).astype(np.uint8)
    uniform = measure_tone(base, lighter, keep)
    assert uniform is not None and uniform["shift_de"] > 5 and uniform["uneven_de"] < 1.5
    ramp = np.linspace(0, 60, SIZE)[None, :, None]
    uneven = measure_tone(base, np.clip(base + ramp, 0, 255).astype(np.uint8), keep)
    assert uneven is not None and uneven["uneven_de"] > 3 * uniform["uneven_de"] + 5
    assert "uniform shift of delta E" in summarize(structure(base, lighter))


def photo_like(seed: int, side: int = 384) -> np.ndarray:
    """Smooth random shapes with edges and corners at several scales: features for SIFT, as a room photo has."""
    rng = np.random.default_rng(seed)
    noise = rng.random((side // 16, side // 16)).astype(np.float32)
    coarse = np.asarray(Image.fromarray((noise * 255).astype(np.uint8)).resize((side, side), Image.BICUBIC), dtype=np.float32)
    picture = Image.fromarray(np.clip(coarse, 0, 255).astype(np.uint8)).convert("RGB")
    from PIL import ImageDraw

    draw = ImageDraw.Draw(picture)
    for _ in range(60):
        x, y, w, h = rng.integers(0, side, 2).tolist() + rng.integers(8, side // 5, 2).tolist()
        draw.rectangle((x, y, x + w, y + h), fill=tuple(int(v) for v in rng.integers(0, 255, 3)))
    return np.asarray(picture)


def similarity(image: np.ndarray, scale: float, degrees: float, shift: tuple[float, float]) -> np.ndarray:
    cv2 = pytest.importorskip("cv2")
    h, w = image.shape[:2]
    warp = cv2.getRotationMatrix2D((w / 2, h / 2), degrees, scale)
    warp[:, 2] += shift
    return np.asarray(cv2.warpAffine(image, warp, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT))


def feature_fit(first: np.ndarray, second: np.ndarray) -> dict[str, Any]:
    pytest.importorskip("cv2")
    keep = np.ones(first.shape[:2], dtype=bool)
    keep[120:260, 120:260] = False
    fit = FeatureBackend().estimate(first[..., 0].astype(np.float32), second[..., 0].astype(np.float32), keep)
    return describe_alignment(fit, max(first.shape[:2]))


def test_the_feature_fit_recovers_a_small_reframing() -> None:
    first = photo_like(1)
    alignment = feature_fit(first, similarity(first, 1.03, 1.0, (4.0, -3.0)))
    assert alignment["method"] == "features" and alignment["matched"] >= 12
    assert alignment["scale"] == pytest.approx(1.03, abs=0.005) and abs(alignment["rotation_deg"]) == pytest.approx(1.0, abs=0.1)
    assert alignment["applied"] is True


def test_another_picture_matches_almost_no_feature() -> None:
    alignment = feature_fit(photo_like(1), photo_like(2))
    assert alignment["method"] != "features" and alignment["features"] > 50
    assert alignment["matched"] < 0.05 * alignment["features"]


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
