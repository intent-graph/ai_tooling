"""`structure_map`: the candidate aligned to the original, then the regions outside the removal region whose structure
changed, robust to small shifts, resampling and tone (design/tool_server_api.md: Structure map)."""

from __future__ import annotations

from abc import abstractmethod
from collections import deque
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

import numpy as np
from numpy.typing import NDArray
from PIL import Image

from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.pixels import BoolArray, ByteArray, FloatArray, dilate_square, grey
from virtual_unstaging.serve.tools.base import (
    IMAGE,
    MASK,
    Backend,
    ServerTool,
    ToolOutput,
    number_param,
    refuse_unknown,
)

WORK_SIDE = 512  # long side the structure is compared at
WINDOW = 3  # SSIM window radius: 7 x 7 pixels
CELL = 8  # changes are pooled in cells of this many pixels
MIN_REGION = 0.002  # smallest region kept, as a share of the frame
MAX_REGIONS = 8
SMALL_SCALE = (0.95, 1.05)  # an alignment within these and SMALL_SHIFT is a small reframing, applied
SMALL_SHIFT = 0.03  # fraction of the long side
DEFAULT_MARGIN, DEFAULT_THRESHOLD, DEFAULT_SEARCH = 0.03, 0.45, 0.012
LEGEND = {
    "red outline": "a region outside the removal region whose structure changed",
    "shaded": "the removal region and its margin, not measured",
}

Warp = NDArray[np.float32]  # 2 x 3 affine matrix mapping original coordinates to candidate coordinates


class AlignBackend(Backend):
    @abstractmethod
    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Warp:
        """The affine warp that maps the original's pixels onto the candidate's, fitted where `keep` is true."""

    @abstractmethod
    def apply(self, image: ByteArray, warp: Warp) -> ByteArray:
        """The candidate resampled onto the original's grid by `warp`."""


class EccBackend(AlignBackend):
    """OpenCV's enhanced correlation coefficient maximization, affine motion."""

    ident: ClassVar[str] = "opencv-ecc-affine"
    model: ClassVar[str] = "OpenCV findTransformECC, affine (no learned model)"

    def load(self) -> None:
        import cv2  # noqa: F401  (fail at warm-up, not at the first call)

    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Warp:
        self.warm()
        import cv2

        warp = np.eye(2, 3, dtype=np.float32)
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-5)
        try:
            _, found = cv2.findTransformECC(original, candidate, warp, cv2.MOTION_AFFINE, criteria, keep.astype(np.uint8), 5)
        except cv2.error:  # no convergence: no alignment, which the measures say (scale 1, shift 0)
            return warp
        return np.asarray(found, dtype=np.float32)

    def apply(self, image: ByteArray, warp: Warp) -> ByteArray:
        import cv2

        height, width = image.shape[:2]
        flags = cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP
        return np.asarray(cv2.warpAffine(image, warp, (width, height), flags=flags, borderMode=cv2.BORDER_REFLECT))


class TranslationBackend(AlignBackend):
    """A stand-in with no OpenCV: one whole-pixel translation, found by phase correlation."""

    ident: ClassVar[str] = "phase-correlation-translation"
    model: ClassVar[str] = "none (test double: a whole-pixel translation by FFT phase correlation)"

    def load(self) -> None:
        return None

    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Warp:
        a, b = original - original.mean(), candidate - candidate.mean()
        cross = np.fft.fft2(b) * np.conj(np.fft.fft2(a))
        cross /= np.abs(cross) + 1e-9
        peak_y, peak_x = (int(v) for v in np.unravel_index(int(np.argmax(np.fft.ifft2(cross).real)), a.shape))
        height, width = a.shape
        dy = peak_y - height if peak_y > height // 2 else peak_y
        dx = peak_x - width if peak_x > width // 2 else peak_x
        return np.array([[1, 0, dx], [0, 1, dy]], dtype=np.float32)

    def apply(self, image: ByteArray, warp: Warp) -> ByteArray:
        dx, dy = int(round(float(warp[0, 2]))), int(round(float(warp[1, 2])))
        return np.roll(np.roll(image, -dy, axis=0), -dx, axis=1)


def box_mean(values: FloatArray, radius: int) -> FloatArray:
    """The mean over a (2 radius + 1)-square window around each pixel, the frame's edge repeated."""
    padded = np.pad(values.astype(np.float64), radius + 1, mode="edge")
    total = padded.cumsum(axis=0).cumsum(axis=1)
    size = 2 * radius + 1
    height, width = values.shape
    window = (total[size : size + height, size : size + width] - total[:height, size : size + width]
              - total[size : size + height, :width] + total[:height, :width])
    return np.asarray(window / (size * size), dtype=np.float32)


