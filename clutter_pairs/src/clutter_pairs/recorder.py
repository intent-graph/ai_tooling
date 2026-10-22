"""The endpoint observer: every HTTP exchange of a model call, kept as sent (P8).

virtual_unstaging's `Endpoint.observer` hands each attempt to `observe`; the exchanges are collected per call on the
calling thread, then stored with the call. A text body keeps its bytes with each data URL's base64 replaced by the
hash of the decoded image (`data:<type>;sha256,<hex>`), the image bytes going to the image store; an image body is
kept as an image; the hash of the bytes on the wire is kept, so the store can prove what was sent.
"""

from __future__ import annotations

import base64
import re
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from urllib.parse import urlparse

from virtual_unstaging.clients.http import Exchange
from virtual_unstaging.domain import sha256_bytes

from clutter_pairs.domain import ExchangeRecord

DATA_URL = re.compile(r"data:(image/(?:png|jpeg));base64,([A-Za-z0-9+/=]+)")
HASHED_URL = re.compile(r"data:(image/(?:png|jpeg));sha256,([0-9a-f]{64})")
IMAGE_TYPES = ("image/png", "image/jpeg")


def to_record(exchange: Exchange) -> ExchangeRecord:
    images: dict[str, bytes] = {}
    body_text, body_image, wire_sha = None, None, None
    if exchange.body is not None:
        wire_sha = sha256_bytes(exchange.body)
        request_type = next((v for k, v in exchange.headers.items() if k.lower() == "content-type"), "")
        if request_type.split(";")[0].strip() in IMAGE_TYPES:
            body_image = exchange.body
        else:
            body_text = hash_data_urls(_text(exchange.body, "request body"), images)
    response_text, response_image = None, None
    if exchange.response:
        if exchange.content_type.split(";")[0].strip() in IMAGE_TYPES:
            response_image = exchange.response
        else:
            response_text = _text(exchange.response, "response body")
    return ExchangeRecord(
        method=exchange.method, path=urlparse(exchange.url).path, attempt=exchange.attempt, status=exchange.status,
        body_text=body_text, body_image=body_image, wire_sha=wire_sha, response_text=response_text,
        response_image=response_image, content_type=exchange.content_type, seconds=exchange.seconds,
        error=exchange.error, images=images,
    )


def hash_data_urls(text: str, images: dict[str, bytes]) -> str:
    def replace(match: re.Match[str]) -> str:
        data = base64.b64decode(match.group(2), validate=True)
        sha = sha256_bytes(data)
        images[sha] = data
        return f"data:{match.group(1)};sha256,{sha}"

    return DATA_URL.sub(replace, text)


def rebuild_text(stored: str, image_bytes: dict[str, bytes]) -> bytes:
    """A stored text body as it went on the wire: each hashed data URL back to base64 of the stored bytes."""

    def replace(match: re.Match[str]) -> str:
        return f"data:{match.group(1)};base64,{base64.b64encode(image_bytes[match.group(2)]).decode('ascii')}"

    return HASHED_URL.sub(replace, stored).encode("utf-8")


def hashed_images(stored: str) -> list[str]:
    return [m.group(2) for m in HASHED_URL.finditer(stored)]


def _text(data: bytes, what: str) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError(f"the {what} is neither an image nor UTF-8 text: it cannot be stored as sent") from None


class Recorder:
    """Collects exchanges per call on the calling thread. An exchange outside a call fails it: nothing goes unrecorded."""

    def __init__(self) -> None:
        self._local = threading.local()

    def observe(self, exchange: Exchange) -> None:
        buffer: list[ExchangeRecord] | None = getattr(self._local, "buffer", None)
        if buffer is None:
            raise RuntimeError(f"an exchange outside a recorded call: {exchange.method} {exchange.url}")
        buffer.append(to_record(exchange))

    @contextmanager
    def call(self) -> Iterator[list[ExchangeRecord]]:
        if getattr(self._local, "buffer", None) is not None:
            raise RuntimeError("a recorded call is already open on this thread")
        buffer: list[ExchangeRecord] = []
        self._local.buffer = buffer
        try:
            yield buffer
        finally:
            self._local.buffer = None
