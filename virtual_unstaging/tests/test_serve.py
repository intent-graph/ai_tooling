"""The tool server on its fake recipe and fake tools: auth, blobs, capabilities, generate, tools, deadline, recipes."""

from __future__ import annotations

import io
import socket
import subprocess
import sys
import threading
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import numpy as np
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from virtual_unstaging.cli import main
from virtual_unstaging.clients.generators import ToolServerGenerator
from virtual_unstaging.clients.http import Endpoint, EndpointError
from virtual_unstaging.clients.remote_tools import RemoteTools
from virtual_unstaging.clients.toolserver import ToolServerClient
from virtual_unstaging.domain import (
    GeneratorCapabilities,
    GeneratorRequest,
    ModelRef,
    RoleImage,
    sha256_bytes,
)
from virtual_unstaging.serve import images as imaging
from virtual_unstaging.serve.app import create_app, run_server, watch_deadline
from virtual_unstaging.serve.auth import load_key
from virtual_unstaging.serve.blobdir import BlobDir
from virtual_unstaging.serve.deadline import Deadline, parse_deadline
from virtual_unstaging.serve.errors import STATUS_OF_CODE, ApiError, ServeConfigError
from virtual_unstaging.serve.generation import (
    FakeGenerator,
    GenerationJob,
    ImageInput,
    check_request,
    check_roles,
    plan_call,
)
from virtual_unstaging.serve.pixels import box_of, delta_e76, dilate_square
from virtual_unstaging.serve.recipe import FIELDS, available_recipes, load_recipe, parse_recipe
from virtual_unstaging.serve.tools import build_tools
from virtual_unstaging.serve.tools.changemap import FarnebackBackend, PhaseCorrelationBackend, measure_change
from virtual_unstaging.serve.tools.classdiff import BrightnessClassBackend, compare_classes, resolve_classes
from virtual_unstaging.serve.tools.segment import assign_labels, label_spans, suppress

KEY = "test-key-0123456789abcdef"
AUTH = {"Authorization": f"Bearer {KEY}"}
T0 = datetime(2026, 1, 1, 12, 0, 0, tzinfo=UTC)


class FakeClock:
    def __init__(self) -> None:
        self.now = T0

    def __call__(self) -> datetime:
        return self.now

    def advance(self, **kwargs: float) -> None:
        self.now += timedelta(**kwargs)


def png(pixels: np.ndarray) -> bytes:
    buffer = io.BytesIO()
    Image.fromarray(pixels).save(buffer, format="PNG")
    return buffer.getvalue()


def room(height: int = 48, width: int = 64, value: int = 120) -> np.ndarray:
    return np.full((height, width, 3), value, dtype=np.uint8)


def mask_png(height: int, width: int, rows: slice, columns: slice) -> bytes:
    mask = np.zeros((height, width), dtype=np.uint8)
    mask[rows, columns] = 255
    return png(mask)


def make_app(tmp_path: Path, clock: FakeClock | None = None, generator: bool = True, tools: bool = True) -> Any:
    clock = clock or FakeClock()
    return create_app(
        KEY,
        Deadline(T0 + timedelta(hours=1), clock),
        tmp_path / "data",
        FakeGenerator(load_recipe("fake")) if generator else None,
        build_tools(["fake"]) if tools else {},
        server_version="test",
    )


@pytest.fixture
def clock() -> FakeClock:
    return FakeClock()


@pytest.fixture
def client(tmp_path: Path, clock: FakeClock) -> TestClient:
    return TestClient(make_app(tmp_path, clock), headers=AUTH)


def put(client: TestClient, data: bytes) -> str:
    sha = sha256_bytes(data)
    assert client.put(f"/blobs/{sha}", content=data, headers={"Content-Type": "image/png"}).status_code == 201
    return sha


def error_code(response: Any) -> str:
    return str(response.json()["error"]["code"])


# --- auth -------------------------------------------------------------------------------------------------------


def test_every_endpoint_but_health_needs_the_key(tmp_path: Path) -> None:
    bare = TestClient(make_app(tmp_path))
    assert bare.get("/health").status_code == 200
    for method, path in [("get", "/capabilities"), ("head", f"/blobs/{'0' * 64}"), ("post", "/generate"), ("post", "/tools/class_diff")]:
        response = getattr(bare, method)(path)
        assert response.status_code == 401
        if method != "head":
            assert error_code(response) == "unauthorized"
    wrong = TestClient(make_app(tmp_path), headers={"Authorization": "Bearer not-the-key-0123456789"})
    assert wrong.get("/capabilities").status_code == 401
    assert TestClient(make_app(tmp_path), headers={"Authorization": f"Basic {KEY}"}).get("/capabilities").status_code == 401


def test_unknown_route_and_method_have_stable_codes(client: TestClient) -> None:
    assert error_code(client.get("/nope")) == "not_found"
    assert error_code(client.delete("/health")) == "bad_request"


def test_key_sources(tmp_path: Path) -> None:
    key_file = tmp_path / "key"
    key_file.write_text(KEY + "\n")
    assert load_key(key_file, None) == KEY
    assert load_key(None, "UNSTAGE_KEY", {"UNSTAGE_KEY": KEY}) == KEY
    with pytest.raises(ServeConfigError, match="exactly one"):
        load_key(key_file, "UNSTAGE_KEY", {})
    with pytest.raises(ServeConfigError, match="exactly one"):
        load_key(None, None)
    with pytest.raises(ServeConfigError, match="empty"):
        load_key(None, "UNSTAGE_KEY", {})
    with pytest.raises(ServeConfigError, match="at least"):
        load_key(None, "UNSTAGE_KEY", {"UNSTAGE_KEY": "short"})
    with pytest.raises(ServeConfigError, match="not an environment variable name"):
        load_key(None, "A B", {})
    with pytest.raises(ServeConfigError, match="cannot read"):
        load_key(tmp_path / "missing", None)


# --- blobs --------------------------------------------------------------------------------------------------------


def test_blob_put_head_get(client: TestClient) -> None:
    data = png(room())
    sha = sha256_bytes(data)
    assert client.head(f"/blobs/{sha}").status_code == 404
    first = client.put(f"/blobs/{sha}", content=data, headers={"Content-Type": "image/png"})
    again = client.put(f"/blobs/{sha}", content=data, headers={"Content-Type": "image/png"})
    assert first.status_code == again.status_code == 201
    assert client.head(f"/blobs/{sha}").status_code == 200
    got = client.get(f"/blobs/{sha}")
    assert got.status_code == 200 and got.content == data and got.headers["content-type"] == "image/png"


def test_blob_hash_mismatch_and_bad_input(client: TestClient) -> None:
    data = png(room())
    wrong = sha256_bytes(b"other")
    response = client.put(f"/blobs/{wrong}", content=data, headers={"Content-Type": "image/png"})
    assert response.status_code == 400 and error_code(response) == "hash_mismatch"
    assert client.head(f"/blobs/{wrong}").status_code == 404
    sha = sha256_bytes(data)
    assert error_code(client.put(f"/blobs/{sha}", content=data, headers={"Content-Type": "text/plain"})) == "bad_request"
    assert error_code(client.put(f"/blobs/{sha}", content=data, headers={"Content-Type": "image/jpeg"})) == "bad_request"
    junk = b"not an image at all"
    assert error_code(client.put(f"/blobs/{sha256_bytes(junk)}", content=junk, headers={"Content-Type": "image/png"})) == "bad_request"
    for bad in ("not-a-hash", "A" * 64, "0" * 63):
        assert client.get(f"/blobs/{bad}").status_code == 400
        assert error_code(client.get(f"/blobs/{bad}")) == "bad_request"
    assert error_code(client.get(f"/blobs/{'0' * 64}")) == "not_found"


def test_blob_paths_come_from_hashes_only(tmp_path: Path) -> None:
    blobs = BlobDir(tmp_path / "blobs")
    for bad in ("../../etc/passwd", "a" * 64 + "/..", "", "0" * 64 + "\n"):
        with pytest.raises(ApiError):
            blobs.path(bad)
    sha = blobs.add(b"x")
    assert blobs.path(sha).parent.parent == blobs.root


