"""
Tests for Merkaba Router implementation
"""

import unittest
import sys
import os
import importlib.util

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import using path-based import since directory name has hyphens
spec = importlib.util.spec_from_file_location(
    "merkaba_router", 
    os.path.join(os.path.dirname(__file__), '../../tier1-sacred-mcp/kings-chamber/merkaba-router.py')
)
merkaba_router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(merkaba_router)

MerkabaRouter = merkaba_router.MerkabaRouter
MerkabaNode = merkaba_router.MerkabaNode


class TestMerkabaNode(unittest.TestCase):
    """Test MerkabaNode dataclass"""
    
    def test_node_creation(self):
        """Test creating a MerkabaNode"""
        node = MerkabaNode(
            name='Test Node',
            frequency=396,
            symbol='◻',
            position='base',
            element='earth',
            port=3960
        )
        
        self.assertEqual(node.name, 'Test Node')
        self.assertEqual(node.frequency, 396)
        self.assertEqual(node.symbol, '◻')
        self.assertEqual(node.position, 'base')
        self.assertEqual(node.element, 'earth')
        self.assertEqual(node.port, 3960)
    
    def test_node_string_representation(self):
        """Test string representation of node"""
        node = MerkabaNode(
            name='Akron Gateway',
            frequency=396,
            symbol='◻',
            position='base',
            element='earth',
            port=3960
        )
        
        expected = "◻ Akron Gateway (396 Hz)"
        self.assertEqual(str(node), expected)


