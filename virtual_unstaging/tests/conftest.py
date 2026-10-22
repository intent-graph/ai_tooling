"""Shared fixtures: synthetic room photos and masks, and a project built with the stand-in models."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from virtual_unstaging.cli import main

RULES = """\
[all]
fixed = ["door", "window", "radiator"]
movable = ["sofa", "wardrobe", "chair"]
"""


def draw_room(folder: Path, masks: Path, count: int = 3) -> None:
    """Photos of a wall, a floor and a dark box (the furniture), and the box's mask, named alike."""
    folder.mkdir(parents=True, exist_ok=True)
    masks.mkdir(parents=True, exist_ok=True)
    for index in range(count):
        pixels = np.zeros((240, 320, 3), dtype=np.uint8)
        pixels[:150] = (200, 190, 170)
        pixels[150:] = (120, 90, 60)
        x = 70 + 30 * index
        pixels[100:200, x : x + 80] = (40, 30, 30)
        Image.fromarray(pixels).save(folder / f"room_{index}.jpg", quality=92)
        mask = np.zeros((240, 320), dtype=np.uint8)
        mask[97:203, x - 3 : x + 83] = 255
        Image.fromarray(mask).save(masks / f"room_{index}.png")


def fake_project(root: Path, max_images: int = 6, workers: int = 1) -> Path:
    """A project with photos, rules and masks, its generator and judge set to the stand-in models."""
    project = root / "project"
    assert main(["--project", str(project), "init", "--name", "test"]) == 0
    text = (project / "project.toml").read_text(encoding="utf-8")
    text = text.replace('adapter = "toolserver" ', 'adapter = "fake"       ')
    text = text.replace('adapter = "openai_chat" ', 'adapter = "fake"        ')
    text = text.replace("max_images = 4", f"max_images = {max_images}")
    text = text.replace("workers = 2", f"workers = {workers}")
    (project / "project.toml").write_text(text, encoding="utf-8")
    draw_room(root / "photos" / "living", root / "masks")
    (root / "rules.toml").write_text(RULES, encoding="utf-8")
    assert main(["--project", str(project), "import", str(root / "photos" / "living")]) == 0
    assert main(["--project", str(project), "rules", str(root / "rules.toml")]) == 0
    assert main(["--project", str(project), "masks", str(root / "masks")]) == 0
    return project


@pytest.fixture
def project(tmp_path: Path) -> Path:
    return fake_project(tmp_path)


@pytest.fixture
def make_project() -> object:
    """The project builder itself, for tests that need several projects."""
    return fake_project
