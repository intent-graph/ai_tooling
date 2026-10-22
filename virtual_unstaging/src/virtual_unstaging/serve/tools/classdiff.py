"""`class_diff`: semantic classes (ADE20K) of the original and the candidate, and what changed in and around the region."""

from __future__ import annotations

import re
from abc import abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

import numpy as np
from numpy.typing import NDArray
from PIL import Image

from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.errors import ApiError
from virtual_unstaging.serve.pixels import BoolArray, ByteArray, box_of, dilate_square, grey
from virtual_unstaging.serve.tools.base import (
    IMAGE,
    MASK,
    Backend,
    ServerTool,
    ToolOutput,
    number_param,
    refuse_unknown,
)

CLASS_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9 ;'\-]{0,59}$")
DEFAULT_OPENING_CLASSES = ("door", "window", "doorway")
# Words a person uses for an opening, as ADE20K names them (it has no "doorway" class).
ALIASES: dict[str, tuple[str, ...]] = {
    "door": ("door", "screen door"),
    "doorway": ("door",),
    "window": ("windowpane",),
}
WORK_SIDE = 1024  # long side the images are compared at
EDGE = 0.03  # width of the region's edge, as a fraction of the long side: what the original shows there continues inside
LEGEND = {
    "red": "pixels that became an opening class",
    "blue": "pixels that stopped being an opening class",
    "yellow": "pixels of a class that appeared (absent from the original in that zone)",
    "cyan": "pixels (original) of a class that vanished (absent from the candidate in that zone)",
    "uncoloured inside the region": "a class the original shows on the region's edge, continued into it",
    "brightness": "the region keeps full brightness; outside it the picture is dimmed",
}
_COLOURS = {"red": (255, 40, 40), "blue": (60, 120, 255), "yellow": (255, 210, 0), "cyan": (0, 210, 210)}

IntArray = NDArray[np.int32]


class ClassBackend(Backend):
    @abstractmethod
    def class_names(self) -> dict[int, str]:
        """Class id to ADE20K name; a name may hold synonyms separated by semicolons."""

    @abstractmethod
    def label_map(self, image: Image.Image) -> IntArray:
        """The class id of every pixel, at the image's own size."""


def short_name(name: str) -> str:
    return name.split(";")[0].strip()


def resolve_classes(requested: Sequence[str], names: Mapping[int, str]) -> dict[int, str]:
    """Class ids for the requested names: a person's word (door, window, doorway) or an ADE20K name or synonym."""
    synonyms = {i: {part.strip().lower() for part in name.split(";")} for i, name in names.items()}
    resolved: dict[int, str] = {}
    for word in requested:
        wanted = {word.lower(), *ALIASES.get(word.lower(), ())}
        ids = [i for i, tokens in synonyms.items() if tokens & wanted]
        if not ids:
            raise ApiError("bad_request", f"class_diff: no ADE20K class named {word!r}")
        for i in ids:
            resolved[i] = short_name(names[i])
    return resolved


@dataclass(frozen=True)
class ClassChanges:
    measures: dict[str, Any]
    became_opening: BoolArray
    lost_opening: BoolArray
    appeared: BoolArray
    vanished: BoolArray


def _present(ids: IntArray, zone: BoolArray, count: int) -> NDArray[np.float64]:
    total = int(zone.sum())
    if total == 0:
        return np.zeros(count)
    return np.bincount(ids[zone], minlength=count) / total


def _class_changes(
    original: IntArray,
    candidate: IntArray,
    zone: BoolArray,
    names: Mapping[int, str],
    min_share: float,
    continued_ids: frozenset[int] = frozenset(),
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], BoolArray, BoolArray, list[dict[str, Any]]]:
    """Classes present in one picture and absent in the other, within a zone, with a box around their pixels; a class in
    `continued_ids` (shown by the original next to the zone) is continued, not appeared."""
    count = max(names) + 1
    before, after = _present(original, zone, count), _present(candidate, zone, count)
    appeared: list[dict[str, Any]] = []
    vanished: list[dict[str, Any]] = []
    continued: list[dict[str, Any]] = []
    appeared_pixels = np.zeros(zone.shape, dtype=bool)
    vanished_pixels = np.zeros(zone.shape, dtype=bool)
    for class_id, name in names.items():
        if after[class_id] >= min_share and before[class_id] < min_share and class_id in continued_ids:
            pixels = (candidate == class_id) & zone
            continued.append({"class": short_name(name), "share": round(float(after[class_id]), 4), "box": box_of(pixels)})
        elif after[class_id] >= min_share and before[class_id] < min_share:
            pixels = (candidate == class_id) & zone
            appeared.append({"class": short_name(name), "share": round(float(after[class_id]), 4), "box": box_of(pixels)})
            appeared_pixels |= pixels
        elif before[class_id] >= min_share and after[class_id] < min_share:
            pixels = (original == class_id) & zone
            vanished.append({"class": short_name(name), "share": round(float(before[class_id]), 4), "box": box_of(pixels)})
            vanished_pixels |= pixels
    appeared.sort(key=lambda item: -item["share"])
    vanished.sort(key=lambda item: -item["share"])
    continued.sort(key=lambda item: -item["share"])
    return appeared[:8], vanished[:8], appeared_pixels, vanished_pixels, continued[:8]


