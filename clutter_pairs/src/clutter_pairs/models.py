"""The model callers: a canonical request in, an answer out, through virtual_unstaging's clients.

A chat request goes to `chat_json` (streamed, JSON-schema answer, sampling seed through `extra`); a generator
request to the tool server's `/generate` through `ToolServerGenerator`. Images travel by hash in the canonical
request; the caller fetches their bytes from the image store. Every exchange reaches the endpoint's observer.
"""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass, replace
from typing import Any, Protocol

from virtual_unstaging.clients.generators import ToolServerGenerator
from virtual_unstaging.clients.http import Endpoint, Exchange
from virtual_unstaging.clients.openai_compatible import chat_json, image_part, text_part
from virtual_unstaging.clients.toolserver import ToolServerClient
from virtual_unstaging.domain import (
    GeneratorCapabilities,
    GeneratorRequest,
    ModelRef,
    RoleImage,
    canonical_json,
    sha256_bytes,
)

from clutter_pairs.domain import ModelId

Fetch = Callable[[str], bytes]
Observer = Callable[[Exchange], None]


@dataclass(frozen=True)
class Answer:
    text: str  # the answer as used: chat content, or the generation result as canonical JSON
    image: bytes | None
    gpu_seconds: float | None
    wall_seconds: float


class Caller(Protocol):
    model: ModelId

    def call(self, request: dict[str, Any], fetch: Fetch) -> Answer: ...


class ChatCaller:
    """An OpenAI-compatible chat server: judge, writer, reviser and distiller in slice 1."""

    def __init__(self, endpoint: Endpoint, model: ModelId) -> None:
        self.endpoint = endpoint
        self.model = model

    def call(self, request: dict[str, Any], fetch: Fetch) -> Answer:
        messages: list[dict[str, object]] = []
        for message in request["messages"]:
            content: list[dict[str, object]] = []
            for item in message["content"]:
                if item["type"] == "image":
                    content.append(image_part(fetch(item["sha256"]), "image/png"))
                else:
                    content.append(text_part(item["text"]))
            messages.append({"role": message["role"], "content": content})
        started = time.monotonic()
        text = chat_json(self.endpoint, self.model.name, messages, request["schema"],
                         float(request.get("temperature", 0.0)), int(request.get("max_tokens", 1024)),
                         extra={"seed": int(request["seed"])})
        return Answer(text, None, None, time.monotonic() - started)


class GeneratorCaller:
    """The tool server's generator: from text alone (clean images) or from an original (edits)."""

    def __init__(self, generator: ToolServerGenerator, model: ModelId) -> None:
        self.generator = generator
        self.model = model

    def call(self, request: dict[str, Any], fetch: Fetch) -> Answer:
        neutral = GeneratorRequest(
            prompt=str(request["prompt"]),
            images=tuple(RoleImage(im["role"], im["sha256"]) for im in request["images"]),
            settings=tuple(sorted(request["settings"].items())),
            seed=int(request["seed"]),
        )
        started = time.monotonic()
        data, gpu_seconds = self.generator.generate(neutral, fetch)
        wall = time.monotonic() - started
        result = canonical_json({"output_sha256": sha256_bytes(data), "gpu_seconds": round(gpu_seconds, 3)})
        return Answer(result, data, gpu_seconds, wall)


def chat_caller(base_url: str, key: str | None, model: ModelId, observer: Observer, retries: int = 3) -> ChatCaller:
    return ChatCaller(Endpoint(base_url, key, retries=retries, observer=observer), model)


def generator_caller(base_url: str, key: str | None, family: str, licence: str, observer: Observer,
                     retries: int = 3) -> GeneratorCaller:
    """Probe the tool server's capabilities (not a model call, not recorded), then observe every later exchange.
    The model's name and revision are the server's own report: the weights as run."""
    endpoint = Endpoint(base_url, key, retries=retries)
    client = ToolServerClient(endpoint)
    caps = client.capabilities().get("generator") or {}  # the server's profile of its generator
    if not caps.get("text_only"):
        raise ValueError(f"the generator {caps.get('model')} does not make images from text alone (recipe text_only)")
    ref = ModelRef(str(caps["model"]), str(caps["revision"]))
    capabilities = GeneratorCapabilities(frozenset(caps.get("roles", ["original"])), int(caps.get("max_images", 1)),
                                         bool(caps.get("native_mask", False)), bool(caps.get("text_only", False)))
    client.endpoint = replace(endpoint, observer=observer)
    generator = ToolServerGenerator(client, ref, capabilities, licence)
    return GeneratorCaller(generator, ModelId(ref.name, ref.revision, family, licence))
