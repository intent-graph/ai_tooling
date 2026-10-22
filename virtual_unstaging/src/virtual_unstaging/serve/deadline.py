"""The server's deadline: parsed from a duration or an ISO 8601 UTC time, checked on every request."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from virtual_unstaging.serve.errors import ServeConfigError

_DURATION = re.compile(r"^(?:(?P<h>\d{1,4})h)?(?:(?P<m>\d{1,5})m)?(?:(?P<s>\d{1,7})s)?$")


def utc_now() -> datetime:
    return datetime.now(UTC)


def parse_deadline(text: str, now: datetime) -> datetime:
    """A duration ("90m", "2h", "1h30m", "45s") counted from `now`, or an ISO 8601 time with a UTC offset."""
    text = text.strip()
    if not text:
        raise ServeConfigError("the server needs a deadline: a duration such as 90m or 2h, or an ISO 8601 UTC time")
    match = _DURATION.fullmatch(text)
    if match and any(match.group(part) for part in ("h", "m", "s")):
        delta = timedelta(
            hours=int(match.group("h") or 0), minutes=int(match.group("m") or 0), seconds=int(match.group("s") or 0)
        )
        if delta <= timedelta(0):
            raise ServeConfigError(f"the deadline {text!r} is not in the future")
        return now + delta
    try:
        moment = datetime.fromisoformat(text)
    except ValueError:
        raise ServeConfigError(f"the deadline {text!r} is neither a duration (90m, 2h) nor an ISO 8601 UTC time") from None
    if moment.tzinfo is None or moment.utcoffset() != timedelta(0):
        raise ServeConfigError(f"the deadline {text!r} must carry a UTC offset (Z or +00:00)")
    moment = moment.astimezone(UTC)
    if moment <= now:
        raise ServeConfigError(f"the deadline {text!r} is already past")
    return moment


@dataclass(frozen=True)
class Deadline:
    at: datetime
    clock: Callable[[], datetime] = utc_now

    def expired(self) -> bool:
        return self.clock() >= self.at

    def seconds_left(self) -> int:
        return max(0, int((self.at - self.clock()).total_seconds()))

    def iso(self) -> str:
        return self.at.strftime("%Y-%m-%dT%H:%M:%SZ")
