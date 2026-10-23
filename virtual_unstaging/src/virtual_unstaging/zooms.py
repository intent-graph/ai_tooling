"""Zooms: the places a judge is asked about, from a `structure_map` run and the removal area, each shown as one card
(the whole photo with the place framed, BEFORE and AFTER crops) (design/defect_detectors.md: The zoom judge)."""

from __future__ import annotations

from collections import deque
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

import numpy as np
from numpy.typing import NDArray
from PIL import Image, ImageDraw, ImageFont

from virtual_unstaging import imaging

OUTSIDE, INSIDE = "outside", "inside"
MAX_OUTSIDE, MAX_INSIDE = 4, 2
CONTEXT = 1.0  # an outside place grown by its own size on each side (16 of 18 owner boxes held, against 11 at 0.5)
INSIDE_CONTEXT = 0.25  # the removal area is large: a ring of its surroundings is enough
MIN_SIDE = 0.12  # a crop covers at least this share of the long side
CROP_SIDE = 512  # each crop's long side in the zoom image
GAP = 12
LABEL = 36  # height of the label strip above the panels
MIN_PART = 0.001  # a part of the removal area under this share of the frame gets no zoom
GRID = 128  # the removal area's parts are found on a grid of this long side

Box = tuple[float, float, float, float]


@dataclass(frozen=True)
class Place:
    where: str
    box: Box  # in [0, 1] of the original


def places(measures: Mapping[str, Any], region: NDArray[np.bool_]) -> list[Place]:
    """The structure map's changed regions outside the removal area, largest first, then the area's largest parts."""
    found = [Place(OUTSIDE, _box(r["box"])) for r in (measures.get("regions") or [])[:MAX_OUTSIDE]]
    return found + [Place(INSIDE, box) for box in parts(region)[:MAX_INSIDE]]


def parts(region: NDArray[np.bool_]) -> list[Box]:
    """Boxes of the connected parts of the removal area (4-neighbours, on a coarse grid), largest first."""
    height, width = region.shape
    scale = GRID / max(height, width)
    small = np.asarray(Image.fromarray(region).resize((max(1, round(width * scale)), max(1, round(height * scale))),
                                                     Image.Resampling.NEAREST), dtype=bool)
    rows, columns = small.shape
    seen = np.zeros_like(small)
    found: list[tuple[int, Box]] = []
    for start in zip(*np.nonzero(small), strict=True):
        if seen[start]:
            continue
        seen[start] = True
        queue, ys, xs = deque([start]), [], []
        while queue:
            y, x = queue.popleft()
            ys.append(y)
            xs.append(x)
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < rows and 0 <= nx < columns and small[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    queue.append((ny, nx))
        if len(ys) >= MIN_PART * rows * columns:
            found.append((len(ys), (min(xs) / columns, min(ys) / rows, (max(xs) + 1) / columns, (max(ys) + 1) / rows)))
    return [box for _, box in sorted(found, key=lambda item: -item[0])]


def crop_box(place: Place, size: tuple[int, int]) -> tuple[int, int, int, int]:
    """The place grown for context, at least MIN_SIDE of the long side, in pixels of an image of `size`."""
    width, height = size
    x0, y0, x1, y1 = place.box
    if place.where == OUTSIDE:  # a square around the change, as measured against the owner's boxes
        half_w = half_h = max((x1 - x0) * width, (y1 - y0) * height, MIN_SIDE * max(size)) * (1 + 2 * CONTEXT) / 2
    else:
        half_w = max((x1 - x0) * width * (1 + 2 * INSIDE_CONTEXT), MIN_SIDE * max(size)) / 2
        half_h = max((y1 - y0) * height * (1 + 2 * INSIDE_CONTEXT), MIN_SIDE * max(size)) / 2
    cx, cy = (x0 + x1) / 2 * width, (y0 + y1) / 2 * height
    return (max(0, round(cx - half_w)), max(0, round(cy - half_h)), min(width, round(cx + half_w)),
            min(height, round(cy + half_h)))


def aligned_candidate(original: Image.Image, candidate: Image.Image, measures: Mapping[str, Any]) -> Image.Image:
    """The candidate at the original's size, moved onto it by the structure map's warp when the map applied it."""
    picture = candidate.convert("RGB").resize(original.size, Image.Resampling.LANCZOS)
    alignment, warp = measures.get("alignment") or {}, measures.get("warp")
    if not alignment.get("applied") or warp is None or not measures.get("compared_at"):
        return picture
    s = original.width / float(measures["compared_at"][0])
    (a, b, c), (d, e, f) = warp
    return picture.transform(original.size, Image.Transform.AFFINE, (a, b, c * s, d, e, f * s),
                             resample=Image.Resampling.BICUBIC)


def render(original: Image.Image, aligned: Image.Image, place: Place) -> bytes:
    """One card: the whole photo with the place framed in red, then BEFORE and AFTER cut to the frame, each labelled;
    no shading and no outline (owner, 2026-10-23: "if it is confusing for me, its confusing for judge")."""
    box = crop_box(place, original.size)
    crops = [picture.convert("RGB").crop(box) for picture in (original, aligned)]
    scale = CROP_SIDE / max(crops[0].size)
    size = (max(1, round(crops[0].width * scale)), max(1, round(crops[0].height * scale)))
    crops = [crop.resize(size, Image.Resampling.LANCZOS) for crop in crops]
    whole = original.convert("RGB")
    s = size[1] / whole.height
    whole = whole.resize((max(1, round(whole.width * s)), size[1]), Image.Resampling.LANCZOS)
    ImageDraw.Draw(whole).rectangle([box[0] * s, box[1] * s, box[2] * s, box[3] * s], outline=(255, 30, 30),
                                    width=max(3, size[1] // 120))
    panels = [("WHERE", whole), ("BEFORE", crops[0]), ("AFTER (room emptied)", crops[1])]
    width = sum(panel.width for _, panel in panels) + GAP * (len(panels) - 1)
    sheet = Image.new("RGB", (width, size[1] + LABEL), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=LABEL * 2 // 3)
    x = 0
    for label, panel in panels:
        draw.text((x + 4, 2), label, fill=(0, 0, 0), font=font)
        sheet.paste(panel, (x, LABEL))
        x += panel.width + GAP
    return imaging.encode_png(sheet)


def _box(value: Any) -> Box:
    x0, y0, x1, y1 = (float(v) for v in value)
    return (x0, y0, x1, y1)
