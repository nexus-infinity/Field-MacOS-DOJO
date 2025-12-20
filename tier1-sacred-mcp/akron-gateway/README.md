# Akron Gateway - Prime Petal Generator

**Sacred Geometry Folder Organization System**

Akron Gateway provides tools to generate recursive Prime Petal structures (P1-P11) that make folders self-organizing and fractal-ready within the FIELD architecture.

---

## 🌸 What is Prime Petal Structure?

Prime Petal is a recursive organizational system based on sacred geometry and prime numbers. Each folder contains 6 files representing geometric progression from 0D (point) to 3D (grid):

| Prime | Symbol | Name | Dimension | Purpose |
|-------|--------|------|-----------|---------|
| **P1** | · | Seed | 0D (point) | Core purpose/why folder exists |
| **P3** | △ | Identity | 2D (triangle) | What folder is/structure schema |
| **P5** | ⬠ | Vessel | 2D (pentagon, φ) | How files are processed/rules |
| **P7** | ⬡ | Temporal | 2D→3D (hexagon) | When events happen/lifecycle |
| **P9** | ✦ | Wisdom | 2D (star) | Synthesized knowledge/patterns |
| **P11** | ⊞ | Registry | 2D→3D (grid) | Complete manifest/index |

---

## 🎯 Why Use Prime Petals?

### Fractal Organization
Every subfolder contains the same P1-P11 structure, creating infinite recursive depth while maintaining coherence at all scales.

### Trust Tier Integration
Compatible with FIELD trust tiers (◉◎◐○◯) for evidence depth encoding.

### Merkaba Flow Awareness
Folders participate in bidirectional sacred geometry flows:
- **Ascending:** Material → Divine (◻ Akron → ◼︎ DOJO)
- **Descending:** Divine → Material (◼︎ DOJO → ◻ Akron)

### Alchemical Transformation
Supports 4-stage transformation: 🜚 Nigredo → 🜛 Albedo → 🜜 Citrinitas → 🜝 Rubedo

---

## 🚀 Quick Start

### 1. Generate Prime Petals in a Single Folder

```bash
cd ~/FIELD-macOS-DOJO
python3 tier1-sacred-mcp/akron-gateway/prime_petal_generator.py
```

Or programmatically:

```python
from pathlib import Path
from prime_petal_generator import RefinedPrimePetalGenerator

generator = RefinedPrimePetalGenerator()

generator.generate_prime_structure(
    folder_path=Path("/Volumes/Akron/evidence/case456"),
    purpose="Evidence archive for Case #456",
    context={
        "case_id": "case456",
        "matter": "Legal Matter Name",
        "jurisdiction": "NSW Supreme Court"
    }
)
```

### 2. Batch Generate Across Folder Tree

```bash
# Generate in all subfolders (skip existing)
python3 tier1-sacred-mcp/akron-gateway/batch_generate_prime_petals.py \
    /Volumes/Akron/evidence \
    --max-depth 5 \
    --auto-context

# Force regenerate (overwrite existing)
python3 tier1-sacred-mcp/akron-gateway/batch_generate_prime_petals.py \
    /Volumes/Akron/evidence \
    --no-skip
```

### 3. Verify Prime Petal Structure

```bash
# Single folder
python3 tier1-sacred-mcp/akron-gateway/verify_prime_petals.py \
    /Volumes/Akron/evidence/case123

# Recursive verification
python3 tier1-sacred-mcp/akron-gateway/verify_prime_petals.py \
    /Volumes/Akron/evidence \
    --recursive \
    --max-depth 5
```

---

## 📂 Generated File Structure

```
folder_name/
├── · P1_seed_purpose.txt           # Core purpose (0D seed)
├── △ P3_identity_schema.json       # Structure/identity (2D triangle)
├── ⬠ P5_operational_rules.yaml     # Processing rules (2D pentagon, φ)
├── ⬡ P7_temporal_lifecycle.json    # Timeline/events (2D→3D hexagon)
├── ✦ P9_wisdom_synthesis.md        # Synthesized knowledge (2D star)
└── ⊞ P11_registry_manifest.json    # Complete manifest (2D→3D grid)
```

---

## 🔧 File Descriptions

### · P1 Seed Purpose (TXT)
- **Encoding:** Plain text
- **Purpose:** Declares why this folder exists
- **Contains:** Core purpose statement, context, recursive properties
- **Dimension:** 0D (single origin point)

### △ P3 Identity Schema (JSON)
- **Encoding:** JSON
- **Purpose:** Defines what this folder is
- **Contains:** Folder type, relationships, schema definition
- **Dimension:** 2D (3 vertices = triangle)

### ⬠ P5 Operational Rules (YAML)
- **Encoding:** YAML
- **Purpose:** Defines how files are processed
- **Contains:** Ingestion, validation, routing, storage rules
- **Dimension:** 2D (5 vertices = pentagon, golden ratio φ = 1.618)

### ⬡ P7 Temporal Lifecycle (JSON)
- **Encoding:** JSON
- **Purpose:** Records when events happen
- **Contains:** Creation timestamp, lifecycle events, temporal anchors, alchemical stage
- **Dimension:** 2D→3D (hexagon tessellates into depth)

### ✦ P9 Wisdom Synthesis (Markdown)
- **Encoding:** Markdown
- **Purpose:** Synthesizes knowledge about folder
- **Contains:** Insights, patterns, relationships, Merkaba geometry
- **Dimension:** 2D (radial expansion like star)

### ⊞ P11 Registry Manifest (JSON)
- **Encoding:** JSON
- **Purpose:** Complete index of folder contents
- **Contains:** All files, subfolders, Prime Petal structure, fractal properties
- **Dimension:** 2D→3D (grid extends recursively)
- **Self-Referential:** Registry includes itself

