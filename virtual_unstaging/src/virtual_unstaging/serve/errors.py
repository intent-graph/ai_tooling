"""Stable error codes of the tool-server API, their HTTP statuses, and the exceptions that carry them."""

from __future__ import annotations

STATUS_OF_CODE: dict[str, int] = {
    "unauthorized": 401,
    "not_found": 404,
    "blob_missing": 404,
    "hash_mismatch": 400,
    "bad_request": 400,
    "generator_unavailable": 503,
    "generator_failed": 500,
    "generator_changed": 409,
    "tool_unknown": 404,
    "tool_failed": 500,
    "deadline_reached": 503,
}


class ApiError(Exception):
    """A failed call, answered as the HTTP status of its code plus `{"error": {"code", "message"}}`."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        if code not in STATUS_OF_CODE:
            raise ValueError(f"unknown error code {code!r}")
        self.code = code
        self.status = STATUS_OF_CODE[code]
        self.message = message

    def body(self) -> dict[str, dict[str, str]]:
        return {"error": {"code": self.code, "message": self.message}}


class ServeConfigError(ValueError):
    """The server cannot start as configured (no deadline, no key, unknown recipe or tool): a usage error."""
