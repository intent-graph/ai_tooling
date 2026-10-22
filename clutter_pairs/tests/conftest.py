"""Fixtures: a dataset folder wired to the fake model server, small images, no retries."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import pytest

from clutter_pairs import config
from clutter_pairs.fakes import FakeBehaviour, FakeModelServer


def write_config(folder: Path, server: FakeModelServer, **run: int) -> None:
    settings = {"pair_target": 6, "output_side": 256, "wave_width": 2, "max_iterations": 4, **run}
    lines = [config.template()]
    text = "\n".join(lines)
    text = text.replace('[generator]                    # makes', f'[generator]\nendpoint = "{server.tools_url}"\n# makes', 1)
    text = text.replace('[judge]                        # judges', f'[judge]\nendpoint = "{server.chat_url}"\n# judges', 1)
    for key, value in settings.items():
        text = _set(text, key, value)
    (folder / config.CONFIG_NAME).write_text(text, encoding="utf-8")


def _set(text: str, key: str, value: int) -> str:
    out = []
    for line in text.splitlines():
        if line.split("=")[0].strip() == key:
            line = f"{key} = {value}"
        out.append(line)
    return "\n".join(out) + "\n"


@pytest.fixture
def behaviour() -> FakeBehaviour:
    return FakeBehaviour()


@pytest.fixture
def server(behaviour: FakeBehaviour) -> Iterator[FakeModelServer]:
    with FakeModelServer(behaviour) as running:
        yield running


@pytest.fixture
def folder(tmp_path: Path, server: FakeModelServer) -> Path:
    write_config(tmp_path, server)
    return tmp_path
