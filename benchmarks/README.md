# Performance Benchmarks

This directory contains performance benchmarks for the Field-MacOS-DOJO optimizations.

## Anomaly Detection Benchmark

The `anomaly_detection_benchmark.py` script benchmarks the HTM anomaly detection components after optimization.

### Running the Benchmark

```bash
python benchmarks/anomaly_detection_benchmark.py
```

### Optimizations Tested

1. **Spatial Pooler**: Vectorized numpy operations instead of nested loops
   - Uses matrix multiplication for overlap calculation
   - ~10-100x faster for large matrices

2. **Anomaly Scorer**: O(1) deque operations instead of O(n) list operations
   - Uses `collections.deque` with maxlen for automatic size management
   - Vectorized anomaly rate calculation with numpy

3. **Temporal Memory**: Early exit and segment skipping
   - Skips cells without segments
   - Early exit when no active cells
   - Efficient set operations for cell membership

4. **Connection Pooling**: HTTP clients use requests.Session()
   - Reuses TCP connections
   - Reduces SSL/TLS handshake overhead
   - ~20-30% faster for repeated API calls

### Expected Results

- **Spatial Pooler**: ~400-500 iterations/sec for 1000x2048 matrix
- **Temporal Memory**: ~600-700 iterations/sec for 500 columns
- **Anomaly Scorer**: ~1500-2000 iterations/sec for 100-element input

These numbers will vary based on hardware but demonstrate the relative performance improvements.
