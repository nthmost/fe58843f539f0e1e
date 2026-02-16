"""Wikipedia API client for knowledge archive queries."""

import httpx


def build_url(topic: str) -> str:
    """Construct Wikipedia REST API URL for topic."""
    encoded_topic = topic.replace(" ", "_")
    return f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_topic}"


def fetch_json(url: str) -> dict:
    """Fetch JSON from URL."""
    headers = {
        "User-Agent": "NEON-AI-Copilot/1.0 (naomi@example.com)"
    }
    try:
        response = httpx.get(url, headers=headers, timeout=10.0)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError as e:
        raise ValueError(f"HTTP request failed: {e}")


def extract_summary_text(data: dict) -> str:
    """Extract summary text from Wikipedia API response."""
    if "extract" not in data:
        raise ValueError(f"No 'extract' field in response: {data}")
    return data["extract"]


def get_summary(topic: str) -> str:
    """Fetch Wikipedia summary for topic."""
    url = build_url(topic)
    data = fetch_json(url)
    return extract_summary_text(data)
