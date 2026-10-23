"""`structure_map`: the candidate aligned to the original, then the regions outside the removal region whose structure
changed, robust to small shifts, resampling and tone, and the tone change outside it (design/tool_server_api.md:
Structure map)."""

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
MIN_MATCHED = 12  # features that must fit one similarity for the feature fit to be trusted
RATIO = 0.75  # Lowe's ratio test on feature matches
TONE_SIGMA = 1 / 32  # tone, not detail: the colour difference smoothed over this fraction of the long side
DEFAULT_MARGIN, DEFAULT_THRESHOLD, DEFAULT_SEARCH = 0.03, 0.45, 0.012
LEGEND = {
    "red outline": "a region outside the removal region whose structure changed",
    "shaded": "the removal region and its margin, not measured",
}

Warp = NDArray[np.float32]  # 2 x 3 affine matrix mapping original coordinates to candidate coordinates


@dataclass(frozen=True)
class Fit:
    """An alignment: the warp, how it was found (`none`: no fit, the warp is the identity and says nothing), and for a
    feature fit, the original's features outside the region and how many of them fit one motion."""

    warp: Warp
    method: str
    features: int | None = None
    matched: int | None = None


class AlignBackend(Backend):
    @abstractmethod
    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Fit:
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

    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Fit:
        self.warm()
        import cv2

        warp = np.eye(2, 3, dtype=np.float32)
        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-5)
        try:
            _, found = cv2.findTransformECC(original, candidate, warp, cv2.MOTION_AFFINE, criteria, keep.astype(np.uint8), 5)
        except cv2.error:  # no convergence: said as no fit, not as "no motion"
            return Fit(warp, "none")
        return Fit(np.asarray(found, dtype=np.float32), "ecc")

    def apply(self, image: ByteArray, warp: Warp) -> ByteArray:
        import cv2

        height, width = image.shape[:2]
        flags = cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP
        return np.asarray(cv2.warpAffine(image, warp, (width, height), flags=flags, borderMode=cv2.BORDER_REFLECT))


class FeatureBackend(EccBackend):
    """A similarity (scale, rotation, shift) fitted by RANSAC on SIFT features of the original outside the region,
    matched in the candidate; ECC when too few fit. Measured on reviewed pairs: it fits reframings ECC diverges on, and
    the share of features that fit tells another picture from the same one (design/defect_detectors.md)."""

    ident: ClassVar[str] = "opencv-sift-similarity"
    model: ClassVar[str] = "OpenCV SIFT, RANSAC similarity; ECC affine as the fallback (no learned model)"

    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Fit:
        self.warm()
        import cv2

        sift = cv2.SIFT.create(nfeatures=4000)
        first, second = (np.clip(x, 0, 255).astype(np.uint8) for x in (original, candidate))
        points_o, described_o = sift.detectAndCompute(first, keep.astype(np.uint8) * 255)
        points_c, described_c = sift.detectAndCompute(second, None)
        features, matched = len(points_o), 0
        if described_o is not None and described_c is not None and len(points_o) >= 2 and len(points_c) >= 2:
            pairs = cv2.BFMatcher().knnMatch(described_o, described_c, k=2)
            good = [m for m, n in (p for p in pairs if len(p) == 2) if m.distance < RATIO * n.distance]
            if len(good) >= MIN_MATCHED:
                source = np.array([points_o[m.queryIdx].pt for m in good], dtype=np.float32)
                target = np.array([points_c[m.trainIdx].pt for m in good], dtype=np.float32)
                warp, inliers = cv2.estimateAffinePartial2D(source, target, method=cv2.RANSAC,
                                                            ransacReprojThreshold=0.01 * max(original.shape))
                if warp is not None and inliers is not None:
                    scale = float(np.sqrt(abs(np.linalg.det(warp[:, :2]))))
                    if 0.5 <= scale <= 2.0:  # many matches on one impossible motion: a degenerate fit, no fit
                        matched = int(inliers.sum())
                        if matched >= MIN_MATCHED:
                            return Fit(np.asarray(warp, dtype=np.float32), "features", features, matched)
        fallback = super().estimate(original, candidate, keep)
        return Fit(fallback.warp, fallback.method, features, matched)


