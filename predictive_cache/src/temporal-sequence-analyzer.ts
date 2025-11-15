/**
 * Temporal Sequence Analyzer
 * 
 * Analyzes temporal sequences to predict future access patterns
 */

export interface SequenceNode {
  key: string;
  count: number;
  next: Map<string, SequenceNode>;
}

export class TemporalSequenceAnalyzer {
  private root: Map<string, SequenceNode>;
  private maxDepth: number;
  private minSupport: number;
  
  constructor(maxDepth: number = 5, minSupport: number = 2) {
    this.root = new Map();
    this.maxDepth = maxDepth;
    this.minSupport = minSupport;
  }
  
  /**
   * Learn from an access sequence
   */
  learn(sequence: string[]): void {
    for (let i = 0; i < sequence.length; i++) {
      const subseq = sequence.slice(i, Math.min(i + this.maxDepth, sequence.length));
      this.addSequence(subseq);
    }
  }
  
  /**
   * Predict next items based on current sequence
   */
  predict(recentSequence: string[], topK: number = 3): string[] {
    const predictions: Map<string, number> = new Map();
    
    // Try different sequence lengths
    for (let len = Math.min(recentSequence.length, this.maxDepth); len > 0; len--) {
      const subseq = recentSequence.slice(-len);
      const nextItems = this.getNextItems(subseq);
      
      for (const [item, count] of nextItems.entries()) {
        predictions.set(item, (predictions.get(item) || 0) + count * len);
      }
    }
    
    // Sort by score and return top K
    return Array.from(predictions.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, topK)
      .map(([item]) => item);
  }
  
  /**
   * Get confidence score for a prediction
   */
  getConfidence(sequence: string[], nextItem: string): number {
    const node = this.findNode(sequence);
    if (!node) return 0;
    
    const nextNode = node.next.get(nextItem);
    if (!nextNode) return 0;
    
    const totalCount = Array.from(node.next.values())
      .reduce((sum, n) => sum + n.count, 0);
    
    return totalCount > 0 ? nextNode.count / totalCount : 0;
  }
  
  /**
   * Clear learned sequences
   */
  clear(): void {
    this.root.clear();
  }
  
  /**
   * Get statistics about learned patterns
   */
  getStats(): {
    totalPatterns: number;
    averageDepth: number;
    maxCount: number;
  } {
    let totalPatterns = 0;
    let totalDepth = 0;
    let maxCount = 0;
    
    const traverse = (node: SequenceNode, depth: number) => {
      totalPatterns++;
      totalDepth += depth;
      maxCount = Math.max(maxCount, node.count);
      
      for (const child of node.next.values()) {
        traverse(child, depth + 1);
      }
    };
    
    for (const node of this.root.values()) {
      traverse(node, 1);
    }
    
    return {
      totalPatterns,
      averageDepth: totalPatterns > 0 ? totalDepth / totalPatterns : 0,
      maxCount
    };
  }
  
  private addSequence(sequence: string[]): void {
    if (sequence.length === 0) return;
    
    const firstKey = sequence[0];
    let node = this.root.get(firstKey);
    
    if (!node) {
      node = { key: firstKey, count: 0, next: new Map() };
      this.root.set(firstKey, node);
    }
    
    node.count++;
    
    // Add remaining items
    let current = node;
    for (let i = 1; i < sequence.length; i++) {
      const key = sequence[i];
      let nextNode = current.next.get(key);
      
      if (!nextNode) {
        nextNode = { key, count: 0, next: new Map() };
        current.next.set(key, nextNode);
      }
      
      nextNode.count++;
      current = nextNode;
    }
  }
  
  private findNode(sequence: string[]): SequenceNode | null {
    if (sequence.length === 0) return null;
    
    let node = this.root.get(sequence[0]);
    if (!node) return null;
    
    for (let i = 1; i < sequence.length; i++) {
      node = node.next.get(sequence[i]) || null;
      if (!node) return null;
    }
    
    return node;
  }
  
  private getNextItems(sequence: string[]): Map<string, number> {
    const result = new Map<string, number>();
    const node = this.findNode(sequence);
    
    if (node) {
      for (const [key, nextNode] of node.next.entries()) {
        if (nextNode.count >= this.minSupport) {
          result.set(key, nextNode.count);
        }
      }
    }
    
    return result;
  }
}
