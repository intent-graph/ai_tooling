"""The time limit: parsed from a positive grammar, bounded, and printed back."""

from __future__ import annotations

import re

from virtual_unstaging.provision.errors import ProvisionError

MIN_LIMIT_SECONDS = 5 * 60
MAX_LIMIT_SECONDS = 24 * 3600
_LIMIT = re.compile(r"^(?:(?P<h>[0-9]{1,2})h)?(?:(?P<m>[0-9]{1,4})m)?(?:(?P<s>[0-9]{1,6})s)?$")


def parse_limit(text: str | None) -> int:
    """`3h`, `90m`, `1h30m`, `45m30s` to seconds. A missing limit is refused: no machine runs without one."""
    if text is None or not text.strip():
        raise ProvisionError(
            "limit_required",
            "a GPU is never rented without a time limit",
            "pass --limit, for example --limit 3h (between 5m and 24h)",
        )
    match = _LIMIT.fullmatch(text.strip().lower())
    if match is None or not any(match.group(name) for name in ("h", "m", "s")):
        raise ProvisionError("limit_invalid", f"cannot read {text!r} as a duration", "use forms like 3h, 90m, 1h30m")
    seconds = int(match["h"] or 0) * 3600 + int(match["m"] or 0) * 60 + int(match["s"] or 0)
    if not MIN_LIMIT_SECONDS <= seconds <= MAX_LIMIT_SECONDS:
        raise ProvisionError(
            "limit_out_of_range",
            f"{text!r} is {format_seconds(seconds)}; the limit must be between 5m and 24h",
            "a longer job is rented again after the deadline (`gpu up`, then `run --resume`)",
        )
    return seconds


def format_seconds(seconds: float) -> str:
    total = int(round(seconds))
    hours, rest = divmod(total, 3600)
    minutes, secs = divmod(rest, 60)
    if hours:
        return f"{hours}h{minutes:02d}m"
    if minutes:
        return f"{minutes}m{secs:02d}s" if secs else f"{minutes}m"
    return f"{secs}s"
