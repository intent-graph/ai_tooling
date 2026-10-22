"""The user's own files: the config and state folders, the provider key sources, and the session key files."""

from __future__ import annotations

import os
import secrets
import tomllib
from dataclasses import dataclass
from pathlib import Path

from virtual_unstaging.config import Secret, SecretError
from virtual_unstaging.provision.errors import ProvisionError

APP_FOLDER = "virtual-unstaging"
USER_CONFIG_NAME = "provision.toml"
KEYS_FOLDER = "keys"
_SOURCE_KEYS = {"key_file", "key_command"}


def config_dir() -> Path:
    base = os.environ.get("XDG_CONFIG_HOME")
    return (Path(base) if base else Path.home() / ".config") / APP_FOLDER


def state_dir() -> Path:
    base = os.environ.get("XDG_STATE_HOME")
    return (Path(base) if base else Path.home() / ".local" / "state") / APP_FOLDER


@dataclass(frozen=True)
class KeySource:
    """Where a service key is read from: a file (mode 600) or a command run without a shell."""

    key_file: str = ""
    key_command: tuple[str, ...] = ()


def key_source(config_folder: Path, section: str, default_file: str) -> KeySource:
    """The `[<section>]` of `provision.toml` in the config folder; without it, the default key file."""
    path = config_folder / USER_CONFIG_NAME
    if not path.is_file():
        return KeySource(key_file=str(config_folder / default_file))
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise ProvisionError("user_config_invalid", f"{path}: {error}") from error
    for name, values in data.items():
        if not isinstance(values, dict) or set(values) - _SOURCE_KEYS:
            raise ProvisionError(
                "user_config_invalid", f"{path}: [{name}] takes only key_file and key_command (a key is never written here)"
            )
    values = data.get(section, {})
    command = values.get("key_command", [])
    if not isinstance(command, list) or not all(isinstance(part, str) for part in command):
        raise ProvisionError("user_config_invalid", f"{path}: key_command must be a list of strings (no shell)")
    key_file = values.get("key_file", "")
    if not isinstance(key_file, str):
        raise ProvisionError("user_config_invalid", f"{path}: key_file must be a string")
    if not key_file and not command:
        key_file = str(config_folder / default_file)
    return KeySource(key_file=key_file, key_command=tuple(command))


def read_key(source: KeySource, what: str) -> str:
    """The key's text, read by the project's one key reader (`config.Secret`). Never echoed."""
    try:
        value = Secret(source.key_file, source.key_command).read()
    except SecretError as error:
        hint = "write the key there (chmod 600) or name a key_command" if error.code == "key_missing" else ""
        raise ProvisionError(error.code, f"{what}: {error}", hint) from None
    if value is None:
        raise ProvisionError("key_missing", f"{what}: no key source named")
    return value


def new_session_key() -> str:
    """One key per session, for the machine's endpoints; it dies with the machine."""
    return secrets.token_urlsafe(32)


def write_session_key(config_folder: Path, session: str, key: str) -> Path:
    """Create the key file for a session, mode 600, refusing to overwrite."""
    folder = config_folder / KEYS_FOLDER
    folder.mkdir(parents=True, exist_ok=True, mode=0o700)
    path = folder / f"session-{session}.key"
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(key + "\n")
    return path


def remove_session_key(path: Path) -> None:
    path.unlink(missing_ok=True)
