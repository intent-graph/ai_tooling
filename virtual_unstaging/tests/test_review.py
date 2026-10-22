"""The review page: security at the edge, typed reviews, blind preferences, human deliveries, images by hash."""

from __future__ import annotations

import hashlib
import http.client
import json
import re
import shutil
import socketserver
import sqlite3
import threading
from collections.abc import Iterator
from contextlib import closing
from pathlib import Path
from typing import Any

import pytest
from PIL import Image, ImageDraw

from virtual_unstaging.cli import main
from virtual_unstaging.review import server as review_server
from virtual_unstaging.review.server import ReviewServer, start_review_server
from virtual_unstaging.review.service import shown_left_for
from virtual_unstaging.store import review_queries
from virtual_unstaging.store.blobs import BlobStore
from virtual_unstaging.store.db import connect

REVIEWER = "tester"
SHA256 = re.compile(r"^[0-9a-f]{64}$")


# --- a project built with the command line and its stand-in models ----------------------------------------------


def _draw(photos: Path, masks: Path) -> None:
    photos.mkdir(parents=True)
    masks.mkdir(parents=True)
    for index in range(3):
        image = Image.new("RGB", (320, 240), (200, 190, 170))  # the wall
        draw = ImageDraw.Draw(image)
        draw.rectangle([0, 150, 320, 240], fill=(120, 90, 60))  # the floor
        x = 70 + 30 * index
        draw.rectangle([x, 100, x + 80, 200], fill=(40, 30, 30))  # the dark box
        image.save(photos / f"photo_{index:03d}.jpg", quality=92)
        mask = Image.new("L", (320, 240), 0)
        ImageDraw.Draw(mask).rectangle([x - 3, 97, x + 83, 203], fill=255)
        mask.save(masks / f"photo_{index:03d}.png")


