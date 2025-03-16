# 🧠 PromptWeaver - Intelligent Prompt Generation Tool

## 🔍 Project Overview

PromptWeaver is an AI-powered tool designed to automatically generate well-structured prompts for AI interactions. It analyzes user input to understand intent, extract relevant entities, and create optimized prompts using predefined templates. This tool bridges the gap between user needs and effective AI prompt engineering.

Think of PromptWeaver as a skilled interpreter who not only understands what you're asking for but also knows exactly how to phrase your request to get the best possible response from an AI system. Just like a chef who transforms raw ingredients (your inputs) into a delicious meal (structured prompt), PromptWeaver turns your casual requests into precisely formatted prompts that yield better AI results.

## 📄 File Descriptions

### 🎯 MainCodeRef.py

The brain of the application that coordinates the prompt generation workflow:
- Initializes AI models for intent classification and named entity recognition
- Analyzes user input to determine the intention behind the request
- Extracts relevant entities (domains, tools, concepts, etc.)
- Applies templates based on detected intent
- Generates structured prompt components

**Human Analogy**: MainCodeRef.py works like a skilled interviewer who asks clarifying questions to understand exactly what you need, picks out the important details, and then rephrases your request in the most effective way.

```python
# Example usage
processor = IntentProcessor()
intent = processor.get_intent("Help me learn about machine learning algorithms")
entities = processor.get_entities(user_input, intent)
prompt = processor.generate_prompt(intent, entities)
```

### ⚙️ config.py

The configuration center that defines the parameters and settings for the prompt generation system:
- Model configuration for intent classification
- NER (Named Entity Recognition) settings and entity mapping
- Template definitions for different types of queries
- Intent filters to extract relevant entities based on intent

**Human Analogy**: config.py is like a reference manual for a translator, containing all the vocabulary, grammar rules, and stylistic guidelines they need to translate effectively in different contexts.

```python
# Sample configuration
INTENT_CONFIG = {
    "model_name": "MoritzLaurer/deberta-v3-base-zeroshot-v1",
    "candidate_labels": ["learn", "explain", "compare", ...],
    "threshold": 0.7
}
```

### 🔧 prompt_generator.py

An interactive tool that provides a user interface for generating and fine-tuning prompts:
- Loads and manages language models for prompt generation
- Provides a developer mode for manual parameter configuration
- Includes templates for different types of content
- Handles formatting and error detection

**Human Analogy**: prompt_generator.py functions like a custom tailoring shop where you can adjust every aspect of your outfit (prompt) to fit perfectly for the occasion, with expert guidance available when you need it.

```python
# Interactive usage
generator = InteractivePromptGenerator()
generator.interactive_dev_mode()  # Configure parameters interactively
prompt = generator.generate_prompt("Write a creative story about space exploration")
```

## 🚀 Setup Instructions

1. **Prerequisites**
   - Python 3.7+
   - PyTorch
   - Transformers library by Hugging Face
   - Internet connection (for downloading models on first run)

2. **Installation**
   ```bash
   # Clone the repository (if applicable)
   git clone <repository-url>
   
   # Navigate to the project directory
   cd Project/Version_1
   
   # Install required packages
   pip install torch transformers
   ```

3. **First-Time Setup**
   - The application will download the required pre-trained models on first run
   - This may take several minutes depending on your internet connection
   - Models are cached for future use

## 💡 Usage

### Basic Usage

```python
# Import the IntentProcessor
from MainCodeRef import IntentProcessor

# Initialize the processor
processor = IntentProcessor()

# Process a user request
user_input = "Help me learn about Python programming for data science"
intent = processor.get_intent(user_input)
entities = processor.get_entities(user_input, intent)
prompt_components = processor.generate_prompt(intent, entities)

# View the generated prompt components
print(f"Intent: {intent}")
print(f"Header: {prompt_components['header']}")
print(f"Required Fields: {prompt_components['fields']}")
```

### Interactive Developer Mode

```python
# Import the interactive generator
from prompt_generator import InteractivePromptGenerator

# Initialize the generator
generator = InteractivePromptGenerator()

# Enter developer mode for fine-tuning
generator.interactive_dev_mode()

# Generate prompts with customized settings
prompt = generator.generate_prompt("Analyze the impact of AI on healthcare")
print(prompt)
```

## 🌟 Example Scenarios

### Scenario 1: Learning Request

**User Input:**
```
"I want to learn about machine learning algorithms for image recognition"
```

**Generated Prompt Components:**
```
Intent: learn
Header: You are a knowledgeable assistant helping with machine learning, image recognition
Required Fields: ['Domain/Concept', 'Technology/Company']
```

### Scenario 2: Comparison Request

**User Input:**
```
"Compare PyTorch and TensorFlow for deep learning projects"
```

**Generated Prompt Components:**
```
Intent: compare
Header: Technical comparison expert specializing in deep learning
Fields: ['subject1', 'subject2', 'comparison_aspects']
Detected Entities: {'relevant': [{'text': 'PyTorch', 'type': 'Technology/Company'}, 
                                {'text': 'TensorFlow', 'type': 'Technology/Company'}, 
                                {'text': 'deep learning', 'type': 'Domain/Concept'}]}
```

## 🔧 Troubleshooting

- **Low Confidence Intent Classification**: If the system displays "general" as the intent when you expected something more specific, try rephrasing your request with more explicit intent keywords.
- **Missing Entities**: If important entities aren't being detected, try using more standard terminology or explicitly mention key concepts.
- **Model Download Issues**: If models fail to download, ensure you have a stable internet connection and sufficient disk space.

---

## 🔮 Future Enhancements

- Add support for multi-turn conversations to refine prompts
- Implement custom template creation UI
- Expand the range of supported intent types
- Improve entity extraction for specialized domains

---

👨‍💻 Created with PromptWeaver - Enhancing Human-AI Interaction, One Prompt at a Time

