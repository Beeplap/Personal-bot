"""
Model configurations for different LLM providers
"""

from typing import Dict, List
from pydantic import BaseModel


class LLMConfig(BaseModel):
    """Configuration model for LLM"""
    provider: str
    model: str
    api_key: str = ""
    temperature: float = 0.7
    max_tokens: int = 500


# Available models for different providers
AVAILABLE_MODELS: Dict[str, List[str]] = {
    "openai": [
        "gpt-4",
        "gpt-4-turbo-preview",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-16k"
    ],
    "anthropic": [
        "claude-3-5-sonnet-20241022",
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-haiku-20240307"
    ],
    "huggingface": [
        "gpt2",
        "google/flan-t5-base",
        "microsoft/DialoGPT-medium"
    ]
}
