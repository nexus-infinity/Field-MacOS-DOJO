"""
MQTT Stream Encoder

Encodes MQTT message streams into binary representations for HTM processing
"""

from typing import Dict, Any, List
import json
import hashlib


class MQTTStreamEncoder:
    """
    Encoder for MQTT message streams
    
    Converts MQTT messages into sparse binary vectors suitable for HTM processing
    """
    
    def __init__(self, encoding_width: int = 2048, max_value: float = 1000.0):
        """
        Initialize MQTT Stream Encoder
        
        Args:
            encoding_width: Width of the encoded binary vector
            max_value: Maximum expected numeric value for normalization
        """
        self.encoding_width = encoding_width
        self.max_value = max_value
        self.field_indices: Dict[str, int] = {}
        self.next_index = 0
    
    def encode(self, message: Dict[str, Any]) -> List[int]:
        """
        Encode an MQTT message into a binary vector
        
        Args:
            message: MQTT message as a dictionary
            
        Returns:
            Binary vector as list of integers (0 or 1)
        """
        encoding = [0] * self.encoding_width
        
        # Flatten the message structure
        flat_message = self._flatten_dict(message)
        
        for key, value in flat_message.items():
            # Get or create index for this field
            if key not in self.field_indices:
                self.field_indices[key] = self.next_index % self.encoding_width
                self.next_index += 100  # Spread out encodings
            
            base_idx = self.field_indices[key]
            
            # Encode based on value type
            if isinstance(value, (int, float)):
                # Numeric encoding: use multiple bits based on value
                normalized = min(value / self.max_value, 1.0)
                active_bits = int(normalized * 20)  # Use up to 20 bits
                
                for i in range(active_bits):
                    idx = (base_idx + i) % self.encoding_width
                    encoding[idx] = 1
            
            elif isinstance(value, str):
                # String encoding: use hash to determine active bits
                hash_val = int(hashlib.md5(value.encode()).hexdigest(), 16)
                
                for i in range(10):  # Use 10 bits for string
                    if hash_val & (1 << i):
                        idx = (base_idx + i) % self.encoding_width
                        encoding[idx] = 1
            
            elif isinstance(value, bool):
                # Boolean encoding: single bit
                if value:
                    encoding[base_idx % self.encoding_width] = 1
        
        return encoding
    
    def _flatten_dict(self, d: Dict[str, Any], parent_key: str = '') -> Dict[str, Any]:
        """
        Flatten nested dictionary structure
        
        Args:
            d: Dictionary to flatten
            parent_key: Parent key for nested items
            
        Returns:
            Flattened dictionary
        """
        items = []
        
        for k, v in d.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key).items())
            elif isinstance(v, list):
                # Encode lists as their length and first few items
                items.append((f"{new_key}.length", len(v)))
                for i, item in enumerate(v[:3]):  # Only first 3 items
                    if isinstance(item, (int, float, str, bool)):
                        items.append((f"{new_key}.{i}", item))
            else:
                items.append((new_key, v))
        
        return dict(items)
    
    def decode_topic(self, topic: str) -> Dict[str, str]:
        """
        Parse MQTT topic into components
        
        Args:
            topic: MQTT topic string (e.g., "sensor/temperature/room1")
            
        Returns:
            Dictionary of topic components
        """
        parts = topic.split('/')
        return {
            f"topic_level_{i}": part
            for i, part in enumerate(parts)
        }
    
    def encode_message_with_topic(self, topic: str, payload: str) -> List[int]:
        """
        Encode complete MQTT message (topic + payload)
        
        Args:
            topic: MQTT topic
            payload: Message payload (JSON string or plain string)
            
        Returns:
            Binary vector encoding
        """
        # Parse topic
        topic_parts = self.decode_topic(topic)
        
        # Parse payload
        try:
            payload_data = json.loads(payload)
        except (json.JSONDecodeError, TypeError):
            payload_data = {"value": payload}
        
        # Combine topic and payload
        message = {**topic_parts, **payload_data}
        
        return self.encode(message)
    
    def reset(self) -> None:
        """Reset encoder state"""
        self.field_indices = {}
        self.next_index = 0
