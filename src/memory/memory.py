"""
Conversation memory management
"""

from typing import List, Dict, Optional
from collections import deque


class ConversationMemory:
    """Manages conversation history with a fixed-size retailer"""
    
    def __init__(self, max_size: int = 100):
        """
        Initialize conversation memory
        
        Args:
            max_size: Maximum number of conversation turns to remember
        """
        self.max_size = max_size
        self.messages = deque(maxlen=max_size)
    
    def add_message(self, role: str, content: str):
        """
        Add a message to the conversation history
        
        Args:
            role: Role of the speaker ('user' or 'assistant')
            content: Message content
        """
        self.messages.append({
            "role": role,
            "content": content
        })
    
    def get_history(self, n: Optional[int] = None) -> List[Dict[str, str]]:
        """
        Get conversation history
        
        Args:
            n: Number of most recent messages to return. If None, returns all.
            
        Returns:
            List of message dictionaries
        """
        if n is None:
            return list(self.messages)
        return list(self.messages)[-n:]
    
    def clear(self):
        """Clear all conversation history"""
        self.messages.clear()
    
    def get_last_n_exchanges(self, n: int = 5) -> List[Dict[str, str]]:
        """
        Get last N conversation exchanges (user + assistant pairs)
        
        Args:
            n: Number of exchanges to return
            
        Returns:
            List of exchanges
        """
        messages = list(self.messages)
        exchanges = []
        
        i = len(messages) - 1
        while i >= 0 and len(exchanges) < n:
            if messages[i]["role"] == "assistant":
                exchange = {"assistant": messages[i]["content"]}
                if i > 0 and messages[i-1]["role"] == "user":
                    exchange["user"] = messages[i-1]["content"]
                    exchanges.insert(0, exchange)
                    i -= 2
                else:
                    i -= 1
            else:
                i -= 1
        
        return exchanges
    
    def size(self) -> int:
        """Get current number of messages in memory"""
        return len(self.messages)
