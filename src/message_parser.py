"""Message parsing and fragment reconstruction."""


def sort_fragments(fragments: list[dict]) -> list[dict]:
    """Sort fragments by timestamp in ascending order."""
    return sorted(fragments, key=lambda f: f["timestamp"])


def join_words(fragments: list[dict]) -> str:
    """Join fragment words with spaces."""
    words = [f["word"] for f in fragments]
    return " ".join(words)


def reconstruct_message(fragments: list[dict]) -> str:
    """Reconstruct message from fragments: sort by timestamp, join words."""
    sorted_frags = sort_fragments(fragments)
    return join_words(sorted_frags)


def parse_challenge(message: dict) -> str:
    """Extract and reconstruct the challenge message from NEON."""
    if "message" not in message:
        raise ValueError(f"No 'message' field in: {message}")

    fragments = message["message"]
    return reconstruct_message(fragments)
