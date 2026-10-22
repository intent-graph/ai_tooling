"""The server-side tool set: real tools by name, or `fake` for stand-ins that need no torch and no weights."""

from __future__ import annotations

from collections.abc import Sequence

from virtual_unstaging.serve.errors import ServeConfigError
from virtual_unstaging.serve.tools.base import ServerTool
from virtual_unstaging.serve.tools.changemap import ChangeMap, FarnebackBackend, PhaseCorrelationBackend
from virtual_unstaging.serve.tools.classdiff import BrightnessClassBackend, ClassDiff, SegformerAdeBackend
from virtual_unstaging.serve.tools.segment import ColourWordBackend, GroundedSam2Backend, SegmentElements

TOOL_NAMES = ("segment_elements", "class_diff", "change_map")
FAKE = "fake"


def real_tool(name: str) -> ServerTool:
    if name == "segment_elements":
        return SegmentElements(GroundedSam2Backend())
    if name == "class_diff":
        return ClassDiff(SegformerAdeBackend())
    if name == "change_map":
        return ChangeMap(FarnebackBackend())
    raise ServeConfigError(f"unknown tool {name!r}; tools: {', '.join(TOOL_NAMES)}, or {FAKE} for stand-ins")


def fake_tool(name: str) -> ServerTool:
    if name == "segment_elements":
        return SegmentElements(ColourWordBackend())
    if name == "class_diff":
        return ClassDiff(BrightnessClassBackend())
    if name == "change_map":
        return ChangeMap(PhaseCorrelationBackend())
    raise ServeConfigError(f"unknown tool {name!r}")


def build_tools(names: Sequence[str]) -> dict[str, ServerTool]:
    """The tools to serve, by name; the name `fake` stands for stand-ins of all three (no torch, no weights)."""
    tools: dict[str, ServerTool] = {}
    for name in names:
        if name == FAKE:
            tools |= {tool: fake_tool(tool) for tool in TOOL_NAMES}
        elif name not in tools:
            tools[name] = real_tool(name)
    return tools
