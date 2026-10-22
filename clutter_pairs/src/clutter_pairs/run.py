"""The run: waves of scenes until the pair target or the deadline; in each scene, the clean loop, then a clutter loop
per clutter spec (design/loops.md).

The store is the queue: a scene's work is whatever its loops have not finished. A loop resumes by replaying its stored
iterations through `engines.replay`; every call it makes again is answered from the store. Each call is composed
from recorded parts, sent through the recorder, and stored with its exchanges.
"""

from __future__ import annotations

import sqlite3
import time
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any

import numpy as np
from PIL import Image
from virtual_unstaging import imaging
from virtual_unstaging.clients.http import EndpointError
from virtual_unstaging.domain import canonical_json
from virtual_unstaging.engines import ReplayMismatch, replay

from clutter_pairs import lessons, pairs
from clutter_pairs.compose import (
    ComposeError,
    answer_text,
    canonical,
    compose,
    parse_json_answer,
    parse_judgment,
    render_assessment,
    render_lesson,
    render_spec,
)
from clutter_pairs.config import ConfigError
from clutter_pairs.dataset import Dataset
from clutter_pairs.domain import (
    Action,
    Halt,
    Judgment,
    Measure,
    ModelId,
    Outcome,
    Part,
    PixelResult,
    SourceRef,
    Stage,
    SubjectSpec,
    derive_seed,
)
from clutter_pairs.engine import LoopProblem, Reviser, engine_label, score_of
from clutter_pairs.models import Caller, chat_caller, generator_caller
from clutter_pairs.pairs import Thresholds
from clutter_pairs.recorder import Recorder
from clutter_pairs.space import DENSITY, Space, camera_aspect, mask_share_range, parse_space, subject_spec
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction, utc_now

PIXEL_FAILURES = {"misaligned", "global_repaint"}  # answered by a reseed first
RESUMABLE = (None, "deadline")
SMOKE_SCENES = 2
ACTIVATION_RULE = "rule:activate_lessons@1"
KNOWLEDGE = "knowledge/fixed_and_movable.md"  # what is part of the building, given to both judges


class RunPaused(RuntimeError):
    """An endpoint failed: the run stops; its loops stay unfinished and resume on the next `run`."""


class DeadlineReached(RuntimeError):
    """No call starts that the rental's deadline would cut."""


@dataclass
class Models:
    generator: Caller
    chat: Caller
    recorder: Recorder


@dataclass(frozen=True)
class RunOptions:
    smoke: bool = False
    deadline: datetime | None = None
    rental_id: int | None = None
    replan: Callable[[sqlite3.Connection], int] | None = None  # tops up the planned scenes before each wave


@dataclass
class RunSummary:
    run_id: int
    waves: int = 0
    stopped: str = ""
    pairs: int = 0
    loops: dict[str, int] = field(default_factory=dict)


@dataclass(frozen=True)
class Subject:
    stage: Stage
    id: int
    seed: int
    spec: SubjectSpec
    item_ids: tuple[int, ...]
    density: str | None
    aspect: float


def connect_models(ds: Dataset, retries: int = 3) -> Models:
    """The generator and the chat server from the configuration (the GPU session's endpoints when a rental is up)."""
    cfg = ds.cfg
    for name, service in (("generator", cfg.generator.service), ("judge", cfg.judge.service)):
        if not service.endpoint:
            raise ConfigError(f"no endpoint for the {name}: `cpairs gpu up` writes them, or set [{name}] endpoint")
    recorder = Recorder()
    generator = generator_caller(cfg.generator.service.endpoint, cfg.generator.service.secret.read(),
                                 cfg.generator.family, cfg.generator.licence, recorder.observe, retries)
    judge = ModelId(cfg.judge.model, cfg.judge.revision, cfg.judge.family, cfg.judge.licence)
    chat = chat_caller(cfg.judge.service.endpoint, cfg.judge.service.secret.read(), judge, recorder.observe, retries)
    return Models(generator, chat, recorder)


