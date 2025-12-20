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

## References

- ADR-001: Hub-and-Spoke LLM Architecture
- FIELD Brand Kit: Sacred Geometry Visual System
- DOJO Suite Xcode Development Blueprint (device-specific models)
