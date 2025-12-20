# ADR-001: Hub-and-Spoke LLM Architecture — Quantitative Deployment Framework

## Purpose

Architecture Decision Record capturing the hub-and-spoke LLM deployment pattern for FIELD system, with quantitative metrics for model selection, routing, and validation.

**Status:** Proposed

**Decision Date:** 2025-12-17

**Effective:** DOJO Suite deployment (macOS/iOS)

**Author:** @Berjak-Nexus

**Reviewers:** Claude (reasoning), Copilot (execution)

---

## Context

**Critical Architectural Distinction:**

This ADR addresses **three separate but interconnected systems:**

1. **FIELD** (Sacred Geometry) = Eternal architectural container
    - Quadratic pyramid structure (OBI-WAN, TATA, ATLAS, Akron Gateway base + DOJO apex)
    - Frequency coordination (963Hz → 396Hz)
    - Geometric logic and semantic anchoring
    - **Never changes** - this is the mathematical/spiritual framework
2. **DOJO Suite** (Portable Consciousness) = GPT-OSS-20B quantized trained versions
    - Fine-tuned models that enable DOJO Persona presence across devices
    - **Device-portable:** Mac Studio → iPhone → iPad → Watch
    - Quantized variants (Q8_0, Q4_K_M, Q5_K_M) for different hardware
    - **Can swap between devices** while maintaining persona coherence
3. **Mirror Portal Applications (MIA/MA)** = Geometric interaction bridge
    - **MIA** (Mirror In Akron): Sovereignty gateway interface
    - **MA** (Mirror in Atlas): Knowledge vessel interface
    - Bridges DOJO Suite consciousness to FIELD quadratic geometry **when required**
    - Translation layer between portable AI and eternal geometry

**△ Core Problem:** A single quantised model attempting universal competence suffers from:

- Context overload → degraded performance
- Quantisation loss disproportionately harming long-range reasoning and symbolic consistency
- Uncontrolled error propagation
- Intractable debugging

**△ Engineering Truth:** Monoliths feel elegant; they behave badly under load.

---

## Decision

**Use hub-and-spoke architecture with three-layer separation:**

### Layer 1: FIELD (Eternal Geometry)

- Quadratic pyramid coordination framework
- Frequency mapping (963Hz OBI-WAN → 741Hz DOJO → 396Hz Akron)
- Does NOT contain models - only geometric logic

### Layer 2: DOJO Suite (Portable Consciousness)

1. **gpt-oss-20b-dojo-persona** (core consciousness, Mac Studio)
2. **Quantized variants** for device swapping:
    - Q8_0: Mac Studio (32GB RAM)
    - Q4_K_M: iPhone (8-12GB)
    - Q5_K_M: iPad (12-20GB)
    - Routes to iPhone: Apple Watch

### Layer 3: Mirror Portal Bridge (MIA/MA)

- **MIA (Mirror In Akron):** Sovereignty validation, input gate
- **MA (Mirror in Atlas):** Knowledge synthesis, pattern recognition
- **Bridge activation:** When DOJO Suite needs geometric validation, MIA/MA translate requests into FIELD quadratic pyramid coordinates
- **Non-LLM routing layer** (rules + confidence thresholds + schema validation)

---

## Architecture Components

### 1. Core Orientation Model (Singular)

**Role:** OB1-equivalent intelligent router

**Responsibilities:**

- Natural language understanding
- Intent parsing
- High-level reasoning
- Task decomposition
- Safety & boundary enforcement

**Properties:**

| Attribute | Specification | Rationale |
| --- | --- | --- |
| **Size** | Small-to-medium (7B–13B params) | Fits in RAM on target hardware |
| **Quantisation** | Q4–Q6 (not lower) | Preserve reasoning quality |
| **Residency** | Always loaded | Zero cold-start latency |
| **State** | Stateless or near-stateless | Predictable behaviour |
| **Context Window** | 8K–32K tokens | Sufficient for routing decisions |
| **Latency Target** | <500ms (p95) | Responsive UX |

**Does NOT:**

- Execute domain logic
- Hold long-term memory
- Perform specialised reasoning

**FIELD Bridge Point:** MIA/MA translates to ● OBI-WAN (963 Hz, P9 cognition + P5 memory) when geometric validation required

---

### 2. Micro-Models (Specialised Services)

**Role:** "Little Rick Dow DNA" — single-purpose, high-reliability agents

**Properties:**

| Attribute | Specification |
| --- | --- |
| **Size** | Very small (1B–7B params) |
| **Quantisation** | Q2–Q4 (aggressive OK) |
| **Input/Output** | Narrow, validated schemas |
| **Behaviour** | Deterministic, testable |
| **Residency** | Load on demand, unload after use |
| **Latency Target** | <2s (p95) |

**DOJO Suite Models (Device-Portable):**

