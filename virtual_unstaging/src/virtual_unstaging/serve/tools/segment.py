"""`segment_elements`: open-vocabulary detection (Grounding DINO) then promptable segmentation (SAM 2.1)."""

from __future__ import annotations

import logging
import re
from abc import abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

import numpy as np
from PIL import Image

from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.errors import ApiError
from virtual_unstaging.serve.pixels import BoolArray, FloatArray
from virtual_unstaging.serve.tools.base import (
    IMAGE,
    Backend,
    ServerTool,
    ToolOutput,
    number_param,
    refuse_unknown,
)

LOG = logging.getLogger("virtual_unstaging.serve")
LABEL = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 '\-]{0,79}$")
MAX_LABELS = 64
DEFAULT_THRESHOLD = 0.3


@dataclass(frozen=True)
class Instance:
    label: int  # index into the labels asked for
    box: tuple[float, float, float, float]  # absolute pixels [x0, y0, x1, y1]
    score: float
    mask: BoolArray  # image-sized


@dataclass(frozen=True)
class SegmentResult:
    masks: list[BoolArray]  # one per label, in label order, image-sized
    detections: list[int]  # boxes kept per label
    fell_back_to_boxes: bool = False
    instances: tuple[Instance, ...] = ()  # one per box kept, highest score first


class SegmentBackend(Backend):
    @abstractmethod
    def segment(self, image: Image.Image, labels: list[str], threshold: float) -> SegmentResult: ...


def label_spans(token_ids: Sequence[int], separators: set[int], count: int) -> list[list[int]]:
    """Token positions of each label in the detector's prompt ("[CLS] a. b. c. [SEP]"): the runs between separators, in
    label order; ValueError when there are not `count` of them."""
    spans: list[list[int]] = []
    current: list[int] = []
    for position, token in enumerate(token_ids):
        if token in separators:
            if current:
                spans.append(current)
            current = []
        else:
            current.append(position)
    if current:
        spans.append(current)
    if len(spans) != count:
        raise ValueError(f"the prompt holds {len(spans)} labels, {count} were sent")
    return spans


def assign_labels(token_scores: FloatArray, spans: Sequence[Sequence[int]], threshold: float) -> list[tuple[int, int, float]]:
    """(query, label, score) for each detector query whose best label scores at least `threshold`: a label's score is
    its best token's, as Grounding DINO scores a phrase; each box gets the one label it matches best."""
    per_label = np.stack([token_scores[:, list(span)].max(axis=1) for span in spans], axis=1)
    best = per_label.argmax(axis=1)
    score = per_label[np.arange(per_label.shape[0]), best]
    return [(int(q), int(best[q]), float(score[q])) for q in np.flatnonzero(score >= threshold)]


def box_overlap(a: Sequence[float], b: Sequence[float]) -> float:
    """Intersection over union of two [x0, y0, x1, y1] boxes."""
    width = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    height = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    inter = width * height
    union = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter
    return inter / union if union > 0 else 0.0


def suppress(found: Sequence[tuple[int, list[float], float]], overlap: float) -> list[tuple[int, list[float], float]]:
    """Highest score first; a box of the same label overlapping a kept one by `overlap` or more is the same detection."""
    kept: list[tuple[int, list[float], float]] = []
    for item in sorted(found, key=lambda f: -f[2]):
        if not any(k[0] == item[0] and box_overlap(k[1], item[1]) >= overlap for k in kept):
            kept.append(item)
    return kept


def box_mask(box: Sequence[float], shape: tuple[int, int]) -> BoolArray:
    """A filled rectangle from absolute pixel box [x0, y0, x1, y1], clipped to the frame."""
    height, width = shape
    mask = np.zeros(shape, dtype=bool)
    x0, y0, x1, y1 = (int(round(v)) for v in box)
    mask[max(0, y0) : min(height, y1), max(0, x0) : min(width, x1)] = True
    return mask


