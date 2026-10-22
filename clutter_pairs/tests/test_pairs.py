"""The pixel side: shift, global repaint, mask, composite (P1 by construction), explained change."""

from __future__ import annotations

import numpy as np

from clutter_pairs import pairs
from clutter_pairs.domain import Box
from clutter_pairs.pairs import Thresholds


def _room(seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return np.clip(0.5 + rng.normal(0, 0.05, size=(96, 128, 3)), 0, 1).astype(np.float32)


def test_composite_is_the_clean_image_wherever_alpha_is_zero() -> None:
    clean = _room()
    edit = clean.copy()
    edit[40:70, 30:60] = (0.9, 0.1, 0.1)
    edit += 0.01  # a slight repaint everywhere: the composite must not carry it outside the mask
    prepared = pairs.prepare(clean, np.clip(edit, 0, 1), (0.01, 0.5), Thresholds())
    assert not prepared.result.findings
    out = pairs.composite(clean, prepared.corrected, prepared.alpha)
    outside = prepared.alpha == 0
    assert outside.any() and np.array_equal(out[outside], pairs.to_uint8(clean)[outside])
    assert (prepared.alpha[45:65, 35:55] == 255).all()


def test_shift_and_global_repaint_are_caught_before_any_judge() -> None:
    clean = _room()
    shifted = np.roll(clean, 5, axis=1)
    result = pairs.prepare(clean, shifted, (0.0, 1.0), Thresholds()).result
    assert [f.code for f in result.findings][0] == "misaligned"
    repainted = np.clip(clean * 0.7, 0, 1).astype(np.float32)
    assert "global_repaint" in [f.code for f in pairs.prepare(clean, repainted, (0.0, 1.0), Thresholds()).result.findings]


def test_mask_share_outside_the_density_range_is_off_spec() -> None:
    clean = _room()
    edit = clean.copy()
    edit[40:50, 30:40] = 0.0
    result = pairs.prepare(clean, edit, (0.3, 0.6), Thresholds()).result
    assert [f.code for f in result.findings] == ["clutter_off_spec"]


def test_a_change_outside_every_located_item_is_unexplained() -> None:
    mask = np.zeros((100, 100), dtype=bool)
    mask[10:30, 10:30] = True
    mask[60:90, 60:90] = True
    result = pairs.explain(mask, [Box(0.05, 0.05, 0.35, 0.35)], Thresholds())
    assert [f.code for f in result.findings] == ["unexplained_change"]
    assert abs(result.measures[0].value - 900 / 1300) < 1e-6


def test_components_are_eight_connected() -> None:
    mask = np.zeros((6, 6), dtype=bool)
    mask[0, 0] = mask[1, 1] = mask[4, 4] = mask[4, 5] = True
    _, count = pairs.label_components(mask)
    assert count == 2
