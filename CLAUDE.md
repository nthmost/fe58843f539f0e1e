# CLAUDE.md - Neon Health AI Co-Pilot Project

## Project Overview

Building an AI co-pilot to solve the NEON Nerdsnipe challenge - a 12-checkpoint WebSocket authentication sequence that tests:
- Message reconstruction from fragmented signals
- JavaScript arithmetic evaluation
- Wikipedia API querying
- Resume-based Q&A
- Conversational memory

**Challenge Endpoint:** `ws://neonhealth.software/agent-puzzle/challenge`

## Coding Standards

### Function Design
- **TINY functions only** - Each function should do ONE thing
- Functions should be 5-15 lines maximum
- If a function is getting long, break it into smaller pieces
- Prefer many small, well-named functions over fewer large ones

### Import Organization
- **NO in-function imports** - All imports at module top
- Organize imports: stdlib, third-party, local
- No lazy imports inside functions

### Error Handling
- **NO lengthy try-except blocks**
- Keep try-except blocks small and focused
- Wrap minimal code - just the line(s) that can fail
- Create separate error-handling functions if needed
- Prefer early returns and guard clauses over nested try-except

### Code Style
- Clear, descriptive function and variable names
- Type hints on all functions
- Docstrings for non-obvious functions
- Flat is better than nested

## Project Structure

```
neon_health/
├── CLAUDE.md                    # This file
├── neon_complete_briefing.txt   # Challenge specification
├── src/                         # Source code
│   ├── main.py                  # Entry point
│   ├── websocket_client.py      # WebSocket connection
│   ├── message_handler.py       # Message reconstruction
│   ├── checkpoint_handlers.py   # Individual checkpoint solvers
│   └── utils.py                 # Helper functions
└── requirements.txt             # Dependencies
```

## Dependencies

- `websockets` - WebSocket client
- `httpx` - HTTP requests for Wikipedia API
- Python 3.11+

## Development Notes

- The challenge allows unlimited attempts
- Messages arrive as fragmented, timestamped signal bursts
- Must track conversation history for final verification checkpoint
- Strict character length requirements on some responses
