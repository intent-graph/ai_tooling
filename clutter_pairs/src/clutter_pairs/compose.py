"""Composition: a request is a pure function of its composer file, the call's model and its ordered parts (P9).

A composer (TOML, one per stage and role) places each part in a slot: message content for a chat request; prompt,
images, settings and seed for a generator request. The renderers turn records (a subject's spec, an assessment, a
lesson) into the text of a part; each has a name and a version, and the composer names the spec renderer it uses.
"""

from __future__ import annotations

import json
import tomllib
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, Literal

from virtual_unstaging.domain import canonical_json, sha256_text

from clutter_pairs.domain import (
    Box,
    Finding,
    Judgment,
    Lesson,
    Measure,
    ModelId,
    Part,
    RegionItems,
    Role,
    SubjectSpec,
)

SPEC_RENDERERS = {("spec_text", 1)}
SETTINGS_SLOT = "setting"  # setting parts in this slot are request settings; in any other slot, text the model reads
RequestKind = Literal["chat", "generator"]


class ComposeError(ValueError):
    """A composer file that does not parse, or parts that do not fit it."""


@dataclass(frozen=True)
class Slot:
    slot: str
    header: str | None = None  # text placed before the slot's parts, only when at least one part fills it
    image_role: str | None = None  # generator requests: the role the slot's image takes


@dataclass(frozen=True)
class Composer:
    name: str
    role: Role
    request: RequestKind
    renderer: str
    renderer_version: int
    messages: tuple[tuple[str, tuple[Slot, ...]], ...] = ()  # chat: (message role, content slots)
    schema_slot: str | None = None
    prompt_slot: str | None = None  # generator: the call_output part holding the prompt
    images: tuple[Slot, ...] = ()  # generator
    settings: tuple[str, ...] = ()  # names of the setting parts the request takes
    seed_slot: str = "seed"


def parse_composer(name: str, text: str) -> Composer:
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as error:
        raise ComposeError(f"composer {name}: {error}") from None
    known = {"role", "request", "renderer", "renderer_version", "messages", "schema", "prompt", "images", "settings",
             "seed"}
    if set(data) - known:
        raise ComposeError(f"composer {name}: unknown keys {sorted(set(data) - known)}")
    request, role = data.get("request"), data.get("role")
    if request not in ("chat", "generator") or role not in ("write", "generate", "edit", "judge", "revise", "distill"):
        raise ComposeError(f"composer {name}: request must be chat or generator, role a known role")
    renderer = (str(data.get("renderer", "")), data.get("renderer_version"))
    if renderer not in SPEC_RENDERERS:
        raise ComposeError(f"composer {name}: unknown spec renderer {renderer}")
    composer = Composer(
        name=name, role=role, request=request, renderer=renderer[0], renderer_version=int(renderer[1]),
        messages=tuple((str(m["role"]), tuple(_slot(s) for s in m["content"])) for m in data.get("messages", [])),
        schema_slot=data.get("schema"), prompt_slot=data.get("prompt"),
        images=tuple(_slot(s) for s in data.get("images", [])),
        settings=tuple(str(s) for s in data.get("settings", [])), seed_slot=str(data.get("seed", "seed")),
    )
    if request == "chat" and (not composer.messages or composer.schema_slot is None):
        raise ComposeError(f"composer {name}: a chat request needs messages and a schema slot")
    if request == "generator" and composer.prompt_slot is None:
        raise ComposeError(f"composer {name}: a generator request needs a prompt slot")
    return composer


def _slot(raw: Any) -> Slot:
    if not isinstance(raw, dict) or not isinstance(raw.get("slot"), str) or set(raw) - {"slot", "header", "role"}:
        raise ComposeError(f"a slot is a table with slot, and optionally header or role: {raw!r}")
    return Slot(raw["slot"], raw.get("header"), raw.get("role"))


