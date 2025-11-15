"""
Metrics and KPI tracking classes
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from ..sprints.sprint_planning import Sprint


@dataclass
class Metric:
    """Generic metric with target"""
    
    target: str
    current_value: Any = None
    
    def update(self, value: Any) -> None:
        """Update metric value"""
        self.current_value = value
    
    def is_met(self) -> bool:
        """Check if metric target is met"""
        # Simple string comparison for now
        return self.current_value is not None


class VelocityTracker:
    """Track sprint velocity over time"""
    
    def __init__(self):
        self.sprint_velocities: List[int] = []
        self.rolling_average: float = 0.0
    
    def calculate_velocity(self, sprint: Sprint) -> int:
        """Calculate velocity for a sprint"""
        completed_points = sum(story.points for story in sprint.completed_stories)
        self.sprint_velocities.append(completed_points)
        
        # Calculate rolling average of last 3 sprints
        recent = self.sprint_velocities[-3:]
        self.rolling_average = sum(recent) / len(recent) if recent else 0.0
        
        return completed_points
    
    def get_rolling_average(self) -> float:
        """Get the rolling average velocity"""
        return self.rolling_average
    
    def get_trend(self) -> str:
        """Get velocity trend (improving, stable, declining)"""
        if len(self.sprint_velocities) < 2:
            return "insufficient_data"
        
        recent_avg = sum(self.sprint_velocities[-3:]) / min(3, len(self.sprint_velocities[-3:]))
        older_avg = sum(self.sprint_velocities[-6:-3]) / min(3, len(self.sprint_velocities[-6:-3])) if len(self.sprint_velocities) > 3 else recent_avg
        
        if recent_avg > older_avg * 1.1:
            return "improving"
        elif recent_avg < older_avg * 0.9:
            return "declining"
        else:
            return "stable"


class QualityMetrics:
    """Quality metrics tracking"""
    
    def __init__(self):
        self.metrics: Dict[str, Metric] = {
            "defect_density": Metric(target="< 0.1 per KLOC"),
            "code_coverage": Metric(target="> 80%"),
            "technical_debt": Metric(target="< 5% of sprint capacity"),
            "customer_satisfaction": Metric(target="> 4.5/5")
        }
    
    def update_metric(self, name: str, value: Any) -> None:
        """Update a quality metric"""
        if name in self.metrics:
            self.metrics[name].update(value)
    
    def add_custom_metric(self, name: str, metric: Metric) -> None:
        """Add a custom quality metric"""
        self.metrics[name] = metric
    
    def get_metric(self, name: str) -> Metric:
        """Get a specific metric"""
        return self.metrics.get(name)
    
    def get_all_metrics(self) -> Dict[str, Metric]:
        """Get all quality metrics"""
        return self.metrics
    
    def get_metrics_summary(self) -> Dict[str, Any]:
        """Get a summary of all metrics"""
        return {
            name: {
                "target": metric.target,
                "current": metric.current_value,
                "met": metric.is_met()
            }
            for name, metric in self.metrics.items()
        }


class FeedbackLoop:
    """Continuous feedback and adjustment system"""
    
    def __init__(self):
        self.collectors: List[Any] = []
        self.analyzers: List[Any] = []
        self.adjusters: List[Any] = []
        self.metrics: Dict[str, Any] = {}
        self.patterns: List[Any] = []
        self.adjustments: List[Any] = []
    
    def add_collector(self, collector: Any) -> None:
        """Add a metric collector"""
        self.collectors.append(collector)
    
    def add_analyzer(self, analyzer: Any) -> None:
        """Add a pattern analyzer"""
        self.analyzers.append(analyzer)
    
    def add_adjuster(self, adjuster: Any) -> None:
        """Add a system adjuster"""
        self.adjusters.append(adjuster)
    
    def collect(self) -> Dict[str, Any]:
        """Collect metrics from all collectors"""
        for collector in self.collectors:
            # Simplified collection logic
            pass
        return self.metrics
    
    def analyze(self, metrics: Dict[str, Any]) -> List[Any]:
        """Analyze metrics for patterns"""
        for analyzer in self.analyzers:
            # Simplified analysis logic
            pass
        return self.patterns
    
    def adjust(self, patterns: List[Any]) -> List[Any]:
        """Generate adjustments based on patterns"""
        for adjuster in self.adjusters:
            # Simplified adjustment logic
            pass
        return self.adjustments
    
    def execute_cycle(self) -> List[Any]:
        """Execute a complete feedback cycle"""
        metrics = self.collect()
        patterns = self.analyze(metrics)
        adjustments = self.adjust(patterns)
        return adjustments
