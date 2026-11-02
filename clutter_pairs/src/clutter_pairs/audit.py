"""Audit: every check of the data model (data_model.md, "Checks run by `audit`"), and a pair's lineage.

Requests are recomposed from their recorded parts (P9), bodies rebuilt from their stored form (P8), images checked
against their hashes, the denormalized verdicts recomputed, the values checked against their space versions, each
iteration's numbered regions and their image recomputed from its mask, and every pair's clean and cluttered images
compared outside the mask (P1). An imported scene's import record is checked too: its line in the stored manifest,
its two images, the sizing rule.
"""

from __future__ import annotations

import io
import sqlite3
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Any

import numpy as np
from PIL import Image
from virtual_unstaging import imaging
from virtual_unstaging.domain import sha256_bytes

from clutter_pairs import pairs
from clutter_pairs.compose import (
    ComposeError,
    answer_text,
    canonical,
    compose,
    parse_composer,
    parse_judgment,
    render_assessment,
    render_lesson,
    render_spec,
)
from clutter_pairs.dataset import Dataset
from clutter_pairs.domain import Part, SourceRef
from clutter_pairs.manifest import ManifestError, parse_entry
from clutter_pairs.recorder import hashed_images, rebuild_text
from clutter_pairs.sizing import opaque_rgb, pixel_sha, resized
from clutter_pairs.space import ROOM_TYPE, Space, SpaceError, imported_size, parse_space, subject_spec
from clutter_pairs.store import repo


@dataclass
class AuditResult:
    checked: dict[str, int] = field(default_factory=dict)
    problems: list[str] = field(default_factory=list)

    def count(self, check: str, n: int = 1) -> None:
        self.checked[check] = self.checked.get(check, 0) + n

    @property
    def ok(self) -> bool:
        return not self.problems


@dataclass
class _Known:
    """What the checks look up many times: parsed spaces, the stored image hashes, iteration numbers."""

    conn: sqlite3.Connection
    spaces: dict[int, Space] = field(default_factory=dict)
    images: set[str] = field(default_factory=set)
    numbers: dict[int, int] = field(default_factory=dict)

    def space(self, version: int) -> Space:
        if version not in self.spaces:
            ontology, taxonomy = repo.space_version_files(self.conn, version)
            self.spaces[version] = parse_space(repo.file_content(self.conn, ontology),
                                               repo.file_content(self.conn, taxonomy))
        return self.spaces[version]


def audit(ds: Dataset) -> AuditResult:
    result = AuditResult()
    conn = ds.conn
    known = _Known(conn, images=set(repo.all_image_shas(conn)),
                   numbers={it.id: it.n for it in repo.all_iterations(conn)})
    for check in (_requests, _exchanges, _images, _verdicts, _structure, _values, _imports, _regions, _judgments,
                  _pairs):
        check(conn, ds, result, known)
    return result


