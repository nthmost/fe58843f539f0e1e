"""Main orchestrator for NEON challenge."""

import asyncio
import os
from dotenv import load_dotenv

from . import ws_client
from . import message_parser
from .checkpoints import handshake, arithmetic, knowledge, manifest, verification
from .utils.history import clear_history


def detect_checkpoint_type(prompt: str) -> str:
    """Determine checkpoint type from prompt."""
    prompt_lower = prompt.lower()

    # Check arithmetic first (higher priority than handshake)
    if "calculate" in prompt_lower or "math." in prompt_lower or "evaluate" in prompt_lower:
        return "arithmetic"
    if "knowledge archive" in prompt_lower:
        return "knowledge"
    if "recall" in prompt_lower or "earlier" in prompt_lower:
        return "verification"
    if "frequency" in prompt_lower or "authorization code" in prompt_lower:
        return "handshake"

    return "manifest"


def route_checkpoint(prompt: str, checkpoint_type: str, context: dict) -> dict:
    """Route to appropriate checkpoint handler."""
    if checkpoint_type == "handshake":
        return handshake.handle_handshake(prompt, context["neon_code"])

    if checkpoint_type == "arithmetic":
        return arithmetic.handle_arithmetic(prompt)

    if checkpoint_type == "knowledge":
        return knowledge.handle_knowledge(prompt)

    if checkpoint_type == "verification":
        return verification.handle_verification(prompt)

    if checkpoint_type == "manifest":
        checkpoint_id = f"manifest_{context.get('manifest_count', 0)}"
        context["manifest_count"] = context.get("manifest_count", 0) + 1
        return manifest.handle_manifest(prompt, context["api_key"], checkpoint_id)

    raise ValueError(f"Unknown checkpoint type: {checkpoint_type}")


async def process_message(msg: dict, context: dict) -> dict | None:
    """Process a message from NEON and return response."""
    msg_type = msg.get("type")

    if msg_type == "challenge":
        prompt = message_parser.parse_challenge(msg)
        print(f"\n📡 NEON: {prompt}")

        checkpoint_type = detect_checkpoint_type(prompt)
        print(f"🔍 Detected checkpoint: {checkpoint_type}")

        response = route_checkpoint(prompt, checkpoint_type, context)
        print(f"📤 Response: {response}")
        return response

    if msg_type == "success":
        print("\n✅ SUCCESS! Authentication complete!")
        return None

    if msg_type == "error":
        error_msg = msg.get("message", "Unknown error")
        print(f"\n❌ ERROR: {error_msg}")
        raise RuntimeError(f"Challenge failed: {error_msg}")

    print(f"\n⚠️  Unknown message type: {msg_type}")
    return None


async def run_challenge(neon_code: str, api_key: str) -> None:
    """Run the NEON authentication challenge."""
    clear_history()
    url = "wss://neonhealth.software/agent-puzzle/challenge"

    context = {
        "neon_code": neon_code,
        "api_key": api_key,
        "manifest_count": 0,
    }

    print(f"🚀 Connecting to NEON at {url}...")

    ws = await ws_client.connect(url)

    try:
        while True:
            msg = await ws_client.receive_message(ws)
            response = await process_message(msg, context)

            if response is None:
                break

            await ws_client.send_message(ws, response)

    finally:
        await ws_client.close_connection(ws)
        print("\n🔌 Connection closed")


def main():
    """Entry point."""
    load_dotenv()

    neon_code = os.getenv("NEON_CODE")
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not neon_code:
        raise ValueError("NEON_CODE not set in .env")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in .env")

    asyncio.run(run_challenge(neon_code, api_key))


if __name__ == "__main__":
    main()
