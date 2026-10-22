"""The pixel side of a pair: shift and colour checks, correction, change mask, composite, explained change.

Pure functions on arrays (design/loops.md, "The clutter loop", steps 3 to 7). Images are float RGB arrays in [0, 1];
the mask's alpha is an 8-bit array, so "alpha is 0" is exact and the composite equals the clean image there (P1).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from virtual_unstaging import imaging

from clutter_pairs.domain import Box, Finding, Measure, PixelResult

FloatImage = NDArray[np.float32]
Mask = NDArray[np.bool_]
Alpha = NDArray[np.uint8]
MIN_SPREAD = 0.05  # standard deviation of a far-field channel, in [0, 1], below which no gain is fitted
GAIN_RANGE = (0.8, 1.25)


@dataclass(frozen=True)
class Thresholds:
    """Every value the pixel tests compare against; the owner sets them on 20 to 30 pairs (S4)."""

    max_shift_px: float = 2.0
    far_field_delta_e: float = 20.0  # pixels above it before correction are a change, not the far field
    far_field_dilation_px: int = 16
    max_global_delta_e: float = 6.0  # median colour difference on the far field, before correction
    change_delta_e: float = 8.0  # the change mask's per-pixel threshold, after correction and a small blur
    blur_px: int = 1
    open_px: int = 2
    close_px: int = 3
    dilate_px: int = 4
    feather_px: int = 4
    explained_min_share: float = 0.6  # a component is explained when this share of it lies in a located box
    box_margin: float = 0.02  # each located box widened by this share of the image's side (shadows, loose boxes)
    min_component_px: int = 64

    def as_dict(self) -> dict[str, float]:
        return {name: float(getattr(self, name)) for name in self.__dataclass_fields__}


@dataclass(frozen=True)
class Prepared:
    """The edit after the global tests: corrected, with its change mask (binary and feathered alpha)."""

    corrected: FloatImage
    mask: Mask
    alpha: Alpha
    result: PixelResult


def prepare(clean: FloatImage, edit: FloatImage, share_range: tuple[float, float], t: Thresholds) -> Prepared:
    """Steps 3 to 4: size, shift, global colour change; correction; change mask and its share."""
    if clean.shape != edit.shape:
        finding = Finding("misaligned", None, None, f"edit size {edit.shape[1]}x{edit.shape[0]} differs from the clean image")
        return Prepared(edit, np.zeros(clean.shape[:2], bool), np.zeros(clean.shape[:2], np.uint8),
                        PixelResult((), (finding,)))
    shift = estimate_shift(clean, edit)
    shift_px = float(np.hypot(*shift))
    raw_diff = imaging.delta_e76(clean, edit)
    far = ~imaging.dilate(raw_diff > t.far_field_delta_e, t.far_field_dilation_px)
    if far.mean() < 0.05:  # nearly everything changed: the far field is the whole image
        far = np.ones_like(far)
    global_delta = float(np.median(raw_diff[far]))
    corrected = correct_colour(clean, edit, far)
    mask = change_mask(clean, corrected, t)
    share = float(mask.mean())
    measures = [
        Measure("shift_px", shift_px, t.max_shift_px),
        Measure("global_delta_e", global_delta, t.max_global_delta_e),
        Measure("mask_share_min", share, share_range[0]),
        Measure("mask_share_max", share, share_range[1]),
    ]
    findings: list[Finding] = []
    if shift_px > t.max_shift_px:
        findings.append(Finding("misaligned", None, None, f"shifted by {shift[0]:+d}, {shift[1]:+d} px"))
    if global_delta > t.max_global_delta_e:
        findings.append(Finding("global_repaint", None, None, f"median colour change {global_delta:.1f} on the far field"))
    if not findings and not share_range[0] <= share <= share_range[1]:
        findings.append(Finding("clutter_off_spec", None, None,
                                f"the change covers {share:.1%} of the image, outside {share_range[0]:.0%} to {share_range[1]:.0%}"))
    return Prepared(corrected, mask, feather(mask, t.feather_px), PixelResult(tuple(measures), tuple(findings)))


def estimate_shift(a: FloatImage, b: FloatImage) -> tuple[int, int]:
    """Integer translation (dx, dy) of b against a, by phase correlation on grey levels."""
    ga, gb = a.mean(axis=2), b.mean(axis=2)
    fa, fb = np.fft.fft2(ga - ga.mean()), np.fft.fft2(gb - gb.mean())
    cross = fa.conj() * fb
    cross /= np.maximum(np.abs(cross), 1e-9)
    corr = np.abs(np.fft.ifft2(cross))
    dy, dx = np.unravel_index(int(np.argmax(corr)), corr.shape)
    h, w = corr.shape
    return (int(dx - w) if dx > w // 2 else int(dx)), (int(dy - h) if dy > h // 2 else int(dy))


def correct_colour(clean: FloatImage, edit: FloatImage, far: Mask) -> FloatImage:
    """The edit with a per-channel gain and offset fitted on the far field to bring it back to the clean image. A far
    field with little spread (a bare wall) fixes no gain: the offset alone is fitted, and the gain stays in
    GAIN_RANGE, so a flat region never makes the correction blow up the colours inside the mask."""
    out = np.empty_like(edit)
    for c in range(3):
        x, y = edit[..., c][far].astype(np.float64), clean[..., c][far].astype(np.float64)
        if x.size < 16:
            out[..., c] = edit[..., c]
            continue
        gain = 1.0
        if float(x.std()) >= MIN_SPREAD:
            gain = float(np.clip(np.cov(x, y, bias=True)[0, 1] / x.var(), *GAIN_RANGE))
        offset = float(y.mean() - gain * x.mean())
        out[..., c] = edit[..., c] * gain + offset
    return np.clip(out, 0.0, 1.0).astype(np.float32)


def change_mask(clean: FloatImage, corrected: FloatImage, t: Thresholds) -> Mask:
    """Per-pixel colour difference after a small blur, thresholded, opened, closed, dilated."""
    diff = imaging.delta_e76(box_blur(clean, t.blur_px), box_blur(corrected, t.blur_px))
    mask = diff > t.change_delta_e
    mask = imaging.dilate(erode(mask, t.open_px), t.open_px)  # opening: drop specks
    mask = erode(imaging.dilate(mask, t.close_px), t.close_px)  # closing: fill pinholes
    return imaging.dilate(mask, t.dilate_px)


def feather(mask: Mask, radius_px: int) -> Alpha:
    """A soft alpha: the binary mask blurred, then kept at 255 inside the mask so the item is the edit's own pixels.
    Zero exactly where no pixel of the mask is within the radius."""
    soft = box_blur(mask.astype(np.float32)[..., None], radius_px)[..., 0]
    alpha = np.where(mask, 1.0, soft)
    return np.asarray(np.round(alpha * 255), dtype=np.uint8)


def composite(clean: FloatImage, corrected: FloatImage, alpha: Alpha) -> NDArray[np.uint8]:
    """The cluttered image: the clean image where alpha is 0, the corrected edit where it is 255, blended between.
    Computed on 8-bit values so a pixel with alpha 0 is the clean pixel exactly."""
    c8 = to_uint8(clean).astype(np.int32)
    e8 = to_uint8(corrected).astype(np.int32)
    a = alpha.astype(np.int32)[..., None]
    return ((c8 * (255 - a) + e8 * a + 127) // 255).astype(np.uint8)


def explain(mask: Mask, located: Sequence[Box], t: Thresholds) -> PixelResult:
    """Step 7: every connected component of the change mask must lie in a located item's box."""
    labels, count = label_components(mask)
    h, w = mask.shape
    boxes = np.zeros((h, w), dtype=bool)
    m = t.box_margin
    for box in located:
        boxes[int(max(box.y0 - m, 0) * h):int(np.ceil(min(box.y1 + m, 1) * h)),
              int(max(box.x0 - m, 0) * w):int(np.ceil(min(box.x1 + m, 1) * w))] = True
    unexplained_px, findings = 0, []
    for label in range(1, count + 1):
        component = labels == label
        size = int(component.sum())
        if size < t.min_component_px:
            continue
        inside = float((component & boxes).sum()) / size
        if inside < t.explained_min_share:
            unexplained_px += size
            ys, xs = np.nonzero(component)
            region = Box(xs.min() / w, ys.min() / h, (xs.max() + 1) / w, (ys.max() + 1) / h)
            findings.append(Finding("unexplained_change", None, region,
                                    f"a changed region of {size} px is {inside:.0%} inside the located items"))
    total = max(int(mask.sum()), 1)
    measures = (Measure("unexplained_share", unexplained_px / total, 0.0),)
    return PixelResult(measures, tuple(findings))


