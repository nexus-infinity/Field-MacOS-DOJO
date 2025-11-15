#!/usr/bin/env python3
"""
Example: Using Trident Scrum for Sprint Planning

This example demonstrates how to use the Trident Scrum methodology
to plan and execute a sprint with the three-pronged approach.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from trident_scrum import (
    Sprint, Story, Task, Deliverable, 
    VelocityTracker, SprintRetrospective
)
from trident_scrum.epics import AnomalyDetectionEpic, PredictiveCacheEpic


def main():
    print("=" * 70)
    print("TRIDENT SCRUM SPRINT PLANNING EXAMPLE")
    print("=" * 70)
    print()
    
    # Create Sprint 1: Core Implementation
    sprint1 = Sprint(
        goal="Establish HTM foundation layers",
        capacity=40
    )
    
    print(f"Sprint 1 Goal: {sprint1.goal}")
    print(f"Capacity: {sprint1.capacity} story points")
    print()
    
    # Setup the three prongs
    print("Initializing Three Prongs:")
    print("-" * 70)
    
    # Prong Alpha: Build Pipeline
    build = sprint1.get_build_pipeline()
    build.add_feature("HTM Spatial Pooler")
    build.add_feature("Temporal Memory Module")
    build.add_feature("MQTT Stream Encoder")
    build.set_status("in_progress")
    print(f"✓ Prong Alpha (Build): {len(build.features)} features added")
    
    # Prong Beta: Test Harness
    test = sprint1.get_test_harness()
    test.add_test_suite("Unit Tests")
    test.add_test_suite("Integration Tests")
    test.add_test_suite("Performance Tests")
    test.update_coverage(85.5)
    test.set_tests_passing(True)
    print(f"✓ Prong Beta (Test): {len(test.test_suites)} test suites, {test.coverage}% coverage")
    
    # Prong Gamma: Learning Loop
    learn = sprint1.get_learning_loop()
    learn.capture_insight({
        "type": "performance",
        "description": "HTM performs well with sparse data"
    })
    learn.add_action_item("Document HTM parameter tuning")
    print(f"✓ Prong Gamma (Learn): {len(learn.insights)} insights captured")
    print()
    
    # Add deliverables
    print("Sprint Deliverables:")
    print("-" * 70)
    
    deliverable1 = Deliverable(
        artifact="temporal_monitor.py",
        repository="FIELD",
        acceptance_criteria=[
            "Processes 1000 msg/sec",
            "Memory < 256MB",
            "Accuracy > 85%"
        ]
    )
    sprint1.add_deliverable(deliverable1)
    print(f"✓ {deliverable1.artifact} ({deliverable1.repository})")
    for criterion in deliverable1.acceptance_criteria:
        print(f"  - {criterion}")
    print()
    
    # Use Feature Epics
    print("Feature Epics:")
    print("-" * 70)
    
    anomaly_epic = AnomalyDetectionEpic()
    cache_epic = PredictiveCacheEpic()
    
    print(f"1. {anomaly_epic.name}")
    print(f"   Total Points: {anomaly_epic.get_total_points()}")
    print(f"   User Stories: {len(anomaly_epic.user_stories)}")
    print(f"   Tasks: {len(anomaly_epic.tasks)}")
    print()
    
    print(f"2. {cache_epic.name}")
    print(f"   Total Points: {cache_epic.get_total_points()}")
    print(f"   User Stories: {len(cache_epic.user_stories)}")
    print(f"   Tasks: {len(cache_epic.tasks)}")
    print()
    
    # Complete some stories
    print("Completing User Stories:")
    print("-" * 70)
    
    for i, story in enumerate(anomaly_epic.user_stories[:2], 1):
        story.complete()
        sprint1.complete_story(story)
        print(f"✓ Story {i}: {story.points} points")
    
    print()
    print(f"Sprint Velocity: {sprint1.get_velocity()} points")
    print(f"Capacity Utilization: {sprint1.get_capacity_utilization():.1f}%")
    print(f"Epic Completion: {anomaly_epic.get_completion_percentage():.1f}%")
    print()
    
    # Health Status
    print("Sprint Health Status:")
    print("-" * 70)
    
    health = sprint1.get_health_status()
    print(f"Build Status: {health['build']['status']}")
    print(f"Features: {health['build']['features']}")
    print(f"Test Coverage: {health['test']['coverage']}%")
    print(f"Tests Passing: {health['test']['passing']}")
    print(f"Insights: {health['learn']['insights']}")
    print(f"Action Items: {health['learn']['actions']}")
    print()
    
    # Velocity Tracking
    print("Velocity Tracking:")
    print("-" * 70)
    
    tracker = VelocityTracker()
    velocity = tracker.calculate_velocity(sprint1)
    print(f"Sprint 1 Velocity: {velocity} points")
    print(f"Rolling Average: {tracker.get_rolling_average():.1f} points")
    print()
    
    # Sprint Retrospective
    print("Sprint Retrospective:")
    print("-" * 70)
    
    retro = SprintRetrospective(sprint1)
    insights = retro.capture_insights()
    
    print("What went well:")
    for item in insights["what_went_well"]:
        print(f"  ✓ {item}")
    
    print("\nWhat needs improvement:")
    for item in insights["what_needs_improvement"]:
        print(f"  → {item}")
    
    print()
    print("=" * 70)
    print("SPRINT PLANNING COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
