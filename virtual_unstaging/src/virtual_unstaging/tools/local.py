"""Tools the orchestrator runs itself: mask dilation, region outline, a pixel-level change map."""

from __future__ import annotations

from typing import Any

import numpy as np

from virtual_unstaging import imaging
from virtual_unstaging.tools import Fetch, ToolResult

VERSION = "local-1"


class LocalTools:
    names = ("mask_ops", "outline", "change_map")

    def version(self, name: str) -> str:
        return VERSION

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
        """Colour difference outside the region, at the original's size: a proxy for drift and colour shift."""
        original_sha, candidate_sha, region_sha = inputs
        original = fetch(original_sha)
        width, height, _ = imaging.describe(original)
        a = imaging.rgb_array(original)
        b = imaging.rgb_array(fetch(candidate_sha), (width, height))
        region = imaging.mask_array(fetch(region_sha), (width, height))
        delta = imaging.delta_e76(a, b)
        outside = delta[~region] if (~region).any() else np.zeros(1, dtype=np.float32)
        median = float(np.median(outside))
        p95 = float(np.percentile(outside, 95))
        changed = float((outside > 10.0).mean())
        heat = np.where(region, 0.0, delta).astype(np.float32)
        summary = (
            f"outside the removal region: median colour difference {median:.1f} (ΔE76), 95th percentile {p95:.1f}; "
            f"{changed:.1%} of those pixels changed visibly (ΔE > 10)"
        )
        measures = {"median_delta_e": round(median, 2), "p95_delta_e": round(p95, 2), "share_changed": round(changed, 4)}
        return ToolResult("change_map", VERSION, {"heatmap": imaging.heatmap_png(heat, 30.0)}, measures, summary)
