"""The whole flow on the fake model server: loops, recording, resume, carry-forward, audit, export."""

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest
from conftest import write_config
from helpers import run_dataset

from clutter_pairs import audit, config, export, run
from clutter_pairs.dataset import open_dataset
from clutter_pairs.fakes import FakeBehaviour, FakeModelServer
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction


def test_a_run_reaches_its_pair_target_and_passes_every_audit_check(folder: Path) -> None:
    """P1, P8 and P9 through the audit: pairs equal outside the mask, bodies rebuilt, requests recomposed."""
    ds, summary = run_dataset(folder)
    assert summary.stopped == "pair_target" and summary.pairs >= 6
    result = audit.audit(ds)
    assert result.ok, result.problems
    for check in ("requests recomposed", "exchanges rebuilt", "pairs compared", "images checked", "regions checked"):
        assert result.checked[check] > 0
    assert ds.conn.execute("SELECT COUNT(*) FROM region_item").fetchone()[0] > 0
    assert result.checked["judgments parsed again"] > 0
    with ds.conn:
        ds.conn.execute("UPDATE region_answer SET other_change = 1 WHERE rowid = (SELECT MIN(rowid) FROM region_answer)")
    problems = audit.audit(ds).problems
    assert any("not its call's answer parsed again" in p for p in problems)
    assert any("explained-change assessment does not recompute" in p for p in problems)
    with ds.conn:
        ds.conn.execute("UPDATE region_answer SET other_change = 0")
    with ds.conn:
        ds.conn.execute("UPDATE mask_region SET px = px + 1 WHERE rowid = (SELECT MIN(rowid) FROM mask_region)")
    assert any("do not recompute" in p for p in audit.audit(ds).problems)
    pairs = repo.query(ds.conn, "pair")
    assert {p["clean_family"] for p in pairs} == {"flux2"} and {p["editor_family"] for p in pairs} == {"flux2"}


def test_p2_a_finished_run_started_again_makes_no_model_call(folder: Path) -> None:
    """Every loop reopened and run again replays its stored history: the engine asks what is stored, every call is
    answered from the store, and the verdicts and images come out the same."""
    ds, _ = run_dataset(folder)
    calls, pairs = repo.actual_call_count(ds.conn), repo.query(ds.conn, "pair")
    with transaction(ds.conn):
        ds.conn.execute("UPDATE loop_run SET stop_reason = NULL")
        wave = repo.create_wave(ds.conn, repo.create_run(ds.conn, ds.config_sha, ds.target_set_id, 99, None, "now"),
                                False, "now")
    models = run.connect_models(ds, retries=0)
    work = run.SceneWork(ds, ds.conn, models, config.thresholds(ds.cfg, {}), run.RunOptions(), wave)
    for scene in sorted({r[0] for r in ds.conn.execute("SELECT scene_id FROM clean_image")}):
        work.run(scene)
    assert repo.actual_call_count(ds.conn) == calls
    assert [(p["clean_image"], p["cluttered_image"]) for p in repo.query(ds.conn, "pair")] == \
        [(p["clean_image"], p["cluttered_image"]) for p in pairs]
    assert audit.audit(ds).ok


def test_a_paused_run_resumes_where_it_stopped(folder: Path, behaviour: FakeBehaviour) -> None:
    behaviour.down_after = 23
    with pytest.raises(run.RunPaused):
        run_dataset(folder)
    behaviour.down_after = None
    ds, summary = run_dataset(folder)
    assert summary.stopped == "pair_target"
    assert audit.audit(ds).ok
    seen = set()
    for call in repo.all_calls(ds.conn):
        if call.reused_call_id is None and call.error_code is None:
            key = (call.loop_run_id, call.iteration_id, call.role)
            assert key not in seen, f"a step was called twice: {key}"
            seen.add(key)


def test_carry_forward_the_on_arm_starts_better(tmp_path: Path, server: FakeModelServer) -> None:
    """The scripted judge rejects until the marker is in the prompt; the distiller makes it a lesson. From the second
    wave on, a loop of the `on` arm is accepted at its first iteration, a loop of the `off` arm is not."""
    write_config(tmp_path, server, pair_target=30, wave_width=2)
    ds, summary = run_dataset(tmp_path)
    assert summary.waves >= 3
    rows = repo.query(ds.conn, "carry_forward_loop")
    on = [r["iterations"] for r in rows if r["lessons_arm"] == "on"]
    off = [r["iterations"] for r in rows if r["lessons_arm"] == "off"]
    assert on and off and set(on) == {1} and min(off) >= 2
    assert any(lesson["used_by_loops"] for lesson in repo.lessons_table(ds.conn))
    texts = [lesson["text"] for lesson in repo.lessons_table(ds.conn)]
    assert len(texts) == len(set((t, s) for t, s in zip(texts, [r["stage"] for r in repo.lessons_table(ds.conn)], strict=True)))


