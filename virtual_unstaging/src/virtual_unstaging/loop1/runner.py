"""The runner of loop 1: create a run, then optimize its photos with K workers, resumably
(design/loop1.md: Runner). Everything a resumed run needs is read back from the database."""

from __future__ import annotations

import json
import logging
import sqlite3
import time
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from virtual_unstaging import __version__, imaging
from virtual_unstaging.clients.generators import Generator
from virtual_unstaging.clients.http import EndpointError
from virtual_unstaging.domain import (
    Budget,
    Cost,
    DefectType,
    Dimension,
    Evaluation,
    GeneratorCapabilities,
    JudgeRequestOptions,
    ModelRef,
    Point,
    Problem,
    Release,
    Stop,
    canonical_json,
)
from virtual_unstaging.engines import make_engine, replay
from virtual_unstaging.instructions import InstructionStack
from virtual_unstaging.judge import Chat, ContractError, Judge, JudgeImage, JudgeInput, JudgeOutput
from virtual_unstaging.loop1.compile import Guide, PhotoContext, compile_request
from virtual_unstaging.loop1.evidence import inventory_names
from virtual_unstaging.registry import prune
from virtual_unstaging.store import repo
from virtual_unstaging.store.blobs import BlobStore
from virtual_unstaging.store.db import connect, transaction
from virtual_unstaging.tools import ToolBox

log = logging.getLogger(__name__)

# Endpoint failures that pause the whole run (resume later), rather than failing one attempt.
PAUSING = {"endpoint_unreachable", "deadline_reached", "unauthorized", "api_version", "http_error"}


class RunPaused(RuntimeError):
    """An endpoint is unreachable or past its deadline: the run stops, resumable with `run --resume`."""


@dataclass(frozen=True)
class Adapters:
    """The live connections a run needs; everything else comes from the database."""

    db_path: Path
    blobs: BlobStore
    generator: Generator
    chat: Chat
    judge_model: ModelRef
    judge_box_scale: str
    image_part: Callable[[bytes, str], dict[str, object]]
    text_part: Callable[[str], dict[str, object]]
    tools: ToolBox
    use_class_diff: bool
    use_inventory: bool = False
    workers: int = 2
    fixed_settings: tuple[tuple[str, Any], ...] = ()
    judge_request: JudgeRequestOptions = JudgeRequestOptions()  # the judge's speed version; its revision says it


@dataclass(frozen=True)
class RunVersions:
    """What a new run is pinned to: written once into the run row."""

    engine: str
    label: str | None
    budget: Budget
    minor_tolerance: int
    release: Release
    defects: tuple[DefectType, ...]
    generator_stack: InstructionStack
    judge_stack: InstructionStack
    rule_set_id: int


def seed_for(image_sha: str) -> int:
    """Common random numbers (design D5): the seed depends on the photo only, so every engine shares it."""
    return int(image_sha[:8], 16)


def create_run(conn: sqlite3.Connection, adapters: Adapters, versions: RunVersions, photo_names: Sequence[str]) -> int:
    photos = repo.photos(conn, photo_names)
    for photo in photos:
        found = repo.eligibility(conn, photo.photo_id, versions.rule_set_id)
        if found is None:
            raise LookupError(f"{photo.source_name}: no masks for the current rules; run `masks` or `prepare` first")
        if found.decision != "attempt":
            raise LookupError(f"{photo.source_name}: set aside at stage 0 ({found.reason}); leave it out of the run")
    with transaction(conn):
        repo.ensure_defect_types(conn, versions.defects)
        release_id, _ = repo.ensure_release(conn, versions.release)
        gen = adapters.generator
        gen_model = repo.ensure_model(conn, "generator", gen.model.name, gen.model.revision)
        judge_model = repo.ensure_model(conn, "judge", adapters.judge_model.name, adapters.judge_model.revision)
        gen_instr = _ensure_stack(conn, versions.generator_stack)
        judge_instr = _ensure_stack(conn, versions.judge_stack)
        caps = gen.capabilities
        run_id = repo.create_run(
            conn,
            label=versions.label,
            engine=versions.engine,
            engine_config_json=canonical_json({}),
            budget_json=canonical_json(asdict(versions.budget)),
            minor_tolerance=versions.minor_tolerance,
            generator_model_id=gen_model,
            generator_capabilities_json=canonical_json(
                {"roles": sorted(caps.roles), "max_images": caps.max_images, "native_mask": caps.native_mask}
            ),
            judge_model_id=judge_model,
            generator_instructions_id=gen_instr,
            judge_instructions_id=judge_instr,
            registry_release_id=release_id,
            rule_set_id=versions.rule_set_id,
            code_version=__version__,
        )
        for photo in photos:
            repo.create_optimization(conn, run_id, photo.photo_id, seed_for(photo.image_sha256))
    return run_id


