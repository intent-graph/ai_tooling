"""Open a project database with the required pragmas, create its schema, run transactions."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from importlib import resources
from pathlib import Path

SCHEMA_VERSION = 2
MIGRATIONS = {2: "migrate_2.sql"}  # version reached -> the script that reaches it from the one before


def connect(path: Path) -> sqlite3.Connection:
    """One connection per thread; autocommit mode, so every write goes through `transaction`."""
    conn = sqlite3.connect(path, timeout=30.0, isolation_level=None, check_same_thread=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA busy_timeout = 30000")
    return conn


def create_schema(conn: sqlite3.Connection, backup: Path | None = None) -> None:
    """A new database gets the whole schema; an older one the migrations from its version, each in one transaction,
    after a copy of it to `<backup>.v<version>.bak` when `backup` names the database file."""
    version = conn.execute("PRAGMA user_version").fetchone()[0]
    if version == SCHEMA_VERSION:
        return
    if version > SCHEMA_VERSION:
        raise RuntimeError(f"database schema version {version}, this code knows {SCHEMA_VERSION}")
    files = resources.files("virtual_unstaging.store")
    if version == 0:
        sql = files.joinpath("schema.sql").read_text(encoding="utf-8")
        for step in range(2, SCHEMA_VERSION + 1):
            sql += "\n" + files.joinpath(MIGRATIONS[step]).read_text(encoding="utf-8")
        conn.executescript("BEGIN;\n" + sql + f"\nPRAGMA user_version = {SCHEMA_VERSION};\nCOMMIT;")
        return
    if backup is not None:  # before the first migration step: a copy the older code can still open
        with sqlite3.connect(backup.with_name(f"{backup.name}.v{version}.bak")) as copy:
            conn.backup(copy)
    for step in range(version + 1, SCHEMA_VERSION + 1):
        sql = files.joinpath(MIGRATIONS[step]).read_text(encoding="utf-8")
        conn.executescript("BEGIN;\n" + sql + f"\nPRAGMA user_version = {step};\nCOMMIT;")


@contextmanager
def transaction(conn: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    """BEGIN IMMEDIATE takes the write lock up front, so concurrent workers wait instead of deadlocking."""
    conn.execute("BEGIN IMMEDIATE")
    try:
        yield conn
    except BaseException:
        conn.execute("ROLLBACK")
        raise
    conn.execute("COMMIT")