def execute(ds: Dataset, models: Models, thresholds: Thresholds, options: RunOptions) -> RunSummary:
    conn = ds.conn
    with transaction(conn):
        run_id = repo.create_run(conn, ds.config_sha, ds.target_set_id, ds.cfg.run.pair_target, options.rental_id,
                                 utc_now())
    summary = RunSummary(run_id)
    smoke_only = options.smoke or (options.rental_id is not None and not repo.rental_has_waves(conn, options.rental_id))
    try:
        while True:
            if repo.accepted_pairs(conn) >= ds.cfg.run.pair_target:
                summary.stopped = "pair_target"
                break
            if _too_late(options.deadline, ds.cfg.run.expected_call_seconds):
                summary.stopped = "deadline"
                break
            if options.replan is not None:
                with transaction(conn):
                    options.replan(conn)
            scenes = repo.wave_scenes(conn, SMOKE_SCENES if smoke_only else ds.cfg.run.wave_width)
            if not scenes:
                summary.stopped = "nothing_left"
                break
            with transaction(conn):
                wave_id = repo.create_wave(conn, run_id, smoke_only, utc_now())
                activate_lessons(conn, ds, wave_id)
            summary.waves += 1
            _run_wave(ds, models, thresholds, options, wave_id, scenes)
            if smoke_only:
                summary.stopped = "smoke_wave"
                break
    finally:
        with transaction(conn):
            repo.end_run(conn, run_id, utc_now())
    summary.pairs = repo.accepted_pairs(conn)
    for loop in repo.all_loops(conn):
        key = f"{loop.stage}:{loop.stop_reason or 'unfinished'}"
        summary.loops[key] = summary.loops.get(key, 0) + 1
    return summary


def _run_wave(ds: Dataset, models: Models, thresholds: Thresholds, options: RunOptions, wave_id: int,
              scenes: Sequence[int]) -> None:
    """The wave's scenes in parallel, each on its own connection; the first failure is raised once all are done."""

    def work(scene_id: int) -> None:
        conn = ds.connect()
        try:
            SceneWork(ds, conn, models, thresholds, options, wave_id).run(scene_id)
        finally:
            conn.close()

    with ThreadPoolExecutor(max_workers=max(1, len(scenes))) as pool:
        futures = [pool.submit(work, scene_id) for scene_id in scenes]
    errors = [f.exception() for f in futures if f.exception() is not None]
    paused = [e for e in errors if isinstance(e, RunPaused)]
    if paused:
        raise paused[0]
    if errors:
        raise errors[0]  # type: ignore[misc]


def activate_lessons(conn: sqlite3.Connection, ds: Dataset, wave_id: int) -> None:
    """Lessons distilled in earlier waves become active at this one; the owner's retirements and promotions end here.
    Each distill answer is processed once, and the rule's act recorded: the lessons added, the ones dropped and why
    (a text already active for its stage, or just added, is dropped)."""
    texts = {stage: {lesson.text for lesson in repo.active_lessons(conn, stage, wave_id)} for stage in ("clean", "clutter")}
    for call in repo.unprocessed_distill_calls(conn, ACTIVATION_RULE):
        loop = repo.loop(conn, call.loop_run_id)
        values = _loop_values(conn, loop)
        active = [lesson.id for lesson in repo.active_lessons(conn, loop.stage, loop.wave_id)]
        numbers = repo.evidence_iterations(conn, loop.id)
        added: list[int] = []
        try:
            new, dropped = lessons.parse_answer(parse_json_answer(call.answer or ""), values, len(numbers), active)
        except (ComposeError, ValueError) as error:
            new, dropped = [], [str(error)]
        for lesson in new:
            if lesson.text in texts[loop.stage]:
                dropped.append(f"already active: {lesson.text[:80]}")
                continue
            texts[loop.stage].add(lesson.text)
            added.append(repo.insert_lesson(conn, loop.stage, lesson, call.id, wave_id,
                                            [numbers[n] for n in lesson.evidence]))
            if lesson.replaces is not None:
                repo.end_lesson(conn, lesson.replaces, wave_id, "replaced")
        repo.add_decision(conn, utc_now(), ACTIVATION_RULE, "decision_rule",
                          {"distill_call": call.id, "wave": wave_id, "added": added, "dropped": dropped})
    for lesson_id, kind in repo.pending_lesson_ends(conn):
        repo.end_lesson(conn, lesson_id, wave_id, kind)


