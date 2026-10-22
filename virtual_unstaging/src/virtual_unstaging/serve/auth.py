"""The bearer key: read once at start from a file or from a named environment variable, compared in constant time."""

from __future__ import annotations

import hmac
import os
import re
from collections.abc import Mapping
from pathlib import Path

from virtual_unstaging.serve.errors import ServeConfigError

MIN_KEY_LENGTH = 16
_KEY = re.compile(r"^[\x21-\x7e]+$")  # printable ASCII, no whitespace
_ENV_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def load_key(key_file: Path | None, key_env: str | None, environ: Mapping[str, str] | None = None) -> str:
    """The key from exactly one source: `key_file` (preferred), or the variable named by `key_env`."""
    if (key_file is None) == (key_env is None):
        raise ServeConfigError("give the key by exactly one of --key-file or --key-env")
    if key_file is not None:
        try:
            raw = Path(key_file).read_text(encoding="utf-8")
        except OSError as error:
            raise ServeConfigError(f"cannot read the key file: {error.strerror or error}") from None
        origin = "the key file"
    else:
        assert key_env is not None
        if not _ENV_NAME.fullmatch(key_env):
            raise ServeConfigError(f"{key_env!r} is not an environment variable name")
        raw = (os.environ if environ is None else environ).get(key_env, "")
        origin = f"the environment variable {key_env}"
    key = raw.strip()
    if not key:
        raise ServeConfigError(f"{origin} is empty")
    if len(key) < MIN_KEY_LENGTH or not _KEY.fullmatch(key):
        raise ServeConfigError(f"{origin} must hold at least {MIN_KEY_LENGTH} printable characters without spaces")
    return key


def bearer_matches(header: str | None, key: str) -> bool:
    """True when the Authorization header is exactly `Bearer <key>`."""
    if header is None:
        return False
    scheme, _, token = header.partition(" ")
    return scheme.lower() == "bearer" and hmac.compare_digest(token.strip().encode(), key.encode())
