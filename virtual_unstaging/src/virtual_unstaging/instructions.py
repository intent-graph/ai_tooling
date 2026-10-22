"""Instruction stacks: a base text per role and model, an optional project overlay, rendered into prompts."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from importlib import resources
from string import Template

OVERLAY_HEADING = "Additional instructions for this project:"


@dataclass(frozen=True)
class InstructionStack:
    """A base instruction text and, optionally, the project overlay written on top of it."""

    role: str
    target_model: str
    base: str
    overlay: str | None = None

    def template(self) -> str:
        if not self.overlay or not self.overlay.strip():
            return self.base
        return f"{self.base.rstrip()}\n\n{OVERLAY_HEADING}\n{self.overlay.strip()}\n"


def load_base(role: str, name: str = "default") -> str:
    if not re.fullmatch(r"[a-z0-9_]+", role) or not re.fullmatch(r"[a-z0-9_.-]+", name):
        raise ValueError("invalid instruction name")
    return resources.files("virtual_unstaging.data").joinpath(f"instructions/{role}.{name}.md").read_text("utf-8")


def render(template: str, slots: Mapping[str, str], context: Mapping[str, str | list[str]]) -> str:
    """Fill a template's slots with fragments, then substitute the context into both.

    A fragment that names a context list which is empty is dropped (nothing to name). Unknown placeholders
    raise, so a template and its context cannot silently drift apart.
    """
    flat = {k: (", ".join(v) if isinstance(v, list) else v) for k, v in context.items()}
    empty_lists = {k for k, v in context.items() if isinstance(v, list) and not v}
    filled: dict[str, str] = {}
    for name, fragment in slots.items():
        names = set(Template(fragment).get_identifiers())
        filled[name] = "" if names & empty_lists else Template(fragment).substitute(flat)
    text = Template(template).substitute({**flat, **filled})
    return normalize(text)


def normalize(text: str) -> str:
    """Trim trailing spaces, drop empty lines left by empty slots beyond one, end with one newline."""
    lines = [line.rstrip() for line in text.strip().splitlines()]
    out: list[str] = []
    for line in lines:
        if not line and out and not out[-1]:
            continue
        out.append(line)
    return "\n".join(out) + "\n"
