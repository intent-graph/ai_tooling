"""Renting the GPU through virtual_unstaging's provisioning: a plan built from this dataset's configuration, a session
file in the dataset folder, a rental row with its price and deadline (P4: no rental without a limit)."""

from __future__ import annotations

import sys
from collections.abc import Callable
from pathlib import Path

from virtual_unstaging.provision import lifecycle, switch, userfiles
from virtual_unstaging.provision.plan import (
    DEFAULT_DISK_GB,
    DEFAULT_GPU_PREFER,
    DEFAULT_IMAGE,
    DEFAULT_MIN_CUDA,
    DEFAULT_MIN_VRAM_GB,
    JudgePlan,
    ProjectPlan,
)

from clutter_pairs.config import Config
from clutter_pairs.store import repo
from clutter_pairs.store.db import open_store, transaction, utc_now


def project_plan(cfg: Config) -> ProjectPlan:
    """The machine: the tool server with the generator recipe and no tools, and the judge's chat server."""
    m, j = cfg.gpu.machine, cfg.gpu.judge
    judge = JudgePlan(
        model=cfg.judge.model, revision=None if cfg.judge.revision == "unpinned" else cfg.judge.revision,
        quantization=j.get("quantization"), max_model_len=int(j.get("max_model_len", 16384)),
        images_per_prompt=int(j.get("images_per_prompt", 4)),
        gpu_memory_utilization=j.get("gpu_memory_utilization"), max_num_seqs=int(j.get("max_num_seqs", 16)),
    )
    return ProjectPlan(
        name=cfg.folder.resolve().name, serves_generator_endpoint=True, judge=judge,
        image=str(m.get("image", DEFAULT_IMAGE)), min_cuda=str(m.get("min_cuda", DEFAULT_MIN_CUDA)),
        disk_gb=int(m.get("disk_gb", DEFAULT_DISK_GB)), min_vram_gb=int(m.get("min_vram_gb", DEFAULT_MIN_VRAM_GB)),
        gpu_prefer=tuple(m.get("gpu_prefer", DEFAULT_GPU_PREFER)), tools=(),
    )


def context(cfg: Config, interactive: bool, confirm: Callable[[str], bool]) -> lifecycle.Context:
    plan = project_plan(cfg)
    return lifecycle.Context(
        project=cfg.folder, config_folder=userfiles.config_dir(), state_folder=userfiles.state_dir(),
        interactive=interactive, confirm=confirm, progress=lambda message: print(message, file=sys.stderr, flush=True),
        plan_source=lambda project, overrides: plan,
    )


def up(cfg: Config, ctx: lifecycle.Context, limit: str | None, gpu: str | None, assume_yes: bool) -> tuple[str, str, float]:
    """Rent; returns (session id, deadline, price per hour). The provisioning refuses to start without a limit."""
    session = lifecycle.up(ctx, provider_name=cfg.gpu.provider, gpu=gpu or cfg.gpu.gpu, limit=limit,
                           recipe=cfg.generator.recipe, assume_yes=assume_yes)
    price = session.price_per_hour or session.estimated_price_per_hour
    started = (session.created_at or session.requested_at).isoformat(timespec="seconds")
    deadline = session.deadline.isoformat(timespec="seconds")
    conn, _ = open_store(cfg.folder)
    with transaction(conn):
        repo.create_rental(conn, cfg.gpu.provider, session.id, session.gpu, session.gpu_count, price, started, deadline)
    return session.id, deadline, price


def switch_judge(ctx: lifecycle.Context) -> str:
    """Serve the judge this dataset's configuration names on the live machine (its session file in the folder)."""
    model: str = switch.switch_judge(ctx)
    return model


def down(folder: Path, ctx: lifecycle.Context) -> list[str]:
    ended = lifecycle.down(ctx)
    conn, _ = open_store(folder)
    with transaction(conn):
        for session in ended:
            repo.end_rental(conn, session.id, utc_now())
    return [s.id for s in ended]
