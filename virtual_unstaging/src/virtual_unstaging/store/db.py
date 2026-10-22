"""Open a project database with the required pragmas, create its schema, run transactions."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from importlib import resources
from pathlib import Path

SCHEMA_VERSION = 1


def connect(path: Path) -> sqlite3.Connection:
    """One connection per thread; autocommit mode, so every write goes through `transaction`."""
    conn = sqlite3.connect(path, timeout=30.0, isolation_level=None, check_same_thread=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA busy_timeout = 30000")
    return conn


def create_schema(conn: sqlite3.Connection) -> None:
    version = conn.execute("PRAGMA user_version").fetchone()[0]
    if version == SCHEMA_VERSION:
        return
    if version != 0:
        raise RuntimeError(f"database schema version {version}, this code knows {SCHEMA_VERSION}")
    sql = resources.files("virtual_unstaging.store").joinpath("schema.sql").read_text(encoding="utf-8")
    conn.executescript("BEGIN;\n" + sql + f"\nPRAGMA user_version = {SCHEMA_VERSION};\nCOMMIT;")


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
