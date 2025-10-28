"""
Tests for Personal Bot
"""

import pytest
from src.bot import PersonalBot
from src.memory.memory import ConversationMemory


def test_memory_creation():
    """Test conversation memory creation"""
    memory = ConversationMemory(max_size=10)
    assert memory.size() == 0
    assert memory.max_size == 10


def test_memory_add_message():
    """Test adding messages to memory"""
    memory = ConversationMemory(max_size=10)
    memory.add_message("user", "Hello")
    memory.add_message("assistant", "Hi there!")
    
    assert memory.size() == 2
    history = memory.get_history()
    assert history[0]["role"] == "user"
    assert history[1]["content"] == "Hi there!"


def test_memory_clear():
    """Test clearing memory"""
    memory = ConversationMemory()
    memory.add_message("user", "Hello")
    memory.clear()
    assert memory.size() == 0


def test_memory_max_size():
    """Test that memory respects max size"""
    memory = ConversationMemory(max_size=3)
    memory.add_message("user", "Message 1")
    memory.add_message("assistant", "Response 1")
    memory.add_message("user", "Message 2")
    memory.add_message("assistant", "Response 2")
    memory.add_message("user", "Message 3")
    
    # Should only keep last 3 messages
    assert memory.size() == 3


def test_bot_initialization():
    """Test bot initialization"""
    bot = PersonalBot()
    assert bot is not None
    assert bot.config is not None
    assert bot.memory is not None
