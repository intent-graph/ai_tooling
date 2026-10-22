"""The declared space: parsing, targets, sampling, and the image-size check."""

from __future__ import annotations

import random

import pytest

from clutter_pairs import config
from clutter_pairs.space import (
    SpaceError,
    check_sizes,
    parse_space,
    parse_targets,
    sample_items,
    size_for_aspect,
    subject_spec,
)


def _texts() -> tuple[str, str, str]:
    cfg_files = {name: config.read_data_file(_cfg(), name)[1]
                 for name in ("space/ontology.toml", "space/taxonomy.toml", "space/targets.toml")}
    return cfg_files["space/ontology.toml"], cfg_files["space/taxonomy.toml"], cfg_files["space/targets.toml"]


def _cfg() -> config.Config:
    import tempfile
    from pathlib import Path

    folder = Path(tempfile.mkdtemp())
    (folder / config.CONFIG_NAME).write_text(config.template(), encoding="utf-8")
    return config.load(folder)


def test_default_space_and_targets() -> None:
    ontology, taxonomy, targets = _texts()
    space = parse_space(ontology, taxonomy)
    assert space.axes_for("room") == ("room_type", "style")
    cells = parse_targets(targets, space)
    assert len(cells) == 18 and sum(t.pairs for t in cells) == 54  # choice C9: about 50 pairs


def test_size_check_accepts_the_default_cameras_and_rejects_a_drifting_aspect() -> None:
    ontology, taxonomy, _ = _texts()
    space = parse_space(ontology, taxonomy)
    sizes = check_sizes(space, 1024, 32, 1024 * 1024)
    assert sizes["wide_landscape"] == (1248, 832)
    drifting = ontology.replace("aspect = 1.5", "aspect = 1.7777")
    with pytest.raises(SpaceError, match="comes back at"):
        check_sizes(parse_space(drifting, taxonomy), 1024, 32, 1024 * 1024)
    with pytest.raises(SpaceError, match="condition-image limit"):
        check_sizes(space, 1024, 32, 1_000_000)
    assert size_for_aspect(1.0, 256, 32) == (256, 256)


def test_a_target_on_an_item_axis_is_rejected() -> None:
    ontology, taxonomy, _ = _texts()
    space = parse_space(ontology, taxonomy)
    with pytest.raises(SpaceError, match="clutter items"):
        parse_targets('[[target]]\npairs = 1\ncategory = "boxes"\n', space)


def test_sampling_is_seeded_and_follows_the_taxonomy() -> None:
    ontology, taxonomy, _ = _texts()
    space = parse_space(ontology, taxonomy)
    first = sample_items(space, "kitchen", "cluttered", random.Random(7))
    assert first == sample_items(space, "kitchen", "cluttered", random.Random(7))
    assert 4 <= len(first) <= 6
    for item in first:
        category = space.value("category", item["category"])
        assert "kitchen" in category.attrs["rooms"] and item["placement"] in category.attrs["placements"]
    spec = subject_spec(space, "clutter", [("room_type", "kitchen"), ("density", "cluttered")],
                        [tuple(i.items()) for i in first])
    assert spec.rules[0] == space.fixed_for("kitchen") and len(spec.items) == len(first)
