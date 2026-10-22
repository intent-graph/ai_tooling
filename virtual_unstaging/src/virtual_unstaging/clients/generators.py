"""Generator adapters on the orchestrator side: map a model-neutral request onto an endpoint protocol."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Protocol

from virtual_unstaging.clients.http import Endpoint, EndpointError
from virtual_unstaging.clients.openai_compatible import image_edit
from virtual_unstaging.clients.toolserver import ToolServerClient
from virtual_unstaging.domain import GeneratorCapabilities, GeneratorRequest, ModelRef

Fetch = Callable[[str], bytes]


class Generator(Protocol):
    model: ModelRef
    capabilities: GeneratorCapabilities
    licence: str

    def generate(self, request: GeneratorRequest, fetch: Fetch) -> tuple[bytes, float]:
        """Return the edited image's bytes and the GPU-seconds it took."""
        ...


class ToolServerGenerator:
    """The tool server's `/generate`: the server-side adapter maps roles to the model's pipeline."""

    def __init__(self, client: ToolServerClient, model: ModelRef, capabilities: GeneratorCapabilities, licence: str):
        self.client = client
        self.model = model
        self.capabilities = capabilities
        self.licence = licence

    def generate(self, request: GeneratorRequest, fetch: Fetch) -> tuple[bytes, float]:
        for image in request.images:
            self.client.ensure_blob(fetch(image.sha256), "image/png")
        reply = self.client.generate(request.payload())
        sha = reply.get("output_sha256")
        if not isinstance(sha, str):
            raise EndpointError("bad_response", "generate returned no output hash")
        return self.client.get_blob(sha), float(reply.get("gpu_seconds", 0.0))


class OpenAIImageEditGenerator:
    """An OpenAI-style `/images/edits` server (e.g. vLLM-Omni): images in role order, mask native or as an image."""

    def __init__(
        self,
        endpoint: Endpoint,
        model: ModelRef,
        capabilities: GeneratorCapabilities,
        licence: str,
        fields: dict[str, str] | None = None,
    ):
        self.endpoint = endpoint
        self.model = model
        self.capabilities = capabilities
        self.licence = licence
        self.fields = fields or {}

    def generate(self, request: GeneratorRequest, fetch: Fetch) -> tuple[bytes, float]:
        if not request.images:
            raise EndpointError("bad_request", "an /images/edits endpoint edits an image; it cannot generate from text alone")
        images: list[tuple[bytes, str]] = []
        mask: tuple[bytes, str] | None = None
        for image in request.images:
            if image.role == "removal_mask" and self.capabilities.native_mask:
                mask = (fetch(image.sha256), "image/png")
            else:
                images.append((fetch(image.sha256), "image/png"))
        fields = {**self.fields, **{k: str(v) for k, v in request.settings}, "seed": str(request.seed)}
        started = time.monotonic()
        data = image_edit(self.endpoint, self.model.name, request.prompt, images, mask, fields)
        return data, time.monotonic() - started