def test_oversized_blob_is_refused(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("virtual_unstaging.serve.app.MAX_BLOB_BYTES", 100)
    data = png(room())
    response = client.put(f"/blobs/{sha256_bytes(data)}", content=data, headers={"Content-Type": "image/png"})
    assert response.status_code == 400 and error_code(response) == "bad_request"


# --- capabilities and health ------------------------------------------------------------------------------------


def test_capabilities_and_health(client: TestClient, clock: FakeClock) -> None:
    caps = client.get("/capabilities").json()
    assert caps["api_version"] == "1.2" and caps["server_version"] == "test"
    generator = caps["generator"]
    assert {"model", "revision", "max_images", "roles", "native_mask", "text_only", "settings", "licence"} <= set(generator)
    assert generator["native_mask"] is False and "removal_mask" in generator["roles"]
    assert generator["text_only"] is True and generator["settings"]["output_aspect"] == 1.0
    assert {t["name"] for t in caps["tools"]} == {"segment_elements", "class_diff", "change_map", "element_inventory", "structure_map"}
    assert all(t["version"] and t["model"] for t in caps["tools"])
    health = client.get("/health").json()
    assert health["status"] == "ok" and health["api_version"] == "1.2" and health["seconds_left"] == 3600
    assert health["deadline"] == "2026-01-01T13:00:00Z"
    clock.advance(minutes=10)
    assert client.get("/health").json()["seconds_left"] == 3000


def test_capabilities_without_generator_or_tools(tmp_path: Path) -> None:
    caps = TestClient(make_app(tmp_path, generator=False, tools=False), headers=AUTH).get("/capabilities").json()
    assert caps["generator"] is None and caps["tools"] == []


# --- generate ---------------------------------------------------------------------------------------------------


def generate_body(original: str, mask: str | None = None, **extra: Any) -> dict[str, Any]:
    images = [{"role": "original", "sha256": original}]
    if mask:
        images.append({"role": "removal_mask", "sha256": mask})
    return {"prompt": "empty the room", "seed": 7, "settings": {}, "images": images, **extra}


def test_generate_fills_the_mask_and_stores_the_output(client: TestClient) -> None:
    pixels = room(48, 64, 120)
    pixels[10:30, 10:30] = (200, 0, 0)
    original = put(client, png(pixels))
    mask = put(client, mask_png(48, 64, slice(8, 32), slice(8, 32)))
    response = client.post("/generate", json=generate_body(original, mask))
    assert response.status_code == 200, response.text
    reply = response.json()
    assert reply["media_type"] == "image/png" and reply["gpu_seconds"] >= 0
    assert reply["width"] / reply["height"] == pytest.approx(64 / 48, rel=0.02)
    out = imaging.decode(client.get(f"/blobs/{reply['output_sha256']}").content)
    assert out.size == (reply["width"], reply["height"])
    centre = np.asarray(out)[out.height // 2, out.width // 2].astype(int)
    assert abs(centre - np.array([120, 120, 120])).max() < 12  # the red square is gone, wall colour is back


def test_generate_from_text_alone(client: TestClient) -> None:
    body = {"prompt": "an empty room", "seed": 3, "settings": {"output_aspect": 1.5}, "images": []}
    response = client.post("/generate", json=body)
    assert response.status_code == 200, response.text
    reply = response.json()
    assert reply["width"] / reply["height"] == pytest.approx(1.5, rel=0.03)
    out = imaging.decode(client.get(f"/blobs/{reply['output_sha256']}").content)
    assert out.size == (reply["width"], reply["height"])
    assert client.post("/generate", json=body).json()["output_sha256"] == reply["output_sha256"]  # seeded
    assert client.post("/generate", json={"prompt": "an empty room", "seed": 3}).status_code == 200  # images may be left out


def test_the_generator_can_be_switched_to_another_packaged_recipe(tmp_path: Path) -> None:
    app = make_app(tmp_path)
    state = app.state.server
    old = state.generator
    unloaded: list[bool] = []
    old.unload = lambda: unloaded.append(True)
    client = TestClient(app, headers=AUTH)
    reply = client.put("/generator", json={"recipe": "fake"})
    assert reply.status_code == 200, reply.text
    assert reply.json() == {"recipe": "fake", "state": "ready"} and unloaded == [True] and state.generator is not old
    for bad in ("../fake", "absent", "fake.toml"):
        assert client.put("/generator", json={"recipe": bad}).json()["error"]["code"] == "bad_request"
    assert client.put("/generator", json={"recipe": "fake"}, headers={"Authorization": "Bearer nope"}).status_code == 401


def test_a_request_accepted_before_a_switch_is_refused(tmp_path: Path) -> None:
    from virtual_unstaging.serve.app import GenerateBody, _prepare_generate

    app = make_app(tmp_path)
    client = TestClient(app, headers=AUTH)
    original, mask = put(client, png(room(48, 64, 120))), put(client, mask_png(48, 64, slice(8, 32), slice(8, 32)))
    execute = _prepare_generate(app.state.server, GenerateBody(**generate_body(original, mask)))
    assert client.put("/generator", json={"recipe": "fake"}).status_code == 200
    with pytest.raises(ApiError) as refused:
        execute(lambda: None)
    assert refused.value.code == "generator_changed"


def test_generate_is_deterministic_in_seed_and_prompt(client: TestClient) -> None:
    original = put(client, png(room()))
    mask = put(client, mask_png(48, 64, slice(8, 32), slice(8, 32)))
    one = client.post("/generate", json=generate_body(original, mask)).json()["output_sha256"]
    two = client.post("/generate", json=generate_body(original, mask)).json()["output_sha256"]
    other = client.post("/generate", json={**generate_body(original, mask), "seed": 8}).json()["output_sha256"]
    assert one == two and one != other


def test_generate_errors(client: TestClient, tmp_path: Path) -> None:
    original = put(client, png(room()))
    mask = put(client, mask_png(48, 64, slice(0, 8), slice(0, 8)))
    absent = sha256_bytes(b"absent")
    response = client.post("/generate", json=generate_body(original, absent))
    assert response.status_code == 404 and error_code(response) == "blob_missing" and absent in response.json()["error"]["message"]
    body = generate_body(original, mask)
    assert error_code(client.post("/generate", json={**body, "images": [{"role": "banana", "sha256": original}]})) == "bad_request"
    assert error_code(client.post("/generate", json={**body, "images": [{"role": "reference", "sha256": original}]})) == "bad_request"
    two_originals = [{"role": "original", "sha256": original}] * 2
    assert error_code(client.post("/generate", json={**body, "images": two_originals})) == "bad_request"
    seven = [{"role": "original", "sha256": original}] + [{"role": "reference", "sha256": original}] * 6
    assert error_code(client.post("/generate", json={**body, "images": seven})) == "bad_request"
    assert error_code(client.post("/generate", json={**body, "settings": {"nonsense": 1}})) == "bad_request"
    assert error_code(client.post("/generate", json={**body, "settings": {"num_inference_steps": 0}})) == "bad_request"
    assert error_code(client.post("/generate", json={**body, "extra": 1})) == "bad_request"
    assert error_code(client.post("/generate", json={**body, "seed": -1})) == "bad_request"
    assert error_code(client.post("/generate", json={"prompt": "x"})) == "bad_request"
    assert error_code(client.post("/generate", content=b"{not json", headers={"Content-Type": "application/json"})) == "bad_request"
    bare = TestClient(make_app(tmp_path / "other", generator=False), headers=AUTH)
    response = bare.post("/generate", json=body)
    assert response.status_code == 503 and error_code(response) == "generator_unavailable"


def test_generate_settings_reach_the_adapter(tmp_path: Path) -> None:
    generator = FakeGenerator(load_recipe("fake"))
    app = create_app(KEY, Deadline(T0 + timedelta(hours=1), FakeClock()), tmp_path, generator, {}, "test")
    client = TestClient(app, headers=AUTH)
    original = put(client, png(room()))
    reply = client.post("/generate", json=generate_body(original, settings={"num_inference_steps": 3, "output_side": 256}))
    assert reply.status_code == 200
    plan = generator.calls[-1]
    assert plan.arguments["num_inference_steps"] == 3 and plan.arguments["true_cfg_scale"] == 4.0
    assert plan.width * plan.height <= 256 * 256 and "output_side" not in plan.arguments


# --- tools ------------------------------------------------------------------------------------------------------


def run_tool(client: TestClient, name: str, inputs: list[str], params: dict[str, Any] | None = None) -> Any:
    return client.post(f"/tools/{name}", json={"inputs": inputs, "params": params or {}})


def test_segment_elements(client: TestClient) -> None:
    pixels = np.zeros((40, 60, 3), dtype=np.uint8) + 100
    pixels[:, 0:20] = (230, 20, 20)
    pixels[:, 30:45] = (20, 230, 20)
    image = put(client, png(pixels))
    response = run_tool(client, "segment_elements", [image], {"labels": ["red box", "green box", "blue box"], "threshold": 0.4})
    assert response.status_code == 200, response.text
    reply = response.json()
    assert reply["tool"] == "segment_elements" and reply["version"] and reply["gpu_seconds"] >= 0
    assert set(reply["outputs"]) == {"mask", "mask_0", "mask_1", "mask_2"}
    found = reply["measures"]["found"]
    assert found == {"red box": pytest.approx(800 / 2400, abs=1e-4), "green box": pytest.approx(600 / 2400, abs=1e-4), "blue box": 0.0}
    union = imaging.decode(client.get(f"/blobs/{reply['outputs']['mask']}").content, "L")
    assert int((np.asarray(union) > 127).sum()) == 1400
    first = imaging.decode(client.get(f"/blobs/{reply['outputs']['mask_0']}").content, "L")
    assert int((np.asarray(first) > 127).sum()) == 800
    assert "found 2 of 3" in reply["summary"] and "not found: blue box" in reply["summary"]


def test_segment_elements_parses_its_params(client: TestClient) -> None:
    image = put(client, png(room()))
    for params in (
        {},
        {"labels": []},
        {"labels": "chair"},
        {"labels": ["chair", "Chair"]},
        {"labels": ["chair; rm -rf /"]},
        {"labels": ["chair"], "threshold": 2},
        {"labels": ["chair"], "threshold": True},
        {"labels": ["chair"], "extra": 1},
        {"labels": [f"label {i}" for i in range(65)]},
    ):
        response = run_tool(client, "segment_elements", [image], params)
        assert response.status_code == 400 and error_code(response) == "bad_request", params


def test_class_diff_finds_a_new_opening_and_a_vanished_window(client: TestClient) -> None:
    original = room(64, 64, 120)
    original[0:10, 0:10] = 230  # a bright window outside the region
    candidate = room(64, 64, 120)
    candidate[20:40, 20:40] = 20  # a dark door appears inside the region
    region = mask_png(64, 64, slice(16, 48), slice(16, 48))
    shas = [put(client, png(original)), put(client, png(candidate)), put(client, region)]
    response = run_tool(client, "class_diff", shas)
    assert response.status_code == 200, response.text
    reply = response.json()
    measures = reply["measures"]
    assert measures["opening_share_of_region"] == pytest.approx(400 / 1024, abs=1e-4)
    assert measures["opening_box"] == [0.3125, 0.3125, 0.625, 0.625]
    assert measures["region_share"] == pytest.approx(0.25)
    assert [c["class"] for c in measures["inside"]["appeared"]] == ["door"]
    assert [c["class"] for c in measures["outside"]["vanished"]] == ["windowpane"]
    assert measures["outside"]["vanished"][0]["box"] == [0.0, 0.0, 0.1562, 0.1562]
    assert "became door/windowpane" in reply["summary"] and "39.1%" in reply["summary"]
    assert "(0.31, 0.31)-(0.62, 0.62)" in reply["summary"] or "(0.31, 0.31)-(0.63, 0.63)" in reply["summary"]
    picture = imaging.decode(client.get(f"/blobs/{reply['outputs']['map']}").content)
    assert picture.size == (64, 64)
    assert tuple(np.asarray(picture)[30, 30]) == (255, 40, 40)  # red where the opening appeared


def test_class_diff_without_change_and_with_named_classes(client: TestClient) -> None:
    image = put(client, png(room(32, 32, 120)))
    region = put(client, mask_png(32, 32, slice(8, 24), slice(8, 24)))
    reply = run_tool(client, "class_diff", [image, image, region], {"opening_classes": ["windowpane"]}).json()
    assert reply["measures"]["opening_classes"] == ["windowpane"]
    assert reply["measures"]["opening_share_of_region"] == 0.0 and reply["measures"]["opening_box"] is None
    assert "no pixel became windowpane" in reply["summary"] and "no class appeared or vanished" in reply["summary"]
    response = run_tool(client, "class_diff", [image, image, region], {"opening_classes": ["spaceship"]})
    assert response.status_code == 400 and error_code(response) == "bad_request"
    assert run_tool(client, "class_diff", [image, image, region], {"opening_classes": ["door; drop"]}).status_code == 400
    assert run_tool(client, "class_diff", [image, image, region], {"unknown": 1}).status_code == 400


def test_change_map_reports_displacement_outside_the_region(client: TestClient) -> None:
    rng = np.random.default_rng(3)
    texture = rng.integers(0, 256, size=(96, 96, 3), dtype=np.uint8)
    shifted = np.roll(texture, 5, axis=1)
    region = mask_png(96, 96, slice(40, 56), slice(40, 56))
    shas = [put(client, png(texture)), put(client, png(shifted)), put(client, region)]
    response = run_tool(client, "change_map", shas)
    assert response.status_code == 200, response.text
    reply = response.json()
    measures = reply["measures"]
    assert measures["displacement_median_pct"] == pytest.approx(100 * 5 / 96, abs=0.01)
    assert measures["displacement_p95_pct"] == pytest.approx(100 * 5 / 96, abs=0.01)
    assert measures["global_shift_px"] == [5.0, 0.0]
    assert measures["delta_e_median"] > 1.0
    assert "median shift 5.21%" in reply["summary"]
    heat = np.asarray(imaging.decode(client.get(f"/blobs/{reply['outputs']['heatmap']}").content))
    assert tuple(heat[48, 48]) == (50, 60, 100)  # the region is drawn apart, not measured
    still = run_tool(client, "change_map", [shas[0], shas[0], shas[2]]).json()["measures"]
    assert still["displacement_median_pct"] == 0.0 and still["delta_e_median"] == 0.0


def test_change_map_with_the_region_covering_the_frame(client: TestClient) -> None:
    image = put(client, png(room(32, 32)))
    full = put(client, mask_png(32, 32, slice(0, 32), slice(0, 32)))
    reply = run_tool(client, "change_map", [image, image, full]).json()
    assert reply["measures"]["displacement_median_pct"] is None and "nothing outside it to measure" in reply["summary"]


def test_candidate_of_another_size_is_resized(client: TestClient) -> None:
    original = put(client, png(room(64, 64)))
    candidate = put(client, png(room(96, 96)))
    region = put(client, mask_png(64, 64, slice(0, 8), slice(0, 8)))
    assert run_tool(client, "change_map", [original, candidate, region]).json()["measures"]["candidate_resized"] is True
    assert run_tool(client, "class_diff", [original, candidate, region]).json()["measures"]["candidate_resized"] is True


def test_tool_errors(client: TestClient, tmp_path: Path) -> None:
    image = put(client, png(room()))
    assert error_code(run_tool(client, "nope", [image])) == "tool_unknown"
    assert run_tool(client, "nope", [image]).status_code == 404
    assert error_code(run_tool(client, "class_diff", [image])) == "bad_request"  # needs three images
    assert error_code(run_tool(client, "segment_elements", [image, image], {"labels": ["a"]})) == "bad_request"
    missing = sha256_bytes(b"missing")
    response = run_tool(client, "segment_elements", [missing], {"labels": ["red"]})
    assert response.status_code == 404 and error_code(response) == "blob_missing"
    assert error_code(run_tool(client, "segment_elements", ["../etc/passwd"], {"labels": ["red"]})) == "bad_request"
    assert error_code(client.post("/tools/segment_elements", json={"inputs": [image], "params": {"labels": ["a"]}, "x": 1})) == "bad_request"
    only_one = TestClient(
        create_app(KEY, Deadline(T0 + timedelta(hours=1), FakeClock()), tmp_path / "one", None, {"change_map": build_tools(["fake"])["change_map"]}),
        headers=AUTH,
    )
    assert error_code(only_one.post("/tools/class_diff", json={"inputs": [image], "params": {}})) == "tool_unknown"


def test_a_tool_that_raises_is_reported_as_tool_failed(client: TestClient) -> None:
    tool = client.app.state.server.tools["change_map"]  # type: ignore[attr-defined]

    def boom(*_: Any, **__: Any) -> Any:
        raise RuntimeError("out of memory")

    tool.run = boom
    image = put(client, png(room()))
    response = run_tool(client, "change_map", [image, image, image])
    assert response.status_code == 500 and error_code(response) == "tool_failed" and "out of memory" in response.json()["error"]["message"]


# --- deadline ---------------------------------------------------------------------------------------------------


def test_deadline_parsing() -> None:
    assert parse_deadline("90m", T0) == T0 + timedelta(minutes=90)
    assert parse_deadline("2h", T0) == T0 + timedelta(hours=2)
    assert parse_deadline("1h30m", T0) == T0 + timedelta(minutes=90)
    assert parse_deadline("45s", T0) == T0 + timedelta(seconds=45)
    assert parse_deadline("2026-01-01T15:00:00Z", T0) == T0 + timedelta(hours=3)
    assert parse_deadline("2026-01-01T15:00:00+00:00", T0) == T0 + timedelta(hours=3)
    for bad in ("", "  ", "soon", "0m", "m", "90", "2026-01-01T15:00:00", "2026-01-01T15:00:00+02:00", "2025-01-01T00:00:00Z", "-5m"):
        with pytest.raises(ServeConfigError):
            parse_deadline(bad, T0)


def test_past_the_deadline_everything_but_health_answers_503(client: TestClient, clock: FakeClock) -> None:
    original = put(client, png(room()))
    assert client.get("/capabilities").status_code == 200
    clock.advance(hours=1, seconds=1)
    for response in (
        client.get("/capabilities"),
        client.post("/generate", json=generate_body(original)),
        client.post("/tools/change_map", json={"inputs": [original] * 3, "params": {}}),
        client.get(f"/blobs/{original}"),
        client.put(f"/blobs/{original}", content=b"x", headers={"Content-Type": "image/png"}),
    ):
        assert response.status_code == 503 and error_code(response) == "deadline_reached"
    health = client.get("/health")
    assert health.status_code == 200 and health.json()["status"] == "deadline_reached" and health.json()["seconds_left"] == 0
    assert TestClient(client.app).get("/capabilities").status_code == 401  # the key is still checked first


def test_work_that_waited_for_the_gpu_past_the_deadline_is_refused(tmp_path: Path, clock: FakeClock) -> None:
    app = make_app(tmp_path, clock)
    state = app.state.server
    with pytest.raises(ApiError) as caught:
        clock.advance(hours=2)
        with state.gpu():
            pytest.fail("must not start")
    assert caught.value.code == "deadline_reached"


def test_the_deadline_watch_calls_back_once_idle(tmp_path: Path, clock: FakeClock) -> None:
    state = make_app(tmp_path, clock).state.server
    stop, done = threading.Event(), threading.Event()
    thread = threading.Thread(target=watch_deadline, args=(state, stop, done.set, 1.0, 0.01))
    thread.start()
    time.sleep(0.05)
    assert not done.is_set()
    state.enter()  # a call in flight holds the exit back
    clock.advance(hours=2)
    assert not done.wait(0.1)
    state.leave()
    assert done.wait(2.0)
    thread.join(2.0)


def test_the_deadline_watch_gives_up_waiting_after_the_grace(tmp_path: Path, clock: FakeClock) -> None:
    state = make_app(tmp_path, clock).state.server
    state.enter()
    clock.advance(hours=2)
    done = threading.Event()
    thread = threading.Thread(target=watch_deadline, args=(state, threading.Event(), done.set, 0.05, 0.01))
    thread.start()
    assert done.wait(2.0)
    thread.join(2.0)


def test_gpu_work_is_serialised(tmp_path: Path, clock: FakeClock) -> None:
    state = make_app(tmp_path, clock).state.server
    inside: list[int] = []
    overlap = []

    def work() -> None:
        with state.gpu():
            inside.append(1)
            if len(inside) > 1:
                overlap.append(True)
            time.sleep(0.02)
            inside.pop()

    threads = [threading.Thread(target=work) for _ in range(6)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert not overlap


# --- start-up checks ----------------------------------------------------------------------------------------------


def test_the_server_refuses_to_start_without_a_deadline_or_key(tmp_path: Path) -> None:
    key_file = tmp_path / "key"
    key_file.write_text(KEY)
    base: dict[str, Any] = dict(host="127.0.0.1", port=0, key_file=key_file, key_env=None, recipe=None, tools=[], data_dir=tmp_path)
    for deadline in (None, "", "soon", "0m"):
        with pytest.raises(ServeConfigError):
            run_server(deadline=deadline, **base)
    with pytest.raises(ServeConfigError, match="exactly one"):
        run_server(deadline="1h", **{**base, "key_file": None})
    with pytest.raises(ServeConfigError, match="unknown recipe"):
        run_server(deadline="1h", **{**base, "recipe": "no_such_recipe"})
    with pytest.raises(ServeConfigError, match="unknown tool"):
        run_server(deadline="1h", **{**base, "tools": ["bogus"]})


def test_the_command_line_reports_a_usage_error_not_a_traceback(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["serve", "--deadline", "1h", "--data-dir", str(tmp_path)]) == 1
    assert "exactly one of --key-file or --key-env" in capsys.readouterr().err
    with pytest.raises(SystemExit):
        main(["serve", "--key-env", "X"])  # --deadline is required by the parser


def test_importing_the_server_loads_no_heavy_library() -> None:
    code = (
        "import sys, virtual_unstaging.serve.app, virtual_unstaging.serve.tools, virtual_unstaging.serve.generation;"
        "heavy = [m for m in ('torch', 'diffusers', 'transformers', 'cv2') if m in sys.modules];"
        "sys.exit(1 if heavy else 0)"
    )
    assert subprocess.run([sys.executable, "-c", code], check=False).returncode == 0


# --- recipes ----------------------------------------------------------------------------------------------------------

EXPECTED_PIPELINES = {
    "qwen_image_edit_2511": "QwenImageEditPlusPipeline",
    "firered_image_edit_1_1": "QwenImageEditPlusPipeline",
    "flux2_dev": "Flux2Pipeline",
    "flux2_klein_9b": "Flux2KleinPipeline",
    "flux2_klein_4b": "Flux2KleinPipeline",
    "qwen_image_2_1_turbo": "QwenImage21Pipeline",
    "qwen_image_edit_2511_lightning": "QwenImageEditPlusPipeline",
    "qwen_image_edit_2511_lightning_resident": "QwenImageEditPlusPipeline",
    "qwen_image_2_1": "QwenImage21Pipeline",
    "fibo_2_0_edit": "BriaFibo2Pipeline",
    "fibo_2_0_dev_edit": "BriaFibo2Pipeline",
}


def test_the_packaged_recipes() -> None:
    names = set(available_recipes())
    assert names == set(EXPECTED_PIPELINES) | {"fake"}
    for name, pipeline in EXPECTED_PIPELINES.items():
        recipe = load_recipe(name)
        assert recipe.name == name and recipe.pipeline_class == pipeline and recipe.adapter == "diffusers"
        assert len(recipe.revision) == 40 and recipe.licence and set(recipe.unverified) <= set(FIELDS)
        assert recipe.steps_argument in recipe.defaults
        profile = recipe.profile()
        assert profile["model"] == recipe.repository and profile["unverified"] == list(recipe.unverified)
    assert load_recipe("fibo_2_0_edit").native_mask and not load_recipe("flux2_dev").native_mask


def test_a_recipe_by_file_path(tmp_path: Path) -> None:
    text = (Path(__file__).parent.parent / "src/virtual_unstaging/serve/recipes/fake.toml").read_text()
    path = tmp_path / "mine.toml"
    path.write_text(text.replace('name = "fake"', 'name = "mine"'))
    assert load_recipe(str(path)).name == "mine"
    with pytest.raises(ServeConfigError, match="unknown recipe"):
        load_recipe(str(tmp_path / "absent.toml"))
    with pytest.raises(ServeConfigError, match="unknown recipe"):
        load_recipe("../fake")


def fake_text() -> str:
    return (Path(__file__).parent.parent / "src/virtual_unstaging/serve/recipes/fibo_2_0_edit.toml").read_text()


def test_a_recipe_is_parsed_strictly() -> None:
    text = fake_text()
    assert parse_recipe(text).native_mask
    broken = {
        "unknown key": text.replace('adapter = "diffusers"', 'adapter = "diffusers"\nsurprise = 1'),
        "unknown table key": text.replace('dtype = "bfloat16"', 'dtype = "bfloat16"\nextra = 1'),
        "bad dtype": text.replace("bfloat16", "bfloat8"),
        "bad revision": text.replace("7a7f8221ccec999ccac0ea309b93e859e1f49ab5", "main"),
        "bad class": text.replace('class = "BriaFibo2Pipeline"', 'class = "os.system"'),
        "bad repository": text.replace("briaai/Fibo-2.0-edit-turbo", "../../etc"),
        "mask without argument": text.replace('mask_argument = "mask"\n', ""),
        "unknown role": text.replace('"reference", "removal_mask"]', '"banana", "removal_mask"]'),
        "no original": text.replace('roles = ["original", ', 'roles = ['),
        "bad unverified": text.replace('unverified = ["placement"', 'unverified = ["colour"'),
        "bad fp8 storage": text.replace('dtype = "bfloat16"', 'dtype = "bfloat16"\nfp8_storage = ["os.system"]'),
        "repeated fp8 storage": text.replace('dtype = "bfloat16"', 'dtype = "bfloat16"\nfp8_storage = ["unet", "unet"]'),
        "steps not a default": text.replace('steps_argument = "num_inference_steps"', 'steps_argument = "iterations"'),
        "bad passing": text.replace('"single_when_one"', '"tuple"'),
        "mask limit too high": text.replace("max_images_with_native_mask = 1", "max_images_with_native_mask = 9"),
        "text_only not a boolean": text.replace("native_mask = true", 'native_mask = true\ntext_only = "yes"'),
        "not toml": "name = ",
    }
    for label, bad in broken.items():
        with pytest.raises(ServeConfigError):
            parse_recipe(bad)
        assert bad != text, label


def test_settings_are_checked_against_the_recipe() -> None:
    recipe = load_recipe("qwen_image_edit_2511")
    assert recipe.settings_for({})["num_inference_steps"] == 40
    merged = recipe.settings_for({"num_inference_steps": 12, "true_cfg_scale": 3, "negative_prompt": "blur", "output_side": 768})
    assert merged["num_inference_steps"] == 12 and merged["true_cfg_scale"] == 3.0 and merged["output_side"] == 768
    for bad in ({"seed": 1}, {"num_inference_steps": True}, {"num_inference_steps": 2.5}, {"num_inference_steps": 0},
                {"true_cfg_scale": float("inf")}, {"true_cfg_scale": "4"}, {"negative_prompt": 3}, {"output_side": 100},
                {"output_side": 1024.0}, {"output_side": True}):
        with pytest.raises(ApiError):
            recipe.settings_for(bad)  # type: ignore[arg-type]


def job(recipe_name: str, roles: list[str], size: tuple[int, int] = (400, 300), settings: dict[str, Any] | None = None) -> tuple[Any, GenerationJob]:
    recipe = load_recipe(recipe_name)
    check_roles(recipe, roles)
    images = tuple(
        ImageInput(role, Image.new("L" if role.endswith("_mask") else "RGB", size if role in ("original", "removal_mask") else (200, 100)))
        for role in roles
    )
    return recipe, GenerationJob("a prompt", 42, recipe.settings_for(settings or {}), images)


def test_plan_for_a_list_pipeline_keeps_the_order_and_sends_the_mask_as_an_image() -> None:
    recipe, the_job = job("qwen_image_edit_2511", ["original", "removal_mask", "reference"])
    plan = plan_call(recipe, the_job)
    assert [im.size for im in plan.arguments["image"]] == [(400, 300), (400, 300), (200, 100)]
    assert all(im.mode == "RGB" for im in plan.arguments["image"])
    assert "mask" not in plan.arguments and plan.arguments["prompt"] == "a prompt" and plan.seed == 42
    assert (plan.arguments["width"], plan.arguments["height"]) == (1152, 864) == (plan.width, plan.height)
    assert plan.arguments["num_inference_steps"] == 40 and plan.arguments["true_cfg_scale"] == 4.0
    assert plan.arguments["negative_prompt"] == " " and "output_side" not in plan.arguments


def test_plan_follows_the_order_the_orchestrator_chose() -> None:
    recipe, the_job = job("qwen_image_2_1", ["reference", "original"])
    assert [im.size for im in plan_call(recipe, the_job).arguments["image"]] == [(200, 100), (400, 300)]


def test_plan_for_a_native_mask_pipeline() -> None:
    recipe, the_job = job("fibo_2_0_edit", ["original", "removal_mask"], settings={"output_side": 512})
    plan = plan_call(recipe, the_job)
    assert isinstance(plan.arguments["image"], Image.Image) and plan.arguments["image"].size == (400, 300)
    assert plan.arguments["mask"].mode == "L" and plan.arguments["mask"].size == (400, 300)
    assert plan.arguments["num_inference_steps"] == 4 and plan.arguments["guidance_scale"] == 1.0
    assert (plan.width, plan.height) == (576, 416) and plan.width % 32 == 0 and plan.height % 32 == 0
    without_mask = plan_call(*job("fibo_2_0_edit", ["original", "reference"]))
    assert isinstance(without_mask.arguments["image"], list) and "mask" not in without_mask.arguments
    with pytest.raises(ApiError, match="at most 1 image"):
        job("fibo_2_0_edit", ["original", "removal_mask", "reference"])


def test_native_mask_of_another_size_is_resized_to_the_original() -> None:
    recipe = load_recipe("fibo_2_0_edit")
    images = (ImageInput("original", Image.new("RGB", (400, 300))), ImageInput("removal_mask", Image.new("L", (100, 75), 255)))
    plan = plan_call(recipe, GenerationJob("p", 1, recipe.settings_for({}), images))
    assert plan.arguments["mask"].size == (400, 300) and plan.arguments["mask"].getextrema() == (255, 255)


def test_condition_images_are_reduced_for_a_speed_version_and_the_setting_stays_out_of_the_pipeline() -> None:
    recipe, the_job = job("flux2_klein_4b", ["original", "removal_mask", "reference"], size=(1600, 1200),
                          settings={"output_side": 512, "condition_side": 400})
    plan = plan_call(recipe, the_job)
    sizes = [im.size for im in plan.arguments["image"]]
    assert sizes[0][0] * sizes[0][1] <= 400 * 400 and sizes[0][0] / sizes[0][1] == pytest.approx(4 / 3, abs=0.01)
    assert sizes[1] == sizes[0] and sizes[2] == (200, 100)  # the mask follows the original; a small image is kept
    assert "condition_side" not in plan.arguments and "output_side" not in plan.arguments
    native = plan_call(*job("fibo_2_0_edit", ["original", "removal_mask"], size=(1600, 1200), settings={"condition_side": 400}))
    assert native.arguments["mask"].size == native.arguments["image"].size
    full = plan_call(*job("flux2_klein_4b", ["original"], size=(1600, 1200)))
    assert full.arguments["image"][0].size == (1600, 1200)  # 0, the default: as given
    recipe = load_recipe("flux2_klein_4b")
    assert recipe.settings_for({})["condition_side"] == 0 and recipe.profile()["settings"]["condition_side"] == 0
    for bad in ({"condition_side": 100}, {"condition_side": 4096}, {"condition_side": True}, {"condition_side": 512.0}):
        with pytest.raises(ApiError):
            recipe.settings_for(bad)  # type: ignore[arg-type]


def test_role_checks_per_recipe() -> None:
    flux = load_recipe("flux2_dev")
    check_roles(flux, ["original", "reference", "removal_mask", "protected_mask"])
    with pytest.raises(ApiError, match="exactly one"):
        check_roles(flux, ["reference"])
    with pytest.raises(ApiError, match="at most 6"):
        check_roles(flux, ["original", *["reference"] * 6])
    with pytest.raises(ApiError, match="not accepted"):
        check_roles(load_recipe("fibo_2_0_edit"), ["original", "protected_mask"])
    with pytest.raises(ApiError, match="at most one"):
        check_roles(load_recipe("fibo_2_0_edit"), ["original", "removal_mask", "removal_mask"])


def test_a_text_only_request_has_no_image_argument_and_the_requested_shape() -> None:
    recipe = load_recipe("fake")
    settings = check_request(recipe, [], {"output_aspect": 1.5, "output_side": 512})
    plan = plan_call(recipe, GenerationJob("an empty room", 3, settings, ()))
    assert "image" not in plan.arguments and plan.arguments["prompt"] == "an empty room"
    assert (plan.width, plan.height) == (624, 416) == (plan.arguments["width"], plan.arguments["height"])
    assert "output_aspect" not in plan.arguments and "output_side" not in plan.arguments
    square = plan_call(recipe, GenerationJob("p", 1, check_request(recipe, [], {}), ()))
    assert square.width == square.height
    with pytest.raises(ApiError, match="applies only without images"):
        check_request(recipe, ["original"], {"output_aspect": 1.5})
    for bad in (0.1, 5, True, "1.5", float("inf")):
        with pytest.raises(ApiError):
            check_request(recipe, [], {"output_aspect": bad})  # type: ignore[dict-item]


def test_a_recipe_that_is_not_text_only_needs_an_original() -> None:
    editor = load_recipe("qwen_image_edit_2511")
    assert not editor.text_only and editor.profile()["text_only"] is False
    with pytest.raises(ApiError, match="does not generate from text alone"):
        check_roles(editor, [])
    with pytest.raises(ApiError, match="unknown setting"):
        editor.settings_for({"output_aspect": 1.5})
    klein = load_recipe("flux2_klein_4b")
    assert klein.text_only and "text_only" in klein.unverified  # declared from the model's documentation, not run yet


def test_output_size_keeps_the_aspect_ratio() -> None:
    for original in ((400, 300), (300, 400), (1000, 1000), (6000, 1500), (90, 5000)):
        width, height = imaging.output_size(original, 1024, 32)
        assert width % 32 == 0 and height % 32 == 0 and width >= 32 and height >= 32
        if min(original) > 1000 or original[0] / original[1] < 4:
            assert width / height == pytest.approx(original[0] / original[1], rel=0.08)


# --- pure cores --------------------------------------------------------------------------------------------------------


def test_dilation_matches_a_brute_force_window() -> None:
    rng = np.random.default_rng(1)
    mask = rng.random((20, 25)) > 0.93
    for radius in (0, 1, 3):
        expected = np.zeros_like(mask)
        for y, x in zip(*np.where(mask), strict=True):
            expected[max(0, y - radius) : y + radius + 1, max(0, x - radius) : x + radius + 1] = True
        assert (dilate_square(mask, radius) == expected).all()


def test_colour_difference_and_boxes() -> None:
    white, black = np.full((2, 2, 3), 255, np.uint8), np.zeros((2, 2, 3), np.uint8)
    assert delta_e76(white, black) == pytest.approx(np.full((2, 2), 100.0), abs=0.05)
    assert delta_e76(white, white).max() == 0
    mask = np.zeros((10, 20), dtype=bool)
    mask[2:5, 4:10] = True
    assert box_of(mask) == [0.2, 0.2, 0.5, 0.5] and box_of(~mask & False) is None


def test_labels_come_from_the_detector_token_scores() -> None:
    # "[CLS] chair . built - in cupboard . table . [SEP]" with "." = 9, CLS = 1, SEP = 2
    tokens = [1, 30, 9, 31, 32, 33, 34, 9, 35, 9, 2]
    spans = label_spans(tokens, {1, 2, 9}, 3)
    assert spans == [[1], [3, 4, 5, 6], [8]]
    with pytest.raises(ValueError):
        label_spans(tokens, {1, 2, 9}, 4)
    scores = np.zeros((3, len(tokens)), dtype=np.float32)
    scores[0, 1] = 0.8  # query 0: chair
    scores[1, 5] = 0.6  # query 1: one token of "built - in cupboard" carries the label
    scores[1, 8] = 0.4
    scores[2, 8] = 0.2  # query 2: below the threshold
    assert assign_labels(scores, spans, 0.3) == [(0, 0, pytest.approx(0.8)), (1, 1, pytest.approx(0.6))]
    found = [(0, [0.0, 0.0, 10.0, 10.0], 0.5), (0, [1.0, 0.0, 10.0, 10.0], 0.9), (1, [0.0, 0.0, 10.0, 10.0], 0.4)]
    assert suppress(found, 0.7) == [(0, [1.0, 0.0, 10.0, 10.0], 0.9), (1, [0.0, 0.0, 10.0, 10.0], 0.4)]


def test_class_names_resolve_through_aliases() -> None:
    names = {0: "wall", 8: "windowpane;window", 14: "door;double;door", 58: "screen door;screen;door"}
    assert resolve_classes(["door", "window", "doorway"], names) == {14: "door", 58: "screen door", 8: "windowpane"}
    assert resolve_classes(["wall"], names) == {0: "wall"}
    with pytest.raises(ApiError):
        resolve_classes(["spaceship"], names)


def test_compare_classes_core() -> None:
    names = BrightnessClassBackend().class_names()
    before = np.zeros((20, 20), dtype=np.int32)
    after = before.copy()
    after[5:10, 5:10] = 1  # door
    region = np.zeros((20, 20), dtype=bool)
    region[4:12, 4:12] = True
    changes = compare_classes(before, after, region, names, {1: "door"}, 0.005)
    assert changes.measures["opening_share_of_region"] == pytest.approx(25 / 64, abs=1e-4)
    assert changes.measures["opening_share_outside"] == 0.0
    assert changes.became_opening.sum() == 25 and changes.lost_opening.sum() == 0
    empty = compare_classes(before, after, np.zeros((20, 20), dtype=bool), names, {1: "door"}, 0.005)
    assert empty.measures["opening_share_of_region"] == 0.0 and empty.measures["opening_share_outside"] > 0


def test_measure_change_core_on_a_known_shift() -> None:
    rng = np.random.default_rng(5)
    base = Image.fromarray(rng.integers(0, 256, size=(80, 120, 3), dtype=np.uint8))
    moved = Image.fromarray(np.roll(np.asarray(base), -4, axis=0))
    region = np.zeros((80, 120), dtype=bool)
    change = measure_change(base, moved, region, 0.0, PhaseCorrelationBackend())
    assert change.measures["global_shift_px"] == [0.0, -4.0]
    assert change.measures["displacement_median_pct"] == pytest.approx(100 * 4 / 120, abs=0.01)


def test_the_opencv_flow_sees_a_smooth_shift() -> None:
    cv2 = pytest.importorskip("cv2")
    rng = np.random.default_rng(2)
    noise = rng.integers(0, 256, size=(128, 160), dtype=np.uint8)
    smooth = cv2.GaussianBlur(noise, (0, 0), 3)
    smooth = cv2.normalize(smooth, None, 0, 255, cv2.NORM_MINMAX)
    base = Image.fromarray(np.repeat(smooth[..., None], 3, axis=2))
    moved = Image.fromarray(np.roll(np.asarray(base), 4, axis=1))
    region = np.zeros((128, 160), dtype=bool)
    region[50:70, 60:90] = True
    change = measure_change(base, moved, region, 0.02, FarnebackBackend())
    assert change.measures["displacement_median_pct"] == pytest.approx(100 * 4 / 160, abs=0.8)
    assert change.measures["global_shift_px"][0] == pytest.approx(4.0, abs=1.0)


def test_error_codes_are_the_contract_codes() -> None:
    assert set(STATUS_OF_CODE) == {
        "unauthorized", "not_found", "blob_missing", "hash_mismatch", "bad_request", "generator_unavailable",
        "generator_failed", "generator_changed", "tool_unknown", "tool_failed", "deadline_reached",
    }
    with pytest.raises(ValueError):
        ApiError("made_up", "x")


# --- the real HTTP server, driven by the orchestrator's own clients ------------------------------------------------


def free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


def wait_until(condition: Any, seconds: float = 10.0) -> None:
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        if condition():
            return
        time.sleep(0.02)
    raise AssertionError("condition not reached")


def test_the_orchestrators_clients_against_a_real_server(tmp_path: Path) -> None:
    pytest.importorskip("uvicorn")
    key_file = tmp_path / "key"
    key_file.write_text(KEY)
    port = free_port()
    outcome: list[BaseException] = []

    def serve() -> None:
        try:
            run_server(
                host="127.0.0.1", port=port, deadline="4s", key_file=key_file, key_env=None, recipe="fake", tools=["fake"],
                data_dir=tmp_path / "data", warm=True, grace_seconds=2.0,
            )
        except BaseException as error:  # noqa: BLE001 - reported to the test thread
            outcome.append(error)

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    endpoint = Endpoint(f"http://127.0.0.1:{port}", KEY, timeout=10.0, retries=0)
    client = ToolServerClient(endpoint)
    client.sleep = lambda _: time.sleep(0.05)
    wait_until(lambda: _answers(client))
    wait_until(lambda: client.health()["models"]["generator"] == "ready")

    caps = client.capabilities()
    profile = caps["generator"]
    capabilities = GeneratorCapabilities(
        frozenset(profile["roles"]), int(profile["max_images"]), bool(profile["native_mask"]), bool(profile["text_only"])
    )
    generator = ToolServerGenerator(client, ModelRef(profile["model"], profile["revision"]), capabilities, profile["licence"])
    pixels = room(48, 64, 120)
    pixels[10:30, 10:30] = (200, 0, 0)
    original, mask = png(pixels), mask_png(48, 64, slice(8, 32), slice(8, 32))
    blobs = {sha256_bytes(original): original, sha256_bytes(mask): mask}
    request = GeneratorRequest(
        "empty the room",
        (RoleImage("original", sha256_bytes(original)), RoleImage("removal_mask", sha256_bytes(mask))),
        (("num_inference_steps", 5),),
        11,
    )
    data, gpu_seconds = generator.generate(request, lambda sha: blobs[sha])
    assert imaging.decode(data).width > 0 and gpu_seconds >= 0
    assert capabilities.text_only
    from_text, _ = generator.generate(GeneratorRequest("an empty room", (), (("output_aspect", 2.0),), 5), lambda sha: blobs[sha])
    wide = imaging.decode(from_text)
    assert wide.width / wide.height == pytest.approx(2.0, rel=0.05)

    tools = RemoteTools(client)
    assert tools.version("change_map")
    result = tools.run("segment_elements", [sha256_bytes(original)], {"labels": ["red square"]}, lambda sha: blobs[sha])
    assert result.measures["found"]["red square"] == pytest.approx(400 / (48 * 64), abs=1e-4)
    assert set(result.outputs) == {"mask", "mask_0"} and result.summary.startswith("found 1 of 1")
    with pytest.raises(EndpointError) as caught:
        tools.run("nope", [sha256_bytes(original)], {}, lambda sha: blobs[sha])
    assert caught.value.code == "tool_unknown"
    with pytest.raises(EndpointError) as unauthorised:
        ToolServerClient(Endpoint(f"http://127.0.0.1:{port}", "wrong-key-0123456789", retries=0)).capabilities()
    assert unauthorised.value.code == "unauthorized"

    wait_until(lambda: client.health()["status"] == "deadline_reached", 10.0)
    with pytest.raises(EndpointError) as late:
        client.capabilities()
    assert late.value.code == "deadline_reached"
    thread.join(timeout=15.0)
    assert not thread.is_alive(), "the server must exit after its deadline"
    assert not outcome


def _answers(client: ToolServerClient) -> bool:
    try:
        client.health()
    except EndpointError:
        return False
    return True


# --- the glue around torch, diffusers and transformers, run against stand-in modules --------------------------------


class StubTorch:
    """Just enough of torch for the adapter's own calls; records what it was asked for."""

    bfloat16 = "bfloat16-token"
    float8_e4m3fn = "float8-token"

    class cuda:  # noqa: N801 - mirrors torch.cuda
        @staticmethod
        def is_available() -> bool:
            return False

    @staticmethod
    def no_grad() -> Any:
        import contextlib

        return contextlib.nullcontext()

    class Generator:
        def __init__(self, device: str = "cpu") -> None:
            self.device, self.seed = device, None

        def manual_seed(self, seed: int) -> StubTorch.Generator:
            self.seed = seed
            return self


def stub_diffusers(record: dict[str, Any], fail_on_call: bool = False) -> Any:
    import types

    class Transformer:
        def enable_layerwise_casting(self, storage_dtype: Any, compute_dtype: Any) -> None:
            record.setdefault("fp8", []).append((storage_dtype, compute_dtype))

    class Scheduler:
        def __init__(self, config: dict[str, Any]) -> None:
            self.config = config

        @classmethod
        def from_config(cls, config: dict[str, Any]) -> Any:
            record["scheduler"] = dict(config)
            return cls(config)

    class Pipeline:
        transformer = Transformer()
        scheduler = Scheduler({"shift": 3.0, "shift_terminal": 0.02, "use_dynamic_shifting": False})

        def load_lora_weights(self, repository: str, **kwargs: Any) -> None:
            record.setdefault("lora", []).append(("load", repository, kwargs))

        def fuse_lora(self, lora_scale: float) -> None:
            record.setdefault("lora", []).append(("fuse", lora_scale))

        def unload_lora_weights(self) -> None:
            record.setdefault("lora", []).append(("unload",))

        @classmethod
        def from_pretrained(cls, repository: str, **kwargs: Any) -> Pipeline:
            record["loaded"] = (repository, kwargs)
            return cls()

        def to(self, device: str) -> Pipeline:
            record["device"] = device
            return self

        def enable_model_cpu_offload(self) -> None:
            record["offload"] = True

        def __call__(self, **kwargs: Any) -> Any:
            if fail_on_call:
                raise RuntimeError("CUDA out of memory")
            record["call"] = kwargs
            return types.SimpleNamespace(images=[Image.new("RGB", (kwargs["width"], kwargs["height"]), (9, 9, 9))])

    module = types.ModuleType("diffusers")
    for name in ("QwenImageEditPlusPipeline", "Flux2Pipeline", "Flux2KleinPipeline", "QwenImage21Pipeline", "BriaFibo2Pipeline"):
        setattr(module, name, type(name, (Pipeline,), {}))
    return module


def test_the_diffusers_adapter_loads_once_and_calls_the_pipeline(monkeypatch: pytest.MonkeyPatch) -> None:
    from virtual_unstaging.serve.generation import DiffusersGenerator

    record: dict[str, Any] = {}
    monkeypatch.setitem(sys.modules, "torch", StubTorch)
    monkeypatch.setitem(sys.modules, "diffusers", stub_diffusers(record))
    recipe, the_job = job("qwen_image_edit_2511", ["original", "removal_mask", "reference"])
    generator = DiffusersGenerator(recipe)
    assert generator.state() == "not_loaded" and generator.profile()["recipe"] == "qwen_image_edit_2511"
    result = generator.generate(the_job)
    assert generator.state() == "ready"
    repository, kwargs = record["loaded"]
    assert repository == "Qwen/Qwen-Image-Edit-2511" and kwargs == {"revision": recipe.revision, "dtype": "bfloat16-token"}
    assert record["offload"] is True and "device" not in record
    assert record["fp8"] == [("float8-token", "bfloat16-token")]  # the transformer stored in FP8, computed in bfloat16
    assert generator.profile()["revision"] == f"{recipe.revision}+fp8:transformer"
    call = record["call"]
    assert call["generator"].seed == 42 and call["generator"].device == "cuda"
    assert call["prompt"] == "a prompt" and len(call["image"]) == 3 and call["num_inference_steps"] == 40
    assert (result.width, result.height) == (1152, 864) and imaging.decode(result.png).size == (1152, 864)
    record.clear()
    generator.generate(the_job)
    assert "loaded" not in record  # resident: no second load


def test_the_adapter_reports_peak_memory_and_reloads_after_unload(monkeypatch: pytest.MonkeyPatch) -> None:
    from virtual_unstaging.serve.generation import DiffusersGenerator

    class CudaTorch(StubTorch):
        class cuda:  # noqa: N801 - mirrors torch.cuda
            @staticmethod
            def is_available() -> bool:
                return True

            @staticmethod
            def reset_peak_memory_stats() -> None:
                return None

            @staticmethod
            def max_memory_allocated() -> int:
                return 12_345_000_000

            @staticmethod
            def empty_cache() -> None:
                return None

            @staticmethod
            def synchronize() -> None:
                return None

    record: dict[str, Any] = {}
    monkeypatch.setitem(sys.modules, "torch", CudaTorch)
    monkeypatch.setitem(sys.modules, "diffusers", stub_diffusers(record))
    recipe, the_job = job("flux2_klein_4b", ["original", "reference"])
    generator = DiffusersGenerator(recipe)
    result = generator.generate(the_job)
    assert result.peak_gpu_gb == 12.35 and generator.profile()["peak_gpu_gb"] == 12.35
    generator.unload()
    assert generator.state() == "not_loaded" and "peak_gpu_gb" not in generator.profile()
    record.clear()
    generator.generate(the_job)
    assert "loaded" in record  # released, so loaded again on the next call


def test_a_distillation_lora_and_its_scheduler_are_applied_before_fp8_storage(monkeypatch: pytest.MonkeyPatch) -> None:
    from virtual_unstaging.serve.generation import DiffusersGenerator

    record: dict[str, Any] = {}
    monkeypatch.setitem(sys.modules, "torch", StubTorch)
    monkeypatch.setitem(sys.modules, "diffusers", stub_diffusers(record))
    recipe, the_job = job("qwen_image_edit_2511_lightning", ["original", "reference"])
    generator = DiffusersGenerator(recipe)
    generator.generate(the_job)
    assert record["scheduler"]["shift_terminal"] is None and record["scheduler"]["use_dynamic_shifting"] is True
    assert record["scheduler"]["base_shift"] == pytest.approx(1.0986, abs=1e-4)
    load, fuse, unload = record["lora"]
    assert load[1] == "lightx2v/Qwen-Image-Edit-2511-Lightning" and load[2]["weight_name"].endswith("4steps-V1.0-bf16.safetensors")
    assert fuse == ("fuse", 1.0) and unload == ("unload",) and record["fp8"]
    assert record["call"]["num_inference_steps"] == 4 and record["call"]["true_cfg_scale"] == 1.0
    revision = generator.profile()["revision"]
    assert revision.startswith(recipe.revision + "+lora:") and "+scheduler:" in revision and revision.endswith("+fp8:transformer")


def test_a_recipe_lora_and_scheduler_are_checked() -> None:
    text = (Path(__file__).parent.parent / "src/virtual_unstaging/serve/recipes/qwen_image_edit_2511_lightning.toml").read_text()
    assert parse_recipe(text).lora is not None
    for broken in (text.replace('weight_name = "Qwen', 'weight_name = "../Qwen'),
                   text.replace('revision = "107d238d68b8387e32843d0b4a2e24ceb0d3ad86"', 'revision = "main"'),
                   text.replace("[pipeline.lora]", "[pipeline.lora]\nextra = 1"),
                   text.replace('scheduler_none = ["shift_terminal"]', 'scheduler_none = ["os.system"]')):
        with pytest.raises(ServeConfigError):
            parse_recipe(broken)


def test_the_adapter_offloads_when_the_recipe_says_so(monkeypatch: pytest.MonkeyPatch) -> None:
    from virtual_unstaging.serve.generation import DiffusersGenerator

    record: dict[str, Any] = {}
    monkeypatch.setitem(sys.modules, "torch", StubTorch)
    monkeypatch.setitem(sys.modules, "diffusers", stub_diffusers(record))
    recipe, the_job = job("flux2_dev", ["original", "reference"])
    DiffusersGenerator(recipe).generate(the_job)
    assert record["offload"] is True and "device" not in record and "fp8" not in record
    record.clear()
    recipe, the_job = job("fibo_2_0_dev_edit", ["original"])
    DiffusersGenerator(recipe).generate(the_job)
    assert record["device"] == "cuda" and "offload" not in record
    assert DiffusersGenerator(recipe).profile()["revision"] == recipe.revision  # no FP8: the plain commit


def test_adapter_failures_carry_stable_codes(monkeypatch: pytest.MonkeyPatch) -> None:
    from virtual_unstaging.serve.generation import DiffusersGenerator

    record: dict[str, Any] = {}
    monkeypatch.setitem(sys.modules, "torch", StubTorch)
    monkeypatch.setitem(sys.modules, "diffusers", stub_diffusers(record, fail_on_call=True))
    recipe, the_job = job("qwen_image_2_1", ["original"])
    with pytest.raises(ApiError) as failed:
        DiffusersGenerator(recipe).generate(the_job)
    assert failed.value.code == "generator_failed" and "out of memory" in failed.value.message
    monkeypatch.setitem(sys.modules, "diffusers", None)  # an import that fails
    broken = DiffusersGenerator(recipe)
    with pytest.raises(ApiError) as unavailable:
        broken.generate(the_job)
    assert unavailable.value.code == "generator_unavailable" and broken.state() == "failed"


def test_the_segmentation_glue_against_stand_in_models(monkeypatch: pytest.MonkeyPatch) -> None:
    import types

    from virtual_unstaging.serve.tools.segment import GroundedSam2Backend

    class Array:  # a tensor as the adapter uses it: indexing, sigmoid, float, cpu, numpy, tolist
        def __init__(self, values: Any) -> None:
            self.values = np.asarray(values)

        def __getitem__(self, index: Any) -> Array:
            return Array(self.values[index])

        def sigmoid(self) -> Array:
            return self  # the stand-in holds probabilities already

        def float(self) -> Array:
            return self

        def cpu(self) -> Array:
            return self

        def numpy(self) -> np.ndarray:
            return self.values

        def tolist(self) -> Any:
            return self.values.tolist()

    class Tokenizer:  # "[CLS] a . b . [SEP]": CLS 1, SEP 2, "." 9, then one token per label
        cls_token_id, sep_token_id = 1, 2

        def convert_tokens_to_ids(self, token: str) -> int:
            return 9

    class Batch(dict[str, Any]):  # transformers' BatchEncoding is a mapping too
        def __init__(self, input_ids: list[int] | None = None) -> None:
            super().__init__(original_sizes=np.array([[48, 64]]))
            self.input_ids = Array([input_ids or []])

        def to(self, _: str) -> Batch:
            return self

    def centre(box: list[float]) -> list[float]:  # absolute [x0, y0, x1, y1] to the detector's (cx, cy, w, h) in [0, 1]
        x0, y0, x1, y1 = box
        return [(x0 + x1) / 2 / 64, (y0 + y1) / 2 / 48, (x1 - x0) / 64, (y1 - y0) / 48]

    detections = {  # what the detector says per pass: (label position in the pass, box, score)
        0: [(0, [2, 2, 12, 12], 0.9), (1, [30, 5, 40, 15], 0.8)],
        1: [(0, [0, 0, 3, 3], 0.3)],  # under the threshold
    }
    passes: list[list[str]] = []

    class DetectorProcessor:
        tokenizer = Tokenizer()

        def __call__(self, images: Any, text: list[list[str]], return_tensors: str) -> Batch:
            passes.append(text[0])
            ids = [1]
            for i, _ in enumerate(text[0]):
                ids += [10 + i, 9]
            return Batch(ids + [2])

    class Detector:
        def __call__(self, **_: Any) -> Any:
            found = detections[len(passes) - 1]
            tokens = 2 + 2 * len(passes[-1])
            logits = np.zeros((len(found), tokens), dtype=np.float32)
            for query, (label, _, score) in enumerate(found):
                logits[query, 1 + 2 * label] = score
            return types.SimpleNamespace(logits=Array([logits]), pred_boxes=Array([[centre(f[1]) for f in found]]))

    class SegmenterProcessor:
        def __call__(self, images: Any, input_boxes: list[list[list[float]]], return_tensors: str) -> Batch:
            self.boxes = input_boxes[0]
            return Batch()

        def post_process_masks(self, masks: Any, sizes: Any) -> list[np.ndarray]:
            per_box = np.zeros((len(self.boxes), 1, 48, 64), dtype=bool)
            for i, (x0, y0, x1, y1) in enumerate(self.boxes):
                per_box[i, 0, int(y0) : int(y1), int(x0) : int(x1)] = i != 1  # the second box's mask comes back empty
            return [per_box]

    class Model:
        def __init__(self, broken: bool = False) -> None:
            self.broken = broken

        def __call__(self, **_: Any) -> Any:
            if self.broken:
                raise RuntimeError("sam failed")
            return types.SimpleNamespace(pred_masks=types.SimpleNamespace(cpu=lambda: None))

    monkeypatch.setitem(sys.modules, "torch", StubTorch)
    backend = GroundedSam2Backend()
    backend.labels_per_pass = 3
    backend._loaded = True
    backend._detector, backend._detector_processor = Detector(), DetectorProcessor()
    backend._segmenter, backend._segmenter_processor = Model(), SegmenterProcessor()
    image = Image.new("RGB", (64, 48))
    result = backend.segment(image, ["chair", "table", "lamp", "Rug"], 0.4)
    assert passes == [["chair", "table", "lamp"], ["rug"]]
    assert result.detections == [1, 1, 0, 0] and not result.fell_back_to_boxes
    assert int(result.masks[0].sum()) == 100 and int(result.masks[1].sum()) == 0  # SAM's mask rules, even when empty
    backend._segmenter = Model(broken=True)
    passes.clear()
    fallback = backend.segment(image, ["chair", "table", "lamp", "Rug"], 0.4)
    assert fallback.fell_back_to_boxes and int(fallback.masks[1].sum()) == 100 and int(fallback.masks[0].sum()) == 100


# --- asynchronous jobs (`Prefer: respond-async`) -----------------------------------------------------------------------

ASYNC = {"Prefer": "respond-async"}


def poll(client: TestClient, job_id: str, until: str, seconds: float = 5.0) -> dict[str, Any]:
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        body: dict[str, Any] = client.get(f"/jobs/{job_id}").json()
        if body["status"] == until:
            return body
        time.sleep(0.01)
    raise AssertionError(f"job never reached {until}: {body}")


def test_the_preference_header_is_read_as_a_token_list() -> None:
    from virtual_unstaging.serve.jobs import wants_async

    for yes in ("respond-async", "RESPOND-ASYNC", "wait=5, respond-async", "respond-async; x=1", " return=minimal ,respond-async"):
        assert wants_async(yes), yes
    for no in (None, "", "return=minimal", "respond-async-not", "wait=5"):
        assert not wants_async(no), no


def test_a_generate_job_runs_to_done_with_the_synchronous_body(client: TestClient) -> None:
    original = put(client, png(room()))
    mask = put(client, mask_png(48, 64, slice(8, 32), slice(8, 32)))
    body = generate_body(original, mask)
    sync = client.post("/generate", json=body)
    assert sync.status_code == 200
    accepted = client.post("/generate", json=body, headers=ASYNC)
    assert accepted.status_code == 202 and accepted.headers["preference-applied"] == "respond-async"
    job_id = accepted.json()["job"]
    assert accepted.json()["status"] == "queued" and accepted.headers["location"] == f"/jobs/{job_id}"
    done = poll(client, job_id, "done")
    assert set(done) == {"job", "status", "result"} and done["job"] == job_id
    assert done["result"]["output_sha256"] == sync.json()["output_sha256"]  # same seed, same bytes
    assert set(done["result"]) == set(sync.json())
    assert client.get(f"/jobs/{job_id}").json() == done  # still there on the next poll


def test_a_job_is_queued_while_the_gpu_is_busy_then_running_then_done(client: TestClient) -> None:
    state = client.app.state.server  # type: ignore[attr-defined]
    tool = state.tools["change_map"]
    entered, release = threading.Event(), threading.Event()
    real_run = tool.run

    def slow(*args: Any, **kwargs: Any) -> Any:
        entered.set()
        assert release.wait(5.0)
        return real_run(*args, **kwargs)

    tool.run = slow
    image = put(client, png(room(32, 32)))
    region = put(client, mask_png(32, 32, slice(0, 4), slice(0, 4)))
    inputs = {"inputs": [image, image, region], "params": {}}
    state.lock.acquire()  # the GPU is taken by someone else
    try:
        job_id = client.post("/tools/change_map", json=inputs, headers=ASYNC).json()["job"]
        time.sleep(0.1)
        assert client.get(f"/jobs/{job_id}").json() == {"job": job_id, "status": "queued"}
        assert client.get("/health").json()["jobs"] == 1
    finally:
        state.lock.release()
    assert entered.wait(5.0)
    assert client.get(f"/jobs/{job_id}").json() == {"job": job_id, "status": "running"}
    release.set()
    done = poll(client, job_id, "done")
    assert done["result"]["tool"] == "change_map" and done["result"]["measures"]["displacement_median_pct"] == 0.0
    assert client.get("/health").json()["jobs"] == 0


def test_a_failed_job_carries_the_tools_error_code(client: TestClient) -> None:
    tool = client.app.state.server.tools["change_map"]  # type: ignore[attr-defined]

    def boom(*_: Any, **__: Any) -> Any:
        raise RuntimeError("out of memory")

    tool.run = boom
    image = put(client, png(room(32, 32)))
    job_id = client.post("/tools/change_map", json={"inputs": [image] * 3, "params": {}}, headers=ASYNC).json()["job"]
    failed = poll(client, job_id, "failed")
    assert set(failed) == {"job", "status", "error"}
    assert failed["error"]["code"] == "tool_failed" and "out of memory" in failed["error"]["message"]

    def refuse(*_: Any, **__: Any) -> Any:
        raise ApiError("bad_request", "this input cannot be segmented")

    tool.run = refuse
    job_id = client.post("/tools/change_map", json={"inputs": [image] * 3, "params": {}}, headers=ASYNC).json()["job"]
    assert poll(client, job_id, "failed")["error"] == {"code": "bad_request", "message": "this input cannot be segmented"}


def test_an_unexpected_error_in_a_job_still_gets_a_stable_code() -> None:
    from virtual_unstaging.serve.jobs import JobBoard

    board = JobBoard()

    def explode(started: Any) -> dict[str, Any]:
        started()
        raise KeyError("surprise")

    job_id = board.submit(explode, "generator_failed")
    end = time.monotonic() + 5
    while board.get(job_id)["status"] != "failed" and time.monotonic() < end:
        time.sleep(0.01)
    assert board.get(job_id)["error"]["code"] == "generator_failed"


def test_unknown_and_malformed_job_ids_are_not_found(client: TestClient) -> None:
    for job_id in ("0" * 32, "nope", "A" * 32, "0" * 33, "%2e%2e%2fhealth"):
        response = client.get(f"/jobs/{job_id}")
        assert response.status_code == 404 and error_code(response) == "not_found", job_id
    assert TestClient(client.app).get(f"/jobs/{'0' * 32}").status_code == 401  # the key is needed to poll


def test_invalid_requests_are_refused_at_once_even_when_asking_for_a_job(client: TestClient) -> None:
    original = put(client, png(room()))
    missing = sha256_bytes(b"missing")
    response = client.post("/generate", json=generate_body(original, missing), headers=ASYNC)
    assert response.status_code == 404 and error_code(response) == "blob_missing"
    response = client.post("/tools/segment_elements", json={"inputs": [original], "params": {"labels": []}}, headers=ASYNC)
    assert response.status_code == 400 and error_code(response) == "bad_request"
    response = client.post("/tools/nope", json={"inputs": [original], "params": {}}, headers=ASYNC)
    assert response.status_code == 404 and error_code(response) == "tool_unknown"
    assert client.get("/health").json()["jobs"] == 0


def test_finished_jobs_are_forgotten_after_an_hour() -> None:
    from virtual_unstaging.serve.jobs import KEEP_SECONDS, JobBoard

    now = [1000.0]
    board = JobBoard(clock=lambda: now[0])
    job_id = board.submit(lambda started: {"ok": True}, "tool_failed")
    end = time.monotonic() + 5
    while board.get(job_id)["status"] != "done" and time.monotonic() < end:
        time.sleep(0.01)
    now[0] += KEEP_SECONDS - 1
    assert board.get(job_id)["result"] == {"ok": True}
    now[0] += 2
    with pytest.raises(ApiError) as gone:
        board.get(job_id)
    assert gone.value.code == "not_found"


def test_after_the_deadline_submitting_is_refused_but_polling_works(client: TestClient, clock: FakeClock) -> None:
    original = put(client, png(room()))
    job_id = client.post("/generate", json=generate_body(original), headers=ASYNC).json()["job"]
    poll(client, job_id, "done")
    clock.advance(hours=2)
    late = client.post("/generate", json=generate_body(original), headers=ASYNC)
    assert late.status_code == 503 and error_code(late) == "deadline_reached"
    assert client.get(f"/jobs/{job_id}").json()["status"] == "done"
    assert client.get("/capabilities").status_code == 503


def test_a_job_that_waited_for_the_gpu_past_the_deadline_fails_with_deadline_reached(client: TestClient, clock: FakeClock) -> None:
    state = client.app.state.server  # type: ignore[attr-defined]
    original = put(client, png(room()))
    state.lock.acquire()
    try:
        job_id = client.post("/generate", json=generate_body(original), headers=ASYNC).json()["job"]
        clock.advance(hours=2)
    finally:
        state.lock.release()
    assert poll(client, job_id, "failed")["error"]["code"] == "deadline_reached"


def test_a_job_in_flight_holds_the_deadline_watch_back(tmp_path: Path, clock: FakeClock) -> None:
    state = make_app(tmp_path, clock).state.server
    release = threading.Event()
    state.jobs.submit(lambda started: (release.wait(5.0), {})[1], "tool_failed")
    time.sleep(0.05)
    assert state.in_flight == 1
    clock.advance(hours=2)
    done = threading.Event()
    thread = threading.Thread(target=watch_deadline, args=(state, threading.Event(), done.set, 5.0, 0.01))
    thread.start()
    assert not done.wait(0.2)
    release.set()
    assert done.wait(2.0)
    thread.join(2.0)


# --- the orchestrator's client over a real socket, async path ---------------------------------------------------------


class RunningServer:
    """The app under uvicorn in a thread, on a free port."""

    def __init__(self, app: Any) -> None:
        import uvicorn

        self.port = free_port()
        self.server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=self.port, log_level="warning"))
        self.thread = threading.Thread(target=self.server.run, daemon=True)

    def __enter__(self) -> RunningServer:
        self.thread.start()
        wait_until(lambda: self.server.started)
        return self

    def __exit__(self, *_: object) -> None:
        self.server.should_exit = True
        self.thread.join(5.0)

    def client(self) -> ToolServerClient:
        """A client whose waits between polls are recorded (in `sleeps`) and shortened."""
        client = ToolServerClient(Endpoint(f"http://127.0.0.1:{self.port}", KEY, timeout=10.0, retries=0))
        self.sleeps: list[float] = []

        def wait(seconds: float) -> None:
            self.sleeps.append(seconds)
            time.sleep(0.02)

        client.sleep = wait
        return client


def test_the_client_polls_a_slow_job_until_it_is_done(tmp_path: Path) -> None:
    pytest.importorskip("uvicorn")
    app = make_app(tmp_path)
    tool = app.state.server.tools["change_map"]
    real_run = tool.run
    seen: list[str] = []

    def slow(*args: Any, **kwargs: Any) -> Any:
        time.sleep(0.3)
        return real_run(*args, **kwargs)

    tool.run = slow
    with RunningServer(app) as running:
        client = running.client()
        data = png(room(32, 32))
        sha = client.ensure_blob(data, "image/png")
        region = client.ensure_blob(mask_png(32, 32, slice(0, 4), slice(0, 4)), "image/png")
        original_await = client._await_job
        client._await_job = lambda job_id: (seen.append(job_id), original_await(job_id))[1]  # type: ignore[method-assign]
        reply = client.run_tool("change_map", [sha, sha, region], {})
        assert seen and reply["tool"] == "change_map" and reply["measures"]["delta_e_median"] == 0.0
        assert running.sleeps, "a 0.3 s job needs at least one wait between polls"
        generated = client.generate(generate_body(sha))
        assert generated["media_type"] == "image/png" and len(client.get_blob(generated["output_sha256"])) > 0


def test_the_client_raises_the_jobs_error_code(tmp_path: Path) -> None:
    pytest.importorskip("uvicorn")
    app = make_app(tmp_path)

    def boom(*_: Any, **__: Any) -> Any:
        raise RuntimeError("out of memory")

    app.state.server.tools["change_map"].run = boom
    with RunningServer(app) as running:
        client = running.client()
        sha = client.ensure_blob(png(room(32, 32)), "image/png")
        with pytest.raises(EndpointError) as caught:
            client.run_tool("change_map", [sha, sha, sha], {})
        assert caught.value.code == "tool_failed" and "out of memory" in str(caught.value)
        with pytest.raises(EndpointError) as refused:  # refused at submission: no job at all
            client.run_tool("change_map", [sha], {})
        assert refused.value.code == "bad_request"


def test_the_client_still_works_against_a_server_that_ignores_the_preference() -> None:
    import http.server
    import json as jsonlib

    class Old(http.server.BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            self.rfile.read(int(self.headers["Content-Length"]))
            Old.preferred = self.headers.get("Prefer")  # type: ignore[attr-defined]
            body = jsonlib.dumps({"output_sha256": "a" * 64, "gpu_seconds": 1.5}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_: Any) -> None:
            return None

    server = http.server.HTTPServer(("127.0.0.1", 0), Old)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        client = ToolServerClient(Endpoint(f"http://127.0.0.1:{server.server_address[1]}", KEY, timeout=5.0, retries=0))
        client._checked = True
        reply = client.generate({"prompt": "x"})
        assert reply["output_sha256"] == "a" * 64 and Old.preferred == "respond-async"  # type: ignore[attr-defined]
    finally:
        server.shutdown()
        thread.join(2.0)


def test_the_clients_polling_backs_off_from_two_to_five_seconds(monkeypatch: pytest.MonkeyPatch) -> None:
    import json as jsonlib

    from virtual_unstaging.clients import toolserver

    job_id = "ab" * 16
    answers = [{"job": job_id, "status": "queued"}] * 2 + [{"job": job_id, "status": "running"}] * 4
    answers.append({"job": job_id, "status": "done", "result": {"ok": 1}})
    polled: list[str] = []

    def fake_request(endpoint: Any, method: str, path: str, *_: Any, **__: Any) -> tuple[int, bytes, str]:
        polled.append(path)
        return 200, jsonlib.dumps(answers.pop(0)).encode(), "application/json"

    monkeypatch.setattr(toolserver, "request", fake_request)
    client = ToolServerClient(Endpoint("http://127.0.0.1:1", KEY, retries=0))
    waits: list[float] = []
    client.sleep = waits.append
    assert client._await_job(job_id) == {"ok": 1}
    assert waits == [2.0, 2.5, 3.125, 3.90625, 4.8828125, 5.0] and set(polled) == {f"/jobs/{job_id}"}
    for bad in ({"job": job_id, "status": "weird"}, {"job": job_id, "status": "done", "result": "x"}):
        answers[:] = [bad]
        with pytest.raises(EndpointError) as caught:
            client._await_job(job_id)
        assert caught.value.code == "bad_response"
    monkeypatch.setattr(toolserver, "request", lambda *_, **__: (202, b'{"job": "../x"}', "application/json"))
    with pytest.raises(EndpointError, match="malformed"):
        client._submit("/generate", {})