def compare_classes(
    original: IntArray,
    candidate: IntArray,
    region: BoolArray,
    names: Mapping[int, str],
    opening_ids: Mapping[int, str],
    min_share: float,
) -> ClassChanges:
    """Pure core of `class_diff`: all arrays share one size; `region` is where the generator was asked to edit."""
    outside = ~region
    opening = np.isin(candidate, list(opening_ids))
    was_opening = np.isin(original, list(opening_ids))
    became, lost = opening & ~was_opening, was_opening & ~opening
    region_size, outside_size = int(region.sum()), int(outside.sum())
    edge = dilate_square(region, max(1, round(EDGE * max(region.shape)))) & outside
    on_edge = _present(original, edge, max(names) + 1)
    continued_ids = frozenset(int(i) for i in np.flatnonzero(on_edge >= min_share))
    inside_appeared, inside_vanished, appeared_in, vanished_in, inside_continued = _class_changes(
        original, candidate, region, names, min_share, continued_ids
    )
    outside_appeared, outside_vanished, appeared_out, vanished_out, _ = _class_changes(
        original, candidate, outside, names, min_share
    )
    measures: dict[str, Any] = {
        "opening_classes": sorted(set(opening_ids.values())),
        "region_share": round(region_size / region.size, 4),
        "opening_share_of_region": round(int((became & region).sum()) / region_size, 4) if region_size else 0.0,
        "opening_box": box_of(became & region),
        "opening_share_outside": round(int((became & outside).sum()) / outside_size, 4) if outside_size else 0.0,
        "opening_at_edge": bool(any(i in continued_ids for i in opening_ids)),
        "inside": {"appeared": inside_appeared, "vanished": inside_vanished, "continued": inside_continued},
        "outside": {"appeared": outside_appeared, "vanished": outside_vanished},
        "min_share": min_share,
        "legend": LEGEND,
    }
    return ClassChanges(measures, became, lost, appeared_in | appeared_out, vanished_in | vanished_out)


def render_map(base: ByteArray, region: BoolArray, changes: ClassChanges) -> Image.Image:
    """The candidate in grey, dimmed outside the region, with the changes painted over it in colour."""
    luma = grey(base)
    shade = np.where(region, 0.85, 0.4).astype(np.float32)
    canvas = np.repeat((luma * shade)[..., None], 3, axis=2).astype(np.uint8)
    for colour, layer in (
        ("cyan", changes.vanished),
        ("yellow", changes.appeared),
        ("blue", changes.lost_opening),
        ("red", changes.became_opening),
    ):
        canvas[layer] = _COLOURS[colour]
    return Image.fromarray(canvas)


def _describe(item: Mapping[str, Any]) -> str:
    box = item["box"]
    where = f" at ({box[0]:.2f}, {box[1]:.2f})-({box[2]:.2f}, {box[3]:.2f})" if box else ""
    return f"{item['class']} {item['share']:.1%}{where}"


def summarize(measures: Mapping[str, Any]) -> str:
    opening_names = "/".join(measures["opening_classes"])
    if measures["region_share"] == 0:
        inside = "the region is empty, nothing to compare inside it"
    elif measures["opening_share_of_region"] > 0:
        box = measures["opening_box"]
        inside = (
            f"inside the removed region, {measures['opening_share_of_region']:.1%} of pixels became {opening_names}, "
            f"at ({box[0]:.2f}, {box[1]:.2f})-({box[2]:.2f}, {box[3]:.2f})"
        )
        if measures.get("opening_at_edge"):
            inside += (
                f", continuing a {opening_names} the original shows at the region's edge (revealed or extended, "
                "not necessarily invented)"
            )
    else:
        inside = f"inside the removed region, no pixel became {opening_names}"
    notes = []
    for zone, where in (("inside", "inside the region"), ("outside", "outside the region")):
        for kind in ("appeared", "vanished"):
            items = measures[zone][kind][:3]
            if items:
                notes.append(f"{where}, class {kind}: " + "; ".join(_describe(item) for item in items))
    continued = measures["inside"].get("continued", [])[:3]
    if continued:
        notes.append(
            "inside the region, class continued from the region's edge in the original: "
            + "; ".join(_describe(item) for item in continued)
        )
    if not notes:
        notes.append("no class appeared or vanished in or outside the region")
    return "; ".join([inside, *notes])


