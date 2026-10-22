"""The command line on the stand-in models: exit codes and outputs."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from clutter_pairs.cli import EXIT_OK, main


def test_the_commands_end_to_end(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    folder = tmp_path / "ds"
    assert main(["init", str(folder)]) == EXIT_OK
    config = (folder / "clutter_pairs.toml").read_text()
    config = config.replace("output_side = 1024 ", "output_side = 256 ").replace("pair_target = 50 ", "pair_target = 4 ")
    (folder / "clutter_pairs.toml").write_text(config)
    base = ["--dataset", str(folder)]
    assert main([*base, "plan"]) == EXIT_OK
    assert main([*base, "run", "--fake", "--smoke"]) == EXIT_OK
    assert main([*base, "run", "--fake"]) == EXIT_OK
    capsys.readouterr()
    assert main([*base, "report", "--json"]) == EXIT_OK
    assert json.loads(capsys.readouterr().out)["pairs"] >= 4
    assert main([*base, "audit"]) == EXIT_OK
    assert main([*base, "audit", "--json"]) == EXIT_OK
    pair = None
    capsys.readouterr()
    assert main([*base, "lessons", "--json"]) == EXIT_OK
    lessons = json.loads(capsys.readouterr().out)
    if lessons:
        assert main([*base, "lessons", "retire", str(lessons[0]["id"]), "--reason", "test"]) == EXIT_OK
    assert main([*base, "decide", "threshold", "max_shift_px", "3"]) == EXIT_OK
    assert main([*base, "decide", "threshold", "no_such", "3"]) != EXIT_OK
    assert main([*base, "export", "v1"]) == EXIT_OK
    assert main([*base, "export", "v1"]) != EXIT_OK
    del pair


def test_run_without_endpoints_says_how_to_get_them(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    folder = tmp_path / "ds"
    assert main(["init", str(folder)]) == EXIT_OK
    assert main(["--dataset", str(folder), "run"]) != EXIT_OK
    assert "gpu up" in capsys.readouterr().err
