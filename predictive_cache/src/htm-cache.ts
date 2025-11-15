/**
 * HTM Cache Interface
 * 
 * Defines the interface for Hierarchical Temporal Memory inspired caching
 */

export interface CacheEntry<T> {
  key: string;
  value: T;
  accessCount: number;
  lastAccessed: number;
  predicted: boolean;
}

export interface AccessPattern {
  sequence: string[];
  frequency: number;
  lastSeen: number;
}

export interface HTMCacheInterface<T> {
  /**
   * Get value from cache
   */
  get(key: string): T | undefined;
  
  /**
   * Set value in cache
   */
  set(key: string, value: T): void;
  
  /**
   * Check if key exists in cache
   */
  has(key: string): boolean;
  
  /**
   * Clear cache
   */
  clear(): void;
  
  /**
   * Get cache statistics
   */
  getStats(): CacheStats;
  
  /**
   * Predict next likely accesses
   */
  predictNext(currentKey: string): string[];
}

export interface CacheStats {
  hits: number;
  misses: number;
  hitRatio: number;
  size: number;
  predictions: number;
  predictionAccuracy: number;
}

export class HTMCache<T> implements HTMCacheInterface<T> {
  private cache: Map<string, CacheEntry<T>>;
  private maxSize: number;
  private accessHistory: string[];
  private patterns: Map<string, AccessPattern>;
  private stats: {
    hits: number;
    misses: number;
    predictions: number;
    correctPredictions: number;
  };
  
  constructor(maxSize: number = 1000) {
    this.cache = new Map();
    this.maxSize = maxSize;
    this.accessHistory = [];
    this.patterns = new Map();
    this.stats = {
      hits: 0,
      misses: 0,
      predictions: 0,
      correctPredictions: 0
    };
  }
  
  get(key: string): T | undefined {
    const entry = this.cache.get(key);
    
    if (entry) {
      this.stats.hits++;
      entry.accessCount++;
      entry.lastAccessed = Date.now();
      
      // Track access for pattern learning
      this.recordAccess(key);
      
      // Check if this was predicted
      if (entry.predicted) {
        this.stats.correctPredictions++;
        entry.predicted = false;
      }
      
      return entry.value;
    }
    
    this.stats.misses++;
    this.recordAccess(key);
    return undefined;
  }
  
  set(key: string, value: T): void {
    // Evict if at capacity
    if (this.cache.size >= this.maxSize && !this.cache.has(key)) {
      this.evict();
    }
    
    this.cache.set(key, {
      key,
      value,
      accessCount: 0,
      lastAccessed: Date.now(),
      predicted: false
    });
  }
  
  has(key: string): boolean {
    return this.cache.has(key);
  }
  
  clear(): void {
    this.cache.clear();
    this.accessHistory = [];
    this.patterns.clear();
  }
  
  getStats(): CacheStats {
    const total = this.stats.hits + this.stats.misses;
    const hitRatio = total > 0 ? this.stats.hits / total : 0;
    const predictionAccuracy = this.stats.predictions > 0 
      ? this.stats.correctPredictions / this.stats.predictions 
      : 0;
    
    return {
      hits: this.stats.hits,
      misses: this.stats.misses,
      hitRatio,
      size: this.cache.size,
      predictions: this.stats.predictions,
      predictionAccuracy
    };
  }
  
  predictNext(currentKey: string): string[] {
    const predictions: string[] = [];
    
    // Look for patterns that start with current key
    for (const [seq, pattern] of this.patterns.entries()) {
      const seqArray = seq.split(',');
      const currentIndex = seqArray.indexOf(currentKey);
      
      if (currentIndex >= 0 && currentIndex < seqArray.length - 1) {
        const nextKey = seqArray[currentIndex + 1];
        predictions.push(nextKey);
        
        // Mark as predicted for accuracy tracking
        const entry = this.cache.get(nextKey);
        if (entry) {
          entry.predicted = true;
          this.stats.predictions++;
        }
      }
    }
    
    return predictions;
  }
  
  private recordAccess(key: string): void {
    this.accessHistory.push(key);
    
    // Keep history window manageable
    if (this.accessHistory.length > 100) {
      this.accessHistory.shift();
    }
    
    // Learn patterns from recent history
    this.learnPatterns();
  }
  
  private learnPatterns(): void {
    const windowSize = 3;
    
    if (this.accessHistory.length < windowSize) {
      return;
    }
    
    // Extract sequence patterns
    for (let i = 0; i <= this.accessHistory.length - windowSize; i++) {
      const sequence = this.accessHistory.slice(i, i + windowSize);
      const seqKey = sequence.join(',');
      
      const existing = this.patterns.get(seqKey);
      if (existing) {
        existing.frequency++;
        existing.lastSeen = Date.now();
      } else {
        this.patterns.set(seqKey, {
          sequence,
          frequency: 1,
          lastSeen: Date.now()
        });
      }
    }
    
    // Prune old patterns
    const now = Date.now();
    const maxAge = 3600000; // 1 hour
    
    for (const [key, pattern] of this.patterns.entries()) {
      if (now - pattern.lastSeen > maxAge) {
        this.patterns.delete(key);
      }
    }
  }
  
  private evict(): void {
    // Evict least recently used entry
    let lruKey: string | null = null;
    let lruTime = Infinity;
    
    for (const [key, entry] of this.cache.entries()) {
      if (entry.lastAccessed < lruTime) {
        lruTime = entry.lastAccessed;
        lruKey = key;
      }
    }
    
    if (lruKey) {
      this.cache.delete(lruKey);
    }
  }
}
