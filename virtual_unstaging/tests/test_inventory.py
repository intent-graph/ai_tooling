"""The judge's evidence: the element inventory (core, tool, names, in the runner), the change map's colour shift, the
semantic diff's continued classes, and the schema's moves."""

from __future__ import annotations

import io
from pathlib import Path
from typing import Any

import numpy as np
import pytest
from fastapi.testclient import TestClient
from PIL import Image
from test_loop1 import api_run
from test_serve import AUTH, make_app, mask_png, png, put, run_tool

from virtual_unstaging import imaging as local_imaging
from virtual_unstaging.clients.fakes import FAKE_CAPABILITIES, FakeChat
from virtual_unstaging.domain import JudgeRequestOptions, Point, sha256_bytes
from virtual_unstaging.judge import _tool_line, output_schema
from virtual_unstaging.loop1.evidence import MAX_NAMES, building_elements, clean, inventory_names
from virtual_unstaging.registry import load_defects, load_release, prune
from virtual_unstaging.serve.tools.classdiff import compare_classes
from virtual_unstaging.serve.tools.inventory import (
    Seen,
    annotate,
    match,
    seen_elements,
    summarize,
    take_inventory,
)
from virtual_unstaging.serve.tools.segment import Instance
from virtual_unstaging.store.db import connect
from virtual_unstaging.tools.local import LocalTools

SIZE = (40, 40)  # width, height of the synthetic masks


def block(rows: slice, columns: slice) -> np.ndarray:
    mask = np.zeros((SIZE[1], SIZE[0]), dtype=bool)
    mask[rows, columns] = True
    return mask


def seen(label: str, kind: str, mask: np.ndarray, score: float = 0.9) -> Seen:
    return Seen(label, kind, score, mask, [0.0, 0.0, 1.0, 1.0])


REGION = block(slice(10, 30), slice(10, 30))


def statuses(elements: list[Any]) -> dict[str, tuple[str, str]]:
    return {e.label: (e.status, e.where) for e in elements}


# --- the pure core ---------------------------------------------------------------------------------------------


def test_each_element_gets_its_status() -> None:
    before = [
        seen("sofa", "movable", block(slice(12, 20), slice(12, 28))),  # removed as asked
        seen("chair", "movable", block(slice(22, 28), slice(12, 18))),  # still there: left
        seen("radiator", "fixed", block(slice(0, 6), slice(0, 10))),  # unchanged, outside: kept
        seen("door", "fixed", block(slice(10, 30), slice(30, 34))),  # partly hidden: revealed
        seen("window", "fixed", block(slice(0, 8), slice(30, 40))),  # gone, outside: removed
        seen("lamp", "fixed", block(slice(32, 40), slice(0, 8))),  # moved: changed
    ]
    after = [
        seen("chair", "movable", block(slice(22, 28), slice(12, 18))),
        seen("radiator", "fixed", block(slice(0, 6), slice(0, 10))),
        seen("door", "fixed", block(slice(10, 30), slice(22, 34))),
        seen("lamp", "fixed", block(slice(32, 40), slice(4, 12))),
        seen("fireplace", "fixed", block(slice(12, 20), slice(14, 26))),  # where the sofa stood: new
    ]
    elements = take_inventory(before, after, REGION)
    assert statuses(elements) == {
        "fireplace": ("new", "inside"),
        "window": ("removed", "outside"),
        "lamp": ("changed", "outside"),
        "chair": ("left", "inside"),
        "door": ("revealed", "inside"),
        "sofa": ("removed", "inside"),
        "radiator": ("kept", "outside"),
    }
    new = next(e for e in elements if e.label == "fireplace")
    assert new.stood == ("sofa",) and new.box_original is None
    door = next(e for e in elements if e.label == "door")
    assert door.growth == 3.0
    assert [e.label for e in elements][:2] == ["fireplace", "window"]  # what bears on a defect comes first


