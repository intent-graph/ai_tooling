"""The names the element inventory looks for: the photo's fixed and movable elements and the package's generic
building elements, cleaned for the detector (design/loop1.md: Automatic tool runs)."""

from __future__ import annotations

import re
from collections.abc import Sequence
from importlib import resources

MAX_NAMES = 96  # the tool server's limit, fixed and movable together
_LEADING_ARTICLE = re.compile(r"^(the|a|an)\s+")
_NOT_ALLOWED = re.compile(r"[^a-z0-9 '\-]+")
# Surfaces, not elements: a detector's box for "walls" moves from one picture to the next, and the change map measures
# surfaces already. A name whose last word is one of these is left out.
SURFACES = frozenset({"wall", "walls", "floor", "floors", "ceiling", "ceilings", "tiles", "tiling", "flooring", "panelling"})


def building_elements() -> tuple[str, ...]:
    text = resources.files("virtual_unstaging.data").joinpath("building_elements.txt").read_text(encoding="utf-8")
    return tuple(line.strip() for line in text.splitlines() if line.strip() and not line.startswith("#"))


def clean(name: str) -> str:
    """Lower case, no leading article, only letters, digits, spaces, hyphens and apostrophes; '' when nothing is left."""
    text = " ".join(_NOT_ALLOWED.sub(" ", name.lower()).split())
    return _LEADING_ARTICLE.sub("", text)[:80].strip()


def inventory_names(fixed: Sequence[str], movable: Sequence[str]) -> tuple[list[str], list[str]]:
    """Fixed names (the photo's, then the generic building elements), then movable ones; each name once, a name that is
    both fixed and movable counted fixed; surfaces left out; at most MAX_NAMES, fixed first."""
    seen: set[str] = set()
    lists: tuple[list[str], list[str]] = ([], [])
    for target, names in ((lists[0], [*fixed, *building_elements()]), (lists[1], list(movable))):
        for name in names:
            cleaned = clean(name)
            if cleaned and cleaned not in seen and cleaned.split()[-1] not in SURFACES and len(seen) < MAX_NAMES:
                seen.add(cleaned)
                target.append(cleaned)
    return lists
