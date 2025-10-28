"""
Main bot class for Personal Bot
"""

import json
import os
from typing import Optional, Dict, Any
from .llm.provider import LLMProvider
from .memory.memory import ConversationMemory


class PersonalBot:
    """Main bot class that handles conversations and integrates with LLM providers"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the Personal Bot
        
        Args:
            config_path: Path to configuration file. Defaults to config/config.json
        """
        if config_path is None:
            config_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "config",
                "config.json"
            )
        
        self.config = self._load_config(config_path)
        self.llm_provider = LLMProvider(self.config)
        self.memory = ConversationMemory(
            max_size=self.config["bot"]["max_memory_size"]
        )
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def chat(self, message: str) -> str:
        """
        Send a message to the bot and get a response
        
        Args:
            message: User's message
            
        Returns:
            Bot's response
        """
        # Add message to memory
        self.memory.add_message("user", message)
        
        # Get conversation history
        history = self.memory.get_history()
        
        # Get response from LLM
        response = self.llm_provider.get_response(
            message=message,
            history=history,
            system_prompt=self.config["bot"]["system_prompt"]
        )
        
        # Add response to memory
        self.memory.add_message("assistant", response)
        
        return response
    
    def clear_memory(self):
        """Clear conversation memory"""
        self.memory.clear()
    
    def get_config(self) -> Dict[str, Any]:
        """Get current configuration"""
        return self.config


def main():
    """Main entry point for running the bot interactively"""
    bot = PersonalBot()
    
    print(f"Welcome to {bot.config['bot']['name']}!")
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = bot.chat(user_input)
            print(f"\n{bot.config['bot']['name']}: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

