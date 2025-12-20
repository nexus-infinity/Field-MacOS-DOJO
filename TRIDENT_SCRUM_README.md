# Trident Scrum Methodology

An object-oriented sequential planning approach implementing the three-pronged Trident Scrum methodology with HTM (Hierarchical Temporal Memory) inspired features for the Field-MacOS-DOJO repository.

## Overview

The Trident Scrum methodology provides a structured approach to agile development with three integrated prongs:

1. **Build Pipeline (Prong Alpha)** - Feature development and implementation
2. **Test Harness (Prong Beta)** - Validation and quality assurance
3. **Learning Loop (Prong Gamma)** - Feedback integration and continuous improvement

## Architecture

### Core Components

```
trident_scrum/
├── core/
│   ├── sprint_trident.py      # Three-pronged sprint framework
│   └── feature_epic.py         # Epic and story management
├── sprints/
│   └── sprint_planning.py      # Sprint planning and execution
├── epics/
│   ├── anomaly_detection_epic.py
│   └── predictive_cache_epic.py
└── utils/
    └── metrics.py              # Velocity tracking and quality metrics
```

### HTM-Inspired Features

#### 1. Anomaly Detection Module

Located in `anomaly_detection/`, this module implements HTM-inspired anomaly detection:

- **SpatialPooler**: Converts input patterns into sparse distributed representations
- **TemporalMemory**: Learns sequences and temporal patterns
- **MQTT Stream Encoder**: Encodes MQTT messages for HTM processing
- **Anomaly Scorer**: Combines spatial and temporal analysis

**Acceptance Criteria:**
- Processes 1000 msg/sec
- Memory usage < 256MB
- Accuracy > 85%

#### 2. Predictive Cache System

Located in `predictive_cache/`, this TypeScript module provides intelligent caching:

- **HTMCache**: Main cache interface with pattern recognition
- **TemporalSequenceAnalyzer**: Analyzes access patterns
- **PredictionBuffer**: Prefetches data based on predictions

**Acceptance Criteria:**
- Cache hit ratio > 60%
- Prediction latency < 10ms
- Learning convergence < 500 iterations

## Usage

### Basic Sprint Setup

```python
from trident_scrum import SprintTrident, Sprint, Story, Task

# Create a sprint
sprint = Sprint(goal="Establish HTM foundation layers", capacity=40)

# Access the three prongs
build_pipeline = sprint.get_build_pipeline()
test_harness = sprint.get_test_harness()
learning_loop = sprint.get_learning_loop()

# Add features to build pipeline
build_pipeline.add_feature("Anomaly Detection")
build_pipeline.set_status("in_progress")

# Track tests
test_harness.add_test_suite("Unit Tests")
test_harness.update_coverage(85.0)
test_harness.set_tests_passing(True)

# Capture learning
learning_loop.capture_insight({
    "type": "performance",
    "description": "Optimized memory usage"
})
```

### Using Feature Epics

```python
from trident_scrum.epics import AnomalyDetectionEpic, PredictiveCacheEpic

# Create epics
anomaly_epic = AnomalyDetectionEpic()
cache_epic = PredictiveCacheEpic()

# Track progress
print(f"Anomaly Detection: {anomaly_epic.get_completion_percentage()}% complete")
print(f"Total points: {anomaly_epic.get_total_points()}")

# Complete stories
anomaly_epic.user_stories[0].complete()
```

### Sprint Planning

```python
from trident_scrum.sprints import Sprint, Deliverable, ExitCriteria, Phase

# Create sprint with deliverables
sprint = Sprint(goal="Core Implementation", capacity=40)

deliverable = Deliverable(
    artifact="temporal_monitor.py",
    repository="FIELD",
    acceptance_criteria=[
        "Processes 1000 msg/sec",
        "Memory < 256MB",
        "Accuracy > 85%"
    ]
)

sprint.add_deliverable(deliverable)

# Track velocity
story = Story(value="Implement SpatialPooler", points=8)
sprint.complete_story(story)

velocity = sprint.get_velocity()
utilization = sprint.get_capacity_utilization()
```

### Metrics and Tracking

```python
from trident_scrum.utils import VelocityTracker, QualityMetrics

# Track velocity over sprints
tracker = VelocityTracker()
velocity = tracker.calculate_velocity(sprint)
trend = tracker.get_trend()  # "improving", "stable", or "declining"

# Track quality metrics
quality = QualityMetrics()
quality.update_metric("code_coverage", 85.5)
quality.update_metric("defect_density", 0.08)

summary = quality.get_metrics_summary()
```

## HTM Anomaly Detection

### Using the Anomaly Detector

```python
import numpy as np
from anomaly_detection import SpatialPooler, TemporalMemory, AnomalyScorer

# Initialize components
sp = SpatialPooler(input_size=2048, column_count=2048, sparsity=0.02)
tm = TemporalMemory(column_count=2048, cells_per_column=32)
scorer = AnomalyScorer(sp, tm)

# Process data stream
input_vector = np.random.randint(0, 2, 2048)
anomaly_score = scorer.compute_anomaly(input_vector, learn=True)

if scorer.is_anomalous(anomaly_score):
    print(f"Anomaly detected! Score: {anomaly_score}")

# Get performance metrics
metrics = scorer.get_metrics()
print(f"Throughput: {metrics['throughput']} msg/sec")
print(f"Average anomaly: {metrics['average_anomaly']}")
```

### Using the MQTT Encoder

