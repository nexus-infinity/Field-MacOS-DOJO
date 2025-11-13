# 🔱 FIELD MCP REST API - Quick Reference

**Server**: http://localhost:9630  
**Docs**: http://localhost:9630/docs

## Quick Start

```bash
# Start server
python3 .field/scripts/field_mcp_rest_server.py

# Test health
curl http://localhost:9630/health | jq
```

## Endpoints

### GET /health
**Check system status**
```bash
curl http://localhost:9630/health
```
Response:
```json
{
  "status": "ok",
  "sailing_intel": true,
  "nodes": {
    "obi-wan": { "symbol": "●", "port": 963, "status": "operational" },
    "tata": { "symbol": "▼", "port": 2850, "status": "operational" },
    "atlas": { "symbol": "▲", "port": 4320, "status": "operational" },
    "dojo": { "symbol": "◼︎", "port": 6390, "status": "operational" }
  }
}
```

---

### GET /documents
**List all documents**
```bash
curl "http://localhost:9630/documents?limit=10&node=atlas"
```
Query params:
- `node`: Filter by node (obi-wan, tata, atlas, dojo)
- `gate`: Filter by gate (3, 6, 9, 11)
- `limit`: Max results (default: 100)
- `offset`: Pagination offset

Response:
```json
[
  {
    "id": "sha1_hash",
    "title": "Document Title",
    "path": "/path/to/file.md",
    "node": "atlas",
    "gate": 6,
    "size": 4096,
    "mtime": 1699900000.0,
    "createdAt": "2025-11-13T10:00:00",
    "updatedAt": "2025-11-13T21:00:00"
  }
]
```

---

### GET /documents/{id}
**Get single document with content**
```bash
curl http://localhost:9630/documents/abc123...
```
Response:
```json
{
  "id": "abc123...",
  "title": "Document Title",
  "content": "# Full markdown content here...",
  "path": "/path/to/file.md",
  "node": "obi-wan",
  "gate": 3
}
```

---

### POST /documents/search
**Search documents via Sailing Intel**
```bash
curl -X POST http://localhost:9630/documents/search \
  -H "Content-Type: application/json" \
  -d '{"query": "sacred geometry", "node": "atlas", "limit": 50}'
```
Request body:
```json
{
  "query": "sacred geometry",
  "node": "atlas",  // optional
  "limit": 50       // optional, default: 50
}
```
Response:
```json
{
  "query": "sacred geometry",
  "total_matches": 47,
  "results": [
    {
      "id": "sha1_hash",
      "title": "Sacred Geometry Manifest",
      "path": "/Users/jbear/DOJO/sacred_geometry_manifest.json",
      "node": "dojo",
      "gate": 9,
      "relevance": 0.95
    }
  ]
}
```

---

### POST /documents
**Create new document**
```bash
curl -X POST http://localhost:9630/documents \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Memory",
    "content": "# Sacred memory content...",
    "node": "obi-wan",
    "gate": 3,
    "tags": ["memory", "intake"]
  }'
```
Response:
```json
{
  "id": "new_sha1_hash",
  "path": "/Users/jbear/FIELD/●OBI-WAN/INTAKE/new_memory.md",
  "status": "created"
}
```

---

### PUT /documents/{id}
**Update existing document**
```bash
curl -X PUT http://localhost:9630/documents/abc123... \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "content": "# Updated content...",
    "node": "obi-wan"
  }'
```

---

### DELETE /documents/{id}
**Delete document**
```bash
curl -X DELETE http://localhost:9630/documents/abc123...
```
Response:
```json
{
  "status": "deleted",
  "id": "abc123..."
}
```

---

### GET /nodes/{node_name}/status
**Get specific node status**
```bash
curl http://localhost:9630/nodes/atlas/status
```
Response:
```json
{
  "node": "atlas",
  "symbol": "▲",
  "port": 4320,
  "path": "/Users/jbear/FIELD/▲ATLAS",
  "exists": true,
  "file_count": 1547,
  "status": "operational"
}
```

---

## Node Names & Ports

| Node | Symbol | Port | Role |
|------|--------|------|------|
| obi-wan | ● | 963 | Observer - Memory intake |
| tata | ▼ | 2850 | Verifier - Truth validation |
| atlas | ▲ | 4320 | Architect - Model design |
| dojo | ◼︎ | 6390 | Weaver - Integration |

## Integration with Sailing Intel

The REST API automatically routes searches through **Sailing Intel** which indexes **1,068,138 files** across the FIELD system for instant search.

## Interactive API Docs

Visit **http://localhost:9630/docs** for full Swagger UI with:
- Try-it-now interface
- Complete schema documentation
- Example requests/responses

---

🔱 **The Trident Manifests Through the REST API**
