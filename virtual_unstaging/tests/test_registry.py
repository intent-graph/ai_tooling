"""Registry and defects: the shipped files load; malformed entries are refused; pruning by capability."""

from __future__ import annotations

import pytest

from virtual_unstaging.domain import GeneratorCapabilities
from virtual_unstaging.registry import RegistryError, load_defects, load_release, prune

DEFECTS = load_defects()

MINIMAL = """
defect_steps = [{ defect = "drift", dimension = "rule", direction = 1, priority = 1 }]

[[dimension]]
key = "rule"
input = "instructions"
realizer = "text_slot"
slot = "constraints"
default = "on"
levels = [{ label = "off", text = "" }, { label = "on", text = "Keep it." }]
"""


def test_shipped_files_load() -> None:
    release = load_release(DEFECTS)
    assert [d.key for d in release.dimensions] == [
        "wall_rule", "fixed_elements_named", "fidelity_clause", "reference_count", "mask_extent", "protected_mask",
    ]
    assert len(DEFECTS) == 9
    assert all(step.dimension in release.keys() for step in release.defect_map)


def test_release_hash_is_stable_and_content_based() -> None:
    assert load_release(DEFECTS, MINIMAL).sha256 == load_release(DEFECTS, MINIMAL).sha256
    assert load_release(DEFECTS, MINIMAL).sha256 != load_release(DEFECTS, MINIMAL.replace("Keep it.", "Keep.")).sha256


@pytest.mark.parametrize(
    "change",
    [
        ('default = "on"', 'default = "maybe"'),
        ('slot = "constraints"', 'slot = "constraints"\nrole = "reference"'),
        ('realizer = "text_slot"', 'realizer = "magic"'),
        ('defect = "drift"', 'defect = "unknown_defect"'),
        ('{ label = "on", text = "Keep it." }', '{ label = "on", text = 3 }'),
        ('key = "rule"', 'key = "rule"\ncolour = "red"'),
    ],
)
def test_malformed_registry_is_refused(change: tuple[str, str]) -> None:
    with pytest.raises(RegistryError):
        load_release(DEFECTS, MINIMAL.replace(*change))


def test_prune_by_capability() -> None:
    release = load_release(DEFECTS)
    small = GeneratorCapabilities(frozenset({"original", "removal_mask", "reference"}), max_images=3, native_mask=False)
    dims = {d.key: d for d in prune(release, small)}
    assert [lv.label for lv in dims["reference_count"].levels] == ["0", "1"]
    assert "protected_mask" not in dims  # role not accepted: only "off" left, so the dimension is dropped
    native = GeneratorCapabilities(frozenset({"original", "removal_mask", "reference"}), max_images=3, native_mask=True)
    dims = {d.key: d for d in prune(release, native)}
    assert [lv.label for lv in dims["reference_count"].levels] == ["0", "1", "2"]
    prompt_only = GeneratorCapabilities(frozenset({"original"}), max_images=1, native_mask=False)
    keys = {d.key for d in prune(release, prompt_only)}
    assert keys == {"wall_rule", "fixed_elements_named", "fidelity_clause"}
