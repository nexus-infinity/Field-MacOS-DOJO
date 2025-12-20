"""
Anomaly Scoring Algorithm

Combines spatial and temporal anomaly scores to detect anomalies
"""

from typing import List, Tuple
from collections import deque
import numpy as np
from .htm.spatial_pooler import SpatialPooler
from .htm.temporal_memory import TemporalMemory


class AnomalyScorer:
    """
    Anomaly scoring algorithm combining spatial and temporal analysis
    """
    
    def __init__(self, spatial_pooler: SpatialPooler, temporal_memory: TemporalMemory):
        """
        Initialize Anomaly Scorer
        
        Args:
            spatial_pooler: SpatialPooler instance
            temporal_memory: TemporalMemory instance
        """
        self.spatial_pooler = spatial_pooler
        self.temporal_memory = temporal_memory
        
        # Scoring parameters
        self.history_window = 100
        self.anomaly_threshold = 0.7
        
        # Tracking - using deque for O(1) append and popleft operations
        self.anomaly_scores: deque = deque(maxlen=self.history_window)
        self.throughput_counter = 0
        self.memory_usage_mb = 0.0
    
    def compute_anomaly(self, input_vector: np.ndarray, learn: bool = True) -> float:
        """
        Compute anomaly score for input vector
        
        Args:
            input_vector: Input binary vector
            learn: Whether to apply learning
            
        Returns:
            Anomaly score between 0 (normal) and 1 (anomalous)
        """
        # Spatial processing
        active_columns = self.spatial_pooler.compute(input_vector, learn=learn)
        
        # Temporal processing
        active_cells, predictive_cells = self.temporal_memory.compute(active_columns, learn=learn)
        
        # Calculate anomaly score
        anomaly_score = self.temporal_memory.get_anomaly_score()
        
        # Track score - deque automatically maintains maxlen
        self.anomaly_scores.append(anomaly_score)
        
        # Update throughput counter
        self.throughput_counter += 1
        
        return anomaly_score
    
    def is_anomalous(self, score: float) -> bool:
        """
        Determine if a score indicates an anomaly
        
        Args:
            score: Anomaly score
            
        Returns:
            True if anomalous, False otherwise
        """
        return score >= self.anomaly_threshold
    
    def get_average_anomaly(self) -> float:
        """
        Get average anomaly score over history window
        
        Returns:
            Average anomaly score
        """
        if not self.anomaly_scores:
            return 0.0
        return np.mean(self.anomaly_scores)
    
    def get_anomaly_rate(self) -> float:
        """
        Get rate of anomalies in history window
        
        Returns:
            Percentage of anomalous scores
        """
        if not self.anomaly_scores:
            return 0.0
        # Convert to numpy array for faster comparison
        scores_array = np.array(self.anomaly_scores)
        anomalous = np.sum(scores_array >= self.anomaly_threshold)
        return (anomalous / len(self.anomaly_scores)) * 100
    
    def reset(self) -> None:
        """Reset anomaly scorer state"""
        self.spatial_pooler.reset()
        self.temporal_memory.reset()
        self.anomaly_scores.clear()
        self.throughput_counter = 0
    
    def get_metrics(self) -> dict:
        """
        Get performance metrics
        
        Returns:
            Dictionary of metrics
        """
        return {
            "throughput": self.throughput_counter,
            "memory_usage_mb": self.memory_usage_mb,
            "average_anomaly": self.get_average_anomaly(),
            "anomaly_rate": self.get_anomaly_rate(),
            "history_size": len(self.anomaly_scores)
        }
    
    def set_threshold(self, threshold: float) -> None:
        """
        Set anomaly detection threshold
        
        Args:
            threshold: New threshold value (0-1)
        """
        self.anomaly_threshold = max(0.0, min(1.0, threshold))
