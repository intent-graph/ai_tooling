"""Search engines for the per-image loop: pattern searches on the lattice of levels, behind ask / tell.

All three poll opportunistically (the first probe that beats the incumbent becomes the incumbent) and differ
only in the order they poll the neighbours of the incumbent (design/loop1.md: Engines). Each is a deterministic
function of the problem and the sequence of `tell`, so a run resumes by replaying its history.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from typing import Protocol, TypeVar

from virtual_unstaging.domain import Dimension, Evaluation, Point, Problem, Severity, Stop, is_better

ProblemT = TypeVar("ProblemT", contravariant=True)
CandidateT = TypeVar("CandidateT")
EvaluationT = TypeVar("EvaluationT", contravariant=True)


class SearchEngine(Protocol[ProblemT, CandidateT, EvaluationT]):
    """The ask / tell contract, whatever a candidate is: a point of the lattice for the engines below, any value for
    an engine of another kind. One rule for all: the same problem and the same sequence of `tell` give the same
    sequence of `ask` (design D10), so a run resumes by replaying its history."""

    name: str

    def start(self, problem: ProblemT, /) -> None: ...

    def ask(self) -> CandidateT | Stop: ...

    def tell(self, candidate: CandidateT, evaluation: EvaluationT | None, /) -> None: ...


Engine = SearchEngine[Problem, Point, Evaluation]  # the engines of this module: points of the lattice of levels


class PatternSearch:
    """Shared state and loop of the pattern searches; subclasses give the poll order."""

    name = "pattern"

    def __init__(self) -> None:
        self.problem: Problem | None = None
        self.evaluated: dict[Point, Evaluation | None] = {}
        self.incumbent: Point | None = None
        self.incumbent_evaluation: Evaluation | None = None

    def start(self, problem: Problem) -> None:
        self.problem = problem
        self.evaluated = {}
        self.incumbent = None
        self.incumbent_evaluation = None

    def ask(self) -> Point | Stop:
        problem = self._problem()
        if self.incumbent is None:
            return problem.start
        if self.incumbent_evaluation is not None and self.incumbent_evaluation.accepted:
            return Stop("accepted")
        for point in _unique(self.poll_order()):
            if point not in self.evaluated:
                return point
        return Stop("no_progress")

    def tell(self, point: Point, evaluation: Evaluation | None) -> None:
        self.evaluated[point] = evaluation
        if self.incumbent is None or is_better(evaluation, self.incumbent_evaluation):
            self.incumbent = point
            self.incumbent_evaluation = evaluation

    def poll_order(self) -> Iterable[Point]:
        raise NotImplementedError

    def _problem(self) -> Problem:
        if self.problem is None:
            raise RuntimeError("engine not started")
        return self.problem

    def one_step_neighbours(self) -> Iterator[Point]:
        """Registry order; for each dimension, one level up, then one level down."""
        assert self.incumbent is not None
        for dim in self._problem().dimensions:
            for direction in (1, -1):
                neighbour = _step(self.incumbent, dim, direction)
                if neighbour is not None:
                    yield neighbour


class SingleAttempt(PatternSearch):
    """The baseline: the start point, once."""

    name = "single"

    def ask(self) -> Point | Stop:
        if self.incumbent is None:
            return self._problem().start
        return Stop("engine")


class CoordinateSearch(PatternSearch):
    """Fixed poll order: registry order, one step up then one step down on each dimension."""

    name = "coordinate"

    def poll_order(self) -> Iterable[Point]:
        return self.one_step_neighbours()


class GuidedSearch(PatternSearch):
    """Poll order from the findings: the judge's moves, then the defect-to-dimension map, then the rest."""

    name = "guided"

    def poll_order(self) -> Iterable[Point]:
        yield from self._judge_moves()
        yield from self._mapped_steps()
        yield from self.one_step_neighbours()

    def _judge_moves(self) -> Iterator[Point]:
        assert self.incumbent is not None
        if self.incumbent_evaluation is None:
            return
        dims = {d.key: d for d in self._problem().dimensions}
        for move in self.incumbent_evaluation.moves:
            dim = dims.get(move.dimension)
            if dim is None or not 0 <= move.to_ordinal < len(dim.levels):
                continue
            if move.to_ordinal != self.incumbent.get(dim.key):
                yield self.incumbent.with_level(dim.key, move.to_ordinal)

    def _mapped_steps(self) -> Iterator[Point]:
        assert self.incumbent is not None
        if self.incumbent_evaluation is None:
            return
        problem = self._problem()
        dims = {d.key: d for d in problem.dimensions}
        severity_rank: dict[Severity, int] = {"blocking": 0, "minor": 1}
        findings = sorted(self.incumbent_evaluation.findings, key=lambda f: severity_rank[f.severity])
        for finding in findings:
            steps = sorted((s for s in problem.defect_map if s.defect == finding.code), key=lambda s: s.priority)
            for step in steps:
                dim = dims.get(step.dimension)
                if dim is not None:
                    neighbour = _step(self.incumbent, dim, step.direction)
                    if neighbour is not None:
                        yield neighbour


ENGINES: dict[str, Callable[[], PatternSearch]] = {
    SingleAttempt.name: SingleAttempt,
    CoordinateSearch.name: CoordinateSearch,
    GuidedSearch.name: GuidedSearch,
}


def make_engine(name: str) -> Engine:
    try:
        return ENGINES[name]()
    except KeyError:
        raise ValueError(f"unknown engine {name!r}; known: {sorted(ENGINES)}") from None


def _step(point: Point, dim: Dimension, direction: int) -> Point | None:
    target = point.get(dim.key) + direction
    if 0 <= target < len(dim.levels):
        return point.with_level(dim.key, target)
    return None


def _unique(points: Iterable[Point]) -> Iterator[Point]:
    seen: set[Point] = set()
    for point in points:
        if point not in seen:
            seen.add(point)
            yield point
