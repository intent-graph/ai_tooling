"""Value types shared by every module: dimensions, points, generator requests, findings, evaluations, budgets."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Literal, get_args

Input = Literal["instructions", "clues", "guides", "settings"]
Realizer = Literal["text_slot", "reference_count", "mask_dilation", "guide_toggle", "setting"]
Role = Literal["original", "reference", "removal_mask", "protected_mask", "depth", "annotation"]
Severity = Literal["minor", "blocking"]
StopReason = Literal["accepted", "no_progress", "engine"]

INPUTS: tuple[str, ...] = get_args(Input)
REALIZERS: tuple[str, ...] = get_args(Realizer)
ROLES: tuple[str, ...] = get_args(Role)
SEVERITIES: tuple[str, ...] = get_args(Severity)

JsonScalar = str | int | float | bool


def canonical_json(value: object) -> str:
    """Serialize deterministically: sorted keys, no whitespace; the basis of every cache key."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# --- Dimensions of exploration -------------------------------------------------------------------------------


@dataclass(frozen=True)
class Level:
    """One level of a dimension; `realization` says what the generator receives at this level."""

    ordinal: int
    label: str
    realization: Mapping[str, JsonScalar]


@dataclass(frozen=True)
class Dimension:
    key: str
    input: Input
    realizer: Realizer
    levels: tuple[Level, ...]
    default_ordinal: int
    probe_cost: float = 0.0
    targets: tuple[str, ...] = ()
    slot: str | None = None  # text_slot: the prompt-template slot it fills
    role: Role | None = None  # guide_toggle: the image role it sends or not
    setting: str | None = None  # setting: the generator setting it sets

    def level(self, ordinal: int) -> Level:
        return self.levels[ordinal]

    def ordinal_of(self, label: str) -> int:
        for level in self.levels:
            if level.label == label:
                return level.ordinal
        raise KeyError(f"dimension {self.key!r} has no level {label!r}")

    def definition(self) -> dict[str, object]:
        """The content that identifies this dimension; its hash is the dimension's identity in the store."""
        return {
            "key": self.key,
            "input": self.input,
            "realizer": self.realizer,
            "levels": [{"label": lv.label, **dict(lv.realization)} for lv in self.levels],
            "default": self.levels[self.default_ordinal].label,
            "probe_cost": self.probe_cost,
            "targets": list(self.targets),
            "slot": self.slot,
            "role": self.role,
            "setting": self.setting,
        }


@dataclass(frozen=True)
class DefectStep:
    """For a defect seen, one step to try: which dimension, which way, in which priority (1 first)."""

    defect: str
    dimension: str
    direction: int
    priority: int


@dataclass(frozen=True)
class DefectType:
    code: str
    label: str
    description: str


@dataclass(frozen=True)
class Release:
    """A registry as loaded: the dimensions in registry order, and the defect-to-dimension map."""

    dimensions: tuple[Dimension, ...]
    defect_map: tuple[DefectStep, ...]
    sha256: str

    def dimension(self, key: str) -> Dimension:
        for dim in self.dimensions:
            if dim.key == key:
                return dim
        raise KeyError(key)

    def keys(self) -> tuple[str, ...]:
        return tuple(d.key for d in self.dimensions)


# --- Points --------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Point:
    """One level per dimension, as (key, ordinal) pairs sorted by key, so that equal points hash equal."""

    levels: tuple[tuple[str, int], ...]

    @classmethod
    def of(cls, mapping: Mapping[str, int]) -> Point:
        return cls(tuple(sorted(mapping.items())))

    def as_dict(self) -> dict[str, int]:
        return dict(self.levels)

    def get(self, key: str) -> int:
        return self.as_dict()[key]

    def with_level(self, key: str, ordinal: int) -> Point:
        values = self.as_dict()
        if key not in values:
            raise KeyError(key)
        values[key] = ordinal
        return Point.of(values)

    def differences(self, other: Point) -> dict[str, tuple[int, int]]:
        """Dimensions where the two points differ: key -> (own ordinal, other's ordinal)."""
        mine, theirs = self.as_dict(), other.as_dict()
        return {k: (mine[k], theirs[k]) for k in mine if mine[k] != theirs.get(k)}


def default_point(release: Release) -> Point:
    return Point.of({d.key: d.default_ordinal for d in release.dimensions})


# --- Generator requests --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class ModelRef:
    name: str
    revision: str


@dataclass(frozen=True)
class GeneratorCapabilities:
    """What a generator adapter accepts: image roles, how many images in all, whether a mask is an argument, whether
    it also makes an image from the prompt alone (a request with no image)."""

    roles: frozenset[str]
    max_images: int
    native_mask: bool
    text_only: bool = False

    def images_used_by_guides(self, protected_mask_possible: bool) -> int:
        """Image slots that guides can take, at most: the masks, unless the mask is a native argument."""
        if self.native_mask:
            return 0
        used = 1 if "removal_mask" in self.roles else 0
        if protected_mask_possible and "protected_mask" in self.roles:
            used += 1
        return used


