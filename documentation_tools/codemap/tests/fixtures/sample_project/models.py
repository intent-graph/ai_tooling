"""Data models for the sample project."""

from sample_project.utils import check_email


class BaseModel:
    """Base class for all models."""

    def save(self) -> None:
        """Persist the model."""
        pass


class User(BaseModel):
    """A user in the system."""

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def validate(self) -> bool:
        """Validate user data against rules."""
        return check_email(self.email)


class Order(BaseModel):
    """An order placed by a user."""

    def __init__(self, user: User, total: float) -> None:
        self.user = user
        self.total = total
