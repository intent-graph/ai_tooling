"""The loops' policies behind virtual_unstaging's ask / tell contract: write, then revise or reseed until a stop; and
the one-iteration policy of an imported scene's clean loop.

A deterministic function of its problem and the sequence of `tell` (virtual_unstaging design D10), so a loop resumes
by replaying its stored iterations through `engines.replay` (design/loops.md, "The run").
"""

from __future__ import annotations

from dataclasses import dataclass

from clutter_pairs.domain import Action, Halt, Outcome, Score

NAME = "reviser@1"  # recorded on loop_run.engine with the stop rule's name and version
STOP_RULE = "no_progress_2@1"
PATIENCE = 2  # iterations without a strict improvement of the best score before `no_progress`
IMPORT_NAME = "import@1"  # the clean loop of an imported scene: its one iteration judges the imported image
IMPORT_STOP_RULE = "one_iteration@1"


@dataclass(frozen=True)
class LoopProblem:
    max_iterations: int


def engine_label() -> str:
    return f"{NAME}+{STOP_RULE}"


def import_engine_label() -> str:
    return f"{IMPORT_NAME}+{IMPORT_STOP_RULE}"


class Reviser:
    """Write first; after a pixel failure, reseed once (a prompt rarely fixes it); otherwise revise from the last
    assessment. Stops when accepted, at the iteration limit, or when the best score has not improved strictly for
    PATIENCE iterations."""

    name = NAME

    def __init__(self) -> None:
        self.problem: LoopProblem | None = None
        self.history: list[tuple[Action, Outcome | None]] = []

    def start(self, problem: LoopProblem, /) -> None:
        self.problem = problem
        self.history = []

    def ask(self) -> Action | Halt:
        if self.problem is None:
            raise RuntimeError("engine not started")
        if not self.history:
            return Action("write")
        last_action, last = self.history[-1]
        if last is None:
            return Halt("error")
        if last.accepted:
            return Halt("accepted")
        if len(self.history) >= self.problem.max_iterations:
            return Halt("max_iterations")
        if self._stalled():
            return Halt("no_progress")
        if last.pixel_failure and last_action.kind != "reseed":
            return Action("reseed")
        return Action("revise")

    def tell(self, candidate: Action | Halt, evaluation: Outcome | None, /) -> None:
        if not isinstance(candidate, Action):
            raise ValueError("only an action is told")
        self.history.append((candidate, evaluation))

    def _stalled(self) -> bool:
        scores = [o.score for _, o in self.history if o is not None]
        if len(scores) <= PATIENCE:
            return False
        best_before = min(scores[:-PATIENCE])
        return not any(s < best_before for s in scores[-PATIENCE:])


def score_of(blocking: int, minor: int) -> Score:
    return Score(blocking, minor)


class Importer:
    """The clean loop of an imported scene: judge the imported image once. Accepted, the loop stops; rejected, the one
    iteration is spent and the loop stops (there is no prompt to revise)."""

    name = IMPORT_NAME

    def __init__(self) -> None:
        self.history: list[tuple[Action, Outcome | None]] = []

    def start(self, problem: LoopProblem, /) -> None:
        self.history = []

    def ask(self) -> Action | Halt:
        if not self.history:
            return Action("import")
        _, last = self.history[-1]
        if last is None:
            return Halt("error")
        return Halt("accepted" if last.accepted else "max_iterations")

    def tell(self, candidate: Action | Halt, evaluation: Outcome | None, /) -> None:
        if not isinstance(candidate, Action):
            raise ValueError("only an action is told")
        self.history.append((candidate, evaluation))
