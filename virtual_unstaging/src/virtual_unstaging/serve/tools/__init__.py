"""The server-side tool set: real tools by name, or `fake` for stand-ins that need no torch and no weights."""

from __future__ import annotations

from collections.abc import Sequence

from virtual_unstaging.serve.errors import ServeConfigError
from virtual_unstaging.serve.tools.base import Backend, ServerTool
from virtual_unstaging.serve.tools.changemap import ChangeMap, FarnebackBackend, PhaseCorrelationBackend
from virtual_unstaging.serve.tools.classdiff import BrightnessClassBackend, ClassDiff, SegformerAdeBackend
from virtual_unstaging.serve.tools.inventory import ElementInventory
from virtual_unstaging.serve.tools.segment import ColourWordBackend, GroundedSam2Backend, SegmentElements
from virtual_unstaging.serve.tools.structure import FeatureBackend, StructureMap, TranslationBackend

TOOL_NAMES = ("segment_elements", "class_diff", "change_map", "element_inventory", "structure_map")
FAKE = "fake"


def real_tool(name: str, shared: dict[str, Backend] | None = None) -> ServerTool:
    """The tool by name; `shared` holds backends already built, so two tools on one model load it once."""
    shared = {} if shared is None else shared
    if name in ("segment_elements", "element_inventory"):
        backend = shared.setdefault("grounded_sam2", GroundedSam2Backend())
        assert isinstance(backend, GroundedSam2Backend)
        return SegmentElements(backend) if name == "segment_elements" else ElementInventory(backend)
    if name == "class_diff":
        return ClassDiff(SegformerAdeBackend())
    if name == "change_map":
        return ChangeMap(FarnebackBackend())
    if name == "structure_map":
        return StructureMap(FeatureBackend())
    raise ServeConfigError(f"unknown tool {name!r}; tools: {', '.join(TOOL_NAMES)}, or {FAKE} for stand-ins")


def fake_tool(name: str) -> ServerTool:
    if name == "segment_elements":
        return SegmentElements(ColourWordBackend())
    if name == "element_inventory":
        return ElementInventory(ColourWordBackend())
    if name == "class_diff":
        return ClassDiff(BrightnessClassBackend())
    if name == "change_map":
        return ChangeMap(PhaseCorrelationBackend())
    if name == "structure_map":
        return StructureMap(TranslationBackend())
    raise ServeConfigError(f"unknown tool {name!r}")


def build_tools(names: Sequence[str]) -> dict[str, ServerTool]:
    """The tools to serve, by name; the name `fake` stands for stand-ins of all of them (no torch, no weights)."""
    tools: dict[str, ServerTool] = {}
    shared: dict[str, Backend] = {}
    for name in names:
        if name == FAKE:
            tools |= {tool: fake_tool(tool) for tool in TOOL_NAMES}
        elif name not in tools:
            tools[name] = real_tool(name, shared)
    return tools
