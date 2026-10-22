"""The judge's tool library, as the orchestrator sees it: cheap tools run here, GPU tools on the tool server."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from typing import Any, Protocol

Fetch = Callable[[str], bytes]


@dataclass(frozen=True)
class ToolResult:
    tool: str
    version: str
    outputs: Mapping[str, bytes]
    measures: Mapping[str, Any] = field(default_factory=dict)
    summary: str = ""
    gpu_seconds: float = 0.0


class ToolProvider(Protocol):
    def version(self, name: str) -> str: ...

    def run(self, name: str, inputs: list[str], params: dict[str, Any], fetch: Fetch) -> ToolResult: ...


class ToolBox:
    """Routes each tool name to the provider that runs it; unknown names fail loudly."""

    def __init__(self, routes: Mapping[str, ToolProvider]) -> None:
        self.routes = dict(routes)

    def available(self, name: str) -> bool:
        return name in self.routes

    def version(self, name: str) -> str:
        return self._provider(name).version(name)

    def run(self, name: str, inputs: list[str], params: dict[str, Any], fetch: Fetch) -> ToolResult:
        return self._provider(name).run(name, inputs, params, fetch)

    def _provider(self, name: str) -> ToolProvider:
        try:
            return self.routes[name]
        except KeyError:
            raise KeyError(f"no provider for tool {name!r}") from None
