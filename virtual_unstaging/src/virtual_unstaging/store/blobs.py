"""Content-addressed image store: files named by the SHA-256 of their bytes, written once, never modified."""

from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path

from virtual_unstaging.domain import sha256_bytes

_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def check_sha256(sha: str) -> str:
    """A hash is the only thing a blob path is built from: validate it before it touches the file system."""
    if not _SHA256.fullmatch(sha):
        raise ValueError(f"not a SHA-256 hex digest: {sha!r}")
    return sha


class BlobStore:
    def __init__(self, root: Path) -> None:
        self.root = root

    def path(self, sha: str) -> Path:
        check_sha256(sha)
        return self.root / sha[:2] / sha

    def has(self, sha: str) -> bool:
        return self.path(sha).is_file()

    def put(self, data: bytes) -> str:
        sha = sha256_bytes(data)
        target = self.path(sha)
        if target.is_file():
            return sha
        target.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=target.parent, prefix=".tmp-")
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
            os.replace(tmp, target)
        except BaseException:
            Path(tmp).unlink(missing_ok=True)
            raise
        return sha

    def get(self, sha: str) -> bytes:
        data = self.path(sha).read_bytes()
        if sha256_bytes(data) != sha:
            raise ValueError(f"blob {sha} is corrupted")
        return data
