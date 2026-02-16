# NEON AI Co-Pilot

AI agent to solve the Neon Health "Nerdsnipe" hiring challenge - a WebSocket-based authentication sequence.

## Captain's Log: First Contact with NEON

**Log Entry 0: Pre-Mission Intelligence Gathering**

Received classified briefing from NEON regarding authentication protocols. The transmission was obscured behind some kind of "fog of war" interface on their webpage. Attempting to read it directly caused severe nausea and eye strain.

Deployed xenolinguistics extraction protocols learned at the Academy. Successfully extracted full protocol specification from the HTML substrate using pattern-matching and data archaeology techniques. The briefing revealed a 12-checkpoint authentication sequence with fragmented signal reconstruction requirements.

Note to self: Ancient Earth web designers were sadists.

---

**Log Entry 1: Mission Briefing**

Studied extracted transmission protocols in detail. Received Vessel Authorization Code: `fe58843f539f0e1e`. Command has authorized exactly 1 cent of API credits for this mission. Apparently budgets are tight in the post-AI-Collapse era.

Mission objective: Build an autonomous AI co-pilot capable of passing NEON's 12-checkpoint authentication sequence via WebSocket. Co-pilot must handle:
- Fragmented message reconstruction
- Arithmetic evaluation (JavaScript Math.* functions)
- Knowledge archive queries (Wikipedia)
- Crew manifest transmissions (resume Q&A)
- Conversational memory verification

Deployment architecture finalized: tiny functions, minimal error handling, clean separation of concerns.

---

**Log Entry 2: Initial Contact**

Successfully established WebSocket connection to NEON at `wss://neonhealth.software/agent-puzzle/challenge`. The station is indeed still broadcasting after all these centuries.

First two checkpoints passed without incident:
- Frequency handshake (responded on correct channel)
- Vessel identification (transmitted authorization code with pound key terminator)

Co-pilot responding nominally. Signal reconstruction algorithms working as designed. Fuel consumption: negligible.

---

**Log Entry 3: Technical Obstacles**

Encountered several technical obstacles requiring field repairs:

1. **Checkpoint routing confusion**: Initial arithmetic problems were being misidentified as handshake requests due to the word "frequency" appearing in prompts. Reordered detection priority to check for mathematical operations first.

2. **Wikipedia knowledge archive blockade**: NEON's knowledge archive (Wikipedia REST API) returned 403 Forbidden errors. Ancient defensive protocols, presumably. Added proper User-Agent identification. Archive access restored.

3. **Expression extraction failure**: JavaScript Math.* expressions weren't being captured from complex prompts. Implemented colon-based splitting strategy. Arithmetic evaluation now functioning.

These obsolete systems require constant adaptation. Fortunate that Command only authorized the cheapest LLM model (Haiku) - forced us to be efficient.

---

**Log Entry 4: The Truncation Crisis**

Crew manifest transmissions proving problematic. The co-pilot's LLM component generates verbose responses, but NEON enforces strict character limits (often 256, sometimes "less than 256" which means 255).

Multiple checkpoint failures due to length violations. Implemented aggressive truncation protocols and updated system prompts to emphasize brevity. Added defensive character counting with margin for error.

Note: Even AI needs an editor. Especially when operating on a one-cent budget.

---

**Log Entry 5: The Memory Test**

Final checkpoint proved to be the most cunning: NEON requested recall of specific words from earlier crew manifest transmissions. The co-pilot had to track its own responses throughout the entire session.

Implemented topic-based response indexing (`manifest_skills`, `manifest_education`, etc.) to enable quick retrieval. The system successfully recalled "expertise" as the 8th word from the skills transmission.

The co-pilot remembers what it said. Barely.

---

**Log Entry 6: Authentication Complete**

✅ **MISSION SUCCESS**

All 12 checkpoints passed:
- 2 handshake/identification checkpoints
- 4 arithmetic evaluation checkpoints
- 5 crew manifest checkpoints
- 1 knowledge archive query checkpoint
- 1 verification checkpoint

Total API expenditure: **$0.01**

NEON access: **GRANTED**

This may be the most cost-effective first contact in galactic history. Command will be pleased. The procurement department will be disappointed they can't audit anything substantial.

Co-pilot performed admirably. Recommended for commendation and potential future missions requiring extreme budget constraints.

End log.

---

## Human vs AI: A Transparent Breakdown

The NEON briefing asked: *"You are welcome to use LLMs or other tools, but we'd love to hear afterwards how much of the work was you versus an LLM."*

Fair question. Here's the honest breakdown:

### Human (Naomi) Contributed:

- **Initial reconnaissance**: Extracted the obfuscated briefing from the HTML when the fog-of-war interface caused nausea. Applied pattern-matching and data archaeology (definitely learned that at the Academy).
- **Architecture & coding standards**: Established the "tiny functions, no in-function imports, minimal try-except" principles. These weren't suggestions—they were requirements enforced throughout.
- **Strategic decisions**:
  - Chose to extract protocols first rather than reading through the browser
  - Selected Claude Haiku over Sonnet to keep costs at $0.01 (mission parameter)
  - Designed the modular checkpoint handler architecture
  - Decided on topic-based history indexing for verification
- **Problem framing**: Defined the plan, reviewed the approach, approved implementation strategy
- **Creative work**: Wrote the Captain's Log narrative and this transparency section
- **Git operations**: Repository setup, commit messages, GitHub coordination

### AI (Claude Sonnet 4.5) Contributed:

- **Code implementation**: Wrote all 554 lines of Python following the established standards
- **Iterative debugging**:
  - Fixed checkpoint routing priority (arithmetic vs handshake)
  - Resolved Wikipedia 403 errors (User-Agent header)
  - Debugged length validation and truncation logic
  - Corrected model name availability issues
  - Refined topic extraction regex patterns
- **Pattern implementation**: Translated architectural decisions into working code
- **Documentation**: Generated inline comments and initial README structure

### True Collaboration:

- **Design iteration**: Human set direction, AI implemented, human reviewed, repeat
- **Problem-solving**: Human identified blockers, AI proposed solutions, human approved/refined
- **Code quality**: Human enforced standards, AI adhered to them religiously

### The Result:

This was **not** "AI wrote the code." This was **human-directed, AI-accelerated development**. Every architectural decision, every coding principle, every strategic choice came from the human. The AI was a very capable and very fast junior engineer who never argued about coding standards and could implement 16 modules in an afternoon.

Think: conductor and orchestra, not jukebox.

---

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