```python
from anomaly_detection.encoders import MQTTStreamEncoder

encoder = MQTTStreamEncoder(encoding_width=2048)

# Encode MQTT message
topic = "sensor/temperature/room1"
payload = '{"value": 23.5, "unit": "celsius"}'

encoding = encoder.encode_message_with_topic(topic, payload)
# Returns binary vector suitable for HTM processing
```

## Predictive Cache System

### Using the HTM Cache

```typescript
import { HTMCache } from './predictive_cache/src/htm-cache';

// Create cache
const cache = new HTMCache<string>(1000);

// Basic operations
cache.set('user:123', userData);
const data = cache.get('user:123');

// Get predictions
const predictions = cache.predictNext('user:123');
console.log('Predicted next accesses:', predictions);

// Get statistics
const stats = cache.getStats();
console.log(`Hit ratio: ${stats.hitRatio * 100}%`);
console.log(`Prediction accuracy: ${stats.predictionAccuracy * 100}%`);
```

### Using the Temporal Sequence Analyzer

```typescript
import { TemporalSequenceAnalyzer } from './predictive_cache/src/temporal-sequence-analyzer';

const analyzer = new TemporalSequenceAnalyzer(maxDepth: 5, minSupport: 2);

// Learn from access patterns
analyzer.learn(['page1', 'page2', 'page3']);
analyzer.learn(['page1', 'page2', 'page4']);

// Predict next accesses
const predictions = analyzer.predict(['page1', 'page2'], topK: 3);
const confidence = analyzer.getConfidence(['page1', 'page2'], 'page3');
```

## Testing

### Running Python Tests

```bash
# Run all Trident Scrum tests
python -m pytest tests/trident_scrum/

# Run specific test file
python -m pytest tests/trident_scrum/test_sprint_trident.py

# Run with coverage
python -m pytest tests/trident_scrum/ --cov=trident_scrum
```

### Running Anomaly Detection Tests

```bash
# Install dependencies
pip install numpy

# Run tests
python -m pytest tests/anomaly_detection/
```

### Running TypeScript Tests

```bash
# Install dependencies
npm install

# Run all tests
npm test

# Run specific test
npm test -- tests/predictive_cache/htm-cache.test.ts
```

## Sprint Execution Pipeline

```python
from collections import OrderedDict
from trident_scrum.sprints import ExecutionPipeline, Phase, ExitCriteria

pipeline = ExecutionPipeline()

# Phase 1: Foundation
pipeline.add_phase(Phase(
    name="Foundation",
    tasks=[
        "Setup HTM core libraries",
        "Create base encoder classes",
        "Establish test frameworks"
    ],
    exit_criteria=ExitCriteria(coverage=80, tests_passing=True)
))

# Phase 2: Feature Development
pipeline.add_phase(Phase(
    name="FeatureDevelopment",
    tasks=[
        "Implement anomaly detection",
        "Build predictive cache",
        "Create feedback mechanisms"
    ],
    exit_criteria=ExitCriteria(features_complete=True, integrated=True)
))

# Get current phase
current = pipeline.get_current_phase()
print(f"Working on: {current.name}")

# Track progress
completion = pipeline.get_completion_percentage()
print(f"Pipeline: {completion}% complete")
```

## Definition of Done

```python
from trident_scrum.sprints import DefinitionOfDone

dod = DefinitionOfDone()

# Default criteria:
# - code_complete: All code peer-reviewed and merged
# - tests_passing: Unit, integration, and performance tests green
# - documented: API docs and usage examples provided
# - deployed: Running in test environment
# - monitored: Metrics and alerts configured
# - learned: Retrospective insights captured

# Add custom criterion
dod.add_criterion("security_scan", "Security vulnerabilities addressed")
```

## Retrospectives

```python
from trident_scrum.sprints import SprintRetrospective

retro = SprintRetrospective(sprint)

# Capture insights
insights = retro.capture_insights()
print("What went well:", insights["what_went_well"])
print("What needs improvement:", insights["what_needs_improvement"])
print("Action items:", insights["action_items"])

# Apply to next sprint
next_sprint = Sprint(goal="Integration & Optimization", capacity=40)
retro.apply_to_next_sprint(next_sprint)
```

## Best Practices

1. **Start with Sprint Zero**: Use Sprint 0 to establish foundation and tooling
2. **Maintain Balance**: Keep all three prongs (Build, Test, Learn) active
3. **Track Velocity**: Use VelocityTracker to predict future capacity
4. **Define Clear Criteria**: Set explicit exit criteria for phases
5. **Learn Continuously**: Capture insights in the Learning Loop
6. **Measure Quality**: Track quality metrics alongside velocity
7. **Optimize Iteratively**: Use HTM predictions to improve efficiency

## Integration Points

### MQTT Bridge (FIELD ↔ DOJO)

```python
mqtt_bridge = Integration(
    source="FIELD.temporal_monitor",
    target="DOJO.predictive_cache",
    protocol="MQTT"
)
```

### Feedback Loop (DOJO → FIELD)

```python
feedback_loop = Integration(
    source="DOJO.cache_metrics",
    target="FIELD.anomaly_tuning",
    protocol="gRPC"
)
```

## Performance Targets

### Anomaly Detection
- **Throughput**: > 1000 messages/second
- **Memory**: < 256MB
- **Accuracy**: > 85%

### Predictive Cache
- **Hit Ratio**: > 60%
- **Latency**: < 10ms
- **Convergence**: < 500 iterations

## Contributing

When contributing to the Trident Scrum methodology:

1. Follow the three-pronged approach (Build, Test, Learn)
2. Add tests for all new functionality
3. Update documentation
4. Track metrics and performance
5. Capture learnings in retrospectives

## License

See LICENSE file for details.
