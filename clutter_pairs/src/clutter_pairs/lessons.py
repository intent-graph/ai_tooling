"""Lessons: which apply to a subject, in which order; how a distiller's answer is parsed (design/loops.md, "Lessons").

Pure: the store gives the lessons active at a wave; this module picks and parses.
"""

from __future__ import annotations

import random
from collections.abc import Iterable, Sequence
from typing import Any

from clutter_pairs.domain import Arm, Lesson, NewLesson

ARM_SALT = "lessons_arm"


def draw_arm(subject_seed: int, off_share: float) -> Arm:
    """The subject's arm: `off` with probability `off_share`, by a draw seeded from the subject's seed."""
    return "off" if random.Random(f"{ARM_SALT}:{subject_seed}").random() < off_share else "on"


def select(active: Iterable[Lesson], subject_values: frozenset[tuple[str, str]], limit: int) -> list[Lesson]:
    """The lessons whose scope is included in the subject's values, most specific first, then oldest first."""
    fitting = [lesson for lesson in active if set(lesson.scope) <= subject_values]
    fitting.sort(key=lambda lesson: (-len(lesson.scope), lesson.id))
    return fitting[:limit]


def parse_answer(answer: Any, subject_values: frozenset[tuple[str, str]], iterations: int,
                 active_ids: Sequence[int]) -> tuple[list[NewLesson], list[str]]:
    """The distiller's answer as lessons; a lesson with a scope outside the subject's values, evidence outside the
    loop or a replaced lesson not in use is dropped, with the reason (the answer itself stays recorded)."""
    if not isinstance(answer, dict) or not isinstance(answer.get("lessons"), list):
        raise ValueError("the distiller's answer has no lessons list")
    kept: list[NewLesson] = []
    dropped: list[str] = []
    for raw in answer["lessons"]:
        try:
            text = str(raw["text"]).strip()
            scope = tuple(sorted((str(s["axis"]), str(s["value"])) for s in raw["scope"]))
            evidence = tuple(sorted({int(n) for n in raw["evidence"]}))
            replaces = None if raw["replaces"] is None else int(raw["replaces"])
        except (KeyError, TypeError, ValueError):
            dropped.append("malformed lesson")
            continue
        if not text:
            dropped.append("empty text")
        elif not set(scope) <= subject_values or len({a for a, _ in scope}) != len(scope):
            dropped.append(f"scope {scope} is not a subset of the subject's values")
        elif not all(1 <= n <= iterations for n in evidence):
            dropped.append(f"evidence {evidence} outside iterations 1 to {iterations}")
        elif replaces is not None and replaces not in active_ids:
            dropped.append(f"replaces lesson {replaces}, which is not in use")
        else:
            kept.append(NewLesson(text, scope, evidence, replaces))
    return kept, dropped
