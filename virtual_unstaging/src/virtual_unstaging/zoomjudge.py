"""The zoom judge: a separate judge call on one attempt's zooms, one closed question per zoom with several answers
allowed, and its strict parsing (design/defect_detectors.md: The zoom judge)."""

from __future__ import annotations

import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass

from virtual_unstaging import imaging
from virtual_unstaging.domain import JudgeRequestOptions, ModelRef, canonical_json, sha256_bytes, sha256_text
from virtual_unstaging.instructions import load_base
from virtual_unstaging.judge import ContractError, ImagePart, JudgeRequest
from virtual_unstaging.zooms import INSIDE, OUTSIDE, Place

ANSWERS = {
    OUTSIDE: ("same", "sharper_or_softer", "added", "removed", "changed_shape", "tone", "surface_wrong"),
    INSIDE: ("continues", "revealed", "invented_element", "invented_opening", "object_left", "surface_wrong"),
}
SEVERITIES = ("none", "minor", "blocking")
COMMENT_MAX = 120
MAX_ANSWERS = 4


@dataclass(frozen=True)
class ZoomAnswer:
    n: int
    answers: tuple[str, ...]
    severity: str
    comment: str


def build(model: ModelRef, zooms: Sequence[tuple[Place, bytes]], image_part: ImagePart,
          text_part: Callable[[str], dict[str, object]], options: JudgeRequestOptions) -> JudgeRequest:
    """The request: the instructions, then per zoom its kind and its image; the answer schema has one item per zoom."""
    system = load_base("zoom_judge")
    content: list[dict[str, object]] = []
    identity: list[object] = []
    media_type = "image/jpeg" if options.image_format == "jpeg" else "image/png"
    for n, (place, data) in enumerate(zooms, start=1):
        shown = imaging.shrink(data, options.image_side, options.image_format) \
            if options.image_side or options.image_format != "png" else data
        content.append(text_part(f"Zoom {n} ({place.where}): original left, edited right."))
        content.append(image_part(shown, media_type))
        identity.append([place.where, sha256_bytes(shown)])
    text = (f"Answer for each of the {len(zooms)} zooms under its key (zoom_1, zoom_2, ...): answers, severity, comment "
            f"(under {COMMENT_MAX} characters).")
    content.append(text_part(text))
    schema = output_schema([place for place, _ in zooms])
    messages: list[dict[str, object]] = [{"role": "system", "content": system}, {"role": "user", "content": content}]
    sha = sha256_text(canonical_json({"model": [model.name, model.revision], "system": system, "images": identity,
                                      "text": text, "schema": schema}))
    return JudgeRequest(messages, schema, sha)


def output_schema(zooms: Sequence[Place]) -> dict[str, object]:
    """One key per zoom (`zoom_<n>`), each offering only its own kind's answers: constrained decoding cannot give an
    inside answer to an outside zoom (a single list of every answer let a judge do so)."""

    def item(place: Place) -> dict[str, object]:
        # no uniqueItems: vLLM's grammar backend refuses it; a repeated answer is dropped when parsed
        return {"type": "object",
                "properties": {"answers": {"type": "array", "items": {"enum": list(ANSWERS[place.where])}, "minItems": 1,
                                           "maxItems": MAX_ANSWERS},
                               "severity": {"enum": list(SEVERITIES)},
                               "comment": {"type": "string", "maxLength": COMMENT_MAX}},
                "required": ["answers", "severity", "comment"], "additionalProperties": False}

    keys = [f"zoom_{n}" for n in range(1, len(zooms) + 1)]
    return {"type": "object", "properties": {k: item(p) for k, p in zip(keys, zooms, strict=True)}, "required": keys,
            "additionalProperties": False}


def parse(raw: str, zooms: Sequence[Place]) -> tuple[ZoomAnswer, ...]:
    """Each zoom answered under its key, with answers of its own kind; anything else breaks the contract."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ContractError(f"not JSON: {error}") from error
    keys = [f"zoom_{n}" for n in range(1, len(zooms) + 1)]
    if not isinstance(data, dict) or sorted(data) != sorted(keys):
        raise ContractError(f"expected exactly the keys {', '.join(keys)}")
    found = []
    for n, (key, place) in enumerate(zip(keys, zooms, strict=True), start=1):
        item = data[key]
        if not isinstance(item, dict) or set(item) != {"answers", "severity", "comment"}:
            raise ContractError(f"{key} needs exactly answers, severity, comment")
        answers, severity, comment = item["answers"], item["severity"], item["comment"]
        allowed = ANSWERS[place.where]
        if isinstance(answers, list):
            answers = list(dict.fromkeys(answers))
        if (not isinstance(answers, list) or not 1 <= len(answers) <= MAX_ANSWERS
                or any(a not in allowed for a in answers)):
            raise ContractError(f"{key} ({place.where}): answers must be 1 to {MAX_ANSWERS} of {', '.join(allowed)}")
        if severity not in SEVERITIES or not isinstance(comment, str):
            raise ContractError(f"{key}: bad severity or comment")
        found.append(ZoomAnswer(n, tuple(answers), severity, comment[:COMMENT_MAX]))
    return tuple(found)
