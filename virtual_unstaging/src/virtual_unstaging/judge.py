"""The judge: build its request (instructions, images, tool summaries, dimensions), its output contract,
and parse its answer strictly at the edge (design/loop1.md: The judge call)."""

from __future__ import annotations

import json
import re
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from typing import Any, Literal

from virtual_unstaging import imaging
from virtual_unstaging.domain import (
    MAX_FINDINGS,
    MAX_MOVES,
    Box,
    DefectType,
    Dimension,
    Finding,
    JudgeRequestOptions,
    ModelRef,
    Move,
    Point,
    Severity,
    canonical_json,
    sha256_bytes,
    sha256_text,
)
from virtual_unstaging.instructions import InstructionStack, render

BoxScale = Literal["unit", "per_mille"]
CRITIQUE_MAX = 600

# A chat backend: (messages, schema) -> the answer's text. Bound to an endpoint by the caller; faked in tests.
Chat = Callable[[list[dict[str, object]], dict[str, object]], str]
ImagePart = Callable[[bytes, str], dict[str, object]]


class ContractError(ValueError):
    """The judge's answer does not meet the output contract."""


@dataclass(frozen=True)
class JudgeImage:
    label: str
    data: bytes


@dataclass(frozen=True)
class JudgeInput:
    images: tuple[JudgeImage, ...]  # original, candidate, outline, then tool images, in that order
    tool_summaries: tuple[tuple[str, str], ...]
    fixed: tuple[str, ...]
    movable: tuple[str, ...]
    history: tuple[str, ...]
    dimensions: tuple[Dimension, ...]
    point: Point


@dataclass(frozen=True)
class JudgeOutput:
    findings: tuple[Finding, ...]
    own_verdict: str
    critique: str
    moves: tuple[Move, ...]


@dataclass
class JudgeRequest:
    messages: list[dict[str, object]]
    schema: dict[str, object]
    request_sha256: str
    meta: dict[str, Any] = field(default_factory=dict)


class Judge:
    def __init__(
        self,
        model: ModelRef,
        stack: InstructionStack,
        defects: Sequence[DefectType],
        box_scale: BoxScale,
        image_part: ImagePart,
        text_part: Callable[[str], dict[str, object]],
        request: JudgeRequestOptions | None = None,
    ) -> None:
        self.model = model
        self.stack = stack
        self.defects = tuple(defects)
        self.box_scale = box_scale
        self.image_part = image_part
        self.text_part = text_part
        self.request = request or JudgeRequestOptions()

    def build(self, judge_input: JudgeInput) -> JudgeRequest:
        system = render(
            self.stack.template(),
            {},
            {
                "defects": "\n".join(f"- `{d.code}`: {d.description}" for d in self.defects),
                "box_convention": _BOX_TEXT[self.box_scale],
                "fixed": list(judge_input.fixed),
                "movable": list(judge_input.movable),
            },
        )
        content: list[dict[str, object]] = []
        identity: list[object] = []
        options = self.request
        reshape = options.image_side > 0 or options.image_format != "png"
        media_type = "image/jpeg" if options.image_format == "jpeg" else "image/png"
        for index, image in enumerate(judge_input.images, start=1):
            data = imaging.shrink(image.data, options.image_side, options.image_format) if reshape else image.data
            content.append(self.text_part(f"Image {index}: {image.label}."))
            content.append(self.image_part(data, media_type))
            identity.append([image.label, sha256_bytes(data)])
        text = _request_text(judge_input) + _brevity(options)
        content.append(self.text_part(text))
        schema = output_schema(self.defects, judge_input.dimensions, options)
        messages: list[dict[str, object]] = [
            {"role": "system", "content": system},
            {"role": "user", "content": content},
        ]
        sha = sha256_text(
            canonical_json(
                {
                    "model": [self.model.name, self.model.revision],
                    "system": system,
                    "images": identity,
                    "text": text,
                    "schema": schema,
                }
            )
        )
        return JudgeRequest(messages, schema, sha)

    def parse(self, raw: str, dimensions: Sequence[Dimension], point: Point) -> JudgeOutput:
        return parse_answer(raw, {d.code for d in self.defects}, dimensions, point, self.box_scale)


