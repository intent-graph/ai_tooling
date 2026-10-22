"""Strict image decoding and encoding for the tool server: PNG and JPEG only, bounded size, arrays for the tools."""

from __future__ import annotations

import io

import numpy as np
from numpy.typing import NDArray
from PIL import Image, ImageOps

MAX_PIXELS = 80_000_000  # decompression-bomb guard, checked on the header before decoding
MEDIA_TYPES = ("image/png", "image/jpeg")
_PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
_JPEG_SIGNATURE = b"\xff\xd8\xff"


def sniff_media_type(data: bytes) -> str | None:
    """The media type the bytes start as, or None when they are neither PNG nor JPEG."""
    if data.startswith(_PNG_SIGNATURE):
        return "image/png"
    if data.startswith(_JPEG_SIGNATURE):
        return "image/jpeg"
    return None


def check_header(data: bytes) -> tuple[int, int, str]:
    """Width, height and media type from the header alone; ValueError unless a bounded PNG or JPEG."""
    try:
        with Image.open(io.BytesIO(data)) as probe:
            media_type = {"PNG": "image/png", "JPEG": "image/jpeg"}.get(probe.format or "")
            if media_type is None:
                raise ValueError(f"unsupported image format {probe.format}")
            if probe.width * probe.height > MAX_PIXELS:
                raise ValueError(f"image too large: {probe.width} x {probe.height}")
            return probe.width, probe.height, media_type
    except (OSError, SyntaxError) as error:
        raise ValueError(f"not a decodable image: {error}") from None


def decode(data: bytes, mode: str = "RGB") -> Image.Image:
    """Decode a bounded PNG or JPEG, apply EXIF orientation once, convert to `mode` ("RGB" or "L")."""
    check_header(data)
    with Image.open(io.BytesIO(data)) as opened:
        upright = ImageOps.exif_transpose(opened)
        upright.load()
        return upright.convert(mode)


def encode_png(image: Image.Image) -> bytes:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=False)
    return buffer.getvalue()


def to_mask(image: Image.Image, size: tuple[int, int] | None = None) -> NDArray[np.bool_]:
    """A grey image as booleans (white = True, threshold 128), resized with nearest neighbour to `size`."""
    grey = image.convert("L")
    if size is not None and grey.size != size:
        grey = grey.resize(size, Image.Resampling.NEAREST)
    return np.asarray(grey) >= 128


def mask_image(mask: NDArray[np.bool_]) -> Image.Image:
    return Image.fromarray(mask.astype(np.uint8) * 255, mode="L")


def resize_to(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return image if image.size == size else image.resize(size, Image.Resampling.LANCZOS)


def reduce_area(image: Image.Image, side: int, nearest: bool = False) -> Image.Image:
    """The image with about side x side pixels at most, its aspect ratio kept; a smaller one is returned as is."""
    area = image.width * image.height
    if area <= side * side:
        return image
    scale = (side * side / area) ** 0.5
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    return image.resize(size, Image.Resampling.NEAREST if nearest else Image.Resampling.LANCZOS)


def output_size(original: tuple[int, int], side: int, multiple: int) -> tuple[int, int]:
    """Width and height with the original's aspect ratio and about side x side pixels, as multiples of `multiple`."""
    width, height = original
    ratio = width / height
    out_width = (side * side * ratio) ** 0.5
    out_height = out_width / ratio
    return max(multiple, int(out_width // multiple * multiple)), max(multiple, int(out_height // multiple * multiple))