def compose(composer: Composer, model: ModelId, parts: Sequence[Part]) -> dict[str, Any]:
    """The canonical request (images by hash). Every part must find its place; nothing else enters the request."""
    used: set[int] = set()

    def take(slot: str) -> list[tuple[int, Part]]:
        found = [(i, p) for i, p in enumerate(parts) if p.slot == slot and i not in used]
        used.update(i for i, _ in found)
        return found

    def single(slot: str) -> Part:
        found = take(slot)
        if len(found) != 1:
            raise ComposeError(f"composer {composer.name}: slot {slot} needs exactly one part, got {len(found)}")
        return found[0][1]

    settings: dict[str, Any] = {}
    for i, part in enumerate(parts):
        if part.kind == "setting" and part.slot == SETTINGS_SLOT:
            name = part.source.setting_name
            if name not in composer.settings or name in settings or part.text is None:
                raise ComposeError(f"composer {composer.name}: setting {name} is not taken, or given twice")
            settings[name] = json.loads(part.text)
            used.add(i)
    seed_part = single(composer.seed_slot)
    if seed_part.kind != "seed" or seed_part.text is None:
        raise ComposeError(f"composer {composer.name}: the seed slot holds a seed part")
    request: dict[str, Any] = {"kind": composer.request, "model": [model.name, model.revision],
                               "seed": int(seed_part.text)}
    if composer.request == "chat":
        messages = []
        for message_role, slots in composer.messages:
            content: list[dict[str, Any]] = []
            for slot in slots:
                found = take(slot.slot)
                if found and slot.header:
                    content.append({"type": "text", "text": slot.header})
                content.extend(_content(p) for _, p in found)
            if content:
                messages.append({"role": message_role, "content": content})
        assert composer.schema_slot is not None
        schema_part = single(composer.schema_slot)
        if schema_part.kind != "schema" or schema_part.text is None:
            raise ComposeError(f"composer {composer.name}: the schema slot holds a schema part")
        request.update(messages=messages, schema=json.loads(schema_part.text), **settings)
    else:
        assert composer.prompt_slot is not None
        prompt = single(composer.prompt_slot)
        images = []
        for slot in composer.images:
            for _, part in take(slot.slot):
                if part.kind != "image" or part.image_sha is None:
                    raise ComposeError(f"composer {composer.name}: slot {slot.slot} takes images")
                images.append({"role": slot.image_role or "original", "sha256": part.image_sha})
        request.update(prompt=prompt.text, images=images, settings=settings)
    unused = [parts[i].slot for i in range(len(parts)) if i not in used]
    if unused:
        raise ComposeError(f"composer {composer.name}: parts in slots it does not have: {unused}")
    return request


def _content(part: Part) -> dict[str, Any]:
    if part.kind == "image":
        return {"type": "image", "sha256": part.image_sha}
    return {"type": "text", "text": part.text}


def canonical(request: dict[str, Any]) -> tuple[str, str]:
    """The canonical text of a request and its hash: the cache key."""
    text = canonical_json(request)
    return text, sha256_text(text)


# --- Renderers ------------------------------------------------------------------------------------------------


def render_spec(spec: SubjectSpec, renderer: str, version: int) -> str:
    if (renderer, version) != ("spec_text", 1):
        raise ComposeError(f"unknown spec renderer {renderer}@{version}")
    lines = [f"- {v.axis}: {v.value} ({v.text})" for v in spec.values]
    if spec.items:
        lines.append("Items:")
        for item in spec.items:
            described = "; ".join(f"{v.axis}: {v.value} ({v.text})" for v in item.values)
            lines.append(f"{item.ordinal}. {described}")
    lines.append("Rules:")
    lines.extend(f"- {rule}" for rule in spec.rules)
    return "\n".join(lines)


def render_assessment(iteration: int, kind: str, judgment: Judgment, measures: Sequence[Measure]) -> str:
    """An assessment as a reviser or the distiller reads it; boxes in thousandths, like the judges write them."""
    lines = [f"Assessment of iteration {iteration} ({kind}):"]
    for m in measures:
        bound = "" if m.threshold is None else f" (threshold {m.threshold:g})"
        lines.append(f"- measure {m.name} = {m.value:.4g}{bound}")
    for f in judgment.findings:
        where = "" if f.box is None else f" at {_thousandths(f.box)}"
        cited = "" if not f.regions else " in region" + ("s " if len(f.regions) > 1 else " ") + _numbers(f.regions)
        lines.append(f"- finding {f.code}{where}{cited}: {f.comment}")
    for r in judgment.regions:
        held = f"items {_numbers(r.items)}" if r.items else "no item"
        lines.append(f"- region {r.region} holds {held}")
    for rank, text in enumerate(judgment.guidance, start=1):
        lines.append(f"- guidance {rank}: {text}")
    if len(lines) == 1:
        lines.append("- no finding")
    return "\n".join(lines)


