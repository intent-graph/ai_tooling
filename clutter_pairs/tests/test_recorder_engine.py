"""P8's unit: a stored body rebuilds to the bytes sent; the engine's policy and its replay."""

from __future__ import annotations

import base64
import json

import pytest
from virtual_unstaging.clients.http import Exchange
from virtual_unstaging.domain import sha256_bytes
from virtual_unstaging.engines import ReplayMismatch, replay

from clutter_pairs.domain import Action, Halt, Outcome, Score
from clutter_pairs.engine import LoopProblem, Reviser
from clutter_pairs.recorder import Recorder, hashed_images, rebuild_text, to_record

PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")


def test_a_text_body_rebuilds_byte_for_byte() -> None:
    body = json.dumps({"messages": [{"content": [{"type": "image_url", "image_url": {
        "url": "data:image/png;base64," + base64.b64encode(PNG).decode()}}]}]}).encode()
    record = to_record(Exchange("POST", "http://x/v1/chat/completions", {"Content-Type": "application/json"}, body,
                                200, b"{}", "application/json", 0.1, None, 0))
    assert record.body_text is not None and "base64" not in record.body_text
    assert hashed_images(record.body_text) == [sha256_bytes(PNG)]
    assert sha256_bytes(rebuild_text(record.body_text, record.images)) == record.wire_sha


def test_an_exchange_outside_a_call_fails_it() -> None:
    recorder = Recorder()
    with pytest.raises(RuntimeError, match="outside a recorded call"):
        recorder.observe(Exchange("GET", "http://x/", {}, None, 200, b"", "", 0.0, None, 0))


def _outcome(blocking: int, pixel: bool = False) -> Outcome:
    return Outcome(Score(blocking, 0), blocking == 0, pixel)


def test_the_policy_writes_reseeds_after_a_pixel_failure_then_revises() -> None:
    engine = Reviser()
    engine.start(LoopProblem(6))
    assert engine.ask() == Action("write")
    engine.tell(Action("write"), _outcome(1, pixel=True))
    assert engine.ask() == Action("reseed")
    engine.tell(Action("reseed"), _outcome(1, pixel=True))
    assert engine.ask() == Action("revise")
    engine.tell(Action("revise"), _outcome(0))
    assert engine.ask() == Halt("accepted")


def test_the_policy_stops_without_progress_and_at_the_limit() -> None:
    engine = Reviser()
    engine.start(LoopProblem(10))
    for action in ("write", "revise", "revise"):
        assert engine.ask() == Action(action)  # type: ignore[arg-type]
        engine.tell(Action(action), _outcome(2))  # type: ignore[arg-type]
    assert engine.ask() == Halt("no_progress")
    engine = Reviser()
    engine.start(LoopProblem(1))
    engine.tell(Action("write"), _outcome(1))
    assert engine.ask() == Halt("max_iterations")


def test_replay_checks_the_engine_asks_what_is_stored() -> None:
    history = [(Action("write"), _outcome(1)), (Action("revise"), _outcome(1))]
    engine = Reviser()
    engine.start(LoopProblem(6))
    replay(engine, history, lambda h: h[0], lambda h: h[1])
    engine = Reviser()
    engine.start(LoopProblem(6))
    with pytest.raises(ReplayMismatch):
        replay(engine, [(Action("reseed"), _outcome(1))], lambda h: h[0], lambda h: h[1])
