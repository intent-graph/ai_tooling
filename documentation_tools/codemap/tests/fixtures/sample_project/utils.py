"""Utility functions for the sample project."""


def check_email(email: str) -> bool:
    """Check if an email address is valid."""
    return "@" in email


def format_name(first: str, last: str) -> str:
    """Format a full name from parts."""
    return f"{first} {last}"