def render_lesson(lesson: Lesson) -> str:
    return f"(lesson {lesson.id}) {lesson.text}"


def _thousandths(box: Box) -> str:
    return "[" + ", ".join(str(round(v * 1000)) for v in (box.x0, box.y0, box.x1, box.y1)) + "]"


def answer_text(answer: str) -> str:
    """The text of a free-text answer (schema `text.json`)."""
    try:
        value = json.loads(_strip_reasoning(answer))["text"]
    except (ValueError, KeyError, TypeError):
        raise ComposeError("the answer is not a {\"text\": ...} object") from None
    if not isinstance(value, str) or not value.strip():
        raise ComposeError("the answer's text is empty")
    return value.strip()


def _strip_reasoning(answer: str) -> str:
    """A reasoning model may prefix its JSON with a <think> block; the JSON is what follows it."""
    end = answer.rfind("</think>")
    return answer[end + len("</think>"):] if end >= 0 else answer


def parse_json_answer(answer: str) -> Any:
    try:
        return json.loads(_strip_reasoning(answer))
    except ValueError:
        raise ComposeError("the answer is not JSON") from None


def parse_judgment(answer: str, stage: str, item_count: int, allowed_codes: set[str], region_count: int = 0) -> Judgment:
    """A judge's answer, at the trust boundary: codes from the stage's reasons, boxes in thousandths turned into
    [0, 1]. A degenerate finding box becomes no box; an unknown item or region number is left out, as is a region's
    second answer. Every region 1..region_count is in the result; one without an answer holds no item. Anything else
    malformed rejects the answer."""
    data = parse_json_answer(answer)
    try:
        findings = []
        for raw in data["findings"]:
            code = str(raw["code"])
            if code not in allowed_codes:
                raise ComposeError(f"finding code {code!r} is not a {stage} code")
            severity = raw.get("severity")
            if severity not in ("blocking", "minor"):
                raise ComposeError(f"severity {severity!r}")
            cited = _ordinals(raw.get("regions", []), region_count)
            findings.append(Finding(code, severity, _box(raw.get("box")), str(raw.get("comment", ""))[:1000], cited))
        guidance = tuple(str(g)[:1000] for g in data["guidance"])
        regions: dict[int, RegionItems] = {}
        if stage == "clutter":
            for raw in data["regions"]:
                n = int(raw["region"])
                if 1 <= n <= region_count and n not in regions:
                    regions[n] = RegionItems(n, _ordinals(raw["items"], item_count))
    except (KeyError, TypeError, ValueError) as error:
        if isinstance(error, ComposeError):
            raise
        raise ComposeError(f"malformed judgment: {error!r}") from None
    every = tuple(regions.get(n, RegionItems(n, ())) for n in range(1, region_count + 1)) if stage == "clutter" else ()
    return Judgment(tuple(findings), guidance, every)


def _ordinals(raw: object, count: int) -> tuple[int, ...]:
    """Distinct numbers in 1..count, sorted; others dropped."""
    if not isinstance(raw, list):
        raise ComposeError(f"a list of numbers: {raw!r}")
    return tuple(sorted({int(v) for v in raw if isinstance(v, int) and 1 <= v <= count}))


def _numbers(values: Sequence[int]) -> str:
    return ", ".join(str(v) for v in values)


def _box(raw: object) -> Box | None:
    if raw is None:
        return None
    if not isinstance(raw, list) or len(raw) != 4 or not all(isinstance(v, (int, float)) for v in raw):
        raise ComposeError(f"a box is four numbers: {raw!r}")
    x0, y0, x1, y1 = (min(max(float(v) / 1000, 0.0), 1.0) for v in raw)
    if not (x0 < x1 and y0 < y1):
        return None
    return Box(x0, y0, x1, y1)
