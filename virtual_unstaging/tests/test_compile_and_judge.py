"""Compile (point to request) and the judge's contract (schema, strict parsing at the edge)."""

from __future__ import annotations

import base64
import io
import json

import pytest
from PIL import Image

from virtual_unstaging.clients.fakes import FAKE_CAPABILITIES
from virtual_unstaging.clients.openai_compatible import image_part, text_part
from virtual_unstaging.domain import GeneratorCapabilities, JudgeRequestOptions, ModelRef, Point
from virtual_unstaging.instructions import InstructionStack, load_base, render
from virtual_unstaging.judge import ContractError, Judge, JudgeImage, JudgeInput, output_schema, parse_answer
from virtual_unstaging.loop1.compile import Guide, PhotoContext, compile_request
from virtual_unstaging.registry import load_defects, load_release, prune

DEFECTS = load_defects()
RELEASE = load_release(DEFECTS)
DIMS = prune(RELEASE, FAKE_CAPABILITIES)
START = Point.of({d.key: d.default_ordinal for d in DIMS})
CODES = {d.code for d in DEFECTS}
TEMPLATE = load_base("generator")

CONTEXT = PhotoContext(
    photo_id=1,
    original="a" * 64,
    removal_masks={-1: Guide("b" * 64, None), 0: Guide("c" * 64, 10), 1: Guide("d" * 64, 11), 2: Guide("e" * 64, 12)},
    protected_mask=Guide("f" * 64, None),
    references=("1" * 64, "2" * 64, "3" * 64),
    movable=("sofa", "chair"),
    fixed_visible=(),
    fixed_group=("door", "radiator"),
    seed=42,
)


def test_compile_start_point() -> None:
    compiled = compile_request(START, DIMS, CONTEXT, TEMPLATE, FAKE_CAPABILITIES)
    roles = [im.role for im in compiled.request.images]
    assert roles == ["original", "removal_mask", "reference"]  # mask dilated, one reference, protected mask off
    assert compiled.request.images[1].sha256 == "d" * 64 and compiled.image_tool_runs[1] == 11
    prompt = compiled.request.prompt
    assert "Image 1 is the photo to edit." in prompt
    assert "Image 2 is a mask" in prompt and "Image 3 is another photo of the same room" in prompt
    assert "sofa, chair" in prompt and "Do not add doors" in prompt
    assert "Keep these fixed elements" not in prompt  # `visible` names an empty list: the fragment is dropped
    assert "${" not in prompt


def test_compile_respects_the_image_budget_and_native_mask() -> None:
    point = START.with_level("reference_count", 2).with_level("protected_mask", 1)
    tight = GeneratorCapabilities(frozenset({"original", "reference", "removal_mask", "protected_mask"}), 4, False)
    roles = [im.role for im in compile_request(point, DIMS, CONTEXT, TEMPLATE, tight).request.images]
    assert roles == ["original", "removal_mask", "protected_mask", "reference"]
    native = GeneratorCapabilities(frozenset({"original", "reference", "removal_mask"}), 3, True)
    request = compile_request(point, DIMS, CONTEXT, TEMPLATE, native).request
    assert [im.role for im in request.images] == ["original", "removal_mask", "reference", "reference"]
    assert "The mask given with the request" in request.prompt and "Images 2 to 3 are" in request.prompt


def test_cache_key_depends_on_everything_sent() -> None:
    model = ModelRef("m", "1")
    a = compile_request(START, DIMS, CONTEXT, TEMPLATE, FAKE_CAPABILITIES).request
    b = compile_request(START.with_level("wall_rule", 2), DIMS, CONTEXT, TEMPLATE, FAKE_CAPABILITIES).request
    assert a.cache_key(model) == compile_request(START, DIMS, CONTEXT, TEMPLATE, FAKE_CAPABILITIES).request.cache_key(model)
    assert a.cache_key(model) != b.cache_key(model) != a.cache_key(ModelRef("m", "2"))


def test_render_refuses_unknown_placeholders() -> None:
    with pytest.raises(KeyError):
        render("Hello ${nobody}", {}, {})


def answer(findings: list[object] | None = None, moves: list[object] | None = None, **evaluation: object) -> str:
    body = {"findings": findings or [], "verdict": "reject", "critique": "c", **evaluation}
    return json.dumps({"evaluation": body, "guidance": {"moves": moves or []}})


def test_parse_a_good_answer_per_mille() -> None:
    raw = "<think>hmm</think>```json\n" + answer(
        [{"code": "opening_invented", "severity": "blocking", "box": [100, 200, 500, 900], "comment": "door"}],
        [{"dimension": "wall_rule", "to_level": "emphasized", "targets": "opening_invented", "reason": "r"}],
    ) + "\n```"
    out = parse_answer(raw, CODES, DIMS, START, "per_mille")
    assert out.findings[0].box is not None and out.findings[0].box.x1 == 0.5
    assert out.moves[0].dimension == "wall_rule" and out.moves[0].to_ordinal == 2


