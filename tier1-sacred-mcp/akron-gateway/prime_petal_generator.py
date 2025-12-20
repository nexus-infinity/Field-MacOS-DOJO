#!/usr/bin/env python3
"""
Prime Petal Generator - Recursive Sacred Geometry Structure
Generates P1-P11 fractal organization in folders

Refined Symbols:
- P1:  · (dot, 0D seed)
- P3:  △ (hollow triangle, 2D identity)
- P5:  ⬠ (pentagon, 2D golden ratio vessel)
- P7:  ⬡ (hollow hexagon, temporal pattern)
- P9:  ✦ (star, wisdom synthesis)
- P11: ⊞ (grid, registry manifest)
"""

from pathlib import Path
import json
import yaml
from datetime import datetime
from typing import Optional, Dict, List


class RefinedPrimePetalGenerator:
    """
    Generate recursive Prime Petal structure (P1-P11) with refined symbols

    Makes folders self-contained and fractal-ready with sacred geometry
    """

    # Refined Prime Symbols
    PRIME_SYMBOLS = {
        1: "·",   # P1 Seed (single dot, 0D point)
        3: "△",   # P3 Identity (hollow triangle, 3 vertices)
        5: "⬠",   # P5 Vessel (pentagon, 5 sides, golden ratio)
        7: "⬡",   # P7 Temporal (hollow hexagon, 6 sides = 7 cycle)
        9: "✦",   # P9 Wisdom (4-point star, radial synthesis)
        11: "⊞"   # P11 Registry (squared plus, grid structure)
    }

    # Prime Colors (frequency-aligned)
    PRIME_COLORS = {
        1: "#9CA3AF",   # Gray (neutral seed)
        3: "#FFD700",   # Gold (ATLAS wisdom/structure)
        5: "#00CC66",   # Green (operational/living)
        7: "#FF8C00",   # Orange (TATA temporal)
        9: "#9370DB",   # Purple (OBI-WAN consciousness)
        11: "#0066CC"   # Blue (DOJO synthesis/registry)
    }

    # Dimensional progression
    PRIME_DIMENSIONS = {
        1: "0D (point)",
        3: "2D (3 vertices)",
        5: "2D (5 vertices, φ ratio)",
        7: "2D→3D (tessellating)",
        9: "2D (radial expansion)",
        11: "2D→3D (recursive grid)"
    }

    def generate_prime_structure(
        self,
        folder_path: Path,
        purpose: Optional[str] = None,
        context: Optional[Dict] = None
    ):
        """
        Create complete P1-P11 structure in given folder
        Makes folder self-contained and fractal-ready

        Args:
            folder_path: Path to folder
            purpose: Core purpose description (for P1)
            context: Additional context (case info, matter details, etc.)
        """

        folder_path = Path(folder_path)
        folder_path.mkdir(parents=True, exist_ok=True)

        print(f"\n🌸 Generating Prime Petal structure in: {folder_path.name}")
        print(f"   Location: {folder_path}")

        # Generate each prime level
        self._create_p1_seed(folder_path, purpose, context)
        self._create_p3_identity(folder_path, context)
        self._create_p5_vessel(folder_path, context)
        self._create_p7_temporal(folder_path, context)
        self._create_p9_wisdom(folder_path, context)
        self._create_p11_registry(folder_path, context)

        print(f"\n✅ Prime Petal structure complete!")
        print(f"   Folder is now fractal-ready (P1→P11 recursive)")
        print(f"\n   Files created:")
        print(f"   · P1_seed_purpose.txt")
        print(f"   △ P3_identity_schema.json")
        print(f"   ⬠ P5_operational_rules.yaml")
        print(f"   ⬡ P7_temporal_lifecycle.json")
        print(f"   ✦ P9_wisdom_synthesis.md")
        print(f"   ⊞ P11_registry_manifest.json")

    def _create_p1_seed(
        self,
        folder: Path,
        purpose: Optional[str],
        context: Optional[Dict]
    ):
        """
        P1 = Seed/Core Purpose (· single dot, 0D)
        The origin point, why this folder exists
        """
        file_path = folder / f"{self.PRIME_SYMBOLS[1]} P1_seed_purpose.txt"

        default_purpose = f"Core purpose of {folder.name} folder within FIELD architecture"
        content = purpose or default_purpose

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"· P1 SEED PURPOSE\n")
            f.write(f"═══════════════════\n\n")
            f.write(f"Prime Level: 1\n")
            f.write(f"Symbol: · (single dot)\n")
            f.write(f"Dimension: {self.PRIME_DIMENSIONS[1]}\n")
            f.write(f"Color: {self.PRIME_COLORS[1]} (neutral seed)\n\n")

            f.write(f"Folder: {folder.name}\n")
            f.write(f"Path: {folder}\n")
            f.write(f"Created: {datetime.now().isoformat()}\n\n")

            f.write(f"═══════════════════\n")
            f.write(f"CORE PURPOSE:\n")
            f.write(f"═══════════════════\n\n")
            f.write(f"{content}\n\n")

            if context:
                f.write(f"═══════════════════\n")
                f.write(f"CONTEXT:\n")
                f.write(f"═══════════════════\n\n")
                for key, value in context.items():
                    f.write(f"{key}: {value}\n")
                f.write(f"\n")

            f.write(f"═══════════════════\n")
            f.write(f"RECURSIVE PROPERTIES:\n")
            f.write(f"═══════════════════\n\n")
            f.write(f"Recursion Depth: 0 (seed level)\n")
            f.write(f"Contains Primes: [P1]\n")
            f.write(f"Self-Similar: Yes (every subfolder also has P1)\n")
            f.write(f"Fractal Nature: Origin point for recursive expansion\n")

        print(f"   ✓ Created: · P1_seed_purpose.txt")

    def _create_p3_identity(self, folder: Path, context: Optional[Dict]):
        """
        P3 = Identity/Structure Schema (△ hollow triangle, 2D)
        Defines WHAT this folder is
        """
        file_path = folder / f"{self.PRIME_SYMBOLS[3]} P3_identity_schema.json"

        schema = {
            "prime_level": 3,
            "symbol": "△",
            "dimension": self.PRIME_DIMENSIONS[3],
            "color": self.PRIME_COLORS[3],

            "folder_identity": {
                "name": folder.name,
                "path": str(folder),
                "type": self._infer_folder_type(folder, context),
                "structure": "recursive_prime_petals",
                "created": datetime.now().isoformat()
            },

            "schema_definition": {
                "purpose": "Define identity and structure of this folder",
                "contains": "Metadata about folder's role in FIELD",
                "relationships": self._extract_relationships(folder, context)
            },

            "context": context or {},

            "recursive_properties": {
                "contains_primes": ["P3", "P1"],
                "recursion_depth": 1,
                "self_similar": True,
                "fractal_note": "Every subfolder also has P3 identity"
            }
        }

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)

        print(f"   ✓ Created: △ P3_identity_schema.json")

    def _create_p5_vessel(self, folder: Path, context: Optional[Dict]):
        """
        P5 = Operational Rules/Vessel (⬠ pentagon, 2D golden ratio)
        Defines HOW files are processed in this folder
        """
        file_path = folder / f"{self.PRIME_SYMBOLS[5]} P5_operational_rules.yaml"

        rules = {
            "prime_level": 5,
            "symbol": "⬠",
            "dimension": self.PRIME_DIMENSIONS[5],
            "color": self.PRIME_COLORS[5],
            "golden_ratio_note": "Pentagon embodies φ (phi) = 1.618 relationships",

            "operational_rules": {
                "ingestion": {
                    "stage": "Akron Gateway strip/index/stage",
                    "trust_classification": "Assign trust tier (◉◎◐○◯)",
                    "metadata_extraction": "Extract soul (🜍), spirit (🜔), body (🜕)"
                },

                "validation": {
                    "queens_chamber": "20% height validation checkpoint (✓)",
                    "trust_elevation": "Upgrade from ◯→○→◐ based on cross-ref",
                    "quarantine_rules": "◯ unknown sources isolated for review"
                },

                "routing": {
                    "kings_chamber": "⬥ Translation through 852 Hz (φ⁻¹ = 38.2%)",
                    "frequency_mapping": self._get_frequency_routing(folder, context),
                    "alchemical_transformation": "△ Solve → ⬥ Transform → ▽ Coagula"
                },

                "storage": {
                    "field_node_assignment": "Route to ◻▼●▲◼︎⬥ based on classification",
                    "depth_encoding": "Apply trust tier depth to files",
                    "prime_tagging": "Tag with appropriate P1-P11 level"
                }
            },

            "context_specific_rules": self._get_context_rules(folder, context),

            "recursive_properties": {
                "contains_primes": ["P5", "P3", "P1"],
                "recursion_depth": 2,
                "self_similar": True,
                "fractal_note": "Subfolders inherit and refine these rules"
            }
        }

        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(rules, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        print(f"   ✓ Created: ⬠ P5_operational_rules.yaml")

    def _create_p7_temporal(self, folder: Path, context: Optional[Dict]):
        """
        P7 = Temporal Lifecycle/Pattern (⬡ hollow hexagon, 2D→3D)
        Records WHEN things happen in this folder
        """
        file_path = folder / f"{self.PRIME_SYMBOLS[7]} P7_temporal_lifecycle.json"

        lifecycle = {
            "prime_level": 7,
            "symbol": "⬡",
            "dimension": self.PRIME_DIMENSIONS[7],
            "color": self.PRIME_COLORS[7],
            "temporal_note": "7 = days of week, lifecycle patterns, hexagon tessellates (depth)",

            "creation": {
                "timestamp": datetime.now().isoformat(),
                "event": "Folder created with Prime Petal structure",
                "frequency": "432 Hz (TATA temporal anchor)"
            },

            "lifecycle_events": [
                {
                    "timestamp": datetime.now().isoformat(),
                    "event": "Prime Petal structure generated (P1→P11)",
                    "actor": "RefinedPrimePetalGenerator",
                    "phase": "🜛 Albedo (purification/structuring)"
                }
            ],

            "temporal_anchors": self._extract_temporal_anchors(folder, context),

            "timeline": {
                "past_events": [],
                "current_state": "Active Prime Petal folder",
                "future_projections": []
            },

            "alchemical_stage": {
                "current": "🜛 Albedo (whitening, organization)",
                "progression": "🜚 Nigredo → 🜛 Albedo → 🜜 Citrinitas → 🜝 Rubedo"
            },

            "recursive_properties": {
                "contains_primes": ["P7", "P5", "P3", "P1"],
                "recursion_depth": 3,
                "self_similar": True,
                "fractal_note": "Temporal events nest recursively in subfolders"
            }
        }

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lifecycle, f, indent=2, ensure_ascii=False)

        print(f"   ✓ Created: ⬡ P7_temporal_lifecycle.json")

    def _create_p9_wisdom(self, folder: Path, context: Optional[Dict]):
        """
        P9 = Wisdom Synthesis/Expression (✦ star, radial 2D)
        Synthesized KNOWLEDGE about this folder's contents
        """
        file_path = folder / f"{self.PRIME_SYMBOLS[9]} P9_wisdom_synthesis.md"

        content = f"""# ✦ P9 WISDOM SYNTHESIS

## Prime Level: 9
**Symbol:** ✦ (4-point star, radial expansion)
**Dimension:** {self.PRIME_DIMENSIONS[9]}
**Color:** {self.PRIME_COLORS[9]} (purple, OBI-WAN consciousness)
**Frequency:** 963 Hz (unity, observation, synthesis)

---

## Folder: {folder.name}

**Path:** `{folder}`
**Created:** {datetime.now().isoformat()}

---

## Purpose

This folder contains evidence/data organized according to recursive Prime Petal structure (P1→P11).

Every file and subfolder participates in the sacred geometric FIELD architecture, enabling:

- **Fractal organization** (self-similar at all scales)
- **Trust tier verification** (◉◎◐○◯ depth encoding)
- **Alchemical transformation** (🜚→🜛→🜜→🜝 progression)
- **Frequency alignment** (396-963 Hz chakra resonance)

---

## Synthesized Insights

_(This section grows as wisdom accumulates about folder contents)_

### Current State

- Prime Petal structure complete (P1→P11)
- Folder ready for recursive expansion
- Awaiting data ingestion and classification

### Knowledge Patterns

_(Patterns emerge as files are added and relationships discovered)_

---

## Connections & Relationships

**Contains Primes:** P9, P7, P5, P3, P1
**Recursion Depth:** 4
**Self-Similar:** Yes (every subfolder also has P9 wisdom)

### FIELD Node Relationships

- **◻ Akron:** Sovereignty gateway (data enters here)
- **▼ TATA:** Temporal truth anchor (evidence grounding)
- **● OBI-WAN:** Unified observation (consciousness witness)
- **▲ ATLAS:** Knowledge synthesis (pattern intelligence)
- **◼︎ DOJO:** Manifestation output (final creation)
- **⬥ King's Chamber:** Translation bridge (frequency conversion)

---

## Merkaba Geometry

This folder participates in bidirectional flow:

```
Ascending (Material → Divine):
  ◻ Akron → ▼ TATA → ▲ ATLAS → ● OBI-WAN → ⬥ King's → ◼︎ DOJO

Descending (Divine → Material):
  ◼︎ DOJO → ⬥ King's → ● OBI-WAN → ▲ ATLAS → ▼ TATA → ◻ Akron
```

---

## Fractal Properties

Every subfolder contains the same P1→P11 structure, creating infinite recursive depth:

```
{folder.name}/
├── · P1_seed_purpose.txt
├── △ P3_identity_schema.json
├── ⬠ P5_operational_rules.yaml
├── ⬡ P7_temporal_lifecycle.json
├── ✦ P9_wisdom_synthesis.md (you are here)
├── ⊞ P11_registry_manifest.json
│
└── subfolder/
    ├── · P1_seed_purpose.txt
    ├── △ P3_identity_schema.json
    ├── ⬠ P5_operational_rules.yaml
    ├── ⬡ P7_temporal_lifecycle.json
    ├── ✦ P9_wisdom_synthesis.md
    └── ⊞ P11_registry_manifest.json
```

---

## Evolution & Growth

As this folder accumulates data:

1. **P7 Temporal** tracks lifecycle events
2. **P5 Operational** refines processing rules
3. **P3 Identity** clarifies folder structure
4. **P9 Wisdom** (this file) synthesizes patterns
5. **P11 Registry** maintains complete manifest

The wisdom radiates outward (✦ star symbol) as understanding deepens.

---

## Sacred Geometry Notes

- **·** P1 = Point (0D seed)
- **△** P3 = Triangle (2D identity, 3 vertices)
- **⬠** P5 = Pentagon (2D vessel, golden ratio φ)
- **⬡** P7 = Hexagon (2D→3D temporal, tessellates)
- **✦** P9 = Star (2D radial, wisdom expands)
- **⊞** P11 = Grid (2D→3D registry, recursive index)

---

**This folder is a living fractal within the FIELD.**
"""

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"   ✓ Created: ✦ P9_wisdom_synthesis.md")

    def _create_p11_registry(self, folder: Path, context: Optional[Dict]):
        """
        P11 = Complete Registry/Archive Manifest (⊞ grid, 2D→3D)
        Complete index of this folder (self-referential)
        """
        file_path = folder / f"{self.PRIME_SYMBOLS[11]} P11_registry_manifest.json"

        # Scan folder for existing files and subfolders
        files = sorted([f.name for f in folder.iterdir() if f.is_file() and not f.name.startswith('.')])
        subfolders = sorted([f.name for f in folder.iterdir() if f.is_dir() and not f.name.startswith('.')])

        registry = {
            "prime_level": 11,
            "symbol": "⊞",
            "dimension": self.PRIME_DIMENSIONS[11],
            "color": self.PRIME_COLORS[11],
            "grid_note": "Registry as grid structure, recursive manifest of all contents",

            "folder_metadata": {
                "name": folder.name,
                "path": str(folder),
                "created": datetime.now().isoformat(),
                "prime_petal_version": "2.0_refined_symbols"
            },

            "prime_petal_structure": {
                "P11": {
                    "file": f"{self.PRIME_SYMBOLS[11]} P11_registry_manifest.json",
                    "symbol": "⊞",
                    "purpose": "Complete registry/manifest of this folder",
                    "recursive": True,
                    "self_referential": True,
                    "contains": ["P11", "P9", "P7", "P5", "P3", "P1"]
                },
                "P9": {
                    "file": f"{self.PRIME_SYMBOLS[9]} P9_wisdom_synthesis.md",
                    "symbol": "✦",
                    "purpose": "Synthesized knowledge about folder contents",
                    "contains": ["P9", "P7", "P5", "P3", "P1"]
                },
                "P7": {
                    "file": f"{self.PRIME_SYMBOLS[7]} P7_temporal_lifecycle.json",
                    "symbol": "⬡",
                    "purpose": "Timeline and lifecycle tracking",
                    "contains": ["P7", "P5", "P3", "P1"]
                },
                "P5": {
                    "file": f"{self.PRIME_SYMBOLS[5]} P5_operational_rules.yaml",
                    "symbol": "⬠",
                    "purpose": "Processing rules for folder contents",
                    "contains": ["P5", "P3", "P1"]
                },
                "P3": {
                    "file": f"{self.PRIME_SYMBOLS[3]} P3_identity_schema.json",
                    "symbol": "△",
                    "purpose": "Structure definition and identity",
                    "contains": ["P3", "P1"]
                },
                "P1": {
                    "file": f"{self.PRIME_SYMBOLS[1]} P1_seed_purpose.txt",
                    "symbol": "·",
                    "purpose": "Core purpose (seed/origin point)",
                    "contains": ["P1"]
                }
            },

            "files_in_folder": files,
            "total_files": len(files),

            "subfolders": [
                {
                    "name": subfolder,
                    "prime_level": 11,
                    "recursive": True,
                    "note": "Subfolder also contains P1→P11 structure"
                }
                for subfolder in subfolders
            ],
            "total_subfolders": len(subfolders),

            "fractal_properties": {
                "depth": "Infinite (each subfolder is also P11)",
                "self_similar": True,
                "recursion_depth": 5,
                "grid_structure": "⊞ represents recursive registry grid"
            },

            "field_integration": {
                "merkaba_aware": True,
                "trust_tier_encoding": True,
                "alchemical_transformation": True,
                "frequency_aligned": True
            },

            "context": context or {}
        }

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)

        print(f"   ✓ Created: ⊞ P11_registry_manifest.json")

    # Helper methods

    def _infer_folder_type(self, folder: Path, context: Optional[Dict]) -> str:
        """Infer folder type from name and context"""
        name_lower = folder.name.lower()

        if context and 'type' in context:
            return context['type']
        elif 'evidence' in name_lower or 'case' in name_lower:
            return "evidence_archive"
        elif 'contract' in name_lower:
            return "legal_contracts"
        elif 'communication' in name_lower or 'email' in name_lower:
            return "communications"
        elif 'knowledge' in name_lower or 'research' in name_lower:
            return "knowledge_base"
        elif 'output' in name_lower or 'generated' in name_lower:
            return "manifestation_outputs"
        else:
            return "general_archive"

    def _extract_relationships(self, folder: Path, context: Optional[Dict]) -> Dict:
        """Extract relationship metadata"""
        relationships = {
            "parent_folder": str(folder.parent) if folder.parent != folder else None,
            "field_node": self._infer_field_node(folder, context),
            "trust_tier": "To be assigned upon data ingestion"
        }

        if context:
            if 'case_id' in context:
                relationships['case_id'] = context['case_id']
            if 'matter' in context:
                relationships['matter'] = context['matter']

        return relationships

    def _infer_field_node(self, folder: Path, context: Optional[Dict]) -> str:
        """Infer primary FIELD node for folder"""
        name_lower = folder.name.lower()

        if 'evidence' in name_lower or 'contract' in name_lower:
            return "▼ TATA (evidence/truth)"
        elif 'communication' in name_lower or 'email' in name_lower:
            return "● OBI-WAN (observation/communication)"
        elif 'knowledge' in name_lower or 'research' in name_lower:
            return "▲ ATLAS (knowledge/patterns)"
        elif 'output' in name_lower or 'generated' in name_lower:
            return "◼︎ DOJO (manifestation/output)"
        elif 'archive' in name_lower or 'akron' in name_lower:
            return "◻ Akron (sovereignty/archive)"
        else:
            return "◻ Akron (default gateway)"

    def _get_frequency_routing(self, folder: Path, context: Optional[Dict]) -> Dict:
        """Get frequency routing rules"""
        return {
            "396_Hz": "◻ Akron (sovereignty, gateway)",
            "432_Hz": "▼ TATA (temporal, evidence)",
            "528_Hz": "▲ ATLAS (knowledge, patterns)",
            "741_Hz": "◼︎ DOJO (manifestation, output)",
            "852_Hz": "⬥ King's Chamber (translation)",
            "963_Hz": "● OBI-WAN (observation, unity)"
        }

    def _get_context_rules(self, folder: Path, context: Optional[Dict]) -> Dict:
        """Get context-specific processing rules"""
        if not context:
            return {"note": "No context-specific rules defined"}

        rules = {}

        if 'case_id' in context:
            rules['case_processing'] = f"All files tagged with case_id: {context['case_id']}"

        if 'matter' in context:
            rules['matter_type'] = f"Legal matter: {context['matter']}"

        return rules

    def _extract_temporal_anchors(self, folder: Path, context: Optional[Dict]) -> List[Dict]:
        """Extract temporal anchors from context"""
        anchors = []

        if context:
            if 'created_date' in context:
                anchors.append({
                    "date": context['created_date'],
                    "event": "Folder creation date",
                    "symbol": "◯"
                })

            if 'case_start_date' in context:
                anchors.append({
                    "date": context['case_start_date'],
                    "event": "Case/matter start date",
                    "symbol": "◯"
                })

        return anchors