class GroundedSam2Backend(SegmentBackend):
    """Grounding DINO boxes for the labels, SAM 2.1 masks for the boxes (both from transformers)."""

    detector_repository = "IDEA-Research/grounding-dino-base"
    detector_revision = "12bdfa3120f3e7ec7b434d90674b3396eccf88eb"
    segmenter_repository = "facebook/sam2.1-hiera-large"
    segmenter_revision = "665f8e2ad61cf5f53d65644ff27c8ee525124610"
    ident: ClassVar[str] = "grounding-dino-base+sam2.1-hiera-large"
    model: ClassVar[str] = "IDEA-Research/grounding-dino-base + facebook/sam2.1-hiera-large"
    labels_per_pass = 8  # the detector's text input is limited in length
    max_boxes = 48
    same_box = 0.7  # overlap above which two boxes of one label are one detection

    def __init__(self) -> None:
        super().__init__()
        self._device = "cpu"
        self._detector: Any = None
        self._detector_processor: Any = None
        self._segmenter: Any = None
        self._segmenter_processor: Any = None

    def load(self) -> None:
        import torch
        from transformers import AutoModelForZeroShotObjectDetection, AutoProcessor, Sam2Model, Sam2Processor

        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._detector_processor = AutoProcessor.from_pretrained(
            self.detector_repository, revision=self.detector_revision
        )
        self._detector = (
            AutoModelForZeroShotObjectDetection.from_pretrained(self.detector_repository, revision=self.detector_revision)
            .to(self._device)
            .eval()
        )
        self._segmenter_processor = Sam2Processor.from_pretrained(
            self.segmenter_repository, revision=self.segmenter_revision
        )
        self._segmenter = (
            Sam2Model.from_pretrained(self.segmenter_repository, revision=self.segmenter_revision)
            .to(self._device)
            .eval()
        )

    def segment(self, image: Image.Image, labels: list[str], threshold: float) -> SegmentResult:
        self.warm()
        import torch

        width, height = image.size
        found: list[tuple[int, list[float], float]] = []  # (label index, box, score)
        for start in range(0, len(labels), self.labels_per_pass):
            batch = labels[start : start + self.labels_per_pass]
            inputs = self._detector_processor(images=image, text=[[label.lower() for label in batch]], return_tensors="pt")
            inputs = inputs.to(self._device)
            with torch.no_grad():
                outputs = self._detector(**inputs)
            # Labels from the per-token scores, not from the decoded phrase: the tokenizer re-spaces names
            # ("built - in"), and a phrase may span several labels.
            tokenizer = self._detector_processor.tokenizer
            separators = {tokenizer.convert_tokens_to_ids("."), tokenizer.cls_token_id, tokenizer.sep_token_id}
            spans = label_spans(inputs.input_ids[0].tolist(), separators, len(batch))
            token_scores = outputs.logits[0].sigmoid().float().cpu().numpy()
            centres = outputs.pred_boxes[0].float().cpu().numpy()  # (cx, cy, w, h) in [0, 1]
            for query, local, score in assign_labels(token_scores, spans, threshold):
                cx, cy, w, h = (float(v) for v in centres[query])
                box = [(cx - w / 2) * width, (cy - h / 2) * height, (cx + w / 2) * width, (cy + h / 2) * height]
                found.append((start + local, box, score))
        found = suppress(found, self.same_box)[: self.max_boxes]
        masks = [np.zeros((height, width), dtype=bool) for _ in labels]
        counts = [0] * len(labels)
        if not found:
            return SegmentResult(masks, counts)
        boxes = [item[1] for item in found]
        fell_back = False
        try:
            inputs = self._segmenter_processor(images=image, input_boxes=[boxes], return_tensors="pt").to(self._device)
            with torch.no_grad():
                prediction = self._segmenter(**inputs, multimask_output=False)
            shaped = self._segmenter_processor.post_process_masks(prediction.pred_masks.cpu(), inputs["original_sizes"])[0]
            per_box = np.asarray(shaped).reshape(len(boxes), height, width).astype(bool)
        except Exception as error:  # a box is a coarser mask than SAM's, but better than none; the result says so
            LOG.warning("segmentation fell back to boxes: %s: %s", type(error).__name__, str(error)[:200])
            per_box = np.stack([box_mask(box, (height, width)) for box in boxes])
            fell_back = True
        instances: list[Instance] = []
        for (index, box, score), mask in zip(found, per_box, strict=True):
            masks[index] |= mask
            counts[index] += 1
            instances.append(Instance(index, (box[0], box[1], box[2], box[3]), score, mask))
        return SegmentResult(masks, counts, fell_back, tuple(instances))


_COLOURS: dict[str, Any] = {
    "red": lambda r, g, b: (r > 150) & (g < 100) & (b < 100),
    "green": lambda r, g, b: (g > 150) & (r < 100) & (b < 100),
    "blue": lambda r, g, b: (b > 150) & (r < 100) & (g < 100),
    "yellow": lambda r, g, b: (r > 150) & (g > 150) & (b < 100),
    "white": lambda r, g, b: (r > 215) & (g > 215) & (b > 215),
    "black": lambda r, g, b: (r < 40) & (g < 40) & (b < 40),
}


