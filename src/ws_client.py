"""WebSocket client for NEON communication."""

import json
import websockets


async def connect(url: str):
    """Establish WebSocket connection to NEON."""
    return await websockets.connect(url)


async def send_message(ws, message: dict) -> None:
    """Send JSON message to NEON."""
    json_str = json.dumps(message)
    await ws.send(json_str)


async def receive_message(ws) -> dict:
    """Receive and parse JSON message from NEON."""
    raw = await ws.recv()
    return json.loads(raw)


async def close_connection(ws) -> None:
    """Close WebSocket connection cleanly."""
    await ws.close()