_BOX_TEXT: dict[str, str] = {
    "unit": "as [x0, y0, x1, y1] in fractions of the width and height, from 0 to 1, origin at the top left",
    "per_mille": "as [x0, y0, x1, y1] in integers from 0 to 1000 relative to the width and height, origin at the "
    "top left",
}


def _request_text(judge_input: JudgeInput) -> str:
    lines = ["Tool measurements:"]
    lines += [f"- {tool}: {summary}" for tool, summary in judge_input.tool_summaries] or ["- none"]
    lines += ["", "Earlier attempts on this photo:"]
    lines += [f"- {entry}" for entry in judge_input.history] or ["- none, this is the first"]
    lines += ["", "Dimensions you may move, with their levels; the current level is marked with *:"]
    current = judge_input.point.as_dict()
    for dim in judge_input.dimensions:
        levels = ", ".join(("*" if lv.ordinal == current.get(dim.key) else "") + lv.label for lv in dim.levels)
        lines.append(f"- {dim.key} ({dim.input}): {levels}")
    return "\n".join(lines)


def _brevity(options: JudgeRequestOptions) -> str:
    """The answer's caps, stated in the request so the model writes short instead of being cut off; '' when uncapped."""
    parts = []
    if (options.max_findings, options.max_moves) != (MAX_FINDINGS, MAX_MOVES):
        parts.append(f"at most {options.max_findings} findings and {options.max_moves} moves")
    if options.comment_chars:
        parts.append(f"each comment and reason under {options.comment_chars} characters")
    if options.critique_chars:
        parts.append(f"the critique under {options.critique_chars} characters")
    return "\n\nKeep the answer short: " + "; ".join(parts) + "." if parts else ""


def _text_schema(chars: int) -> dict[str, object]:
    return {"type": "string", "maxLength": chars} if chars else {"type": "string"}


