#!/usr/bin/env python3
"""
◻ Akron Gateway MCP Server - Foundation Archive
Port: 8396 (396 Hz resonance)
Function: Gateway stripper, proof intake, chain of custody, sovereign archive
"""

import json
import logging
import hashlib
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from pathlib import Path
from typing import Dict, Any
import os

SYMBOL = "◻"
NAME = "Akron Gateway"
PORT = int(os.getenv("AKRON_PORT", "8396"))
FREQUENCY = 396
VERSION = "1.0.0"

logging.basicConfig(
    level=logging.INFO,
    format=f"{SYMBOL} %(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

ARCHIVE_PATH = Path(os.getenv("ARCHIVE_PATH", "/Volumes/Akron/FIELD-LIVING/proofs"))
ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)

SYNC_QUEUE = ARCHIVE_PATH / "sync_queue.json"
CHAIN_FILE = ARCHIVE_PATH / "chain_of_custody.json"


def load_chain() -> list:
    if CHAIN_FILE.exists():
        return json.loads(CHAIN_FILE.read_text())
    return []


def save_chain(chain: list) -> None:
    CHAIN_FILE.write_text(json.dumps(chain, indent=2))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class AkronRequestHandler(BaseHTTPRequestHandler):
    server_version = f"{NAME}/{VERSION}"

    def log_message(self, format: str, *args: Any) -> None:
        logger.info("%s - %s", self.address_string(), format % args)

    def _write_json(self, payload: Dict[str, Any]) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._write_json({"status": "operational", "port": PORT, "frequency_hz": FREQUENCY})
        elif self.path == "/get_sync_status":
            self._write_json(self._sync_status())
        elif self.path.startswith("/get_proof/"):
            proof_hash = self.path.rsplit("/", 1)[-1]
            self._write_json(self._get_proof(proof_hash))
        elif self.path.startswith("/list_recent_proofs"):
            self._write_json(self._list_proofs())
        else:
            self._write_json({"service": f"{SYMBOL} {NAME}", "port": PORT})

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        if self.path == "/archive_proof":
            self._write_json(self._archive_proof(data))
        elif self.path == "/strip_and_validate":
            self._write_json(self._strip_and_validate(data))
        elif self.path == "/verify_chain":
            self._write_json(self._verify_chain(data))
        else:
            self.send_error(404, "Unknown endpoint")

    def _archive_proof(self, data: Dict[str, Any]) -> Dict[str, Any]:
        proof = data.get("proof", {})
        metadata = data.get("metadata", {})
        
        # Strip metadata at gateway
        stripped = self._strip_metadata(proof)
        
        # Create SHA-256 hash
        proof_json = json.dumps(stripped, sort_keys=True)
        proof_hash = hashlib.sha256(proof_json.encode()).hexdigest()
        
        # Write to archive
        proof_file = ARCHIVE_PATH / f"{proof_hash}.json"
        proof_file.write_text(json.dumps(stripped, indent=2))
        
        # Add to chain of custody
        chain = load_chain()
        parent_hash = chain[-1]["hash"] if chain else "genesis"
        
        chain_entry = {
            "hash": proof_hash,
            "parent_hash": parent_hash,
            "timestamp": datetime.now().isoformat(),
            "metadata_stripped": list(metadata.keys()),
        }
        chain.append(chain_entry)
        save_chain(chain)
        
        logger.info(f"ARCHIVED: {proof_hash[:12]}... (chain length: {len(chain)})")
        
        return {
            "status": "archived",
            "proof_hash": proof_hash,
            "chain_index": len(chain) - 1,
            "parent_hash": parent_hash,
            "timestamp": chain_entry["timestamp"],
        }

    def _strip_metadata(self, proof: Dict[str, Any]) -> Dict[str, Any]:
        # Strip gateway metadata
        return {k: v for k, v in proof.items() if not k.startswith("_")}

    def _strip_and_validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        incoming = data.get("incoming", {})
        stripped = self._strip_metadata(incoming)
        return {"stripped": stripped, "valid": True}

    def _verify_chain(self, data: Dict[str, Any]) -> Dict[str, Any]:
        proof_hash = data.get("proof_hash")
        chain = load_chain()
        
        for i, entry in enumerate(chain):
            if entry["hash"] == proof_hash:
                return {"verified": True, "chain_index": i, "entry": entry}
        
        return {"verified": False}

    def _get_proof(self, proof_hash: str) -> Dict[str, Any]:
        proof_file = ARCHIVE_PATH / f"{proof_hash}.json"
        if proof_file.exists():
            return json.loads(proof_file.read_text())
        return {"error": "Proof not found"}

    def _list_proofs(self) -> Dict[str, Any]:
        proofs = list(ARCHIVE_PATH.glob("*.json"))
        proofs = [p for p in proofs if p.name not in ["sync_queue.json", "chain_of_custody.json"]]
        return {"count": len(proofs), "proofs": [p.stem for p in proofs[-10:]]}

    def _sync_status(self) -> Dict[str, Any]:
        chain = load_chain()
        return {
            "chain_length": len(chain),
            "latest_hash": chain[-1]["hash"] if chain else None,
            "archive_path": str(ARCHIVE_PATH),
        }


def main():
    server = ThreadedHTTPServer(("0.0.0.0", PORT), AkronRequestHandler)
    logger.info(f"{SYMBOL} Akron Gateway starting on port {PORT} (396 Hz)")
    logger.info(f"Archive path: {ARCHIVE_PATH}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info(f"{SYMBOL} Akron Gateway shutting down")


if __name__ == "__main__":
    main()