@dataclass
class ClassDiff(ServerTool):
    name: ClassVar[str] = "class_diff"
    code_version: ClassVar[str] = "2"
    input_kinds: ClassVar[tuple[str, ...]] = (IMAGE, IMAGE, MASK)

    def parse_params(self, params: Mapping[str, Any]) -> dict[str, Any]:
        refuse_unknown(params, {"opening_classes", "min_share"}, self.name)
        classes = params.get("opening_classes", list(DEFAULT_OPENING_CLASSES))
        if not isinstance(classes, list) or not 1 <= len(classes) <= 16:
            raise ApiError("bad_request", f"{self.name}: opening_classes must be a list of 1 to 16 class names")
        for word in classes:
            if not isinstance(word, str) or not CLASS_NAME.fullmatch(word):
                raise ApiError("bad_request", f"{self.name}: {word!r} is not a class name")
        return {"opening_classes": list(classes), "min_share": number_param(params, "min_share", 0.005, 0.0001, 0.5, self.name)}

    def run(self, images: Sequence[Image.Image], params: Mapping[str, Any]) -> ToolOutput:
        backend: ClassBackend = self.backend  # type: ignore[assignment]
        original, candidate, region_image = images
        scale = min(1.0, WORK_SIDE / max(original.size))
        size = (max(1, round(original.width * scale)), max(1, round(original.height * scale)))
        original, candidate = imaging.resize_to(original, size), imaging.resize_to(candidate, size)
        region = imaging.to_mask(region_image, size)
        names = backend.class_names()
        opening_ids = resolve_classes(params["opening_classes"], names)
        changes = compare_classes(
            backend.label_map(original), backend.label_map(candidate), region, names, opening_ids, float(params["min_share"])
        )
        changes.measures["candidate_resized"] = bool(images[1].size != images[0].size)
        changes.measures["compared_at"] = [size[0], size[1]]
        picture = render_map(np.asarray(candidate), region, changes)
        return ToolOutput({"map": picture}, changes.measures, summarize(changes.measures))


class SegformerAdeBackend(ClassBackend):
    """SegFormer-B2 fine-tuned on ADE20K (150 classes), from transformers."""

    repository = "nvidia/segformer-b2-finetuned-ade-512-512"
    revision = "de01bae28967510f9ddd496c60a969357195400c"
    ident: ClassVar[str] = "segformer-b2-ade20k"
    model: ClassVar[str] = "nvidia/segformer-b2-finetuned-ade-512-512"

    def __init__(self) -> None:
        super().__init__()
        self._device = "cpu"
        self._processor: Any = None
        self._network: Any = None

    def load(self) -> None:
        import torch
        from transformers import AutoImageProcessor, SegformerForSemanticSegmentation

        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._processor = AutoImageProcessor.from_pretrained(self.repository, revision=self.revision)
        self._network = (
            SegformerForSemanticSegmentation.from_pretrained(self.repository, revision=self.revision)
            .to(self._device)
            .eval()
        )

    def class_names(self) -> dict[int, str]:
        self.warm()
        return {int(i): str(name) for i, name in self._network.config.id2label.items()}

    def label_map(self, image: Image.Image) -> IntArray:
        self.warm()
        import torch

        inputs = self._processor(images=image, return_tensors="pt").to(self._device)
        with torch.no_grad():
            logits = self._network(**inputs).logits
            full = torch.nn.functional.interpolate(logits, size=(image.height, image.width), mode="bilinear", align_corners=False)
            return np.asarray(full.argmax(dim=1)[0].cpu().numpy(), dtype=np.int32)


class BrightnessClassBackend(ClassBackend):
    """A stand-in with no model: bright pixels are windowpane, dark ones door, the rest wall."""

    ident: ClassVar[str] = "brightness-classes"
    model: ClassVar[str] = "none (test double: bright = windowpane, dark = door, else wall)"

    def load(self) -> None:
        return None

    def class_names(self) -> dict[int, str]:
        return {0: "wall", 1: "door", 2: "windowpane"}

    def label_map(self, image: Image.Image) -> IntArray:
        luma = grey(np.asarray(image.convert("RGB")))
        return np.where(luma >= 200, 2, np.where(luma <= 50, 1, 0)).astype(np.int32)
