"""The pixel side: shift, global repaint, mask, composite (P1 by construction), numbered regions, explained change."""

from __future__ import annotations

import numpy as np

from clutter_pairs import pairs
from clutter_pairs.domain import Box, RegionItems
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


def _two_patches_and_a_speck() -> np.ndarray:
    mask = np.zeros((100, 100), dtype=bool)
    mask[10:30, 10:30] = True  # 400 px
    mask[60:90, 60:90] = True  # 900 px
    mask[10:13, 90:93] = True  # 9 px: a speck
    return mask


def test_regions_are_grouped_numbered_by_size_and_specks_dropped() -> None:
    mask = _two_patches_and_a_speck()
    mask[32:34, 10:30] = True  # a shadow under the first patch, 2 px away: same region
    found = pairs.regions(mask, Thresholds(region_group_px=3, region_min_px=100))
    assert [(r.n, r.px) for r in found.numbered] == [(1, 900), (2, 440)]
    assert found.numbered[0].box == Box(0.6, 0.6, 0.9, 0.9)
    assert found.speck_px == 9
    assert int(found.labels[11, 11]) == 2 and int(found.labels[11, 91]) == 0


def test_a_region_holding_no_item_is_unexplained() -> None:
    t = Thresholds(region_group_px=3, region_min_px=100, max_speck_share=0.01)
    found = pairs.regions(_two_patches_and_a_speck(), t)
    result = pairs.explain(found, [RegionItems(1, ()), RegionItems(2, (1,))], 2, t)
    assert [(f.code, f.box, f.regions) for f in result.findings] == [("unexplained_change", Box(0.6, 0.6, 0.9, 0.9), (1,))]
    measures = {m.name: m.value for m in result.measures}
    assert abs(measures["unexplained_share"] - 900 / 1309) < 1e-6 and measures["regions"] == 2
    assert measures["regions_unanswered"] == 0 and measures["regions_holding_every_item"] == 0
    assert len(pairs.explain(found, [RegionItems(1, (2,))], 2, t).findings) == 1  # region 2 not answered
    assert len(pairs.explain(found, [RegionItems(1, (2,), answered=False), RegionItems(2, (1,))], 2, t).findings) == 1


def test_a_region_holding_an_item_and_another_change_is_unexplained() -> None:
    """An invented door merged with the coat in front of it: the item does not explain the door."""
    t = Thresholds(region_group_px=3, region_min_px=100, max_speck_share=0.01)
    found = pairs.regions(_two_patches_and_a_speck(), t)
    result = pairs.explain(found, [RegionItems(1, (1,), other_change=True), RegionItems(2, (2,))], 2, t)
    assert [f.regions for f in result.findings] == [(1,)]
    assert pairs.explain(found, [RegionItems(1, (1,)), RegionItems(2, (2,))], 2, t).findings == ()


def test_specks_above_their_share_of_the_mask_are_an_unexplained_change() -> None:
    t = Thresholds(region_group_px=3, region_min_px=100, max_speck_share=0.005)  # the speck is 9 / 1309 = 0.7 %
    found = pairs.regions(_two_patches_and_a_speck(), t)
    result = pairs.explain(found, [RegionItems(1, (1,)), RegionItems(2, (2,))], 2, t)
    assert [(f.code, f.box) for f in result.findings] == [("unexplained_change", None)]


def test_regions_past_the_cap_are_unexplained_and_not_drawn() -> None:
    t = Thresholds(region_group_px=3, region_min_px=100, max_regions=1, max_speck_share=0.01)
    found = pairs.regions(_two_patches_and_a_speck(), t)
    assert len(pairs.explain(found, [RegionItems(1, (1,)), RegionItems(2, (1,))], 1, t).findings) == 1
    cluttered = np.full((100, 100, 3), 128, dtype=np.uint8)
    drawn = pairs.draw_regions(cluttered, found, t)
    assert (drawn[56:94, 56:94] != 128).any() and (drawn[6:34, 6:34] == 128).all()  # region 1 drawn, region 2 not


def test_the_regions_image_outlines_and_numbers_each_region() -> None:
    t = Thresholds(region_group_px=3, region_min_px=100)
    found = pairs.regions(_two_patches_and_a_speck(), t)
    cluttered = np.full((100, 100, 3), 128, dtype=np.uint8)
    drawn = pairs.draw_regions(cluttered, found, t)
    mask = _two_patches_and_a_speck()
    assert (drawn[mask] == 128).all()  # nothing drawn over a pixel of the mask
    assert (drawn[75, 58] == (255, 214, 0)).all()  # the outline of region 1, just outside its left edge
    assert (drawn[40:60, 55:80] == 255).all(axis=-1).any()  # a white digit in the label above region 1
    assert np.array_equal(drawn, pairs.draw_regions(cluttered, found, t))


def test_components_are_eight_connected() -> None:
    mask = np.zeros((6, 6), dtype=bool)
    mask[0, 0] = mask[1, 1] = mask[4, 4] = mask[4, 5] = True
    _, count = pairs.label_components(mask)
    assert count == 2