def _requests(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """P9: every request recomposes byte for byte, and every part's text is its source's rendering."""
    for call in repo.all_calls(conn):
        result.count("requests recomposed")
        try:
            composer = parse_composer("audited", repo.file_content(conn, call.composer_sha))
            parts = [_part(row) for row in repo.parts_of(conn, call.id)]
            _, sha = canonical(compose(composer, repo.model_by_id(conn, call.model_id), parts))
        except (ComposeError, LookupError, ValueError) as error:
            result.problems.append(f"call {call.id}: does not recompose ({error})")
            continue
        if sha != call.request_sha:
            result.problems.append(f"call {call.id}: recomposed request {sha[:12]} differs from stored {call.request_sha[:12]}")
        for problem in _part_sources(conn, call, composer.renderer, composer.renderer_version, known):
            result.problems.append(f"call {call.id}: {problem}")


def _part(row: repo.PartRow) -> Part:
    source = SourceRef(row.file_sha, row.lesson_id, row.assessment_id, row.call_id, row.setting_name, row.origin)  # type: ignore[arg-type]
    return Part(row.slot, row.source_kind, row.text, row.image_sha, source)  # type: ignore[arg-type]


def _part_sources(conn: sqlite3.Connection, call: repo.CallRow, renderer: str, version: int,
                  known: _Known) -> Iterator[str]:
    for row in repo.parts_of(conn, call.id):
        kind = row.source_kind
        if kind in ("template", "instruction", "schema") and row.text != repo.file_content(conn, row.file_sha or ""):
            yield f"part {row.ordinal} is not its file's text"
        elif kind == "lesson" and row.text != render_lesson(repo.lesson(conn, row.lesson_id or 0)):
            yield f"part {row.ordinal} is not lesson {row.lesson_id}'s rendering"
        elif kind == "call_output":
            source = repo.call(conn, row.call_id or 0)
            if row.text != answer_text(source.answer or ""):
                yield f"part {row.ordinal} is not call {row.call_id}'s answer"
        elif kind == "assessment":
            a = repo.assessment(conn, row.assessment_id or 0)
            if row.text != render_assessment(known.numbers[a.iteration_id], a.kind, a.judgment, a.measures):
                yield f"part {row.ordinal} is not assessment {row.assessment_id}'s rendering"
        elif kind == "spec" and row.text != _spec_text(conn, call, renderer, version, known):
            yield f"part {row.ordinal} is not the loop subject's spec"
        elif kind == "image" and row.image_sha not in known.images:
            yield f"part {row.ordinal}: image {row.image_sha} is not in the store"


def _spec_text(conn: sqlite3.Connection, call: repo.CallRow, renderer: str, version: int, known: _Known) -> str:
    loop = repo.loop(conn, call.loop_run_id)
    if loop.stage == "clean":
        scene = repo.scene(conn, loop.scene_id or 0)
        return render_spec(subject_spec(known.space(scene.space_version_id), "clean", scene.values),
                           renderer, version)
    spec = repo.clutter_spec(conn, loop.clutter_spec_id or 0)
    scene = repo.scene(conn, spec.scene_id)
    space = known.space(scene.space_version_id)
    return render_spec(subject_spec(space, "clutter", scene.values + spec.values, spec.items), renderer, version)


def _exchanges(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """P8: every stored body, rebuilt, hashes to the bytes that went on the wire."""
    for call in repo.all_calls(conn):
        for ordinal, body_text, body_image, wire in repo.exchanges_of(conn, call.id):
            result.count("exchanges rebuilt")
            if body_text is None and body_image is None:
                if wire is not None:
                    result.problems.append(f"call {call.id} exchange {ordinal}: a wire hash without a body")
                continue
            try:
                if body_text is not None:
                    data = rebuild_text(body_text, {sha: ds.blobs.get(sha) for sha in hashed_images(body_text)})
                else:
                    data = ds.blobs.get(body_image or "")
            except (OSError, ValueError, KeyError) as error:
                result.problems.append(f"call {call.id} exchange {ordinal}: cannot rebuild ({error})")
                continue
            if sha256_bytes(data) != wire:
                result.problems.append(f"call {call.id} exchange {ordinal}: the rebuilt body does not match the wire hash")


def _images(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    for sha in repo.all_image_shas(conn):
        result.count("images checked")
        try:
            ds.blobs.get(sha)
        except (OSError, ValueError) as error:
            result.problems.append(f"image {sha}: {error}")


def _verdicts(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """The denormalized verdicts equal the verdict rule applied to the findings; a loop is accepted exactly when one
    of its iterations is."""
    severities = repo.severities(conn)
    for iteration in repo.all_iterations(conn):
        rows = repo.assessments(conn, iteration.id)
        blocking = 0
        for a in rows:
            result.count("assessments checked")
            blocks = sum(1 for f in a.judgment.findings if severities[f.code] == "blocking")
            blocking += blocks
            if a.verdict != ("fail" if blocks else "pass"):
                result.problems.append(f"assessment {a.id}: verdict {a.verdict} does not follow from its findings")
        if iteration.verdict is not None and iteration.verdict != ("revise" if blocking else "accept"):
            result.problems.append(f"iteration {iteration.id}: verdict {iteration.verdict} does not follow from its findings")
    for loop in repo.all_loops(conn):
        result.count("loops checked")
        accepted = any(it.verdict == "accept" for it in repo.iterations(conn, loop.id))
        if (loop.stop_reason == "accepted") != accepted:
            result.problems.append(f"loop {loop.id}: stop reason {loop.stop_reason} but accepted={accepted}")


def _structure(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    for loop_id in repo.loops_with_bad_input(conn):
        result.problems.append(f"loop {loop_id}: its input image is not an accepted clean image of its scene")
    for iteration_id, role in repo.misplaced_image_roles(conn):
        result.problems.append(f"iteration {iteration_id}: image role {role} does not fit its loop's stage")
    for iteration_id in repo.misplaced_import_actions(conn):
        result.problems.append(f"iteration {iteration_id}: the action `import` belongs to the clean loop of an "
                               "imported scene, and to nothing else")
    result.problems.extend(repo.export_problems(conn))


def _values(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """Every owner holds one value for every axis of its kind, declared by its building's space version; the room and
    scene of an imported image hold the values its manifest gave, the room type at least (design/imports.md, I2)."""
    axes = repo.axes_by_kind(conn)
    declared = repo.space_values(conn)
    imported = repo.imported_owners(conn)
    held: dict[tuple[str, int], set[str]] = {}
    for kind, owner, version, axis, value in repo.owner_values(conn):
        held.setdefault((kind, owner), set()).add(axis)
        if (version, axis, value) not in declared:
            result.problems.append(f"{kind} {owner}: {axis}={value} is not declared by space version {version}")
    for kind, owner in repo.owners(conn):
        result.count("owners checked")
        version_axes = set(known.space(repo.owner_space_version(conn, kind, owner)).axes_for(kind))  # type: ignore[arg-type]
        required = version_axes & {ROOM_TYPE} if (kind, owner) in imported else version_axes
        missing = required - held.get((kind, owner), set())
        extra = held.get((kind, owner), set()) - axes.get(kind, set())
        if missing or extra:
            result.problems.append(f"{kind} {owner}: missing axes {sorted(missing)}, foreign axes {sorted(extra)}")


def _imports(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """Every imported image has its line in the stored manifest (and its scene's values, source, group and origin are
    that line's), its images in the image store, the hash of its decoded pixels, and a clean image equal, pixel for
    pixel, to its original resized again with the sizing parameters its import set recorded; the scenes of one room
    share one group and one source; the judged image of each imported iteration is the recorded one."""
    for room in repo.badly_grouped_rooms(conn):
        result.problems.append(f"room {room}: its imported scenes do not share one group and one source")
    for iteration_id in repo.misplaced_imported_iteration_images(conn):
        result.problems.append(f"iteration {iteration_id}: the image it judged is not the one its scene's import recorded")
    for iteration_id in repo.accepted_clutter_iterations_without_pair(conn):
        result.problems.append(f"iteration {iteration_id}: accepted, but it is not a pair (an image or a link is missing)")
    for row in repo.imported_images(conn):
        result.count("imports checked")
        who = f"scene {row.scene_id}"
        scene = repo.scene(conn, row.scene_id)
        lines = repo.import_manifest(conn, row.import_set_id).splitlines()
        if row.line > len(lines) or not lines[row.line - 1].strip():
            result.problems.append(f"{who}: line {row.line} is not in the stored manifest of import set {row.import_set_id}")
        else:
            try:
                entry = parse_entry(row.line, lines[row.line - 1], known.space(scene.space_version_id))
            except ManifestError as error:
                result.problems.append(f"{who}: its manifest line does not parse ({error})")
            else:
                given = {ROOM_TYPE: entry.room_type, **dict(entry.values)}
                if (dict(scene.values) != given or repo.model_by_id(conn, row.source_model_id) != entry.source
                        or row.origin != entry.origin or row.group_name != entry.group):
                    result.problems.append(f"{who}: its values, source, group or origin differ from line {row.line} "
                                           "of its manifest")
        if row.original_sha not in known.images or row.image_sha not in known.images:
            result.problems.append(f"{who}: an image of its import record is not in the image store")
            continue
        problem = _import_image_problem(conn, ds, row)
        if problem:
            result.problems.append(f"{who}: {problem}")


def _import_image_problem(conn: sqlite3.Connection, ds: Dataset, row: repo.ImportedRow) -> str | None:
    """Why the clean image is not its original made again (pixel hash, sizing rule, resize), or None."""
    params = repo.import_set(conn, row.import_set_id)
    try:
        original = opaque_rgb(imaging.decode(ds.blobs.get(row.original_sha)))
        expected = imported_size(original.size, params.output_side, params.size_multiple, params.condition_max_pixels)
        again = np.asarray(resized(original, expected, params.resampler))
        stored = np.asarray(imaging.decode(ds.blobs.get(row.image_sha)).convert("RGB"))
    except (OSError, ValueError, SpaceError) as error:
        return f"the import cannot be made again from its original ({error})"
    if pixel_sha(original) != row.pixel_sha:
        return "the hash of its original's pixels is not the recorded one"
    if repo.image_size(conn, row.image_sha) != expected or stored.shape != again.shape:
        return f"its image is {repo.image_size(conn, row.image_sha)}, the sizing rule gives {expected} for its original"
    # a resize is deterministic for one Pillow; one level of slack keeps an upgrade of it from failing every import
    if int(np.abs(stored.astype(np.int16) - again.astype(np.int16)).max()) > 1:
        return "its image is not its original resized again with the recorded parameters"
    return None


def _regions(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """Every clutter iteration the pair judge was called on has a region set and a regions image; its regions
    recompute from its change mask with the region set's thresholds, the image redraws pixel for pixel from its
    composite, and its explained-change assessment equals the test run again on the judge's region answers (A2)."""
    for iteration_id in repo.pair_judged_iterations(conn):
        result.count("regions checked")
        stored = repo.region_set(conn, iteration_id)
        images = repo.iteration_images(conn, iteration_id)
        if stored is None or not {"change_mask", "composite", "regions"} <= set(images):
            result.problems.append(f"iteration {iteration_id}: judged without a region set and its images")
            continue
        params, speck_px = stored
        if params["drawing"] != pairs.REGION_DRAWING:
            result.problems.append(f"iteration {iteration_id}: regions drawn by version {params['drawing']}, "
                                   f"this code draws version {pairs.REGION_DRAWING}")
            continue
        t = pairs.Thresholds.of({k: v for k, v in params.items() if k != "drawing"})
        alpha = np.asarray(Image.open(io.BytesIO(ds.blobs.get(images["change_mask"]))).convert("L"))
        found = pairs.regions(alpha == 255, t)
        if ([(r.n, r.box, r.px) for r in found.numbered] != repo.mask_regions(conn, iteration_id)
                or found.speck_px != speck_px):
            result.problems.append(f"iteration {iteration_id}: its regions do not recompute from its mask")
            continue
        cluttered = np.asarray(imaging.decode(ds.blobs.get(images["composite"])).convert("RGB"))
        drawn = np.asarray(imaging.decode(ds.blobs.get(images["regions"])).convert("RGB"))
        if not np.array_equal(pairs.draw_regions(cluttered, found, t), drawn):
            result.problems.append(f"iteration {iteration_id}: its regions image does not redraw from its composite")
        rows = repo.assessments(conn, iteration_id)
        judged = [a for a in rows if a.kind == "judge"]
        explained = [a for a in rows if a.kind == "pixel" and any(m.name == "unexplained_share" for m in a.measures)]
        if judged and explained:
            items = len(_spec_of(conn, iteration_id).item_ids)
            again = pairs.explain(found, judged[0].judgment.regions, items, pairs.Thresholds.of(explained[0].thresholds))
            if (again.findings != explained[0].judgment.findings
                    or [(m.name, m.value) for m in again.measures] != [(m.name, m.value) for m in explained[0].measures]):
                result.problems.append(f"iteration {iteration_id}: its explained-change assessment does not recompute")


def _judgments(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """Every judge assessment equals its call's stored answer parsed again: findings (the derived opening_changed
    among them), guidance, region answers."""
    for assessment_id in repo.all_assessment_ids(conn):
        a = repo.assessment(conn, assessment_id)
        if a.kind != "judge" or a.model_call_id is None:
            continue
        result.count("judgments parsed again")
        call = repo.call(conn, a.model_call_id)
        stage = repo.loop(conn, call.loop_run_id).stage
        items = len(_spec_of(conn, a.iteration_id).item_ids) if stage == "clutter" else 0
        regions = len(repo.mask_regions(conn, a.iteration_id)) if stage == "clutter" else 0
        try:
            again = parse_judgment(call.answer or "", stage, items, ds.judge_codes(stage), regions)
        except ComposeError as error:
            result.problems.append(f"assessment {assessment_id}: its call's answer no longer parses: {error}")
            continue
        if again != a.judgment:
            result.problems.append(f"assessment {assessment_id}: it is not its call's answer parsed again")


def _spec_of(conn: sqlite3.Connection, iteration_id: int) -> repo.SpecRow:
    loop = repo.loop(conn, repo.loop_of_iteration(conn, iteration_id))
    return repo.clutter_spec(conn, loop.clutter_spec_id or 0)


def _pairs(conn: sqlite3.Connection, ds: Dataset, result: AuditResult, known: _Known) -> None:
    """P1: clean and cluttered images are equal wherever the mask's alpha is 0."""
    for pair in repo.query(conn, "pair"):
        result.count("pairs compared")
        clean = np.asarray(imaging.decode(ds.blobs.get(str(pair["clean_image"]))).convert("RGB"))
        cluttered = np.asarray(imaging.decode(ds.blobs.get(str(pair["cluttered_image"]))).convert("RGB"))
        alpha = np.asarray(Image.open(io.BytesIO(ds.blobs.get(str(pair["mask_image"])))).convert("L"))
        if clean.shape != cluttered.shape or alpha.shape != clean.shape[:2]:
            result.problems.append(f"pair {pair['pair_id']}: images of different sizes")
            continue
        outside = alpha == 0
        if not np.array_equal(clean[outside], cluttered[outside]):
            changed = int((clean[outside] != cluttered[outside]).any(axis=-1).sum())
            result.problems.append(f"pair {pair['pair_id']}: {changed} pixels differ where the mask is 0")


# --- Lineage -----------------------------------------------------------------------------------------------------


def lineage(conn: sqlite3.Connection, pair_id: int) -> dict[str, Any]:
    """From a pair to every iteration, call, part and exchange behind it, and each part's origin, recursively."""
    pair = next((p for p in repo.query(conn, "pair") if p["pair_id"] == pair_id), None)
    if pair is None:
        raise LookupError(f"no accepted pair {pair_id}")
    clean_loop = repo.find_loop(conn, "clean", int(pair["scene_id"]))  # type: ignore[call-overload]
    imported = repo.imported_image(conn, int(pair["scene_id"]))  # type: ignore[call-overload]
    source = None if imported is None else repo.model_by_id(conn, imported.source_model_id)
    return {
        "pair": pair_id,
        "building": pair["building_id"], "room": pair["room_id"], "scene": pair["scene_id"],
        "clutter_spec": pair["clutter_spec_id"],
        "import": None if imported is None or source is None else {
            "import_set": imported.import_set_id, "line": imported.line, "original": imported.original_sha,
            "origin": imported.origin, "group": imported.group_name, "source": f"{source.name}@{source.revision}", "family": source.family,
            "licence": source.licence},
        "images": {"clean": pair["clean_image"], "cluttered": pair["cluttered_image"], "mask": pair["mask_image"]},
        "clutter_loop": _loop_tree(conn, int(pair["loop_run_id"])),  # type: ignore[call-overload]
        "clean_loop": None if clean_loop is None else _loop_tree(conn, clean_loop.id),
    }


def _loop_tree(conn: sqlite3.Connection, loop_id: int) -> dict[str, Any]:
    loop = repo.loop(conn, loop_id)
    calls = repo.calls_of_loop(conn, loop_id)
    return {
        "loop": loop.id, "stage": loop.stage, "wave": loop.wave_id, "arm": loop.lessons_arm, "engine": loop.engine,
        "stop_reason": loop.stop_reason,
        "iterations": [{
            "n": it.n, "action": it.action, "seed": it.seed, "verdict": it.verdict,
            "images": repo.iteration_images(conn, it.id),
            "assessments": [{"id": a.id, "kind": a.kind, "verdict": a.verdict, "call": a.model_call_id,
                             "findings": [f.code for f in a.judgment.findings],
                             "measures": {m.name: m.value for m in a.measures}}
                            for a in repo.assessments(conn, it.id)],
            "calls": [_call_tree(conn, c) for c in calls if c.iteration_id == it.id],
        } for it in repo.iterations(conn, loop_id)],
        "after_loop": [_call_tree(conn, c) for c in calls if c.iteration_id is None],
    }


def _call_tree(conn: sqlite3.Connection, call: repo.CallRow) -> dict[str, Any]:
    model = repo.model_by_id(conn, call.model_id)
    return {
        "call": call.id, "role": call.role, "model": f"{model.name}@{model.revision}", "family": model.family,
        "composer": call.composer_sha, "request": call.request_sha, "reused_call": call.reused_call_id,
        "error": call.error_code, "output_image": call.output_image,
        "parts": [{"ordinal": p.ordinal, "slot": p.slot, "kind": p.source_kind,
                   "source": {k: v for k, v in (("file", p.file_sha), ("lesson", p.lesson_id),
                                                ("assessment", p.assessment_id), ("call", p.call_id),
                                                ("image", p.image_sha), ("setting", p.setting_name),
                                                ("origin", p.origin)) if v is not None}}
                  for p in repo.parts_of(conn, call.id)],
        "exchanges": len(repo.exchanges_of(conn, call.id)),
    }

