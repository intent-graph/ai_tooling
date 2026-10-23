"""Pixel detectors: from the measures of one `structure_map` run, a band per defect code (absent, present, or ask the
judge), with the places a judge's zoom would be cut around (design/defect_detectors.md). Pure: thresholds from the
package's `data/detectors.toml`; in shadow mode the bands are recorded and compared, never acted on."""

from __future__ import annotations

import tomllib
from collections.abc import Mapping
from dataclasses import dataclass, field
from importlib import resources
from typing import Any

from virtual_unstaging.domain import canonical_json, sha256_text

ABSENT, PRESENT, ASK, SKIPPED = "absent", "present", "ask", "skipped"
CODES = ("other_picture", "viewpoint_changed", "colour_shift", "drift")
# The gate's code is not a defect code: "absent" means the same picture, which says nothing about a scene invented in
# part; "present" (another picture) is a blocking `scene_invented`.
DEFECT_OF = {"other_picture": "scene_invented"}


@dataclass(frozen=True)
class Detection:
    code: str
    band: str
    reason: str
    severity: str | None = None
    boxes: tuple[tuple[float, float, float, float], ...] = ()
    measures: dict[str, Any] = field(default_factory=dict)


def load_thresholds(text: str | None = None) -> dict[str, Any]:
    if text is None:
        text = resources.files("virtual_unstaging.data").joinpath("detectors.toml").read_text(encoding="utf-8")
    return tomllib.loads(text)


def version(thresholds: Mapping[str, Any]) -> str:
    """The detectors' version: this code's and the thresholds' (a change of either is another detector)."""
    return "1+" + sha256_text(canonical_json(dict(thresholds)))[:12]


def _band(value: float, absent_below: float, present_above: float) -> str:
    return ABSENT if value < absent_below else PRESENT if value > present_above else ASK


def detect(measures: Mapping[str, Any], thresholds: Mapping[str, Any]) -> list[Detection]:
    """The detections of one attempt from its `structure_map` measures; a measure the tool version did not give is asked."""
    alignment = measures.get("alignment") or {}
    outside = measures.get("outside_changed_share")
    gate = thresholds["same_picture"]
    features, matched = alignment.get("features"), alignment.get("matched")
    if features is None or outside is None:
        same = Detection("other_picture", ASK, "no feature count in this structure_map version")
    else:
        share = (matched or 0) / max(1, features)
        seen = {"matched": matched, "features": features, "matched_share": round(share, 4), "outside_changed_share": outside}
        if share < gate["max_matched_share"] and outside > gate["min_outside_changed"]:
            return [Detection("other_picture", PRESENT, f"{matched} of {features} features fit and {outside:.0%} of the "
                              "outside changed: another picture", "blocking", measures=seen)] + [
                Detection(code, SKIPPED, "another picture: not measured") for code in CODES[1:]]
        fitted = alignment.get("method") == "features" and (matched or 0) >= gate["min_matched"]
        same = Detection("other_picture", ABSENT if fitted else ASK,
                         "the camera fits on the original's features" if fitted else "too few features fit to tell",
                         measures=seen)
    found = [same, _viewpoint(alignment, thresholds["viewpoint_changed"], same.band == ABSENT)]
    tone = measures.get("tone") or {}
    rule = thresholds["colour_shift"]
    if rule["measure"] in tone:
        value = float(tone[rule["measure"]])
        band = _band(value, rule["absent_below"], rule["present_above"])
        found.append(Detection("colour_shift", band, f"{rule['measure']} {value:.1f}", "minor" if band == PRESENT else None,
                               measures={rule["measure"]: value}))
    else:
        found.append(Detection("colour_shift", ASK, "no tone measure in this structure_map version"))
    rule = thresholds["drift"]
    if outside is None:
        found.append(Detection("drift", ASK, "nothing outside the removal region to compare"))
    else:
        band = _band(float(outside), rule["absent_below"], rule["present_above"])
        boxes = tuple(tuple(r["box"]) for r in measures.get("regions") or [])
        found.append(Detection("drift", band, f"{outside:.1%} of the outside changed in structure, in {len(boxes)} places",
                               boxes=boxes, measures={"outside_changed_share": outside}))  # severity: the judge's
    return found


def _viewpoint(alignment: Mapping[str, Any], rule: Mapping[str, Any], fitted: bool) -> Detection:
    if not fitted:
        return Detection("viewpoint_changed", ASK, "no feature fit: the camera cannot be measured")
    scale, rotation = float(alignment["scale"]), abs(float(alignment["rotation_deg"]))
    seen = {"scale": scale, "rotation_deg": rotation, "shift_pct": alignment.get("shift_pct")}
    low, high = rule["kept_scale"]
    if low <= scale <= high and rotation <= rule["kept_rotation_deg"]:
        return Detection("viewpoint_changed", ABSENT, "within the generator's own reframing", measures=seen)
    low, high = rule["changed_scale"]
    if not low <= scale <= high or rotation > rule["changed_rotation_deg"]:
        return Detection("viewpoint_changed", PRESENT, f"scale {scale:.3f}, rotation {rotation:.1f} degrees", measures=seen)
    return Detection("viewpoint_changed", ASK, f"scale {scale:.3f}, rotation {rotation:.1f} degrees: between the bands",
                     measures=seen)
