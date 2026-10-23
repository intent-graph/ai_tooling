"""Pixel detectors in shadow: bands from structure_map measures, another picture stopping the cascade, a measure an
older tool version did not give asked rather than guessed, and the report beside the judge."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from test_loop1 import api_run

from virtual_unstaging import detectors
from virtual_unstaging.cli import main
from virtual_unstaging.report import detector_report, render_detectors
from virtual_unstaging.store.db import connect

THRESHOLDS = detectors.load_thresholds()


def measures(scale: float = 1.01, rotation: float = 0.2, matched: int = 40, features: int = 120, method: str = "features",
             outside: float | None = 0.03, uneven: float = 5.0) -> dict[str, Any]:
    return {"alignment": {"scale": scale, "shift_pct": 0.5, "rotation_deg": rotation, "applied": True, "method": method,
                          "features": features, "matched": matched},
            "outside_changed_share": outside, "regions": [{"box": [0.1, 0.1, 0.2, 0.2], "share": 0.01}],
            "tone": {"shift_de": 2.0, "shift_lab": [1.0, 1.0, 1.0], "uneven_de": uneven}}


def bands(found: list[detectors.Detection]) -> dict[str, str]:
    return {d.code: d.band for d in found}


def test_a_clean_output_is_the_same_picture_framed_alike_with_drift_asked() -> None:
    found = detectors.detect(measures(), THRESHOLDS)
    assert bands(found) == {"other_picture": "absent", "viewpoint_changed": "absent", "colour_shift": "absent",
                            "drift": "ask"}
    drift = found[-1]
    assert drift.boxes == ((0.1, 0.1, 0.2, 0.2),) and drift.severity is None  # the zoom's place; severity is the judge's


def test_another_picture_is_blocking_and_stops_the_cascade() -> None:
    found = detectors.detect(measures(matched=2, features=500, method="ecc", outside=0.4), THRESHOLDS)
    assert found[0].band == "present" and found[0].severity == "blocking"
    assert detectors.DEFECT_OF["other_picture"] == "scene_invented"
    assert {d.band for d in found[1:]} == {"skipped"}


def test_few_features_ask_instead_of_deciding() -> None:
    found = bands(detectors.detect(measures(matched=0, features=14, method="ecc", outside=0.0), THRESHOLDS))
    assert found["other_picture"] == "ask" and found["viewpoint_changed"] == "ask" and found["drift"] == "absent"


@pytest.mark.parametrize(("scale", "rotation", "band"), [(1.03, 0.5, "absent"), (1.045, 1.5, "ask"), (1.1, 0.0, "present"),
                                                         (1.0, 3.0, "present")])
def test_viewpoint_bands(scale: float, rotation: float, band: str) -> None:
    assert bands(detectors.detect(measures(scale=scale, rotation=rotation), THRESHOLDS))["viewpoint_changed"] == band


@pytest.mark.parametrize(("uneven", "band"), [(5.0, "absent"), (11.0, "ask"), (20.0, "present")])
def test_colour_bands(uneven: float, band: str) -> None:
    assert bands(detectors.detect(measures(uneven=uneven), THRESHOLDS))["colour_shift"] == band


def test_measures_of_an_older_structure_map_are_asked_not_guessed() -> None:
    old = {"alignment": {"scale": 1.0, "shift_pct": 0.0, "rotation_deg": 0.0, "applied": True},
           "outside_changed_share": 0.2, "regions": []}
    assert bands(detectors.detect(old, THRESHOLDS)) == {"other_picture": "ask", "viewpoint_changed": "ask",
                                                        "colour_shift": "ask", "drift": "present"}


def test_the_version_follows_the_thresholds() -> None:
    changed = {**THRESHOLDS, "drift": {**THRESHOLDS["drift"], "present_above": 0.2}}
    assert detectors.version(THRESHOLDS) != detectors.version(changed)


def test_the_report_counts_bands_beside_the_judge(project: Path, capsys: pytest.CaptureFixture[str]) -> None:
    run, _ = api_run(project, "single")
    report = detector_report(connect(project / "project.sqlite"), [run])
    assert report["judged_attempts"] > 0 and report["without_structure_map"] == 0
    assert report["codes"]["drift"]["bands"] == {"ask": report["judged_attempts"]}  # the fake map measures nothing outside
    assert "pixel detectors in shadow" in render_detectors(report)
    assert main(["--project", str(project), "report", "--detectors"]) == 0
    assert "other_picture" in capsys.readouterr().out
