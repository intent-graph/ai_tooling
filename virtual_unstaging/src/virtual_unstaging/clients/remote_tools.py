"""Tools that run on the tool server (segmentation, class difference, optical-flow change map)."""

from __future__ import annotations

from typing import Any

from virtual_unstaging.clients.http import EndpointError
from virtual_unstaging.clients.toolserver import ToolServerClient
from virtual_unstaging.tools import Fetch, ToolResult


class RemoteTools:
    def __init__(self, client: ToolServerClient) -> None:
        self.client = client
        self._versions: dict[str, str] | None = None

    def version(self, name: str) -> str:
        if self._versions is None:
            caps = self.client.capabilities()
            self._versions = {str(t["name"]): str(t["version"]) for t in caps.get("tools", [])}
        try:
            return self._versions[name]
        except KeyError:
            raise EndpointError("tool_unknown", f"the tool server has no tool {name!r}") from None

    def run(self, name: str, inputs: list[str], params: dict[str, Any], fetch: Fetch) -> ToolResult:
        for sha in inputs:
            self.client.ensure_blob(fetch(sha), "image/png")
        reply = self.client.run_tool(name, inputs, params)
        outputs = {str(k): self.client.get_blob(str(v)) for k, v in dict(reply.get("outputs", {})).items()}
        return ToolResult(
            tool=name,
            version=str(reply.get("version", self.version(name))),
            outputs=outputs,
            measures=dict(reply.get("measures", {})),
            summary=str(reply.get("summary", "")),
            gpu_seconds=float(reply.get("gpu_seconds", 0.0)),
        )
