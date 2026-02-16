"""Conversation history tracking for verification checkpoint."""

_history: dict[str, str] = {}


def record_response(checkpoint_id: str, text: str) -> None:
    """Save a response for later recall."""
    _history[checkpoint_id] = text


def get_response(checkpoint_id: str) -> str:
    """Retrieve a previously recorded response."""
    if checkpoint_id in _history:
        return _history[checkpoint_id]

    # If not found, try finding most recent manifest_* entry
    if checkpoint_id == "manifest":
        manifest_keys = [k for k in _history.keys() if k.startswith("manifest_")]
        if manifest_keys:
            # Return the most recent one
            last_key = sorted(manifest_keys)[-1]
            return _history[last_key]

    raise KeyError(f"No response found for checkpoint: {checkpoint_id}")


def extract_word(text: str, position: int) -> str:
    """Get the Nth word from text (1-indexed)."""
    words = text.split()
    if position < 1 or position > len(words):
        raise IndexError(f"Position {position} out of range for {len(words)} words")
    return words[position - 1]


def clear_history() -> None:
    """Clear all recorded responses (for new challenge runs)."""
    _history.clear()
