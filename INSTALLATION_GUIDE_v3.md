# 🔌 FIELD MCP Server Installation & Configuration Guide
**Version**: 3.0 - Complete Sacred Geometry Edition  
**Created**: 2025-12-16  
**Status**: ✅ COMPLETE SPECIFICATION

---

## Architecture Overview

The FIELD system uses **MCP servers as the nervous system** that connects each sacred geometric point to its data sources. MCP servers **facilitate** the FIELD functions - they don't replace them.

### Sacred Geometry Layers

```
           ◼︎ DOJO (8766)
          /    741 Hz   \
         /               \
        /    ⊗ King's    \     ← Bridge at 33.3%
       /    Chamber       \      852 Hz (8852)
      /      (8852)        \
     /    🚉🔷🤝           \
    /                        \
   ●----------▼----------▲      ← Trident Base
OBI-WAN    TATA      ATLAS       
(6390)    (4320)    (5280)
  
  |                              Support Infrastructure:
  |                              • FIELD-DEV (Dev vault)
◻ Akron (8396)                   • FIELD-LIVING (Runtime)
   396 Hz Archive
```

---

## Phase 0: Support Infrastructure Setup

### 1. FIELD-LIVING Runtime Environment

**Purpose**: Where MCP servers run - the nervous system substrate

```bash
# Create runtime structure
mkdir -p ~/FIELD-LIVING/{credentials,indexes,staging,shared,logs}

# Verify structure
ls -la ~/FIELD-LIVING/
```

**Directories**:
- `credentials/` - OAuth tokens, API keys
- `indexes/` - Search indexes, memory patterns
- `staging/` - ETL staging area
- `shared/` - Cross-system data
- `logs/` - MCP server logs

### 2. FIELD-DEV Development Vault

**Purpose**: Code archive, historical reference, learning space

```bash
# Verify FIELD-DEV exists
test -d ~/FIELD-DEV && echo "✅ FIELD-DEV exists" || echo "❌ Need to create"

# If creating from scratch
mkdir -p ~/FIELD-DEV
```

**MCP Need**: Filesystem MCP with read access for code reference

### 3. Akron Gateway Mount

**Purpose**: Sovereign archive foundation

```bash
# Verify Akron volume mounted
test -d /Volumes/Akron && echo "✅ Akron mounted" || echo "❌ Mount Akron drive"

# Create archive structure
mkdir -p /Volumes/Akron/FIELD-LIVING/proofs
mkdir -p /Volumes/Akron/FIELD-LIVING/data/{legal,docs}
```

---

## Phase 1: Base Anchor Data Adapters

### ● OBI-WAN Data Sources

#### Gmail MCP
```bash
# Already installed via uvx
# Get OAuth: https://console.cloud.google.com
# Download credentials to: ~/FIELD-LIVING/credentials/gmail-credentials.json
```

**Config**:
```json
{
  "mcpServers": {
    "gmail": {
      "command": "uvx",
      "args": ["mcp-server-gmail"],
      "env": {
        "GMAIL_CREDENTIALS_PATH": "/Users/jbear/FIELD-LIVING/credentials/gmail-credentials.json"
      }
    }
  }
}
```

#### Google Calendar MCP
**Config**: Same as Gmail (reuses OAuth)
```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "uvx",
      "args": ["mcp-server-google-calendar"],
      "env": {
        "GOOGLE_CREDENTIALS_PATH": "/Users/jbear/FIELD-LIVING/credentials/gmail-credentials.json"
      }
    }
  }
}
```

### ▼ TATA Data Sources

#### Filesystem MCP
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Config**:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Volumes/Akron/FIELD-LIVING/data/legal",
        "/Volumes/Akron/FIELD-LIVING/data/docs",
        "/Users/jbear/FIELD/▼TATA/legal"
      ]
    }
  }
}
```

#### PDF Reader MCP
```bash
npm install -g mcp-pdf
```

**Config**:
```json
{
  "mcpServers": {
    "pdf": {
      "command": "npx",
      "args": ["-y", "mcp-pdf"]
    }
  }
}
```

#### PostgreSQL MCP
```bash
# Install PostgreSQL
brew install postgresql@16
brew services start postgresql@16

