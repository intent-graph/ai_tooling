"""OpenAI-compatible endpoints: chat completions with images and a JSON schema; image edits (multipart)."""

from __future__ import annotations

import base64
import json
import uuid

from virtual_unstaging.clients.http import Endpoint, EndpointError, request


def image_part(data: bytes, media_type: str) -> dict[str, object]:
    url = f"data:{media_type};base64,{base64.b64encode(data).decode('ascii')}"
    return {"type": "image_url", "image_url": {"url": url}}


def text_part(text: str) -> dict[str, object]:
    return {"type": "text", "text": text}


def chat_json(
    endpoint: Endpoint,
    model: str,
    messages: list[dict[str, object]],
    schema: dict[str, object],
    temperature: float,
    max_tokens: int,
    extra: dict[str, object] | None = None,
) -> str:
    """One chat completion constrained to `schema`; returns the message content as received.

    Streamed, so bytes keep flowing while the model thinks: rental proxies cut a request that stays silent for
    about 100 seconds. Reasoning text streamed apart from the content (vLLM's reasoning parser) is not returned.
    """
    payload: dict[str, object] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_schema", "json_schema": {"name": "judgment", "schema": schema, "strict": True}},
        "stream": True,
        **(extra or {}),
    }
    _, body, content_type = request(
        endpoint, "POST", "/chat/completions", json.dumps(payload).encode("utf-8"), "application/json",
        accept="text/event-stream, application/json",
    )
    if "text/event-stream" not in content_type:  # a server that ignored `stream`
        try:
            content = json.loads(body)["choices"][0]["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError):
            raise EndpointError("bad_response", f"no message content in {body[:300]!r}") from None
        if not isinstance(content, str):
            raise EndpointError("bad_response", "message content is not text")
        return content
    return _content_from_events(body)


def _content_from_events(body: bytes) -> str:
    """Join the `delta.content` pieces of a server-sent event stream, up to `data: [DONE]`."""
    pieces: list[str] = []
    for line in body.decode("utf-8").splitlines():
        if not line.startswith("data:"):
            continue
        data = line[5:].strip()
        if data == "[DONE]":
            return "".join(pieces)
        try:
            event = json.loads(data)
        except ValueError:
            raise EndpointError("bad_response", f"unreadable stream event {data[:120]!r}") from None
        if "error" in event:
            raise EndpointError("judge_error", str(event["error"])[:300])
        for choice in event.get("choices", []):
            piece = (choice.get("delta") or {}).get("content")
            if isinstance(piece, str):
                pieces.append(piece)
    raise EndpointError("bad_response", "the stream ended without [DONE]")


def image_edit(
    endpoint: Endpoint,
    model: str,
    prompt: str,
    images: list[tuple[bytes, str]],
    mask: tuple[bytes, str] | None,
    fields: dict[str, str],
) -> bytes:
    """POST /images/edits as multipart form: repeated `image` fields, optional `mask`; returns the PNG bytes."""
    boundary = uuid.uuid4().hex
    parts: list[bytes] = []

    def field(name: str, value: str) -> None:
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode())

    def file(name: str, data: bytes, media_type: str, index: int) -> None:
        head = (
            f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"; filename="{name}{index}.png"\r\n'
            f"Content-Type: {media_type}\r\n\r\n"
        )
        parts.append(head.encode() + data + b"\r\n")

    field("model", model)
    field("prompt", prompt)
    field("response_format", "b64_json")
    for name, value in fields.items():
        field(name, value)
    for index, (data, media_type) in enumerate(images):
        file("image", data, media_type, index)
    if mask is not None:
        file("mask", mask[0], mask[1], 0)
    body = b"".join(parts) + f"--{boundary}--\r\n".encode()
    _, data, _ = request(endpoint, "POST", "/images/edits", body, f"multipart/form-data; boundary={boundary}")
    try:
        encoded = json.loads(data)["data"][0]["b64_json"]
        return base64.b64decode(encoded)
    except (ValueError, KeyError, IndexError, TypeError):
        raise EndpointError("bad_response", "no image in the edit response") from None
