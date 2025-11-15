"""
Sprint planning and execution classes
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from collections import OrderedDict
from ..core.sprint_trident import SprintTrident
from ..core.feature_epic import Story


@dataclass
class ExitCriteria:
    """Exit criteria for phases and sprints"""
    
    coverage: Optional[float] = None
    tests_passing: Optional[bool] = None
    features_complete: Optional[bool] = None
    integrated: Optional[bool] = None
    performance_targets_met: Optional[bool] = None
    
    def is_met(self) -> bool:
        """Check if all specified criteria are met"""
        criteria = []
        if self.coverage is not None:
            criteria.append(self.coverage >= 80)
        if self.tests_passing is not None:
            criteria.append(self.tests_passing)
        if self.features_complete is not None:
            criteria.append(self.features_complete)
        if self.integrated is not None:
            criteria.append(self.integrated)
        if self.performance_targets_met is not None:
            criteria.append(self.performance_targets_met)
        return all(criteria) if criteria else False


@dataclass
class Phase:
    """Development phase with tasks and exit criteria"""
    
    name: str
    tasks: List[str] = field(default_factory=list)
    exit_criteria: Optional[ExitCriteria] = None
    completed: bool = False
    
    def add_task(self, task: str) -> None:
        """Add a task to the phase"""
        self.tasks.append(task)
    
    def complete(self) -> None:
        """Mark phase as completed"""
        self.completed = True


@dataclass
class Deliverable:
    """Sprint deliverable artifact"""
    
    artifact: str
    repository: str
    acceptance_criteria: List[str] = field(default_factory=list)
    delivered: bool = False
    
    def mark_delivered(self) -> None:
        """Mark deliverable as delivered"""
        self.delivered = True
    
    def add_acceptance_criterion(self, criterion: str) -> None:
        """Add an acceptance criterion"""
        self.acceptance_criteria.append(criterion)


class Sprint(SprintTrident):
    """Sprint with goals, capacity, and deliverables"""
    
    def __init__(self, goal: str = "", capacity: int = 40):
        super().__init__()
        self.goal = goal
        self.capacity = capacity
        self.completed_stories: List[Story] = []
        self.deliverables: List[Deliverable] = []
        self.dependencies: List['Sprint'] = []
    
    def add_deliverable(self, deliverable: Deliverable) -> None:
        """Add a deliverable to the sprint"""
        self.deliverables.append(deliverable)
    
    def add_dependency(self, sprint: 'Sprint') -> None:
        """Add a sprint dependency"""
        self.dependencies.append(sprint)
    
    def complete_story(self, story: Story) -> None:
        """Mark a story as completed"""
        story.complete()
        self.completed_stories.append(story)
    
    def get_velocity(self) -> int:
        """Calculate sprint velocity (completed story points)"""
        return sum(story.points for story in self.completed_stories)
    
    def get_capacity_utilization(self) -> float:
        """Calculate capacity utilization percentage"""
        velocity = self.get_velocity()
        return (velocity / self.capacity * 100) if self.capacity > 0 else 0.0


class ExecutionPipeline:
    """Sequential execution pipeline for phases"""
    
    def __init__(self):
        self.sequence: OrderedDict[str, Phase] = OrderedDict()
    
    def add_phase(self, phase: Phase) -> None:
        """Add a phase to the execution pipeline"""
        self.sequence[phase.name] = phase
    
    def get_phase(self, name: str) -> Optional[Phase]:
        """Get a phase by name"""
        return self.sequence.get(name)
    
    def get_current_phase(self) -> Optional[Phase]:
        """Get the current active phase (first incomplete phase)"""
        for phase in self.sequence.values():
            if not phase.completed:
                return phase
        return None
    
    def get_completion_percentage(self) -> float:
        """Calculate overall pipeline completion percentage"""
        if not self.sequence:
            return 0.0
        completed = sum(1 for phase in self.sequence.values() if phase.completed)
        return (completed / len(self.sequence)) * 100


class DefinitionOfDone:
    """Definition of Done criteria"""
    
    def __init__(self):
        self.criteria: Dict[str, str] = {
            "code_complete": "All code peer-reviewed and merged",
            "tests_passing": "Unit, integration, and performance tests green",
            "documented": "API docs and usage examples provided",
            "deployed": "Running in test environment",
            "monitored": "Metrics and alerts configured",
            "learned": "Retrospective insights captured"
        }
    
    def add_criterion(self, key: str, description: str) -> None:
        """Add a custom criterion"""
        self.criteria[key] = description
    
    def get_criteria(self) -> Dict[str, str]:
        """Get all criteria"""
        return self.criteria


class SprintRetrospective:
    """Sprint retrospective for capturing learnings"""
    
    def __init__(self, sprint: Sprint):
        self.sprint = sprint
        self.insights: List[Dict[str, Any]] = []
        self.action_items: List[str] = []
    
    def identify_successes(self) -> List[str]:
        """Identify what went well"""
        return [f"Completed {self.sprint.get_velocity()} story points"]
    
    def identify_challenges(self) -> List[str]:
        """Identify what needs improvement"""
        utilization = self.sprint.get_capacity_utilization()
        if utilization < 80:
            return [f"Capacity utilization was only {utilization:.1f}%"]
        return []
    
    def generate_actions(self) -> List[str]:
        """Generate action items"""
        return self.action_items
    
    def document_learnings(self) -> Dict[str, Any]:
        """Document captured learnings"""
        return {
            "insights": self.insights,
            "velocity": self.sprint.get_velocity(),
            "capacity_utilization": self.sprint.get_capacity_utilization()
        }
    
    def capture_insights(self) -> Dict[str, Any]:
        """Capture comprehensive retrospective insights"""
        return {
            "what_went_well": self.identify_successes(),
            "what_needs_improvement": self.identify_challenges(),
            "action_items": self.generate_actions(),
            "knowledge_captured": self.document_learnings()
        }
    
    def apply_to_next_sprint(self, next_sprint: Sprint) -> None:
        """Apply learnings to the next sprint"""
        for action in self.action_items:
            next_sprint.get_learning_loop().add_action_item(action)
