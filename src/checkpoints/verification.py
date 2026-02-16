"""Transmission verification checkpoint."""

import re
from ..utils.history import get_response, extract_word


def extract_word_position_from_verification(prompt: str) -> int:
    """Parse word position from verification prompt."""
    match = re.search(r"(\d+)(?:st|nd|rd|th)\s+word", prompt, re.IGNORECASE)
    if not match:
        raise ValueError(f"No word position found in: {prompt}")
    return int(match.group(1))


def identify_manifest_topic(prompt: str) -> str:
    """Identify which manifest topic is being referenced."""
    prompt_lower = prompt.lower()

    if "skills" in prompt_lower:
        return "skills"
    if "education" in prompt_lower:
        return "education"
    if "experience" in prompt_lower or "work" in prompt_lower:
        return "experience"
    if "project" in prompt_lower:
        return "project"
    if "reason" in prompt_lower or "granted access" in prompt_lower:
        return "reason"

    return "unknown"


def extract_checkpoint_reference(prompt: str) -> str:
    """Parse which checkpoint is being referenced."""
    # For manifest checkpoints, try to be more specific
    if "manifest" in prompt.lower() or "crew" in prompt.lower():
        topic = identify_manifest_topic(prompt)
        if topic != "unknown":
            return f"manifest_{topic}"
        return "manifest"

    return "manifest"


def handle_verification(prompt: str) -> dict:
    """Handle transmission verification checkpoint."""
    checkpoint_ref = extract_checkpoint_reference(prompt)
    word_position = extract_word_position_from_verification(prompt)

    # Retrieve the recorded response
    original_response = get_response(checkpoint_ref)

    # Extract the requested word
    word = extract_word(original_response, word_position)

    return {"type": "speak_text", "text": word}