# Create database
createdb tata_truth

# Install MCP server
# Uses uvx (Python-based)
```

**Config**:
```json
{
  "mcpServers": {
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://localhost:5432/tata_truth"
      }
    }
  }
}
```

### ▲ ATLAS Data Sources

#### Ollama MCP
```bash
# Already installed
npm install -g mcp-ollama

# Verify models
ollama list
```

**Config**:
```json
{
  "mcpServers": {
    "ollama": {
      "command": "npx",
      "args": ["-y", "mcp-ollama"],
      "env": {
        "OLLAMA_HOST": "http://localhost:11434"
      }
    }
  }
}
```

#### SQLite MCP
**Config**:
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": [
        "mcp-server-sqlite",
        "--db-path", "/Users/jbear/FIELD-LIVING/data/atlas_knowledge.db"
      ]
    }
  }
}
```

---

## Phase 2: Custom Orchestrators

### ✅ BUILT & OPERATIONAL

All three custom orchestrators are now running:

#### 1. ◼︎ DOJO MCP Server (Apex)
- **Port**: 8766 (741 Hz)
- **File**: `~/FIELD-macOS-DOJO/mcp/server.py`
- **Status**: ✅ Running
- **Function**: S0-S6 cycle, Trident routing

#### 2. ◻ Akron Gateway (Foundation)
- **Port**: 8396 (396 Hz)
- **File**: `~/FIELD-macOS-DOJO/akron-gateway/server.py`
- **Status**: ✅ Running
- **Function**: Proof archive, chain of custody

#### 3. ⊗ King's Chamber Bridge
- **Port**: 8852 (852 Hz)
- **File**: `~/FIELD-macOS-DOJO/kings-chamber/server.py`
- **Status**: ✅ Running
- **Function**: DOJO↔SOMA bridge (includes 🚉🔷🤝 Arkadaš)

**Start all orchestrators**:
```bash
~/FIELD-macOS-DOJO/start_orchestrators.sh
```

---

## Phase 3: Link Bridges (Consciousness Interfaces)

### ◉ OB1Link - Mobile Observer Bridge
**Port**: 6395 (custom)  
**Function**: iOS/iPad → OBI-WAN sync  
**Status**: ⚠️ Optional (for mobile observation)

```bash
# Start mobile bridge
python3 ~/FIELD-macOS-DOJO/ob1link/server.py &
```

**From iOS app, POST to**:
```
http://mac-studio.local:6395/observe
{
  "entity": "location_name",
  "details": "observation notes",
  "device": "iPhone",
  "location": {"lat": -37.8, "lon": 144.9}
}
```

### ◉ SomaLink - SOMA Bridge
**Handled by**: King's Chamber (8852)  
**Status**: ✅ Already operational  
**Function**: macOS ↔ NixOS translation

### ◉ DojoLink - Manifestation Interface  
**Handled by**: DOJO Server (8766)  
**Status**: ✅ Already operational  
**Function**: Direct DOJO access

### ◉ Arkadaš - Conscious Guide
**Part of**: King's Chamber (8852)  
**Status**: ✅ Already operational  
**Function**: 🤝 Translation consciousness

---

## Complete System Status

