"""
Spatial Pooler implementation

Converts input patterns into sparse distributed representations
"""

from typing import List, Set
import numpy as np


class SpatialPooler:
    """
    Spatial Pooler for creating sparse distributed representations
    
    Inspired by HTM theory for spatial pattern learning
    """
    
    def __init__(self, input_size: int, column_count: int, sparsity: float = 0.02):
        """
        Initialize the Spatial Pooler
        
        Args:
            input_size: Size of input vector
            column_count: Number of columns in the pooler
            sparsity: Target sparsity level (percentage of active columns)
        """
        self.input_size = input_size
        self.column_count = column_count
        self.sparsity = sparsity
        self.active_columns_count = int(column_count * sparsity)
        
        # Initialize random synaptic connections
        self.connections = np.random.rand(column_count, input_size)
        self.permanences = np.random.uniform(0.3, 0.5, (column_count, input_size))
        
        # Learning parameters
        self.permanence_increment = 0.05
        self.permanence_decrement = 0.01
        self.connected_threshold = 0.5
    
    def compute(self, input_vector: np.ndarray, learn: bool = True) -> Set[int]:
        """
        Compute active columns for the given input
        
        Args:
            input_vector: Input bit array
            learn: Whether to apply learning
            
        Returns:
            Set of active column indices
        """
        # Calculate overlap scores
        overlaps = np.zeros(self.column_count)
        
        for col in range(self.column_count):
            connected = self.permanences[col] >= self.connected_threshold
            overlaps[col] = np.sum(input_vector * connected)
        
        # Select top-k columns with highest overlap
        active_columns = set(np.argsort(overlaps)[-self.active_columns_count:])
        
        # Apply learning if enabled
        if learn:
            self._learn(input_vector, active_columns)
        
        return active_columns
    
    def _learn(self, input_vector: np.ndarray, active_columns: Set[int]) -> None:
        """
        Update synaptic permanences based on active columns
        
        Args:
            input_vector: Input bit array
            active_columns: Set of active column indices
        """
        for col in active_columns:
            # Increase permanence for active inputs
            self.permanences[col] += input_vector * self.permanence_increment
            
            # Decrease permanence for inactive inputs
            self.permanences[col] -= (1 - input_vector) * self.permanence_decrement
            
            # Clip permanences to valid range
            self.permanences[col] = np.clip(self.permanences[col], 0.0, 1.0)
    
    def get_sparsity(self) -> float:
        """Get the configured sparsity level"""
        return self.sparsity
    
    def reset(self) -> None:
        """Reset the spatial pooler state"""
        self.permanences = np.random.uniform(0.3, 0.5, (self.column_count, self.input_size))
