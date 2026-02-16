"""Signal handshake and vessel identification checkpoint."""

import re


def extract_frequency(prompt: str) -> str:
    """Extract frequency number from prompt."""
    match = re.search(r"frequency\s+(\d+)", prompt, re.IGNORECASE)
    if not match:
        raise ValueError(f"No frequency found in: {prompt}")
    return match.group(1)


def needs_pound_key(prompt: str) -> bool:
    """Check if prompt requires pound key suffix."""
    return "pound key" in prompt.lower() or "followed by #" in prompt.lower()


def format_digits(value: str, with_pound: bool) -> str:
    """Format digits with optional pound key suffix."""
    if with_pound:
        return f"{value}#"
    return value


def is_code_request(prompt: str) -> bool:
    """Check if prompt asks for authorization code."""
    keywords = ["authorization code", "vessel code", "neon code"]
    return any(kw in prompt.lower() for kw in keywords)


def handle_handshake(prompt: str, neon_code: str) -> dict:
    """Handle signal handshake checkpoint."""
    if is_code_request(prompt):
        digits = neon_code
    else:
        digits = extract_frequency(prompt)

    formatted = format_digits(digits, needs_pound_key(prompt))
    return {"type": "enter_digits", "digits": formatted}
