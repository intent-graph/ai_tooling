"""Domain exceptions for CodeMap operations."""


class CodeMapError(Exception):
    """Base exception for all CodeMap operations."""


class ParseError(CodeMapError):
    """Raised when a file or project cannot be parsed.

    Includes the file path and underlying cause in the message.
    """


class NodeNotFoundError(CodeMapError):
    """Raised when a qualified_name doesn't exist in the graph."""
