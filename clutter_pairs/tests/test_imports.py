"""Imported clean images (design/imports.md): the manifest, the import, the judge-only clean loop, the views, the
audit, replay and the export, on generated images and the stand-in models."""

from __future__ import annotations

import io
import json
import sqlite3
from collections.abc import Callable
from pathlib import Path

import numpy as np
import pytest
from conftest import write_config
from helpers import make_import_set, run_imports
from PIL import Image
from virtual_unstaging import imaging
from virtual_unstaging.domain import sha256_bytes
from virtual_unstaging.serve.images import output_size

from clutter_pairs import audit, config, export, importer, run
from clutter_pairs.cli import EXIT_FAILURE, EXIT_OK, main
from clutter_pairs.config import ConfigError
from clutter_pairs.dataset import Dataset, open_dataset
from clutter_pairs.domain import ModelId
from clutter_pairs.fakes import FakeBehaviour, FakeModelServer
from clutter_pairs.manifest import ManifestError, parse_manifest
from clutter_pairs.space import SpaceError, imported_size, sample_clutter_specs, size_problem
from clutter_pairs.store import repo

SOURCE = ModelId("render-tool", "1.0", "procedural", "MIT")
SET = [("a.png", "kitchen", True), ("b.png", "bedroom", True), ("c.png", "living_room", False)]


@pytest.fixture
def import_set(folder: Path, server: FakeModelServer) -> Path:
    write_config(folder, server, pair_target=50)
    return make_import_set(folder / "import_set", SET)


def _line(**changes: object) -> str:
    line: dict[str, object] = {"file": "a.png", "room_type": "kitchen",
                               "source": {"name": "n", "revision": "1", "family": "f", "licence": "MIT"}}
    return json.dumps({**line, **changes})


# --- The manifest ----------------------------------------------------------------------------------------------


def test_a_manifest_line_gives_a_typed_entry(folder: Path) -> None:
    space = open_dataset(folder).space
    text = _line(values={"style": "modern", "light": "overcast"}, origin="seed 7") + "\n\n" + _line(file="b.png")
    first, second = parse_manifest(text, space)
    assert (first.line, first.file, first.room_type, first.origin) == (1, "a.png", "kitchen", "seed 7")
    assert first.values == (("light", "overcast"), ("style", "modern"))
    assert first.source == ModelId("n", "1", "f", "MIT")
    assert (second.line, second.values, second.origin) == (3, (), None)


@pytest.mark.parametrize("text, message", [
    ("not json", "not JSON"),
    (_line(room_type="castle"), "not declared"),
    (_line(extra=1), "unknown keys"),
    (_line(source={"name": "n"}), "source must be an object"),
    (_line(values={"room_type": "kitchen"}), "key of the line"),
    (_line(values={"density": "lived_in"}), "room or scene axes"),
    (_line(values={"style": "gothic"}), "not declared"),
    (_line(file="/etc/passwd"), "relative path"),
    (_line(file="../a.png"), "relative path"),
    (_line(origin=3), "origin must be a text"),
    (_line() + "\n" + _line(), "already listed on line 1"),
    ("\n \n", "lists no image"),
])
def test_a_manifest_off_its_contract_is_refused_with_its_line(folder: Path, text: str, message: str) -> None:
    with pytest.raises(ManifestError, match=message):
        parse_manifest(text, open_dataset(folder).space)


# --- The import ------------------------------------------------------------------------------------------------


def test_an_import_makes_a_building_room_scene_and_k_specs_per_image(folder: Path, import_set: Path) -> None:
    make_import_set(import_set, SET, extra={"a.png": {"values": {"style": "modern", "light": "overcast"}}})
    ds = open_dataset(folder)
    summary = importer.import_folder(ds, import_set)
    assert (summary.scenes, summary.specs, summary.skipped) == (3, 9, ())
    count = {t: ds.conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
             for t in ("building", "room", "scene", "clutter_spec", "imported_image", "import_set")}
    assert count == {"building": 3, "room": 3, "scene": 3, "clutter_spec": 9, "imported_image": 3, "import_set": 1}
    first = repo.scene(ds.conn, 1)  # scenes follow the manifest's order
    assert dict(first.values) == {"room_type": "kitchen", "style": "modern", "light": "overcast"}
    assert dict(repo.scene(ds.conn, 2).values) == {"room_type": "bedroom"}  # values only where given (I2)
    assert {spec.variant for spec in repo.clutter_specs(ds.conn, 2)} == {1, 2, 3}
    row = repo.imported_image(ds.conn, 1)
    assert row is not None and row.origin == "seed 0" and row.line == 1
    assert repo.model_by_id(ds.conn, row.source_model_id) == SOURCE
    assert ds.conn.execute("SELECT kind FROM source_file WHERE sha256 = (SELECT manifest_sha FROM import_set)"
                           ).fetchone()[0] == "import_manifest"
    assert audit.audit(ds).ok


