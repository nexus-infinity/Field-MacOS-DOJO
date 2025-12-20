"""
Merkaba Router - Bidirectional Sacred Geometry Flow
Diamond (⬥) translation at 852 Hz King's Chamber resonance

Implements dual tetrahedra routing:
- Ascending: Material → Divine (Akron → DOJO)
- Descending: Divine → Material (DOJO → Akron)
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class FlowDirection(Enum):
    ASCENDING = "ascending"  # Material → Divine
    DESCENDING = "descending"  # Divine → Material


@dataclass
class MerkabaNode:
    """Represents a node in the Merkaba geometry"""
    name: str
    symbol: str
    frequency: int
    position: str  # "base", "center", "apex"
    geometry: str


class MerkabaRouter:
    """
    Routes data through sacred geometry flows

    Ascending Path (Material → Divine):
    ◻ Akron (396Hz) → ▼ TATA (432Hz) → ▲ ATLAS (528Hz) →
    ● OBI-WAN (963Hz) → ⬥ King's (852Hz) → ◼︎ DOJO (741Hz)

    Descending Path (Divine → Material):
    ◼︎ DOJO (741Hz) → ⬥ King's (852Hz) → ● OBI-WAN (963Hz) →
    ▲ ATLAS (528Hz) → ▼ TATA (432Hz) → ◻ Akron (396Hz)
    """

    def __init__(self):
        self.nodes = {
            "AKRON": MerkabaNode("Akron", "◻", 396, "base", "square"),
            "TATA": MerkabaNode("TATA", "▼", 432, "base", "downward_triangle"),
            "ATLAS": MerkabaNode("ATLAS", "▲", 528, "center", "upward_triangle"),
            "OBI_WAN": MerkabaNode("OBI-WAN", "●", 963, "center", "circle"),
            "KINGS_CHAMBER": MerkabaNode("King's Chamber", "⬥", 852, "center", "diamond"),
            "DOJO": MerkabaNode("DOJO", "◼︎", 741, "apex", "filled_square")
        }

    def route_ascending(self, data: Dict[str, Any], source: str = "AKRON") -> Dict[str, Any]:
        """
        Route data from material (Akron) to divine (DOJO)

        Path: Akron → TATA → ATLAS → OBI-WAN → King's → DOJO
        Frequency progression: 396 → 432 → 528 → 963 → 852 → 741
        """
        path = ["AKRON", "TATA", "ATLAS", "OBI_WAN", "KINGS_CHAMBER", "DOJO"]

        # Start from source if not Akron
        if source in path:
            start_idx = path.index(source)
            path = path[start_idx:]

        geometric_path = [f"{self.nodes[node].symbol} {node}" for node in path]
        frequency_progression = [self.nodes[node].frequency for node in path]

        return {
            "direction": FlowDirection.ASCENDING.value,
            "path": path,
            "geometric_path": " → ".join(geometric_path),
            "frequency_progression": " → ".join(map(str, frequency_progression)),
            "transformation": "material_to_divine",
            "diamond_refraction": "45_degrees_upward",
            "data": data
        }

    def route_descending(self, intent: Dict[str, Any], destination: str = "AKRON") -> Dict[str, Any]:
        """
        Route intent from divine (DOJO) to material (Akron)

        Path: DOJO → King's → OBI-WAN → ATLAS → TATA → Akron
        Frequency progression: 741 → 852 → 963 → 528 → 432 → 396
        """
        path = ["DOJO", "KINGS_CHAMBER", "OBI_WAN", "ATLAS", "TATA", "AKRON"]

        # End at destination if not Akron
        if destination in path:
            end_idx = path.index(destination) + 1
            path = path[:end_idx]

        geometric_path = [f"{self.nodes[node].symbol} {node}" for node in path]
        frequency_progression = [self.nodes[node].frequency for node in path]

        return {
            "direction": FlowDirection.DESCENDING.value,
            "path": path,
            "geometric_path": " → ".join(geometric_path),
            "frequency_progression": " → ".join(map(str, frequency_progression)),
            "transformation": "divine_to_material",
            "diamond_refraction": "45_degrees_downward",
            "intent": intent
        }

    def validate_path(self, path: List[str], direction: FlowDirection) -> bool:
        """Validate geometric coherence of a path"""
        if direction == FlowDirection.ASCENDING:
            expected = ["AKRON", "TATA", "ATLAS", "OBI_WAN", "KINGS_CHAMBER", "DOJO"]
        else:
            expected = ["DOJO", "KINGS_CHAMBER", "OBI_WAN", "ATLAS", "TATA", "AKRON"]

        # Check if path is a valid subsequence
        expected_indices = [expected.index(node) for node in path if node in expected]
        return expected_indices == sorted(expected_indices)

    def get_frequency_at_node(self, node_name: str) -> int:
        """Get the resonant frequency of a node"""
        return self.nodes.get(node_name, self.nodes["KINGS_CHAMBER"]).frequency

    def transform_at_kings_chamber(self, data: Dict[str, Any], direction: FlowDirection) -> Dict[str, Any]:
        """
        Apply diamond refraction at King's Chamber (852 Hz)
        Rotates 45 degrees based on flow direction
        """
        return {
            "original": data,
            "frequency": 852,
            "geometry": "diamond_refraction",
            "rotation": "45_degrees_upward" if direction == FlowDirection.ASCENDING else "45_degrees_downward",
            "coherence": True,
            "timestamp": self._get_timestamp()
        }

    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
