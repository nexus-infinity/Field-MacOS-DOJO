/**
 * Prediction Buffer
 * 
 * Manages prefetched data based on predictions
 */

export interface PredictionEntry<T> {
  key: string;
  value: T;
  confidence: number;
  timestamp: number;
  used: boolean;
}

export class PredictionBuffer<T> {
  private buffer: Map<string, PredictionEntry<T>>;
  private maxSize: number;
  private ttl: number; // Time to live in milliseconds
  private stats: {
    prefetches: number;
    hits: number;
    misses: number;
  };
  
  constructor(maxSize: number = 100, ttl: number = 60000) {
    this.buffer = new Map();
    this.maxSize = maxSize;
    this.ttl = ttl;
    this.stats = {
      prefetches: 0,
      hits: 0,
      misses: 0
    };
  }
  
  /**
   * Add a prediction to the buffer
   */
  add(key: string, value: T, confidence: number): void {
    // Evict if at capacity
    if (this.buffer.size >= this.maxSize && !this.buffer.has(key)) {
      this.evictLowestConfidence();
    }
    
    this.buffer.set(key, {
      key,
      value,
      confidence,
      timestamp: Date.now(),
      used: false
    });
    
    this.stats.prefetches++;
  }
  
  /**
   * Get a prediction from the buffer
   */
  get(key: string): T | undefined {
    const entry = this.buffer.get(key);
    
    if (!entry) {
      this.stats.misses++;
      return undefined;
    }
    
    // Check if entry has expired
    if (Date.now() - entry.timestamp > this.ttl) {
      this.buffer.delete(key);
      this.stats.misses++;
      return undefined;
    }
    
    entry.used = true;
    this.stats.hits++;
    return entry.value;
  }
  
  /**
   * Check if a key exists in the buffer
   */
  has(key: string): boolean {
    const entry = this.buffer.get(key);
    if (!entry) return false;
    
    // Check expiration
    if (Date.now() - entry.timestamp > this.ttl) {
      this.buffer.delete(key);
      return false;
    }
    
    return true;
  }
  
  /**
   * Remove a prediction from the buffer
   */
  remove(key: string): void {
    this.buffer.delete(key);
  }
  
  /**
   * Clear the buffer
   */
  clear(): void {
    this.buffer.clear();
  }
  
  /**
   * Clean up expired entries
   */
  cleanup(): void {
    const now = Date.now();
    const toDelete: string[] = [];
    
    for (const [key, entry] of this.buffer.entries()) {
      if (now - entry.timestamp > this.ttl) {
        toDelete.push(key);
      }
    }
    
    for (const key of toDelete) {
      this.buffer.delete(key);
    }
  }
  
  /**
   * Get buffer statistics
   */
  getStats(): {
    size: number;
    prefetches: number;
    hits: number;
    misses: number;
    hitRate: number;
    utilizationRate: number;
  } {
    const total = this.stats.hits + this.stats.misses;
    const hitRate = total > 0 ? this.stats.hits / total : 0;
    
    const usedCount = Array.from(this.buffer.values())
      .filter(entry => entry.used).length;
    const utilizationRate = this.stats.prefetches > 0 
      ? usedCount / this.stats.prefetches 
      : 0;
    
    return {
      size: this.buffer.size,
      prefetches: this.stats.prefetches,
      hits: this.stats.hits,
      misses: this.stats.misses,
      hitRate,
      utilizationRate
    };
  }
  
  /**
   * Get all predictions sorted by confidence
   */
  getPredictions(): PredictionEntry<T>[] {
    return Array.from(this.buffer.values())
      .sort((a, b) => b.confidence - a.confidence);
  }
  
  /**
   * Evict entry with lowest confidence
   */
  private evictLowestConfidence(): void {
    let lowestKey: string | null = null;
    let lowestConfidence = Infinity;
    
    for (const [key, entry] of this.buffer.entries()) {
      if (entry.confidence < lowestConfidence) {
        lowestConfidence = entry.confidence;
        lowestKey = key;
      }
    }
    
    if (lowestKey) {
      this.buffer.delete(lowestKey);
    }
  }
}
