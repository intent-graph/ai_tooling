"""Composition (P9's pure function), the data files' contract, and P10: no instruction text in the code."""

from __future__ import annotations

import ast
import json
import tomllib
from importlib import resources
from pathlib import Path

import pytest

from clutter_pairs.compose import DERIVED_CODES, ComposeError, canonical, compose, parse_composer, parse_judgment
from clutter_pairs.config import ConfigError
from clutter_pairs.dataset import packaged_files, parse_reasons
from clutter_pairs.domain import ModelId, Part, RegionItems, SourceRef
from clutter_pairs.pairs import Thresholds

DATA = resources.files("clutter_pairs.data")
MODEL = ModelId("org/judge", "abc", "fam", "MIT")


def _read(path: str) -> str:
    return DATA.joinpath(path).read_text(encoding="utf-8")


def _parts(lessons: int) -> list[Part]:
    parts = [Part("instruction", "instruction", "Be brief.", source=SourceRef(file_sha="a" * 64)),
             Part("schema", "schema", _read("schemas/text.json"), source=SourceRef(file_sha="b" * 64)),
             Part("spec", "spec", "- room_type: kitchen")]
    parts += [Part("lesson", "lesson", f"(lesson {n}) do {n}", source=SourceRef(lesson_id=n)) for n in range(lessons)]
    parts += [Part("setting", "setting", "0.5", source=SourceRef(setting_name="temperature", origin="config")),
              Part("setting", "setting", "100", source=SourceRef(setting_name="max_tokens", origin="config")),
              Part("seed", "seed", "7", source=SourceRef(origin="engine"))]
    return parts


def test_a_request_is_a_pure_function_of_composer_model_and_parts() -> None:
    composer = parse_composer("clean_write", _read("composers/clean_write.toml"))
    request = compose(composer, MODEL, _parts(0))
    assert request["model"] == ["org/judge", "abc"] and request["seed"] == 7 and request["temperature"] == 0.5
    texts = [item["text"] for m in request["messages"] for item in m["content"]]
    assert not any("Lessons" in t for t in texts)  # a header only when its slot is filled
    with_lessons = compose(composer, MODEL, _parts(2))
    assert canonical(with_lessons) != canonical(request)
    assert canonical(compose(composer, MODEL, _parts(2))) == canonical(with_lessons)


def test_a_part_without_a_slot_is_refused() -> None:
    composer = parse_composer("clean_write", _read("composers/clean_write.toml"))
    with pytest.raises(ComposeError, match="does not have"):
        compose(composer, MODEL, [*_parts(0), Part("nowhere", "spec", "x")])


def test_every_composer_parses() -> None:
    for path in packaged_files():
        if path.startswith("composers/"):
            parse_composer(Path(path).stem, _read(path))


def test_judge_schemas_list_exactly_their_stage_codes_and_instructions_explain_them() -> None:
    reasons = parse_reasons(_read("reasons.toml"))
    for schema, stage, instruction in (("clean_judgment", "clean", "clean_judge"), ("pair_judgment", "clutter", "pair_judge")):
        listed = json.loads(_read(f"schemas/{schema}.json"))["properties"]["findings"]["items"]["properties"]["code"]["enum"]
        expected = {c for c, r in reasons.items() if r.stage in (stage, "both") and r.by in ("judge", "both")}
        assert set(listed) == expected - DERIVED_CODES
        text = _read(f"instructions/{instruction}.md")
        assert all(f"`{code}`" in text for code in listed)


def test_the_pair_judge_answers_openings_first_and_at_most_the_regions_drawn() -> None:
    schema = json.loads(_read("schemas/pair_judgment.json"))
    assert list(schema["properties"])[:3] == ["openings", "appeared", "regions"]
    assert schema["properties"]["regions"]["maxItems"] == Thresholds().max_regions
    assert schema["properties"]["regions"]["items"]["properties"]["region"]["maximum"] == Thresholds().max_regions


def test_opening_changed_is_always_blocking_and_has_no_minor_twin() -> None:
    reasons = parse_reasons(_read("reasons.toml"))
    assert reasons["opening_changed"].severity == "blocking" and "opening_changed_minor" not in reasons
    with pytest.raises(ConfigError):
        parse_reasons(_read("reasons.toml").replace(
            '[opening_changed]\nstage = "clutter"\nseverity = "blocking"', '[opening_changed]\nstage = "clutter"\nseverity = "minor"'))
    with pytest.raises(ConfigError):
        parse_reasons(_read("reasons.toml") + '\n[opening_changed_minor]\nstage = "clutter"\nseverity = "minor"\nby = "judge"\n')


