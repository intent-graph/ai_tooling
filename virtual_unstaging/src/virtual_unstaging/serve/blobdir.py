"""The tool server's blob directory: image bytes addressed by SHA-256, paths built from validated hashes only."""

from __future__ import annotations

import os
import re
import tempfile
from collections.abc import Iterable
from pathlib import Path

from virtual_unstaging.domain import sha256_bytes
from virtual_unstaging.serve.errors import ApiError

_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def is_sha256(text: str) -> bool:
    return bool(_SHA256.fullmatch(text))


class BlobDir:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def path(self, sha: str) -> Path:
        """The file of a blob; the hash is validated first, so no other text ever reaches the file system."""
        if not is_sha256(sha):
            raise ApiError("bad_request", "a blob address is 64 lowercase hexadecimal characters")
        return self.root / sha[:2] / sha

    def has(self, sha: str) -> bool:
        return self.path(sha).is_file()

    def size(self, sha: str) -> int:
        return self.path(sha).stat().st_size

    def get(self, sha: str) -> bytes:
        try:
            return self.path(sha).read_bytes()
        except FileNotFoundError:
            raise ApiError("not_found", f"no blob {sha}") from None

    def put(self, sha: str, data: bytes) -> None:
        """Store bytes under their hash (atomically); `hash_mismatch` unless they hash to `sha`."""
        target = self.path(sha)
        if sha256_bytes(data) != sha:
            raise ApiError("hash_mismatch", f"the bytes do not hash to {sha}")
        if target.is_file():
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        handle, temporary = tempfile.mkstemp(dir=target.parent, prefix=".part-")
        try:
            with os.fdopen(handle, "wb") as stream:
                stream.write(data)
            os.replace(temporary, target)
        except BaseException:
            Path(temporary).unlink(missing_ok=True)
            raise

    def add(self, data: bytes) -> str:
        """Store bytes under their own hash and return it."""
        sha = sha256_bytes(data)
        self.put(sha, data)
        return sha

    def missing(self, shas: Iterable[str]) -> list[str]:
        seen: list[str] = []
        for sha in shas:
            if sha not in seen and not self.has(sha):
                seen.append(sha)
        return seen
