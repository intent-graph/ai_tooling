"""Value types shared by every module: stages, roles, actions, parts, findings, outcomes, specs."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Literal, get_args

Stage = Literal["clean", "clutter"]
Role = Literal["write", "generate", "edit", "judge", "revise", "distill"]
ActionKind = Literal["write", "revise", "reseed"]
Severity = Literal["blocking", "minor"]
StopReason = Literal["accepted", "no_progress", "max_iterations", "deadline", "error"]
SourceKind = Literal["template", "instruction", "schema", "spec", "lesson", "assessment", "call_output", "image",
                     "setting", "seed"]
Origin = Literal["config", "spec", "engine", "subject"]
ImageRole = Literal["generated", "raw_edit", "corrected_edit", "change_mask", "composite"]
AssessmentKind = Literal["pixel", "judge", "detector", "human"]
Arm = Literal["on", "off"]
OwnerKind = Literal["room", "scene", "clutter_spec", "clutter_item"]

STAGES: tuple[str, ...] = get_args(Stage)
ROLES: tuple[str, ...] = get_args(Role)
OWNER_KINDS: tuple[str, ...] = get_args(OwnerKind)
SEED_MODULUS = 2**31  # seeds stay below it: every model server takes them


# --- The engine's candidates and evaluations -----------------------------------------------------------------


@dataclass(frozen=True)
class Action:
    """What the engine asks next: write the first prompt, revise it from the last assessment, or reseed."""

    kind: ActionKind


@dataclass(frozen=True)
class Halt:
    """The engine's answer when the loop is over."""

    reason: StopReason


@dataclass(frozen=True, order=True)
class Score:
    """Lower is better: blocking findings first, then minor ones."""

    blocking: int
    minor: int


@dataclass(frozen=True)
class Outcome:
    """One iteration as the engine sees it: its score, its verdict, whether a pixel test (not the judge) failed it."""

    score: Score
    accepted: bool
    pixel_failure: bool


# --- Requests and their parts ------------------------------------------------------------------------------


@dataclass(frozen=True)
class SourceRef:
    """Where a part comes from: exactly the field matching the part's kind is set (data model: composition_part)."""

    file_sha: str | None = None
    lesson_id: int | None = None
    assessment_id: int | None = None
    call_id: int | None = None
    setting_name: str | None = None
    origin: Origin | None = None


@dataclass(frozen=True)
class Part:
    """One input of a request: its slot in the composer, its kind and source, its text (None for an image)."""

    slot: str
    kind: SourceKind
    text: str | None
    image_sha: str | None = None
    source: SourceRef = field(default_factory=SourceRef)


@dataclass(frozen=True)
class ModelId:
    """A model as recorded: what it is, the weights as run, its family (choice C8), its licence."""

    name: str
    revision: str
    family: str
    licence: str


# --- Judgments -------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Box:
    """A region in [0, 1] image coordinates, x0 < x1 and y0 < y1."""

    x0: float
    y0: float
    x1: float
    y1: float

    def __post_init__(self) -> None:
        if not (0 <= self.x0 < self.x1 <= 1 and 0 <= self.y0 < self.y1 <= 1):
            raise ValueError(f"box out of bounds: {self}")


@dataclass(frozen=True)
class Finding:
    code: str
    judged_severity: Severity | None  # the judge's own call, recorded, never scored
    box: Box | None
    comment: str
    regions: tuple[int, ...] = ()  # the numbered mask regions it cites (pair judge)


@dataclass(frozen=True)
class RegionItems:
    """The pair judge's answer for one numbered region of the change mask: the items it holds, possibly none."""

    region: int
    items: tuple[int, ...]  # the clutter items' ordinals in their spec


@dataclass(frozen=True)
class Judgment:
    findings: tuple[Finding, ...]
    guidance: tuple[str, ...]
    regions: tuple[RegionItems, ...] = ()

    def assigned(self) -> dict[int, tuple[int, ...]]:
        return {r.region: r.items for r in self.regions}


@dataclass(frozen=True)
class Measure:
    name: str
    value: float
    threshold: float | None = None


@dataclass(frozen=True)
class PixelResult:
    """A pixel test: what it measured, against which thresholds, and the findings it raised."""

    measures: tuple[Measure, ...]
    findings: tuple[Finding, ...]


@dataclass(frozen=True)
class NewLesson:
    """A lesson as the distiller proposes it, parsed: scope as (axis, value) pairs, evidence as iteration numbers."""

    text: str
    scope: tuple[tuple[str, str], ...]
    evidence: tuple[int, ...]
    replaces: int | None


@dataclass(frozen=True)
class Lesson:
    id: int
    stage: Stage
    text: str
    scope: tuple[tuple[str, str], ...]


# --- Exchanges --------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class ExchangeRecord:
    method: str
    path: str
    attempt: int
    status: int | None
    body_text: str | None
    body_image: bytes | None
    wire_sha: str | None
    response_text: str | None
    response_image: bytes | None
    content_type: str
    seconds: float
    error: str | None
    images: dict[str, bytes] = field(default_factory=dict)  # decoded data-URL images by hash


# --- Subjects ------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class ValueText:
    """An axis value with the text the declared space gives it."""

    axis: str
    value: str
    text: str


@dataclass(frozen=True)
class ItemSpec:
    ordinal: int
    values: tuple[ValueText, ...]


@dataclass(frozen=True)
class SubjectSpec:
    """What a loop's subject is, as the spec renderer receives it: the values in the space's axis order, the clutter
    items (clutter loop), and the rules that apply (the fixed elements, or the placement rules of the items)."""

    stage: Stage
    values: tuple[ValueText, ...]
    items: tuple[ItemSpec, ...]
    rules: tuple[str, ...]

    def pairs(self) -> frozenset[tuple[str, str]]:
        return frozenset((v.axis, v.value) for v in self.values)


def derive_seed(*parts: object) -> int:
    """A seed below SEED_MODULUS from any JSON-serializable parts: the same parts, the same seed."""
    text = json.dumps(parts, sort_keys=True, separators=(",", ":"))
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16) % SEED_MODULUS
