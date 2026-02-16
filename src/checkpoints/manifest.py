"""Crew manifest transmission checkpoint."""

import re
from ..services.resume import load_resume, query_resume
from ..utils.history import record_response


def extract_length_requirement(prompt: str) -> tuple[int | None, int | None]:
    """Parse character length requirements from prompt."""
    # Look for "between X and Y characters"
    match = re.search(r"between (\d+) and (\d+) characters", prompt, re.IGNORECASE)
    if match:
        return int(match.group(1)), int(match.group(2))

    # Look for "exactly X characters"
    match = re.search(r"exactly (\d+) characters", prompt, re.IGNORECASE)
    if match:
        length = int(match.group(1))
        return length, length

    return None, None


def validate_length(text: str, min_len: int | None, max_len: int | None) -> bool:
    """Check if text meets length requirements."""
    if min_len is None and max_len is None:
        return True

    text_len = len(text)

    if min_len is not None and text_len < min_len:
        return False
    if max_len is not None and text_len > max_len:
        return False

    return True


def truncate_to_length(text: str, max_len: int) -> str:
    """Truncate text to fit within max length."""
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip()


def identify_topic(prompt: str) -> str:
    """Identify the topic of the manifest question."""
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

    return "general"


def handle_manifest(prompt: str, api_key: str, checkpoint_id: str = "manifest") -> dict:
    """Handle crew manifest transmission checkpoint."""
    resume = load_resume()
    min_len, max_len = extract_length_requirement(prompt)

    # "less than X" means X-1 max
    if "less than" in prompt.lower():
        if max_len:
            max_len = max_len - 1
        else:
            # Default to 255 if "less than" but no number found
            max_len = 255

    # Set LLM max conservatively
    llm_max = (max_len - 10) if max_len else 240
    llm_min = min_len if min_len else 64
    answer = query_resume(prompt, resume, api_key, llm_max, llm_min)

    # Truncate to max_len if needed
    final_max = max_len if max_len else 250
    if len(answer) > final_max:
        answer = truncate_to_length(answer, final_max)

    if not validate_length(answer, min_len, max_len):
        raise ValueError(f"Answer length {len(answer)} not in range [{min_len}, {max_len}]")

    # Record for verification checkpoint with both numeric and topic-based IDs
    record_response(checkpoint_id, answer)

    # Also record with topic-based ID for easier lookup
    topic = identify_topic(prompt)
    record_response(f"manifest_{topic}", answer)

    return {"type": "speak_text", "text": answer}
