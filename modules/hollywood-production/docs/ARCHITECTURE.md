# Hollywood Production Architecture

## Geometric Positioning

Hollywood Production sits at the **DOJO apex (741 Hz)** of the quadratic pyramid, receiving input from:

- **TATA Anchor (432 Hz):** Evidence-based narrative validation
- **OBI-WAN Observer (963 Hz):** Character consciousness

All data passes through **King's Chamber (852 Hz)** for frequency translation.

## Data Flow

```
User Input → DOJO MCP (7410)
      ↓
Scene Generation
      ↓
TATA Validation (4320) ← Evidence Check
      ↓
OBI-WAN Dialogue (9630) ← Character Voice
      ↓
King's Chamber (8520) ← Frequency Translation
      ↓
Video Export
```

## MCP Client Architecture

Each service connects to its corresponding MCP server:

```typescript
// src/services/dojo-client.ts
export class DOJOMCPClient {
  private baseURL = 'http://localhost:7410';
  
  async generateScene(prompt: string): Promise<Scene> {
    // Scene generation via DOJO MCP
  }
}

// src/services/tata-client.ts
export class TATAMCPClient {
  private baseURL = 'http://localhost:4320';
  
  async validateNarrative(scene: Scene): Promise<ValidationResult> {
    // Evidence-based validation
  }
}

// src/services/obi-wan-client.ts
export class OBIWANMCPClient {
  private baseURL = 'http://localhost:9630';
  
  async generateDialogue(character: string, context: string): Promise<Dialogue> {
    // Character consciousness dialogue
  }
}
```

## Sacred Geometry Compliance

Hollywood Production follows FIELD geometric principles:

1. **Sovereignty:** All data stays local, no cloud rendering
2. **Geometric Coherence:** Frequency validation at every crossing
3. **Triadic Handshake:** Capture → Validate → Route (no two-way fragility)
4. **Akron Archive:** All production outputs archived with chain of custody

## Technology Stack

- **Frontend:** Next.js 14 + React + TypeScript
- **Backend:** Node.js MCP clients
- **Video:** FFmpeg for rendering
- **State:** Vercel KV for session management
- **Deployment:** Vercel Edge Functions
