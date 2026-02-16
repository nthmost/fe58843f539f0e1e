"""Knowledge archive query checkpoint."""

import re
from ..services.wikipedia import get_summary


def extract_word_position(prompt: str) -> int:
    """Parse word position from prompt (e.g., '8th word' -> 8)."""
    match = re.search(r"(\d+)(?:st|nd|rd|th)\s+word", prompt, re.IGNORECASE)
    if not match:
        raise ValueError(f"No word position found in: {prompt}")
    return int(match.group(1))


def extract_topic(prompt: str) -> str:
    """Extract Wikipedia topic from prompt."""
    # Try quoted format first: 'Topic_name' or "Topic_name"
    match = re.search(r"['\"]([\w_]+)['\"]", prompt)
    if match:
        return match.group(1)

    # Try "entry for Topic" format
    match = re.search(r"entry for\s+([A-Z][a-zA-Z\s]+)", prompt)
    if match:
        return match.group(1).strip()

    raise ValueError(f"No topic found in: {prompt}")


def get_nth_word(text: str, n: int) -> str:
    """Extract the Nth word from text (1-indexed)."""
    words = text.split()
    if n < 1 or n > len(words):
        raise IndexError(f"Position {n} out of range for {len(words)} words")
    return words[n - 1]


def handle_knowledge(prompt: str) -> dict:
    """Handle knowledge archive query checkpoint."""
    topic = extract_topic(prompt)
    position = extract_word_position(prompt)
    summary = get_summary(topic)
    word = get_nth_word(summary, position)
    return {"type": "speak_text", "text": word}