def test_a_misaligned_edit_is_answered_by_a_reseed(tmp_path: Path) -> None:
    with FakeModelServer(FakeBehaviour(misalign_first_edit=True)) as server:
        write_config(tmp_path, server)
        ds, summary = run_dataset(tmp_path)
    actions = [r[0] for r in ds.conn.execute(
        "SELECT i.action FROM iteration i JOIN loop_run l ON l.id = i.loop_run_id WHERE l.stage = 'clutter'"
        " AND i.n = 2 ORDER BY l.id")]
    assert actions[0] == "reseed"
    assert "misaligned" in {r[0] for r in ds.conn.execute("SELECT code FROM finding")}
    assert summary.pairs > 0 and audit.audit(ds).ok


def test_a_change_no_item_explains_fails_the_pair(tmp_path: Path) -> None:
    with FakeModelServer(FakeBehaviour(locate_items=False)) as server:
        write_config(tmp_path, server, pair_target=2)
        ds, summary = run_dataset(tmp_path, smoke=True)
    assert summary.pairs == 0
    assert "unexplained_change" in {r[0] for r in ds.conn.execute("SELECT code FROM finding")}


def test_an_invented_opening_fails_the_pair_and_reaches_the_reviser(tmp_path: Path) -> None:
    with FakeModelServer(FakeBehaviour(invent_door=True)) as server:
        write_config(tmp_path, server, pair_target=2)
        ds, summary = run_dataset(tmp_path, smoke=True)
    assert summary.pairs == 0
    rows = ds.conn.execute("SELECT f.code, f.judged_severity, f.comment, fr.n FROM finding f"
                           " LEFT JOIN finding_region fr ON fr.finding_id = f.id WHERE f.code = 'opening_changed'").fetchall()
    assert rows and {tuple(r) for r in rows} == {("opening_changed", "blocking", "door, left wall: appeared", 1)}
    revised = [r[0] for r in ds.conn.execute(
        "SELECT t.content FROM composition_part cp JOIN model_call mc ON mc.id = cp.model_call_id"
        " JOIN text_blob t ON t.sha256 = cp.text_sha WHERE mc.role = 'revise' AND cp.slot = 'assessment'")]
    assert any("finding opening_changed in region 1: door, left wall: appeared" in t for t in revised)
    assert audit.audit(ds).ok


def test_a_judge_answer_off_its_contract_stops_the_loop(tmp_path: Path) -> None:
    with FakeModelServer(FakeBehaviour(broken_judge=True)) as server:
        write_config(tmp_path, server)
        ds, summary = run_dataset(tmp_path, smoke=True)
    assert summary.loops == {"clean:error": 2}
    assert {r[0] for r in ds.conn.execute("SELECT error_code FROM model_call WHERE role = 'judge'")} == {"bad_answer"}
    assert audit.audit(ds).ok


def test_p4_no_call_starts_that_the_deadline_would_cut(folder: Path) -> None:
    ds, summary = run_dataset(folder, deadline=datetime.now(UTC) + timedelta(seconds=30))
    assert summary.stopped == "deadline" and repo.actual_call_count(ds.conn) == 0


def test_p5_coverage_counts_each_pair_in_its_cell(folder: Path) -> None:
    ds, summary = run_dataset(folder)
    coverage = repo.query(ds.conn, "coverage")
    assert sum(int(r["accepted"]) for r in coverage) == summary.pairs  # the default cells partition the pairs


def test_p6_an_export_never_puts_one_building_in_two_splits(folder: Path) -> None:
    ds, summary = run_dataset(folder)
    target, count = export.export(ds, "v1")
    lines = [json.loads(line) for line in (target / "manifest.jsonl").read_text().splitlines()]
    assert count == summary.pairs == len(lines)
    split_of: dict[str, str] = {}
    for line in lines:
        assert split_of.setdefault(line["building"], line["split"]) == line["split"]
        assert (target / line["clean"]).is_file() and (target / line["mask"]).is_file()
    with pytest.raises(ValueError, match="snapshots"):
        export.export(ds, "v1")
    assert audit.audit(ds).ok


def test_the_audit_catches_tampering(folder: Path) -> None:
    ds, _ = run_dataset(folder)
    with transaction(ds.conn):
        part = ds.conn.execute("SELECT model_call_id, ordinal FROM composition_part WHERE source_kind = 'spec' LIMIT 1").fetchone()
        sha = repo.record_text(ds.conn, "- room_type: castle")
        ds.conn.execute("UPDATE composition_part SET text_sha = ? WHERE model_call_id = ? AND ordinal = ?", (sha, *part))
        body = ds.conn.execute("SELECT model_call_id, ordinal FROM exchange WHERE body_text_sha IS NOT NULL LIMIT 1").fetchone()
        sha = repo.record_text(ds.conn, "{}")
        ds.conn.execute("UPDATE exchange SET body_text_sha = ? WHERE model_call_id = ? AND ordinal = ?", (sha, *body))
    problems = audit.audit(open_dataset(folder)).problems
    assert any("differs from stored" in p for p in problems)
    assert any("not the loop subject's spec" in p for p in problems)
    assert any("wire hash" in p for p in problems)