def _loop_values(conn: sqlite3.Connection, loop: repo.LoopRow) -> frozenset[tuple[str, str]]:
    if loop.stage == "clean":
        assert loop.scene_id is not None
        return frozenset(repo.scene(conn, loop.scene_id).values)
    assert loop.clutter_spec_id is not None
    spec = repo.clutter_spec(conn, loop.clutter_spec_id)
    return frozenset(repo.scene(conn, spec.scene_id).values + spec.values)


def subject_of(conn: sqlite3.Connection, ds: Dataset, stage: str, subject_id: int) -> Subject:
    """A loop's subject from the store, as the spec renderer and the pixel tests need it: rendered with the space
    version its building was sampled from, which may be older than the dataset's current one."""
    if stage == "clean":
        scene = repo.scene(conn, subject_id)
        space = space_of(conn, ds, scene.space_version_id)
        spec = subject_spec(space, "clean", scene.values)
        return Subject("clean", subject_id, scene.seed, spec, (), None, camera_aspect(space, dict(scene.values)["camera"]))
    clutter = repo.clutter_spec(conn, subject_id)
    scene = repo.scene(conn, clutter.scene_id)
    space = space_of(conn, ds, scene.space_version_id)
    spec = subject_spec(space, "clutter", scene.values + clutter.values, clutter.items)
    return Subject("clutter", subject_id, clutter.seed, spec, clutter.item_ids, dict(clutter.values)[DENSITY],
                   camera_aspect(space, dict(scene.values)["camera"]))


def space_of(conn: sqlite3.Connection, ds: Dataset, version: int) -> Space:
    if version == ds.space_version_id:
        return ds.space
    ontology, taxonomy = repo.space_version_files(conn, version)
    return parse_space(repo.file_content(conn, ontology), repo.file_content(conn, taxonomy))


def outcome_of(conn: sqlite3.Connection, severities: dict[str, str], iteration: repo.IterationRow) -> Outcome:
    """A stored iteration as the engine was told it."""
    codes = [f.code for a in repo.assessments(conn, iteration.id) for f in a.judgment.findings]
    blocking = sum(1 for c in codes if severities[c] == "blocking")
    return Outcome(score_of(blocking, len(codes) - blocking), iteration.verdict == "accept",
                   any(c in PIXEL_FAILURES for c in codes))


def _too_late(deadline: datetime | None, seconds: float) -> bool:
    return deadline is not None and datetime.now(UTC) + timedelta(seconds=seconds) > deadline