class TestMerkabaRouter(unittest.TestCase):
    """Test MerkabaRouter class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.router = MerkabaRouter()
    
    def test_router_initialization(self):
        """Test router initializes with correct nodes"""
        self.assertEqual(len(self.router.nodes), 6)
        
        # Check all required nodes exist
        required_nodes = ['akron', 'tata', 'atlas', 'dojo', 'kings_chamber', 'obi_wan']
        for node_key in required_nodes:
            self.assertIn(node_key, self.router.nodes)
    
    def test_ascending_path(self):
        """Test ascending path is correct"""
        expected_path = ['akron', 'tata', 'atlas', 'obi_wan', 'kings_chamber', 'dojo']
        self.assertEqual(self.router.ascending_path, expected_path)
    
    def test_descending_path(self):
        """Test descending path is correct"""
        expected_path = ['dojo', 'kings_chamber', 'obi_wan', 'atlas', 'tata', 'akron']
        self.assertEqual(self.router.descending_path, expected_path)
    
    def test_route_ascending(self):
        """Test ascending route from Material to Divine"""
        test_data = {
            'type': 'test_upload',
            'content': 'Test data for ascending flow'
        }
        
        result = self.router.route_ascending(test_data)
        
        # Check result structure
        self.assertEqual(result['direction'], 'ascending')
        self.assertIn('route', result)
        self.assertIn('coherence', result)
        self.assertEqual(len(result['route']), 6)
        
        # Check path symbols
        self.assertEqual(result['path'], '◻ → ▼ → ▲ → ● → ⬥ → ◼︎')
        
        # Check frequency progression
        expected_frequencies = [396, 432, 528, 963, 852, 741]
        self.assertEqual(result['frequencies'], expected_frequencies)
        
        # Check coherence
        self.assertTrue(result['coherence']['coherent'])
        self.assertTrue(result['coherence']['kings_chamber_refracted'])
    
    def test_route_descending(self):
        """Test descending route from Divine to Material"""
        test_intent = {
            'type': 'ai_generation',
            'content': 'AI-generated insights'
        }
        
        result = self.router.route_descending(test_intent)
        
        # Check result structure
        self.assertEqual(result['direction'], 'descending')
        self.assertIn('route', result)
        self.assertIn('coherence', result)
        self.assertEqual(len(result['route']), 6)
        
        # Check path symbols
        self.assertEqual(result['path'], '◼︎ → ⬥ → ● → ▲ → ▼ → ◻')
        
        # Check frequency progression
        expected_frequencies = [741, 852, 963, 528, 432, 396]
        self.assertEqual(result['frequencies'], expected_frequencies)
        
        # Check coherence
        self.assertTrue(result['coherence']['coherent'])
        self.assertTrue(result['coherence']['kings_chamber_refracted'])
    
    def test_kings_chamber_in_both_paths(self):
        """Test that King's Chamber appears in both paths"""
        test_data = {'test': 'data'}
        
        asc_result = self.router.route_ascending(test_data)
        desc_result = self.router.route_descending(test_data)
        
        # Check King's Chamber (852 Hz) is in both
        asc_has_kc = any(entry['frequency'] == 852 for entry in asc_result['route'])
        desc_has_kc = any(entry['frequency'] == 852 for entry in desc_result['route'])
        
        self.assertTrue(asc_has_kc)
        self.assertTrue(desc_has_kc)
    
    def test_validate_merkaba_coherence(self):
        """Test Merkaba coherence validation"""
        test_data = {'test': 'data'}
        
        ascending = self.router.route_ascending(test_data)
        descending = self.router.route_descending(test_data)
        
        validation = self.router.validate_merkaba_coherence(ascending, descending)
        
        # Check validation results
        self.assertTrue(validation['merkaba_coherent'])
        self.assertTrue(validation['ascending_coherent'])
        self.assertTrue(validation['descending_coherent'])
        self.assertTrue(validation['kings_chamber_bridge'])
        self.assertTrue(validation['akron_dual_nature'])
        self.assertTrue(validation['dojo_dual_nature'])
        self.assertTrue(validation['all_frequencies_present'])
        self.assertEqual(len(validation['errors']), 0)
    
    def test_akron_dual_nature(self):
        """Test that Akron serves as both BASE and APEX"""
        test_data = {'test': 'data'}
        
        ascending = self.router.route_ascending(test_data)
        descending = self.router.route_descending(test_data)
        
        # Akron should be first in ascending (BASE)
        self.assertEqual(ascending['route'][0]['frequency'], 396)
        
        # Akron should be last in descending (APEX)
        self.assertEqual(descending['route'][-1]['frequency'], 396)
    
    def test_dojo_dual_nature(self):
        """Test that DOJO serves as both APEX and BASE"""
        test_data = {'test': 'data'}
        
        ascending = self.router.route_ascending(test_data)
        descending = self.router.route_descending(test_data)
        
        # DOJO should be last in ascending (APEX)
        self.assertEqual(ascending['route'][-1]['frequency'], 741)
        
        # DOJO should be first in descending (BASE)
        self.assertEqual(descending['route'][0]['frequency'], 741)
    
    def test_transformation_angle_kings_chamber(self):
        """Test transformation angle to/from King's Chamber is 45°"""
        angle_to_kc = self.router.get_transformation_angle('akron', 'kings_chamber')
        angle_from_kc = self.router.get_transformation_angle('kings_chamber', 'dojo')
        
        # Both should be 45° (diamond rotation)
        self.assertEqual(angle_to_kc, 45.0)
        self.assertEqual(angle_from_kc, 45.0)
    
    def test_transformation_angle_akron_dojo(self):
        """Test transformation angle between Akron and DOJO is 180°"""
        angle = self.router.get_transformation_angle('akron', 'dojo')
        
        # Should be 180° (apex/base inversion)
        self.assertEqual(angle, 180.0)
    
    def test_visualize_merkaba(self):
        """Test Merkaba visualization generates valid ASCII art"""
        visualization = self.router.visualize_merkaba(show_rotation=False)
        
        # Check that visualization contains key elements
        self.assertIn('MERKABA', visualization)
        self.assertIn('ASCENDING TETRAHEDRON', visualization)
        self.assertIn('DESCENDING TETRAHEDRON', visualization)
        self.assertIn('◻', visualization)  # Akron symbol
        self.assertIn('⬥', visualization)  # King's Chamber symbol
        self.assertIn('◼︎', visualization)  # DOJO symbol
        self.assertIn('396 Hz', visualization)
        self.assertIn('852 Hz', visualization)
        self.assertIn('741 Hz', visualization)
    
    def test_visualize_merkaba_with_rotation(self):
        """Test Merkaba visualization with rotation markers"""
        visualization = self.router.visualize_merkaba(show_rotation=True)
        
        # Check for rotation markers
        self.assertIn('↻', visualization)
        self.assertIn('↺', visualization)
    
    def test_get_node_info(self):
        """Test getting node information"""
        akron = self.router.get_node_info('akron')
        
        self.assertIsNotNone(akron)
        self.assertEqual(akron.frequency, 396)
        self.assertEqual(akron.symbol, '◻')
        self.assertEqual(akron.element, 'earth')
    
    def test_get_all_nodes(self):
        """Test getting all nodes"""
        all_nodes = self.router.get_all_nodes()
        
        self.assertEqual(len(all_nodes), 6)
        self.assertIn('akron', all_nodes)
        self.assertIn('kings_chamber', all_nodes)
        self.assertIn('dojo', all_nodes)
    
    def test_get_path_info_ascending(self):
        """Test getting ascending path information"""
        path_info = self.router.get_path_info('ascending')
        
        self.assertEqual(path_info['direction'], 'ascending')
        self.assertEqual(path_info['path_symbols'], '◻ → ▼ → ▲ → ● → ⬥ → ◼︎')
        self.assertEqual(len(path_info['nodes']), 6)
        self.assertEqual(path_info['frequencies'][0], 396)
        self.assertEqual(path_info['frequencies'][-1], 741)
    
    def test_get_path_info_descending(self):
        """Test getting descending path information"""
        path_info = self.router.get_path_info('descending')
        
        self.assertEqual(path_info['direction'], 'descending')
        self.assertEqual(path_info['path_symbols'], '◼︎ → ⬥ → ● → ▲ → ▼ → ◻')
        self.assertEqual(len(path_info['nodes']), 6)
        self.assertEqual(path_info['frequencies'][0], 741)
        self.assertEqual(path_info['frequencies'][-1], 396)
    
    def test_all_frequencies_unique(self):
        """Test that all six frequencies are unique"""
        frequencies = {node.frequency for node in self.router.nodes.values()}
        
        self.assertEqual(len(frequencies), 6)
        expected = {396, 432, 528, 741, 852, 963}
        self.assertEqual(frequencies, expected)
    
    def test_all_symbols_unique(self):
        """Test that all six symbols are unique"""
        symbols = {node.symbol for node in self.router.nodes.values()}
        
        self.assertEqual(len(symbols), 6)
        expected = {'◻', '▼', '▲', '◼︎', '⬥', '●'}
        self.assertEqual(symbols, expected)
    
    def test_transformation_log_created(self):
        """Test that transformation log is created during routing"""
        test_data = {'content': 'test'}
        
        result = self.router.route_ascending(test_data)
        
        # Check that final output has transformation log
        self.assertIn('_transformation_log', result['final_output'])
        self.assertEqual(len(result['final_output']['_transformation_log']), 6)
    
    def test_kings_chamber_refraction_marker(self):
        """Test that King's Chamber adds refraction marker"""
        test_data = {'content': 'test'}
        
        result = self.router.route_ascending(test_data)
        
        # Check that King's Chamber refraction marker exists
        self.assertIn('_kings_chamber_refracted', result['final_output'])
        self.assertTrue(result['final_output']['_kings_chamber_refracted'])
        self.assertEqual(result['final_output']['_refraction_angle'], 45)


if __name__ == '__main__':
    unittest.main()
