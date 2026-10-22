"""Clients against a local HTTP server: the judge's chat is streamed (and tolerates a server that does not stream);
an endpoint's observer sees every exchange; generator adapters and the fake generator from text alone."""

from __future__ import annotations

import io
import json
import threading
from collections.abc import Iterator
from dataclasses import replace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest
from PIL import Image

from virtual_unstaging.clients.fakes import FAKE_CAPABILITIES, FakeGenerator
from virtual_unstaging.clients.generators import OpenAIImageEditGenerator
from virtual_unstaging.clients.http import Endpoint, EndpointError, Exchange
from virtual_unstaging.clients.openai_compatible import chat_json
from virtual_unstaging.domain import GeneratorRequest, ModelRef

ANSWER = '{"evaluation": {"findings": [], "verdict": "accept", "critique": "clean"}, "guidance": {"moves": []}}'


class Handler(BaseHTTPRequestHandler):
    mode = "stream"
    received: dict[str, object] = {}

    def do_POST(self) -> None:  # noqa: N802 (http.server's naming)
        length = int(self.headers["Content-Length"])
        Handler.received = json.loads(self.rfile.read(length))
        Handler.received["_auth"] = self.headers.get("Authorization")
        if Handler.mode == "plain":
            body = json.dumps({"choices": [{"message": {"content": ANSWER}}]}).encode()
            self._send(body, "application/json")
            return
        events = [{"choices": [{"delta": {"reasoning_content": "looking at the region"}}]}]
        events += [{"choices": [{"delta": {"content": ANSWER[i : i + 20]}}]} for i in range(0, len(ANSWER), 20)]
        lines = [f"data: {json.dumps(e)}\n\n" for e in events]
        if Handler.mode == "stream":
            lines.append("data: [DONE]\n\n")
        self._send("".join(lines).encode(), "text/event-stream")

    def _send(self, body: bytes, content_type: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args: object) -> None:
        pass


@pytest.fixture
def server() -> Iterator[Endpoint]:
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    yield Endpoint(f"http://127.0.0.1:{httpd.server_address[1]}/v1", "session-key", timeout=10, retries=0)
    httpd.shutdown()


def test_chat_is_streamed_and_reasoning_is_left_out(server: Endpoint) -> None:
    Handler.mode = "stream"
    content = chat_json(server, "judge", [{"role": "user", "content": "hi"}], {"type": "object"}, 0.0, 512)
    assert content == ANSWER
    assert Handler.received["stream"] is True and Handler.received["_auth"] == "Bearer session-key"


def test_a_server_that_ignores_streaming_still_works(server: Endpoint) -> None:
    Handler.mode = "plain"
    assert chat_json(server, "judge", [], {"type": "object"}, 0.0, 512) == ANSWER


def test_a_truncated_stream_is_an_error(server: Endpoint) -> None:
    Handler.mode = "truncated"
    with pytest.raises(EndpointError) as caught:
        chat_json(server, "judge", [], {"type": "object"}, 0.0, 512)
    assert caught.value.code == "bad_response"


def test_an_observer_sees_each_exchange_as_sent_without_the_key(server: Endpoint) -> None:
    Handler.mode = "stream"
    seen: list[Exchange] = []
    chat_json(replace(server, observer=seen.append), "judge", [{"role": "user", "content": "hi"}], {"type": "object"}, 0.0, 512)
    assert len(seen) == 1
    exchange = seen[0]
    assert exchange.method == "POST" and exchange.url.endswith("/v1/chat/completions") and exchange.status == 200
    assert json.loads(exchange.body or b"") == {key: value for key, value in Handler.received.items() if key != "_auth"}
    assert "Authorization" not in exchange.headers and b"[DONE]" in exchange.response and exchange.error is None


def test_an_observer_sees_a_failed_attempt() -> None:
    seen: list[Exchange] = []
    unreachable = Endpoint("http://127.0.0.1:9/v1", "session-key", timeout=2, retries=0, observer=seen.append)
    with pytest.raises(EndpointError):
        chat_json(unreachable, "judge", [], {"type": "object"}, 0.0, 512)
    assert [(exchange.status, exchange.error) for exchange in seen] == [(None, "endpoint_unreachable")]


TEXT_ONLY =GeneratorRequest("an empty room", (), (("output_side", 64), ("output_aspect", 2.0)), 9)


def test_the_fake_generator_makes_an_image_from_text_alone() -> None:
    generator = FakeGenerator()
    data, _ = generator.generate(TEXT_ONLY, lambda sha: b"")
    image = Image.open(io.BytesIO(data))
    assert FAKE_CAPABILITIES.text_only and image.width / image.height == pytest.approx(2.0, rel=0.05)
    assert generator.generate(TEXT_ONLY, lambda sha: b"")[0] == data  # set by prompt and seed


def test_an_image_edits_endpoint_refuses_a_request_without_image() -> None:
    editor = OpenAIImageEditGenerator(Endpoint("http://127.0.0.1:9/v1", "session-key", retries=0), ModelRef("m", "1"),
                                      FAKE_CAPABILITIES, "none")
    with pytest.raises(EndpointError) as caught:
        editor.generate(TEXT_ONLY, lambda sha: b"")
    assert caught.value.code == "bad_request"
