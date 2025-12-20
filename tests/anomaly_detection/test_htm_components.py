"""
Tests for HTM Anomaly Detection components
"""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from anomaly_detection.htm.spatial_pooler import SpatialPooler
from anomaly_detection.htm.temporal_memory import TemporalMemory
from anomaly_detection.anomaly_scorer import AnomalyScorer


class TestSpatialPooler(unittest.TestCase):
    """Test SpatialPooler class"""
    
    def setUp(self):
        self.input_size = 100
        self.column_count = 500
        self.pooler = SpatialPooler(self.input_size, self.column_count, sparsity=0.02)
    
    def test_initialization(self):
        """Test SpatialPooler initialization"""
        self.assertEqual(self.pooler.input_size, self.input_size)
        self.assertEqual(self.pooler.column_count, self.column_count)
        self.assertEqual(self.pooler.sparsity, 0.02)
    
    def test_compute(self):
        """Test computing active columns"""
        input_vector = np.random.randint(0, 2, self.input_size)
        active_columns = self.pooler.compute(input_vector, learn=False)
        
        # Check that we get the right number of active columns
        expected_count = int(self.column_count * 0.02)
        self.assertEqual(len(active_columns), expected_count)
        
        # Check that all columns are valid indices
        for col in active_columns:
            self.assertGreaterEqual(col, 0)
            self.assertLess(col, self.column_count)
    
    def test_learning(self):
        """Test learning updates permanences"""
        input_vector = np.ones(self.input_size)
        
        # Get initial permanences
        initial_perm = self.pooler.permanences.copy()
        
        # Compute with learning
        self.pooler.compute(input_vector, learn=True)
        
        # Permanences should have changed
        self.assertFalse(np.array_equal(initial_perm, self.pooler.permanences))
    
    def test_reset(self):
        """Test resetting the pooler"""
        input_vector = np.ones(self.input_size)
        self.pooler.compute(input_vector, learn=True)
        
        # Reset and check permanences changed
        initial_perm = self.pooler.permanences.copy()
        self.pooler.reset()
        
        self.assertFalse(np.array_equal(initial_perm, self.pooler.permanences))


class TestTemporalMemory(unittest.TestCase):
    """Test TemporalMemory class"""
    
    def setUp(self):
        self.column_count = 100
        self.cells_per_column = 32
        self.tm = TemporalMemory(self.column_count, self.cells_per_column)
    
    def test_initialization(self):
        """Test TemporalMemory initialization"""
        self.assertEqual(self.tm.column_count, self.column_count)
        self.assertEqual(self.tm.cells_per_column, self.cells_per_column)
        self.assertEqual(len(self.tm.cells), self.column_count)
        self.assertEqual(len(self.tm.cells[0]), self.cells_per_column)
    
    def test_compute(self):
        """Test computing active and predictive cells"""
        active_columns = {0, 1, 2}
        active_cells, predictive_cells = self.tm.compute(active_columns, learn=False)
        
        # Should have some active cells
        self.assertGreater(len(active_cells), 0)
    
    def test_anomaly_score(self):
        """Test anomaly score calculation"""
        # First timestep - everything is anomalous
        active_columns = {0, 1, 2}
        self.tm.compute(active_columns, learn=True)
        score1 = self.tm.get_anomaly_score()
        
        # Should have high anomaly initially
        self.assertGreater(score1, 0)
    
    def test_reset(self):
        """Test resetting temporal memory"""
        active_columns = {0, 1, 2}
        self.tm.compute(active_columns, learn=True)
        
        self.assertGreater(len(self.tm.active_cells), 0)
        
        self.tm.reset()
        
        self.assertEqual(len(self.tm.active_cells), 0)
        self.assertEqual(len(self.tm.predictive_cells), 0)


class TestAnomalyScorer(unittest.TestCase):
    """Test AnomalyScorer class"""
    
    def setUp(self):
        input_size = 100
        column_count = 500
        sp = SpatialPooler(input_size, column_count)
        tm = TemporalMemory(column_count)
        self.scorer = AnomalyScorer(sp, tm)
    
    def test_initialization(self):
        """Test AnomalyScorer initialization"""
        self.assertEqual(self.scorer.anomaly_threshold, 0.7)
        self.assertEqual(len(self.scorer.anomaly_scores), 0)
    
    def test_compute_anomaly(self):
        """Test computing anomaly scores"""
        input_vector = np.random.randint(0, 2, 100)
        score = self.scorer.compute_anomaly(input_vector, learn=False)
        
        # Score should be between 0 and 1
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)
        
        # Should have recorded the score
        self.assertEqual(len(self.scorer.anomaly_scores), 1)
    
    def test_is_anomalous(self):
        """Test anomaly detection"""
        self.assertTrue(self.scorer.is_anomalous(0.8))
        self.assertFalse(self.scorer.is_anomalous(0.5))
    
    def test_metrics(self):
        """Test getting metrics"""
        input_vector = np.random.randint(0, 2, 100)
        
        for _ in range(10):
            self.scorer.compute_anomaly(input_vector, learn=False)
        
        metrics = self.scorer.get_metrics()
        
        self.assertEqual(metrics['throughput'], 10)
        self.assertIn('average_anomaly', metrics)
        self.assertIn('anomaly_rate', metrics)
    
    def test_set_threshold(self):
        """Test setting anomaly threshold"""
        self.scorer.set_threshold(0.5)
        self.assertEqual(self.scorer.anomaly_threshold, 0.5)
        
        # Test bounds
        self.scorer.set_threshold(1.5)
        self.assertEqual(self.scorer.anomaly_threshold, 1.0)
        
        self.scorer.set_threshold(-0.5)
        self.assertEqual(self.scorer.anomaly_threshold, 0.0)


if __name__ == '__main__':
    unittest.main()
