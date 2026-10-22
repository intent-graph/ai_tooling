"""A dataset as the commands see it: its configuration, its store, the data files in force, its space and targets.

Opening a dataset records every data file in force (`source_file`, by content hash) and registers the reasons, the
space version and the target set, so every later row can point to them.
"""

from __future__ import annotations

import sqlite3
import tomllib
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import Any

from virtual_unstaging.store.blobs import BlobStore

from clutter_pairs import config
from clutter_pairs.compose import Composer, parse_composer
from clutter_pairs.config import Config, ConfigError
from clutter_pairs.space import Space, Target, check_sizes, parse_space, parse_targets
from clutter_pairs.store import repo
from clutter_pairs.store.db import DB_NAME, connect, open_store, transaction, utc_now

DECISION_RULE = "decision_rules/carry_forward.md"
ALWAYS_BLOCKING = ("opening_changed",)  # owner, 2026-10-22: a changed opening is the worst defect a pair can carry


@dataclass(frozen=True)
class Reason:
    stage: str
    severity: str
    by: str


@dataclass
class Dataset:
    folder: Path
    cfg: Config
    conn: sqlite3.Connection
    blobs: BlobStore
    files: dict[str, tuple[str, str]]  # packaged path -> (sha, content), every data file in force
    config_sha: str
    space: Space
    space_version_id: int
    targets: tuple[Target, ...]
    target_set_id: int
    reasons: dict[str, Reason]
    rule: dict[str, Any]  # the carry-forward decision rule's parameters
    sizes: dict[str, tuple[int, int]]  # each camera's image size

    def connect(self) -> sqlite3.Connection:
        """Another connection to the store, for a worker thread."""
        return connect(self.folder / DB_NAME)

    def file(self, packaged: str) -> tuple[str, str]:
        return self.files[packaged]

    def composer(self, name: str) -> tuple[str, Composer]:
        sha, content = self.files[f"composers/{name}.toml"]
        return sha, parse_composer(name, content)

    def severities(self) -> dict[str, str]:
        return {code: r.severity for code, r in self.reasons.items()}

    def judge_codes(self, stage: str) -> set[str]:
        """The codes a judge's answer may carry at a stage."""
        return {c for c, r in self.reasons.items() if r.stage in (stage, "both") and r.by in ("judge", "both")}


def packaged_files() -> list[str]:
    """Every data file shipped with the package, as `folder/name` paths."""
    root = resources.files("clutter_pairs.data")
    out = ["reasons.toml"]
    for folder in config.DATA_FOLDERS:
        for entry in sorted(root.joinpath(folder).iterdir(), key=lambda e: e.name):
            if entry.is_file() and not entry.name.startswith((".", "_")):
                out.append(f"{folder}/{entry.name}")
    return out


def open_dataset(folder: Path) -> Dataset:
    cfg = config.load(folder)
    conn, blobs = open_store(folder)
    now = utc_now()
    files: dict[str, tuple[str, str]] = {}
    with transaction(conn):
        for packaged in packaged_files():
            label, content = config.read_data_file(cfg, packaged)
            files[packaged] = (repo.record_file(conn, config.file_kind(packaged), label, content, now), content)
        config_sha = repo.record_file(conn, "config", config.CONFIG_NAME, cfg.text, now)
        reasons = parse_reasons(files["reasons.toml"][1])
        repo.register_reasons(conn, {c: (r.stage, r.severity) for c, r in reasons.items()}, files["reasons.toml"][0])
        space = parse_space(files["space/ontology.toml"][1], files["space/taxonomy.toml"][1])
        version = repo.register_space(conn, space, files["space/ontology.toml"][0], files["space/taxonomy.toml"][0])
        targets = parse_targets(files["space/targets.toml"][1], space)
        target_set = repo.register_targets(conn, version, files["space/targets.toml"][0], targets)
    sizes = check_sizes(space, cfg.run.output_side, cfg.generator.size_multiple, cfg.generator.condition_max_pixels)
    return Dataset(folder, cfg, conn, blobs, files, config_sha, space, version, targets, target_set, reasons,
                   parse_rule(files[DECISION_RULE][1]), sizes)


def parse_reasons(text: str) -> dict[str, Reason]:
    data = tomllib.loads(text)
    out: dict[str, Reason] = {}
    for code, body in data.items():
        if (not isinstance(body, dict) or body.get("stage") not in ("clean", "clutter", "both")
                or body.get("severity") not in ("blocking", "minor") or body.get("by") not in ("judge", "pixels", "both")):
            raise ConfigError(f"reasons.toml [{code}]: stage, severity and by are required")
        out[code] = Reason(body["stage"], body["severity"], body["by"])
    for code in ALWAYS_BLOCKING:
        if code not in out or out[code].severity != "blocking" or f"{code}_minor" in out:
            raise ConfigError(f"reasons.toml: {code} is blocking and has no _minor twin (owner's rule)")
    return out


def parse_rule(text: str) -> dict[str, Any]:
    """The parameters of a decision rule: the one ```toml block of its Markdown file."""
    start = text.find("```toml\n")
    end = text.find("```", start + 8)
    if start < 0 or end < 0:
        raise ConfigError(f"{DECISION_RULE}: no ```toml block of parameters")
    rule = tomllib.loads(text[start + 8:end])
    required = {"off_share", "min_difference", "alpha", "permutations", "permutation_seed", "min_loops_per_arm"}
    if set(rule) != required:
        raise ConfigError(f"{DECISION_RULE}: the parameters are {sorted(required)}")
    return rule
