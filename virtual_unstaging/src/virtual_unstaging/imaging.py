"""Image decoding and the cheap pixel operations the orchestrator runs itself (no GPU, no network)."""

from __future__ import annotations

import io
from typing import cast

import numpy as np
from numpy.typing import NDArray
from PIL import Image, ImageOps

MAX_PIXELS = 80_000_000  # decompression-bomb guard, checked on the header before decoding


def decode(data: bytes) -> Image.Image:
    """Decode an image strictly: known format only, bounded size, EXIF orientation applied."""
    with Image.open(io.BytesIO(data)) as probe:
        if probe.format not in ("PNG", "JPEG"):
            raise ValueError(f"unsupported image format {probe.format}")
        if probe.width * probe.height > MAX_PIXELS:
            raise ValueError(f"image too large: {probe.width} x {probe.height}")
        image = ImageOps.exif_transpose(probe)
        image.load()
        return image


def describe(data: bytes) -> tuple[int, int, str]:
    """Width, height and media type of encoded image bytes."""
    with Image.open(io.BytesIO(data)) as probe:
        media_type = {"PNG": "image/png", "JPEG": "image/jpeg"}.get(probe.format or "")
        if media_type is None:
            raise ValueError(f"unsupported image format {probe.format}")
        return probe.width, probe.height, media_type


def encode_png(image: Image.Image) -> bytes:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=False)
    return buffer.getvalue()


def shrink(data: bytes, side: int, image_format: str) -> bytes:
    """The image with its long side reduced to `side` (0 or a larger side: kept), encoded as PNG or JPEG (quality 90)."""
    image = decode(data)
    if side and max(image.size) > side:
        scale = side / max(image.size)
        size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
        image = image.resize(size, Image.Resampling.LANCZOS)
    if image_format != "jpeg":
        return encode_png(image)
    buffer = io.BytesIO()
    image.convert("RGB").save(buffer, format="JPEG", quality=90)
    return buffer.getvalue()


def normalize_photo(data: bytes) -> bytes:
    """An imported photo as stored: orientation applied, RGB, PNG (lossless from here on)."""
    return encode_png(decode(data).convert("RGB"))


def mask_array(data: bytes, size: tuple[int, int] | None = None) -> NDArray[np.bool_]:
    """A mask image as booleans (white = True), resized with nearest neighbour to `size` if given."""
    image = decode(data).convert("L")
    if size is not None and image.size != size:
        image = image.resize(size, Image.Resampling.NEAREST)
    return np.asarray(image) >= 128


def mask_png(mask: NDArray[np.bool_]) -> bytes:
    return encode_png(Image.fromarray((mask.astype(np.uint8) * 255), mode="L"))


def dilate(mask: NDArray[np.bool_], radius_px: int) -> NDArray[np.bool_]:
    """Binary dilation by a square of side 2 * radius + 1, computed with a summed-area table."""
    if radius_px <= 0:
        return mask.copy()
    padded = np.pad(mask.astype(np.int32), radius_px + 1)
    table = padded.cumsum(0).cumsum(1)
    k = 2 * radius_px + 1
    h, w = mask.shape
    window = (
        table[k : k + h, k : k + w]
        - table[0:h, k : k + w]
        - table[k : k + h, 0:w]
        + table[0:h, 0:w]
    )
    return window > 0


def outline(original: bytes, mask: NDArray[np.bool_], width_px: int = 4) -> bytes:
    """The original with the mask's border drawn in a saturated colour, for the judge to see the region."""
    image = decode(original).convert("RGB")
    if mask.shape != (image.height, image.width):
        raise ValueError("mask and image sizes differ")
    border = dilate(mask, width_px) & ~mask
    pixels = np.asarray(image).copy()
    pixels[border] = (255, 0, 255)
    return encode_png(Image.fromarray(pixels))


def rgb_array(data: bytes, size: tuple[int, int] | None = None) -> NDArray[np.float32]:
    image = decode(data).convert("RGB")
    if size is not None and image.size != size:
        image = image.resize(size, Image.Resampling.BICUBIC)
    return cast(NDArray[np.float32], np.asarray(image, dtype=np.float32) / np.float32(255.0))


def delta_e76(a: NDArray[np.float32], b: NDArray[np.float32]) -> NDArray[np.float32]:
    """Per-pixel CIE76 colour difference between two RGB arrays in [0, 1]."""
    return cast(NDArray[np.float32], np.linalg.norm(_rgb_to_lab(a) - _rgb_to_lab(b), axis=-1).astype(np.float32))


def lab(rgb: NDArray[np.float32]) -> NDArray[np.float32]:
    """CIE L*a*b* (D65) of an RGB array in [0, 1]."""
    return _rgb_to_lab(rgb)


def _rgb_to_lab(rgb: NDArray[np.float32]) -> NDArray[np.float32]:
    linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    matrix = np.array(
        [[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]], dtype=np.float32
    )
    xyz = linear @ matrix.T / np.array([0.95047, 1.0, 1.08883], dtype=np.float32)
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16.0 / 116.0)
    lab = np.stack(
        [116.0 * f[..., 1] - 16.0, 500.0 * (f[..., 0] - f[..., 1]), 200.0 * (f[..., 1] - f[..., 2])], axis=-1
    )
    return lab.astype(np.float32)


def heatmap_png(values: NDArray[np.float32], vmax: float) -> bytes:
    """A grey-to-red heat map of non-negative values, saturating at `vmax`."""
    scaled = np.clip(values / max(vmax, 1e-6), 0.0, 1.0)
    pixels = np.zeros((*values.shape, 3), dtype=np.uint8)
    pixels[..., 0] = (255 * scaled).astype(np.uint8)
    pixels[..., 1] = (64 * (1 - scaled)).astype(np.uint8)
    pixels[..., 2] = (64 * (1 - scaled)).astype(np.uint8)
    return encode_png(Image.fromarray(pixels))