def test_an_import_resizes_to_the_editor_size_and_keeps_the_original(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    row = repo.imported_image(ds.conn, 1)
    assert row is not None
    original = (import_set / "a.png").read_bytes()
    assert row.original_sha == sha256_bytes(original) and ds.blobs.get(row.original_sha) == original
    assert repo.image_size(ds.conn, row.original_sha) == (400, 300)
    expected = output_size((400, 300), ds.cfg.run.output_side, ds.cfg.generator.size_multiple)
    assert repo.image_size(ds.conn, row.image_sha) == expected == imaging.decode(ds.blobs.get(row.image_sha)).size
    assert output_size(expected, ds.cfg.run.output_side, ds.cfg.generator.size_multiple) == expected  # I3: edit = clean


def test_an_image_the_editor_would_return_at_another_size_is_refused_with_every_other_problem(
        folder: Path, import_set: Path) -> None:
    make_import_set(import_set / "odd", [("odd.png", "kitchen", True)], size=(360, 200))
    (import_set / "odd" / "manifest.jsonl").write_text(
        (import_set / "odd" / "manifest.jsonl").read_text() + _line(file="missing.png") + "\n")
    ds = open_dataset(folder)
    with pytest.raises(ManifestError) as error:
        importer.import_folder(ds, import_set / "odd")
    message = str(error.value)
    assert "nothing imported" in message and "line 1 (odd.png)" in message and "line 2 (missing.png)" in message
    assert repo.scene_count(ds.conn) == 0 and repo.imported_hashes(ds.conn) == (set(), set(), set())


def test_the_sizing_rule_refuses_the_editors_limit_and_a_size_that_does_not_come_back() -> None:
    assert imported_size((1280, 720), 1024, 32, 1_048_576) == (1344, 768)
    with pytest.raises(SpaceError, match="condition-image limit"):
        imported_size((1280, 720), 1024, 32, 1_000_000)
    with pytest.raises(SpaceError, match="return it at 352x160"):
        imported_size((360, 200), 256, 32, 1_048_576)


def test_importing_again_skips_what_is_already_in_the_dataset(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    again = importer.import_folder(ds, import_set)
    assert (again.import_set_id, again.scenes, again.skipped) == (None, 0, ("a.png", "b.png", "c.png"))
    assert repo.scene_count(ds.conn) == 3
    more = make_import_set(import_set / "more", [("a_copy.png", "kitchen", True), ("new.png", "kitchen", True)],
                           indices=[0, 10])  # the first has the bytes of a.png under another name
    mixed = importer.import_folder(ds, more)
    assert (mixed.scenes, mixed.skipped) == (1, ("a_copy.png",))
    assert repo.scene_count(ds.conn) == 4


def test_a_source_name_with_two_licences_is_refused(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    other = make_import_set(import_set / "other", [("x.png", "kitchen", True)], indices=[20],
                            source={"name": "render-tool", "revision": "1.0", "family": "procedural", "licence": "CC0"})
    with pytest.raises(ManifestError, match="one source name per licence"):
        importer.import_folder(ds, other)
    assert repo.scene_count(ds.conn) == 3


def test_the_planning_of_specs_is_shared_with_the_planner(folder: Path) -> None:
    space = open_dataset(folder).space
    cell = {"density": "cluttered"}
    specs = sample_clutter_specs(space, "kitchen", 11, 3, cell)
    assert [values["density"] for _, _, values, _ in specs] == ["cluttered", "lived_in", "moving_day"]
    assert specs == sample_clutter_specs(space, "kitchen", 11, 3, cell)  # seeded: the same draws again


# --- The clean loop of an imported scene -----------------------------------------------------------------------


def test_an_imported_scene_is_judged_once_without_generation_and_feeds_the_clutter_loops(
        folder: Path, import_set: Path) -> None:
    ds, summary = run_imports(folder, import_set)
    assert summary.stopped == "nothing_left"
    accepted = [r for r in repo.imported_images(ds.conn) if repo.accepted_clean_image(ds.conn, r.scene_id)]
    assert len(accepted) == 2
    for row in accepted:
        loop = repo.find_loop(ds.conn, "clean", row.scene_id)
        assert loop is not None and (loop.stop_reason, loop.lessons_arm, loop.max_iterations) == ("accepted", "off", 1)
        assert loop.engine == "import@1+one_iteration@1"
        (iteration,) = repo.iterations(ds.conn, loop.id)
        assert (iteration.action, iteration.verdict) == ("import", "accept")
        assert repo.iteration_images(ds.conn, iteration.id) == {"imported": row.image_sha}
        assert [c.role for c in repo.calls_of_loop(ds.conn, loop.id)] == ["judge"]  # no write, no generate, no distill
        assert repo.accepted_clean_image(ds.conn, row.scene_id) == row.image_sha
        assert [r[0] for r in ds.conn.execute("SELECT stop_reason FROM loop_run WHERE clutter_spec_id IN"
                                              " (SELECT id FROM clutter_spec WHERE scene_id = ?)", (row.scene_id,))
                ] == ["accepted"] * 3
    pairs = repo.query(ds.conn, "pair")
    assert len(pairs) == 6 and {p["clean_family"] for p in pairs} == {"procedural"}  # the source's, from the view
    assert {p["editor_family"] for p in pairs} == {"flux2"}
    assert {p["clean_image"] for p in pairs} == {r.image_sha for r in accepted}  # the resized image is the clean image
    assert audit.audit(ds).ok


def test_a_rejected_import_stops_after_its_one_iteration_and_plans_no_more_work(folder: Path, import_set: Path) -> None:
    ds, summary = run_imports(folder, import_set)
    rejected = repo.imported_images(ds.conn)[2]
    loop = repo.find_loop(ds.conn, "clean", rejected.scene_id)
    assert loop is not None and loop.stop_reason == "max_iterations"
    assert len(repo.iterations(ds.conn, loop.id)) == 1
    assert repo.accepted_clean_image(ds.conn, rejected.scene_id) is None
    assert all(repo.find_loop(ds.conn, "clutter", s.id) is None for s in repo.clutter_specs(ds.conn, rejected.scene_id))
    assert summary.loops["clean:max_iterations"] == 1 and summary.loops["clean:accepted"] == 2
    assert repo.wave_scenes(ds.conn, 10) == []  # nothing left to do: a rejected import is not retried
    assert audit.audit(ds).ok


def test_the_clean_loop_of_an_imported_scene_is_left_out_of_the_carry_forward_comparison(
        folder: Path, import_set: Path) -> None:
    ds, _ = run_imports(folder, import_set)
    with ds.conn:  # a lesson in each stage from wave 1 on switches the comparison's view on
        for stage in ("clean", "clutter"):
            ds.conn.execute("INSERT INTO lesson (stage, text_sha, distill_call_id, active_from_wave_id)"
                            " SELECT ?, request_sha, id, 1 FROM model_call LIMIT 1", (stage,))
    finished = [r for r in repo.query(ds.conn, "iteration_curve") if r["stage"] == "clean" and r["stop_reason"]]
    assert len(finished) == 3  # three finished clean loops, all of imported scenes ...
    assert {r["stage"] for r in repo.query(ds.conn, "carry_forward_loop")} == {"clutter"}  # ... none compared


def test_imported_pairs_count_only_in_the_cells_their_values_name(folder: Path, import_set: Path) -> None:
    (folder / "my_targets.toml").write_text('[[target]]\npairs = 6\nroom_type = "kitchen"\n\n'
                                            '[[target]]\npairs = 3\nroom_type = "kitchen"\nstyle = "modern"\n\n'
                                            '[[target]]\npairs = 3\nroom_type = "bedroom"\nstyle = "modern"\n')
    text = (folder / config.CONFIG_NAME).read_text().replace(
        "[files]", '[files]\n"space/targets.toml" = "my_targets.toml"', 1)
    (folder / config.CONFIG_NAME).write_text(text)
    make_import_set(import_set, [("a.png", "kitchen", True), ("b.png", "kitchen", True), ("c.png", "bedroom", True)],
                    extra={"a.png": {"values": {"style": "modern"}}})
    ds, _ = run_imports(folder, import_set)
    by_cell = {tuple(sorted(repo.target_values(ds.conn, int(r["target_id"])))): int(r["accepted"])  # type: ignore[call-overload]
               for r in repo.query(ds.conn, "coverage")}
    assert by_cell == {(("room_type", "kitchen"),): 6,
                       (("room_type", "kitchen"), ("style", "modern")): 3,  # only the kitchen that names its style
                       (("room_type", "bedroom"), ("style", "modern")): 0}  # a bedroom that does not name one


def test_a_paused_import_run_resumes_where_it_stopped(folder: Path, import_set: Path, behaviour: FakeBehaviour) -> None:
    behaviour.down_after = 7
    with pytest.raises(run.RunPaused):
        run_imports(folder, import_set)
    behaviour.down_after = None
    ds = open_dataset(folder)
    summary = run.execute(ds, run.connect_models(ds, retries=0), config.thresholds(ds.cfg, {}), run.RunOptions())
    assert summary.pairs == 6 and audit.audit(ds).ok
    seen = set()
    for call in repo.all_calls(ds.conn):
        if call.reused_call_id is None and call.error_code is None:
            key = (call.loop_run_id, call.iteration_id, call.role)
            assert key not in seen, f"a step was called twice: {key}"
            seen.add(key)


def test_p2_a_finished_run_over_imported_scenes_started_again_makes_no_model_call(
        folder: Path, import_set: Path) -> None:
    ds, _ = run_imports(folder, import_set)
    calls = repo.actual_call_count(ds.conn)
    before = [(p["clean_image"], p["cluttered_image"]) for p in repo.query(ds.conn, "pair")]
    verdicts = [(it.id, it.verdict) for it in repo.all_iterations(ds.conn)]
    with ds.conn:
        ds.conn.execute("UPDATE loop_run SET stop_reason = NULL")
        wave = repo.create_wave(ds.conn, repo.create_run(ds.conn, ds.config_sha, ds.target_set_id, 99, None, "now"),
                                False, "now")
    work = run.SceneWork(ds, ds.conn, run.connect_models(ds, retries=0), config.thresholds(ds.cfg, {}),
                         run.RunOptions(), wave)
    for scene in range(1, repo.scene_count(ds.conn) + 1):  # the accepted and the rejected import alike
        work.run(scene)
    assert repo.actual_call_count(ds.conn) == calls
    assert [(p["clean_image"], p["cluttered_image"]) for p in repo.query(ds.conn, "pair")] == before
    assert [(it.id, it.verdict) for it in repo.all_iterations(ds.conn)] == verdicts
    assert audit.audit(ds).ok


# --- The audit and the export ----------------------------------------------------------------------------------


def _tamper(ds: Dataset, statement: str, parameters: tuple[object, ...], expected: str, undo: Callable[[], None]) -> None:
    with ds.conn:
        ds.conn.execute(statement, parameters)
    problems = audit.audit(ds).problems
    assert any(expected in p for p in problems), problems
    undo()
    assert audit.audit(ds).ok


def test_the_audit_checks_the_import_record_of_every_imported_scene(folder: Path, import_set: Path) -> None:
    ds, _ = run_imports(folder, import_set)
    result = audit.audit(ds)
    assert result.ok, result.problems
    assert result.checked["imports checked"] == 3  # a room that names no style passes: only room_type is required (I2)
    row = repo.imported_image(ds.conn, 1)
    assert row is not None

    def restore(statement: str, value: object) -> Callable[[], None]:
        def undo() -> None:
            with ds.conn:
                ds.conn.execute(statement, (value,))
        return undo

    manifest = ds.conn.execute("SELECT sha256, content FROM source_file WHERE kind = 'import_manifest'").fetchone()
    _tamper(ds, "UPDATE source_file SET content = replace(content, 'seed 0', 'seed 99') WHERE sha256 = ?", (manifest[0],),
            "differ from line 1", restore_manifest := (lambda: _set_content(ds, manifest[0], manifest[1])))
    assert restore_manifest is not None
    _tamper(ds, "UPDATE imported_image SET line = 9 WHERE scene_id = 1", (), "is not in the stored manifest",
            restore("UPDATE imported_image SET line = 1 WHERE scene_id = ?", 1))
    _tamper(ds, "UPDATE imported_image SET origin = 'elsewhere' WHERE scene_id = 1", (), "differ from line 1",
            restore("UPDATE imported_image SET origin = 'seed 0' WHERE scene_id = ?", 1))
    _tamper(ds, "UPDATE image SET height = height + 32 WHERE sha256 = ?", (row.image_sha,), "the sizing rule gives",
            restore("UPDATE image SET height = height - 32 WHERE sha256 = ?", row.image_sha))
    _tamper(ds, "DELETE FROM room_value WHERE axis = 'room_type' AND room_id = (SELECT room_id FROM scene WHERE id = 1)",
            (), "missing axes", lambda: _put_back_room_type(ds))
    iteration = ds.conn.execute("SELECT id FROM iteration WHERE loop_run_id = (SELECT id FROM loop_run WHERE scene_id = 1)"
                                ).fetchone()[0]
    _tamper(ds, "UPDATE iteration SET action = 'write' WHERE id = ?", (iteration,), "belongs to the clean loop",
            restore("UPDATE iteration SET action = 'import' WHERE id = ?", iteration))
    _tamper(ds, "UPDATE iteration_image SET role = 'generated' WHERE iteration_id = ?", (iteration,),
            "does not fit its loop's stage", restore("UPDATE iteration_image SET role = 'imported' WHERE iteration_id = ?",
                                                      iteration))


def _set_content(ds: Dataset, sha: str, content: str) -> None:
    with ds.conn:
        ds.conn.execute("UPDATE source_file SET content = ? WHERE sha256 = ?", (content, sha))


def _put_back_room_type(ds: Dataset) -> None:
    with ds.conn:
        ds.conn.execute("INSERT INTO room_value (room_id, axis, value) VALUES ((SELECT room_id FROM scene WHERE id = 1),"
                        " 'room_type', 'kitchen')")


def test_a_pairs_lineage_names_its_import(folder: Path, import_set: Path) -> None:
    ds, _ = run_imports(folder, import_set)
    pair = repo.query(ds.conn, "pair")[0]
    scene = int(pair["scene_id"])  # type: ignore[call-overload]
    row = repo.imported_image(ds.conn, scene)
    assert row is not None
    lineage = audit.lineage(ds.conn, int(pair["pair_id"]))  # type: ignore[call-overload]
    assert lineage["import"] == {"import_set": 1, "line": scene, "original": row.original_sha, "origin": f"seed {scene - 1}", "group": None,
                                 "source": "render-tool@1.0", "family": "procedural", "licence": "MIT"}
    assert [i["action"] for i in lineage["clean_loop"]["iterations"]] == ["import"]


def test_an_export_names_the_import_as_the_clean_model_of_its_pairs(folder: Path, import_set: Path) -> None:
    ds, summary = run_imports(folder, import_set)
    target, count = export.export(ds, "v1")
    lines = [json.loads(line) for line in (target / "manifest.jsonl").read_text().splitlines()]
    assert count == summary.pairs == len(lines) == 6
    assert {json.dumps(line["models"]["clean"], sort_keys=True) for line in lines} == {
        json.dumps({"family": "procedural", "licence": "MIT", "name": "render-tool", "revision": "1.0"}, sort_keys=True)}
    split_of: dict[str, str] = {}
    for line in lines:
        assert split_of.setdefault(line["building"], line["split"]) == line["split"]  # P6: one split per building
        assert (target / line["clean"]).is_file()
        assert set(line["values"]) == {"room_type", "density"}  # no style, no light: the manifest gave none (I2)
    assert audit.audit(ds).ok


# --- The command line ------------------------------------------------------------------------------------------


def test_the_import_command_reports_counts_and_refuses_a_bad_manifest(
        folder: Path, import_set: Path, capsys: pytest.CaptureFixture[str]) -> None:
    base = ["--dataset", str(folder)]
    assert main([*base, "import", str(import_set), "--json"]) == EXIT_OK
    out = json.loads(capsys.readouterr().out)
    assert (out["scenes_imported"], out["buildings"], out["clutter_specs"], out["skipped"], out["scenes"]) == (3, 3, 9, [], 3)
    assert main([*base, "import", str(import_set)]) == EXIT_OK
    assert "3 skipped" in capsys.readouterr().out
    (import_set / "manifest.jsonl").write_text(_line(room_type="castle") + "\n")
    assert main([*base, "import", str(import_set)]) == EXIT_FAILURE
    assert "line 1: room_type 'castle' is not declared" in capsys.readouterr().err
    assert main([*base, "import", str(import_set / "nowhere")]) == EXIT_FAILURE
    assert "no manifest.jsonl" in capsys.readouterr().err
    assert main([*base, "plan"]) == EXIT_OK and main([*base, "audit"]) == EXIT_OK


# --- Views of one room: groups (design/imports.md, I1) ---------------------------------------------------------

GROUPED = [("k1.png", "kitchen", True), ("k2.png", "kitchen", True), ("b1.png", "bedroom", True),
           ("b2.png", "bedroom", True), ("solo.png", "kitchen", True)]
GROUPS = {"k1.png": {"group": "kitchen 1"}, "k2.png": {"group": "kitchen 1"},
          "b1.png": {"group": "bedroom 1"}, "b2.png": {"group": "bedroom 1"}}


def _grouped(import_set: Path) -> Path:
    return make_import_set(import_set / "grouped", GROUPED, indices=[30, 31, 32, 33, 34], extra=GROUPS)


def test_views_of_one_group_share_a_building_and_a_room_and_keep_their_own_scenes(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    summary = importer.import_folder(ds, _grouped(import_set))
    assert (summary.scenes, summary.buildings, summary.specs) == (5, 3, 15)
    counts = {t: ds.conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("building", "room", "scene")}
    assert counts == {"building": 3, "room": 3, "scene": 5}
    rooms = {repo.imported_image(ds.conn, s).line: repo.scene(ds.conn, s).room_id for s in range(1, 6)}  # type: ignore[union-attr]
    assert rooms[1] == rooms[2] and rooms[3] == rooms[4] and len({rooms[1], rooms[3], rooms[5]}) == 3
    assert len({repo.scene(ds.conn, s).seed for s in range(1, 6)}) == 5  # each view its own scene, its own seed
    assert audit.audit(ds).ok


def test_the_views_of_a_group_land_in_one_split_of_an_export(folder: Path, import_set: Path) -> None:
    ds, summary = run_imports(folder, _grouped(import_set))
    assert summary.pairs == 15
    target, _ = export.export(ds, "v1")
    lines = [json.loads(line) for line in (target / "manifest.jsonl").read_text().splitlines()]
    assert len({line["building"] for line in lines}) == 3 and len({line["room"] for line in lines}) == 3
    assert len({line["scene"] for line in lines}) == 5  # five views, three rooms
    split_of: dict[str, str] = {}
    for line in lines:
        assert split_of.setdefault(line["building"], line["split"]) == line["split"]
    assert audit.audit(ds).ok


def test_a_group_is_one_room_of_one_source_and_may_grow_in_a_later_import(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    importer.import_folder(ds, _grouped(import_set))
    more = make_import_set(import_set / "more_views", [("k3.png", "kitchen", True)], indices=[40], extra={"k3.png": GROUPS["k1.png"]})
    again = importer.import_folder(ds, more)
    assert (again.scenes, again.buildings) == (1, 0)  # a third view of "kitchen 1": the same room
    assert repo.scene(ds.conn, 6).room_id == repo.scene(ds.conn, 1).room_id
    other = make_import_set(import_set / "other_source", [("k4.png", "kitchen", True)], indices=[41], extra={"k4.png": GROUPS["k1.png"]},
                            source={"name": "other-tool", "revision": "1", "family": "p", "licence": "MIT"})
    assert importer.import_folder(ds, other).buildings == 1  # the same group name of another source is another room
    assert audit.audit(ds).ok


def test_views_of_a_group_must_agree_on_the_room(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    bad = make_import_set(import_set / "bad", [("k1.png", "kitchen", True), ("k2.png", "kitchen", True)],
                          indices=[30, 31], extra={"k1.png": {"group": "g", "values": {"style": "modern"}},
                                                   "k2.png": {"group": "g", "values": {"style": "rustic"}}})
    with pytest.raises(ManifestError, match=r"line 2 \(k2.png\): group 'g' gives other room type or room values than line 1"):
        importer.import_folder(ds, bad)
    importer.import_folder(ds, _grouped(import_set))
    late = make_import_set(import_set / "late", [("k5.png", "kitchen", True)], indices=[42],
                           extra={"k5.png": {**GROUPS["k1.png"], "values": {"style": "modern"}}})
    with pytest.raises(ManifestError, match="is a room of an earlier import with other values"):
        importer.import_folder(ds, late)
    assert repo.scene_count(ds.conn) == 5


def test_the_audit_checks_the_grouping_of_imported_scenes(folder: Path, import_set: Path) -> None:
    ds, _ = run_imports(folder, _grouped(import_set))
    assert audit.audit(ds).ok
    _tamper(ds, "UPDATE imported_image SET group_name = 'elsewhere' WHERE scene_id = 2", (), "do not share one group",
            lambda: _set_group(ds, "kitchen 1"))


def _set_group(ds: Dataset, group: str) -> None:
    with ds.conn:
        ds.conn.execute("UPDATE imported_image SET group_name = ? WHERE scene_id = 2", (group,))


@pytest.mark.parametrize("text, message", [(_line(group=3), "group must be a non-empty text"),
                                           (_line(group=" "), "group must be a non-empty text")])
def test_a_group_is_a_non_empty_text(folder: Path, text: str, message: str) -> None:
    with pytest.raises(ManifestError, match=message):
        parse_manifest(text, open_dataset(folder).space)
    assert parse_manifest(_line(group="room 1"), open_dataset(folder).space)[0].group == "room 1"


# --- One picture enters once, as opaque RGB -------------------------------------------------------------------


def test_the_same_pixels_saved_with_other_bytes_are_one_picture(folder: Path, import_set: Path) -> None:
    """Review probe E5: another PNG compression of an imported picture is not a second building."""
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    Image.open(import_set / "a.png").save(import_set / "a_again.png", compress_level=1)
    assert (import_set / "a_again.png").read_bytes() != (import_set / "a.png").read_bytes()
    again = make_import_set(import_set / "again", [("x.png", "kitchen", True)], indices=[50])
    (again / "a_again.png").write_bytes((import_set / "a_again.png").read_bytes())
    lines = (again / "manifest.jsonl").read_text() + _line(file="a_again.png") + "\n"
    (again / "manifest.jsonl").write_text(lines)
    summary = importer.import_folder(ds, again)
    assert (summary.scenes, summary.skipped) == (1, ("a_again.png",))
    assert repo.scene_count(ds.conn) == 4 and ds.conn.execute("SELECT COUNT(*) FROM building").fetchone()[0] == 4
    with pytest.raises(sqlite3.IntegrityError), ds.conn:  # and the store refuses the same picture twice
        ds.conn.execute("UPDATE imported_image SET image_sha = (SELECT image_sha FROM imported_image WHERE scene_id = 2)"
                        " WHERE scene_id = 1")


def test_an_image_with_an_alpha_channel_or_one_grey_channel_is_stored_as_opaque_rgb(folder: Path, import_set: Path) -> None:
    """Review probe E8: the clean image has the cluttered image's mode, and a transparent pixel is refused."""
    s = import_set / "modes"
    s.mkdir()
    rgba = np.full((300, 400, 4), 120, np.uint8)
    rgba[..., 3] = 255
    rgba[:64, :64, :3] = 255
    Image.fromarray(rgba, "RGBA").save(s / "opaque.png")
    grey = np.full((300, 380), 120, np.uint8)
    grey[:64, :64] = 255
    Image.fromarray(grey, "L").save(s / "grey.png")
    transparent = rgba.copy()
    transparent[200:, 200:, 3] = 0
    Image.fromarray(transparent, "RGBA").save(s / "transparent.png")
    source = {"name": "t", "revision": "1", "family": "f", "licence": "MIT"}

    def manifest(*files: str) -> None:
        (s / "manifest.jsonl").write_text("".join(json.dumps({"file": f, "room_type": "kitchen", "source": source}) + "\n"
                                                  for f in files))

    ds = open_dataset(folder)
    manifest("opaque.png", "grey.png", "transparent.png")
    with pytest.raises(ManifestError, match=r"line 3 \(transparent.png\): it has transparent pixels"):
        importer.import_folder(ds, s)
    assert repo.scene_count(ds.conn) == 0
    manifest("opaque.png", "grey.png")
    importer.import_folder(ds, s)
    assert {Image.open(io.BytesIO(ds.blobs.get(r.image_sha))).mode for r in repo.imported_images(ds.conn)} == {"RGB"}
    thresholds = config.thresholds(ds.cfg, {})
    summary = run.execute(ds, run.connect_models(ds, retries=0), thresholds, run.RunOptions())
    assert summary.pairs == 6 and audit.audit(ds).ok


# --- What the audit ties together ------------------------------------------------------------------------------


def test_the_audit_ties_the_clean_image_to_its_original_and_the_judged_image_to_the_record(
        folder: Path, import_set: Path) -> None:
    """Review probes E10 and E1b."""
    ds, _ = run_imports(folder, import_set)
    one, two = repo.imported_image(ds.conn, 1), repo.imported_image(ds.conn, 2)
    assert one is not None and two is not None
    with pytest.raises(sqlite3.IntegrityError), ds.conn:  # E10: another import's clean image cannot be put in its place
        ds.conn.execute("UPDATE imported_image SET image_sha = ? WHERE scene_id = 1", (two.image_sha,))
    size = repo.image_size(ds.conn, one.image_sha)
    other = Image.fromarray(np.random.default_rng(5).integers(0, 255, (size[1], size[0], 3), dtype=np.uint8))
    with ds.conn:  # a picture of the same size that is nobody's original resized
        swapped = repo.record_image(ds.conn, ds.blobs, imaging.encode_png(other))
        ds.conn.execute("UPDATE imported_image SET image_sha = ? WHERE scene_id = 1", (swapped,))
    problems = audit.audit(ds).problems
    assert any("scene 1: its image is not its original resized again" in p for p in problems), problems
    with ds.conn:
        ds.conn.execute("UPDATE imported_image SET image_sha = ? WHERE scene_id = 1", (one.image_sha,))
    _tamper(ds, "UPDATE imported_image SET pixel_sha = ? WHERE scene_id = 1", ("a" * 64,), "hash of its original's pixels",
            lambda: _set_pixel_sha(ds, one.pixel_sha))
    iteration = ds.conn.execute("SELECT it.id FROM iteration it JOIN loop_run l ON l.id = it.loop_run_id"
                                " WHERE l.scene_id = 1 AND l.stage = 'clean'").fetchone()[0]
    with ds.conn:  # E1b: the judged image and the clutter loops' input both moved to another image
        ds.conn.execute("UPDATE iteration_image SET image_sha = ? WHERE iteration_id = ? AND role = 'imported'",
                        (two.image_sha, iteration))
        ds.conn.execute("UPDATE loop_run SET input_image = ? WHERE clutter_spec_id IN"
                        " (SELECT id FROM clutter_spec WHERE scene_id = 1)", (two.image_sha,))
    assert any("the image it judged is not the one its scene's import recorded" in p for p in audit.audit(ds).problems)


def _set_pixel_sha(ds: Dataset, sha: str) -> None:
    with ds.conn:
        ds.conn.execute("UPDATE imported_image SET pixel_sha = ? WHERE scene_id = 1", (sha,))


def test_an_accepted_clutter_iteration_that_is_not_a_pair_is_an_audit_problem(folder: Path, import_set: Path) -> None:
    ds, _ = run_imports(folder, import_set)
    pair = int(repo.query(ds.conn, "pair")[0]["pair_id"])  # type: ignore[call-overload]
    with ds.conn:
        ds.conn.execute("DELETE FROM iteration_image WHERE iteration_id = ? AND role = 'composite'", (pair,))
    problems = audit.audit(ds).problems
    assert any(f"iteration {pair}: accepted, but it is not a pair" in p for p in problems), problems


# --- The sizing parameters stay with the import ----------------------------------------------------------------


def test_the_sizing_parameters_are_recorded_and_a_changed_configuration_stops_the_run(
        folder: Path, import_set: Path, server: FakeModelServer) -> None:
    """Review probe E2: an image resized for output_side 256 must not be edited under output_side 320."""
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    params = repo.import_set(ds.conn, 1)
    assert (params.output_side, params.size_multiple, params.condition_max_pixels, params.resampler) == \
        (256, 32, 1_048_576, "lanczos")
    ds.conn.close()
    write_config(folder, server, pair_target=50, output_side=320)
    ds = open_dataset(folder)
    assert audit.audit(ds).ok  # the audit judges the import against the parameters it recorded
    with pytest.raises(ConfigError, match=r"(?s)no longer fit the configuration.*scene 1: edited at output_side 320"):
        run.execute(ds, run.connect_models(ds, retries=0), config.thresholds(ds.cfg, {}), run.RunOptions())
    assert repo.all_calls(ds.conn) == [] and repo.accepted_pairs(ds.conn) == 0


def test_a_size_that_the_editor_changes_is_a_problem() -> None:
    assert size_problem((288, 192), 256, 32, 1_048_576) is None
    assert "comes back at 352x160" in str(size_problem((320, 160), 256, 32, 1_048_576))
    assert "condition-image limit" in str(size_problem((288, 192), 256, 32, 50_000))


# --- Problems come together; the file read twice is the same file ---------------------------------------------


def test_a_licence_clash_is_reported_with_the_other_problems_and_writes_nothing(folder: Path, import_set: Path) -> None:
    """Review probe E3."""
    ds = open_dataset(folder)
    importer.import_folder(ds, import_set)
    blobs_before = sum(1 for p in (folder / "images").rglob("*") if p.is_file())
    mixed = make_import_set(import_set / "mixed", [("odd.png", "kitchen", True), ("x.png", "kitchen", True)],
                            indices=[60, 61])
    Image.fromarray(np.full((200, 360, 3), 90, np.uint8)).save(mixed / "odd.png")  # a size the editor would change
    clash = json.dumps({"file": "x.png", "room_type": "kitchen", "source": {"name": "render-tool", "revision": "1.0",
                                                                           "family": "procedural", "licence": "CC0"}})
    (mixed / "manifest.jsonl").write_text((mixed / "manifest.jsonl").read_text().splitlines()[0] + "\n" + clash + "\n"
                                          + _line(file="missing.png") + "\n")
    with pytest.raises(ManifestError) as error:
        importer.import_folder(ds, mixed)
    message = str(error.value)
    assert "line 1 (odd.png)" in message and "line 3 (missing.png)" in message
    assert "line 2 (x.png): source render-tool@1.0 is recorded with family procedural and licence MIT" in message
    assert repo.scene_count(ds.conn) == 3 and sum(1 for p in (folder / "images").rglob("*") if p.is_file()) == blobs_before


def test_a_licence_clash_inside_one_manifest_is_found_before_anything_is_written(folder: Path, import_set: Path) -> None:
    ds = open_dataset(folder)
    both = make_import_set(import_set / "both", [("x.png", "kitchen", True), ("y.png", "kitchen", True)], indices=[70, 71])
    first, second = (both / "manifest.jsonl").read_text().splitlines()
    changed = json.loads(second)
    changed["source"]["licence"] = "CC0"
    (both / "manifest.jsonl").write_text(first + "\n" + json.dumps(changed) + "\n")
    with pytest.raises(ManifestError, match=r"line 2 \(y.png\): source render-tool@1.0 has another family or licence than on line 1"):
        importer.import_folder(ds, both)
    assert repo.scene_count(ds.conn) == 0 and not (folder / "images").exists()


def test_a_file_that_changes_between_validation_and_writing_is_refused(
        folder: Path, import_set: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    ds = open_dataset(folder)
    real = importer._validated

    def validated_then_changed(*args: object) -> object:
        found = real(*args)  # type: ignore[arg-type]
        (import_set / "b.png").write_bytes(b"not the image that was validated")
        return found

    monkeypatch.setattr(importer, "_validated", validated_then_changed)
    with pytest.raises(ManifestError, match=r"line 2 \(b.png\): the file changed during the import"):
        importer.import_folder(ds, import_set)
    assert repo.scene_count(ds.conn) == 0 and ds.conn.execute("SELECT COUNT(*) FROM import_set").fetchone()[0] == 0
