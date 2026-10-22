"""Command line: set up a dataset, plan, rent a GPU, run the loops, report, audit, decide, export."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from dataclasses import replace
from datetime import datetime
from pathlib import Path
from typing import Any

from virtual_unstaging.provision.errors import ProvisionError

from clutter_pairs import __version__, audit, config, export, gpu, plan, report, run
from clutter_pairs.dataset import Dataset, open_dataset
from clutter_pairs.fakes import FakeModelServer
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction, utc_now

EXIT_OK, EXIT_FAILURE, EXIT_USAGE, EXIT_PAUSED, EXIT_DEADLINE = 0, 1, 2, 3, 4


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result: int = args.handler(args)
        return result
    except run.RunPaused as error:
        print(f"paused: {error}\nresume with `cpairs run` once the endpoint answers", file=sys.stderr)
        return EXIT_PAUSED
    except ProvisionError as error:
        print(f"error [{error.code}]: {error.message}" + (f"\nhint: {error.hint}" if error.hint else ""), file=sys.stderr)
        return int(error.exit_code)
    except (config.ConfigError, LookupError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return EXIT_FAILURE


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cpairs", description=__doc__)
    parser.add_argument("--version", action="version", version=f"cpairs {__version__}")
    parser.add_argument("--dataset", type=Path, default=Path("."), help="dataset folder (default: current folder)")
    sub = parser.add_subparsers(required=True, metavar="command")

    p = sub.add_parser("init", help="write clutter_pairs.toml with the default space and models in a folder")
    p.add_argument("folder", type=Path)
    p.set_defaults(handler=cmd_init)

    p = sub.add_parser("plan", help="sample scenes and clutter specs into the target cells with the largest shortfall")
    p.add_argument("--json", action="store_true")
    p.set_defaults(handler=cmd_plan)

    p = sub.add_parser("gpu", help="rent or release the GPU (virtual_unstaging's provisioning, with a deadline)")
    gsub = p.add_subparsers(required=True, metavar="action")
    up = gsub.add_parser("up", help="rent a GPU serving the generator and the judge; shows the price and the deadline")
    up.add_argument("--limit", required=True, help="the machine deletes itself after this, e.g. 2h or 90m")
    up.add_argument("--gpu", help="GPU type; default: [gpu] gpu, else the first in stock of the preference list")
    up.add_argument("--yes", action="store_true", help="do not ask before renting")
    up.set_defaults(handler=cmd_gpu_up)
    judge = gsub.add_parser("judge", help="serve the judge [judge] names on the live machine (no new rental)")
    judge.set_defaults(handler=cmd_gpu_judge)
    down = gsub.add_parser("down", help="release the GPU before its deadline")
    down.set_defaults(handler=cmd_gpu_down)

    p = sub.add_parser("run", help="waves of loops until the pair target or the deadline")
    p.add_argument("--smoke", action="store_true", help="run the smoke wave only (two scenes through both loops)")
    p.add_argument("--fake", action="store_true", help="use the stand-in models (no GPU, no network)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(handler=cmd_run)

    p = sub.add_parser("report", help="coverage, iteration curve, carry-forward under its decision rule, cost")
    p.add_argument("--json", action="store_true")
    p.set_defaults(handler=cmd_report)

    p = sub.add_parser("audit", help="every check of the data model; with a pair id, its lineage")
    p.add_argument("pair", nargs="?", type=int)
    p.add_argument("--json", action="store_true")
    p.set_defaults(handler=cmd_audit)

    p = sub.add_parser("decide", help="record an owner's act: a threshold, or a review mark on an assessment")
    dsub = p.add_subparsers(required=True, metavar="act")
    t = dsub.add_parser("threshold", help="set a pixel-test threshold (see [pixels] in clutter_pairs.toml)")
    t.add_argument("name")
    t.add_argument("value", type=float)
    t.add_argument("--reason", default="")
    t.set_defaults(handler=cmd_decide_threshold)
    m = dsub.add_parser("mark", help="mark an assessment right or wrong")
    m.add_argument("assessment", type=int)
    m.add_argument("mark", choices=("right", "wrong"))
    m.add_argument("--note", default="")
    m.set_defaults(handler=cmd_decide_mark)

    p = sub.add_parser("lessons", help="list the lessons; retire or promote one (from the next wave on)")
    p.add_argument("action", nargs="?", choices=("list", "retire", "promote"), default="list")
    p.add_argument("lesson", nargs="?", type=int)
    p.add_argument("--reason", default="")
    p.add_argument("--json", action="store_true")
    p.set_defaults(handler=cmd_lessons)

    p = sub.add_parser("export", help="write a dataset version: images, manifest, splits by building")
    p.add_argument("name")
    p.set_defaults(handler=cmd_export)
    return parser


def _emit(value: Any, as_json: bool, text: str) -> None:
    print(json.dumps(value, indent=2, sort_keys=True, default=str) if as_json else text)


def cmd_init(args: argparse.Namespace) -> int:
    folder: Path = args.folder
    path = folder / config.CONFIG_NAME
    if path.exists():
        print(f"error: {path} exists", file=sys.stderr)
        return EXIT_FAILURE
    folder.mkdir(parents=True, exist_ok=True)
    path.write_text(config.template(), encoding="utf-8")
    open_dataset(folder)
    print(path)
    return EXIT_OK


def cmd_plan(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    with transaction(ds.conn):
        added = plan.plan(ds.conn, ds)
    _emit({"scenes_added": added, "scenes": repo.scene_count(ds.conn)}, args.json,
          f"{added} scenes added, {repo.scene_count(ds.conn)} in all")
    return EXIT_OK


def cmd_gpu_up(args: argparse.Namespace) -> int:
    cfg = config.load(args.dataset)
    interactive = sys.stdin.isatty() and sys.stderr.isatty()
    ctx = gpu.context(cfg, interactive, _confirm)
    session, deadline, price = gpu.up(cfg, ctx, args.limit, args.gpu, args.yes)
    print(f"session\t{session}\nprice_per_hour\t{price}\ndeadline\t{deadline}")
    return EXIT_OK


def cmd_gpu_judge(args: argparse.Namespace) -> int:
    cfg = config.load(args.dataset)
    print(f"judge\t{gpu.switch_judge(gpu.context(cfg, False, _confirm))}")
    return EXIT_OK


def cmd_gpu_down(args: argparse.Namespace) -> int:
    cfg = config.load(args.dataset)
    for session in gpu.down(args.dataset, gpu.context(cfg, False, _confirm)):
        print(f"ended\t{session}")
    return EXIT_OK


def _confirm(prompt: str) -> bool:
    print(prompt, end="", file=sys.stderr, flush=True)
    return sys.stdin.readline().strip().lower() in ("y", "yes")


def cmd_run(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    thresholds = config.thresholds(ds.cfg, repo.threshold_decisions(ds.conn))
    replan = lambda conn: plan.plan(conn, ds)  # noqa: E731
    if args.fake:
        with FakeModelServer() as server:
            ds.cfg = _with_endpoints(ds, server.tools_url, server.chat_url)
            summary = run.execute(ds, run.connect_models(ds, retries=0), thresholds,
                                  run.RunOptions(smoke=args.smoke, replan=replan))
    else:
        rental = _rental(ds)
        options = run.RunOptions(smoke=args.smoke, deadline=None if rental is None else rental[1],
                                 rental_id=None if rental is None else rental[0], replan=replan)
        summary = run.execute(ds, run.connect_models(ds), thresholds, options)
    _emit(summary.__dict__, args.json,
          f"run {summary.run_id}: {summary.waves} waves, {summary.pairs} accepted pairs, stopped: {summary.stopped}\n"
          + "\n".join(f"  {k}: {v}" for k, v in sorted(summary.loops.items())))
    if summary.stopped == "smoke_wave":
        print("smoke wave done: check it (`cpairs report`, `cpairs audit`), then `cpairs run` again", file=sys.stderr)
    return EXIT_DEADLINE if summary.stopped == "deadline" else EXIT_OK


def _with_endpoints(ds: Dataset, tools: str, chat: str) -> config.Config:
    cfg = ds.cfg
    return replace(cfg, generator=replace(cfg.generator, service=replace(cfg.generator.service, endpoint=tools)),
                   judge=replace(cfg.judge, service=replace(cfg.judge.service, endpoint=chat)))


def _rental(ds: Dataset) -> tuple[int, datetime] | None:
    if ds.cfg.session_id is None:
        return None
    found = repo.rental_by_session(ds.conn, ds.cfg.session_id)
    if found is None:
        raise config.ConfigError(f"GPU session {ds.cfg.session_id} has no rental in this store: was it started with "
                                 "`cpairs gpu up`?")
    return found[0], datetime.fromisoformat(found[1])


def cmd_report(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    built = report.build(ds)
    _emit(built, args.json, report.render_text(built))
    return EXIT_OK


def cmd_audit(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    if args.pair is not None:
        print(json.dumps(audit.lineage(ds.conn, args.pair), indent=2, sort_keys=True))
        return EXIT_OK
    result = audit.audit(ds)
    _emit({"checked": result.checked, "problems": result.problems}, args.json,
          "\n".join([f"{k}: {v}" for k, v in sorted(result.checked.items())] + result.problems
                    + ["audit: " + ("ok" if result.ok else f"{len(result.problems)} problems")]))
    return EXIT_OK if result.ok else EXIT_FAILURE


def cmd_decide_threshold(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    config.thresholds(ds.cfg, {args.name: args.value})  # rejects an unknown name
    with transaction(ds.conn):
        repo.add_decision(ds.conn, utc_now(), "owner", "threshold_set",
                          {"name": args.name, "value": args.value, "reason": args.reason})
    print(f"{args.name} = {args.value} from the next iteration on")
    return EXIT_OK


def cmd_decide_mark(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    repo.assessment(ds.conn, args.assessment)
    with transaction(ds.conn):
        repo.add_decision(ds.conn, utc_now(), "owner", "review_mark", {"mark": args.mark, "note": args.note},
                          assessment_id=args.assessment)
    print(f"assessment {args.assessment} marked {args.mark}")
    return EXIT_OK


def cmd_lessons(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    if args.action == "list":
        rows = repo.lessons_table(ds.conn)
        _emit(rows, args.json, "\n".join(
            f"{r['id']:>4} {r['stage']:<8} waves {r['active_from_wave']}-{r['ended_wave'] or ''} "
            f"{r['end_kind'] or 'active':<9} used {r['used_by_loops']:>3}  {r['text']}" for r in rows) or "no lesson")
        return EXIT_OK
    if args.lesson is None:
        print("error: name the lesson", file=sys.stderr)
        return EXIT_USAGE
    lesson = repo.lesson(ds.conn, args.lesson)
    action = "lesson_retire" if args.action == "retire" else "lesson_promote"
    with transaction(ds.conn):
        repo.add_decision(ds.conn, utc_now(), "owner", action, {"reason": args.reason}, lesson_id=lesson.id)
    print(f"lesson {lesson.id} ends at the next wave")
    if args.action == "promote":
        packaged = f"instructions/{lesson.stage}_writer.md"
        print(f"add it to the {packaged} in force (a new version in git, or a [files] replacement):\n{lesson.text}")
    return EXIT_OK


def cmd_export(args: argparse.Namespace) -> int:
    ds = open_dataset(args.dataset)
    target, count = export.export(ds, args.name)
    print(f"{target}\t{count} pairs")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
