"""
Helper utility functions
"""

import os
import json
from typing import Any, Dict, Optional


def multiple_environment_variables() -> Dict[str, str]:
    """
    Load environment variables from .env file if it exists
    
    Returns:
        Dictionary of environment variables
    """
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    
    return dict(os.environ)


def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Load JSON file
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Dictionary containing JSON data
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_json_file(data: Dict[str, Any], file_path: str):
    """
    Save data to JSON file
    
    Args:
        data: Data to save
        file_path: Path to save the file
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def sanitize_message(message: str) -> str:
    """
    Sanitize user message
    
    Args:
        message: Raw user message
        
    Returns:
        Sanitized message
    """
    return message.strip()


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration dictionary
    
    Args:
        config: Configuration to validate
        
    Returns:
        True if valid, False otherwise
    """
    required_keys = ["llm", "bot"]
    return all(key in config for key in required_keys)

