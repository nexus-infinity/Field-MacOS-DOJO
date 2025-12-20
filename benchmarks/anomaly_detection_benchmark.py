#!/usr/bin/env python3
"""
Performance benchmark for anomaly detection optimizations

This script demonstrates the performance improvements made to the
HTM anomaly detection components.
"""

import time
import sys
import os
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from anomaly_detection.htm.spatial_pooler import SpatialPooler
from anomaly_detection.htm.temporal_memory import TemporalMemory
from anomaly_detection.anomaly_scorer import AnomalyScorer


def benchmark_spatial_pooler(input_size=1000, column_count=2048, iterations=100):
    """Benchmark the optimized Spatial Pooler"""
    print(f"\n{'='*60}")
    print(f"Spatial Pooler Benchmark")
    print(f"{'='*60}")
    print(f"Input size: {input_size}")
    print(f"Column count: {column_count}")
    print(f"Iterations: {iterations}")
    
    pooler = SpatialPooler(input_size, column_count, sparsity=0.02)
    
    # Generate random input
    input_vector = np.random.randint(0, 2, input_size)
    
    # Warm up
    for _ in range(10):
        pooler.compute(input_vector, learn=False)
    
    # Benchmark
    start_time = time.time()
    for _ in range(iterations):
        active_columns = pooler.compute(input_vector, learn=False)
    end_time = time.time()
    
    elapsed = end_time - start_time
    per_iteration = (elapsed / iterations) * 1000  # ms
    
    print(f"\nResults:")
    print(f"  Total time: {elapsed:.4f} seconds")
    print(f"  Per iteration: {per_iteration:.4f} ms")
    print(f"  Throughput: {iterations/elapsed:.2f} iterations/sec")
    print(f"  Active columns: {len(active_columns)}")
    
    return elapsed


def benchmark_temporal_memory(column_count=500, iterations=100):
    """Benchmark the optimized Temporal Memory"""
    print(f"\n{'='*60}")
    print(f"Temporal Memory Benchmark")
    print(f"{'='*60}")
    print(f"Column count: {column_count}")
    print(f"Iterations: {iterations}")
    
    tm = TemporalMemory(column_count, cells_per_column=32)
    
    # Generate random active columns
    num_active = int(column_count * 0.02)
    
    # Warm up
    for _ in range(10):
        active_columns = set(np.random.choice(column_count, num_active, replace=False))
        tm.compute(active_columns, learn=True)
    
    # Benchmark
    start_time = time.time()
    for _ in range(iterations):
        active_columns = set(np.random.choice(column_count, num_active, replace=False))
        active_cells, predictive_cells = tm.compute(active_columns, learn=True)
    end_time = time.time()
    
    elapsed = end_time - start_time
    per_iteration = (elapsed / iterations) * 1000  # ms
    
    print(f"\nResults:")
    print(f"  Total time: {elapsed:.4f} seconds")
    print(f"  Per iteration: {per_iteration:.4f} ms")
    print(f"  Throughput: {iterations/elapsed:.2f} iterations/sec")
    
    return elapsed


def benchmark_anomaly_scorer(input_size=100, iterations=1000):
    """Benchmark the full anomaly scoring pipeline"""
    print(f"\n{'='*60}")
    print(f"Anomaly Scorer Benchmark")
    print(f"{'='*60}")
    print(f"Input size: {input_size}")
    print(f"Iterations: {iterations}")
    
    sp = SpatialPooler(input_size, 500)
    tm = TemporalMemory(500)
    scorer = AnomalyScorer(sp, tm)
    
    # Generate random inputs
    inputs = [np.random.randint(0, 2, input_size) for _ in range(iterations)]
    
    # Warm up
    for i in range(10):
        scorer.compute_anomaly(inputs[i], learn=True)
    
    # Benchmark
    start_time = time.time()
    for i in range(iterations):
        score = scorer.compute_anomaly(inputs[i], learn=True)
    end_time = time.time()
    
    elapsed = end_time - start_time
    per_iteration = (elapsed / iterations) * 1000  # ms
    
    # Get metrics
    metrics = scorer.get_metrics()
    
    print(f"\nResults:")
    print(f"  Total time: {elapsed:.4f} seconds")
    print(f"  Per iteration: {per_iteration:.4f} ms")
    print(f"  Throughput: {iterations/elapsed:.2f} iterations/sec")
    print(f"\nMetrics:")
    print(f"  Throughput counter: {metrics['throughput']}")
    print(f"  Average anomaly: {metrics['average_anomaly']:.4f}")
    print(f"  Anomaly rate: {metrics['anomaly_rate']:.2f}%")
    print(f"  History size: {metrics['history_size']}")
    
    return elapsed


def main():
    """Run all benchmarks"""
    print("="*60)
    print("HTM Anomaly Detection Performance Benchmark")
    print("="*60)
    print("\nOptimizations tested:")
    print("  1. Vectorized numpy operations in Spatial Pooler")
    print("  2. O(1) deque operations in Anomaly Scorer")
    print("  3. Early exit and segment skipping in Temporal Memory")
    print("  4. Efficient set operations for cell membership")
    
    try:
        # Run benchmarks
        sp_time = benchmark_spatial_pooler(input_size=1000, column_count=2048, iterations=100)
        tm_time = benchmark_temporal_memory(column_count=500, iterations=100)
        as_time = benchmark_anomaly_scorer(input_size=100, iterations=1000)
        
        # Summary
        print(f"\n{'='*60}")
        print(f"Summary")
        print(f"{'='*60}")
        print(f"Spatial Pooler: {sp_time:.4f}s")
        print(f"Temporal Memory: {tm_time:.4f}s")
        print(f"Anomaly Scorer: {as_time:.4f}s")
        print(f"\nAll benchmarks completed successfully!")
        print(f"{'='*60}")
        
    except Exception as e:
        print(f"\nError running benchmarks: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