# --- Array helpers -------------------------------------------------------------------------------------------


def box_blur(image: FloatImage, radius: int) -> FloatImage:
    """Mean over a square of side 2r + 1, edges clamped, with a summed-area table."""
    if radius <= 0:
        return image
    k = 2 * radius + 1
    padded = np.pad(image, ((radius + 1, radius), (radius + 1, radius), (0, 0)), mode="edge").astype(np.float64)
    table = padded.cumsum(0).cumsum(1)
    h, w = image.shape[:2]
    window = table[k:k + h, k:k + w] - table[0:h, k:k + w] - table[k:k + h, 0:w] + table[0:h, 0:w]
    return (window / (k * k)).astype(np.float32)


def erode(mask: Mask, radius: int) -> Mask:
    return ~imaging.dilate(~mask, radius) if radius > 0 else mask.copy()


def to_uint8(image: FloatImage) -> NDArray[np.uint8]:
    return np.asarray(np.round(np.clip(image, 0, 1) * 255), dtype=np.uint8)


def label_components(mask: Mask) -> tuple[NDArray[np.int32], int]:
    """8-connected component labels, on runs of each row joined by union-find: fast without a C extension."""
    h, _ = mask.shape
    parent: list[int] = [0]

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    runs: list[tuple[int, int, int, int]] = []  # row, start, end (exclusive), label
    previous: list[tuple[int, int, int]] = []
    for y in range(h):
        row = mask[y].astype(np.int8)
        edges = np.flatnonzero(np.diff(np.concatenate(([0], row, [0]))))
        current: list[tuple[int, int, int]] = []
        for start, end in zip(edges[::2], edges[1::2], strict=True):
            label = 0
            for p_start, p_end, p_label in previous:
                if p_start <= end and start <= p_end:  # overlapping or touching diagonally
                    if label == 0:
                        label = find(p_label)
                    else:
                        a, b = find(label), find(p_label)
                        if a != b:
                            parent[max(a, b)] = min(a, b)
                            label = min(a, b)
            if label == 0:
                label = len(parent)
                parent.append(label)
            current.append((int(start), int(end), label))
            runs.append((y, int(start), int(end), label))
        previous = current
    roots: dict[int, int] = {}
    labels = np.zeros(mask.shape, dtype=np.int32)
    for y, start, end, label in runs:
        root = find(label)
        labels[y, start:end] = roots.setdefault(root, len(roots) + 1)
    return labels, len(roots)
