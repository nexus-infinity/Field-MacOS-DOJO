"""
Feature Epic and Story management classes
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class Story:
    """User story with point estimation"""
    
    value: str
    points: int
    completed: bool = False
    
    def complete(self) -> None:
        """Mark story as completed"""
        self.completed = True
    
    def is_completed(self) -> bool:
        """Check if story is completed"""
        return self.completed


@dataclass
class Task:
    """Development task with hour estimation"""
    
    description: str
    hours: int
    completed: bool = False
    
    def complete(self) -> None:
        """Mark task as completed"""
        self.completed = True
    
    def is_completed(self) -> bool:
        """Check if task is completed"""
        return self.completed


class FeatureEpic:
    """Base class for feature epics"""
    
    def __init__(self, name: str):
        self.name = name
        self.user_stories: List[Story] = []
        self.acceptance_criteria: List[str] = []
        self.definition_of_done: List[str] = []
        self.tasks: List[Task] = []
    
    def add_user_story(self, story: Story) -> None:
        """Add a user story to the epic"""
        self.user_stories.append(story)
    
    def add_acceptance_criterion(self, criterion: str) -> None:
        """Add an acceptance criterion"""
        self.acceptance_criteria.append(criterion)
    
    def add_definition_of_done(self, item: str) -> None:
        """Add a definition of done item"""
        self.definition_of_done.append(item)
    
    def add_task(self, task: Task) -> None:
        """Add a task to the epic"""
        self.tasks.append(task)
    
    def get_total_points(self) -> int:
        """Calculate total story points"""
        return sum(story.points for story in self.user_stories)
    
    def get_completed_points(self) -> int:
        """Calculate completed story points"""
        return sum(story.points for story in self.user_stories if story.completed)
    
    def get_completion_percentage(self) -> float:
        """Calculate completion percentage"""
        total = self.get_total_points()
        if total == 0:
            return 0.0
        return (self.get_completed_points() / total) * 100
    
    def is_complete(self) -> bool:
        """Check if epic is complete"""
        return all(story.completed for story in self.user_stories)
