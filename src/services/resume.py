"""Resume service for crew manifest queries."""

import json
import os
from pathlib import Path
from anthropic import Anthropic


def get_resume_path() -> Path:
    """Get path to resume.json file."""
    return Path(__file__).parent.parent.parent / "data" / "resume.json"


def load_resume() -> dict:
    """Load resume data from JSON file."""
    path = get_resume_path()
    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {path}")

    with open(path) as f:
        return json.load(f)


def format_for_llm(resume: dict) -> str:
    """Format resume data as text for LLM context."""
    sections = []

    if "name" in resume:
        sections.append(f"Name: {resume['name']}")

    if "education" in resume:
        sections.append("Education:")
        for edu in resume["education"]:
            sections.append(f"  - {edu}")

    if "experience" in resume:
        sections.append("Experience:")
        for exp in resume["experience"]:
            sections.append(f"  - {exp}")

    if "skills" in resume:
        sections.append(f"Skills: {', '.join(resume['skills'])}")

    if "projects" in resume:
        sections.append("Notable Projects:")
        for proj in resume["projects"]:
            sections.append(f"  - {proj}")

    return "\n".join(sections)


def query_resume(prompt: str, resume: dict, api_key: str, max_chars: int = 250, min_chars: int = 64) -> str:
    """Use Claude to answer resume questions."""
    client = Anthropic(api_key=api_key)
    resume_text = format_for_llm(resume)

    system_prompt = f"""You are answering questions about a crew member's resume.
Provide concise, accurate answers based ONLY on the resume data.
CRITICAL: Keep your response between {min_chars} and {max_chars} characters.
Aim for around {max_chars - 30} characters to be safe.

Resume:
{resume_text}"""

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=200,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text
