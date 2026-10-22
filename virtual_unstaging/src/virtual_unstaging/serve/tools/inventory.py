"""`element_inventory`: the room's named elements in the original and the candidate, matched by place, each with a
status (kept, revealed, changed, removed, new, left) inside or outside the region (design/tool_server_api.md)."""

from __future__ import annotations

import hashlib
import threading
from collections import Counter, OrderedDict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.errors import ApiError
from virtual_unstaging.serve.pixels import BoolArray, box_of
from virtual_unstaging.serve.tools.base import (
    IMAGE,
    MASK,
    ServerTool,
    ToolOutput,
    number_param,
    refuse_unknown,
)
from virtual_unstaging.serve.tools.segment import DEFAULT_THRESHOLD, LABEL, Instance, SegmentBackend

WORK_SIDE = 1024  # long side the pictures are detected at
MATCH_SIDE = 256  # long side the masks are compared at
MAX_NAMES = 96
SAME_ELEMENT = 0.6  # overlap above which two detections of one kind in one picture are one element
NESTED = 0.8  # share of a detection inside another of its kind above which it is part of it ...
NESTED_SIZE = 0.2  # ... when it is at least this fraction of the other's area (a socket in a cupboard stays apart)
MIN_MATCH = 0.3  # overlap a pair across the pictures needs
KEPT = 0.6  # overlap at or above which a matched element is kept
GROWTH = 1.5  # area ratio at or above which a matched element grew (revealed, when the growth is in the region)
INSIDE = 0.5  # share of an element's mask in the region at or above which it is inside
STOOD = 0.3  # share of a new element covered by an original element for that element to have stood there
MAX_LINES = 24
CACHE_SIZE = 32  # detections of recent pictures: the original is the same for every attempt on a photo

STATUS_ORDER = ("new", "removed", "changed", "left", "revealed", "kept")
COLOURS = {
    "new": (255, 40, 40),
    "removed": (255, 0, 255),
    "changed": (255, 150, 0),
    "left": (255, 220, 0),
    "revealed": (40, 210, 90),
}
LEGEND = {
    "red": "new: in the candidate only",
    "magenta": "removed: in the original only (its box in the original)",
    "orange": "changed: in both, its outline changed",
    "yellow": "left: a movable element still inside the region",
    "green": "revealed: partly hidden in the original, completed inside the region",
}


@dataclass(frozen=True)
class Seen:
    """One element in one picture, duplicates merged."""

    label: str
    kind: str  # fixed | movable
    score: float
    mask: BoolArray  # at the match size
    box: list[float]  # [x0, y0, x1, y1] in [0, 1]


@dataclass(frozen=True)
class Element:
    label: str
    kind: str
    status: str
    where: str  # inside | outside
    inside_share: float
    box_original: list[float] | None
    box_candidate: list[float] | None
    overlap: float | None = None
    growth: float | None = None
    stood: tuple[str, ...] = ()

    def as_dict(self, n: int) -> dict[str, Any]:
        return {
            "n": n, "label": self.label, "kind": self.kind, "status": self.status, "where": self.where,
            "inside_share": self.inside_share, "box_original": self.box_original, "box_candidate": self.box_candidate,
            "overlap": self.overlap, "growth": self.growth, "stood": list(self.stood),
        }


def _shrink(mask: BoolArray, size: tuple[int, int]) -> BoolArray:
    return imaging.to_mask(imaging.mask_image(mask), size) if mask.shape != (size[1], size[0]) else mask


def _overlap(a: BoolArray, b: BoolArray) -> float:
    union = int((a | b).sum())
    return int((a & b).sum()) / union if union else 0.0


def _same(a: BoolArray, b: BoolArray) -> bool:
    """Two detections of one kind are one element: they overlap, or one nearly lies within the other at a comparable size."""
    if _overlap(a, b) >= SAME_ELEMENT:
        return True
    small, large = sorted((int(a.sum()), int(b.sum())))
    return small >= NESTED_SIZE * large and int((a & b).sum()) >= NESTED * small


def seen_elements(
    instances: Sequence[Instance], names: Sequence[str], kinds: Mapping[str, str], size: tuple[int, int]
) -> list[Seen]:
    """The detections of one picture as elements: highest score first, a detection that overlaps a kept one of the same
    kind, or nearly lies within one at a comparable size, is the same element (the names overlap: "door" and "the
    arched doors"; a fireplace and its opening)."""
    kept: list[Seen] = []
    for instance in sorted(instances, key=lambda i: -i.score):
        label = names[instance.label]
        mask = _shrink(instance.mask, size)
        if not mask.any():
            continue
        if any(s.kind == kinds[label] and _same(s.mask, mask) for s in kept):
            continue
        kept.append(Seen(label, kinds[label], instance.score, mask, box_of(mask) or [0.0, 0.0, 0.0, 0.0]))
    return kept


