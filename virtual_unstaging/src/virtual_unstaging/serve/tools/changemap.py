"""`change_map`: how far and how much the picture moved and changed colour outside the edited region."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

import numpy as np
from numpy.typing import NDArray
from PIL import Image

from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.pixels import BoolArray, FloatArray, delta_e76, dilate_square, grey, heat_colours
from virtual_unstaging.serve.tools.base import (
    IMAGE,
    MASK,
    Backend,
    ServerTool,
    ToolOutput,
    number_param,
    refuse_unknown,
)

WORK_SIDE = 1024  # long side the flow is computed at; displacements are reported in % of this side
DEFAULT_MARGIN = 0.02  # fraction of the long side kept clear around the region (blurred edges of the edit)
FULL_DISPLACEMENT = 0.01  # displacement, as a fraction of the long side, drawn as fully red
FULL_DELTA_E = 10.0  # colour difference drawn as fully red
LEGEND = {
    "red": "the larger of: displacement of 1% of the long side, colour difference of 10 (CIE76)",
    "dark grey": "no change",
    "blue-grey": "the removal region and its margin, not measured",
}


class FlowBackend(Backend):
    @abstractmethod
    def flow(self, first: FloatArray, second: FloatArray) -> NDArray[np.float32]:
        """Dense optical flow from `first` to `second` (grey, 0-255): shape (H, W, 2), x then y, in pixels."""


class FarnebackBackend(FlowBackend):
    """Farneback dense optical flow from OpenCV."""

    ident: ClassVar[str] = "opencv-farneback"
    model: ClassVar[str] = "OpenCV calcOpticalFlowFarneback (no learned model)"

    def load(self) -> None:
        import cv2  # noqa: F401  (fail at warm-up, not at the first call)

    def flow(self, first: FloatArray, second: FloatArray) -> NDArray[np.float32]:
        self.warm()
        import cv2

        no_initial_flow: Any = None
        result = cv2.calcOpticalFlowFarneback(
            first.astype(np.uint8), second.astype(np.uint8), no_initial_flow, 0.5, 5, 25, 5, 7, 1.5, 0
        )
        return np.asarray(result, dtype=np.float32)


class PhaseCorrelationBackend(FlowBackend):
    """A stand-in with no OpenCV: one global shift for the whole frame, found by phase correlation."""

    ident: ClassVar[str] = "phase-correlation"
    model: ClassVar[str] = "none (test double: a single global shift by FFT phase correlation)"

    def load(self) -> None:
        return None

    def flow(self, first: FloatArray, second: FloatArray) -> NDArray[np.float32]:
        a, b = first - first.mean(), second - second.mean()
        cross = np.fft.fft2(b) * np.conj(np.fft.fft2(a))
        cross /= np.abs(cross) + 1e-9
        correlation = np.fft.ifft2(cross).real
        peak_y, peak_x = (int(v) for v in np.unravel_index(int(np.argmax(correlation)), correlation.shape))
        height, width = correlation.shape
        shift_y = peak_y - height if peak_y > height // 2 else peak_y
        shift_x = peak_x - width if peak_x > width // 2 else peak_x
        flow = np.zeros((height, width, 2), dtype=np.float32)
        flow[..., 0], flow[..., 1] = shift_x, shift_y
        return flow


@dataclass(frozen=True)
class Change:
    measures: dict[str, Any]
    heat: Image.Image


def measure_change(
    original: Image.Image, candidate: Image.Image, region: BoolArray, margin: float, backend: FlowBackend
) -> Change:
    """Pure core of `change_map`: both pictures and the region are at one size; the region's margin is left out."""
    first, second = np.asarray(original.convert("RGB")), np.asarray(candidate.convert("RGB"))
    long_side = max(region.shape)
    margin_px = round(margin * long_side)
    clear = ~dilate_square(region, margin_px)
    flow = backend.flow(grey(first), grey(second))
    displacement = np.linalg.norm(flow, axis=2)
    colour = delta_e76(first, second)
    measures: dict[str, Any] = {
        "outside_share": round(float(clear.mean()), 4),
        "margin_px": margin_px,
        "compared_at": [region.shape[1], region.shape[0]],
        "legend": LEGEND,
    }
    if clear.any():
        measures |= {
            "displacement_median_pct": round(100 * float(np.median(displacement[clear])) / long_side, 3),
            "displacement_p95_pct": round(100 * float(np.percentile(displacement[clear], 95)) / long_side, 3),
            "global_shift_px": [round(float(np.median(flow[..., 0][clear])), 1), round(float(np.median(flow[..., 1][clear])), 1)],
            "delta_e_median": round(float(np.median(colour[clear])), 2),
            "delta_e_p95": round(float(np.percentile(colour[clear], 95)), 2),
        }
    else:
        measures |= {
            "displacement_median_pct": None, "displacement_p95_pct": None, "global_shift_px": None,
            "delta_e_median": None, "delta_e_p95": None,
        }
    scaled = np.maximum(displacement / (FULL_DISPLACEMENT * long_side), colour / FULL_DELTA_E)
    pixels = heat_colours(scaled.astype(np.float32))
    pixels[~clear] = (50, 60, 100)
    return Change(measures, Image.fromarray(pixels))


def summarize(measures: Mapping[str, Any]) -> str:
    if measures["displacement_median_pct"] is None:
        return "the removal region and its margin cover the whole frame: nothing outside it to measure"
    dx, dy = measures["global_shift_px"]
    return (
        f"outside the removal region: median shift {measures['displacement_median_pct']:.2f}% of the long side, "
        f"95th percentile {measures['displacement_p95_pct']:.2f}%, median shift vector ({dx:+.1f}, {dy:+.1f}) px, "
        f"median colour difference {measures['delta_e_median']:.1f} (CIE76), 95th percentile {measures['delta_e_p95']:.1f}"
    )


@dataclass
class ChangeMap(ServerTool):
    name: ClassVar[str] = "change_map"
    code_version: ClassVar[str] = "1"
    input_kinds: ClassVar[tuple[str, ...]] = (IMAGE, IMAGE, MASK)

    def parse_params(self, params: Mapping[str, Any]) -> dict[str, Any]:
        refuse_unknown(params, {"margin"}, self.name)
        return {"margin": number_param(params, "margin", DEFAULT_MARGIN, 0.0, 0.2, self.name)}

    def run(self, images: Sequence[Image.Image], params: Mapping[str, Any]) -> ToolOutput:
        backend: FlowBackend = self.backend  # type: ignore[assignment]
        original, candidate, region_image = images
        scale = min(1.0, WORK_SIDE / max(original.size))
        size = (max(1, round(original.width * scale)), max(1, round(original.height * scale)))
        original, candidate = imaging.resize_to(original, size), imaging.resize_to(candidate, size)
        region = imaging.to_mask(region_image, size)
        change = measure_change(original, candidate, region, float(params["margin"]), backend)
        change.measures["candidate_resized"] = bool(images[1].size != images[0].size)
        return ToolOutput({"heatmap": change.heat}, change.measures, summarize(change.measures))
