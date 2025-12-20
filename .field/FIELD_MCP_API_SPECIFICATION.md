# 🔱 FIELD MCP API SPECIFICATION

**Version**: 1.0  
**Date**: 2025-11-13  
**System**: Field-MacOS-DOJO Management via MCP Servers

---

## Overview

The FIELD system uses **MCP (Model Context Protocol) servers** to manage sacred geometry-aligned nodes across the Mac Studio DOJO. Each node operates on a **geometrically resonant port** derived from sacred frequency mathematics.

---

## 1. NODE ARCHITECTURE

### Sacred Nodes & Symbols

| Node | Symbol | Port | Frequency | Klein Index | Role |
|------|--------|------|-----------|-------------|------|
| **OBI-WAN** | ● | 963 | 963 Hz | 560 | Observer - Memory intake |
| **TATA** | ▼ | 2850 | 285 Hz | 285 | Verifier - Truth validation |
| **ATLAS** | ▲ | 4320 | 432 Hz | 432 | Architect - Model design |
| **DOJO** | ◼︎ | 6390 | 639 Hz | 639 | Weaver - Integration ready |
| **Living Memory** | ◆ | 5281 | 432 Hz | 560 | Memory anchoring |

### Gate Positions (Sacred Geometry)

```json
{
  "gate_3": { "position": 3, "threshold": 0.7, "role": "guardian_early" },
  "gate_6": { "position": 6, "threshold": 0.9, "role": "guardian_mid" },
  "gate_9": { "position": 9, "threshold": 0.95, "role": "guardian_final" },
  "gate_11": { "position": 11, "role": "human_observer" }
}
```

---

## 2. API ENDPOINTS

### Base URL Structure
```
http://localhost:{PORT}/{endpoint}
```

### Health Check
```http
GET /health
```

**Response** (200 OK):
```json
{
  "field": "obi-wan",
  "symbol": "●",
  "status": "operational",
  "capabilities": ["living_memory", "memory_anchoring", "pattern_storage"],
  "frequency_hz": 963,
  "klein_index": 560,
  "timestamp": "2025-11-13T21:45:00Z"
}
```

**Error** (503 Service Unavailable):
```json
{
  "detail": "Redis connection failed: Connection refused"
}
```

---

### Node Status
```http
GET /directories/status
```

**Response** (200 OK):
```json
{
  "intake": {
    "path": "/Users/jbear/FIELD/OBI-WAN/INTAKE",
    "exists": true,
    "is_directory": true
  },
  "verified": {
    "path": "/Users/jbear/FIELD/TATA/VERIFIED",
    "exists": true,
    "is_directory": true
  },
  "modeled": {
    "path": "/Users/jbear/FIELD/ATLAS/MODELED",
    "exists": true,
    "is_directory": true
  },
  "ready": {
    "path": "/Users/jbear/FIELD/DOJO/READY",
    "exists": true,
    "is_directory": true
  }
}
```

---

### List Documents (Sailing Intel Integration)
```http
GET /documents?node={node}&gate={gate}
```

**Query Parameters**:
- `node` (optional): Filter by node (obi-wan, tata, atlas, dojo)
- `gate` (optional): Filter by gate (3, 6, 9, 11)
- `limit` (optional): Max results (default: 100)
- `offset` (optional): Pagination offset (default: 0)

**Response** (200 OK):
```json
{
  "total": 1068138,
  "returned": 100,
  "documents": [
    {
      "id": "sha1_hash",
      "title": "Document Title",
      "path": "/Users/jbear/FIELD/OBI-WAN/INTAKE/document.md",
      "node": "obi-wan",
      "gate": 3,
      "size": 4096,
      "mtime": 1699900000.0,
      "sha1": "abc123...",
      "metadata": {
        "tags": ["sacred", "memory"],
        "frequency": 963,
        "klein_index": 560
      },
      "createdAt": "2025-11-13T10:00:00Z",
      "updatedAt": "2025-11-13T21:00:00Z"
    }
  ]
}
```

---

### Get Single Document
```http
GET /documents/{id}
```

