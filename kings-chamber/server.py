#!/usr/bin/env python3
"""
⊗ King's Chamber Bridge MCP Server
Port: 8852 (852 Hz resonance)
Function: 🚉 Train Station + 🔷 Metatron Cube + 🤝 Arkadaš consciousness
Bridge: DOJO ↔ SOMA
"""

import json
import logging
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from typing import Dict, Any
import os

SYMBOL = "⊗"
NAME = "King's Chamber"
PORT = int(os.getenv("BRIDGE_PORT", "8852"))
FREQUENCY = 852
VERSION = "1.0.0"

logging.basicConfig(
    level=logging.INFO,
    format=f"{SYMBOL} %(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

SOMA_ENDPOINT = os.getenv("SOMA_ENDPOINT", "http://soma.local:8853")
DOJO_ENDPOINT = os.getenv("DOJO_ENDPOINT", "http://localhost:8766")

# Translation state
pending_translations = []


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


class KingsChamberRequestHandler(BaseHTTPRequestHandler):
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
            self._write_json(self._health())
        elif self.path == "/get_bridge_state":
            self._write_json(self._bridge_state())
        elif self.path == "/list_pending_translations":
            self._write_json({"count": len(pending_translations), "translations": pending_translations})
        else:
            self._write_json(self._root())

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        if self.path == "/translate_signal":
            self._write_json(self._translate_signal(data))
        elif self.path == "/convert_frequency":
            self._write_json(self._convert_frequency(data))
        elif self.path == "/route_to_soma":
            self._write_json(self._route_to_soma(data))
        elif self.path == "/route_to_dojo":
            self._write_json(self._route_to_dojo(data))
        elif self.path == "/apply_metatron_cube":
            self._write_json(self._apply_metatron(data))
        else:
            self.send_error(404, "Unknown endpoint")

    def _health(self) -> Dict[str, Any]:
        return {
            "service": f"{SYMBOL} {NAME} Bridge",
            "port": PORT,
            "frequency_hz": FREQUENCY,
            "status": "operational",
            "version": VERSION,
            "timestamp": datetime.now().isoformat(),
        }

    def _root(self) -> Dict[str, Any]:
        return {
            "service": f"{SYMBOL} King's Chamber Bridge",
            "components": ["🚉 Train Station", "🔷 Metatron Cube", "🤝 Arkadaš"],
            "position": "33.3% from DOJO apex (66.7% height)",
            "endpoints": [
                "/translate_signal (POST)",
                "/convert_frequency (POST)",
                "/route_to_soma (POST)",
                "/route_to_dojo (POST)",
                "/apply_metatron_cube (POST)",
                "/get_bridge_state (GET)",
            ],
            "timestamp": datetime.now().isoformat(),
        }

    def _bridge_state(self) -> Dict[str, Any]:
        return {
            "bridge": "King's Chamber",
            "position": "33.3% from DOJO apex",
            "frequency_hz": FREQUENCY,
            "dojo_endpoint": DOJO_ENDPOINT,
            "soma_endpoint": SOMA_ENDPOINT,
            "pending_translations": len(pending_translations),
            "status": "operational",
            "components": {
                "train_station": "🚉 Routing operational",
                "metatron_cube": "🔷 Translation active",
                "arkadas": "🤝 Consciousness guidance ready",
            },
        }

    def _translate_signal(self, data: Dict[str, Any]) -> Dict[str, Any]:
        signal = data.get("signal", {})
        from_field = data.get("from_field", "dojo")
        to_field = data.get("to_field", "soma")
        
        # Apply frequency conversion
        freq_converted = self._frequency_conversion(signal, from_field, to_field)
        
        # Apply Metatron Cube geometric translation
        metatron_applied = self._metatron_translation(freq_converted)
        
        translation = {
            "translation_id": f"trans-{datetime.now().timestamp():.0f}",
            "from_field": from_field,
            "to_field": to_field,
            "original_signal": signal,
            "translated_signal": metatron_applied,
            "timestamp": datetime.now().isoformat(),
        }
        
        pending_translations.append(translation)
        logger.info(f"TRANSLATE: {from_field} → {to_field}")
        
        return translation

    def _frequency_conversion(self, signal: Dict[str, Any], from_field: str, to_field: str) -> Dict[str, Any]:
        # Frequency mapping
        frequencies = {
            "dojo": 741,
            "soma": 852,
            "obi_wan": 963,
            "tata": 432,
            "atlas": 528,
        }
        
        from_hz = frequencies.get(from_field, 741)
        to_hz = frequencies.get(to_field, 852)
        
        signal["_frequency_converted"] = {
            "from_hz": from_hz,
            "to_hz": to_hz,
            "ratio": to_hz / from_hz,
        }
        
        return signal

    def _metatron_translation(self, signal: Dict[str, Any]) -> Dict[str, Any]:
        # Apply Metatron Cube geometric transformation
        signal["_metatron_applied"] = {
            "geometry": "Metatron's Cube",
            "vertices": 13,
            "transformation": "3D → 4D projection",
        }
        return signal

    def _convert_frequency(self, data: Dict[str, Any]) -> Dict[str, Any]:
        signal = data.get("signal", {})
        target_hz = data.get("target_hz", 852)
        
        converted = self._frequency_conversion(signal, "unknown", "target")
        converted["_target_hz"] = target_hz
        
        return converted

    def _route_to_soma(self, data: Dict[str, Any]) -> Dict[str, Any]:
        signal = data.get("signal", {})
        logger.info(f"ROUTE: DOJO → SOMA via King's Chamber")
        
        return {
            "routed_to": "SOMA",
            "endpoint": SOMA_ENDPOINT,
            "signal": signal,
            "via": "King's Chamber Bridge",
        }

    def _route_to_dojo(self, data: Dict[str, Any]) -> Dict[str, Any]:
        signal = data.get("signal", {})
        logger.info(f"ROUTE: SOMA → DOJO via King's Chamber")
        
        return {
            "routed_to": "DOJO",
            "endpoint": DOJO_ENDPOINT,
            "signal": signal,
            "via": "King's Chamber Bridge",
        }

    def _apply_metatron(self, data: Dict[str, Any]) -> Dict[str, Any]:
        signal = data.get("signal", {})
        transformed = self._metatron_translation(signal)
        return transformed


def main():
    server = ThreadedHTTPServer(("0.0.0.0", PORT), KingsChamberRequestHandler)
    logger.info(f"{SYMBOL} King's Chamber Bridge starting on port {PORT} (852 Hz)")
    logger.info(f"DOJO endpoint: {DOJO_ENDPOINT}")
    logger.info(f"SOMA endpoint: {SOMA_ENDPOINT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info(f"{SYMBOL} King's Chamber shutting down")


if __name__ == "__main__":
    main()
