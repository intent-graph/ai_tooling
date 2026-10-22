"""`unstage gpu up|down|ls|price`: arguments in, exit code out; data on stdout, progress and errors on stderr."""

from __future__ import annotations

import argparse
import signal
import sys
import tomllib
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from types import FrameType
from typing import Any

from virtual_unstaging.provision import lifecycle, plan, sessions, switch, userfiles
from virtual_unstaging.provision.errors import ProvisionError
from virtual_unstaging.provision.sessions import Session

EXIT_OK, EXIT_INTERRUPTED = 0, 130


def default_context(args: argparse.Namespace) -> lifecycle.Context:
    """The real folders, terminal and clock. Tests build their own `Context` instead."""

    def say(message: str) -> None:
        print(message, file=sys.stderr, flush=True)

    def ask(prompt: str) -> bool:
        print(prompt, end="", file=sys.stderr, flush=True)
        return sys.stdin.readline().strip().lower() in ("y", "yes")

    return lifecycle.Context(
        project=Path(args.project),
        config_folder=userfiles.config_dir(),
        state_folder=userfiles.state_dir(),
        interactive=sys.stdin.isatty() and sys.stderr.isatty(),
        confirm=ask,
        progress=say,
        overrides=tuple(getattr(args, "override", None) or ()),
    )


@contextmanager
def terminate_as_interrupt() -> Iterator[None]:
    """SIGTERM and SIGHUP end `up` like Ctrl-C does, so the cleanup that deletes a half-started machine runs."""
    saved: dict[signal.Signals, Any] = {}

    def raise_interrupt(signum: int, frame: FrameType | None) -> None:
        raise KeyboardInterrupt

    try:
        for number in (signal.SIGTERM, signal.SIGHUP):
            saved[number] = signal.signal(number, raise_interrupt)
    except ValueError:  # not the main thread: no handlers, the exceptions still clean up
        saved.clear()
    try:
        yield
    finally:
        for number, handler in saved.items():
            signal.signal(number, handler)


def gpu_command(args: argparse.Namespace, context: lifecycle.Context | None = None) -> int:
    """Run one `gpu` action; returns the exit code (0 success, 1 failure, 2 usage, 130 interrupted)."""
    try:
        ctx = context or default_context(args)
        action = args.action
        if action == "up":
            with terminate_as_interrupt():
                _up(ctx, args)
        elif action == "down":
            _down(ctx)
        elif action == "ls":
            _ls(ctx)
        elif action == "price":
            _price(ctx, args)
        elif action == "recipe":
            _recipe(ctx, args)
        elif action == "judge":
            print(f"judge\t{switch.switch_judge(ctx)}")
        else:
            raise ProvisionError("action_unknown", f"unknown action {action!r}")
    except ProvisionError as error:
        print(f"error [{error.code}]: {error.message}", file=sys.stderr)
        if error.hint:
            print(f"hint: {error.hint}", file=sys.stderr)
        return error.exit_code
    except KeyboardInterrupt:
        print("interrupted: any machine already created was deleted", file=sys.stderr)
        return EXIT_INTERRUPTED
    return EXIT_OK


def _up(ctx: lifecycle.Context, args: argparse.Namespace) -> None:
    session = lifecycle.up(
        ctx, provider_name=args.provider, gpu=args.gpu, limit=args.limit, recipe=args.recipe, assume_yes=args.yes
    )
    tools = _endpoint(ctx, "tools")
    judge = _endpoint(ctx, "judge")
    print(f"session\t{session.id}")
    print(f"tools\t{tools}")
    if judge:
        print(f"judge\t{judge}")
    print(f"deadline\t{sessions.to_iso(session.deadline)}")
    ctx.progress(f"{ctx.session_path.name} written; `unstage gpu down` ends the session before the deadline")


def _recipe(ctx: lifecycle.Context, args: argparse.Namespace) -> None:
    name = getattr(args, "name", None)
    if not name:
        raise ProvisionError("recipe_invalid", "name the recipe to load", "unstage gpu recipe <name>")
    profile = switch.switch_generator(ctx, plan.check_recipe(name) or name)
    print(f"generator\t{profile.get('recipe', name)}\t{profile.get('model', '')}\t{profile.get('revision', '')}")


def _endpoint(ctx: lifecycle.Context, section: str) -> str:
    """Read back the endpoint written to the session file (one place per fact)."""
    data = tomllib.loads(ctx.session_path.read_text(encoding="utf-8"))
    return str(data.get(section, {}).get("endpoint", ""))


def _down(ctx: lifecycle.Context) -> None:
    for ended in lifecycle.down(ctx):
        hours = ended.hours(ctx.now())
        print(f"ended\t{ended.id}\t{hours:.2f} h\t${ended.cost(ctx.now()):.2f} estimated")
    ctx.progress("the provider's billing page is the truth for the cost")


def _ls(ctx: lifecycle.Context) -> None:
    listing = lifecycle.ls(ctx)
    now = ctx.now()
    print("session\tstate\tproject\tgpu\tprice_per_hour\thours\test_cost\tdeadline")
    for s in listing.sessions:
        print(_row(s, now))
    for warning in listing.warnings:
        ctx.progress(f"warning: {warning}")


def _row(s: Session, now: datetime) -> str:
    rate = s.price_per_hour or s.estimated_price_per_hour
    count = f"{s.gpu_count}x " if s.gpu_count > 1 else ""
    return "\t".join(
        [s.id, s.state, s.project, f"{count}{s.gpu}", f"{rate:.2f}", f"{s.hours(now):.2f}", f"{s.cost(now):.2f}",
         sessions.to_iso(s.deadline)]
    )


def _price(ctx: lifecycle.Context, args: argparse.Namespace) -> None:
    offers = lifecycle.price(ctx, args.provider, args.gpu)
    print("gpu\tmemory_gb\tprice_per_hour\tstock\tdatacenters_in_stock")
    for o in offers:
        stocked = ",".join(dc for dc, level in o.datacenters if level != "NONE")
        print(f"{o.gpu_id}\t{o.memory_gb}\t{o.price_per_hour:.2f}\t{o.stock.lower()}\t{stocked}")
    ctx.progress(f"{len(offers)} GPU types; list price per GPU-hour in USD, secure cloud")