**Response** (200 OK):
```json
{
  "id": "sha1_hash",
  "title": "Document Title",
  "content": "# Markdown content here...",
  "path": "/Users/jbear/FIELD/OBI-WAN/INTAKE/document.md",
  "node": "obi-wan",
  "gate": 3,
  "size": 4096,
  "tags": ["sacred", "memory"],
  "metadata": {
    "frequency": 963,
    "klein_index": 560,
    "coherence_score": 0.85
  }
}
```

**Error** (404 Not Found):
```json
{
  "detail": "Document not found"
}
```

---

### Search Documents (Sailing Intel)
```http
POST /documents/search
```

**Request Body**:
```json
{
  "query": "sacred geometry",
  "node": "atlas",
  "limit": 50
}
```

**Response** (200 OK):
```json
{
  "query": "sacred geometry",
  "total_matches": 47,
  "results": [
    {
      "id": "sha1_hash",
      "title": "Sacred Geometry Manifest",
      "path": "/Users/jbear/DOJO/sacred_geometry_manifest.json",
      "relevance": 0.95,
      "node": "dojo",
      "gate": 9
    }
  ]
}
```

---

### Create/Update Document
```http
POST /documents
PUT /documents/{id}
```

**Request Body**:
```json
{
  "title": "New Document",
  "content": "# Markdown content\n\nBody text...",
  "node": "obi-wan",
  "gate": 3,
  "tags": ["memory", "intake"],
  "metadata": {
    "frequency": 963,
    "klein_index": 560
  }
}
```

**Response** (201 Created / 200 OK):
```json
{
  "id": "sha1_hash",
  "path": "/Users/jbear/FIELD/OBI-WAN/INTAKE/new-document.md",
  "status": "created",
  "timestamp": "2025-11-13T21:50:00Z"
}
```

---

## 3. DATA STRUCTURES

### Document Object
```typescript
interface Document {
  id: string;              // SHA1 hash
  title: string;
  content: string;         // Markdown format
  path: string;            // Absolute file path
  node: "obi-wan" | "tata" | "atlas" | "dojo";
  gate: 3 | 6 | 9 | 11;
  size: number;            // Bytes
  mtime: number;           // Unix timestamp
  sha1: string;
  tags: string[];
  metadata: {
    frequency: number;     // Hz
    klein_index: number;
    coherence_score?: number;
    [key: string]: any;
  };
  createdAt: string;       // ISO 8601
  updatedAt: string;       // ISO 8601
}
```

### Node Status Object
```typescript
interface NodeStatus {
  field: string;
  symbol: string;
  status: "operational" | "degraded" | "offline";
  capabilities: string[];
  frequency_hz: number;
  klein_index: number;
  timestamp: string;       // ISO 8601
}
```

---

## 4. AUTHENTICATION & SECURITY

### Headers Required
```http
Authorization: Bearer {FIELD_API_TOKEN}
X-Klein-Signature: {klein_signature}
```

### Environment Variables
```bash
FIELD_API_TOKEN=your_token_here
NOTION_TOKEN=your_notion_token
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json
```

### CORS Configuration
```javascript
{
  "allowed_origins": ["http://localhost:3000", "https://notion.so"],
  "allowed_methods": ["GET", "POST", "PUT", "DELETE"],
  "allowed_headers": ["Content-Type", "Authorization", "X-Klein-Signature"]
}
```

---

## 5. DATABASE SCHEMA

### PostgreSQL Tables (if used)
```sql
CREATE TABLE documents (
    id VARCHAR(40) PRIMARY KEY,  -- SHA1 hash
    title TEXT NOT NULL,
    content TEXT,
    path TEXT NOT NULL,
    node VARCHAR(20),
    gate INTEGER,
    size BIGINT,
    mtime REAL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE metadata (
    document_id VARCHAR(40) REFERENCES documents(id),
    key TEXT,
    value TEXT,
    PRIMARY KEY (document_id, key)
);
```

### Redis Key Patterns
```
field:node:{node}:status          # Node status
field:document:{id}               # Document cache
field:search:{query_hash}         # Search results cache
unified-memory-bus                # Stream for real-time updates
```