def _ensure_stack(conn: sqlite3.Connection, stack: InstructionStack) -> int:
    base_id = repo.ensure_instruction_set(conn, stack.role, stack.target_model, "base", stack.base, None)
    if stack.overlay and stack.overlay.strip():
        return repo.ensure_instruction_set(conn, stack.role, stack.target_model, "project", stack.overlay, base_id)
    return base_id


def execute_run(adapters: Adapters, run_id: int) -> dict[str, int]:
    """Optimize every photo of the run still running; returns counts by outcome. Raises RunPaused."""
    conn = connect(adapters.db_path)
    run = repo.run_row(conn, run_id)
    gen_name, gen_revision = repo.model_ref(conn, run["generator_model_id"])
    if (gen_name, gen_revision) != (adapters.generator.model.name, adapters.generator.model.revision):
        raise ValueError(f"run {run_id} was made with generator {gen_name}@{gen_revision}; configured is another")
    judge_name, judge_revision = repo.model_ref(conn, run["judge_model_id"])
    if (judge_name, judge_revision) != (adapters.judge_model.name, adapters.judge_model.revision):
        raise ValueError(f"run {run_id} was made with judge {judge_name}@{judge_revision}; configured is another")
    pending = [int(row["optimization_id"]) for row in repo.optimizations(conn, run_id, "running")]
    conn.close()
    outcomes: dict[str, int] = {}
    paused: list[str] = []
    with ThreadPoolExecutor(max_workers=max(1, adapters.workers)) as pool:
        futures = [pool.submit(_optimize_safely, adapters, run_id, opt_id, paused) for opt_id in pending]
        for future in futures:
            outcome = future.result()
            outcomes[outcome] = outcomes.get(outcome, 0) + 1
    conn = connect(adapters.db_path)
    with transaction(conn):
        repo.end_run(conn, run_id)
    conn.close()
    if paused:
        raise RunPaused(paused[0])
    return outcomes


def _optimize_safely(adapters: Adapters, run_id: int, optimization_id: int, paused: list[str]) -> str:
    if paused:
        return "paused"
    conn = connect(adapters.db_path)
    try:
        return Optimization(adapters, conn, run_id, optimization_id).run()
    except RunPaused as error:
        paused.append(str(error))
        return "paused"
    except Exception as error:  # one photo's failure must not stop the others; it is recorded
        log.exception("optimization %s failed", optimization_id)
        with transaction(conn):
            repo.finish_optimization(conn, optimization_id, "failed", "error", f"{type(error).__name__}: {error}")
        return "error"
    finally:
        conn.close()


