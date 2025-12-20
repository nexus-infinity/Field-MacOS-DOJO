# ADR-003: Repository Consolidation Strategy

**Status:** APPROVED  
**Date:** 2025-12-20  
**Problem:** ~45 repositories in nexus-infinity, scattered code, conceptual framework duplication

## Decision

Consolidate into **four primary spheres** with fractal perspective lenses:

### Primary Spheres (Keep & Strengthen)

| Repository | Purpose | Sacred Position | Maturity | Action |
|------------|---------|-----------------|----------|--------|
| **nexus-infinity/Field-MacOS-DOJO** | Mac Studio DOJO Suite | ◼︎ 741 Hz | Active | PRIMARY - All DOJO work here |
| **nexus-infinity/field-nixos-soma** | iMac NixOS SOMA | 852 Hz (synthetic) | Planned | Create when ready |
| **nexus-infinity/berjak-website** | Public portal, Vercel | Entry/Gateway | Production | Keep, proven |
| **nexus-infinity/field-docs** | ADRs, architecture | Documentation | Active | Consolidate ADRs |

### Archive to nexus-infinity-archive/

| Repository | Reason | Action |
|------------|--------|--------|
| Agricultural blockchain repos | Business pivot, no active revenue | Archive entire set |
| nexus-infinity/BEAR | Conceptual framework → ADR | Extract principles, archive code |
| nexus-infinity/SAIGES | Overlaps with FIELD docs | Merge into field-docs |
| nexus-infinity/Trident-Framework | Overlaps with FIELD docs | Merge into field-docs |
| jeremy-rich/* | Inactive 1+ year, fragmented | Archive or delete |

### Consolidate Into Field-MacOS-DOJO

| Repositories to Merge | Destination | Action |
|-----------------------|-------------|--------|
| ATLAS, OBI-WAN-SYS-UI, system-monitor | Field-MacOS-DOJO/modules/ | Move as modules |
| FIELD-DEV scattered code | Field-MacOS-DOJO/ | Consolidate |
| Conceptual frameworks (BEAR, SAIGES) | field-docs/ADRs/ | Extract to ADRs |

## Fractal Perspective Lenses

Each primary sphere can be viewed through multiple lenses without duplication:

- **Privacy:** `private`, `community`, `business`
- **Sacred Position:** Which frequencies this sphere embodies
- **Function:** `portal`, `processing`, `archive`, `infrastructure`
- **Maturity:** `experimental`, `active`, `stable`, `production`

Example: `Field-MacOS-DOJO` is:
- Privacy: `private` (sovereign development)
- Sacred Position: 741 Hz DOJO manifestation apex
- Function: `portal` (device consciousness)
- Maturity: `active` (current development focus)

## Rationale

1. **Spheres, not monolith:** Each repo is a coherent cognitive sphere
2. **Fractal views:** Tag-based perspectives, not repository duplication
3. **Clear boundaries:** Arkadaş validates crossings between spheres
4. **Reduce sprawl:** ~45 repos → 4 primary spheres + archived history

## Implementation

- [ ] Create `nexus-infinity-archive` organization
- [ ] Move agricultural repos to archive
- [ ] Consolidate ATLAS/OBI-WAN/system-monitor into Field-MacOS-DOJO/modules/
- [ ] Extract BEAR/SAIGES principles to field-docs/ADRs/
- [ ] Archive jeremy-rich/* repos
- [ ] Apply fractal tags to primary spheres
