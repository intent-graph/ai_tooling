"""Entry point for the sample project."""

from sample_project.models import User
from sample_project.utils import format_name


def create_user(first: str, last: str, email: str) -> User:
    """Create and validate a new user."""
    name = format_name(first, last)
    user = User(name=name, email=email)
    user.validate()
    return user
