"""How an imported image becomes a clean image: opaque RGB, a hash of its pixels, the resize to the editor's size.

Pure: one place for the steps the import applies and the audit applies again (design/imports.md)."""

from __future__ import annotations

import hashlib

from PIL import Image

RESAMPLER = "lanczos"  # recorded on import_set; the only one implemented
_RESAMPLERS = {RESAMPLER: Image.Resampling.LANCZOS}


def opaque_rgb(image: Image.Image) -> Image.Image:
    """The image as RGB; ValueError when it has a transparent pixel (a clean image is opaque: the cluttered image is
    RGB, and a consumer must not see two modes)."""
    if image.mode in ("RGBA", "LA", "PA") or (image.mode == "P" and "transparency" in image.info):
        low, _ = image.convert("RGBA").getchannel("A").getextrema()
        if low != 255:
            raise ValueError("it has transparent pixels; a clean image is opaque")
    return image.convert("RGB")


def pixel_sha(rgb: Image.Image) -> str:
    """The hash of the decoded RGB pixels and the size: the same picture saved with other bytes hashes the same."""
    digest = hashlib.sha256(f"{rgb.width}x{rgb.height}:".encode("ascii"))
    digest.update(rgb.tobytes())
    return digest.hexdigest()


def resized(rgb: Image.Image, size: tuple[int, int], resampler: str = RESAMPLER) -> Image.Image:
    """The image at the editor's size (unchanged when it is already that size)."""
    if resampler not in _RESAMPLERS:
        raise ValueError(f"unknown resampler {resampler!r}")
    return rgb if rgb.size == size else rgb.resize(size, _RESAMPLERS[resampler])
