"""
Tests for Sprint Trident core classes
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from trident_scrum.core.sprint_trident import SprintTrident, BuildPipeline, TestHarness, LearningLoop


class TestBuildPipeline(unittest.TestCase):
    """Test BuildPipeline class"""
    
    def setUp(self):
        self.pipeline = BuildPipeline()
    
    def test_initialization(self):
        """Test BuildPipeline initialization"""
        self.assertEqual(self.pipeline.status, "not_started")
        self.assertEqual(len(self.pipeline.features), 0)
    
    def test_add_feature(self):
        """Test adding features"""
        self.pipeline.add_feature("Feature 1")
        self.pipeline.add_feature("Feature 2")
        
        self.assertEqual(len(self.pipeline.features), 2)
        self.assertIn("Feature 1", self.pipeline.features)
    
    def test_status_management(self):
        """Test status updates"""
        self.pipeline.set_status("in_progress")
        self.assertEqual(self.pipeline.get_status(), "in_progress")


class TestTestHarness(unittest.TestCase):
    """Test TestHarness class"""
    
    def setUp(self):
        self.harness = TestHarness()
    
    def test_initialization(self):
        """Test TestHarness initialization"""
        self.assertEqual(self.harness.coverage, 0.0)
        self.assertFalse(self.harness.tests_passing)
    
    def test_add_test_suite(self):
        """Test adding test suites"""
        self.harness.add_test_suite("Unit Tests")
        self.harness.add_test_suite("Integration Tests")
        
        self.assertEqual(len(self.harness.test_suites), 2)
    
    def test_coverage_update(self):
        """Test coverage updates"""
        self.harness.update_coverage(85.5)
        self.assertEqual(self.harness.coverage, 85.5)
    
    def test_tests_passing(self):
        """Test tests passing status"""
        self.harness.set_tests_passing(True)
        self.assertTrue(self.harness.tests_passing)


class TestLearningLoop(unittest.TestCase):
    """Test LearningLoop class"""
    
    def setUp(self):
        self.loop = LearningLoop()
    
    def test_initialization(self):
        """Test LearningLoop initialization"""
        self.assertEqual(len(self.loop.insights), 0)
        self.assertEqual(len(self.loop.action_items), 0)
    
    def test_capture_insight(self):
        """Test capturing insights"""
        insight = {"type": "performance", "description": "Improved velocity"}
        self.loop.capture_insight(insight)
        
        self.assertEqual(len(self.loop.insights), 1)
        self.assertEqual(self.loop.insights[0], insight)
    
    def test_action_items(self):
        """Test adding action items"""
        self.loop.add_action_item("Improve code review process")
        self.loop.add_action_item("Add more automated tests")
        
        self.assertEqual(len(self.loop.action_items), 2)


class TestSprintTrident(unittest.TestCase):
    """Test SprintTrident class"""
    
    def setUp(self):
        self.trident = SprintTrident()
    
    def test_initialization(self):
        """Test SprintTrident initialization"""
        self.assertIsInstance(self.trident.prong_alpha, BuildPipeline)
        self.assertIsInstance(self.trident.prong_beta, TestHarness)
        self.assertIsInstance(self.trident.prong_gamma, LearningLoop)
    
    def test_get_prongs(self):
        """Test getting individual prongs"""
        build = self.trident.get_build_pipeline()
        test = self.trident.get_test_harness()
        learn = self.trident.get_learning_loop()
        
        self.assertIsInstance(build, BuildPipeline)
        self.assertIsInstance(test, TestHarness)
        self.assertIsInstance(learn, LearningLoop)
    
    def test_health_status(self):
        """Test getting health status"""
        # Setup some state
        self.trident.prong_alpha.add_feature("Feature 1")
        self.trident.prong_alpha.set_status("in_progress")
        self.trident.prong_beta.update_coverage(80.0)
        self.trident.prong_gamma.add_action_item("Action 1")
        
        status = self.trident.get_health_status()
        
        self.assertEqual(status["build"]["status"], "in_progress")
        self.assertEqual(status["build"]["features"], 1)
        self.assertEqual(status["test"]["coverage"], 80.0)
        self.assertEqual(status["learn"]["actions"], 1)


if __name__ == '__main__':
    unittest.main()
