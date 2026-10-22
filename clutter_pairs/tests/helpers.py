"""Shared steps of the integration tests: open, plan and run a dataset on the fake model server."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from clutter_pairs import config, plan, run
from clutter_pairs.dataset import Dataset, open_dataset
from clutter_pairs.store import repo
from clutter_pairs.store.db import transaction


def run_dataset(folder: Path, smoke: bool = False, deadline: datetime | None = None) -> tuple[Dataset, run.RunSummary]:
    ds = open_dataset(folder)
    with transaction(ds.conn):
        plan.plan(ds.conn, ds)
    thresholds = config.thresholds(ds.cfg, repo.threshold_decisions(ds.conn))
    options = run.RunOptions(smoke=smoke, deadline=deadline, replan=lambda conn: plan.plan(conn, ds))
    return ds, run.execute(ds, run.connect_models(ds, retries=0), thresholds, options)