def test_matching_prefers_the_same_name_and_stays_within_a_kind() -> None:
    door = block(slice(0, 20), slice(0, 10))
    before = [seen("door", "fixed", door), seen("wardrobe", "movable", door)]
    after = [seen("arched door", "fixed", door), seen("door", "fixed", block(slice(0, 20), slice(2, 12)))]
    pairs = match(before, after)
    assert (0, 1) in {(i, j) for i, j, _ in pairs}  # door to door although "arched door" overlaps more
    assert all(before[i].kind == after[j].kind for i, j, _ in pairs)  # the wardrobe never matches a door


def test_duplicate_detections_of_one_element_are_merged() -> None:
    mask = np.zeros((80, 80), dtype=bool)
    mask[10:50, 10:30] = True
    nearly = mask.copy()
    nearly[50:52, 10:30] = True
    instances = [Instance(0, (10, 10, 30, 50), 0.5, mask), Instance(1, (10, 10, 30, 52), 0.8, nearly),
                 Instance(2, (10, 10, 30, 50), 0.6, mask)]
    elements = seen_elements(instances, ["door", "the arched doors", "wardrobe"], {"door": "fixed", "the arched doors": "fixed",
                                                                                 "wardrobe": "movable"}, SIZE)
    assert [(e.label, e.kind) for e in elements] == [("the arched doors", "fixed"), ("wardrobe", "movable")]
    assert elements[0].mask.shape == (SIZE[1], SIZE[0])


def test_a_detection_nested_in_one_of_its_kind_is_part_of_it_unless_much_smaller() -> None:
    fireplace = block(slice(10, 30), slice(10, 30))
    opening = block(slice(18, 30), slice(14, 26))  # 144 of 400 pixels, inside the fireplace
    socket = block(slice(12, 14), slice(12, 14))  # 4 pixels: too small to be part of it
    kinds = {"fireplace": "fixed", "socket": "fixed"}
    instances = [Instance(0, (10, 10, 30, 30), 0.9, fireplace), Instance(0, (14, 18, 26, 30), 0.7, opening),
                 Instance(1, (12, 12, 14, 14), 0.6, socket)]
    elements = seen_elements(instances, ["fireplace", "socket"], kinds, SIZE)
    assert [e.label for e in elements] == ["fireplace", "socket"]


def test_the_summary_lists_what_bears_on_a_defect_and_rolls_up_the_rest() -> None:
    before = [seen("sofa", "movable", block(slice(12, 20), slice(12, 28))),
              seen("chair", "movable", block(slice(22, 28), slice(20, 26))),
              seen("radiator", "fixed", block(slice(0, 6), slice(0, 10)))]
    after = [seen("radiator", "fixed", block(slice(0, 6), slice(0, 10))),
             seen("door", "fixed", block(slice(12, 20), slice(14, 26)))]
    text = summarize(take_inventory(before, after, REGION))
    lines = text.splitlines()
    assert lines[1] == "1. door (fixed): new, inside, where the original showed sofa"
    assert "Removed as asked (movable): chair, sofa" in lines
    assert "Kept unchanged: radiator" in lines
    assert lines[-1] == "Counts: new 1, removed 2, kept 1"
    assert summarize([]).splitlines()[1] == "no element of the rules was detected in either picture"


def test_the_annotated_candidate_boxes_what_bears_on_a_defect() -> None:
    candidate = Image.new("RGB", (100, 100), (128, 128, 128))
    elements = take_inventory([], [Seen("door", "fixed", 0.9, block(slice(10, 30), slice(10, 30)), [0.25, 0.25, 0.75, 0.75])], REGION)
    picture = np.asarray(annotate(candidate, elements))
    assert tuple(picture[50, 25]) == (255, 40, 40)  # the left edge of the new door's box, in red
    assert tuple(picture[50, 50]) == (128, 128, 128)


# --- the tool on the server (stand-in detector: a colour word in a name finds that colour) ------------------------


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    return TestClient(make_app(tmp_path), headers=AUTH)