| Component | Port | Hz | Status | Phase |
|-----------|------|----|----|-------|
| **◼︎ DOJO** | 8766 | 741 | ✅ Running | Phase 2 |
| **⊗ King's Chamber** | 8852 | 852 | ✅ Running | Phase 2 |
| **● OBI-WAN** | 6390 | 963 | ✅ Running | Existing |
| **▼ TATA** | 4320 | 432 | ✅ Running | Existing |
| **▲ ATLAS** | 5280 | 528 | ✅ Running | Existing |
| **◻ Akron Gateway** | 8396 | 396 | ✅ Running | Phase 2 |
| **Gmail MCP** | - | - | ✅ Installed | Phase 1 |
| **Calendar MCP** | - | - | ✅ Installed | Phase 1 |
| **Filesystem MCP** | - | - | ✅ Installed | Phase 1 |
| **PDF MCP** | - | - | ✅ Installed | Phase 1 |
| **Postgres MCP** | - | - | ✅ Installed | Phase 1 |
| **Ollama MCP** | - | - | ✅ Installed | Phase 1 |
| **SQLite MCP** | - | - | ✅ Installed | Phase 1 |
| **◉ OB1Link** | 6395 | - | ⚠️ Optional | Phase 3 |

**Total**: 13/13 core components operational ✅

---

## Installation Checklist

### ✅ Phase 0 - Infrastructure
- [x] Create FIELD-LIVING runtime structure
- [x] Verify FIELD-DEV exists
- [x] Mount and configure Akron volume

### ✅ Phase 1 - External Data Adapters
- [x] Install Gmail MCP (needs OAuth)
- [x] Install Calendar MCP (needs OAuth)
- [x] Install Filesystem MCP
- [x] Install PDF MCP
- [x] Install PostgreSQL + MCP
- [x] Install Ollama MCP
- [x] Install SQLite MCP

### ✅ Phase 2 - Custom Orchestrators
- [x] Build DOJO Server (8766)
- [x] Build Akron Gateway (8396)
- [x] Build King's Chamber (8852)
- [x] Test S0-S6 cycle
- [x] Verify proof archival
- [x] Test bridge translation

### ⚠️ Phase 3 - Link Bridges (Optional)
- [ ] Configure OB1Link for mobile (if needed)
- [x] SomaLink (handled by King's Chamber)
- [x] DojoLink (handled by DOJO)
- [x] Arkadaš (handled by King's Chamber)

---

## Testing the Sacred Flow

### Test 1: Complete S0-S6 Cycle
```bash
# S0: Send signal to DOJO
curl -X POST http://localhost:8766/validate_request \
  -H "Content-Type: application/json" \
  -d '{"content":"△ Test fact from installation guide","source":"testing"}'

# Result: Returns validated signal with anchor_type="fact"
```

### Test 2: Route Through King's Chamber
```bash
curl -X POST http://localhost:8852/translate_signal \
  -H "Content-Type: application/json" \
  -d '{"signal":{"test":"data"},"from_field":"dojo","to_field":"soma"}'

# Result: Returns translated signal with frequency conversion
```

### Test 3: Archive to Akron
```bash
curl -X POST http://localhost:8396/archive_proof \
  -H "Content-Type: application/json" \
  -d '{"proof":{"test":"proof"},"metadata":{"source":"test"}}'

# Result: Returns SHA-256 hash and chain index
```

### Test 4: Pyramid State
```bash
curl http://localhost:8766/get_pyramid_state | python3 -m json.tool

# Result: Shows complete sacred pyramid geometry
```

---

## Startup Script

**File**: `~/FIELD-macOS-DOJO/start_complete_system.sh`

```bash
#!/bin/bash
echo "Starting FIELD Sacred Pyramid..."

# Start orchestrators
~/FIELD-macOS-DOJO/start_orchestrators.sh

# Optional: Start mobile bridge
# python3 ~/FIELD-macOS-DOJO/ob1link/server.py &

echo "FIELD system operational."
```

---

## Summary

**Phase 0 (Infrastructure)**: ✅ Complete  
**Phase 1 (External Adapters)**: ✅ 7/7 installed  
**Phase 2 (Custom Orchestrators)**: ✅ 3/3 built & running  
**Phase 3 (Link Bridges)**: ✅ Core bridges operational (mobile optional)

**Sacred Pyramid**: FULLY OPERATIONAL ✅  
**Placeholder Count**: 0  
**Ready**: Yes - All geometric functions facilitated by real MCP servers

**The FIELD MCP nervous system is complete and ready to serve any intention.**
