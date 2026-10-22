"""Parse what a browser sends into typed requests, under a positive definition of valid; anything else is refused."""

from __future__ import annotations

import json
import re
from collections.abc import Collection, Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import parse_qsl

from virtual_unstaging.domain import SEVERITIES, Box, Severity
from virtual_unstaging.review.errors import ReviewError

MAX_BODY_BYTES = 64 * 1024
MAX_COMMENT_CHARS = 2000
MAX_FINDINGS = 50
MAX_ID = 2**31 - 1

VERDICTS = ("usable", "unusable")
CHOICES = ("a", "b", "equal", "both_unusable")
OUTCOMES = ("emptied", "original", "excluded")

_INTEGER = re.compile(r"[0-9]{1,10}")
_REVIEWER = re.compile(r"\w[\w .@-]{0,63}")


def invalid(field: str, why: str) -> ReviewError:
    """An `invalid_body` refusal naming the field, never echoing the value."""
    return ReviewError(400, "invalid_body", f"{field}: {why}")


def check_reviewer(name: str) -> str:
    """A reviewer name is stored in `decided_by`: letters, digits, space and `._@-`, 1 to 64 characters."""
    if not _REVIEWER.fullmatch(name):
        raise ValueError("invalid_reviewer: use 1 to 64 letters, digits, spaces or . _ @ -")
    return name


# --- Query strings -----------------------------------------------------------------------------------------------


def parse_query(query: str) -> dict[str, str]:
    """A query string as a dict; a repeated parameter is refused."""
    try:
        pairs = parse_qsl(query, keep_blank_values=True, strict_parsing=bool(query), max_num_fields=16)
    except ValueError:
        raise ReviewError(400, "invalid_query", "the query string is malformed") from None
    result: dict[str, str] = {}
    for key, value in pairs:
        if key in result:
            raise ReviewError(400, "invalid_query", f"{key}: repeated")
        result[key] = value
    return result


def query_id(params: Mapping[str, str], name: str) -> int:
    value = params.get(name, "")
    if not _INTEGER.fullmatch(value) or not 1 <= int(value) <= MAX_ID:
        raise ReviewError(400, "invalid_query", f"{name}: a positive integer is required")
    return int(value)


# --- JSON bodies -------------------------------------------------------------------------------------------------


def _no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def _no_constants(name: str) -> Any:
    raise ValueError(f"{name} is not JSON")


def parse_json_object(raw: bytes) -> dict[str, Any]:
    """Strict JSON: UTF-8, one object, no duplicate keys, no NaN or Infinity."""
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_no_duplicate_keys, parse_constant=_no_constants)
    except (ValueError, RecursionError):
        raise ReviewError(400, "invalid_json", "the body is not one strict JSON object") from None
    if not isinstance(value, dict):
        raise ReviewError(400, "invalid_json", "the body is not one strict JSON object")
    return value


def _fields(body: Mapping[str, Any], required: Collection[str], optional: Collection[str] = ()) -> None:
    missing = sorted(set(required) - set(body))
    unknown = sorted(set(body) - set(required) - set(optional))
    if missing:
        raise invalid(missing[0], "missing")
    if unknown:
        raise invalid(unknown[0], "unknown field")


def _integer_id(value: object, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= MAX_ID:
        raise invalid(field, "a positive integer is required")
    return value


def _choice(value: object, allowed: tuple[str, ...], field: str) -> str:
    if not isinstance(value, str) or value not in allowed:
        raise invalid(field, "not one of the allowed values")
    return value


def _comment(value: object, field: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or len(value) > MAX_COMMENT_CHARS:
        raise invalid(field, f"text of at most {MAX_COMMENT_CHARS} characters is required")
    if any(ord(c) < 32 and c not in "\n\t" for c in value):
        raise invalid(field, "control characters are not allowed")
    return value.strip() or None


def _box(value: object, field: str) -> Box | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise invalid(field, "an object x0, y0, x1, y1 or null is required")
    _fields(value, ("x0", "y0", "x1", "y1"))
    numbers: list[float] = []
    for key in ("x0", "y0", "x1", "y1"):
        coordinate = value[key]
        if isinstance(coordinate, bool) or not isinstance(coordinate, int | float):
            raise invalid(f"{field}.{key}", "a number is required")
        numbers.append(float(coordinate))
    try:
        return Box(*numbers)
    except ValueError:
        raise invalid(field, "a box needs 0 <= x0 < x1 <= 1 and 0 <= y0 < y1 <= 1") from None


# --- Typed requests ----------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class FindingIn:
    defect_code: str
    severity: Severity
    box: Box | None
    comment: str | None


@dataclass(frozen=True)
class ReviewIn:
    attempt_id: int
    verdict: str
    comment: str | None
    findings: tuple[FindingIn, ...]


@dataclass(frozen=True)
class PreferenceIn:
    attempt_a: int
    attempt_b: int
    shown_left: int
    choice: str


@dataclass(frozen=True)
class DeliveryIn:
    photo_id: int
    outcome: str
    attempt_id: int | None
    reason: str | None


def parse_review(body: Mapping[str, Any], known_codes: Collection[str]) -> ReviewIn:
    _fields(body, ("attempt_id", "verdict"), ("comment", "findings"))
    raw_findings = body.get("findings", [])
    if not isinstance(raw_findings, list) or len(raw_findings) > MAX_FINDINGS:
        raise invalid("findings", f"a list of at most {MAX_FINDINGS} findings is required")
    findings: list[FindingIn] = []
    for index, item in enumerate(raw_findings):
        name = f"findings[{index}]"
        if not isinstance(item, dict):
            raise invalid(name, "an object is required")
        _fields(item, ("defect_code", "severity"), ("box", "comment"))
        code = item["defect_code"]
        if not isinstance(code, str) or code not in known_codes:
            raise ReviewError(400, "unknown_defect", f"{name}.defect_code: not a code of the defect taxonomy")
        severity = _choice(item["severity"], SEVERITIES, f"{name}.severity")
        findings.append(
            FindingIn(code, severity, _box(item.get("box"), f"{name}.box"), _comment(item.get("comment"), f"{name}.comment"))  # type: ignore[arg-type]
        )
    return ReviewIn(
        _integer_id(body["attempt_id"], "attempt_id"),
        _choice(body["verdict"], VERDICTS, "verdict"),
        _comment(body.get("comment"), "comment"),
        tuple(findings),
    )


def parse_preference(body: Mapping[str, Any]) -> PreferenceIn:
    _fields(body, ("attempt_a", "attempt_b", "shown_left", "choice"))
    a = _integer_id(body["attempt_a"], "attempt_a")
    b = _integer_id(body["attempt_b"], "attempt_b")
    left = _integer_id(body["shown_left"], "shown_left")
    if a == b:
        raise invalid("attempt_b", "the two attempts must differ")
    if left not in (a, b):
        raise invalid("shown_left", "must be one of the two attempts")
    return PreferenceIn(a, b, left, _choice(body["choice"], CHOICES, "choice"))


def parse_delivery(body: Mapping[str, Any]) -> DeliveryIn:
    _fields(body, ("photo_id", "outcome"), ("attempt_id", "reason"))
    outcome = _choice(body["outcome"], OUTCOMES, "outcome")
    attempt_id = None if body.get("attempt_id") is None else _integer_id(body["attempt_id"], "attempt_id")
    if (outcome == "emptied") != (attempt_id is not None):
        raise invalid("attempt_id", "required with outcome emptied, and only then")
    return DeliveryIn(_integer_id(body["photo_id"], "photo_id"), outcome, attempt_id, _comment(body.get("reason"), "reason"))
