"""Provisioning errors: every one carries a stable code, a message, and a hint on what to do next."""

from __future__ import annotations

# Codes that mean the command line was wrong (exit 2); every other code is a failure (exit 1).
USAGE_CODES = frozenset(
    {
        "limit_required",
        "limit_invalid",
        "limit_out_of_range",
        "confirmation_required",
        "provider_unknown",
        "recipe_invalid",
        "gpu_invalid",
    }
)


class ProvisionError(Exception):
    def __init__(self, code: str, message: str, hint: str = "") -> None:
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message
        self.hint = hint

    @property
    def exit_code(self) -> int:
        return 2 if self.code in USAGE_CODES else 1
