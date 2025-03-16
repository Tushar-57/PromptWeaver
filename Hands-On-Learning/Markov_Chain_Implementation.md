# Markov Chain Text Generator 🔄


## Description 📝
`Markov_Chain_Implementation.py` brings to life a Markov chain language model that generates text by following a below depicted flow.

### 🧠 Human Analogy for MC.
To understand how the Markov Chain text generator works, consider these examples:

1. **🚶‍♂️ City Navigation:**  
   Just as you choose your next turn based on your current location, the generator picks the next word based on the current one.
   
2. **🎲 Dice-Driven Storytelling:**  
   Imagine crafting a story by rolling dice to determine what happens next. Each roll (or word choice) is random yet influenced by the previous outcome.

## Flow:
1. **Constructs** a probabilistic model of text based on word transitions  
2. **Tokenizes** input text by removing punctuation and splitting it into words  
3. **Builds** a directed graph where each word points to its potential successors  
4. **Generates** new text by randomly traversing the graph  
5. **Demonstrates** its power using biographical snippets about Andrey Markov and Linus Torvalds—perfectly nodding to the origins of the method!

> **Highlight:** This project is a practical demonstration of predictive text in action, giving you a taste of how everyday applications like keyboard suggestions and chatbots work.

Make sure you have the following ready before running the script:

- **Python 3.x**

For the (currently commented out) visualization feature:
- **NetworkX** library
- **Matplotlib** library

## Usage 💻
Get started with text generation in just a few simple steps:

1. **Run the script directly:**
   ```bash
   python Markov_Chain_Implementation.py
   ```

2. The script will:
   - Train a Markov chain on the provided biographical texts as input
   - Generate a sample text completion starting with "Linus Torvald is "
   - Output the generated text to the console

3. To use with your training text:
   ```python
   my_model = MarkovChain()
   my_model.train("Your text goes here") #Replace " Your text goes here with 'training text'."
   generated_text = my_model.generate("Your starting prompt", 10)  # Generate 10 words
   print(generated_text)
   ```

## Code Features 🛠️
- `MarkovChain` class for (highlight)text generation
- (highlight TP)Text preprocessing with punctuation removal
- (Commented) Graph visualization for created Markov Chain

## What's in it for you 💡
- Understand how simple language models work (very simple)
- See defaultdict and random.choice() in practical use
- Learn about graph-based text representation
- Explore the **foundations of text prediction algorithms**
- Experiment with text generation parameters.

## Some Highlights, before you try it out. 📌
- Output Quality: Directly influenced by the size and variety of your training text.
- Educational Simplicity: A beginner-friendly implementation designed for learning.
- Visualization Ready: Uncomment the visualization code for an extra layer of insight (ensure you have the required libraries).
- Customizable: Play around with different texts and parameters for endless creative possibilities.

Happy generating! 🤖✍️