class TranslationBackend(AlignBackend):
    """A stand-in with no OpenCV: one whole-pixel translation, found by phase correlation."""

    ident: ClassVar[str] = "phase-correlation-translation"
    model: ClassVar[str] = "none (test double: a whole-pixel translation by FFT phase correlation)"

    def load(self) -> None:
        return None

    def estimate(self, original: FloatArray, candidate: FloatArray, keep: BoolArray) -> Fit:
        a, b = original - original.mean(), candidate - candidate.mean()
        cross = np.fft.fft2(b) * np.conj(np.fft.fft2(a))
        cross /= np.abs(cross) + 1e-9
        peak_y, peak_x = (int(v) for v in np.unravel_index(int(np.argmax(np.fft.ifft2(cross).real)), a.shape))
        height, width = a.shape
        dy = peak_y - height if peak_y > height // 2 else peak_y
        dx = peak_x - width if peak_x > width // 2 else peak_x
        return Fit(np.array([[1, 0, dx], [0, 1, dy]], dtype=np.float32), "translation")

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


def describe_alignment(fit: Fit, long_side: int) -> dict[str, Any]:
    linear = fit.warp[:, :2].astype(np.float64)
    scale = float(np.sqrt(abs(np.linalg.det(linear))))
    shift = float(np.hypot(fit.warp[0, 2], fit.warp[1, 2])) / long_side
    rotation = float(np.degrees(np.arctan2(linear[1, 0], linear[0, 0])))
    small = SMALL_SCALE[0] <= scale <= SMALL_SCALE[1] and shift <= SMALL_SHIFT and fit.method != "none"
    return {"scale": round(scale, 4), "shift_pct": round(100 * shift, 2), "rotation_deg": round(rotation, 2), "applied": small,
            "method": fit.method, "features": fit.features, "matched": fit.matched}


def lab(rgb: ByteArray) -> FloatArray:
    """CIE L*a*b* (D65) of 8-bit sRGB."""
    c = rgb.astype(np.float64) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    xyz = c @ np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]]).T
    xyz /= np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 216 / 24389, np.cbrt(xyz), (24389 / 27 * xyz + 16) / 116)
    return np.asarray(np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1),
                      dtype=np.float32)


def measure_tone(first: ByteArray, second: ByteArray, keep: BoolArray) -> dict[str, Any] | None:
    """Colour difference outside the region: its uniform part (the median Lab shift, as a CIE76 distance) and how uneven
    it is (90th percentile of the smoothed difference once the uniform part is removed)."""
    if not keep.any():
        return None
    difference = lab(second) - lab(first)
    shift = np.median(difference[keep], axis=0)
    radius = max(1, round(TONE_SIGMA * max(keep.shape) * 0.85))  # three box passes approximate a Gaussian of that sigma
    smooth = np.stack([box_mean(box_mean(box_mean(difference[..., k], radius), radius), radius) for k in range(3)], -1)
    uneven = np.linalg.norm(smooth - shift, axis=-1)[keep]
    return {"shift_de": round(float(np.linalg.norm(shift)), 2), "shift_lab": [round(float(v), 2) for v in shift],
            "uneven_de": round(float(np.percentile(uneven, 90)), 2)}


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
    fit = backend.estimate(grey(first), grey(second), keep)
    alignment = describe_alignment(fit, long_side)
    if alignment["applied"]:
        second = backend.apply(second, fit.warp)
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
        "tone": measure_tone(first, second, keep),
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
    matched = (f" ({a['matched']} of {a['features']} features of the original matched)"
               if a.get("features") is not None else "")
    if a.get("method") == "none":
        framing = f"framing: no fit found between the two pictures{matched}; compared without correction"
    elif a["applied"]:
        framing = (f"framing: aligned by a shift of {a['shift_pct']:.1f}% of the long side, a scale of {a['scale']:.3f} and "
                   f"a rotation of {a['rotation_deg']:.1f} degrees{matched}, corrected before comparing")
    else:
        framing = (f"framing: the best fit is a shift of {a['shift_pct']:.1f}% of the long side, a scale of {a['scale']:.3f} "
                   f"and a rotation of {a['rotation_deg']:.1f} degrees{matched}, beyond a small reframing; compared without "
                   "correction")
    tone = measures.get("tone")
    if tone is not None:
        framing += (f"; tone outside the removal region: a uniform shift of delta E {tone['shift_de']:.1f}, uneven by "
                    f"delta E {tone['uneven_de']:.1f} (90th percentile)")
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
    code_version: ClassVar[str] = "2"
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