def ssim(a: FloatArray, b: FloatArray) -> FloatArray:
    """Structural similarity per pixel (grey levels 0-255, square window)."""
    c1, c2 = (0.01 * 255) ** 2, (0.03 * 255) ** 2
    ma, mb = box_mean(a, WINDOW), box_mean(b, WINDOW)
    va, vb = box_mean(a * a, WINDOW) - ma * ma, box_mean(b * b, WINDOW) - mb * mb
    cov = box_mean(a * b, WINDOW) - ma * mb
    return np.asarray(((2 * ma * mb + c1) * (2 * cov + c2)) / ((ma * ma + mb * mb + c1) * (va + vb + c2)), dtype=np.float32)


def tolerant_dissimilarity(a: FloatArray, b: FloatArray, search: int) -> FloatArray:
    """1 - the best SSIM each point reaches against the other picture shifted by up to `search` pixels, both ways."""
    best_ab = np.full(a.shape, -1.0, dtype=np.float32)
    best_ba = np.full(a.shape, -1.0, dtype=np.float32)
    step = max(1, search // 3)
    for dy in range(-search, search + 1, step):
        for dx in range(-search, search + 1, step):
            best_ab = np.maximum(best_ab, ssim(a, np.roll(np.roll(b, dy, axis=0), dx, axis=1)))
            best_ba = np.maximum(best_ba, ssim(b, np.roll(np.roll(a, dy, axis=0), dx, axis=1)))
    return np.asarray(np.clip(1.0 - np.minimum(best_ab, best_ba), 0.0, 1.0), dtype=np.float32)


def regions(cells: BoolArray, min_cells: int) -> list[list[tuple[int, int]]]:
    """Connected groups of true cells (4-neighbours) of at least `min_cells`, largest first."""
    seen = np.zeros_like(cells)
    groups: list[list[tuple[int, int]]] = []
    rows, columns = cells.shape
    for start in zip(*np.nonzero(cells), strict=True):
        if seen[start]:
            continue
        seen[start] = True
        group, queue = [], deque([start])
        while queue:
            y, x = queue.popleft()
            group.append((int(y), int(x)))
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < rows and 0 <= nx < columns and cells[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    queue.append((ny, nx))
        if len(group) >= min_cells:
            groups.append(group)
    return sorted(groups, key=len, reverse=True)


def describe_alignment(warp: Warp, long_side: int) -> dict[str, Any]:
    linear = warp[:, :2].astype(np.float64)
    scale = float(np.sqrt(abs(np.linalg.det(linear))))
    shift = float(np.hypot(warp[0, 2], warp[1, 2])) / long_side
    rotation = float(np.degrees(np.arctan2(linear[1, 0], linear[0, 0])))
    small = SMALL_SCALE[0] <= scale <= SMALL_SCALE[1] and shift <= SMALL_SHIFT
    return {"scale": round(scale, 4), "shift_pct": round(100 * shift, 2), "rotation_deg": round(rotation, 2), "applied": small}


@dataclass(frozen=True)
class Structure:
    measures: dict[str, Any]
    picture: Image.Image


def measure_structure(
    original: Image.Image, candidate: Image.Image, region: BoolArray, margin: float, threshold: float, search: float,
    backend: AlignBackend,
) -> Structure:
    """Pure core of `structure_map`: both pictures and the region are at one size."""
    first, second = np.asarray(original.convert("RGB")), np.asarray(candidate.convert("RGB"))
    long_side = max(region.shape)
    keep = ~dilate_square(region, round(margin * long_side))
    warp = backend.estimate(grey(first), grey(second), keep)
    alignment = describe_alignment(warp, long_side)
    if alignment["applied"]:
        second = backend.apply(second, warp)
    change = tolerant_dissimilarity(grey(first), grey(second), max(1, round(search * long_side)))
    height, width = region.shape
    rows, columns = height // CELL, width // CELL
    trimmed = (slice(0, rows * CELL), slice(0, columns * CELL))
    pooled = change[trimmed].reshape(rows, CELL, columns, CELL).mean(axis=(1, 3))
    kept_cells = keep[trimmed].reshape(rows, CELL, columns, CELL).mean(axis=(1, 3)) >= 0.5
    min_cells = max(1, round(MIN_REGION * rows * columns))
    found = regions((pooled > threshold) & kept_cells, min_cells)
    changed = np.zeros((rows, columns), dtype=bool)
    listed: list[dict[str, Any]] = []
    for group in found:
        ys, xs = zip(*group, strict=True)
        for y, x in group:
            changed[y, x] = True
        if len(listed) < MAX_REGIONS:
            listed.append({
                "box": [round(min(xs) / columns, 3), round(min(ys) / rows, 3), round((max(xs) + 1) / columns, 3),
                        round((max(ys) + 1) / rows, 3)],
                "share": round(len(group) / (rows * columns), 4),
            })
    outside = int(kept_cells.sum())
    measures: dict[str, Any] = {
        "alignment": alignment,
        "outside_changed_share": round(int(changed.sum()) / outside, 4) if outside else None,
        "regions": listed,
        "compared_at": [width, height],
        "threshold": threshold,
        "legend": LEGEND,
    }
    return Structure(measures, draw(second, keep, changed))


def draw(candidate: ByteArray, keep: BoolArray, changed: BoolArray) -> Image.Image:
    """The aligned candidate, the unmeasured region shaded, the changed cells' outline in red."""
    pixels = candidate.astype(np.float32)
    pixels[~keep] = pixels[~keep] * 0.55 + np.array([60, 60, 110], dtype=np.float32) * 0.45
    mask = np.kron(changed, np.ones((CELL, CELL), dtype=bool))
    full = np.zeros(keep.shape, dtype=bool)
    full[: mask.shape[0], : mask.shape[1]] = mask
    edge = full & ~(np.roll(full, 1, 0) & np.roll(full, -1, 0) & np.roll(full, 1, 1) & np.roll(full, -1, 1))
    edge = dilate_square(edge, 1)
    pixels[edge] = (255, 30, 30)
    return Image.fromarray(np.clip(pixels, 0, 255).astype(np.uint8))


def summarize(measures: Mapping[str, Any]) -> str:
    a = measures["alignment"]
    if a["applied"]:
        framing = (f"framing: the candidate matches the original after a shift of {a['shift_pct']:.1f}% of the long side "
                   f"and a scale of {a['scale']:.3f} (a small reframing, corrected before comparing)")
    else:
        framing = (f"framing differs: a fit needs a shift of {a['shift_pct']:.1f}% of the long side and a scale of "
                   f"{a['scale']:.3f}, more than a small reframing (a sign that the viewpoint changed); compared without "
                   "correction")
    if measures["outside_changed_share"] is None:
        return framing + "; the removal region and its margin cover the whole frame: nothing outside it to compare"
    found = measures["regions"]
    if not found:
        return framing + "; outside the removal region, no structural change"
    places = "; ".join(f"({r['box'][0]:.2f}, {r['box'][1]:.2f})-({r['box'][2]:.2f}, {r['box'][3]:.2f}) {r['share']:.1%} of the frame"
                       for r in found)
    count = f"{len(found)} place" + ("s" if len(found) > 1 else "")
    return (f"{framing}; outside the removal region, the structure changed in {count}, together "
            f"{measures['outside_changed_share']:.1%} of that area: {places}")


@dataclass
class StructureMap(ServerTool):
    name: ClassVar[str] = "structure_map"
    code_version: ClassVar[str] = "1"
    input_kinds: ClassVar[tuple[str, ...]] = (IMAGE, IMAGE, MASK)

    def parse_params(self, params: Mapping[str, Any]) -> dict[str, Any]:
        refuse_unknown(params, {"margin", "threshold", "search"}, self.name)
        return {
            "margin": number_param(params, "margin", DEFAULT_MARGIN, 0.0, 0.2, self.name),
            "threshold": number_param(params, "threshold", DEFAULT_THRESHOLD, 0.05, 1.0, self.name),
            "search": number_param(params, "search", DEFAULT_SEARCH, 0.0, 0.05, self.name),
        }

    def run(self, images: Sequence[Image.Image], params: Mapping[str, Any]) -> ToolOutput:
        backend: AlignBackend = self.backend  # type: ignore[assignment]
        original, candidate, region_image = images
        scale = min(1.0, WORK_SIDE / max(original.size))
        size = (max(1, round(original.width * scale)), max(1, round(original.height * scale)))
        original, candidate = imaging.resize_to(original, size), imaging.resize_to(candidate, size)
        region = imaging.to_mask(region_image, size)
        result = measure_structure(original, candidate, region, float(params["margin"]), float(params["threshold"]),
                                   float(params["search"]), backend)
        result.measures["candidate_resized"] = bool(images[1].size != images[0].size)
        return ToolOutput({"changes": result.picture}, result.measures, summarize(result.measures))