MAX_FINDINGS = 12  # the judge's output contract: findings per judgment, at most
MAX_MOVES = 4  # and moves


@dataclass(frozen=True)
class JudgeRequestOptions:
    """What the judge is sent and how long it may answer: its speed version (design D14). 0 = as stored, no cap."""

    image_side: int = 0
    image_format: Literal["png", "jpeg"] = "png"
    max_findings: int = MAX_FINDINGS
    max_moves: int = MAX_MOVES
    comment_chars: int = 0
    critique_chars: int = 0

    def revision_suffix(self) -> str:
        """Appended to the judge's recorded revision when the request differs from the full one; '' otherwise."""
        suffix = ""
        if self.image_format != "png" or self.image_side:
            suffix += f"+{self.image_format}@{self.image_side or 'full'}"
        if (self.max_findings, self.max_moves, self.comment_chars, self.critique_chars) != (MAX_FINDINGS, MAX_MOVES, 0, 0):
            suffix += f"+answer:{self.max_findings}/{self.max_moves}/{self.comment_chars}/{self.critique_chars}"
        return suffix


@dataclass(frozen=True)
class RoleImage:
    role: Role
    sha256: str


@dataclass(frozen=True)
class GeneratorRequest:
    """A model-neutral request: the adapter maps image roles to the model's inputs."""

    prompt: str
    images: tuple[RoleImage, ...]
    settings: tuple[tuple[str, JsonScalar], ...]
    seed: int

    def payload(self) -> dict[str, object]:
        return {
            "prompt": self.prompt,
            "images": [{"role": im.role, "sha256": im.sha256} for im in self.images],
            "settings": dict(self.settings),
            "seed": self.seed,
        }

    def cache_key(self, model: ModelRef) -> str:
        return sha256_text(canonical_json({"model": [model.name, model.revision], **self.payload()}))


@dataclass(frozen=True)
class GeneratedImage:
    sha256: str
    gpu_seconds: float


# --- Judging -------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Box:
    """A region in [0, 1] image coordinates, x to the right, y down."""

    x0: float
    y0: float
    x1: float
    y1: float

    def __post_init__(self) -> None:
        if not (0.0 <= self.x0 < self.x1 <= 1.0 and 0.0 <= self.y0 < self.y1 <= 1.0):
            raise ValueError(f"invalid box {self}")


@dataclass(frozen=True)
class Finding:
    code: str
    severity: Severity
    box: Box | None
    comment: str


@dataclass(frozen=True)
class Move:
    """A step the judge proposes: one dimension, to one of its levels."""

    dimension: str
    to_ordinal: int
    targets: str | None
    reason: str


@dataclass(frozen=True, order=True)
class Score:
    """Count of findings per severity; fewer blocking first, then fewer minor: smaller is better."""

    blocking: int
    minor: int


@dataclass(frozen=True)
class Cost:
    gpu_seconds: float = 0.0
    judge_calls: int = 0


@dataclass(frozen=True)
class Evaluation:
    """What an engine is told about one attempt."""

    score: Score
    accepted: bool
    findings: tuple[Finding, ...] = ()
    moves: tuple[Move, ...] = ()
    critique: str = ""
    cost: Cost = field(default_factory=Cost)


def is_better(candidate: Evaluation | None, incumbent: Evaluation | None) -> bool:
    """Strictly better: an evaluation beats none; a smaller score beats a larger one; ties keep the incumbent."""
    if candidate is None:
        return False
    if incumbent is None:
        return True
    return candidate.score < incumbent.score


# --- Budget and search ---------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Budget:
    max_attempts: int
    max_gpu_seconds: float
    max_judge_calls: int


@dataclass(frozen=True)
class Spent:
    attempts: int = 0
    gpu_seconds: float = 0.0
    judge_calls: int = 0

    def add(self, attempts: int = 0, gpu_seconds: float = 0.0, judge_calls: int = 0) -> Spent:
        return Spent(self.attempts + attempts, self.gpu_seconds + gpu_seconds, self.judge_calls + judge_calls)

    def exhausts(self, budget: Budget) -> bool:
        """True when no further attempt fits: an attempt costs one generation and at least one judge call."""
        return (
            self.attempts >= budget.max_attempts
            or self.gpu_seconds >= budget.max_gpu_seconds
            or self.judge_calls >= budget.max_judge_calls
        )


@dataclass(frozen=True)
class Stop:
    reason: StopReason


@dataclass(frozen=True)
class Problem:
    """What an engine searches: the dimensions (pruned), the start point, the map from defects to steps."""

    dimensions: tuple[Dimension, ...]
    start: Point
    defect_map: tuple[DefectStep, ...]
