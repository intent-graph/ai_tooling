"""Open a dataset's store: the database with virtual_unstaging's pragmas and this package's schema, the image store."""

from __future__ import annotations

import sqlite3
from datetime import UTC, datetime
from importlib import resources
from pathlib import Path

from virtual_unstaging.store.blobs import BlobStore
from virtual_unstaging.store.db import connect, transaction

SCHEMA_VERSION = 3  # 2: numbered mask regions (judge aid A2); 3: imported clean images
DB_NAME = "store.sqlite"
IMAGES_DIR = "images"

__all__ = ["BlobStore", "connect", "create_schema", "open_store", "transaction", "utc_now"]


def create_schema(conn: sqlite3.Connection) -> None:
    version = conn.execute("PRAGMA user_version").fetchone()[0]
    if version == SCHEMA_VERSION:
        return
    if version != 0:
        raise RuntimeError(f"store schema version {version}, this code knows {SCHEMA_VERSION}")
    sql = resources.files("clutter_pairs.store").joinpath("schema.sql").read_text(encoding="utf-8")
    conn.executescript("BEGIN;\n" + sql + f"\nPRAGMA user_version = {SCHEMA_VERSION};\nCOMMIT;")


def open_store(folder: Path) -> tuple[sqlite3.Connection, BlobStore]:
    """The dataset folder's database (created on first use) and its image store."""
    conn = connect(folder / DB_NAME)
    create_schema(conn)
    return conn, BlobStore(folder / IMAGES_DIR)


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")
