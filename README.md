# Personal Bot

An intelligent personal assistant bot powered by Large Language Models (LLMs) built with Python.

## Features

- 🤖 Conversational AI powered by LLM models
- 💾 Memory and context management
- 🔧 Highly configurable and extensible
- 📝 Command-based and natural language interaction
- 🧪 Comprehensive testing suite

## Prerequisites

- Python 3.9 or higher
- pip package manager

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Beeplap/Personal-bot
cd personal-bot
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the bot by editing `config/config.json`

## Project Structure

```
personal-bot/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── config/                   # Configuration files
│   └── config.json          # Bot configuration
├── src/                      # Source code
│   ├── __init__.py
│   ├── bot.py               # Main bot class
│   ├── llm/                 # LLM integration
│   │   ├── __init__.py
│   │   ├── provider.py      # LLM provider abstraction
│   │   └── models.py        # Model configurations
│   ├── memory/              # Memory management
│   │   ├── __init__.py
│   │   └── memory.py        # Conversation memory
│   └── utils/               # Utilities
│       ├── __init__.py
│       └── helpers.py       # Helper functions
├── models/                   # Model files and storage
├── tests/                    # Test files
│   └── test_bot.py
└── .gitignore               # Git ignore file
```

## Configuration

Edit `config/config.json` to configure your bot:

```json
{
  "llm": {
    "provider": "openai",
    "model": "gpt-3.5-turbo",
    "api_key": "your-api-key-here",
    "temperature": 0.7
  },
  "bot": {
    "name": "Personal Bot",
    "max_memory_size": 100
  }
}
```

## Usage

Run the bot:

```bash
python -m src.bot
```

Or use it as a module:

```python
from src.bot import PersonalBot

bot = PersonalBot()
response = bot.chat("Hello!")
print(response)
```

## Supported LLM Providers

- OpenAI (GPT-3.5, GPT-4, etc.)
- Anthropic (Claude)
- Hugging Face Transformers
- Ollama (for local models)

## Development

Run tests:
```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Acknowledgments

- Built with Python and modern LLM APIs
- Inspired by the need for personal AI assistants