---

## 🌟 Sacred Geometry Principles

### Golden Ratio (φ = 1.618)
- **P5 Pentagon:** Embodies φ in its geometry
- **King's Chamber:** φ⁻¹ = 38.2% height ratio in Great Pyramid

### Dimensional Progression
- **P1:** 0D (point/seed)
- **P3, P5:** 2D (flat geometric shapes)
- **P7, P11:** 2D→3D (structures that tessellate into depth)
- **P9:** 2D radial (expands outward like consciousness)

### Fractal Self-Similarity
Every subfolder mirrors parent structure:
```
Contains(P1) = [P1]
Contains(P3) = [P3, P1]
Contains(P5) = [P5, P3, P1]
Contains(P7) = [P7, P5, P3, P1]
Contains(P9) = [P9, P7, P5, P3, P1]
Contains(P11) = [P11, P9, P7, P5, P3, P1]
```

---

## 🎨 FIELD Integration

### Frequency Mapping
Prime Petals align with FIELD node frequencies:

| Frequency | Node | Symbol | Role |
|-----------|------|--------|------|
| 396 Hz | Akron | ◻ | Sovereignty gateway |
| 432 Hz | TATA | ▼ | Temporal truth |
| 528 Hz | ATLAS | ▲ | Knowledge patterns |
| 741 Hz | DOJO | ◼︎ | Manifestation |
| 852 Hz | King's Chamber | ⬥ | Translation bridge |
| 963 Hz | OBI-WAN | ● | Unified observation |

### Trust Tier Encoding
- **◉ Deep Truth:** Multiple cross-references, validated
- **◎ Strong Trust:** Cross-referenced, verified
- **◐ Medium Trust:** Some verification
- **○ Low Trust:** Single source, unverified
- **◯ Unknown:** No verification yet

### Alchemical Stages
- **🜚 Nigredo:** Blackening (data ingestion, chaos)
- **🜛 Albedo:** Whitening (organization, Prime Petals)
- **🜜 Citrinitas:** Yellowing (wisdom synthesis)
- **🜝 Rubedo:** Reddening (manifestation, completion)

---

## 📖 Usage Examples

### Example 1: Evidence Archive for Legal Case

```python
from pathlib import Path
from prime_petal_generator import RefinedPrimePetalGenerator

generator = RefinedPrimePetalGenerator()

generator.generate_prime_structure(
    folder_path=Path("/Volumes/Akron/evidence/susan_rich_estate"),
    purpose="Complete evidence archive for Susan Janet Rich estate administration dispute",
    context={
        "case_id": "susan_rich_001",
        "matter": "Susan Janet Rich v. Pointon Partners",
        "parties": ["Susan Janet Rich", "Pointon Partners"],
        "jurisdiction": "NSW Supreme Court",
        "case_start_date": "2024-11-15",
        "poa_date": "2016-08-31",
        "attorney": "James Bradley Bear (JBEAR)"
    }
)
```

### Example 2: Knowledge Base

```python
generator.generate_prime_structure(
    folder_path=Path("/Volumes/Akron/knowledge/legal_research"),
    purpose="Legal research and case law analysis repository",
    context={
        "type": "knowledge_base",
        "domain": "legal_research",
        "primary_node": "▲ ATLAS"
    }
)
```

### Example 3: Communication Archive

```python
generator.generate_prime_structure(
    folder_path=Path("/Volumes/Akron/communications/email_2024"),
    purpose="Email communications archive for 2024",
    context={
        "type": "communications",
        "year": 2024,
        "primary_node": "● OBI-WAN"
    }
)
```

---

## 🧪 Testing

```bash
# Run built-in examples
cd ~/FIELD-macOS-DOJO
python3 tier1-sacred-mcp/akron-gateway/prime_petal_generator.py

# Verify test folder
python3 tier1-sacred-mcp/akron-gateway/verify_prime_petals.py test_prime_petal

# Batch generate in test directory
python3 tier1-sacred-mcp/akron-gateway/batch_generate_prime_petals.py \
    test_prime_petal \
    --auto-context

# Verify recursively
python3 tier1-sacred-mcp/akron-gateway/verify_prime_petals.py \
    test_prime_petal \
    --recursive
```

---

## 📋 Command Reference

### prime_petal_generator.py
```bash
python3 prime_petal_generator.py
# Runs built-in examples creating test folders
```

### batch_generate_prime_petals.py
```bash
python3 batch_generate_prime_petals.py <root_dir> [options]

Options:
  --max-depth N        Maximum folder depth (default: 10)
  --no-skip            Regenerate even if Prime Petals exist
  --auto-context       Auto-generate context from folder names
```

### verify_prime_petals.py
```bash
python3 verify_prime_petals.py <folder> [options]

Options:
  -r, --recursive      Recursively verify subfolders
  --max-depth N        Maximum recursion depth (default: 5)
```

---

## 🔗 Related Documentation

- `ADR-004-merkaba-bidirectional-architecture.md` - Merkaba flow architecture
- `docs/MERKABA-GEOMETRY.md` - Sacred geometry principles
- `docs/AKRON-ETYMOLOGY.md` - Akron naming and meaning
- `modules/hollywood-production/README.md` - Descending flow manifestation

---

## 🎯 Roadmap

- [ ] Auto-update P11 registry when files added/removed
- [ ] P7 lifecycle event tracking hooks
- [ ] Trust tier assignment automation
- [ ] Alchemical stage progression detection
- [ ] Prime Petal validation in MCP servers
- [ ] Visualization of fractal structure
- [ ] Export to graph database (Neo4j)

---

## 📜 License

Part of FIELD-macOS-DOJO architecture
Berjak → FRE → DOJO lineage

---

**Generated with sacred geometry and love** ✦⬥◼︎▲●▼◻