class ColourWordBackend(SegmentBackend):
    """A stand-in with no model: a label that holds a colour word finds the pixels of that colour."""

    ident: ClassVar[str] = "colour-words"
    model: ClassVar[str] = "none (test double: finds the colour named in the label)"

    def load(self) -> None:
        return None

    def segment(self, image: Image.Image, labels: list[str], threshold: float) -> SegmentResult:
        pixels = np.asarray(image.convert("RGB")).astype(int)
        r, g, b = pixels[..., 0], pixels[..., 1], pixels[..., 2]
        masks: list[BoolArray] = []
        instances: list[Instance] = []
        for index, label in enumerate(labels):
            word = next((w for w in label.lower().split() if w in _COLOURS), None)
            mask = np.asarray(_COLOURS[word](r, g, b), dtype=bool) if word else np.zeros(r.shape, dtype=bool)
            masks.append(mask)
            if mask.any():  # one instance per colour: the box around all its pixels
                rows, columns = np.where(mask.any(axis=1))[0], np.where(mask.any(axis=0))[0]
                box = (float(columns[0]), float(rows[0]), float(columns[-1] + 1), float(rows[-1] + 1))
                instances.append(Instance(index, box, 1.0, mask))
        return SegmentResult(masks, [int(m.any()) for m in masks], instances=tuple(instances))


@dataclass
class SegmentElements(ServerTool):
    name: ClassVar[str] = "segment_elements"
    code_version: ClassVar[str] = "2"
    input_kinds: ClassVar[tuple[str, ...]] = (IMAGE,)

    def parse_params(self, params: Mapping[str, Any]) -> dict[str, Any]:
        refuse_unknown(params, {"labels", "threshold"}, self.name)
        labels = params.get("labels")
        if not isinstance(labels, list) or not 1 <= len(labels) <= MAX_LABELS:
            raise ApiError("bad_request", f"{self.name}: labels must be a list of 1 to {MAX_LABELS} element names")
        seen: set[str] = set()
        for label in labels:
            if not isinstance(label, str) or not LABEL.fullmatch(label):
                raise ApiError("bad_request", f"{self.name}: each label is 1 to 80 letters, digits, spaces, hyphens or apostrophes")
            if label.lower() in seen:
                raise ApiError("bad_request", f"{self.name}: label {label!r} appears twice")
            seen.add(label.lower())
        threshold = number_param(params, "threshold", DEFAULT_THRESHOLD, 0.01, 1.0, self.name)
        return {"labels": list(labels), "threshold": threshold}

    def run(self, images: Sequence[Image.Image], params: Mapping[str, Any]) -> ToolOutput:
        backend: SegmentBackend = self.backend  # type: ignore[assignment]
        labels: list[str] = list(params["labels"])
        result = backend.segment(images[0], labels, float(params["threshold"]))
        union = np.zeros_like(result.masks[0])
        outputs: dict[str, Image.Image] = {}
        found: dict[str, float] = {}
        for index, (label, mask) in enumerate(zip(labels, result.masks, strict=True)):
            union |= mask
            found[label] = round(float(mask.mean()), 4)
            outputs[f"mask_{index}"] = imaging.mask_image(mask)
        outputs["mask"] = imaging.mask_image(union)
        measures: dict[str, Any] = {
            "found": found,
            "detections": dict(zip(labels, result.detections, strict=True)),
            "labels": labels,
            "union_share": round(float(union.mean()), 4),
            "threshold": params["threshold"],
            "fell_back_to_boxes": result.fell_back_to_boxes,
        }
        return ToolOutput(outputs, measures, _summary(labels, found, measures))


def _summary(labels: list[str], found: dict[str, float], measures: dict[str, Any]) -> str:
    present = [label for label in labels if found[label] > 0.0]
    missing = [label for label in labels if found[label] <= 0.0]
    if not present:
        text = f"none of the {len(labels)} elements was found: {', '.join(labels)}"
    else:
        parts = ", ".join(f"{label} {found[label]:.1%} ({measures['detections'][label]})" for label in present)
        text = f"found {len(present)} of {len(labels)} elements, together {measures['union_share']:.1%} of the frame: {parts}"
        if missing:
            text += f"; not found: {', '.join(missing)}"
    if measures["fell_back_to_boxes"]:
        text += "; the masks are the detection boxes (the segmentation step failed)"
    return text
