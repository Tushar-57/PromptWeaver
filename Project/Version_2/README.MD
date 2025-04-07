 # LLM Prompt Generation Service

A service for generating detailed LLM-ready prompts using the CAMEL framework and Ollama models. Designed for dynamic prompt engineering with customizable parameters.

## Features

- Dynamic prompt template generation
- Integration with Ollama local models (llama3, mistral, etc.)
- Customizable parameters for:
  - Personality/tone control
  - Creativity levels
  - Audience targeting
  - Output formatting
  - Response length
- Detailed logging and debugging
- Token usage tracking

## Requirements

- Python 3.9+
- Anaconda/Miniconda
- Ollama (local installation)
- 4GB+ RAM (8GB recommended for larger models)

## Installation

1. **Set Up Conda Environment**
```bash
conda create -n camel-llm python=3.9
conda activate camel-llm
pip install camel-python python-dotenv
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3 # Or your preferred model 
```

2. **Run The Application**
```bash
cd /Version_2/FrontEnd_With_Application/
npm install
npm run dev
```
> Open new terminal for LLM service.
```bash
python3 app.py
```


