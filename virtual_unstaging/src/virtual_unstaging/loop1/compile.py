"""Compile a point into a model-neutral generator request: a pure function of the point and the photo context."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from virtual_unstaging.domain import (
    Dimension,
    GeneratorCapabilities,
    GeneratorRequest,
    JsonScalar,
    Point,
    Role,
    RoleImage,
)
from virtual_unstaging.instructions import render


@dataclass(frozen=True)
class Guide:
    sha256: str
    tool_run_id: int | None


@dataclass(frozen=True)
class PhotoContext:
    """What compile needs about one photo, read once per optimization."""

    photo_id: int
    original: str
    removal_masks: Mapping[int, Guide]  # mask_extent ordinal -> dilated mask; key -1 when there is no such dimension
    protected_mask: Guide | None
    references: tuple[str, ...]  # candidate reference photos, best first
    movable: tuple[str, ...]
    fixed_visible: tuple[str, ...]
    fixed_group: tuple[str, ...]
    seed: int


@dataclass(frozen=True)
class CompiledRequest:
    request: GeneratorRequest
    image_tool_runs: tuple[int | None, ...]  # per image of the request, the tool run that built it (guides)


def compile_request(
    point: Point,
    dimensions: Sequence[Dimension],
    context: PhotoContext,
    template: str,
    capabilities: GeneratorCapabilities,
    fixed_settings: Mapping[str, JsonScalar] | None = None,
) -> CompiledRequest:
    levels = point.as_dict()
    slots: dict[str, str] = {}
    settings: dict[str, JsonScalar] = dict(fixed_settings or {})
    reference_count = 0
    mask_key = -1
    protected_on = False
    for dim in dimensions:
        level = dim.level(levels[dim.key])
        if dim.realizer == "text_slot":
            assert dim.slot is not None
            slots[dim.slot] = str(level.realization["text"])
        elif dim.realizer == "reference_count":
            reference_count = int(level.realization["count"])
        elif dim.realizer == "mask_dilation":
            mask_key = level.ordinal
        elif dim.realizer == "guide_toggle" and dim.role == "protected_mask":
            protected_on = bool(level.realization["on"])
        elif dim.realizer == "setting":
            assert dim.setting is not None
            settings[dim.setting] = level.realization["value"]

    images: list[tuple[Role, Guide]] = [("original", Guide(context.original, None))]
    removal = context.removal_masks.get(mask_key) or context.removal_masks.get(-1)
    if removal is not None and ("removal_mask" in capabilities.roles or capabilities.native_mask):
        images.append(("removal_mask", removal))
    if protected_on and context.protected_mask is not None and "protected_mask" in capabilities.roles:
        images.append(("protected_mask", context.protected_mask))
    slots_used = sum(1 for role, _ in images if not (role == "removal_mask" and capabilities.native_mask))
    room = max(capabilities.max_images - slots_used, 0) if "reference" in capabilities.roles else 0
    for sha in context.references[: min(reference_count, room)]:
        images.append(("reference", Guide(sha, None)))

    prompt = render(
        template,
        {"constraints": "", "keep": "", "fidelity": "", **slots, "image_legend": _legend(images, capabilities)},
        {
            "movable": list(context.movable),
            "fixed_visible": list(context.fixed_visible),
            "fixed_group": list(context.fixed_group),
        },
    )
    request = GeneratorRequest(
        prompt=prompt,
        images=tuple(RoleImage(role, guide.sha256) for role, guide in images),
        settings=tuple(sorted(settings.items())),
        seed=context.seed,
    )
    return CompiledRequest(request, tuple(guide.tool_run_id for _, guide in images))


def _legend(images: Sequence[tuple[Role, Guide]], capabilities: GeneratorCapabilities) -> str:
    """Say what each image is, in the order the model receives them."""
    lines: list[str] = []
    index = 0
    references: list[int] = []
    for role, _ in images:
        if role == "removal_mask" and capabilities.native_mask:
            lines.append("The mask given with the request marks in white where objects must be removed.")
            continue
        index += 1
        if role == "original":
            lines.append(f"Image {index} is the photo to edit.")
        elif role == "removal_mask":
            lines.append(
                f"Image {index} is a mask of the photo to edit: white marks where objects must be removed; "
                "everything under black must stay unchanged."
            )
        elif role == "protected_mask":
            lines.append(
                f"Image {index} is a mask of the photo to edit: white marks fixed elements of the building, "
                "which must stay exactly as they are."
            )
        elif role == "reference":
            references.append(index)
    if len(references) == 1:
        lines.append(
            f"Image {references[0]} is another photo of the same room, from another viewpoint, given only to show "
            "what its walls and floor look like. Do not copy its viewpoint, its framing or its furniture."
        )
    elif references:
        lines.append(
            f"Images {references[0]} to {references[-1]} are other photos of the same room, from other viewpoints, "
            "given only to show what its walls and floor look like. Do not copy their viewpoint, their framing or "
            "their furniture."
        )
    return "\n".join(lines)