@pytest.mark.parametrize(
    "raw",
    [
        "the image looks fine",
        answer([{"code": "ghost", "severity": "blocking", "box": None, "comment": ""}]),
        answer([{"code": "drift", "severity": "fatal", "box": None, "comment": ""}]),
        answer([{"code": "drift", "severity": "minor", "box": [5, 5, 5, 5], "comment": ""}]),
        answer([{"code": "drift", "severity": "minor", "box": None, "comment": "", "extra": 1}]),
        answer(moves=[{"dimension": "wall_rule", "to_level": "present", "targets": None, "reason": ""}]),
        answer(moves=[{"dimension": "colour", "to_level": "red", "targets": None, "reason": ""}]),
        answer(verdict="maybe"),
    ],
)
def test_parse_refuses_what_breaks_the_contract(raw: str) -> None:
    with pytest.raises(ContractError):
        parse_answer(raw, CODES, DIMS, START, "per_mille")


def test_schema_and_request_come_from_the_run() -> None:
    schema = output_schema(DEFECTS, DIMS)
    finding = schema["properties"]["evaluation"]["properties"]["findings"]["items"]  # type: ignore[index]
    assert set(finding["properties"]["code"]["enum"]) == CODES
    judge = Judge(ModelRef("j", "1"), InstructionStack("judge", "j", load_base("judge")), DEFECTS, "per_mille",
                  image_part, text_part)
    request = judge.build(JudgeInput((JudgeImage("the original photo", b"x"),), (("change_map", "small"),),
                                     ("door",), ("sofa",), (), DIMS, START))
    system = request.messages[0]["content"]
    assert isinstance(system, str) and "`opening_invented`" in system and "0 to 1000" in system
    again = judge.build(JudgeInput((JudgeImage("the original photo", b"x"),), (("change_map", "small"),),
                                   ("door",), ("sofa",), (), DIMS, START))
    assert request.request_sha256 == again.request_sha256


def png_photo(size: tuple[int, int]) -> bytes:
    buffer = io.BytesIO()
    Image.new("RGB", size, (120, 90, 60)).save(buffer, format="PNG")
    return buffer.getvalue()


def judge_with(options: JudgeRequestOptions | None) -> Judge:
    return Judge(ModelRef("j", "1"), InstructionStack("judge", "j", load_base("judge")), DEFECTS, "per_mille",
                 image_part, text_part, options)


def photo_input(data: bytes) -> JudgeInput:
    return JudgeInput((JudgeImage("the original photo", data),), (), ("door",), ("sofa",), (), DIMS, START)


def test_the_full_judge_request_is_what_it_was_before_speed_versions() -> None:
    photo = png_photo((1200, 1600))
    full = judge_with(None).build(photo_input(photo))
    assert full.request_sha256 == judge_with(JudgeRequestOptions()).build(photo_input(photo)).request_sha256
    parts = full.messages[1]["content"]
    assert isinstance(parts, list)
    sent = [part for part in parts if part["type"] == "image_url"][0]["image_url"]["url"]
    assert sent == "data:image/png;base64," + base64.b64encode(photo).decode("ascii")  # the stored bytes, untouched
    assert "Keep the answer short" not in parts[-1]["text"] and "maxLength" not in json.dumps(full.schema)
    assert JudgeRequestOptions().revision_suffix() == ""


def test_a_judge_speed_version_sends_smaller_images_and_asks_for_a_shorter_answer() -> None:
    photo = png_photo((1200, 1600))
    fast = JudgeRequestOptions(image_side=768, image_format="jpeg", max_findings=4, max_moves=1, comment_chars=60,
                               critique_chars=120)
    request = judge_with(fast).build(photo_input(photo))
    assert request.request_sha256 != judge_with(None).build(photo_input(photo)).request_sha256
    parts = request.messages[1]["content"]
    assert isinstance(parts, list)
    url = [part for part in parts if part["type"] == "image_url"][0]["image_url"]["url"]
    assert url.startswith("data:image/jpeg;base64,")
    with Image.open(io.BytesIO(base64.b64decode(url.split(",", 1)[1]))) as sent:
        assert sent.format == "JPEG" and sent.size == (576, 768)
    evaluation = request.schema["properties"]["evaluation"]["properties"]  # type: ignore[index]
    assert evaluation["findings"]["maxItems"] == 4 and evaluation["critique"]["maxLength"] == 120
    assert evaluation["findings"]["items"]["properties"]["comment"]["maxLength"] == 60
    moves = request.schema["properties"]["guidance"]["properties"]["moves"]  # type: ignore[index]
    assert moves["maxItems"] == 1
    assert all(variant["properties"]["reason"]["maxLength"] == 60 for variant in moves["items"]["anyOf"])
    assert "at most 4 findings and 1 moves" in parts[-1]["text"] and "under 60 characters" in parts[-1]["text"]
    assert fast.revision_suffix() == "+jpeg@768+answer:4/1/60/120"
    assert JudgeRequestOptions(image_format="jpeg").revision_suffix() == "+jpeg@full"
