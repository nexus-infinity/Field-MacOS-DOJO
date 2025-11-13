#!/usr/bin/env python3
"""
🔱 FIELD MCP REST API Server
Exposes FIELD nodes via REST endpoints with Sailing Intel integration
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from pathlib import Path
from datetime import datetime
import sqlite3
import hashlib
import json
import uvicorn

# Initialize FastAPI
app = FastAPI(
    title="FIELD MCP Server",
    description="Sacred geometry-aligned document management system",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
HOME = Path.home()
SAILING_DB = HOME / "FIELD-DEV" / "sailing_intel" / "sailing_index.sqlite3"
FIELD_ROOT = HOME / "FIELD"

# Node mapping
NODES = {
    "obi-wan": {"symbol": "●", "port": 963, "path": FIELD_ROOT / "●OBI-WAN"},
    "tata": {"symbol": "▼", "port": 2850, "path": FIELD_ROOT / "▼TATA"},
    "atlas": {"symbol": "▲", "port": 4320, "path": FIELD_ROOT / "▲ATLAS"},
    "dojo": {"symbol": "◼︎", "port": 6390, "path": FIELD_ROOT / "◼︎DOJO_SOVEREIGN"}
}

# Pydantic models
class DocumentCreate(BaseModel):
    title: str
    content: str
    node: str = "obi-wan"
    gate: Optional[int] = 3
    tags: Optional[List[str]] = []
    metadata: Optional[Dict[str, Any]] = {}

class Document(BaseModel):
    id: str
    title: str
    content: Optional[str] = None
    path: str
    node: str
    gate: Optional[int] = None
    size: int
    mtime: float
    sha1: str
    tags: Optional[List[str]] = []
    metadata: Optional[Dict[str, Any]] = {}
    createdAt: str
    updatedAt: str

class SearchQuery(BaseModel):
    query: str
    node: Optional[str] = None
    limit: Optional[int] = 50

# Helper functions
def get_sailing_connection():
    """Connect to Sailing Intel database"""
    if not SAILING_DB.exists():
        raise HTTPException(status_code=503, detail="Sailing Intel database not found")
    return sqlite3.connect(SAILING_DB)

def calculate_sha1(content: str) -> str:
    """Calculate SHA1 hash of content"""
    return hashlib.sha1(content.encode()).hexdigest()

def file_to_document(file_path: Path, include_content: bool = False) -> Document:
    """Convert file to Document object"""
    stat = file_path.stat()
    
    # Determine node from path
    node = "unknown"
    for node_name, node_info in NODES.items():
        if str(node_info["path"]) in str(file_path):
            node = node_name
            break
    
    # Read content if requested
    content = None
    if include_content and file_path.suffix in ['.md', '.txt', '.json']:
        try:
            content = file_path.read_text()
        except:
            content = None
    
    # Calculate SHA1 from content or file
    if content:
        sha1 = calculate_sha1(content)
    else:
        sha1 = hashlib.sha1(str(file_path).encode()).hexdigest()
    
    return Document(
        id=sha1,
        title=file_path.stem,
        content=content,
        path=str(file_path),
        node=node,
        gate=None,
        size=stat.st_size,
        mtime=stat.st_mtime,
        sha1=sha1,
        tags=[],
        metadata={},
        createdAt=datetime.fromtimestamp(stat.st_ctime).isoformat(),
        updatedAt=datetime.fromtimestamp(stat.st_mtime).isoformat()
    )

# API Endpoints

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    node_status = {}
    for node_name, node_info in NODES.items():
        node_status[node_name] = {
            "symbol": node_info["symbol"],
            "port": node_info["port"],
            "exists": node_info["path"].exists(),
            "status": "operational" if node_info["path"].exists() else "offline"
        }
    
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "sailing_intel": SAILING_DB.exists(),
        "nodes": node_status
    }

@app.get("/documents", response_model=List[Document])
async def list_documents(
    node: Optional[str] = Query(None, description="Filter by node"),
    gate: Optional[int] = Query(None, description="Filter by gate"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0)
):
    """List all documents with optional filtering"""
    
    # Query Sailing Intel database
    conn = get_sailing_connection()
    cursor = conn.cursor()
    
    # Build query
    query = "SELECT path, name, size, mtime FROM files"
    params = []
    
    if node and node in NODES:
        node_path = str(NODES[node]["path"])
        query += " WHERE path LIKE ?"
        params.append(f"{node_path}%")
    
    query += f" LIMIT {limit} OFFSET {offset}"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to Document objects
    documents = []
    for path_str, name, size, mtime in rows:
        try:
            file_path = Path(path_str)
            if file_path.exists():
                doc = file_to_document(file_path, include_content=False)
                if gate is None or doc.gate == gate:
                    documents.append(doc)
        except Exception as e:
            continue
    
    return documents

@app.get("/documents/{doc_id}", response_model=Document)
async def get_document(doc_id: str):
    """Get single document by ID (SHA1 hash)"""
    
    # Search Sailing Intel for file
    conn = get_sailing_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM files WHERE sha1 = ?", (doc_id,))
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="Document not found")
    
    file_path = Path(result[0])
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document file not found")
    
    return file_to_document(file_path, include_content=True)

@app.post("/documents/search")
async def search_documents(search: SearchQuery):
    """Search documents using Sailing Intel"""
    
    conn = get_sailing_connection()
    cursor = conn.cursor()
    
    # Build search query
    query = """
        SELECT path, name, size, mtime 
        FROM files 
        WHERE name LIKE ? OR path LIKE ?
    """
    params = [f"%{search.query}%", f"%{search.query}%"]
    
    if search.node and search.node in NODES:
        node_path = str(NODES[search.node]["path"])
        query += " AND path LIKE ?"
        params.append(f"{node_path}%")
    
    query += f" LIMIT {search.limit}"
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to results
    results = []
    for path_str, name, size, mtime in rows:
        try:
            file_path = Path(path_str)
            if file_path.exists():
                doc = file_to_document(file_path, include_content=False)
                results.append({
                    "id": doc.id,
                    "title": doc.title,
                    "path": doc.path,
                    "node": doc.node,
                    "gate": doc.gate,
                    "relevance": 0.85  # Placeholder relevance score
                })
        except Exception:
            continue
    
    return {
        "query": search.query,
        "total_matches": len(results),
        "results": results
    }

@app.post("/documents", response_model=Document)
async def create_document(doc: DocumentCreate):
    """Create new document"""
    
    if doc.node not in NODES:
        raise HTTPException(status_code=400, detail=f"Invalid node: {doc.node}")
    
    node_path = NODES[doc.node]["path"]
    if not node_path.exists():
        raise HTTPException(status_code=503, detail=f"Node path does not exist: {node_path}")
    
    # Create file
    filename = doc.title.replace(" ", "_").lower() + ".md"
    file_path = node_path / "INTAKE" / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write content
    file_path.write_text(doc.content)
    
    # Return created document
    return file_to_document(file_path, include_content=True)

@app.put("/documents/{doc_id}", response_model=Document)
async def update_document(doc_id: str, doc: DocumentCreate):
    """Update existing document"""
    
    # Find document
    conn = get_sailing_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM files WHERE sha1 = ?", (doc_id,))
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="Document not found")
    
    file_path = Path(result[0])
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Document file not found")
    
    # Update content
    file_path.write_text(doc.content)
    
    return file_to_document(file_path, include_content=True)

@app.delete("/documents/{doc_id}")
async def delete_document(doc_id: str):
    """Delete document"""
    
    # Find document
    conn = get_sailing_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT path FROM files WHERE sha1 = ?", (doc_id,))
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="Document not found")
    
    file_path = Path(result[0])
    if file_path.exists():
        file_path.unlink()
    
    return {"status": "deleted", "id": doc_id}

@app.get("/nodes/{node_name}/status")
async def node_status(node_name: str):
    """Get status of specific node"""
    
    if node_name not in NODES:
        raise HTTPException(status_code=404, detail="Node not found")
    
    node_info = NODES[node_name]
    node_path = node_info["path"]
    
    # Count files in node
    file_count = 0
    if node_path.exists():
        file_count = sum(1 for _ in node_path.rglob("*") if _.is_file())
    
    return {
        "node": node_name,
        "symbol": node_info["symbol"],
        "port": node_info["port"],
        "path": str(node_path),
        "exists": node_path.exists(),
        "file_count": file_count,
        "status": "operational" if node_path.exists() else "offline"
    }

if __name__ == "__main__":
    print("🔱 Starting FIELD MCP REST Server...")
    print(f"📡 Sailing Intel: {SAILING_DB.exists()}")
    print(f"🏛️  FIELD Nodes:")
    for node_name, node_info in NODES.items():
        status = "✅" if node_info["path"].exists() else "❌"
        print(f"   {status} {node_info['symbol']} {node_name.upper()} (port {node_info['port']})")
    print()
    print("🌐 Server starting on http://localhost:9630")
    print("📚 Docs available at http://localhost:9630/docs")
    
    uvicorn.run(app, host="0.0.0.0", port=9630, log_level="info")