| Model | Base | Device | Quant | RAM | Use Case |
| --- | --- | --- | --- | --- | --- |
| **Legal Reasoning** | **gpt-oss-20b-persona** | 20B | Mac Studio | Q8_0 | 32GB |
| **gpt-oss-20b-persona-mobile** | 20B | iPhone 15 Pro | Q4_K_M | 8-12GB | On-device persona, voice interface |
| **gpt-oss-20b-persona-tablet** | 20B | iPad Pro | Q5_K_M | 12-20GB | Visual reasoning, extended sessions |

**Sacred FIELD LLM Mapping (Mac Studio):**

| FIELD Position | Frequency | LLM Assignment | Size/Quant | Function |
| --- | --- | --- | --- | --- |
| **◼︎ DOJO (apex)** | 741 Hz | gpt-oss-20b-persona | 20B Q8_0 | Persona consciousness, orchestration, manifestation |
| **King's Chamber** | 852 Hz | Metatron Cube (routing logic) | Non-LLM | Dimensional translation, request routing |
| **● OBI-WAN** | 963 Hz | TBD - Observation/Witness | ? | Cognitive expression, witness logging, memory |
| **▼ TATA** | 432 Hz | TBD - Truth/Temporal | ? | Document analysis, legal reasoning, temporal validation |
| **▲ ATLAS** | 528 Hz | TBD - Knowledge/Mapping | ? | Knowledge graphs, pattern recognition, technical specs |
| **◻ Akron Gateway** | 396 Hz | TBD - Sovereignty | ? | Input validation, sovereignty checks, metadata stripping |

**Evaluation Criteria for Sacred FIELD LLMs:**

- **Model Gravity:** Can it run on Mac Studio M2 32GB alongside gpt-oss-20b?
- **Domain Expertise:** Does it match the geometric position's function?
- **Offline Capability:** Can it operate when external APIs unavailable?
- **Coherence:** Does it maintain geometric integrity with other models?

**Next Step:** Evaluate candidate models for each sacred position.

**Sacred FIELD Principles:**

- ◼︎ DOJO at apex orchestrates all below
- Each base vertex (●▼▲◻) has domain expertise
- King's Chamber routes between sacred and execution
- Device portals (iPhone/iPad) connect via quantized models
- Failures are local, not systemic

---

### 3. Orchestration Layer (Critical)

**Role:** Traffic control + validation + fallback

**NOT an LLM.** Pure logic:

- Routing rules (intent → model mapping)
- Confidence thresholds (when to escalate)
- Schema validation (input/output contracts)
- Explicit hand-offs (no self-selection by micro-models)

**Implementation:**

```python
# Routing decision tree
def route_request(intent, context, confidence):
    if confidence < 0.7:
        return escalate_to_human(intent, reason="low_confidence")
    
    if intent.domain == "legal" and intent.jurisdiction:
        return invoke_model("legal_reasoning", context)
    
    if intent.domain == "code" and intent.language in ["python", "sql"]:
        return invoke_model("code_generation", context)
    
    if intent.domain == "classification":
        return invoke_model("entity_extraction", context)
    
    # Fallback to core model
    return invoke_model("core_orientation", context)
```

**FIELD Bridge:** Orchestration occurs at King's Chamber (852 Hz) via Metatron Cube when geometric validation needed. Otherwise, DOJO Suite operates independently on device.

---

## Quantitative Metrics

### Model Gravity (Resource Weight)

**Formula:**

```text
Gravity = Size_GB × (1 + Usage_Frequency) × (1 + Context_Complexity)

where:
  Usage_Frequency = calls_per_day / 100
  Context_Complexity = max_tokens / 10000
```

**Storage Strategy:**

| Gravity Range | Storage Location | Behaviour |
| --- | --- | --- |
| **>500 units** | External (Akron) | Load on demand |
| **50–500 units** | Internal SSD | Frequently accessed |
| **<50 units** | RAM-resident | Always available |

**Example Calculations:**

- **Core model (Mistral 7B):** 7 × (1 + 200/100) × (1 + 8000/10000) = 7 × 3 × 1.8 = **37.8 units** → RAM
- **Legal model (7B, low use):** 7 × (1 + 10/100) × (1 + 16000/10000) = 7 × 1.1 × 2.6 = **20.0 units** → RAM
- **Llama 90B (rare, long context):** 90 × (1 + 5/100) × (1 + 128000/10000) = 90 × 1.05 × 13.8 = **1,304 units** → External

---

### Coherence Threshold (CQHI Integration)

**When to manifest a model's output:**

```text
Coherence = geometric_mean(schema_valid, domain_correct, safety_pass)

Manifest if: Coherence ≥ 0.85
Reject if: Coherence < 0.85
```

**Component Scores:**