class SceneWork:
    """One scene's work in a wave: its clean loop unless finished, then its clutter loops."""

    def __init__(self, ds: Dataset, conn: sqlite3.Connection, models: Models, thresholds: Thresholds,
                 options: RunOptions, wave_id: int) -> None:
        self.ds, self.conn, self.models, self.t, self.options, self.wave_id = ds, conn, models, thresholds, options, wave_id
        self.severities = ds.severities()
        self.model_ids: dict[str, int] = {}

    def run(self, scene_id: int) -> None:
        loop = repo.find_loop(self.conn, "clean", scene_id)
        if loop is None or loop.stop_reason in RESUMABLE:  # also a loop accepted but not closed (distill, stop)
            self.run_loop("clean", scene_id, None)
        clean = repo.accepted_clean_image(self.conn, scene_id)
        if clean is None:
            return
        for spec in repo.clutter_specs(self.conn, scene_id):
            loop = repo.find_loop(self.conn, "clutter", spec.id)
            if loop is not None and loop.stop_reason not in RESUMABLE:
                continue
            if loop is None and repo.accepted_pairs(self.conn) >= self.ds.cfg.run.pair_target:
                return
            self.run_loop("clutter", spec.id, clean)

    # --- The loop ----------------------------------------------------------------------------------------------

    def run_loop(self, stage: Stage, subject_id: int, input_image: str | None) -> None:
        conn = self.conn
        subject = subject_of(conn, self.ds, stage, subject_id)
        loop = repo.find_loop(conn, stage, subject_id)
        with transaction(conn):
            if loop is None:
                arm = lessons.draw_arm(subject.seed, float(self.ds.rule["off_share"]))
                loop_id = repo.create_loop(conn, self.wave_id, stage, subject_id, input_image, arm, engine_label(),
                                           self.ds.cfg.run.max_iterations)
            else:
                loop_id = loop.id
                repo.set_stop(conn, loop_id, None)
        loop_row = repo.loop(conn, loop_id)
        engine = Reviser()
        engine.start(LoopProblem(loop_row.max_iterations))
        stored = repo.iterations(conn, loop_id)
        done = [it for it in stored if it.verdict is not None]
        pending = next((it for it in stored if it.verdict is None), None)
        candidate_of: Callable[[repo.IterationRow], Action | Halt] = lambda it: Action(it.action)  # type: ignore[arg-type]  # noqa: E731
        evaluation_of: Callable[[repo.IterationRow], Outcome] = lambda it: outcome_of(conn, self.severities, it)  # noqa: E731
        replay(engine, done, candidate_of, evaluation_of, label=f"loop {loop_id}: ")
        reason = "error"
        try:
            while True:
                asked = engine.ask()
                if isinstance(asked, Halt):
                    reason = asked.reason
                    break
                n = len(done) + 1
                with transaction(conn):
                    if pending is not None and pending.n == n:
                        if pending.action != asked.kind:
                            raise ReplayMismatch(f"loop {loop_id}: iteration {n} was {pending.action}, the engine asks {asked.kind}")
                        iteration_id = pending.id
                        repo.clear_iteration_results(conn, iteration_id)
                    else:
                        iteration_id = repo.create_iteration(conn, loop_id, n, asked.kind,
                                                             self._seed(subject, asked, done))
                pending = None
                iteration = next(it for it in repo.iterations(conn, loop_id) if it.id == iteration_id)
                outcome = self.run_iteration(loop_row, subject, iteration, done)
                engine.tell(asked, outcome)
                done.append(next(it for it in repo.iterations(conn, loop_id) if it.id == iteration_id))
            if len(done) >= 2 and reason in ("accepted", "no_progress", "max_iterations"):
                self.distill(loop_row, subject, done, reason)
        except DeadlineReached:
            reason = "deadline"
        with transaction(conn):
            repo.set_stop(conn, loop_id, reason)

    @staticmethod
    def _seed(subject: Subject, asked: Action, done: Sequence[repo.IterationRow]) -> int:
        """The first iteration takes the subject's seed; a revision keeps the seed (only the prompt changes); a
        reseed draws a new one."""
        if not done:
            return subject.seed
        if asked.kind == "revise":
            return done[-1].seed
        return derive_seed(subject.seed, "reseed", len(done) + 1)

    def run_iteration(self, loop: repo.LoopRow, subject: Subject, iteration: repo.IterationRow,
                      done: Sequence[repo.IterationRow]) -> Outcome | None:
        prompt_call = self.prompt(loop, subject, iteration, done)
        if prompt_call is None:
            return None
        if subject.stage == "clean":
            return self.clean_iteration(loop, subject, iteration, prompt_call)
        return self.clutter_iteration(loop, subject, iteration, prompt_call)

    # --- Steps -------------------------------------------------------------------------------------------------

    def prompt(self, loop: repo.LoopRow, subject: Subject, iteration: repo.IterationRow,
               done: Sequence[repo.IterationRow]) -> tuple[int, str] | None:
        """The prompt or instruction this iteration uses: written, revised, or the previous one (reseed)."""
        if iteration.action == "reseed":
            previous = repo.prompt_call_of(self.conn, done[-1].id)
            assert previous is not None
            return previous, answer_text(repo.call(self.conn, previous).answer or "")
        stage, role = subject.stage, iteration.action
        parts = [self._file("instruction", "instruction", f"instructions/{stage}_{'writer' if role == 'write' else 'reviser'}.md"),
                 self._file("schema", "schema", "schemas/text.json"),
                 self._spec(subject, f"{stage}_{role}")]
        if role == "revise":
            previous = repo.prompt_call_of(self.conn, done[-1].id)
            assert previous is not None
            parts.append(self._call_output("previous", previous))
            parts += [self._assessment("assessment", a, done[-1].n) for a in repo.assessments(self.conn, done[-1].id)]
        parts += self._lessons(loop, subject)
        parts += self._chat_settings(self.ds.cfg.judge.writer_temperature, subject, role, iteration.n)
        call = self.call(loop, iteration.id, role, f"{stage}_{role}", self.models.chat, parts)
        try:
            return call.id, answer_text(call.answer or "")
        except ComposeError as error:
            self._bad_answer(call.id, error)
            return None

    def clean_iteration(self, loop: repo.LoopRow, subject: Subject, iteration: repo.IterationRow,
                        prompt_call: tuple[int, str]) -> Outcome | None:
        parts = [self._call_output("prompt", prompt_call[0]),
                 self._setting("output_side", self.ds.cfg.run.output_side, "config"),
                 self._setting("output_aspect", subject.aspect, "spec"),
                 Part("seed", "seed", str(iteration.seed), source=SourceRef(origin="engine"))]
        generated = self.call(loop, iteration.id, "generate", "clean_generate", self.models.generator, parts)
        assert generated.output_image is not None
        with transaction(self.conn):
            repo.add_iteration_image(self.conn, iteration.id, "generated", generated.output_image)
        parts = [self._file("instruction", "instruction", "instructions/clean_judge.md"),
                 self._file("knowledge", "instruction", KNOWLEDGE),
                 self._file("schema", "schema", "schemas/clean_judgment.json"),
                 self._spec(subject, "clean_judge"),
                 Part("image", "image", None, generated.output_image)]
        parts += self._chat_settings(self.ds.cfg.judge.judge_temperature, subject, "judge", iteration.n)
        judged = self.call(loop, iteration.id, "judge", "clean_judge", self.models.chat, parts)
        judgment = self._parse(judged, "clean", 0)
        if judgment is None:
            return None
        return self._conclude(iteration.id, [("judge", judged.id, judgment, ())], subject)

    def clutter_iteration(self, loop: repo.LoopRow, subject: Subject, iteration: repo.IterationRow,
                          prompt_call: tuple[int, str]) -> Outcome | None:
        assert loop.input_image is not None
        parts = [self._call_output("prompt", prompt_call[0]),
                 Part("original", "image", None, loop.input_image),
                 self._setting("output_side", self.ds.cfg.run.output_side, "config"),
                 Part("seed", "seed", str(iteration.seed), source=SourceRef(origin="engine"))]
        edited = self.call(loop, iteration.id, "edit", "clutter_edit", self.models.generator, parts)
        assert edited.output_image is not None
        clean_bytes = self.ds.blobs.get(loop.input_image)
        clean, edit = imaging.rgb_array(clean_bytes), imaging.rgb_array(self.ds.blobs.get(edited.output_image))
        assert subject.density is not None
        prepared = pairs.prepare(clean, edit, mask_share_range(space_of(self.conn, self.ds, self._version(loop)),
                                                                subject.density), self.t)
        images = {"raw_edit": edited.output_image}
        with transaction(self.conn):
            if clean.shape == edit.shape:
                images["corrected_edit"] = self._image(pairs.to_uint8(prepared.corrected))
                images["change_mask"] = self._image(prepared.alpha)
                images["composite"] = self._image(pairs.composite(clean, prepared.corrected, prepared.alpha))
            for role, sha in images.items():
                repo.add_iteration_image(self.conn, iteration.id, role, sha)
        assessments: list[tuple[str, int | None, Judgment, tuple[Measure, ...]]] = [
            ("pixel", None, Judgment(prepared.result.findings, ()), prepared.result.measures)]
        if not prepared.result.findings:
            parts = [self._file("instruction", "instruction", "instructions/pair_judge.md"),
                     self._file("knowledge", "instruction", KNOWLEDGE),
                     self._file("schema", "schema", "schemas/pair_judgment.json"),
                     self._spec(subject, "pair_judge"),
                     Part("clean", "image", None, loop.input_image),
                     Part("cluttered", "image", None, images["composite"]),
                     Part("mask", "image", None, images["change_mask"])]
            parts += self._chat_settings(self.ds.cfg.judge.judge_temperature, subject, "judge", iteration.n)
            judged = self.call(loop, iteration.id, "judge", "pair_judge", self.models.chat, parts)
            judgment = self._parse(judged, "clutter", len(subject.item_ids))
            if judgment is None:
                return None
            explained: PixelResult = pairs.explain(prepared.mask, [i.box for i in judgment.located], self.t)
            assessments.append(("judge", judged.id, judgment, ()))
            assessments.append(("pixel", None, Judgment(explained.findings, ()), explained.measures))
        return self._conclude(iteration.id, assessments, subject)

    def _version(self, loop: repo.LoopRow) -> int:
        spec = repo.clutter_spec(self.conn, loop.clutter_spec_id or 0)
        return repo.scene(self.conn, spec.scene_id).space_version_id

    def _conclude(self, iteration_id: int, assessments: Sequence[tuple[str, int | None, Judgment, tuple[Measure, ...]]],
                  subject: Subject) -> Outcome:
        """Store the assessments and the verdict: accepted when no finding's code is blocking (reasons.toml)."""
        blocking = minor = 0
        pixel_failure = False
        with transaction(self.conn):
            for kind, call_id, judgment, measures in assessments:
                codes = [f.code for f in judgment.findings]
                blocks = sum(1 for c in codes if self.severities[c] == "blocking")
                blocking, minor = blocking + blocks, minor + len(codes) - blocks
                pixel_failure = pixel_failure or (kind == "pixel" and any(c in PIXEL_FAILURES for c in codes))
                repo.add_assessment(self.conn, iteration_id, kind, "fail" if blocks else "pass", call_id, judgment,
                                    measures, subject.item_ids, self.t.as_dict() if kind == "pixel" else {})
            repo.set_verdict(self.conn, iteration_id, "revise" if blocking else "accept")
        return Outcome(score_of(blocking, minor), blocking == 0, pixel_failure)

    def distill(self, loop: repo.LoopRow, subject: Subject, done: Sequence[repo.IterationRow], reason: str) -> None:
        parts = [self._file("instruction", "instruction", "instructions/distiller.md"),
                 self._file("schema", "schema", "schemas/lessons.json"),
                 self._spec(subject, "distill")]
        for it in done:
            if it.action in ("write", "revise"):
                prompt = repo.prompt_call_of(self.conn, it.id)
                if prompt is not None:
                    parts.append(self._call_output("history", prompt))
            parts += [self._assessment("history", a, it.n) for a in repo.assessments(self.conn, it.id)]
        parts.append(Part("outcome", "setting", reason, source=SourceRef(setting_name="stop_reason", origin="engine")))
        active = repo.active_lessons(self.conn, subject.stage, loop.wave_id)
        parts += [self._lesson(lesson) for lesson in lessons.select(active, subject.spec.pairs(), len(active))]
        parts += self._chat_settings(self.ds.cfg.judge.writer_temperature, subject, "distill", 0)
        self.call(loop, None, "distill", "distill", self.models.chat, parts)

    # --- Calls -------------------------------------------------------------------------------------------------

    def call(self, loop: repo.LoopRow, iteration_id: int | None, role: str, composer_name: str, caller: Caller,
             parts: Sequence[Part]) -> repo.CallRow:
        """Compose, then answer from the store when this exact request was answered before; otherwise send it through
        the recorder and store the call with its parts and exchanges."""
        conn = self.conn
        composer_sha, composer = self.ds.composer(composer_name)
        model_id = self._model_id(caller)
        request_text, request_sha = canonical(compose(composer, caller.model, parts))
        own = repo.find_own_call(conn, loop.id, iteration_id, role, request_sha)
        if own is not None:
            return own
        earlier = repo.find_answered_call(conn, request_sha, model_id)
        common: dict[str, Any] = dict(loop_id=loop.id, iteration_id=iteration_id, role=role, model_id=model_id,
                                      composer_sha=composer_sha, request_text=request_text, parts=parts)
        if earlier is not None:
            with transaction(conn):
                call_id = repo.insert_call(conn, self.ds.blobs, answer=earlier.answer, output_image=earlier.output_image,
                                           reused_call_id=earlier.id, started_at=utc_now(), wall_seconds=0.0,
                                           gpu_seconds=None, error_code=earlier.error_code, error_message=None,
                                           exchanges=(), **common)
            return repo.call(conn, call_id)
        if _too_late(self.options.deadline, self.ds.cfg.run.expected_call_seconds):
            raise DeadlineReached(f"no time left for a {role} call before the deadline")
        started, clock = utc_now(), time.monotonic()
        request = compose(composer, caller.model, parts)
        failure: Exception | None = None
        with self.models.recorder.call() as exchanges:
            try:
                answer = caller.call(request, self.ds.blobs.get)
            except Exception as error:  # recorded with its exchanges, then raised
                failure = error
        if failure is not None:
            code = failure.code if isinstance(failure, EndpointError) else "internal"
            with transaction(conn):
                repo.insert_call(conn, self.ds.blobs, answer=None, output_image=None, reused_call_id=None,
                                 started_at=started, wall_seconds=time.monotonic() - clock, gpu_seconds=None,
                                 error_code=code, error_message=str(failure)[:1000], exchanges=exchanges, **common)
            if isinstance(failure, EndpointError):
                raise RunPaused(f"{role} call to {caller.model.name}: {failure}") from failure
            raise failure
        with transaction(conn):
            output = None if answer.image is None else repo.record_image(conn, self.ds.blobs, answer.image)
            call_id = repo.insert_call(conn, self.ds.blobs, answer=answer.text, output_image=output, reused_call_id=None,
                                       started_at=started, wall_seconds=answer.wall_seconds,
                                       gpu_seconds=answer.gpu_seconds, error_code=None, error_message=None,
                                       exchanges=exchanges, **common)
        return repo.call(conn, call_id)

    def _parse(self, call: repo.CallRow, stage: str, items: int) -> Judgment | None:
        allowed = {c for c, r in self.ds.reasons.items() if r.stage in (stage, "both") and r.by in ("judge", "both")}
        try:
            return parse_judgment(call.answer or "", stage, items, allowed)
        except ComposeError as error:
            self._bad_answer(call.id, error)
            return None

    def _bad_answer(self, call_id: int, error: Exception) -> None:
        with transaction(self.conn):
            repo.mark_bad_answer(self.conn, call_id, str(error)[:1000])

    def _model_id(self, caller: Caller) -> int:
        key = f"{caller.model.name}@{caller.model.revision}"
        if key not in self.model_ids:
            with transaction(self.conn):
                self.model_ids[key] = repo.model_row(self.conn, caller.model)
        return self.model_ids[key]

    # --- Parts -------------------------------------------------------------------------------------------------

    def _file(self, slot: str, kind: str, packaged: str) -> Part:
        sha, content = self.ds.file(packaged)
        return Part(slot, kind, content, source=SourceRef(file_sha=sha))  # type: ignore[arg-type]

    def _spec(self, subject: Subject, composer_name: str) -> Part:
        _, composer = self.ds.composer(composer_name)
        return Part("spec", "spec", render_spec(subject.spec, composer.renderer, composer.renderer_version))

    def _call_output(self, slot: str, call_id: int) -> Part:
        return Part(slot, "call_output", answer_text(repo.call(self.conn, call_id).answer or ""),
                    source=SourceRef(call_id=call_id))

    def _assessment(self, slot: str, row: repo.AssessmentRow, n: int) -> Part:
        return Part(slot, "assessment", render_assessment(n, row.kind, row.judgment, row.measures),
                    source=SourceRef(assessment_id=row.id))

    def _lesson(self, lesson: Any) -> Part:
        return Part("lesson", "lesson", render_lesson(lesson), source=SourceRef(lesson_id=lesson.id))

    def _lessons(self, loop: repo.LoopRow, subject: Subject) -> list[Part]:
        if loop.lessons_arm == "off":
            return []
        active = repo.active_lessons(self.conn, subject.stage, loop.wave_id)
        chosen = lessons.select(active, subject.spec.pairs(), self.ds.cfg.run.lessons_per_request)
        return [self._lesson(lesson) for lesson in chosen]

    def _setting(self, name: str, value: Any, origin: str) -> Part:
        return Part("setting", "setting", canonical_json(value), source=SourceRef(setting_name=name, origin=origin))  # type: ignore[arg-type]

    def _chat_settings(self, temperature: float, subject: Subject, role: str, n: int) -> list[Part]:
        seed = derive_seed(subject.seed, subject.stage, role, n)
        return [self._setting("temperature", temperature, "config"),
                self._setting("max_tokens", self.ds.cfg.judge.max_tokens, "config"),
                Part("seed", "seed", str(seed), source=SourceRef(origin="engine"))]

    def _image(self, pixels: np.ndarray) -> str:
        return repo.record_image(self.conn, self.ds.blobs, imaging.encode_png(Image.fromarray(pixels)))
