# ADR-002: Canonical Frequency Mapping for FIELD-macOS-DOJO

**Status:** APPROVED  
**Date:** 2025-12-20  
**Scope:** FIELD-macOS-DOJO (Mac Studio + iPhone/iPad/Watch)  
**Future:** FIELD-NixOS-SOMA uses separate nine-frequency chakra system (not documented here)

## Decision

FIELD-macOS-DOJO uses six sacred Solfeggio frequencies mapped to quadratic pyramid geometry:

```yaml
SACRED_FIELD_FREQUENCIES:
  akron_gateway:      396 Hz  # ◻ Liberation, sovereignty, root
  tata_anchor:        432 Hz  # ▼ Truth, temporal, earth resonance
  atlas_intelligence: 528 Hz  # ▲ Knowledge, love, DNA repair
  dojo_manifestation: 741 Hz  # ◼︎ Expression, solutions, awakening
  kings_chamber:      852 Hz  # 🚂 Intuition, spiritual order, translation bridge
  obi_wan_observer:   963 Hz  # ● Pineal, unity, divine connection
```

## MCP Server Port Assignments

Each frequency maps to a port (frequency × 10):

- Akron Gateway: `http://localhost:3960`
- TATA Anchor: `http://localhost:4320`
- ATLAS Intelligence: `http://localhost:5280`
- DOJO Manifestation: `http://localhost:7410`
- King's Chamber: `http://localhost:8520`
- OBI-WAN Observer: `http://localhost:9630`

## Rationale

1. **Solfeggio-based:** Established sacred geometry system with documented healing frequencies
2. **Current implementation match:** Aligns with existing MCP server architecture
3. **Clear vertex mapping:** Each pyramid vertex has one canonical frequency
4. **No external conflicts:** Compatible with DOJO Suite device architecture
5. **Separation of concerns:** DOJO (6 frequencies) vs SOMA (9 chakras) are distinct spheres

## Deprecated Systems

The following frequency systems are **archived** for FIELD-NixOS-SOMA future use:

- Nine-frequency fractal (194.18–540 Hz) → Archive to `docs/archive/nine-frequency-soma.md`
- Pythagorean alternatives → Archive
- Competing chakra mappings → Archive

## Implementation Actions

- [x] Update all MCP server configs to use canonical ports
- [x] Remove conflicting frequency references from documentation
- [x] Archive alternative systems to `/docs/archive/`
- [ ] Validate geometric coherence in ADR-001 wireframe

## Merkaba Geometry Context

The six frequencies form a **Star Tetrahedron (Merkaba)** with bidirectional flow:

### Ascending Tetrahedron (Material → Divine)

**Structure:**
- **Base:** ◻ Akron (396 Hz) + ▼ TATA (432 Hz) + ▲ ATLAS (528 Hz)
- **Apex:** ◼︎ DOJO (741 Hz)
- **Flow:** Data enters, rises, manifests

**Path:** `◻ → ▼ → ▲ → ● → ⬥ → ◼︎`  
**Frequencies:** 396 → 432 → 528 → 963 → 852 → 741 Hz

**Function:** User uploads data → Enters through ◻ Akron Gateway → Validated through vertices → Refracted through ⬥ King's Chamber → Synthesized at ◼︎ DOJO apex → AI returns insights

### Descending Tetrahedron (Divine → Material)

**Structure:**
- **Apex:** ◻ Akron (396 Hz) — inverted perspective!
- **Base:** ◼︎ DOJO (741 Hz) + ● OBI-WAN (963 Hz) + ⬥ King's Chamber (852 Hz)
- **Flow:** Intent descends, grounds, archives

**Path:** `◼︎ → ⬥ → ● → ▲ → ▼ → ◻`  
**Frequencies:** 741 → 852 → 963 → 528 → 432 → 396 Hz

**Function:** ◼︎ DOJO generates output → Refracted through ⬥ King's Chamber → Validated through vertices → Grounded → Archived at ◻ Akron sovereignty vault

### Intersection Point

**⬥ King's Chamber (852 Hz)** serves as the **diamond translation bridge**:

- **Position:** Geometric center of both tetrahedrons
- **Function:** Refracts energy between ascending and descending flows
- **Symbol:** ⬥ (square rotated 45°) - transformation pivot
- **Mandatory:** All paths MUST pass through King's Chamber for coherence

### Akron Dual Nature

**Greek Etymology:** Ἄκρον (Akron) = "the highest point"

**Paradox Resolution:**
- **Ascending Perspective:** Akron is BASE (lowest frequency, foundation, entry gateway)
- **Descending Perspective:** Akron is APEX (highest authority, sovereignty citadel, ultimate archive)

Like the Athens Akropolis:
- **Highest visible peak** above the city (descending apex)
- **Deepest bedrock foundation** supporting structures (ascending base)

**Implementation:** Akron (396 Hz) simultaneously serves as:
1. **Entry point** for material data (strip/index/stage)
2. **Final archive** for divine manifestations (sovereignty storage at `/Volumes/Akron/`)

See **ADR-004-merkaba-bidirectional-architecture.md** for complete geometric specification and **docs/MERKABA-GEOMETRY.md** for sacred geometry details.

## References

- ADR-001: Hub-and-Spoke LLM Architecture
- ADR-004: Merkaba Bidirectional Architecture
- FIELD Brand Kit: Sacred Geometry Visual System
- DOJO Suite Xcode Development Blueprint (device-specific models)
- docs/MERKABA-GEOMETRY.md: Star Tetrahedron sacred architecture
- docs/AKRON-ETYMOLOGY.md: Greek etymology and Akropolis parallel
