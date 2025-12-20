"""
Core Sprint Trident classes implementing the three-pronged approach
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class BuildPipeline:
    """Feature development prong"""
    
    features: List[str] = field(default_factory=list)
    status: str = "not_started"
    
    def add_feature(self, feature: str) -> None:
        """Add a feature to the build pipeline"""
        self.features.append(feature)
    
    def get_status(self) -> str:
        """Get current build status"""
        return self.status
    
    def set_status(self, status: str) -> None:
        """Update build status"""
        self.status = status


@dataclass
class TestHarness:
    """Validation layer prong"""
    
    test_suites: List[str] = field(default_factory=list)
    coverage: float = 0.0
    tests_passing: bool = False
    
    def add_test_suite(self, suite: str) -> None:
        """Add a test suite to the harness"""
        self.test_suites.append(suite)
    
    def update_coverage(self, coverage: float) -> None:
        """Update test coverage percentage"""
        self.coverage = coverage
    
    def set_tests_passing(self, passing: bool) -> None:
        """Update test passing status"""
        self.tests_passing = passing


@dataclass
class LearningLoop:
    """Feedback integration prong"""
    
    insights: List[Dict[str, Any]] = field(default_factory=list)
    action_items: List[str] = field(default_factory=list)
    
    def capture_insight(self, insight: Dict[str, Any]) -> None:
        """Capture a learning insight"""
        self.insights.append(insight)
    
    def add_action_item(self, action: str) -> None:
        """Add an action item from learning"""
        self.action_items.append(action)
    
    def get_insights(self) -> List[Dict[str, Any]]:
        """Retrieve all captured insights"""
        return self.insights


class SprintTrident:
    """Three-pronged approach: Build, Test, Learn"""
    
    def __init__(self):
        self.prong_alpha = BuildPipeline()
        self.prong_beta = TestHarness()
        self.prong_gamma = LearningLoop()
    
    def get_build_pipeline(self) -> BuildPipeline:
        """Get the build pipeline prong"""
        return self.prong_alpha
    
    def get_test_harness(self) -> TestHarness:
        """Get the test harness prong"""
        return self.prong_beta
    
    def get_learning_loop(self) -> LearningLoop:
        """Get the learning loop prong"""
        return self.prong_gamma
    
    def get_health_status(self) -> Dict[str, Any]:
        """Get overall health status of the sprint trident"""
        return {
            "build": {
                "status": self.prong_alpha.status,
                "features": len(self.prong_alpha.features)
            },
            "test": {
                "coverage": self.prong_beta.coverage,
                "passing": self.prong_beta.tests_passing
            },
            "learn": {
                "insights": len(self.prong_gamma.insights),
                "actions": len(self.prong_gamma.action_items)
            }
        }