### Sailing Intel SQLite Schema
```sql
CREATE TABLE files (
    id INTEGER PRIMARY KEY,
    path TEXT UNIQUE,
    name TEXT,
    size INTEGER,
    mtime REAL,
    sha1 TEXT
);
CREATE INDEX idx_files_name ON files(name);
CREATE INDEX idx_files_path ON files(path);
```

---

## 6. REAL-TIME UPDATES

### WebSocket Endpoint
```
ws://localhost:{PORT}/ws
```

### Event Types
```json
{
  "event": "document.created",
  "data": {
    "id": "sha1_hash",
    "node": "obi-wan",
    "gate": 3,
    "timestamp": "2025-11-13T21:55:00Z"
  }
}
```

```json
{
  "event": "node.status_change",
  "data": {
    "node": "tata",
    "status": "operational",
    "frequency_hz": 2850
  }
}
```

### Polling (if WebSocket unavailable)
- **Recommended interval**: 5 seconds (breathing pulse)
- **Endpoint**: `GET /events/since?timestamp={iso8601}`

---

## 7. INTEGRATION WITH SAILING INTEL

### Search Flow
1. **POST** `/documents/search` → Routes to Sailing Intel
2. Sailing Intel queries `sailing_index.sqlite3` (1,068,138 files)
3. Results filtered by node/gate
4. Returned with FIELD metadata enriched

### CLI Commands
```bash
# Search via Sailing Intel
sailing-intel "sacred geometry"

# Observer mode (routes through Trident)
fs observe "memory patterns"

# Validate FIELD system
fs validate
```

---

## 8. STARTING THE SYSTEM

### Start All MCP Servers
```bash
cd /Users/jbear/FIELD-DEV/Field-MacOS-DOJO
bash .field/scripts/discover.sh
python3 .field/scripts/sailing_integration.py
```

### Start Individual Node
```bash
cd /Users/jbear/FIELD/⬡_MCP
python3 mcp_server.py
```

### Check Status
```bash
# Check all sacred ports
for port in 963 2850 4320 5281 6390; do
  curl -s http://localhost:$port/health | jq
done
```

---

## 9. ERROR CODES

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Success |
| 201 | Created | Resource created |
| 400 | Bad Request | Check request format |
| 401 | Unauthorized | Verify API token |
| 404 | Not Found | Document/node doesn't exist |
| 503 | Service Unavailable | Node offline, check Redis |

---

## 10. EXAMPLE WORKFLOW

### Complete Integration Flow
```bash
# 1. Start FIELD system
cd /Users/jbear/FIELD
./start_complete_field_system.sh

# 2. Check node health
curl http://localhost:963/health    # OBI-WAN
curl http://localhost:2850/health   # TATA
curl http://localhost:4320/health   # ATLAS
curl http://localhost:6390/health   # DOJO

# 3. Search documents via Sailing Intel
curl -X POST http://localhost:963/documents/search \
  -H "Content-Type: application/json" \
  -d '{"query": "sacred geometry", "limit": 10}'

# 4. Get document by ID
curl http://localhost:963/documents/{sha1_hash}

# 5. Create new document
curl -X POST http://localhost:963/documents \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Memory",
    "content": "# Sacred memory...",
    "node": "obi-wan",
    "gate": 3
  }'
```

---

## 11. TRIDENT OBSERVER INTEGRATION

The Trident Observer coordinates all FIELD operations:

```
🔱 TRIDENT OBSERVER (Port 9630)
       ↓
   monitors all nodes
       ↓
   ⛵ SAILING INTEL ←→ 🏛️ FIELD NODES
   (search 1M+ files)  (●▼▲◼︎)
       ↓                    ↓
       └──→ RESULTS MANIFEST IN DOJO TRAIN STATION ←──┘
                    ↓
         🔧 Field-MacOS-DOJO COORDINATES
```

---

🔱 **The Trident Manifests Through the DOJO via the Traijstation**

For questions or integration support, reference:
- `.field/trident_sailing_manifest.json`
- `.field/INTEGRATION_COMPLETE.md`