def test_element_inventory_on_the_tool_server(client: TestClient) -> None:
    original = np.full((64, 64, 3), 120, dtype=np.uint8)
    original[24:40, 24:40] = (230, 20, 20)  # a red chair inside the region
    original[0:10, 50:64] = (20, 20, 230)  # a blue window outside it
    candidate = np.full((64, 64, 3), 120, dtype=np.uint8)
    candidate[0:10, 50:64] = (20, 20, 230)
    candidate[26:38, 26:38] = (20, 230, 20)  # a green door where the chair stood
    shas = [put(client, png(original)), put(client, png(candidate)), put(client, mask_png(64, 64, slice(16, 48), slice(16, 48)))]
    params = {"fixed": ["blue window", "green door"], "movable": ["red chair"]}
    response = run_tool(client, "element_inventory", shas, params)
    assert response.status_code == 200, response.text
    reply = response.json()
    by_label = {e["label"]: e for e in reply["measures"]["elements"]}
    assert (by_label["green door"]["status"], by_label["green door"]["where"]) == ("new", "inside")
    assert by_label["green door"]["stood"] == ["red chair"]
    assert by_label["red chair"]["status"] == "removed" and by_label["blue window"]["status"] == "kept"
    assert reply["measures"]["counts"]["new"] == 1 and reply["measures"]["compared_at"] == [64, 64]
    assert "1. green door (fixed): new, inside, where the original showed red chair" in reply["summary"]
    assert set(reply["outputs"]) == {"annotated"}
    again = run_tool(client, "element_inventory", shas, params).json()
    assert again["measures"] == reply["measures"]


def test_element_inventory_parses_its_params(client: TestClient) -> None:
    image = put(client, png(np.full((16, 16, 3), 120, dtype=np.uint8)))
    region = put(client, mask_png(16, 16, slice(4, 12), slice(4, 12)))
    for params in ({"fixed": [], "movable": []}, {"fixed": ["door"], "movable": ["Door"]}, {"fixed": "door"},
                   {"fixed": ["door;"]}, {"fixed": ["door"], "labels": ["x"]}, {"fixed": [f"n{i}" for i in range(97)]}):
        assert run_tool(client, "element_inventory", [image, image, region], params).status_code == 400, params


# --- the names the inventory looks for --------------------------------------------------------------------------


def test_names_are_cleaned_deduplicated_and_fixed_first() -> None:
    assert clean("The arched wooden doors") == "arched wooden doors"
    assert clean("the mosaic-tiled shower wall, left") == "mosaic-tiled shower wall left"
    fixed, movable = inventory_names(["walls", "the stone wall", "the doors", "Door", "the ceiling beams"],
                                     ["sofa", "door", "the sofa", "radiator"])
    assert fixed[:3] == ["doors", "door", "ceiling beams"] and set(building_elements()) <= set(fixed)
    assert movable == ["sofa"]  # door and radiator are fixed, the second sofa a duplicate
    many_fixed, many_movable = inventory_names([f"fixed {i}" for i in range(80)], [f"movable {i}" for i in range(20)])
    assert len(many_fixed) == 80 + len(building_elements()) and len(many_fixed) + len(many_movable) == MAX_NAMES


# --- the runner sends the inventory to the judge ---------------------------------------------------------------


def test_the_judge_reads_the_inventory_when_the_project_turns_it_on(project: Path) -> None:
    text = (project / "project.toml").read_text(encoding="utf-8").replace("inventory = false", "inventory = true")
    (project / "project.toml").write_text(text, encoding="utf-8")
    sent: list[Any] = []
    fake = FakeChat()

    def chat(messages: list[dict[str, object]], schema: dict[str, object]) -> str:
        sent.append(messages)
        return fake(messages, schema)

    run_id, paused = api_run(project, "single", chat=chat)
    assert paused is None and sent
    parts = sent[0][1]["content"]
    texts = [p["text"] for p in parts if p["type"] == "text"]
    assert any("boxed by status" in t for t in texts)
    assert "- element_inventory:\n  Elements (fake):\n  1. element: removed, inside" in texts[-1]
    conn = connect(project / "project.sqlite")
    params = conn.execute("SELECT params_json FROM tool_run WHERE tool = 'element_inventory'").fetchone()[0]
    assert '"fixed"' in params and '"door"' in params


# --- the fixes to the earlier evidence --------------------------------------------------------------------------


