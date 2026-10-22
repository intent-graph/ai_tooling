"""Engines on a known landscape: poll orders, acceptance, no progress, determinism under replay."""

from __future__ import annotations

from collections.abc import Callable

from virtual_unstaging.domain import (
    DefectStep,
    Dimension,
    Evaluation,
    Finding,
    Level,
    Move,
    Point,
    Problem,
    Score,
    Stop,
)
from virtual_unstaging.engines import (
    CoordinateSearch,
    GuidedSearch,
    PatternSearch,
    SingleAttempt,
    make_engine,
)


def dim(key: str, levels: int, default: int) -> Dimension:
    return Dimension(key, "instructions", "text_slot",
                     tuple(Level(i, f"l{i}", {"text": f"{key}{i}"}) for i in range(levels)), default, slot=key)


DIMS = (dim("a", 3, 1), dim("b", 3, 1), dim("c", 2, 0))
START = Point.of({"a": 1, "b": 1, "c": 0})
PROBLEM = Problem(DIMS, START, (DefectStep("opening_invented", "c", 1, 1),))


def landscape(point: Point, with_moves: bool = False) -> Evaluation:
    """Blocking unless c = 1; minor unless a = 2. The fix for the blocking defect is on the last dimension."""
    levels = point.as_dict()
    findings = []
    if levels["c"] != 1:
        findings.append(Finding("opening_invented", "blocking", None, "door"))
    if levels["a"] != 2:
        findings.append(Finding("movable_left", "minor", None, "leg"))
    blocking = sum(f.severity == "blocking" for f in findings)
    score = Score(blocking, len(findings) - blocking)
    moves = (Move("c", 1, "opening_invented", "wall behind"),) if with_moves and levels["c"] != 1 else ()
    return Evaluation(score, blocking == 0 and score.minor == 0, tuple(findings), moves)


def drive(engine: PatternSearch, objective: Callable[[Point], Evaluation], budget: int = 20) -> tuple[list[Point], str]:
    engine.start(PROBLEM)
    asked: list[Point] = []
    for _ in range(budget):
        point = engine.ask()
        if isinstance(point, Stop):
            return asked, point.reason
        asked.append(point)
        engine.tell(point, objective(point))
    return asked, "budget"


def test_single_attempt_asks_the_start_once() -> None:
    asked, reason = drive(SingleAttempt(), landscape)
    assert asked == [START] and reason == "engine"


def test_coordinate_polls_in_registry_order_and_reaches_the_optimum() -> None:
    asked, reason = drive(CoordinateSearch(), landscape)
    assert asked[1] == START.with_level("a", 2)  # first neighbour: a up
    assert reason == "accepted"
    assert asked[-1].as_dict() == {"a": 2, "b": 1, "c": 1}


def test_guided_follows_the_findings_first() -> None:
    guided, _ = drive(GuidedSearch(), landscape)
    coordinate, _ = drive(CoordinateSearch(), landscape)
    assert guided[1] == START.with_level("c", 1)  # the defect map points at c first
    assert len(guided) < len(coordinate)


def test_guided_takes_the_judge_moves_before_the_map() -> None:
    engine = GuidedSearch()
    engine.start(Problem(DIMS, START, ()))  # no map: only the judge's move points at c
    engine.tell(engine.ask(), landscape(START, with_moves=True))  # type: ignore[arg-type]
    assert engine.ask() == START.with_level("c", 1)


def test_no_progress_when_every_neighbour_is_worse() -> None:
    def bowl(point: Point) -> Evaluation:
        distance = sum(abs(v - START.as_dict()[k]) for k, v in point.as_dict().items())
        return Evaluation(Score(1, distance), False)

    asked, reason = drive(CoordinateSearch(), bowl)
    assert reason == "no_progress"
    assert len(asked) == 1 + 5  # start, then a up/down, b up/down, c up: all worse


def test_failed_attempts_count_as_worse_than_any_evaluation() -> None:
    engine = CoordinateSearch()
    engine.start(PROBLEM)
    engine.tell(engine.ask(), None)  # type: ignore[arg-type]
    neighbour = engine.ask()
    assert isinstance(neighbour, Point)
    engine.tell(neighbour, landscape(neighbour))
    assert engine.incumbent == neighbour


def test_replay_reproduces_the_same_asks() -> None:
    first, _ = drive(make_engine("guided"), lambda p: landscape(p, with_moves=True))
    replayed = make_engine("guided")
    replayed.start(PROBLEM)
    for point in first:
        assert replayed.ask() == point
        replayed.tell(point, landscape(point, with_moves=True))