def match(before: Sequence[Seen], after: Sequence[Seen]) -> list[tuple[int, int, float]]:
    """Pairs (original, candidate, overlap), greedy by overlap: the same name first, then any name of the same kind."""
    pairs = [
        (before[i].label == after[j].label, overlap, i, j)
        for i in range(len(before))
        for j in range(len(after))
        if before[i].kind == after[j].kind and (overlap := _overlap(before[i].mask, after[j].mask)) >= MIN_MATCH
    ]
    pairs.sort(key=lambda p: (not p[0], -p[1]))
    used_before: set[int] = set()
    used_after: set[int] = set()
    matched: list[tuple[int, int, float]] = []
    for _, overlap, i, j in pairs:
        if i in used_before or j in used_after:
            continue
        used_before.add(i)
        used_after.add(j)
        matched.append((i, j, overlap))
    return matched


def _inside(mask: BoolArray, region: BoolArray) -> float:
    area = int(mask.sum())
    return round(int((mask & region).sum()) / area, 3) if area else 0.0


def take_inventory(before: Sequence[Seen], after: Sequence[Seen], region: BoolArray) -> list[Element]:
    """Pure core: every element of either picture once, with its status; `region` is at the masks' size."""
    elements: list[Element] = []
    pairs = match(before, after)
    for i, j, overlap in pairs:
        a, b = before[i], after[j]
        share = _inside(b.mask, region)
        where = "inside" if share >= INSIDE else "outside"
        growth = int(b.mask.sum()) / max(1, int(a.mask.sum()))
        grown = b.mask & ~a.mask
        if b.kind == "movable" and where == "inside":
            status = "left"
        elif growth >= GROWTH and int((grown & region).sum()) * 2 >= int(grown.sum()):
            status = "revealed"
        elif overlap >= KEPT:
            status = "kept"
        else:
            status = "changed"
        elements.append(Element(b.label, b.kind, status, where, share, a.box, b.box, round(overlap, 3), round(growth, 2)))
    matched_before = {i for i, _, _ in pairs}
    matched_after = {j for _, j, _ in pairs}
    for i, a in enumerate(before):
        if i not in matched_before:
            share = _inside(a.mask, region)
            elements.append(Element(a.label, a.kind, "removed", "inside" if share >= INSIDE else "outside", share, a.box, None))
    for j, b in enumerate(after):
        if j in matched_after:
            continue
        share = _inside(b.mask, region)
        area = max(1, int(b.mask.sum()))
        stood = tuple(
            dict.fromkeys(a.label for a in before if a.kind == "movable" and int((a.mask & b.mask).sum()) / area >= STOOD)
        )
        elements.append(Element(b.label, b.kind, "new", "inside" if share >= INSIDE else "outside", share, None, b.box, stood=stood))
    return sorted(elements, key=_order)


def _as_asked(element: Element) -> bool:
    """A movable element removed, wherever it stood: what the rules ask for."""
    return element.status == "removed" and element.kind == "movable"


def _order(element: Element) -> tuple[int, int, str]:
    return (STATUS_ORDER.index(element.status), int(_as_asked(element)), element.label)


def summarize(elements: Sequence[Element]) -> str:
    """The inventory as the judge reads it: one line per element that bears on a defect, the rest rolled up."""
    lines = [
        "Elements of the room's rules, detected in both pictures and matched by place (inside = inside the region to "
        "empty; the detector misses and mislabels, so weigh this against the images; the numbers are the boxes of the "
        "annotated candidate):"
    ]
    listed = [(n, e) for n, e in enumerate(elements, start=1) if e.status != "kept" and not _as_asked(e)]
    for n, element in listed[:MAX_LINES]:
        text = f"{n}. {element.label} ({element.kind}): {element.status}, {element.where}"
        if element.status == "new" and element.stood:
            text += f", where the original showed {', '.join(element.stood)}"
        if element.status == "revealed" and element.growth is not None:
            text += f", {element.growth:.1f} times its visible area in the original"
        if element.status == "changed" and element.overlap is not None:
            text += f", outline overlap {element.overlap:.0%}"
        lines.append(text)
    if len(listed) > MAX_LINES:
        lines.append(f"... and {len(listed) - MAX_LINES} more")
    asked = Counter(e.label for e in elements if _as_asked(e))
    if asked:
        lines.append("Removed as asked (movable): " + ", ".join(_counted(asked)))
    kept = Counter(e.label for e in elements if e.status == "kept")
    if kept:
        lines.append("Kept unchanged: " + ", ".join(_counted(kept)))
    if len(lines) == 1:
        lines.append("no element of the rules was detected in either picture")
    counts = Counter(e.status for e in elements)
    lines.append("Counts: " + ", ".join(f"{status} {counts[status]}" for status in STATUS_ORDER if counts[status]))
    return "\n".join(lines)


def _counted(counter: Counter[str]) -> list[str]:
    return [label if count == 1 else f"{label} x{count}" for label, count in sorted(counter.items())]


def _font(size: int) -> Any:
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow before 10.1: one fixed size
        return ImageFont.load_default()


