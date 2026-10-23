"""Command line: set up a project, prepare masks, run loop 1, report, deliver; review, serve and rent a GPU."""

from __future__ import annotations

import argparse
import json
import logging
import sqlite3
import sys
from collections.abc import Sequence
from dataclasses import replace
from pathlib import Path

from virtual_unstaging import __version__, config, imaging, stage0
from virtual_unstaging.clients.fakes import FakeChat, FakeGenerator, FakeRemoteTools
from virtual_unstaging.clients.generators import Generator, OpenAIImageEditGenerator, ToolServerGenerator
from virtual_unstaging.clients.http import Endpoint, EndpointError
from virtual_unstaging.clients.openai_compatible import chat_json, image_part, text_part
from virtual_unstaging.clients.remote_tools import RemoteTools
from virtual_unstaging.clients.toolserver import ToolServerClient
from virtual_unstaging.domain import GeneratorCapabilities, ModelRef
from virtual_unstaging.instructions import InstructionStack, load_base
from virtual_unstaging.judge import Chat
from virtual_unstaging.loop1.runner import Adapters, RunPaused, RunVersions, create_run, execute_run
from virtual_unstaging.registry import load_defects, load_release
from virtual_unstaging.report import build, detector_report, render_detectors, render_text, to_json
from virtual_unstaging.store import repo
from virtual_unstaging.store.blobs import BlobStore
from virtual_unstaging.store.db import connect, create_schema, transaction
from virtual_unstaging.tools import ToolBox, ToolProvider
from virtual_unstaging.tools.local import LocalTools

EXIT_OK, EXIT_FAILURE, EXIT_USAGE, EXIT_PAUSED = 0, 1, 2, 4
DB_NAME = "project.sqlite"
PHOTO_SUFFIXES = {".jpg", ".jpeg", ".png"}


