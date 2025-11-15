"""
Trident Scrum Methodology Framework

A three-pronged approach to agile development: Build, Test, Learn
"""

from .core.sprint_trident import SprintTrident, BuildPipeline, TestHarness, LearningLoop
from .core.feature_epic import FeatureEpic, Story, Task
from .sprints.sprint_planning import Sprint, Deliverable, ExitCriteria, Phase
from .utils.metrics import VelocityTracker, QualityMetrics, Metric

__version__ = "1.0.0"

__all__ = [
    "SprintTrident",
    "BuildPipeline",
    "TestHarness",
    "LearningLoop",
    "FeatureEpic",
    "Story",
    "Task",
    "Sprint",
    "Deliverable",
    "ExitCriteria",
    "Phase",
    "VelocityTracker",
    "QualityMetrics",
    "Metric",
]
