"""
LLM Provider abstraction for different LLM services
"""

from typing import Dict, Any, List, Optional
from .models import LLMConfig


class LLMProvider:
    """Abstraction layer for different LLM providers"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize LLM provider
        
        Args:
            config: Configuration dictionary
        """
        self.llm_config = config["llm"]
        self.provider_name = self.llm_config["provider"]
        self.api_key = self.llm_config.get("api_key", "")
        
        # Set API key in environment if not already set
        if self.api_key:
            if self.provider_name == "openai":
                import os
                if not os.getenv("OPENAI_API_KEY"):
                    os.environ["OPENAI_API_KEY"] = self.api_key
            elif self.provider_name == "anthropic":
                import os
                if not os.getenv("ANTHROPIC_API_KEY"):
                    os.environ["ANTHROPIC_API_KEY"] = self.api_key
    
    def get_response(
        self,
        message: str,
        history: List[Dict[str, str]],
        system_prompt: str
    ) -> str:
        """
        Get response from the LLM
        
        Args:
            message: Current user message
            history: Conversation history
            system_prompt: System prompt for the bot
            
        Returns:
            LLM response
        """
        try:
            if self.provider_name == "openai":
                return self._get_openai_response(message, history, system_prompt)
            elif self.provider_name == "anthropic":
                return self._get_anthropic_response(message, history, system_prompt)
            elif self.provider_name == "huggingface":
                return self._get_hf_response(message, history, system_prompt)
            else:
                return self._get_fallback_response(message)
        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}"
    
    def _get_openai_response(
        self,
        message: str,
        history: List[Dict[str, str]],
        system_prompt: str
    ) -> str:
        """Get response from OpenAI"""
        try:
            from openai import OpenAI
            
            client = OpenAI()
            
            messages = [{"role": "system", "content": system_prompt}]
            
            # Add stack history
            for entry in history:
                messages.append(entry)
            
            # Add current message
            messages.append({"role": "user", "content": message})
            
            response = client.chat.completions.create(
                model=self.llm_config.get("model", "gpt-3.5-turbo"),
                messages=messages,
                temperature=self.llm_config.get("temperature", 0.7),
                max_tokens=self.llm_config.get("max_tokens", 500)
            )
            
            return response.choices[0].message.content
            
        except ImportError:
            return "OpenAI library not installed. Run: pip install openai"
        except Exception as e:
            return f"OpenAI error: {str(e)}"
    
    def _get_anthropic_response(
        self,
        message: str,
        history: List[Dict[str, str]],
        system_prompt: str
    ) -> str:
        """Get response from Anthropic Claude"""
        try:
            from anthropic import Anthropic
            
            client = Anthropic()
            
            messages = []
            
            # Add conversation history
            for entry in history:
                # Convert to Anthropic format
                if entry["role"] == "user":
                    messages.append({"role": "user", "content": entry["content"]})
                elif entry["role"] == "assistant":
                    messages.append({"role": "assistant", "content": entry["content"]})
            
            # Add current message
            messages.append({"role": "user", "content": message})
            
            response = client.messages.create(
                model=self.llm_config.get("model", "claude-3-sonnet-20240229"),
                max_tokens=self.llm_config.get("max_tokens", 500),
                temperature=self.llm_config.get("temperature", 0.7),
                system=system_prompt,
                messages=messages
            )
            
            return response.content[0].text
            
        except ImportError:
            return "Anthropic library not installed. Run: pip install anthropic"
        except Exception as e:
            return f"Anthropic error: {str(e)}"
    
    def _get_hf_response(
        self,
        message: str,
        history: List[Dict[str, str]],
        system_prompt: str
    ) -> str:
        """Get response from Hugging Face"""
        try:
            from transformers import pipeline
            
            model_name = self.llm_config.get("model", "gpt2")
            generator = pipeline("text-generation", model=model_name)
            
            # Build conversation prompt
            prompt = system_prompt + "\n\n"
            for entry in history[-3:]:  # Last 3 exchanges
                prompt += f"{entry['role']}: {entry['content']}\n"
            prompt += f"user: {message}\nassistant:"
            
            result = generator(
                prompt,
                max_length=len(prompt.split()) + 50,
                temperature=self.llm_config.get("temperature", 0.7),
                num_return_sequences=1
            )
            
            return result[0]['generated_text'].split('assistant:')[-1].strip()
            
        except ImportError:
            return "Transformers library not installed. Run: pip install transformers"
        except Exception as e:
            return f"Hugging Face error: {str(e)}"
    
    def _get_fallback_response(self, message: str) -> str:
        """Fallback response when no provider is available"""
        return f"I received your message: '{message}'. Please configure a valid LLM provider in config/config.json"