def main(argv: Sequence[str] | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s %(message)s")
    if args.override:
        print(f"override files: {', '.join(map(str, args.override))}", file=sys.stderr)
    try:
        result: int = args.handler(args)
        return result
    except (config.ConfigError, LookupError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return EXIT_FAILURE
    except RunPaused as error:
        print(f"paused: {error}\nresume with: unstage run --resume <run id> once the endpoint answers", file=sys.stderr)
        return EXIT_PAUSED
    except EndpointError as error:
        print(f"endpoint error: {error}", file=sys.stderr)
        return EXIT_PAUSED if error.code == "endpoint_unreachable" else EXIT_FAILURE


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="unstage", description=__doc__)
    parser.add_argument("--version", action="version", version=f"unstage {__version__}")
    parser.add_argument("--project", type=Path, default=Path("."), help="project folder (default: current folder)")
    parser.add_argument("--override", type=Path, action="append", default=[], metavar="FILE",
                        help="TOML file layered over project.toml and gpu.toml for this command; repeatable, the last wins")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(required=True, metavar="command")

    p = sub.add_parser("init", help="create a project in --project")
    p.add_argument("--name", default=None)
    p.set_defaults(handler=cmd_init)

    p = sub.add_parser("import", help="import photos (JPEG or PNG files, or folders of them)")
    p.add_argument("paths", nargs="+", type=Path)
    p.add_argument("--group", help="room the photos belong to; default: the name of each photo's folder")
    p.set_defaults(handler=cmd_import)

    p = sub.add_parser("rules", help="load the content rules (TOML: [all] and [groups.\"<room>\"], fixed and movable)")
    p.add_argument("file", type=Path)
    p.set_defaults(handler=cmd_rules)

    p = sub.add_parser("masks", help="attach removal masks from files named like the photos")
    p.add_argument("removal_dir", type=Path)
    p.add_argument("--protected", type=Path, help="folder of protected-element masks, same naming")
    p.set_defaults(handler=cmd_masks)

    p = sub.add_parser("prepare", help="compute masks by segmentation on the tool server")
    p.add_argument("--photos", type=Path, help="file listing photo names, one per line (default: all)")
    p.set_defaults(handler=cmd_prepare)

    p = sub.add_parser("run", help="run loop 1 with one engine, or resume a run")
    p.add_argument("--engine", choices=["single", "coordinate", "guided"])
    p.add_argument("--photos", type=Path, help="file listing photo names, one per line (default: all with masks)")
    p.add_argument("--label")
    p.add_argument("--resume", type=int, metavar="RUN")
    p.add_argument("--dry-run", action="store_true", help="print the plan and the budget, call nothing")
    p.set_defaults(handler=cmd_run)

    p = sub.add_parser("report", help="summarize runs and the blind comparisons between them")
    p.add_argument("runs", nargs="*", type=int)
    p.add_argument("--json", action="store_true")
    p.add_argument("--detectors", action="store_true",
                   help="add the pixel detectors' bands, in shadow, beside the judge and the reviews")
    p.set_defaults(handler=cmd_report)

    p = sub.add_parser("deliver", help="decide each photo's outcome by rule (people's decisions are kept)")
    p.add_argument("--run", type=int, required=True)
    p.set_defaults(handler=cmd_deliver)

    p = sub.add_parser("export", help="write delivered images and a manifest to a folder")
    p.add_argument("folder", type=Path)
    p.set_defaults(handler=cmd_export)

    p = sub.add_parser("review", help="serve the review page on localhost")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--reviewer", default="owner", help="name recorded with each review")
    p.set_defaults(handler=cmd_review)

    p = sub.add_parser("serve", help="GPU side: run the tool server (needs the [serve] extra)")
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--deadline", required=True, help="a duration (90m, 2h) or an ISO 8601 UTC time")
    p.add_argument("--key-file", type=Path)
    p.add_argument("--key-env", help="name of the environment variable holding the key (rented-machine exception)")
    p.add_argument("--recipe", help="generator recipe name or TOML file; none: tools only")
    p.add_argument("--tools", default="segment_elements,class_diff,change_map,element_inventory,structure_map")
    p.add_argument("--data-dir", type=Path, default=Path("/tmp/unstage-serve"))
    p.set_defaults(handler=cmd_serve)

    p = sub.add_parser("gpu", help="rent a GPU with a time limit, list, stop; switch the live generator or judge")
    p.add_argument("action", choices=["up", "down", "ls", "price", "recipe", "judge"])
    p.add_argument("name", nargs="?", help="`recipe`: the packaged recipe to load on the live machine")
    p.add_argument("--provider", default="runpod")
    p.add_argument("--gpu", default=None, help="GPU type, e.g. 'NVIDIA RTX PRO 6000 Blackwell Server Edition'")
    p.add_argument("--limit", default=None, help="time limit, e.g. 3h; required by `up`")
    p.add_argument("--recipe", default=None)
    p.add_argument("--yes", action="store_true", help="do not ask for confirmation")
    p.set_defaults(handler=cmd_gpu)
    return parser


# --- project content -----------------------------------------------------------------------------------------


def _open(project: Path) -> tuple[sqlite3.Connection, BlobStore]:
    db_path = project / DB_NAME
    if not db_path.exists():
        raise config.ConfigError(f"no project in {project}: run `unstage --project {project} init` first")
    conn = connect(db_path)
    return conn, BlobStore(project / "blobs")


def cmd_init(args: argparse.Namespace) -> int:
    project: Path = args.project
    project.mkdir(parents=True, exist_ok=True)
    config.write_template(project, args.name or project.resolve().name)
    (project / "blobs").mkdir(exist_ok=True)
    (project / "instructions").mkdir(exist_ok=True)
    conn = connect(project / DB_NAME)
    create_schema(conn)
    with transaction(conn):
        repo.ensure_defect_types(conn, load_defects())
    print(f"project created in {project}; edit {config.CONFIG_NAME}, then import photos")
    return EXIT_OK


def cmd_import(args: argparse.Namespace) -> int:
    conn, blobs = _open(args.project)
    files: list[Path] = []
    for path in args.paths:
        if path.is_dir():
            files += sorted(p for p in path.rglob("*") if p.suffix.lower() in PHOTO_SUFFIXES)
        elif path.suffix.lower() in PHOTO_SUFFIXES:
            files.append(path)
        else:
            raise ValueError(f"not a photo or folder: {path}")
    added = 0
    for path in files:
        data = imaging.normalize_photo(path.read_bytes())
        sha = stage0.store_image(conn, blobs, data)
        with transaction(conn):
            group = args.group or path.parent.name
            group_id = repo.ensure_group(conn, group)
            _, new = repo.add_photo(conn, group_id, sha, path.name)
        added += int(new)
    print(f"{added} photos imported, {len(files) - added} already there")
    return EXIT_OK


def cmd_rules(args: argparse.Namespace) -> int:
    conn, _ = _open(args.project)
    items = config.parse_rules(args.file.read_text(encoding="utf-8"))
    with transaction(conn):
        rule_set_id = repo.insert_rule_set(conn, items)
    print(f"rule set {rule_set_id}: {len(items)} elements")
    return EXIT_OK


def cmd_masks(args: argparse.Namespace) -> int:
    conn, blobs = _open(args.project)
    rule_set_id = repo.latest_rule_set(conn)
    outcomes = stage0.import_masks(conn, blobs, rule_set_id, args.removal_dir, args.protected)
    for name, outcome in outcomes.items():
        print(f"{name}\t{outcome}")
    return EXIT_OK


def cmd_prepare(args: argparse.Namespace) -> int:
    conn, blobs = _open(args.project)
    cfg = config.load(args.project, args.override)
    rule_set_id = repo.latest_rule_set(conn)
    tools = _toolbox(cfg)
    outcomes = stage0.segment(conn, blobs, tools, rule_set_id, _names(args.photos))
    for name, outcome in outcomes.items():
        print(f"{name}\t{outcome}")
    return EXIT_OK


# --- loop 1 --------------------------------------------------------------------------------------------------


def _names(path: Path | None) -> list[str] | None:
    if path is None:
        return None
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _endpoint(url: str, secret: config.Secret) -> Endpoint:
    if not url:
        raise config.ConfigError("an endpoint URL is missing in project.toml")
    return Endpoint(url, secret.read())


def _toolserver(cfg: config.ProjectConfig) -> ToolServerClient:
    return ToolServerClient(_endpoint(cfg.tools_endpoint, cfg.tools_secret))


def _toolbox(cfg: config.ProjectConfig) -> ToolBox:
    local = LocalTools()
    routes: dict[str, ToolProvider] = {name: local for name in local.names}
    if cfg.generator.adapter == "fake":
        fake = FakeRemoteTools()
        routes |= {"segment_elements": fake, "class_diff": fake, "element_inventory": fake, "structure_map": fake}
    elif cfg.tools_endpoint:
        remote = RemoteTools(_toolserver(cfg))
        routes |= {"segment_elements": remote, "class_diff": remote, "element_inventory": remote, "structure_map": remote}
    return ToolBox(routes)


def _generator(cfg: config.ProjectConfig) -> Generator:
    g = cfg.generator
    if g.adapter == "fake":
        return FakeGenerator(g.capabilities)
    if g.adapter == "openai_images":
        return OpenAIImageEditGenerator(
            _endpoint(g.endpoint, g.secret), ModelRef(g.model, g.revision), g.capabilities, g.licence, g.fields
        )
    client = _toolserver(cfg)
    caps = client.capabilities().get("generator")
    if not caps:
        raise config.ConfigError("the tool server serves no generator")
    native = bool(caps["native_mask"])
    # Some pipelines take fewer images once a native mask is given (the recipe says how many).
    max_images = int(caps.get("max_images_with_native_mask", caps["max_images"])) if native else int(caps["max_images"])
    if caps.get("unverified"):
        print(f"generator recipe {caps.get('recipe')}: fields not verified against the model: "
              f"{', '.join(map(str, caps['unverified']))}", file=sys.stderr)
    # The project narrows what the recipe accepts, never widens it (design: Speed versions).
    wanted = g.capabilities
    capabilities = GeneratorCapabilities(frozenset(caps["roles"]) & wanted.roles, min(max_images, wanted.max_images), native)
    return ToolServerGenerator(client, ModelRef(str(caps["model"]), str(caps["revision"])), capabilities, str(caps.get("licence", "")))


def _chat(cfg: config.ProjectConfig) -> tuple[Chat, ModelRef]:
    j = cfg.judge
    if j.adapter == "fake":
        return FakeChat(), ModelRef("fake/judge", "1")
    endpoint = replace(_endpoint(j.endpoint, j.secret), timeout=float(j.timeout_seconds))

    def chat(messages: list[dict[str, object]], schema: dict[str, object]) -> str:
        return chat_json(endpoint, j.model, messages, schema, j.temperature, j.max_tokens, j.extra)

    return chat, ModelRef(j.model, j.revision + j.request.revision_suffix())


def _adapters(project: Path, cfg: config.ProjectConfig) -> Adapters:
    chat, judge_model = _chat(cfg)
    return Adapters(
        db_path=project / DB_NAME,
        blobs=BlobStore(project / "blobs"),
        generator=_generator(cfg),
        chat=chat,
        judge_model=judge_model,
        judge_box_scale=cfg.judge.box_scale,
        image_part=image_part,
        text_part=text_part,
        tools=_toolbox(cfg),
        use_class_diff=cfg.class_diff,
        use_inventory=cfg.inventory,
        use_structure_map=cfg.structure_map,
        workers=cfg.workers,
        fixed_settings=tuple(sorted(cfg.generator.settings.items())),
        judge_request=cfg.judge.request,
    )


def cmd_run(args: argparse.Namespace) -> int:
    conn, _ = _open(args.project)
    cfg = config.load(args.project, args.override)
    if args.resume is None and args.engine is None:
        print("error: give --engine for a new run, or --resume RUN", file=sys.stderr)
        return EXIT_USAGE
    if args.dry_run:
        planned = _names(args.photos) or [p.source_name for p in repo.photos(conn)]
        b = cfg.budget
        print(f"engine {args.engine}, {len(planned)} photos, at most {b.max_attempts} attempts and "
              f"{b.max_judge_calls} judge calls each: at most {len(planned) * b.max_attempts} generations")
        return EXIT_OK
    adapters = _adapters(args.project, cfg)
    if args.resume is not None:
        run_id = int(args.resume)
    else:
        rule_set_id = repo.latest_rule_set(conn)
        listed = _names(args.photos)
        names = listed if listed is not None else [
            p.source_name for p in repo.photos(conn)
            if (found := repo.eligibility(conn, p.photo_id, rule_set_id)) is not None and found.decision == "attempt"
        ]
        defects = load_defects()
        versions = RunVersions(
            engine=args.engine,
            label=args.label,
            budget=cfg.budget,
            minor_tolerance=cfg.minor_tolerance,
            release=load_release(defects),
            defects=defects,
            generator_stack=InstructionStack("generator", adapters.generator.model.name,
                                             load_base("generator", cfg.generator.instructions),
                                             config.overlay_text(args.project, "generator", cfg.generator.overlay)),
            judge_stack=InstructionStack("judge", adapters.judge_model.name, load_base("judge", cfg.judge.instructions),
                                         config.overlay_text(args.project, "judge", cfg.judge.overlay)),
            rule_set_id=rule_set_id,
        )
        run_id = create_run(conn, adapters, versions, names)
        print(f"run {run_id}: {args.engine}, {len(names)} photos; generator licence: {adapters.generator.licence or 'not stated'}",
              file=sys.stderr)
    outcomes = execute_run(adapters, run_id)
    print(json.dumps({"run": run_id, "outcomes": outcomes}))
    return EXIT_OK


def cmd_report(args: argparse.Namespace) -> int:
    conn, _ = _open(args.project)
    runs = args.runs or [int(r[0]) for r in conn.execute("SELECT run_id FROM run ORDER BY run_id")]
    report = build(conn, runs)
    if args.detectors:
        report["detectors"] = detector_report(conn, runs)
    text = render_text(report) + ("\n" + render_detectors(report["detectors"]) if args.detectors else "")
    print(to_json(report) if args.json else text)
    return EXIT_OK


def cmd_deliver(args: argparse.Namespace) -> int:
    conn, _ = _open(args.project)
    run = repo.run_row(conn, args.run)
    with transaction(conn):
        decided = repo.deliver_by_rule(conn, args.run, int(run["minor_tolerance"]))
    print(f"{decided} photos decided by rule; decisions taken by people kept")
    return EXIT_OK


def cmd_export(args: argparse.Namespace) -> int:
    conn, blobs = _open(args.project)
    folder: Path = args.folder
    folder.mkdir(parents=True, exist_ok=True)
    manifest = []
    for row in repo.deliveries(conn):
        name, outcome, decided_by, output, original = row
        entry = {"photo": name, "outcome": outcome, "decided_by": decided_by}
        if outcome == "emptied":
            target = (folder / f"{Path(name).stem}_empty.png").resolve()
            if folder.resolve() not in target.parents:
                raise ValueError(f"unsafe photo name {name!r}")
            target.write_bytes(blobs.get(output))
            entry["file"] = target.name
        manifest.append(entry)
    (folder / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"{sum(1 for m in manifest if 'file' in m)} images and manifest.json written to {folder}")
    return EXIT_OK


# --- review, serve, gpu: implemented in their own modules, imported only when used ---------------------------


def cmd_review(args: argparse.Namespace) -> int:
    from virtual_unstaging.review.server import serve_review

    _open(args.project)
    serve_review(args.project / DB_NAME, BlobStore(args.project / "blobs"), args.port, args.reviewer)
    return EXIT_OK


def cmd_serve(args: argparse.Namespace) -> int:
    from virtual_unstaging.serve.app import run_server

    run_server(
        host=args.host, port=args.port, deadline=args.deadline, key_file=args.key_file, key_env=args.key_env,
        recipe=args.recipe, tools=[t for t in args.tools.split(",") if t], data_dir=args.data_dir,
    )
    return EXIT_OK


def cmd_gpu(args: argparse.Namespace) -> int:
    from virtual_unstaging.provision.commands import gpu_command

    result: int = gpu_command(args)
    return result


if __name__ == "__main__":
    sys.exit(main())