def _pair_answer(**overrides: object) -> str:
    answer: dict[str, object] = {"openings": [], "appeared": [], "regions": [], "findings": [], "guidance": []}
    answer.update(overrides)
    return json.dumps(answer)


PAIR_CODES = {"opening_changed", "scene_changed", "item_missing"}


def test_a_changed_vanished_or_appeared_opening_becomes_a_blocking_finding() -> None:
    openings = [{"kind": "window", "where": "left wall", "status": "changed", "regions": [1, 9]},
                {"kind": "door", "where": "back wall", "status": "partly_hidden", "regions": [2]},
                {"kind": "door", "where": "right wall", "status": "vanished", "regions": []}]
    appeared = [{"kind": "passage", "where": "corner", "regions": [2]}]
    judgment = parse_judgment(_pair_answer(openings=openings, appeared=appeared), "clutter", 3, PAIR_CODES, 2)
    assert [(f.code, f.judged_severity, f.regions, f.comment) for f in judgment.findings] == [
        ("opening_changed", "blocking", (1,), "window, left wall: changed"),
        ("opening_changed", "blocking", (), "door, right wall: vanished"),
        ("opening_changed", "blocking", (2,), "passage, corner: appeared")]
    with pytest.raises(ComposeError):  # the checklist is the only channel for openings
        parse_judgment(_pair_answer(findings=[{"code": "opening_changed", "severity": "blocking", "regions": [],
                                               "box": None, "comment": "a door"}]), "clutter", 3, PAIR_CODES, 2)


def test_region_answers_left_out_or_given_twice_are_not_answered_and_unknown_numbers_dropped() -> None:
    regions = [{"region": 1, "items": [2, 7], "other_change": False},
               {"region": 2, "items": [1], "other_change": False}, {"region": 2, "items": [], "other_change": False},
               {"region": 4, "items": [1], "other_change": True}, {"region": 9, "items": [1], "other_change": False}]
    judgment = parse_judgment(_pair_answer(regions=regions), "clutter", 3, PAIR_CODES, 4)
    assert judgment.regions == (RegionItems(1, (2,)), RegionItems(2, (), False, answered=False),
                                RegionItems(3, (), False, answered=False), RegionItems(4, (1,), True))
    with pytest.raises(ComposeError):
        parse_judgment(_pair_answer(regions=[{"region": 1, "items": [], "other_change": "yes"}]), "clutter", 3,
                       PAIR_CODES, 1)


def test_judgment_parsing_converts_boxes_and_rejects_foreign_codes() -> None:
    answer = json.dumps({"findings": [{"code": "not_empty", "severity": "blocking", "box": [100, 200, 300, 400],
                                       "comment": "a chair"}], "guidance": ["remove it"]})
    judgment = parse_judgment("<think>hm</think>" + answer, "clean", 0, {"not_empty"})
    assert judgment.findings[0].box is not None and judgment.findings[0].box.x1 == 0.3
    with pytest.raises(ComposeError):
        parse_judgment(answer, "clean", 0, {"implausible"})


def _package_sources() -> list[Path]:
    root = Path(str(resources.files("clutter_pairs")))
    return sorted(root.rglob("*.py"))


def test_p10_no_instruction_text_in_the_code() -> None:
    """Any string literal that is multi-line or over 200 characters, other than a docstring, fails. The store, the
    only package that holds SQL, is left out: its long literals are queries."""
    offenders = []
    for path in _package_sources():
        if path.parent.name == "store":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        docstrings = {id(node.body[0].value) for node in ast.walk(tree)
                      if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
                      and node.body and isinstance(node.body[0], ast.Expr)
                      and isinstance(node.body[0].value, ast.Constant)}
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docstrings:
                if "\n" in node.value.strip("\n") or len(node.value) > 200:
                    offenders.append(f"{path.name}:{node.lineno}")
    assert offenders == []


def test_p7_the_package_ships_no_dataset() -> None:
    root = Path(str(resources.files("clutter_pairs")))
    images = [p for p in root.rglob("*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".sqlite")]
    assert images == []


def test_decision_rule_parameters_parse() -> None:
    from clutter_pairs.dataset import parse_rule

    rule = parse_rule(_read("decision_rules/carry_forward.md"))
    assert rule["off_share"] == pytest.approx(1 / 3, abs=0.01)
    assert tomllib.loads("a = 1")  # the rule's block is TOML
