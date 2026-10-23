"""The zoom judge: a separate judge call on one attempt's cards, the owner's one question per card ("apart from
furniture and belongings being gone, is anything wrong in AFTER?"), and its strict parsing (design/defect_detectors.md:
The zoom judge)."""

from __future__ import annotations

import json
from collections.abc import Callable, Sequence
from dataclasses import dataclass

from virtual_unstaging import imaging
from virtual_unstaging.domain import JudgeRequestOptions, ModelRef, canonical_json, sha256_bytes, sha256_text
from virtual_unstaging.instructions import load_base
from virtual_unstaging.judge import ContractError, ImagePart, JudgeRequest
from virtual_unstaging.zooms import Place

ANSWERS = ("none", "minor", "blocking")  # the owner's three buttons: nothing wrong, a touch-up fixes it, unusable
WHAT_MAX = 120


@dataclass(frozen=True)
class ZoomAnswer:
    n: int
    severity: str
    what: str


def build(model: ModelRef, zooms: Sequence[tuple[Place, bytes]], image_part: ImagePart,
          text_part: Callable[[str], dict[str, object]], options: JudgeRequestOptions) -> JudgeRequest:
    """The request: the instructions, then the cards in order; the answer schema has one key per card."""
    system = load_base("zoom_judge")
    content: list[dict[str, object]] = []
    identity: list[object] = []
    media_type = "image/jpeg" if options.image_format == "jpeg" else "image/png"
    for n, (place, data) in enumerate(zooms, start=1):
        shown = imaging.shrink(data, options.image_side, options.image_format) \
            if options.image_side or options.image_format != "png" else data
        content.append(text_part(f"Card {n}."))
        content.append(image_part(shown, media_type))
        identity.append([place.where, sha256_bytes(shown)])
    text = (f"Answer for each of the {len(zooms)} cards under its key (zoom_1, zoom_2, ...): is anything wrong in AFTER, "
            f"apart from furniture and belongings being gone (none, minor, blocking), and what (under {WHAT_MAX} characters).")
    content.append(text_part(text))
    schema = output_schema([place for place, _ in zooms])
    messages: list[dict[str, object]] = [{"role": "system", "content": system}, {"role": "user", "content": content}]
    sha = sha256_text(canonical_json({"model": [model.name, model.revision], "system": system, "images": identity,
                                      "text": text, "schema": schema}))
    return JudgeRequest(messages, schema, sha)


def output_schema(zooms: Sequence[Place]) -> dict[str, object]:
    """One key per card (`zoom_<n>`): the answer among the three, and what is wrong."""
    item = {"type": "object",
            "properties": {"answer": {"enum": list(ANSWERS)}, "what": {"type": "string", "maxLength": WHAT_MAX}},
            "required": ["answer", "what"], "additionalProperties": False}
    keys = [f"zoom_{n}" for n in range(1, len(zooms) + 1)]
    return {"type": "object", "properties": {k: item for k in keys}, "required": keys, "additionalProperties": False}


def parse(raw: str, zooms: Sequence[Place]) -> tuple[ZoomAnswer, ...]:
    """Each card answered under its key with one of the three answers; anything else breaks the contract."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ContractError(f"not JSON: {error}") from error
    keys = [f"zoom_{n}" for n in range(1, len(zooms) + 1)]
    if not isinstance(data, dict) or sorted(data) != sorted(keys):
        raise ContractError(f"expected exactly the keys {', '.join(keys)}")
    found = []
    for n, key in enumerate(keys, start=1):
        item = data[key]
        if not isinstance(item, dict) or set(item) != {"answer", "what"}:
            raise ContractError(f"{key} needs exactly answer and what")
        if item["answer"] not in ANSWERS or not isinstance(item["what"], str):
            raise ContractError(f"{key}: answer must be one of {', '.join(ANSWERS)}, what a text")
        found.append(ZoomAnswer(n, item["answer"], item["what"][:WHAT_MAX]))
    return tuple(found)