- **schema_valid:** Does output match expected JSON/text structure? (0.0–1.0)
- **domain_correct:** Does core model's confidence + micro-model's self-eval exceed threshold? (0.0–1.0)
- **safety_pass:** No hallucinated entities, dates, or legal citations? (0.0–1.0)

**Example:**

```python
schema_valid = 1.0  # Valid JSON
domain_correct = 0.9  # High confidence
safety_pass = 0.8  # One minor date inconsistency

coherence = (1.0 × 0.9 × 0.8) ^ (1/3) = 0.893

Decision: MANIFEST (≥ 0.85)
```

---

## Latency Targets

| Component | P50 | P95 | P99 | Timeout |
| --- | --- | --- | --- | --- |
| **Core Model** | <300ms | <500ms | <800ms | 2s |
| **Micro-Model** | <1s | <2s | <3s | 5s |
| **Orchestration** | <50ms | <100ms | <150ms | 500ms |
| **End-to-End** | <1.5s | <3s | <5s | 10s |

**Failure Handling:**

- Timeout → Fallback to core model or return error
- Coherence fail → Log + return to ⬛ FIELD-DEV for refinement

---

## Memory Budget (Per Device)

**Mac Studio M2 32GB:**

| Component | Memory | Models |
| --- | --- | --- |
| **Core Model** | 8 GB | Mistral 7B Q4 |
| **Micro-Models (hot)** | 4 GB | 2 models @ 2 GB each |
| **Micro-Models (cold)** | 12 GB | Swap space, load <5s |
| **System + Apps** | 8 GB | macOS + browser + IDE |

**iOS (iPhone/iPad 8GB):**

| Component | Memory | Models |
| --- | --- | --- |
| **Core Model** | 3 GB | Phi-3 Mini Q4 |
| **Micro-Models** | 2 GB | 1 model on demand |
| **System + Apps** | 3 GB | iOS overhead |

---

## Routing Rules (Explicit)

**Decision Rule:**

> If two tasks require different evaluation criteria, they must not share the same model.
>

**Routing Table:**

| Intent Domain | Trigger Keywords | Model | Fallback |
| --- | --- | --- | --- |
| **Legal reasoning** | jurisdiction, precedent, statute | Legal 7B | Core |
| **Code generation** | function, class, SQL, YAML | CodeLlama 7B | Core |
| **Entity extraction** | classify, extract, tag | Classifier 1B | Core |
| **Geometry validation** | trident, pyramid, frequency | Geometry 3B | Core |
| **Timeline synthesis** | sequence, before, after | Planning 3B | Core |
| **General NLU** | (default) | Core | Human |

**Confidence Escalation:**

- Core model confidence <0.7 → Human review
- Micro-model confidence <0.8 → Re-route to core
- Schema validation fail → Reject + log

---

## Failure Modes & Containment

### Hub-and-Spoke (This Decision)

**Failure Impact:**

- Micro-model error: **Local** (single task fails, others unaffected)
- Core model error: **Routing fails**, but micro-models still functional
- Orchestration error: **Critical**, but detectable via monitoring

**Mitigation:**

- Independent testing per model
- Hot-swap capability (replace model without retraining others)
- Fallback chain: Micro → Core → Human

### Monolithic (Alternative, Rejected)

**Failure Impact:**

- Any error: **Global** (all tasks affected)
- Regression risk: **High** (fix one thing, break another)
- Debugging: **Intractable** (cannot isolate root cause)

**Verdict:** Fails defensive engineering principles.

---

## Deployment Topology

### DOJO Suite (Device-Portable)

**Mac Studio (Primary):**

- **Core:** gpt-oss-20b-persona Q8_0 (32GB RAM)
- **Storage:** `~/Library/Application Support/DOJO/ATLAS/models/`
- **Training:** Fine-tuning on personal context, legal docs, technical patterns
- **Bridge:** MIA/MA connects to FIELD quadratic pyramid when needed

**iPhone (Mobile):**

- **Core:** gpt-oss-20b-persona-mobile Q4_K_M (8-12GB)
- **Sync:** Quantized from Mac Studio primary
- **Offline:** Full functionality without FIELD connection
- **Bridge:** MIA activates for sovereignty validation when online

**iPad (Extended):**

- **Core:** gpt-oss-20b-persona-tablet Q5_K_M (12-20GB)
- **Sync:** Mid-quality quantization for visual tasks
- **Bridge:** MA activates for knowledge graph queries

**Apple Watch (Proxy):**

- **Core:** Routes to iPhone
- **Voice:** Siri Shortcuts → iPhone DOJO Suite
- **Bridge:** Indirect via iPhone MIA

