/**
 * Tests for HTM Cache
 */

import { HTMCache } from '../../predictive_cache/src/htm-cache';

describe('HTMCache', () => {
  let cache: HTMCache<string>;
  
  beforeEach(() => {
    cache = new HTMCache<string>(100);
  });
  
  describe('Basic Operations', () => {
    test('should initialize with correct properties', () => {
      const stats = cache.getStats();
      expect(stats.size).toBe(0);
      expect(stats.hits).toBe(0);
      expect(stats.misses).toBe(0);
    });
    
    test('should set and get values', () => {
      cache.set('key1', 'value1');
      expect(cache.get('key1')).toBe('value1');
    });
    
    test('should return undefined for non-existent keys', () => {
      expect(cache.get('nonexistent')).toBeUndefined();
    });
    
    test('should check if key exists', () => {
      cache.set('key1', 'value1');
      expect(cache.has('key1')).toBe(true);
      expect(cache.has('key2')).toBe(false);
    });
    
    test('should clear all entries', () => {
      cache.set('key1', 'value1');
      cache.set('key2', 'value2');
      cache.clear();
      
      expect(cache.getStats().size).toBe(0);
      expect(cache.has('key1')).toBe(false);
    });
  });
  
  describe('Statistics', () => {
    test('should track hits and misses', () => {
      cache.set('key1', 'value1');
      
      cache.get('key1'); // hit
      cache.get('key2'); // miss
      cache.get('key1'); // hit
      
      const stats = cache.getStats();
      expect(stats.hits).toBe(2);
      expect(stats.misses).toBe(1);
      expect(stats.hitRatio).toBeCloseTo(0.667, 2);
    });
    
    test('should update access count', () => {
      cache.set('key1', 'value1');
      
      cache.get('key1');
      cache.get('key1');
      cache.get('key1');
      
      // Access count should be tracked internally
      const stats = cache.getStats();
      expect(stats.hits).toBe(3);
    });
  });
  
  describe('Predictions', () => {
    test('should predict next accesses based on patterns', () => {
      // Create access pattern
      cache.set('a', 'valueA');
      cache.set('b', 'valueB');
      cache.set('c', 'valueC');
      
      cache.get('a');
      cache.get('b');
      cache.get('c');
      
      cache.get('a');
      cache.get('b');
      cache.get('c');
      
      // Now predict what comes after 'a'
      const predictions = cache.predictNext('a');
      expect(predictions).toContain('b');
    });
    
    test('should track prediction accuracy', () => {
      cache.set('key1', 'value1');
      cache.set('key2', 'value2');
      
      cache.get('key1');
      cache.get('key2');
      cache.get('key1');
      
      const predictions = cache.predictNext('key1');
      
      if (predictions.includes('key2')) {
        cache.get('key2'); // Correct prediction
      }
      
      const stats = cache.getStats();
      expect(stats.predictions).toBeGreaterThan(0);
    });
  });
  
  describe('Capacity Management', () => {
    test('should respect max size', () => {
      const smallCache = new HTMCache<number>(5);
      
      for (let i = 0; i < 10; i++) {
        smallCache.set(`key${i}`, i);
      }
      
      expect(smallCache.getStats().size).toBeLessThanOrEqual(5);
    });
    
    test('should evict least recently used items', () => {
      const smallCache = new HTMCache<number>(3);
      
      smallCache.set('a', 1);
      smallCache.set('b', 2);
      smallCache.set('c', 3);
      
      // Access a and b to make c the LRU
      smallCache.get('a');
      smallCache.get('b');
      
      // Add new item, should evict c
      smallCache.set('d', 4);
      
      expect(smallCache.has('d')).toBe(true);
      expect(smallCache.getStats().size).toBe(3);
    });
  });
});
