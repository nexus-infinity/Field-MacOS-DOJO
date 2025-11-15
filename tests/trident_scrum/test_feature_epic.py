"""
Tests for Feature Epic classes
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from trident_scrum.core.feature_epic import FeatureEpic, Story, Task


class TestStory(unittest.TestCase):
    """Test Story class"""
    
    def test_story_creation(self):
        """Test creating a story"""
        story = Story(value="As a user, I need feature X", points=5)
        
        self.assertEqual(story.value, "As a user, I need feature X")
        self.assertEqual(story.points, 5)
        self.assertFalse(story.completed)
    
    def test_complete_story(self):
        """Test completing a story"""
        story = Story(value="Story 1", points=3)
        story.complete()
        
        self.assertTrue(story.is_completed())


class TestTask(unittest.TestCase):
    """Test Task class"""
    
    def test_task_creation(self):
        """Test creating a task"""
        task = Task(description="Implement feature", hours=8)
        
        self.assertEqual(task.description, "Implement feature")
        self.assertEqual(task.hours, 8)
        self.assertFalse(task.completed)
    
    def test_complete_task(self):
        """Test completing a task"""
        task = Task(description="Task 1", hours=5)
        task.complete()
        
        self.assertTrue(task.is_completed())


class TestFeatureEpic(unittest.TestCase):
    """Test FeatureEpic class"""
    
    def setUp(self):
        self.epic = FeatureEpic("Test Epic")
    
    def test_initialization(self):
        """Test epic initialization"""
        self.assertEqual(self.epic.name, "Test Epic")
        self.assertEqual(len(self.epic.user_stories), 0)
        self.assertEqual(len(self.epic.tasks), 0)
    
    def test_add_user_story(self):
        """Test adding user stories"""
        story1 = Story(value="Story 1", points=5)
        story2 = Story(value="Story 2", points=8)
        
        self.epic.add_user_story(story1)
        self.epic.add_user_story(story2)
        
        self.assertEqual(len(self.epic.user_stories), 2)
        self.assertEqual(self.epic.get_total_points(), 13)
    
    def test_add_task(self):
        """Test adding tasks"""
        task1 = Task(description="Task 1", hours=5)
        task2 = Task(description="Task 2", hours=8)
        
        self.epic.add_task(task1)
        self.epic.add_task(task2)
        
        self.assertEqual(len(self.epic.tasks), 2)
    
    def test_completion_tracking(self):
        """Test completion percentage calculation"""
        story1 = Story(value="Story 1", points=5)
        story2 = Story(value="Story 2", points=5)
        
        self.epic.add_user_story(story1)
        self.epic.add_user_story(story2)
        
        # Complete one story
        story1.complete()
        
        self.assertEqual(self.epic.get_completed_points(), 5)
        self.assertEqual(self.epic.get_completion_percentage(), 50.0)
        self.assertFalse(self.epic.is_complete())
        
        # Complete second story
        story2.complete()
        
        self.assertEqual(self.epic.get_completed_points(), 10)
        self.assertEqual(self.epic.get_completion_percentage(), 100.0)
        self.assertTrue(self.epic.is_complete())
    
    def test_acceptance_criteria(self):
        """Test acceptance criteria management"""
        self.epic.add_acceptance_criterion("Criterion 1")
        self.epic.add_acceptance_criterion("Criterion 2")
        
        self.assertEqual(len(self.epic.acceptance_criteria), 2)
    
    def test_definition_of_done(self):
        """Test definition of done management"""
        self.epic.add_definition_of_done("Code reviewed")
        self.epic.add_definition_of_done("Tests passing")
        
        self.assertEqual(len(self.epic.definition_of_done), 2)


if __name__ == '__main__':
    unittest.main()