def annotate(candidate: Image.Image, elements: Sequence[Element]) -> Image.Image:
    """The candidate with every element that bears on a defect boxed in its status colour and numbered."""
    picture = candidate.convert("RGB").copy()
    draw = ImageDraw.Draw(picture)
    width, height = picture.size
    thickness = max(2, round(max(width, height) / 400))
    font = _font(max(12, round(max(width, height) / 50)))
    for n, element in enumerate(elements, start=1):
        if element.status not in COLOURS or _as_asked(element):
            continue
        box = element.box_candidate or element.box_original
        if box is None:
            continue
        x0, y0, x1, y1 = box[0] * width, box[1] * height, box[2] * width, box[3] * height
        colour = COLOURS[element.status]
        draw.rectangle((x0, y0, x1, y1), outline=colour, width=thickness)
        tag = str(n)
        left, top, right, bottom = draw.textbbox((x0, y0), tag, font=font)
        draw.rectangle((left - 2, top - 2, right + 2, bottom + 2), fill=colour)
        draw.text((x0, y0), tag, fill=(0, 0, 0), font=font)
    return picture


class _Detections:
    """Recent detections by picture, names and threshold: the original is detected once per photo, not per attempt."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._entries: OrderedDict[str, tuple[tuple[Instance, ...], bool]] = OrderedDict()

    def get(
        self, backend: SegmentBackend, image: Image.Image, names: list[str], threshold: float
    ) -> tuple[tuple[Instance, ...], bool]:
        digest = hashlib.sha256(np.asarray(image).tobytes())
        digest.update(repr((image.size, names, threshold, backend.ident)).encode())
        key = digest.hexdigest()
        with self._lock:
            if key in self._entries:
                self._entries.move_to_end(key)
                return self._entries[key]
        result = backend.segment(image, names, threshold)
        entry = (result.instances, result.fell_back_to_boxes)
        with self._lock:
            self._entries[key] = entry
            while len(self._entries) > CACHE_SIZE:
                self._entries.popitem(last=False)
        return entry


@dataclass
class ElementInventory(ServerTool):
    name: ClassVar[str] = "element_inventory"
    code_version: ClassVar[str] = "1"
    input_kinds: ClassVar[tuple[str, ...]] = (IMAGE, IMAGE, MASK)

    def __post_init__(self) -> None:
        self._detections = _Detections()

    def parse_params(self, params: Mapping[str, Any]) -> dict[str, Any]:
        refuse_unknown(params, {"fixed", "movable", "threshold"}, self.name)
        seen: set[str] = set()
        lists: dict[str, list[str]] = {}
        for kind in ("fixed", "movable"):
            names = params.get(kind, [])
            if not isinstance(names, list):
                raise ApiError("bad_request", f"{self.name}: {kind} must be a list of element names")
            for label in names:
                if not isinstance(label, str) or not LABEL.fullmatch(label):
                    raise ApiError("bad_request", f"{self.name}: each name is 1 to 80 letters, digits, spaces, hyphens or apostrophes")
                if label.lower() in seen:
                    raise ApiError("bad_request", f"{self.name}: name {label!r} appears twice")
                seen.add(label.lower())
            lists[kind] = list(names)
        if not 1 <= len(seen) <= MAX_NAMES:
            raise ApiError("bad_request", f"{self.name}: 1 to {MAX_NAMES} names in fixed and movable together")
        threshold = number_param(params, "threshold", DEFAULT_THRESHOLD, 0.01, 1.0, self.name)
        return {"fixed": lists["fixed"], "movable": lists["movable"], "threshold": threshold}

    def run(self, images: Sequence[Image.Image], params: Mapping[str, Any]) -> ToolOutput:
        backend: SegmentBackend = self.backend  # type: ignore[assignment]
        original, candidate, region_image = images
        scale = min(1.0, WORK_SIDE / max(original.size))
        size = (max(1, round(original.width * scale)), max(1, round(original.height * scale)))
        original, candidate = imaging.resize_to(original, size), imaging.resize_to(candidate, size)
        names = [*params["fixed"], *params["movable"]]
        kinds = {**{n: "fixed" for n in params["fixed"]}, **{n: "movable" for n in params["movable"]}}
        threshold = float(params["threshold"])
        match_scale = min(1.0, MATCH_SIDE / max(size))
        match_size = (max(1, round(size[0] * match_scale)), max(1, round(size[1] * match_scale)))
        region = imaging.to_mask(region_image, match_size)
        found_before, fell_back_before = self._detections.get(backend, original, names, threshold)
        found_after, fell_back_after = self._detections.get(backend, candidate, names, threshold)
        before = seen_elements(found_before, names, kinds, match_size)
        after = seen_elements(found_after, names, kinds, match_size)
        elements = take_inventory(before, after, region)
        counts = Counter(e.status for e in elements)
        measures: dict[str, Any] = {
            "elements": [e.as_dict(n) for n, e in enumerate(elements, start=1)],
            "counts": {status: counts[status] for status in STATUS_ORDER},
            "compared_at": [size[0], size[1]],
            "candidate_resized": bool(images[1].size != images[0].size),
            "fell_back_to_boxes": fell_back_before or fell_back_after,
            "threshold": threshold,
            "legend": LEGEND,
        }
        return ToolOutput({"annotated": annotate(candidate, elements)}, measures, summarize(elements))