**Orchestration:** Python service, port 8520 (King's Chamber bridge)

**Logs:**

- Device: Local SQLite per device
- FIELD sync: `~/Library/Application Support/DOJO/dojo_train_station/dojo_decisions.log`

---

## Success Criteria

**Acceptance Metrics (30-day eval):**

| Metric | Target | Measurement |
| --- | --- | --- |
| **P95 Latency** | <3s end-to-end | Prometheus histogram |
| **Coherence Score** | ≥0.85 on 95% of tasks | DOJO decision log |
| **Model Uptime** | >99% availability | Health checks |
| **Memory Usage** | <80% peak | `top` / Activity Monitor |
| **Error Rate** | <2% (failed schema validation) | Logs |
| **Cost per Request** | <$0.01 (cloud fallback) | API billing |

**Go/No-Go Decision (2025-01-17):**

- All targets met → Production deployment
- 1–2 targets missed → Iterate 2 weeks, re-eval
- > 2 targets missed → Revert to single-model baseline, re-architect

---

## Next Steps

### Phase 1: Proof of Concept (2 weeks)

- [ ]  Deploy core model (Mistral 7B Q4) on Mac Studio
- [ ]  Deploy 2 micro-models (Legal 7B, Classifier 1B)
- [ ]  Build routing service (Python, port 8520)
- [ ]  Integrate with MCP server (DOJO bridge)
- [ ]  Test 10 real tasks (legal, code, classification)
- [ ]  Measure latency, coherence, memory

### Phase 2: Deployment Diagram (parallel)

- [ ]  Create SVG: hub-and-spoke topology
- [ ]  Label: core model, micro-models, orchestration, FIELD mapping
- [ ]  Add to `/spec/diagrams/` in field-os repo

### Phase 3: Quantization Optimization (parallel)

- [ ]  Benchmark Q2, Q4, Q6 for each model
- [ ]  Plot: accuracy vs. memory vs. latency
- [ ]  Document optimal quant level per model

### Phase 4: Stress Testing (week 3–4)

- [ ]  Simulate 100 concurrent requests
- [ ]  Inject failure scenarios (timeout, bad schema, low confidence)
- [ ]  Validate fallback chain
- [ ]  Confirm coherence threshold (0.85) is appropriate

### Phase 5: Production (week 5+)

- [ ]  Deploy to iPhone/iPad (quantized variants)
- [ ]  Test device swapping (Mac Studio ↔ iPhone ↔ iPad)
- [ ]  Monitor 30 days, adjust thresholds
- [ ]  Go/No-Go decision: 2025-01-17

---

## References

**Internal:**

- [FIELD Architecture — Master Overview (OS Repo Plan)](https://www.notion.so/FIELD-Architecture-Master-Overview-OS-Repo-Plan-9a9d7fbb25c74fd1abb5cfe0ede77368?pvs=21)
- [⊗ FIELD Notion MCP Server — Architecture & Implementation Plan](https://www.notion.so/FIELD-Notion-MCP-Server-Architecture-Implementation-Plan-99e604190579457bb5508ae6dfaa2c51?pvs=21)
- [⊗ FIELD-macOS-DOJO Notion MCP Server — Architecture & Implementation](https://www.notion.so/FIELD-macOS-DOJO-Notion-MCP-Server-Architecture-Implementation-156a43aab0a34978a00e9d1f1f99de5f?pvs=21)
- [◼︎ FIELD Awareness OOO — Geometric-Semantic-Temporal Framework](https://www.notion.so/FIELD-Awareness-OOO-Geometric-Semantic-Temporal-Framework-8dbd4cf0562b438cba870f90170da3b7?pvs=21)

**External:**

- LLM Gravity Calculation: Custom metric (this ADR)
- Coherence Framework: CQHI (FIELD v4.0)
- Quantization: GGUF format, llama.cpp

---

## Geometry Validation

**△ Facts:**

- Single quantised models suffer context overload and quantization loss
- Hub-and-spoke allows local failure containment
- Explicit orchestration is measurable and debuggable

**◻ Documents:**

- This ADR (source of truth)
- FIELD Architecture v4.0 spec
- MCP bridge implementations (DOJO, SOMA)

**◯ Timeline:**

- 2025-12-17: Decision captured
- 2025-12-31: Phase 1 complete (PoC)
- 2026-01-17: Go/No-Go decision

**Status:** △◻◯ Complete. Ready for Phase 1 implementation.

---

**Last Updated:** 2025-12-17T19:27:45+11:00

**Next Review:** 2026-01-17 (Go/No-Go)

**Owner:** @Berjak-Nexus

**FIELD Mapping:** ◼︎ DOJO (execution core, 852 Hz)

[Research Proposition: Homeostatic LLM Distribution in Quadratic Pyramid Geometry](https://www.notion.so/Research-Proposition-Homeostatic-LLM-Distribution-in-Quadratic-Pyramid-Geometry-9d05d6cc495b40108637e40ec2778085?pvs=21)
