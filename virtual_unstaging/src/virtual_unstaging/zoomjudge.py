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
    text = (f"Answer for each of the {len(zooms)} zooms, in order: zoom number, answers, severity, comment (under "
            f"{COMMENT_MAX} characters).")
    content.append(text_part(text))
    schema = output_schema(len(zooms))
    messages: list[dict[str, object]] = [{"role": "system", "content": system}, {"role": "user", "content": content}]
    sha = sha256_text(canonical_json({"model": [model.name, model.revision], "system": system, "images": identity,
                                      "text": text, "schema": schema}))
    return JudgeRequest(messages, schema, sha)


def output_schema(count: int) -> dict[str, object]:
    every = sorted({a for answers in ANSWERS.values() for a in answers})
    item = {
        "type": "object",
        "properties": {
            "zoom": {"type": "integer", "minimum": 1, "maximum": count},
            "answers": {"type": "array", "items": {"enum": every}, "minItems": 1, "maxItems": MAX_ANSWERS,
                        "uniqueItems": True},
            "severity": {"enum": list(SEVERITIES)},
            "comment": {"type": "string", "maxLength": COMMENT_MAX},
        },
        "required": ["zoom", "answers", "severity", "comment"],
        "additionalProperties": False,
    }
    return {"type": "object", "properties": {"zooms": {"type": "array", "items": item, "minItems": count,
                                                       "maxItems": count}},
            "required": ["zooms"], "additionalProperties": False}


def parse(raw: str, zooms: Sequence[Place]) -> tuple[ZoomAnswer, ...]:
    """Each zoom answered once, with answers of its own kind; anything else breaks the contract."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ContractError(f"not JSON: {error}") from error
    items = data.get("zooms") if isinstance(data, dict) else None
    if not isinstance(items, list) or len(items) != len(zooms):
        raise ContractError(f"expected {len(zooms)} zoom answers")
    found: dict[int, ZoomAnswer] = {}
    for item in items:
        if not isinstance(item, dict) or set(item) != {"zoom", "answers", "severity", "comment"}:
            raise ContractError("a zoom answer needs exactly zoom, answers, severity, comment")
        n, answers, severity, comment = item["zoom"], item["answers"], item["severity"], item["comment"]
        if not isinstance(n, int) or not 1 <= n <= len(zooms) or n in found:
            raise ContractError(f"zoom number {n!r} out of range or repeated")
        allowed = ANSWERS[zooms[n - 1].where]
        if (not isinstance(answers, list) or not 1 <= len(answers) <= MAX_ANSWERS or len(set(answers)) != len(answers)
                or any(a not in allowed for a in answers)):
            raise ContractError(f"zoom {n} ({zooms[n - 1].where}): answers must be 1 to {MAX_ANSWERS} of {', '.join(allowed)}")
        if severity not in SEVERITIES or not isinstance(comment, str):
            raise ContractError(f"zoom {n}: bad severity or comment")
        found[n] = ZoomAnswer(n, tuple(answers), severity, comment[:COMMENT_MAX])
    return tuple(found[n] for n in sorted(found))