class Optimization:
    """One engine on one photo."""

    def __init__(self, adapters: Adapters, conn: sqlite3.Connection, run_id: int, optimization_id: int) -> None:
        self.a = adapters
        self.conn = conn
        self.run_row = repo.run_row(conn, run_id)
        self.opt = conn.execute("SELECT * FROM optimization WHERE optimization_id = ?", (optimization_id,)).fetchone()
        self.release = repo.load_release(conn, self.run_row["registry_release_id"])
        caps = json.loads(self.run_row["generator_capabilities_json"])
        self.capabilities = GeneratorCapabilities(frozenset(caps["roles"]), int(caps["max_images"]), bool(caps["native_mask"]))
        self.dimensions: tuple[Dimension, ...] = prune(self.release, self.capabilities)
        self.dimension_ids = repo.release_dimension_ids(conn, self.run_row["registry_release_id"])
        self.budget = Budget(**json.loads(self.run_row["budget_json"]))
        self.minor_tolerance = int(self.run_row["minor_tolerance"])
        self.judge_model_id = int(self.run_row["judge_model_id"])
        self.judge_instr_id = int(self.run_row["judge_instructions_id"])
        base, overlay, target = repo.instruction_layers(conn, self.run_row["generator_instructions_id"])
        self.generator_template = InstructionStack("generator", target, base, overlay).template()
        j_base, j_overlay, j_target = repo.instruction_layers(conn, self.judge_instr_id)
        self.judge = Judge(
            adapters.judge_model, InstructionStack("judge", j_target, j_base, j_overlay), repo.defect_types(conn),
            "per_mille" if adapters.judge_box_scale == "per_mille" else "unit", adapters.image_part, adapters.text_part,
            adapters.judge_request,
        )
        self.context = self._photo_context()

    # --- the loop ----------------------------------------------------------------------------------------------

    def run(self) -> str:
        opt_id = int(self.opt["optimization_id"])
        problem = Problem(
            self.dimensions,
            Point.of({d.key: d.default_ordinal for d in self.dimensions}),
            tuple(s for s in self.release.defect_map if s.dimension in {d.key for d in self.dimensions}),
        )
        engine = make_engine(self.run_row["engine"])
        engine.start(problem)
        history = repo.history(self.conn, opt_id, self.judge_model_id, self.judge_instr_id)
        replay(engine, history, lambda entry: entry.point, self._replayed_evaluation, label=f"optimization {opt_id}: ")
        while True:
            if repo.spent(self.conn, opt_id).exhausts(self.budget):
                return self._finish("budget")
            asked = engine.ask()
            if isinstance(asked, Stop):
                return self._finish(asked.reason)
            attempt_id, output = self._generate(asked)
            evaluation = self._judge(attempt_id, asked, output) if output else None
            engine.tell(asked, evaluation)

    def _replayed_evaluation(self, entry: repo.HistoryEntry) -> Evaluation | None:
        """A stored attempt's evaluation; an attempt never judged by this run's judge is judged now."""
        if not entry.judged and entry.output_sha256 is not None:
            return self._judge(entry.attempt_id, entry.point, entry.output_sha256)
        return self._stored_evaluation(entry.judgment_id, entry.gpu_seconds)

    def _finish(self, reason: str) -> str:
        with transaction(self.conn):
            repo.finish_optimization(self.conn, int(self.opt["optimization_id"]), "done", reason)
        return reason

    # --- one attempt -------------------------------------------------------------------------------------------

    def _generate(self, point: Point) -> tuple[int, str | None]:
        compiled = compile_request(
            point, self.dimensions, self.context, self.generator_template, self.capabilities, dict(self.a.fixed_settings)
        )
        request = compiled.request
        key = request.cache_key(self.a.generator.model)
        output = repo.find_generation(self.conn, key)
        gpu_seconds, cached, error = 0.0, output is not None, None
        if output is None:
            try:
                data, gpu_seconds = self.a.generator.generate(request, self.a.blobs.get)
                output = self._store_image(imaging.normalize_photo(data))
            except EndpointError as failure:
                if failure.code in PAUSING:
                    raise RunPaused(str(failure)) from failure
                error = str(failure)
        levels = {self.dimension_ids[k]: v for k, v in point.as_dict().items()}
        images = [(im.role, im.sha256, tool_run) for im, tool_run in zip(request.images, compiled.image_tool_runs, strict=True)]
        with transaction(self.conn):
            attempt_id = repo.insert_attempt(
                self.conn, int(self.opt["optimization_id"]), request.seed, request.prompt, dict(request.settings), key,
                output, gpu_seconds, cached, error, levels, images,
            )
        return attempt_id, output

    def _judge(self, attempt_id: int, point: Point, candidate: str) -> Evaluation | None:
        original = self.context.original
        region = self._region(point)
        outline = self._tool("outline", [original, region.sha256], {})
        probes = [("change_map", self._tool("change_map", [original, candidate, region.sha256], {}))]
        if self.a.use_class_diff:
            probes.append(("class_diff", self._tool("class_diff", [original, candidate, region.sha256], {})))
        if self.a.use_inventory:
            fixed, movable = inventory_names(self.context.fixed_group, self.context.movable)
            params = {"fixed": fixed, "movable": movable}
            probes.append(("element_inventory", self._tool("element_inventory", [original, candidate, region.sha256], params)))
        images = [
            JudgeImage("the original photo", self.a.blobs.get(original)),
            JudgeImage("the edited candidate", self.a.blobs.get(candidate)),
            JudgeImage("the original with the removal region outlined in magenta", self.a.blobs.get(outline.outputs["image"])),
        ]
        labels = {"heatmap": "a heat map of local colour change outside the removal region, a uniform shift removed (red = changed)",
                  "map": "a map of semantic class changes between original and candidate",
                  "annotated": "the edited candidate with the inventory's elements boxed by status, numbered as in the inventory"}
        for _, row in probes:
            for name, sha in row.outputs.items():
                if name in labels:
                    images.append(JudgeImage(labels[name], self.a.blobs.get(sha)))
        summaries = tuple((name, row.summary) for name, row in probes if row.summary)
        tool_rows = [outline] + [row for _, row in probes]
        judge_input = JudgeInput(
            tuple(images), summaries, self.context.fixed_group, self.context.movable, self._history_lines(attempt_id),
            self.dimensions, point,
        )
        request = self.judge.build(judge_input)
        tool_run_ids = [row.tool_run_id for row in tool_rows]
        cached_id = repo.find_judgment(self.conn, request.request_sha256, self.judge_model_id, self.judge_instr_id)
        if cached_id is not None:
            stored = repo.load_judgment(self.conn, cached_id)
            with transaction(self.conn):
                judgment_id = repo.insert_judgment(
                    self.conn, attempt_id, self.judge_model_id, self.judge_instr_id, stored.raw_response,
                    request.request_sha256, 0.0, True, None, stored.own_verdict, stored.critique, stored.findings,
                    stored.moves, self.dimension_ids, tool_run_ids,
                )
            return self._stored_evaluation(judgment_id, 0.0)
        for _ in range(2):  # one retry on a broken answer
            started = time.monotonic()
            parse_error: str | None
            output: JudgeOutput | None
            try:
                raw = self.a.chat(request.messages, request.schema)
            except EndpointError as failure:
                if failure.code in PAUSING:
                    raise RunPaused(str(failure)) from failure
                raw, parse_error, output = "", f"endpoint error: {failure}", None
            else:
                try:
                    output, parse_error = self.judge.parse(raw, self.dimensions, point), None
                except ContractError as broken:
                    output, parse_error = None, str(broken)
            wall = time.monotonic() - started
            with transaction(self.conn):
                if output is None:
                    repo.insert_judgment(
                        self.conn, attempt_id, self.judge_model_id, self.judge_instr_id, raw, request.request_sha256,
                        wall, False, parse_error, tool_run_ids=tool_run_ids,
                    )
                    continue
                judgment_id = repo.insert_judgment(
                    self.conn, attempt_id, self.judge_model_id, self.judge_instr_id, raw, request.request_sha256, wall,
                    False, None, output.own_verdict, output.critique, output.findings, output.moves,
                    self.dimension_ids, tool_run_ids,
                )
            return self._stored_evaluation(judgment_id, 0.0)
        return None

    def _stored_evaluation(self, judgment_id: int | None, gpu_seconds: float) -> Evaluation | None:
        if judgment_id is None:
            return None
        score = repo.judgment_score(self.conn, judgment_id)
        if score is None:
            return None
        stored = repo.load_judgment(self.conn, judgment_id)
        accepted = score.blocking == 0 and score.minor <= self.minor_tolerance
        return Evaluation(score, accepted, stored.findings, stored.moves, stored.critique, Cost(gpu_seconds, 1))

    def _history_lines(self, current_attempt: int) -> tuple[str, ...]:
        start = Point.of({d.key: d.default_ordinal for d in self.dimensions})
        labels = {d.key: d for d in self.dimensions}
        lines: list[str] = []
        entries = repo.history(self.conn, int(self.opt["optimization_id"]), self.judge_model_id, self.judge_instr_id)
        for entry in entries:
            if entry.attempt_id == current_attempt:
                continue
            changes = ", ".join(
                f"{key} {labels[key].level(old).label} -> {labels[key].level(new).label}"
                for key, (old, new) in start.differences(entry.point).items()
            ) or "the start point"
            if entry.judgment_id is None:
                lines.append(f"attempt {entry.seq} ({changes}): no valid judgment")
                continue
            stored = repo.load_judgment(self.conn, entry.judgment_id)
            found = ", ".join(f"{f.code} ({f.severity})" for f in stored.findings) or "no defect"
            lines.append(f"attempt {entry.seq} ({changes}): {found}")
        return tuple(lines)

    # --- context and tools -------------------------------------------------------------------------------------

    def _region(self, point: Point) -> Guide:
        levels = point.as_dict()
        key = levels.get("mask_extent", -1) if any(d.realizer == "mask_dilation" for d in self.dimensions) else -1
        guide = self.context.removal_masks.get(key) or self.context.removal_masks.get(-1)
        assert guide is not None
        return guide

    def _tool(self, name: str, inputs: list[str], params: dict[str, Any]) -> repo.ToolRunRow:
        version = self.a.tools.version(name)
        key = repo.tool_run_key(name, version, params, inputs)
        found = repo.find_tool_run(self.conn, key)
        if found:
            return found
        try:
            result = self.a.tools.run(name, inputs, params, self.a.blobs.get)
        except EndpointError as failure:
            if failure.code in PAUSING:
                raise RunPaused(str(failure)) from failure
            raise
        outputs = {out: self._store_image(data) for out, data in result.outputs.items()}
        with transaction(self.conn):
            return repo.insert_tool_run(
                self.conn, name, result.version, params, inputs, outputs, result.measures, result.summary, result.gpu_seconds
            )

    def _store_image(self, data: bytes) -> str:
        sha = self.a.blobs.put(data)
        width, height, media_type = imaging.describe(data)
        with transaction(self.conn):
            repo.ensure_image(self.conn, sha, width, height, media_type)
        return sha

    def _photo_context(self) -> PhotoContext:
        rule_set_id = int(self.run_row["rule_set_id"])
        photo = self.conn.execute(
            "SELECT p.photo_id, p.image_sha256, p.group_id, p.source_name FROM photo p WHERE p.photo_id = ?",
            (self.opt["photo_id"],),
        ).fetchone()
        elig = repo.eligibility(self.conn, photo["photo_id"], rule_set_id)
        if elig is None or elig.removal_mask is None:
            raise LookupError(f"{photo['source_name']}: no removal mask")
        fixed_group, movable = repo.rules_for(self.conn, rule_set_id, photo["group_id"])
        masks: dict[int, Guide] = {-1: Guide(elig.removal_mask, None)}
        for dim in self.dimensions:
            if dim.realizer == "mask_dilation":
                for level in dim.levels:
                    row = self._tool("mask_ops", [elig.removal_mask], {"dilation_pct": float(level.realization["dilation_pct"])})
                    masks[level.ordinal] = Guide(row.outputs["mask"], row.tool_run_id)
        protected = Guide(elig.protected_mask, None) if elig.protected_mask else None
        references = self._references(photo["photo_id"], photo["group_id"], rule_set_id)
        visible = elig.measures.get("fixed_visible")
        fixed_visible = tuple(visible) if isinstance(visible, list) else tuple(fixed_group)
        return PhotoContext(
            photo_id=int(photo["photo_id"]),
            original=str(photo["image_sha256"]),
            removal_masks=masks,
            protected_mask=protected,
            references=references,
            movable=tuple(movable),
            fixed_visible=fixed_visible,
            fixed_group=tuple(fixed_group),
            seed=int(self.opt["seed"]),
        )

    def _references(self, photo_id: int, group_id: int | None, rule_set_id: int) -> tuple[str, ...]:
        """Other photos of the same group, the least cluttered first (smallest removal-mask share), then by name."""
        if group_id is None:
            return ()
        rows = self.conn.execute(
            "SELECT p.image_sha256, p.source_name, e.measures_json FROM photo p LEFT JOIN eligibility e "
            "ON e.photo_id = p.photo_id AND e.rule_set_id = ? WHERE p.group_id = ? AND p.photo_id <> ?",
            (rule_set_id, group_id, photo_id),
        ).fetchall()

        def share(row: sqlite3.Row) -> float:
            measures = json.loads(row[2]) if row[2] else {}
            value = measures.get("mask_share")
            return float(value) if isinstance(value, (int, float)) else 1.0

        return tuple(str(r[0]) for r in sorted(rows, key=lambda r: (share(r), r[1])))
