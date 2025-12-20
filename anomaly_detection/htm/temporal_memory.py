"""
Temporal Memory implementation

Learns sequences and temporal patterns in data
"""

from typing import List, Set, Dict, Tuple
from collections import defaultdict


class Cell:
    """Represents a single cell in a column"""
    
    def __init__(self, column_idx: int, cell_idx: int):
        self.column_idx = column_idx
        self.cell_idx = cell_idx
        self.segments: List['Segment'] = []
    
    def __hash__(self):
        return hash((self.column_idx, self.cell_idx))
    
    def __eq__(self, other):
        return (self.column_idx, self.cell_idx) == (other.column_idx, other.cell_idx)


class Segment:
    """Represents a dendritic segment"""
    
    def __init__(self):
        self.synapses: Dict[Cell, float] = {}
    
    def add_synapse(self, cell: Cell, permanence: float = 0.5) -> None:
        """Add a synapse to another cell"""
        self.synapses[cell] = permanence


class TemporalMemory:
    """
    Temporal Memory for learning temporal sequences
    
    Inspired by HTM theory for temporal pattern learning
    """
    
    def __init__(self, column_count: int, cells_per_column: int = 32):
        """
        Initialize Temporal Memory
        
        Args:
            column_count: Number of columns
            cells_per_column: Number of cells per column
        """
        self.column_count = column_count
        self.cells_per_column = cells_per_column
        
        # Initialize cells
        self.cells: List[List[Cell]] = []
        for col in range(column_count):
            column_cells = []
            for cell_idx in range(cells_per_column):
                column_cells.append(Cell(col, cell_idx))
            self.cells.append(column_cells)
        
        # State tracking
        self.active_cells: Set[Cell] = set()
        self.predictive_cells: Set[Cell] = set()
        self.winner_cells: Set[Cell] = set()
        
        # Learning parameters
        self.permanence_increment = 0.1
        self.permanence_decrement = 0.05
        self.connected_threshold = 0.5
        self.activation_threshold = 13
    
    def compute(self, active_columns: Set[int], learn: bool = True) -> Tuple[Set[Cell], Set[Cell]]:
        """
        Compute active and predictive cells for the given active columns
        
        Args:
            active_columns: Set of active column indices
            learn: Whether to apply learning
            
        Returns:
            Tuple of (active_cells, predictive_cells)
        """
        prev_predictive = self.predictive_cells.copy()
        prev_active = self.active_cells.copy()
        
        # Reset state
        self.active_cells = set()
        self.winner_cells = set()
        
        # Activate cells
        for col in active_columns:
            # Check if any cells in column were predicted
            predicted_cells = [cell for cell in self.cells[col] if cell in prev_predictive]
            
            if predicted_cells:
                # Activate predicted cells
                for cell in predicted_cells:
                    self.active_cells.add(cell)
                    self.winner_cells.add(cell)
            else:
                # Burst the column - activate all cells
                for cell in self.cells[col]:
                    self.active_cells.add(cell)
                # Pick a winner cell (first cell for simplicity)
                self.winner_cells.add(self.cells[col][0])
        
        # Compute predictions for next time step
        self.predictive_cells = self._compute_predictive_cells()
        
        # Apply learning if enabled
        if learn:
            self._learn(prev_active, self.winner_cells)
        
        return self.active_cells, self.predictive_cells
    
    def _compute_predictive_cells(self) -> Set[Cell]:
        """
        Compute cells that are predictive based on current active cells
        
        Returns:
            Set of predictive cells
        """
        predictive = set()
        
        # Early exit if no active cells
        if not self.active_cells:
            return predictive
        
        # Iterate through cells with segments
        for col_cells in self.cells:
            for cell in col_cells:
                # Skip cells without segments for efficiency
                if not cell.segments:
                    continue
                    
                for segment in cell.segments:
                    # Count active synapses efficiently using set intersection
                    active_connected_synapses = sum(
                        1 for syn_cell, perm in segment.synapses.items()
                        if perm >= self.connected_threshold and syn_cell in self.active_cells
                    )
                    if active_connected_synapses >= self.activation_threshold:
                        predictive.add(cell)
                        break  # Found one active segment, no need to check others
        
        return predictive
    
    def _learn(self, prev_active_cells: Set[Cell], winner_cells: Set[Cell]) -> None:
        """
        Update synaptic connections based on learning
        
        Args:
            prev_active_cells: Previously active cells
            winner_cells: Winner cells from current computation
        """
        # Simplified learning: add segments to winner cells
        for cell in winner_cells:
            if not cell.segments and prev_active_cells:
                segment = Segment()
                for prev_cell in list(prev_active_cells)[:15]:  # Connect to subset
                    segment.add_synapse(prev_cell, permanence=0.6)
                cell.segments.append(segment)
    
    def reset(self) -> None:
        """Reset temporal memory state"""
        self.active_cells = set()
        self.predictive_cells = set()
        self.winner_cells = set()
    
    def get_anomaly_score(self) -> float:
        """
        Calculate anomaly score based on prediction accuracy
        
        Returns:
            Anomaly score between 0 and 1
        """
        if not self.active_cells:
            return 0.0
        
        # Calculate how many active cells were predicted
        predicted_active = len(self.active_cells & self.predictive_cells)
        total_active = len(self.active_cells)
        
        # Anomaly is proportion of unpredicted active cells
        return 1.0 - (predicted_active / total_active) if total_active > 0 else 0.0