def output_schema(
    defects: Sequence[DefectType], dimensions: Sequence[Dimension], options: JudgeRequestOptions | None = None
) -> dict[str, object]:
    """The output contract, generated from the run's defects and dimensions: one source for decoding and parsing."""
    options = options or JudgeRequestOptions()
    codes = [d.code for d in defects]
    box = {"anyOf": [{"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4}, {"type": "null"}]}
    finding = {
        "type": "object",
        "properties": {
            "code": {"type": "string", "enum": codes},
            "severity": {"type": "string", "enum": ["minor", "blocking"]},
            "box": box,
            "comment": _text_schema(options.comment_chars),
        },
        "required": ["code", "severity", "box", "comment"],
        "additionalProperties": False,
    }
    move_variants = [
        {
            "type": "object",
            "properties": {
                "dimension": {"type": "string", "enum": [dim.key]},
                "to_level": {"type": "string", "enum": [lv.label for lv in dim.levels]},
                "targets": {"anyOf": [{"type": "string", "enum": codes}, {"type": "null"}]},
                "reason": _text_schema(options.comment_chars),
            },
            "required": ["dimension", "to_level", "targets", "reason"],
            "additionalProperties": False,
        }
        for dim in dimensions
    ]
    moves: dict[str, object] = {"type": "array", "maxItems": options.max_moves}
    moves["items"] = {"anyOf": move_variants} if move_variants else {"type": "object"}
    return {
        "type": "object",
        "properties": {
            "evaluation": {
                "type": "object",
                "properties": {
                    "findings": {"type": "array", "items": finding, "maxItems": options.max_findings},
                    "verdict": {"type": "string", "enum": ["accept", "reject"]},
                    "critique": _text_schema(options.critique_chars),
                },
                "required": ["findings", "verdict", "critique"],
                "additionalProperties": False,
            },
            "guidance": {
                "type": "object",
                "properties": {"moves": moves},
                "required": ["moves"],
                "additionalProperties": False,
            },
        },
        "required": ["evaluation", "guidance"],
        "additionalProperties": False,
    }


_THINK = re.compile(r"^.*?</think>", re.S)
_FENCE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.S)


def parse_answer(
    raw: str, codes: set[str], dimensions: Sequence[Dimension], point: Point, box_scale: BoxScale
) -> JudgeOutput:
    """Strict parse of the judge's answer. Tolerated, since the provider is not ours: a leading reasoning block
    closed by </think>, and a fenced code block around the JSON. Everything else must match the contract."""
    text = _THINK.sub("", raw, count=1).strip()
    fenced = _FENCE.match(text)
    if fenced:
        text = fenced.group(1)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise ContractError(f"not JSON: {error}") from None
    evaluation = _obj(data, "evaluation", {"evaluation", "guidance"})
    guidance = _obj(data, "guidance", {"evaluation", "guidance"})
    _keys(evaluation, {"findings", "verdict", "critique"}, "evaluation")
    _keys(guidance, {"moves"}, "guidance")
    raw_findings = evaluation["findings"]
    if not isinstance(raw_findings, list) or len(raw_findings) > MAX_FINDINGS:
        raise ContractError("findings must be a list of at most 12")
    findings = tuple(_finding(item, codes, box_scale) for item in raw_findings)
    verdict = evaluation["verdict"]
    if verdict not in ("accept", "reject"):
        raise ContractError(f"verdict {verdict!r}")
    critique = evaluation["critique"]
    if not isinstance(critique, str):
        raise ContractError("critique must be text")
    raw_moves = guidance["moves"]
    if not isinstance(raw_moves, list) or len(raw_moves) > MAX_MOVES:
        raise ContractError("moves must be a list of at most 4")
    dims = {d.key: d for d in dimensions}
    moves = tuple(_move(item, dims, codes, point) for item in raw_moves)
    return JudgeOutput(findings, verdict, critique[:CRITIQUE_MAX], moves)


def _finding(item: object, codes: set[str], box_scale: BoxScale) -> Finding:
    if not isinstance(item, dict):
        raise ContractError("a finding must be an object")
    _keys(item, {"code", "severity", "box", "comment"}, "finding")
    code, severity, comment = item["code"], item["severity"], item["comment"]
    if code not in codes:
        raise ContractError(f"unknown defect code {code!r}")
    if severity not in ("minor", "blocking"):
        raise ContractError(f"unknown severity {severity!r}")
    if not isinstance(comment, str):
        raise ContractError("comment must be text")
    sev: Severity = "blocking" if severity == "blocking" else "minor"
    return Finding(code, sev, _box(item["box"], box_scale), comment)


def _box(value: object, box_scale: BoxScale) -> Box | None:
    if value is None:
        return None
    if not isinstance(value, list) or len(value) != 4 or not all(
        isinstance(v, (int, float)) and not isinstance(v, bool) for v in value
    ):
        raise ContractError(f"box must be four numbers or null, got {value!r}")
    scale = 1000.0 if box_scale == "per_mille" else 1.0
    x0, y0, x1, y1 = (min(max(float(v) / scale, 0.0), 1.0) for v in value)
    try:
        return Box(x0, y0, x1, y1)
    except ValueError:
        raise ContractError(f"degenerate box {value!r}") from None


def _move(item: object, dims: dict[str, Dimension], codes: set[str], point: Point) -> Move:
    if not isinstance(item, dict):
        raise ContractError("a move must be an object")
    _keys(item, {"dimension", "to_level", "targets", "reason"}, "move")
    dim = dims.get(item["dimension"])
    if dim is None:
        raise ContractError(f"move on unknown dimension {item['dimension']!r}")
    try:
        ordinal = dim.ordinal_of(item["to_level"])
    except KeyError:
        raise ContractError(f"{dim.key} has no level {item['to_level']!r}") from None
    if ordinal == point.get(dim.key):
        raise ContractError(f"move to the current level of {dim.key}")
    targets = item["targets"]
    if targets is not None and targets not in codes:
        raise ContractError(f"move targets unknown defect {targets!r}")
    reason = item["reason"]
    if not isinstance(reason, str):
        raise ContractError("reason must be text")
    return Move(dim.key, ordinal, targets, reason)


def _obj(data: object, name: str, allowed: set[str]) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ContractError("the answer must be a JSON object")
    _keys(data, allowed, "answer")
    value = data[name]
    if not isinstance(value, dict):
        raise ContractError(f"{name} must be an object")
    return value


def _keys(item: dict[str, Any], expected: set[str], what: str) -> None:
    if set(item) != expected:
        raise ContractError(f"{what} keys {sorted(item)}, expected {sorted(expected)}")
