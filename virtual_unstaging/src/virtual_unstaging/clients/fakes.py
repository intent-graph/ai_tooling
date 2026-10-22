"""Stand-in models for tests and dry runs: a deterministic generator, judge and GPU tools, no network.

The fake judge reads the current levels from the request text and applies an objective given as a function,
so the whole loop (compile, generate, tools, judge contract, parsing, scoring, engines) runs for real.
"""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from typing import Any

import numpy as np
from PIL import Image

from virtual_unstaging import imaging
from virtual_unstaging.domain import GeneratorCapabilities, GeneratorRequest, ModelRef, sha256_text
from virtual_unstaging.tools import Fetch, ToolResult

FAKE_CAPABILITIES = GeneratorCapabilities(
    frozenset({"original", "reference", "removal_mask", "protected_mask"}), max_images=6, native_mask=False,
    text_only=True,
)


class FakeGenerator:
    """Fills the mask region with the mean colour around it, plus a faint pattern set by prompt and seed; from text
    alone, a flat colour set by prompt and seed, of the size the settings ask for."""

    licence = "none (test double)"

    def __init__(self, capabilities: GeneratorCapabilities = FAKE_CAPABILITIES) -> None:
        self.model = ModelRef("fake/generator", "1")
        self.capabilities = capabilities
        self.calls = 0

    def generate(self, request: GeneratorRequest, fetch: Fetch) -> tuple[bytes, float]:
        self.calls += 1
        roles = {im.role: im.sha256 for im in request.images}
        if "original" not in roles:
            return self._from_text(request), 0.5
        original = imaging.rgb_array(fetch(roles["original"]))
        height, width = original.shape[:2]
        if "removal_mask" in roles:
            mask = imaging.mask_array(fetch(roles["removal_mask"]), (width, height))
        else:
            mask = np.zeros((height, width), dtype=bool)
        ring = imaging.dilate(mask, 8) & ~mask
        fill = original[ring].mean(axis=0) if ring.any() else original.reshape(-1, 3).mean(axis=0)
        noise = np.random.default_rng(int(sha256_text(request.prompt)[:8], 16) ^ request.seed)
        out = original.copy()
        out[mask] = np.clip(fill + noise.normal(0, 0.01, size=(int(mask.sum()), 3)), 0, 1)
        pixels = (out * 255).astype(np.uint8)
        return imaging.encode_png(Image.fromarray(pixels)), 0.5

    @staticmethod
    def _from_text(request: GeneratorRequest) -> bytes:
        settings = dict(request.settings)
        side, aspect = int(settings.get("output_side", 512)), float(settings.get("output_aspect", 1.0))
        width, height = max(8, round(side * aspect**0.5)), max(8, round(side / aspect**0.5))
        noise = np.random.default_rng(int(sha256_text(request.prompt)[:8], 16) ^ request.seed)
        out = np.clip(noise.uniform(0.15, 0.85, size=3) + noise.normal(0, 0.01, size=(height, width, 3)), 0, 1)
        return imaging.encode_png(Image.fromarray((out * 255).astype(np.uint8)))


Objective = Callable[[dict[str, str]], list[dict[str, Any]]]


def default_objective(levels: dict[str, str]) -> list[dict[str, Any]]:
    """A known landscape: an invented opening unless two references are given; a left object unless the mask is wide."""
    findings: list[dict[str, Any]] = []
    if levels.get("reference_count") not in ("2", "4"):
        findings.append({"code": "opening_invented", "severity": "blocking", "box": [400, 300, 550, 800],
                         "comment": "a door where the wardrobe stood"})
    if levels.get("mask_extent") != "wide":
        findings.append({"code": "movable_left", "severity": "minor", "box": [100, 600, 180, 700],
                         "comment": "a chair leg remains"})
    return findings


_LEVEL_LINE = re.compile(r"^- (\w+) \(\w+\): (.+)$")


class FakeChat:
    """An OpenAI-style chat backend answering as a judge would, from an objective over the current levels."""

    def __init__(self, objective: Objective = default_objective, propose: bool = True, broken_first: bool = False):
        self.objective = objective
        self.propose = propose
        self.broken_first = broken_first
        self.calls = 0

    def __call__(self, messages: list[dict[str, object]], schema: dict[str, object]) -> str:
        self.calls += 1
        if self.broken_first and self.calls == 1:
            return "I think the image is fine."
        content = messages[-1]["content"]
        assert isinstance(content, list)
        text = "\n".join(str(part.get("text", "")) for part in content if isinstance(part, dict))
        levels, options = {}, {}
        for line in text.splitlines():
            match = _LEVEL_LINE.match(line)
            if match:
                labels = [lv.strip() for lv in match.group(2).split(",")]
                options[match.group(1)] = [lv.lstrip("*") for lv in labels]
                levels[match.group(1)] = next(lv[1:] for lv in labels if lv.startswith("*"))
        findings = self.objective(levels)
        moves = []
        if self.propose and any(f["code"] == "opening_invented" for f in findings) and "reference_count" in levels:
            if "2" in options["reference_count"] and levels["reference_count"] != "2":
                moves.append({"dimension": "reference_count", "to_level": "2", "targets": "opening_invented",
                              "reason": "another view shows the wall behind the wardrobe"})
        answer = {
            "evaluation": {
                "findings": findings,
                "verdict": "reject" if findings else "accept",
                "critique": "; ".join(f["comment"] for f in findings) or "clean",
            },
            "guidance": {"moves": moves},
        }
        return "<think>checking the region</think>" + json.dumps(answer)


class FakeRemoteTools:
    """GPU tools without a GPU: segmentation returns a fixed central box, class difference reports nothing."""

    def version(self, name: str) -> str:
        return "fake-1"

    def run(self, name: str, inputs: list[str], params: dict[str, Any], fetch: Fetch) -> ToolResult:
        if name == "segment_elements":
            width, height, _ = imaging.describe(fetch(inputs[0]))
            mask = np.zeros((height, width), dtype=bool)
            mask[height // 3 : 2 * height // 3, width // 3 : 2 * width // 3] = True
            labels = list(params.get("labels", []))
            found = {label: (0.11 if i == 0 else 0.0) for i, label in enumerate(labels)}
            return ToolResult(name, "fake-1", {"mask": imaging.mask_png(mask)}, {"found": found}, "fake segmentation")
        if name == "class_diff":
            width, height, _ = imaging.describe(fetch(inputs[0]))
            blank = imaging.mask_png(np.zeros((height, width), dtype=bool))
            return ToolResult(name, "fake-1", {"map": blank}, {"opening_share": 0.0}, "no class change in the region")
        raise KeyError(name)
