"""Pixel arithmetic in NumPy shared by the tools and the fake generator: dilation, CIE Lab, boxes, colour ramps."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

BoolArray = NDArray[np.bool_]
FloatArray = NDArray[np.float32]
ByteArray = NDArray[np.uint8]

_WHITE_D65 = np.array([0.95047, 1.0, 1.08883], dtype=np.float64)
_SRGB_TO_XYZ = np.array(
    [[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750], [0.0193339, 0.1191920, 0.9503041]],
    dtype=np.float64,
)


def _window_any(mask: BoolArray, radius: int, axis: int) -> BoolArray:
    """True where any value within `radius` along `axis` is True, by prefix sums (cost independent of radius)."""
    padded = np.pad(mask.astype(np.int32), [(radius, radius) if a == axis else (0, 0) for a in range(2)])
    total = np.cumsum(padded, axis=axis)
    zero = np.zeros_like(np.take(total, [0], axis=axis))
    total = np.concatenate([zero, total], axis=axis)
    size = mask.shape[axis]
    upper = np.take(total, np.arange(2 * radius + 1, 2 * radius + 1 + size), axis=axis)
    lower = np.take(total, np.arange(0, size), axis=axis)
    return (upper - lower) > 0


def dilate_square(mask: BoolArray, radius: int) -> BoolArray:
    """The mask grown by `radius` pixels in every direction (a square window, as the orchestrator's own dilation)."""
    if radius <= 0:
        return mask.copy()
    return _window_any(_window_any(mask, radius, 0), radius, 1)


def srgb_to_lab(rgb: ByteArray) -> FloatArray:
    """CIE L*a*b* (D65) of an 8-bit sRGB image of shape (H, W, 3)."""
    linear = rgb.astype(np.float64) / 255.0
    linear = np.where(linear <= 0.04045, linear / 12.92, ((linear + 0.055) / 1.055) ** 2.4)
    xyz = (linear @ _SRGB_TO_XYZ.T) / _WHITE_D65
    f = np.where(xyz > (6 / 29) ** 3, np.cbrt(xyz), xyz / (3 * (6 / 29) ** 2) + 4 / 29)
    lab = np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], axis=-1)
    return lab.astype(np.float32)


def delta_e76(first: ByteArray, second: ByteArray) -> FloatArray:
    """The CIE76 colour difference per pixel between two 8-bit sRGB images."""
    return np.asarray(np.linalg.norm(srgb_to_lab(first) - srgb_to_lab(second), axis=-1), dtype=np.float32)


def grey(rgb: ByteArray) -> FloatArray:
    """Rec. 601 luma of an 8-bit RGB image, as float in [0, 255]."""
    return np.asarray(rgb[..., 0] * 0.299 + rgb[..., 1] * 0.587 + rgb[..., 2] * 0.114, dtype=np.float32)


def box_of(mask: BoolArray) -> list[float] | None:
    """[x0, y0, x1, y1] in [0, 1] around the True pixels (x to the right, y down), None when there are none."""
    rows, columns = np.where(mask.any(axis=1))[0], np.where(mask.any(axis=0))[0]
    if rows.size == 0 or columns.size == 0:
        return None
    height, width = mask.shape
    return [
        round(float(columns[0]) / width, 4),
        round(float(rows[0]) / height, 4),
        round(float(columns[-1] + 1) / width, 4),
        round(float(rows[-1] + 1) / height, 4),
    ]


def heat_colours(scaled: FloatArray) -> ByteArray:
    """Grey to red ramp of values in [0, 1]: 0 is dark grey, 1 is saturated red."""
    scaled = np.clip(scaled, 0.0, 1.0)
    pixels = np.zeros((*scaled.shape, 3), dtype=np.uint8)
    pixels[..., 0] = (64 + 191 * scaled).astype(np.uint8)
    pixels[..., 1] = (64 * (1 - scaled)).astype(np.uint8)
    pixels[..., 2] = (64 * (1 - scaled)).astype(np.uint8)
    return pixels