def encoded(pixels: np.ndarray) -> bytes:
    buffer = io.BytesIO()
    Image.fromarray(pixels).save(buffer, format="PNG")
    return buffer.getvalue()


def test_the_change_map_separates_a_uniform_colour_shift_from_local_change() -> None:
    original = np.full((40, 40, 3), 110, dtype=np.uint8)
    original[:, :20] = 60
    brighter = (original.astype(int) + 25).clip(0, 255).astype(np.uint8)
    moved = brighter.copy()
    moved[0:8, 30:40] = (200, 30, 30)  # one local change outside the region
    region = np.zeros((40, 40), dtype=bool)
    region[15:25, 15:25] = True
    blobs = {sha256_bytes(b): b for b in (encoded(original), encoded(brighter), encoded(moved), local_imaging.mask_png(region))}
    names = list(blobs)
    tools = LocalTools()
    uniform = tools.run("change_map", [names[0], names[1], names[3]], {}, blobs.__getitem__)
    assert uniform.measures["share_changed"] == 0.0 and uniform.measures["share_changed_before_shift"] > 0.4
    assert uniform.measures["global_shift_delta_e"] > 5 and "lighter" in uniform.summary
    local = tools.run("change_map", [names[0], names[2], names[3]], {}, blobs.__getitem__)
    assert local.measures["share_changed"] == pytest.approx(80 / (1600 - 100), abs=1e-3)
    assert tools.version("change_map") != tools.version("outline")


def test_a_class_continued_from_the_region_edge_is_not_said_to_appear() -> None:
    names = {0: "wall", 1: "door", 2: "sofa"}
    region = np.zeros((40, 40), dtype=bool)
    region[10:30, 10:30] = True
    original = np.zeros((40, 40), dtype=np.int32)
    original[10:30, 10:30] = 2  # a sofa fills the region
    original[10:30, 8:10] = 1  # a door shows just left of it
    candidate = np.zeros((40, 40), dtype=np.int32)
    candidate[10:30, 8:16] = 1  # the edit completes the door
    candidate[12:16, 20:24] = 2  # a bit of sofa stays
    changes = compare_classes(original, candidate, region, names, {1: "door"}, 0.005)
    inside = changes.measures["inside"]
    assert {c["class"] for c in inside["continued"]} == {"wall", "door"} and inside["appeared"] == []
    assert changes.measures["opening_at_edge"] is True
    assert not changes.appeared[region].any()


def test_a_class_far_from_the_region_edge_still_appears() -> None:
    names = {0: "wall", 1: "door"}
    region = np.zeros((40, 40), dtype=bool)
    region[10:30, 10:30] = True
    original = np.zeros((40, 40), dtype=np.int32)
    candidate = original.copy()
    candidate[15:25, 15:25] = 1
    changes = compare_classes(original, candidate, region, names, {1: "door"}, 0.005)
    assert [c["class"] for c in changes.measures["inside"]["appeared"]] == ["door"]
    assert changes.measures["opening_at_edge"] is False


# --- the judge's request and schema -----------------------------------------------------------------------------


def test_the_schema_offers_no_move_to_the_current_level() -> None:
    defects = load_defects()
    dims = prune(load_release(defects), FAKE_CAPABILITIES)
    start = Point.of({d.key: d.default_ordinal for d in dims})
    schema = output_schema(defects, dims, JudgeRequestOptions(), start)
    variants = schema["properties"]["guidance"]["properties"]["moves"]["items"]["anyOf"]  # type: ignore[index]
    for variant in variants:
        key = variant["properties"]["dimension"]["enum"][0]
        dim = next(d for d in dims if d.key == key)
        current = dim.level(start.as_dict()[key]).label
        assert current not in variant["properties"]["to_level"]["enum"]
    unbound = output_schema(defects, dims)
    assert len(unbound["properties"]["guidance"]["properties"]["moves"]["items"]["anyOf"]) == len(dims)  # type: ignore[index]


def test_a_tool_summary_of_several_lines_is_indented_under_its_name() -> None:
    assert _tool_line("change_map", "one line") == "- change_map: one line"
    assert _tool_line("element_inventory", "a\nb") == "- element_inventory:\n  a\n  b"
