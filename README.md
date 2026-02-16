# NEON AI Co-Pilot

AI agent to solve the Neon Health "Nerdsnipe" hiring challenge - a WebSocket-based authentication sequence.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env and add your credentials:
   # - NEON_CODE (your vessel authorization code)
   # - ANTHROPIC_API_KEY (your Anthropic API key)
   ```

3. **Add your resume:**
   Edit `data/resume.json` with your actual resume information.

## Run

```bash
python -m src.main
```

## Architecture

- **src/main.py** - Main orchestrator and routing logic
- **src/ws_client.py** - WebSocket connection management
- **src/message_parser.py** - Fragment reconstruction
- **src/checkpoints/** - Individual checkpoint handlers
  - handshake.py - Signal handshake & vessel ID
  - arithmetic.py - Math expression evaluation
  - knowledge.py - Wikipedia queries
  - manifest.py - Resume Q&A
  - verification.py - Memory recall
- **src/services/** - External service clients
  - wikipedia.py - Wikipedia API
  - resume.py - Resume loading and LLM Q&A
- **src/utils/** - Helper utilities
  - history.py - Conversation tracking

## Coding Standards

- **Tiny functions** - Each function does ONE thing (5-15 lines max)
- **No in-function imports** - All imports at module top
- **Minimal try-except** - Only wrap operations that can fail
- Type hints and clear naming

See `CLAUDE.md` for full development guidelines.
