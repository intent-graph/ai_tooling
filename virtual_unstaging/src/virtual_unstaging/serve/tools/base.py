"""What every server-side tool states and returns: name, version, model, input kinds, parsed params, one run."""

from __future__ import annotations

import threading
from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

from PIL import Image

from virtual_unstaging.serve.errors import ApiError

IMAGE, MASK = "image", "mask"  # input kinds: decoded as RGB, or as a grey mask


@dataclass(frozen=True)
class ToolOutput:
    images: dict[str, Image.Image]  # output name -> picture (mode L for masks, RGB for maps)
    measures: dict[str, Any]
    summary: str


class Backend(ABC):
    """The model behind a tool: loads lazily, resident afterwards; `ident` names it in the tool's version."""

    ident: ClassVar[str]
    model: ClassVar[str]

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._loaded = False
        self.failure = ""

    def state(self) -> str:
        if self._loaded:
            return "ready"
        return "failed" if self.failure else "not_loaded"

    def warm(self) -> None:
        with self._lock:
            if self._loaded:
                return
            try:
                self.load()
            except Exception as error:
                self.failure = f"{type(error).__name__}: {str(error)[:300]}"
                raise ApiError("tool_failed", f"cannot load {self.model}: {self.failure}") from error
            self._loaded = True
            self.failure = ""

    @abstractmethod
    def load(self) -> None:
        """Load weights and move them to the device; called once, under the backend's lock."""


@dataclass
class ServerTool(ABC):
    """A tool: parses its params at the edge, then runs on decoded images and a validated params mapping."""

    name: ClassVar[str]
    code_version: ClassVar[str]
    input_kinds: ClassVar[tuple[str, ...]]
    backend: Backend

    @property
    def version(self) -> str:
        """Changes with the tool's code or its model: the orchestrator's cache key includes it."""
        return f"{self.code_version}+{self.backend.ident}"

    @property
    def model(self) -> str:
        return self.backend.model

    def describe(self) -> dict[str, Any]:
        return {"name": self.name, "version": self.version, "model": self.model, "inputs": list(self.input_kinds)}

    def state(self) -> str:
        return self.backend.state()

    def warm(self) -> None:
        self.backend.warm()

    @abstractmethod
    def parse_params(self, params: Mapping[str, Any]) -> dict[str, Any]:
        """The params as the tool uses them, or ApiError bad_request: unknown keys and bad values are refused."""

    @abstractmethod
    def run(self, images: Sequence[Image.Image], params: Mapping[str, Any]) -> ToolOutput:
        """Run on images decoded per `input_kinds`; `params` came from `parse_params`."""


def refuse_unknown(params: Mapping[str, Any], allowed: set[str], tool: str) -> None:
    unknown = set(params) - allowed
    if unknown:
        raise ApiError("bad_request", f"{tool}: unknown params {', '.join(sorted(unknown))} (allowed: {', '.join(sorted(allowed))})")


def number_param(params: Mapping[str, Any], key: str, default: float, low: float, high: float, tool: str) -> float:
    value = params.get(key, default)
    if isinstance(value, bool) or not isinstance(value, int | float) or not low <= value <= high:
        raise ApiError("bad_request", f"{tool}: {key} must be a number in [{low}, {high}]")
    return float(value)
