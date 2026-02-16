"""Base checkpoint handler protocol."""

from typing import Protocol


class CheckpointHandler(Protocol):
    """Protocol for checkpoint handlers."""

    def handle(self, prompt: str) -> dict:
        """Handle a checkpoint prompt and return response dict."""
        ...
