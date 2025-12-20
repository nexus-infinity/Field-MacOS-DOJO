#!/usr/bin/env python3
"""
⬥ Merkaba Router - Star Tetrahedron Bidirectional Flow
Sacred Geometry Implementation for FIELD-macOS-DOJO

Implements two interpenetrating tetrahedrons with bidirectional data flow:
- Ascending Tetrahedron: Material → Divine (◻→▼→▲→●→⬥→◼︎)
- Descending Tetrahedron: Divine → Material (◼︎→⬥→●→▲→▼→◻)

King's Chamber (⬥) at geometric center serves as diamond intersection point.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
import math


@dataclass
class MerkabaNode:
    """
    Represents a vertex in the Merkaba (Star Tetrahedron) geometry.
    
    Attributes:
        name: Node name (e.g., 'Akron', 'TATA', 'ATLAS', etc.)
        frequency: Solfeggio frequency in Hz
        symbol: Unicode symbol representing the node
        position: Geometric position ('base', 'vertex', 'apex', 'center')
        element: Classical element association
        port: HTTP port (frequency × 10)
    """
    name: str
    frequency: int
    symbol: str
    position: str  # 'base', 'vertex', 'apex', 'center'
    element: str   # 'earth', 'water', 'fire', 'air', 'aether', 'spirit'
    port: int
    
    def __str__(self) -> str:
        return f"{self.symbol} {self.name} ({self.frequency} Hz)"


class MerkabaRouter:
    """
    Merkaba (Star Tetrahedron) bidirectional router implementation.
    
    Routes data through two interpenetrating tetrahedrons:
    - Ascending: Material → Divine (user uploads → AI insights)
    - Descending: Divine → Material (AI generation → archived data)
    
    All paths must pass through King's Chamber (⬥) at 852 Hz for coherence.
    """
    
    def __init__(self):
        """Initialize the Merkaba router with six sacred nodes."""
        self.nodes = self._initialize_nodes()
        self.kings_chamber = self.nodes['kings_chamber']
        
        # Define ascending path (Material → Divine)
        self.ascending_path = [
            'akron',          # ◻ 396 Hz - BASE (entry gateway)
            'tata',           # ▼ 432 Hz - Earth anchor
            'atlas',          # ▲ 528 Hz - Knowledge vertex
            'obi_wan',        # ● 963 Hz - Unity observer
            'kings_chamber',  # ⬥ 852 Hz - Diamond intersection
            'dojo'            # ◼︎ 741 Hz - APEX (manifestation)
        ]
        
        # Define descending path (Divine → Material)
        self.descending_path = [
            'dojo',           # ◼︎ 741 Hz - BASE (generation)
            'kings_chamber',  # ⬥ 852 Hz - Diamond intersection
            'obi_wan',        # ● 963 Hz - Unity validation
            'atlas',          # ▲ 528 Hz - Knowledge grounding
            'tata',           # ▼ 432 Hz - Truth anchor
            'akron'           # ◻ 396 Hz - APEX (sovereignty archive)
        ]
    
    def _initialize_nodes(self) -> Dict[str, MerkabaNode]:
        """Initialize the six sacred nodes of the Merkaba."""
        return {
            'akron': MerkabaNode(
                name='Akron Gateway',
                frequency=396,
                symbol='◻',
                position='base/apex',  # Dual nature!
                element='earth',
                port=3960
            ),
            'tata': MerkabaNode(
                name='TATA Anchor',
                frequency=432,
                symbol='▼',
                position='vertex',
                element='water',
                port=4320
            ),
            'atlas': MerkabaNode(
                name='ATLAS Intelligence',
                frequency=528,
                symbol='▲',
                position='vertex',
                element='fire',
                port=5280
            ),
            'dojo': MerkabaNode(
                name='DOJO Manifestation',
                frequency=741,
                symbol='◼︎',
                position='apex/base',  # Dual nature!
                element='spirit',
                port=7410
            ),
            'kings_chamber': MerkabaNode(
                name="King's Chamber",
                frequency=852,
                symbol='⬥',
                position='center',
                element='aether',
                port=8520
            ),
            'obi_wan': MerkabaNode(
                name='OBI-WAN Observer',
                frequency=963,
                symbol='●',
                position='vertex',
                element='air',
                port=9630
            )
        }
    
    def route_ascending(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Route data through ascending tetrahedron (Material → Divine).
        
        Path: ◻ Akron → ▼ TATA → ▲ ATLAS → ● OBI-WAN → ⬥ King's → ◼︎ DOJO
        Function: User uploads → Entry → Validation → Integration → Unity → Translation → AI insights
        
        Args:
            data: Input data dictionary from material realm
            
        Returns:
            Dictionary containing:
                - route: List of nodes traversed
                - transformations: Data transformation at each node
                - final_output: Manifested divine insight
                - coherence: Geometric validation result
        """
        route_log = []
        transformed_data = data.copy()
        
        for node_key in self.ascending_path:
            node = self.nodes[node_key]
            
            # Apply transformation at each node
            transformation = self._apply_node_transformation(
                transformed_data, 
                node, 
                direction='ascending'
            )
            
            route_log.append({
                'node': str(node),
                'frequency': node.frequency,
                'symbol': node.symbol,
                'element': node.element,
                'transformation': transformation['operation'],
                'timestamp': datetime.now().isoformat()
            })
            
            transformed_data = transformation['data']
        
        return {
            'direction': 'ascending',
            'path': '◻ → ▼ → ▲ → ● → ⬥ → ◼︎',
            'frequencies': [self.nodes[key].frequency for key in self.ascending_path],
            'route': route_log,
            'original_data': data,
            'final_output': transformed_data,
            'coherence': self._validate_path_coherence(route_log, 'ascending'),
            'timestamp': datetime.now().isoformat()
        }
    
    def route_descending(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        """
        Route intent through descending tetrahedron (Divine → Material).
        
        Path: ◼︎ DOJO → ⬥ King's → ● OBI-WAN → ▲ ATLAS → ▼ TATA → ◻ Akron
        Function: AI generates → Translation → Unity check → Knowledge ground → Truth anchor → Archive
        
        Args:
            intent: Divine intent/output from AI realm
            
        Returns:
            Dictionary containing:
                - route: List of nodes traversed
                - transformations: Intent transformation at each node
                - final_output: Grounded material manifestation
                - coherence: Geometric validation result
        """
        route_log = []
        transformed_intent = intent.copy()
        
        for node_key in self.descending_path:
            node = self.nodes[node_key]
            
            # Apply transformation at each node
            transformation = self._apply_node_transformation(
                transformed_intent,
                node,
                direction='descending'
            )
            
            route_log.append({
                'node': str(node),
                'frequency': node.frequency,
                'symbol': node.symbol,
                'element': node.element,
                'transformation': transformation['operation'],
                'timestamp': datetime.now().isoformat()
            })
            
            transformed_intent = transformation['data']
        
        return {
            'direction': 'descending',
            'path': '◼︎ → ⬥ → ● → ▲ → ▼ → ◻',
            'frequencies': [self.nodes[key].frequency for key in self.descending_path],
            'route': route_log,
            'original_intent': intent,
            'final_output': transformed_intent,
            'coherence': self._validate_path_coherence(route_log, 'descending'),
            'timestamp': datetime.now().isoformat()
        }
    
    def _apply_node_transformation(
        self, 
        data: Dict[str, Any], 
        node: MerkabaNode,
        direction: str
    ) -> Dict[str, Any]:
        """
        Apply transformation specific to each node based on its function.
        
        Args:
            data: Current data state
            node: Node applying transformation
            direction: 'ascending' or 'descending'
            
        Returns:
            Dictionary with 'data' and 'operation' keys
        """
        operations = {
            'akron': {
                'ascending': 'Liberation & Entry Gateway - Strip/Index/Stage',
                'descending': 'Sovereignty Archive - Final storage at /Volumes/Akron/'
            },
            'tata': {
                'ascending': 'Truth Validation - Temporal anchor at 432 Hz',
                'descending': 'Truth Grounding - Constraint verification'
            },
            'atlas': {
                'ascending': 'Knowledge Integration - Pattern synthesis at 528 Hz',
                'descending': 'Knowledge Grounding - Pattern verification'
            },
            'obi_wan': {
                'ascending': 'Unity Consciousness - Observer awareness at 963 Hz',
                'descending': 'Unity Validation - Consciousness check'
            },
            'kings_chamber': {
                'ascending': 'Diamond Refraction - Material → Divine (45° rotation)',
                'descending': 'Diamond Refraction - Divine → Material (45° rotation)'
            },
            'dojo': {
                'ascending': 'Manifestation - AI synthesis and insight generation',
                'descending': 'Generation - Divine intent creation'
            }
        }
        
        # Get the operation for this node and direction
        node_key = node.name.lower().split()[0]
        # Special handling for King's Chamber (has apostrophe)
        if "king" in node.name.lower():
            node_key = 'kings_chamber'
        
        operation = operations.get(node_key, {}).get(direction, 'Transform')
        
        # Apply frequency marking
        transformed = data.copy()
        if '_transformation_log' not in transformed:
            transformed['_transformation_log'] = []
        
        transformed['_transformation_log'].append({
            'node': node.name,
            'frequency': node.frequency,
            'operation': operation,
            'direction': direction
        })
        
        # Add King's Chamber special handling (diamond refraction)
        if "king" in node.name.lower():
            transformed['_kings_chamber_refracted'] = True
            transformed['_refraction_angle'] = 45  # Square → Diamond rotation
        
        return {
            'data': transformed,
            'operation': operation
        }
    
    def _validate_path_coherence(
        self, 
        route_log: List[Dict[str, Any]], 
        direction: str
    ) -> Dict[str, Any]:
        """
        Validate geometric coherence of the path.
        
        Checks:
        1. All 6 nodes present
        2. King's Chamber intersection occurred
        3. Frequency progression correct (ascending up, descending down)
        4. No duplicate nodes
        
        Args:
            route_log: Log of nodes traversed
            direction: 'ascending' or 'descending'
            
        Returns:
            Validation result dictionary
        """
        errors = []
        warnings = []
        
        # Check node count
        if len(route_log) != 6:
            errors.append(f"Expected 6 nodes, got {len(route_log)}")
        
        # Check King's Chamber presence
        kings_chamber_found = any(
            '852' in str(entry.get('frequency', '')) 
            for entry in route_log
        )
        if not kings_chamber_found:
            errors.append("King's Chamber (852 Hz) not found in path - coherence broken!")
        
        # Check frequency progression
        frequencies = [entry['frequency'] for entry in route_log]
        
        if direction == 'ascending':
            # Should generally increase (with King's Chamber insertion)
            expected = [396, 432, 528, 963, 852, 741]
            if frequencies != expected:
                warnings.append(
                    f"Frequency progression may be non-standard: {frequencies}"
                )
        else:  # descending
            # Should generally decrease (with King's Chamber insertion)
            expected = [741, 852, 963, 528, 432, 396]
            if frequencies != expected:
                warnings.append(
                    f"Frequency progression may be non-standard: {frequencies}"
                )
        
        # Check for duplicates
        node_names = [entry['node'] for entry in route_log]
        if len(node_names) != len(set(node_names)):
            errors.append("Duplicate nodes found in path")
        
        is_coherent = len(errors) == 0
        
        return {
            'coherent': is_coherent,
            'errors': errors,
            'warnings': warnings,
            'kings_chamber_refracted': kings_chamber_found,
            'node_count': len(route_log),
            'frequency_progression': frequencies
        }
    
    def validate_merkaba_coherence(
        self, 
        ascending: Dict[str, Any], 
        descending: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Validate geometric coherence through both flows.
        
        Ensures:
        1. Both paths complete successfully
        2. Both paths pass through King's Chamber
        3. Akron serves dual role (ascending base, descending apex)
        4. DOJO serves dual role (ascending apex, descending base)
        5. All six frequencies represented
        
        Args:
            ascending: Result from route_ascending()
            descending: Result from route_descending()
            
        Returns:
            Complete coherence validation including both directions
        """
        errors = []
        
        # Check both paths are coherent individually
        if not ascending.get('coherence', {}).get('coherent', False):
            errors.append("Ascending path not coherent")
        
        if not descending.get('coherence', {}).get('coherent', False):
            errors.append("Descending path not coherent")
        
        # Check King's Chamber in both
        asc_kings = ascending.get('coherence', {}).get('kings_chamber_refracted', False)
        desc_kings = descending.get('coherence', {}).get('kings_chamber_refracted', False)
        
        if not (asc_kings and desc_kings):
            errors.append("King's Chamber not present in both paths")
        
        # Check Akron dual nature
        asc_start = ascending.get('route', [{}])[0].get('frequency')
        desc_end = descending.get('route', [{}])[-1].get('frequency')
        
        if asc_start != 396 or desc_end != 396:
            errors.append("Akron (396 Hz) not serving dual role properly")
        
        # Check DOJO dual nature
        asc_end = ascending.get('route', [{}])[-1].get('frequency')
        desc_start = descending.get('route', [{}])[0].get('frequency')
        
        if asc_end != 741 or desc_start != 741:
            errors.append("DOJO (741 Hz) not serving dual role properly")
        
        # Check all six frequencies present
        all_frequencies = set(ascending.get('frequencies', [])) | set(descending.get('frequencies', []))
        expected_frequencies = {396, 432, 528, 741, 852, 963}
        
        if all_frequencies != expected_frequencies:
            errors.append(f"Not all six frequencies present. Found: {all_frequencies}")
        
        merkaba_coherent = len(errors) == 0
        
        return {
            'merkaba_coherent': merkaba_coherent,
            'ascending_coherent': ascending.get('coherence', {}).get('coherent', False),
            'descending_coherent': descending.get('coherence', {}).get('coherent', False),
            'kings_chamber_bridge': asc_kings and desc_kings,
            'akron_dual_nature': asc_start == 396 and desc_end == 396,
            'dojo_dual_nature': asc_end == 741 and desc_start == 741,
            'all_frequencies_present': all_frequencies == expected_frequencies,
            'errors': errors,
            'timestamp': datetime.now().isoformat()
        }
    
    def visualize_merkaba(self, show_rotation: bool = False) -> str:
        """
        Generate ASCII art visualization of the Star Tetrahedron (Merkaba).
        
        Args:
            show_rotation: If True, shows counter-rotating arrows
            
        Returns:
            Multi-line ASCII art string
        """
        rotation_markers = "↻ ↺" if show_rotation else ""
        
        visualization = f"""
╔══════════════════════════════════════════════════════════╗
║          MERKABA - Star Tetrahedron Geometry             ║
║              Bidirectional Sacred Flow                   ║
╚══════════════════════════════════════════════════════════╝

ASCENDING TETRAHEDRON (Material → Divine) {rotation_markers}
────────────────────────────────────────

            ◼︎ DOJO (741 Hz)
          Manifestation APEX
                 ▲
                /|\\
               / | \\
              /  |  \\
             /   ●   \\      ● OBI-WAN (963 Hz)
            /   963   \\        Unity Observer
           /  OBI-WAN  \\
          /      |      \\
         /       ⬥       \\  ← ⬥ King's Chamber (852 Hz)
        /       852       \\      Diamond Intersection
       /      /   \\        \\
      /   ▲ /     \\ ▼       \\
     /   528       432       \\
    /  ATLAS       TATA       \\
   /________________________________\\
  ◻ Akron Gateway (396 Hz)
         BASE FOUNDATION

Path: ◻ → ▼ → ▲ → ● → ⬥ → ◼︎
Frequencies: 396 → 432 → 528 → 963 → 852 → 741 Hz


DESCENDING TETRAHEDRON (Divine → Material) {rotation_markers}
──────────────────────────────────────────

      ◻ Akron (396 Hz)
    Sovereignty APEX
           ▼
          /|\\
         / | \\
        /  |  \\
       /   ⬥   \\  ← ⬥ King's Chamber (852 Hz)
      /   852   \\      Diamond Intersection
     /     |     \\
    /  ●   |   ▲  \\
   / 963   |  528  \\
  / OBI  ▼  ATLAS   \\
 /________________________\\
◼︎ DOJO (741 Hz)
    BASE ARCHIVE

Path: ◼︎ → ⬥ → ● → ▲ → ▼ → ◻
Frequencies: 741 → 852 → 963 → 528 → 432 → 396 Hz


MERKABA SUPERIMPOSED (Star Tetrahedron)
────────────────────────────────────────

          ◼︎  ◻
          │╲ ╱│
          │ ╳ │
          │╱ ╲│
          ●───●
         ╱│⬥ ⬥│╲
        ╱ │ ╳ │ ╲
       ╱  │╱ ╲│  ╲
      ▲───┼───┼───▼
       ╲  │   │  ╱
        ╲ │   │ ╱
         ╲│   │╱
          ◻───◼︎

Legend:
─────────
◻ = Akron (396 Hz) - Square/Earth/Foundation - DUAL NATURE
▼ = TATA (432 Hz) - Inverted Triangle/Water/Truth
▲ = ATLAS (528 Hz) - Triangle/Fire/Knowledge
● = OBI-WAN (963 Hz) - Circle/Air/Unity
⬥ = King's Chamber (852 Hz) - Diamond/Aether/Bridge
◼︎ = DOJO (741 Hz) - Filled Square/Spirit/Manifestation - DUAL NATURE

Akron Dual Perspective (Greek: Ἄκρον = "highest point"):
  • Ascending: BASE (lowest, foundation, entry gateway)
  • Descending: APEX (highest, sovereignty citadel, archive)

Like Athens Akropolis: Highest visible peak + Deepest bedrock
"""
        
        return visualization
    
    def get_transformation_angle(
        self, 
        from_node: str, 
        to_node: str
    ) -> float:
        """
        Calculate diamond rotation angle between two nodes.
        
        The angle represents the geometric transformation required
        to move between frequency states in the Merkaba.
        
        Args:
            from_node: Starting node key (e.g., 'akron', 'tata')
            to_node: Destination node key
            
        Returns:
            Rotation angle in degrees (0-360)
            
        Special cases:
            - Any node → King's Chamber: 45° (square → diamond)
            - King's Chamber → any node: 45° (diamond → square)
            - Akron ↔ DOJO: 180° (base ↔ apex inversion)
        """
        if from_node not in self.nodes or to_node not in self.nodes:
            return 0.0
        
        from_freq = self.nodes[from_node].frequency
        to_freq = self.nodes[to_node].frequency
        
        # Special case: King's Chamber transformation (always 45°)
        if from_node == 'kings_chamber' or to_node == 'kings_chamber':
            return 45.0
        
        # Special case: Akron ↔ DOJO (apex/base inversion)
        if {from_node, to_node} == {'akron', 'dojo'}:
            return 180.0
        
        # Calculate based on frequency ratio
        # Map frequency difference to 0-360° rotation
        freq_ratio = to_freq / from_freq
        
        # Use logarithmic scaling for musical/geometric progression
        angle = (math.log2(freq_ratio) * 60) % 360
        
        return round(angle, 2)
    
    def get_node_info(self, node_key: str) -> Optional[MerkabaNode]:
        """Get information about a specific node."""
        return self.nodes.get(node_key)
    
    def get_all_nodes(self) -> Dict[str, MerkabaNode]:
        """Get all nodes in the Merkaba."""
        return self.nodes.copy()
    
    def get_path_info(self, direction: str) -> Dict[str, Any]:
        """
        Get information about a specific path.
        
        Args:
            direction: 'ascending' or 'descending'
            
        Returns:
            Dictionary with path details
        """
        if direction == 'ascending':
            path_keys = self.ascending_path
            path_symbols = '◻ → ▼ → ▲ → ● → ⬥ → ◼︎'
        else:
            path_keys = self.descending_path
            path_symbols = '◼︎ → ⬥ → ● → ▲ → ▼ → ◻'
        
        nodes = [self.nodes[key] for key in path_keys]
        
        return {
            'direction': direction,
            'path_keys': path_keys,
            'path_symbols': path_symbols,
            'nodes': [str(node) for node in nodes],
            'frequencies': [node.frequency for node in nodes],
            'elements': [node.element for node in nodes],
            'ports': [node.port for node in nodes]
        }


def main():
    """Example usage of MerkabaRouter."""
    print("⬥ Merkaba Router - Star Tetrahedron Bidirectional Flow\n")
    
    router = MerkabaRouter()
    
    # Display visualization
    print(router.visualize_merkaba(show_rotation=True))
    
    # Example: Route data ascending
    print("\n" + "="*60)
    print("EXAMPLE: Ascending Flow (Material → Divine)")
    print("="*60 + "\n")
    
    user_data = {
        'type': 'user_upload',
        'content': 'Financial report Q4 2025',
        'user_id': 'user_123'
    }
    
    ascending_result = router.route_ascending(user_data)
    print(f"Path: {ascending_result['path']}")
    print(f"Coherent: {ascending_result['coherence']['coherent']}")
    print(f"King's Chamber Refracted: {ascending_result['coherence']['kings_chamber_refracted']}")
    
    # Example: Route intent descending
    print("\n" + "="*60)
    print("EXAMPLE: Descending Flow (Divine → Material)")
    print("="*60 + "\n")
    
    ai_intent = {
        'type': 'ai_generation',
        'content': 'Generated financial insights based on Q4 data',
        'model': 'gpt-oss-20b-dojo-persona'
    }
    
    descending_result = router.route_descending(ai_intent)
    print(f"Path: {descending_result['path']}")
    print(f"Coherent: {descending_result['coherence']['coherent']}")
    print(f"King's Chamber Refracted: {descending_result['coherence']['kings_chamber_refracted']}")
    
    # Validate complete Merkaba coherence
    print("\n" + "="*60)
    print("MERKABA COHERENCE VALIDATION")
    print("="*60 + "\n")
    
    merkaba_validation = router.validate_merkaba_coherence(ascending_result, descending_result)
    print(f"Merkaba Coherent: {merkaba_validation['merkaba_coherent']}")
    print(f"King's Chamber Bridge: {merkaba_validation['kings_chamber_bridge']}")
    print(f"Akron Dual Nature: {merkaba_validation['akron_dual_nature']}")
    print(f"DOJO Dual Nature: {merkaba_validation['dojo_dual_nature']}")
    
    # Example: Transformation angles
    print("\n" + "="*60)
    print("TRANSFORMATION ANGLES")
    print("="*60 + "\n")
    
    print(f"Akron → King's Chamber: {router.get_transformation_angle('akron', 'kings_chamber')}°")
    print(f"King's Chamber → DOJO: {router.get_transformation_angle('kings_chamber', 'dojo')}°")
    print(f"Akron ↔ DOJO (inversion): {router.get_transformation_angle('akron', 'dojo')}°")


if __name__ == '__main__':
    main()