@pytest.fixture(scope="module")
def template(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Three photos, run 1 with the `single` engine and run 2 with the `guided` engine, built once."""
    root = tmp_path_factory.mktemp("review_template")
    _draw(root / "photos" / "living_room", root / "masks")
    (root / "rules.toml").write_text('[all]\nfixed = ["window"]\nmovable = ["wardrobe"]\n', encoding="utf-8")
    project = root / "project"
    assert main(["--project", str(project), "init"]) == 0
    text = (project / "project.toml").read_text(encoding="utf-8")
    text = text.replace('adapter = "toolserver"', 'adapter = "fake"').replace('adapter = "openai_chat"', 'adapter = "fake"')
    (project / "project.toml").write_text(text, encoding="utf-8")
    for argv in (
        ["import", str(root / "photos")],
        ["rules", str(root / "rules.toml")],
        ["masks", str(root / "masks")],
        ["run", "--engine", "single"],
        ["run", "--engine", "guided"],
    ):
        assert main(["--project", str(project), *argv]) == 0
    return project


@pytest.fixture
def project(template: Path, tmp_path: Path) -> Path:
    """A private copy of the template, so a test can write to it."""
    target = tmp_path / "project"
    shutil.copytree(template, target)
    return target


class Client:
    """Raw HTTP to the server under test, with control over every header a browser would send."""

    def __init__(self, server: ReviewServer) -> None:
        self.server = server
        self.port = server.port

    def call(
        self, method: str, path: str, *, host: str | None = None, headers: dict[str, str] | None = None,
        body: Any = None, raw: bytes | None = None, token: str | None = "header", origin: bool = True,
    ) -> tuple[int, http.client.HTTPMessage, bytes]:
        sent = dict(headers or {})
        if token == "header":
            sent.setdefault("X-Review-Token", self.server.token)
        elif token == "query":
            path += ("&" if "?" in path else "?") + "token=" + self.server.token
        data = raw if raw is not None else (None if body is None else json.dumps(body).encode())
        if method == "POST":
            sent.setdefault("Content-Type", "application/json")
            if origin:
                sent.setdefault("Origin", f"http://127.0.0.1:{self.port}")
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
        try:
            connection.putrequest(method, path, skip_host=True, skip_accept_encoding=True)
            connection.putheader("Host", f"127.0.0.1:{self.port}" if host is None else host)
            for name, value in sent.items():
                connection.putheader(name, value)
            if data is not None:
                connection.putheader("Content-Length", str(len(data)))
            connection.endheaders(data)
            response = connection.getresponse()
            return response.status, response.msg, response.read()
        finally:
            connection.close()

    def get(self, path: str, **kwargs: Any) -> tuple[int, Any]:
        status, _, payload = self.call("GET", path, **kwargs)
        return status, json.loads(payload)

    def post(self, path: str, body: Any, **kwargs: Any) -> tuple[int, Any]:
        status, _, payload = self.call("POST", path, body=body, **kwargs)
        return status, json.loads(payload)


@pytest.fixture
def served(project: Path) -> Iterator[Client]:
    server = start_review_server(project / "project.sqlite", BlobStore(project / "blobs"), 0, REVIEWER)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield Client(server)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def rows(project: Path, sql: str, params: tuple[object, ...] = ()) -> list[tuple[Any, ...]]:
    with closing(sqlite3.connect(project / "project.sqlite")) as conn:
        return [tuple(r) for r in conn.execute(sql, params).fetchall()]


def best_attempt(project: Path, run_id: int, photo_id: int) -> int:
    return int(rows(project, "SELECT best_attempt_id FROM optimization WHERE run_id = ? AND photo_id = ?", (run_id, photo_id))[0][0])


# --- security of a local page -----------------------------------------------------------------------------------


def test_server_binds_the_loopback_address_only(served: Client) -> None:
    assert served.server.server_address[0] == "127.0.0.1"


def test_page_loads_with_the_token_and_is_self_contained(served: Client) -> None:
    status, headers, body = served.call("GET", "/", token="query")
    html = body.decode()
    assert status == 200 and headers["Content-Type"].startswith("text/html")
    assert "__NONCE__" not in html and "Review results" in html
    nonce = re.search(r'<script nonce="([^"]+)"', html)
    assert nonce is not None and f"'nonce-{nonce.group(1)}'" in headers["Content-Security-Policy"]
    assert "img-src 'self'" in headers["Content-Security-Policy"] and "default-src 'none'" in headers["Content-Security-Policy"]
    assert headers["Referrer-Policy"] == "no-referrer" and headers["X-Frame-Options"] == "DENY"
    assert not re.search(r"https?://|//cdn", html), "the page must work offline: no external address"


def test_requests_without_a_valid_token_are_refused(served: Client) -> None:
    assert served.get("/", token=None)[1]["error"]["code"] == "missing_token"
    assert served.call("GET", "/", token=None)[0] == 403
    status, payload = served.get("/api/meta", headers={"X-Review-Token": "wrong"}, token=None)
    assert (status, payload["error"]["code"]) == (403, "bad_token")
    assert served.get("/api/meta?token=wrong", token=None)[1]["error"]["code"] == "bad_token"
    assert served.get("/api/meta", token="header")[0] == 200


def test_a_wrong_host_is_refused_everywhere(served: Client) -> None:
    port = served.port
    for host in (f"evil.example:{port}", "127.0.0.1", f"127.0.0.1:{port + 1}", f"127.0.0.1.evil.example:{port}", ""):
        for path in ("/", "/api/meta", "/image/" + "0" * 64):
            status, payload = served.get(path, host=host, token="query")
            assert (status, payload["error"]["code"]) == (403, "bad_host"), (host, path)
    status, _, _ = served.call("POST", "/api/review", host=f"evil.example:{port}", body={})
    assert status == 403
    assert served.call("GET", "/api/meta", host=f"localhost:{port}")[0] == 200


def test_a_write_needs_the_token_and_the_same_origin(served: Client, project: Path) -> None:
    attempt = best_attempt(project, 1, 1)
    body = {"attempt_id": attempt, "verdict": "usable"}
    cases = [
        ({"token": None}, "missing_token"),  # no token at all
        ({"token": "query"}, "missing_token"),  # the token in the URL does not authorize a write
        ({"origin": False}, "cross_origin"),  # no Origin and no Sec-Fetch-Site: no proof of origin
        ({"headers": {"Origin": "http://evil.example"}}, "cross_origin"),
        ({"headers": {"Origin": f"http://127.0.0.1:{served.port + 1}"}}, "cross_origin"),
        ({"headers": {"Sec-Fetch-Site": "cross-site"}}, "cross_origin"),
        ({"headers": {"Sec-Fetch-Site": "same-site"}}, "cross_origin"),
        ({"headers": {"X-Review-Token": "wrong"}, "token": None}, "bad_token"),
    ]
    for kwargs, code in cases:
        status, payload = served.post("/api/review", body, **kwargs)
        assert (status, payload["error"]["code"]) == (403, code), kwargs
    assert rows(project, "SELECT COUNT(*) FROM review") == [(0,)]
    status, _ = served.post("/api/review", body, origin=False, headers={"Sec-Fetch-Site": "same-origin"})
    assert status == 201  # Fetch Metadata alone is accepted proof of origin
    status, _ = served.post("/api/review", body)
    assert status == 201  # so is an Origin equal to the page's origin


def test_bodies_are_parsed_strictly(served: Client, project: Path) -> None:
    attempt = best_attempt(project, 1, 1)
    good = {"attempt_id": attempt, "verdict": "usable"}
    box = {"x0": 0.1, "y0": 0.1, "x1": 0.4, "y1": 0.5}
    finding = {"defect_code": "movable_left", "severity": "minor", "box": box}
    refused: list[tuple[Any, int, str]] = [
        ({**good, "extra": 1}, 400, "invalid_body"),
        ({"verdict": "usable"}, 400, "invalid_body"),
        ({**good, "verdict": "fine"}, 400, "invalid_body"),
        ({**good, "attempt_id": True}, 400, "invalid_body"),
        ({**good, "attempt_id": "1"}, 400, "invalid_body"),
        ({**good, "attempt_id": 0}, 400, "invalid_body"),
        ({**good, "attempt_id": 10**6}, 404, "unknown_attempt"),
        ({**good, "comment": "x" * 2001}, 400, "invalid_body"),
        ({**good, "comment": "bell\x07"}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "defect_code": "made_up"}]}, 400, "unknown_defect"),
        ({**good, "findings": [{**finding, "defect_code": "x'; DROP TABLE review; --"}]}, 400, "unknown_defect"),
        ({**good, "findings": [{**finding, "severity": "major"}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": {**box, "x1": 1.2}}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": {**box, "x0": -0.1}}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": {**box, "x0": 0.5, "x1": 0.5}}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": {**box, "y0": 0.6}}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": {**box, "x0": "0.1"}}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": {"x0": 0.1, "y0": 0.1, "x1": 0.4}}]}, 400, "invalid_body"),
        ({**good, "findings": [{**finding, "box": [0.1, 0.1, 0.4, 0.5]}]}, 400, "invalid_body"),
        ({**good, "findings": "none"}, 400, "invalid_body"),
        ({**good, "findings": [finding] * 51}, 400, "invalid_body"),
    ]
    for body, status, code in refused:
        got_status, payload = served.post("/api/review", body)
        assert (got_status, payload["error"]["code"]) == (status, code), body
    raw_cases = [
        (b"[1]", 400, "invalid_json"),
        (b"not json", 400, "invalid_json"),
        (b'{"attempt_id": 1, "attempt_id": 2, "verdict": "usable"}', 400, "invalid_json"),
        (b'{"attempt_id": NaN, "verdict": "usable"}', 400, "invalid_json"),
        (b'{"attempt_id": 1, "verdict": "usable", "comment": "\xff"}', 400, "invalid_json"),
        (b"[" * 20_000 + b"]" * 20_000, 400, "invalid_json"),
        (b" " * (64 * 1024 + 1), 413, "payload_too_large"),
    ]
    for raw, status, code in raw_cases:
        got_status, payload = served.post("/api/review", None, raw=raw)
        assert (got_status, payload["error"]["code"]) == (status, code), raw[:30]
    status, payload = served.post("/api/review", good, headers={"Content-Type": "text/plain"})
    assert (status, payload["error"]["code"]) == (415, "unsupported_media_type")
    assert rows(project, "SELECT COUNT(*) FROM review") == [(0,)]
    assert rows(project, "SELECT COUNT(*) FROM finding WHERE review_id IS NOT NULL") == [(0,)]


def test_queries_are_parsed_strictly(served: Client) -> None:
    for path, code in (
        ("/api/review/queue", "invalid_query"),
        ("/api/review/queue?run=abc", "invalid_query"),
        ("/api/review/queue?run=1&run=2", "invalid_query"),
        ("/api/review/queue?run=999", "unknown_run"),
        ("/api/compare?run_a=1&run_b=1", "invalid_query"),
        ("/api/compare?run_a=1&run_b=999", "unknown_run"),
        ("/api/attempt/999999", "unknown_attempt"),
        ("/api/nothing", "not_found"),
    ):
        status, payload = served.get(path)
        assert payload["error"]["code"] == code and status >= 400, path


# --- typed review -----------------------------------------------------------------------------------------------


def test_review_view_shows_the_judges_findings_and_the_outline(served: Client, project: Path) -> None:
    status, queue = served.get("/api/review/queue?run=2")
    assert status == 200 and queue["total"] == 3 and queue["left"] == 3
    item = queue["items"][0]
    assert item["attempt_id"] == best_attempt(project, 2, item["photo_id"])
    status, view = served.get(f"/api/attempt/{item['attempt_id']}")
    assert status == 200 and view["name"] == item["name"] and view["group"] == "living_room"
    outline = rows(
        project,
        "SELECT o.image_sha256 FROM judgment j JOIN judgment_tool_run jt USING (judgment_id) JOIN tool_run t USING (tool_run_id) "
        "JOIN tool_run_output o USING (tool_run_id) WHERE j.attempt_id = ? AND t.tool = 'outline' AND o.name = 'image'",
        (item["attempt_id"],),
    )
    assert view["region"] == {"kind": "outline", "image": outline[0][0]}
    stored = rows(project, "SELECT COUNT(*) FROM finding f JOIN judgment j USING (judgment_id) WHERE j.attempt_id = ?", (item["attempt_id"],))
    assert len(view["judge"]["findings"]) == stored[0][0]
    for finding in view["judge"]["findings"]:
        assert finding["box"] is None or 0 <= finding["box"]["x0"] < finding["box"]["x1"] <= 1
    assert view["mine"] is None


def test_removal_mask_stands_in_when_no_outline_was_stored(served: Client, project: Path) -> None:
    attempt = best_attempt(project, 1, 1)
    with closing(connect(project / "project.sqlite")) as conn:
        conn.execute("DELETE FROM judgment_tool_run WHERE tool_run_id IN (SELECT tool_run_id FROM tool_run WHERE tool = 'outline')")
    mask = rows(project, "SELECT o.image_sha256 FROM eligibility e JOIN tool_run_output o ON o.tool_run_id = e.removal_mask_tool_run_id WHERE e.photo_id = 1")
    _, view = served.get(f"/api/attempt/{attempt}")
    assert view["region"] == {"kind": "removal_mask", "image": mask[0][0]}


def test_a_review_with_findings_is_recorded_typed(served: Client, project: Path) -> None:
    attempt = best_attempt(project, 2, 1)
    box = {"x0": 0.25, "y0": 0.5, "x1": 0.5, "y1": 0.75}
    body = {
        "attempt_id": attempt, "verdict": "unusable", "comment": "  a door appeared  ",
        "findings": [
            {"defect_code": "opening_invented", "severity": "blocking", "box": box, "comment": "wall became a door"},
            {"defect_code": "colour_shift", "severity": "minor", "box": None, "comment": ""},
        ],
    }
    status, saved = served.post("/api/review", body)
    assert status == 201 and saved["findings"] == 2
    assert rows(project, "SELECT review_id, attempt_id, reviewer, verdict, comment FROM review") == [
        (saved["review_id"], attempt, REVIEWER, "unusable", "a door appeared")
    ]
    assert rows(project, "SELECT defect_code, severity, x0, y0, x1, y1, comment, judgment_id FROM finding WHERE review_id = ? ORDER BY finding_id", (saved["review_id"],)) == [
        ("opening_invented", "blocking", 0.25, 0.5, 0.5, 0.75, "wall became a door", None),
        ("colour_shift", "minor", None, None, None, None, None, None),
    ]
    _, queue = served.get("/api/review/queue?run=2")
    assert queue["left"] == 2 and [i["my_verdict"] for i in queue["items"]].count("unusable") == 1
    _, view = served.get(f"/api/attempt/{attempt}")
    assert view["mine"]["verdict"] == "unusable" and len(view["mine"]["findings"]) == 2
    assert view["mine"]["findings"][0]["box"] == box
    _, meta = served.get("/api/meta")
    assert {r["run_id"]: r["reviewed"] for r in meta["runs"]} == {1: 0, 2: 1}


def test_a_later_review_replaces_the_earlier_in_the_rule_for_delivery(served: Client, project: Path) -> None:
    attempt = best_attempt(project, 2, 1)
    assert served.post("/api/review", {"attempt_id": attempt, "verdict": "unusable"})[0] == 201
    assert served.post("/api/review", {"attempt_id": attempt, "verdict": "usable"})[0] == 201
    assert rows(project, "SELECT verdict FROM review ORDER BY review_id") == [("unusable",), ("usable",)]
    _, queue = served.get("/api/review/queue?run=2")
    assert [i["my_verdict"] for i in queue["items"] if i["attempt_id"] == attempt] == ["usable"]


# --- blind comparison -------------------------------------------------------------------------------------------


def test_blind_comparison_hides_the_engines_and_fixes_the_sides(served: Client, project: Path) -> None:
    status, first = served.get("/api/compare?run_a=1&run_b=2")
    assert status == 200 and first["total"] == 3 and first["left"] == 3
    names = {"photo_id", "name", "original", "attempt_a", "attempt_b", "shown_left", "left", "right"}
    for item in first["items"]:
        assert set(item) == names
        a_sha, b_sha = (rows(project, "SELECT output_sha256 FROM attempt WHERE attempt_id = ?", (item[k],))[0][0] for k in ("attempt_a", "attempt_b"))
        assert (item["left"], item["right"]) == ((a_sha, b_sha) if item["shown_left"] == item["attempt_a"] else (b_sha, a_sha))
        assert item["attempt_a"] == best_attempt(project, 1, item["photo_id"])
        assert item["attempt_b"] == best_attempt(project, 2, item["photo_id"])
    text = json.dumps(first)
    assert "engine" not in text and "single" not in text and "guided" not in text and "run" not in text
    _, again = served.get("/api/compare?run_a=1&run_b=2")
    assert [i["shown_left"] for i in again["items"]] == [i["shown_left"] for i in first["items"]]


def test_the_side_is_pseudo_random_but_fixed_per_reviewer_photo_and_pair() -> None:
    sides = {shown_left_for("tester", photo, 10, 20) for photo in range(1, 200)}
    assert sides == {10, 20}
    assert shown_left_for("tester", 5, 10, 20) == shown_left_for("tester", 5, 20, 10) == shown_left_for("tester", 5, 10, 20)
    assert {shown_left_for(name, 5, 10, 20) for name in ("a", "b", "c", "d", "e", "f", "g", "h")} == {10, 20}


def test_a_preference_is_recorded_with_the_side_shown(served: Client, project: Path) -> None:
    _, view = served.get("/api/compare?run_a=1&run_b=2")
    item = view["items"][0]
    body = {k: item[k] for k in ("attempt_a", "attempt_b", "shown_left")} | {"choice": "b"}
    status, saved = served.post("/api/preference", body)
    assert status == 201
    assert rows(project, "SELECT preference_id, reviewer, attempt_a, attempt_b, shown_left, choice FROM preference") == [
        (saved["preference_id"], REVIEWER, item["attempt_a"], item["attempt_b"], item["shown_left"], "b")
    ]
    _, after = served.get("/api/compare?run_a=1&run_b=2")
    assert after["left"] == 2 and after["total"] == 3
    assert item["photo_id"] not in [i["photo_id"] for i in after["items"]]
    _, swapped = served.get("/api/compare?run_a=2&run_b=1")
    assert swapped["left"] == 2  # the pair is the same whichever run is named first
    status, payload = served.post("/api/preference", body)
    assert (status, payload["error"]["code"]) == (409, "already_compared")
    with closing(connect(project / "project.sqlite")) as conn:
        assert [r.compared for r in review_queries.comparison_pairs(conn, 1, 2, "someone else")].count(True) == 0
        assert [r.compared for r in review_queries.comparison_pairs(conn, 1, 2, REVIEWER)].count(True) == 1


def test_a_preference_is_refused_when_it_does_not_match_what_was_shown(served: Client, project: Path) -> None:
    _, view = served.get("/api/compare?run_a=1&run_b=2")
    item = view["items"][0]
    flipped = item["attempt_a"] if item["shown_left"] == item["attempt_b"] else item["attempt_b"]
    base = {k: item[k] for k in ("attempt_a", "attempt_b", "shown_left")} | {"choice": "a"}
    other_photo = next(i for i in view["items"] if i["photo_id"] != item["photo_id"])
    cases = [
        ({**base, "shown_left": flipped}, 400, "shown_left_mismatch"),
        ({**base, "shown_left": 12345}, 400, "invalid_body"),
        ({**base, "attempt_b": item["attempt_a"]}, 400, "invalid_body"),
        ({**base, "attempt_b": other_photo["attempt_b"]}, 400, "invalid_body"),
        ({**base, "attempt_b": 10**6, "shown_left": item["attempt_a"]}, 404, "unknown_attempt"),
        ({**base, "choice": "left"}, 400, "invalid_body"),
        ({**base, "extra": 1}, 400, "invalid_body"),
    ]
    for body, status, code in cases:
        got_status, payload = served.post("/api/preference", body)
        assert (got_status, payload["error"]["code"]) == (status, code), body
    assert rows(project, "SELECT COUNT(*) FROM preference") == [(0,)]
    for photo, choice in zip(view["items"], ("a", "equal", "both_unusable"), strict=True):
        body = {k: photo[k] for k in ("attempt_a", "attempt_b", "shown_left")} | {"choice": choice}
        assert served.post("/api/preference", body)[0] == 201
    assert sorted(r[0] for r in rows(project, "SELECT choice FROM preference")) == ["a", "both_unusable", "equal"]


def test_pairs_whose_best_images_are_identical_are_not_shown(served: Client, project: Path) -> None:
    photo = 1
    run_one, run_two = best_attempt(project, 1, photo), best_attempt(project, 2, photo)
    same = rows(project, "SELECT output_sha256 FROM attempt WHERE attempt_id = ?", (run_one,))[0][0]
    with closing(connect(project / "project.sqlite")) as conn:
        conn.execute("UPDATE attempt SET output_sha256 = ? WHERE attempt_id = ?", (same, run_two))
    _, view = served.get("/api/compare?run_a=1&run_b=2")
    assert view["total"] == 2 and photo not in [i["photo_id"] for i in view["items"]]


# --- delivery ---------------------------------------------------------------------------------------------------


def test_a_human_delivery_is_recorded_and_the_rule_never_overrides_it(served: Client, project: Path) -> None:
    _, before = served.get("/api/delivery")
    assert before["total"] == 3 and before["left"] == 3
    assert all(item["decision"] is None and item["candidates"] for item in before["items"])
    attempt = best_attempt(project, 1, 1)
    status, saved = served.post("/api/delivery", {"photo_id": 1, "outcome": "emptied", "attempt_id": attempt, "reason": " looks right "})
    assert status == 201 and saved["decided_by"] == f"human:{REVIEWER}"
    assert rows(project, "SELECT photo_id, outcome, attempt_id, decided_by, reason FROM delivery") == [
        (1, "emptied", attempt, f"human:{REVIEWER}", "looks right")
    ]
    assert main(["--project", str(project), "deliver", "--run", "2"]) == 0
    assert rows(project, "SELECT photo_id, outcome, attempt_id, decided_by FROM delivery WHERE photo_id = 1") == [
        (1, "emptied", attempt, f"human:{REVIEWER}")
    ]
    assert rows(project, "SELECT COUNT(*) FROM delivery WHERE decided_by = 'rule:best_accepted'") == [(2,)]
    _, after = served.get("/api/delivery")
    assert after["left"] == 2 and after["decided_by_me"] == 1
    assert after["items"][0]["decision"]["decided_by"] == f"human:{REVIEWER}"
    assert served.post("/api/delivery", {"photo_id": 1, "outcome": "excluded", "reason": "glare"})[0] == 201
    assert served.post("/api/delivery", {"photo_id": 2, "outcome": "original"})[0] == 201
    assert rows(project, "SELECT photo_id, outcome, attempt_id, decided_by FROM delivery WHERE photo_id IN (1, 2) ORDER BY photo_id") == [
        (1, "excluded", None, f"human:{REVIEWER}"), (2, "original", None, f"human:{REVIEWER}")
    ]


def test_a_delivery_is_refused_unless_it_is_consistent(served: Client, project: Path) -> None:
    mine, other_photo = best_attempt(project, 1, 1), best_attempt(project, 1, 2)
    cases = [
        ({"photo_id": 1, "outcome": "emptied"}, 400, "invalid_body"),
        ({"photo_id": 1, "outcome": "original", "attempt_id": mine}, 400, "invalid_body"),
        ({"photo_id": 1, "outcome": "emptied", "attempt_id": other_photo}, 400, "invalid_body"),
        ({"photo_id": 1, "outcome": "emptied", "attempt_id": 10**6}, 404, "unknown_attempt"),
        ({"photo_id": 99, "outcome": "original"}, 404, "unknown_photo"),
        ({"photo_id": 1, "outcome": "deleted"}, 400, "invalid_body"),
        ({"photo_id": "1", "outcome": "original"}, 400, "invalid_body"),
        ({"photo_id": 1, "outcome": "original", "decided_by": "rule:best_accepted"}, 400, "invalid_body"),
    ]
    for body, status, code in cases:
        got_status, payload = served.post("/api/delivery", body)
        assert (got_status, payload["error"]["code"]) == (status, code), body
    assert rows(project, "SELECT COUNT(*) FROM delivery") == [(0,)]


# --- images, by hash only ---------------------------------------------------------------------------------------


def test_images_are_served_by_validated_hash_with_the_media_type_of_the_table(served: Client, project: Path) -> None:
    _, queue = served.get("/api/review/queue?run=1")
    for sha in (queue["items"][0]["original"], queue["items"][0]["candidate"]):
        status, headers, data = served.call("GET", f"/image/{sha}", token="query")
        assert status == 200 and hashlib.sha256(data).hexdigest() == sha
        assert headers["Content-Type"] == "image/png" and headers["X-Content-Type-Options"] == "nosniff"
    sha = queue["items"][0]["original"]
    with closing(connect(project / "project.sqlite")) as conn:
        conn.execute("UPDATE image SET media_type = 'image/jpeg' WHERE sha256 = ?", (sha,))
    assert served.call("GET", f"/image/{sha}")[1]["Content-Type"] == "image/jpeg"


def test_image_paths_that_are_not_a_hash_in_the_table_are_refused(served: Client, project: Path) -> None:
    blobs = BlobStore(project / "blobs")
    orphan = blobs.put(b"\x89PNG not registered in the image table")  # in the store, not in the table
    secret = Path(project / "secret.txt")
    secret.write_text("outside the store", encoding="utf-8")
    paths = [
        f"/image/{orphan}", "/image/" + "0" * 64, "/image/" + "A" * 64, "/image/" + "a" * 63, "/image/" + "a" * 65,
        "/image/../project.toml", "/image/..%2fproject.toml", "/image/%2e%2e/%2e%2e/secret.txt", "/image/",
        "/image", "//image/" + "0" * 64, "/image/" + "0" * 64 + "/extra", f"/image/{orphan[:2]}/{orphan}",
        "/blobs/" + orphan, "/project.sqlite", "/project.toml", "/secret.txt",
    ]
    for path in paths:
        status, _, data = served.call("GET", path)
        assert status == 404, path
        assert json.loads(data)["error"]["code"] == "not_found"
    assert served.call("GET", f"/image/{orphan}")[0] == 404


def test_a_blob_that_does_not_match_its_hash_is_not_served(served: Client, project: Path) -> None:
    _, queue = served.get("/api/review/queue?run=1")
    sha = queue["items"][0]["candidate"]
    BlobStore(project / "blobs").path(sha).write_bytes(b"tampered")
    status, payload = served.get(f"/image/{sha}")
    assert (status, payload["error"]["code"]) == (500, "blob_corrupted")


# --- entry points -----------------------------------------------------------------------------------------------


def test_serve_review_prints_the_tokened_url_and_stops_on_interrupt(
    project: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    seen: dict[str, Any] = {}

    def serve_one_request(self: ReviewServer, poll_interval: float = 0.5) -> None:
        url = capsys.readouterr().out.strip()
        thread = threading.Thread(target=socketserver.BaseServer.serve_forever, args=(self,), daemon=True)
        thread.start()
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
        connection.request("GET", url.removeprefix(f"http://127.0.0.1:{self.port}"), headers={"Host": f"127.0.0.1:{self.port}"})
        seen["status"] = connection.getresponse().status
        seen["url"] = url
        self.shutdown()
        thread.join(timeout=5)
        raise KeyboardInterrupt

    monkeypatch.setattr(ReviewServer, "serve_forever", serve_one_request)
    review_server.serve_review(project / "project.sqlite", BlobStore(project / "blobs"), 0, REVIEWER)
    assert seen["status"] == 200
    assert re.fullmatch(r"http://127\.0\.0\.1:\d+/\?token=[A-Za-z0-9_-]{32,}", seen["url"])


def test_the_review_command_passes_its_arguments_to_the_server(project: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[Path, BlobStore, int, str]] = []
    monkeypatch.setattr(review_server, "serve_review", lambda *args: calls.append(args))
    assert main(["--project", str(project), "review", "--port", "4321", "--reviewer", "Remi"]) == 0
    [(db_path, blobs, port, reviewer)] = calls
    assert (db_path, blobs.root, port, reviewer) == (project / "project.sqlite", project / "blobs", 4321, "Remi")


def test_a_reviewer_name_that_cannot_be_stored_safely_is_refused(project: Path) -> None:
    for name in ("", "human:x\n", "a" * 65, "semi;colon", "x'--"):
        with pytest.raises(ValueError, match="invalid_reviewer"):
            start_review_server(project / "project.sqlite", BlobStore(project / "blobs"), 0, name)