def main():
    """
    Example usage of RefinedPrimePetalGenerator
    """
    generator = RefinedPrimePetalGenerator()

    # Example 1: Simple folder
    print("\n" + "="*60)
    print("Example 1: Simple folder with basic context")
    print("="*60)

    test_path = Path.home() / "FIELD-macOS-DOJO" / "test_prime_petal"
    generator.generate_prime_structure(
        folder_path=test_path,
        purpose="Test folder for Prime Petal structure validation",
        context={
            "type": "test_archive",
            "created_by": "RefinedPrimePetalGenerator"
        }
    )

    # Example 2: Legal evidence folder
    print("\n" + "="*60)
    print("Example 2: Legal evidence folder with case context")
    print("="*60)

    # Check if Akron volume exists
    akron_path = Path("/Volumes/Akron")
    if akron_path.exists():
        evidence_path = akron_path / "evidence" / "case123_test"
        generator.generate_prime_structure(
            folder_path=evidence_path,
            purpose="Evidence archive for test case validation",
            context={
                "type": "evidence_archive",
                "case_id": "case123_test",
                "matter": "Prime Petal Structure Validation",
                "jurisdiction": "Test Environment",
                "case_start_date": "2025-12-20",
                "created_date": datetime.now().isoformat()
            }
        )
    else:
        print("\n   ⚠️  /Volumes/Akron not mounted, skipping Akron example")


if __name__ == "__main__":
    main()
