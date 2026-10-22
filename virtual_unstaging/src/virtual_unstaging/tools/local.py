"""Tools the orchestrator runs itself: mask dilation, region outline, a pixel-level change map."""

from __future__ import annotations

from typing import Any

import numpy as np

from virtual_unstaging import imaging
from virtual_unstaging.tools import Fetch, ToolResult

VERSION = "local-1"
VERSIONS = {"change_map": "local-2"}  # a tool whose code changed; the others stay at VERSION
VISIBLE = 10.0  # colour difference (CIE76) counted as a visible change


class LocalTools:
    names = ("mask_ops", "outline", "change_map")

    def version(self, name: str) -> str:
        return VERSIONS.get(name, VERSION)

    def run(self, name: str, inputs: list[str], params: dict[str, Any], fetch: Fetch) -> ToolResult:
        if name == "mask_ops":
            return self._mask_ops(inputs, params, fetch)
        if name == "outline":
            return self._outline(inputs, fetch)
        if name == "change_map":
            return self._change_map(inputs, fetch)
        raise KeyError(f"local tools have no {name!r}")

    def _mask_ops(self, inputs: list[str], params: dict[str, Any], fetch: Fetch) -> ToolResult:
        """Dilate a mask by `dilation_pct` of the image's long side."""
        (mask_sha,) = inputs
        mask = imaging.mask_array(fetch(mask_sha))
        pct = float(params.get("dilation_pct", 0.0))
        radius = round(pct / 100.0 * max(mask.shape))
        dilated = imaging.dilate(mask, radius)
        share = float(dilated.mean())
        return ToolResult(
            "mask_ops", VERSION, {"mask": imaging.mask_png(dilated)},
            {"radius_px": radius, "share": round(share, 4)},
            f"mask dilated by {radius} px; it covers {share:.1%} of the frame",
        )

    def _outline(self, inputs: list[str], fetch: Fetch) -> ToolResult:
        original_sha, mask_sha = inputs
        original = fetch(original_sha)
        width, height, _ = imaging.describe(original)
        mask = imaging.mask_array(fetch(mask_sha), (width, height))
        return ToolResult("outline", VERSION, {"image": imaging.outline(original, mask)})

    def _change_map(self, inputs: list[str], fetch: Fetch) -> ToolResult:
        """Colour difference outside the region, at the original's size: a uniform colour shift (the median Lab difference
        outside the region) measured apart, then the local change left once it is removed, a proxy for drift."""
        original_sha, candidate_sha, region_sha = inputs
        original = fetch(original_sha)
        width, height, _ = imaging.describe(original)
        a = imaging.lab(imaging.rgb_array(original))
        b = imaging.lab(imaging.rgb_array(fetch(candidate_sha), (width, height)))
        region = imaging.mask_array(fetch(region_sha), (width, height))
        difference = b - a
        outside = ~region if (~region).any() else np.ones(region.shape, dtype=bool)
        shift = np.median(difference[outside], axis=0)
        raw = np.linalg.norm(difference, axis=-1)
        local = np.linalg.norm(difference - shift, axis=-1).astype(np.float32)
        shift_size = float(np.linalg.norm(shift))
        median, p95 = float(np.median(local[outside])), float(np.percentile(local[outside], 95))
        changed = float((local[outside] > VISIBLE).mean())
        changed_raw = float((raw[outside] > VISIBLE).mean())
        heat = np.where(region, 0.0, local).astype(np.float32)
        lighter = "lighter" if shift[0] > 0 else "darker"
        summary = (
            f"outside the removal region: a uniform colour shift of {shift_size:.1f} (ΔE76; {lighter} by {abs(float(shift[0])):.1f} "
            f"in lightness); after removing it, {changed:.1%} of those pixels still changed visibly (ΔE > {VISIBLE:.0f}), "
            f"median local difference {median:.1f}, 95th percentile {p95:.1f}"
        )
        measures = {
            "global_shift_delta_e": round(shift_size, 2),
            "global_shift_lab": [round(float(v), 2) for v in shift],
            "median_delta_e": round(median, 2),
            "p95_delta_e": round(p95, 2),
            "share_changed": round(changed, 4),
            "share_changed_before_shift": round(changed_raw, 4),
        }
        return ToolResult("change_map", VERSIONS["change_map"], {"heatmap": imaging.heatmap_png(heat, 30.0)}, measures, summary)
