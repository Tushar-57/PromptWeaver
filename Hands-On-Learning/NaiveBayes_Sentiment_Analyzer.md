# Naive Bayes Sentiment Analyzer & Visualization 🧠📊

## Overview
Discover a simple yet effective sentiment analysis tool built with a **Naive Bayes Classifier**. This project not only classifies text into positive or negative sentiments, but it also visualizes word frequencies and generates word clouds to give you deeper insights into your data.

### 🧠 Human Analogies
To better understand how the Naive Bayes classifier works, consider these everyday examples:

1. **🍽️ Restaurant Reviews**: Imagine reading a restaurant review. Words like "delicious", "amazing", and "friendly" may indicate a positive review, while words like "disappointing", "bad", and "awful" hint at negativity. Just as humans use these cues to form an opinion, the classifier leverages word frequencies to determine sentiment.

2. **🎬 Movie Ratings**: Think of movie ratings where viewers share their thoughts. A review containing "thrilling", "engaging", and "masterful" is likely positive, whereas one with "boring", "predictable", and "mediocre" tends to be negative. The classifier mimics this intuitive judgment by analyzing word patterns in the text.

Much like our everyday impressions, the Naive Bayes classifier simplifies decision-making by assuming each word contributes independently to the overall sentiment.


## Description 📝
This project leverages a collection of labeled post comments to train a basic Naive Bayes classifier. It processes text by tokenizing (removing punctuation and numbers), and then computes word frequencies for both positive and negative categories. Key functionalities include:

- **Sentiment Classification:**  
  - **Tokenization:** Cleans text by removing punctuation, numbers, and splitting the text into words.
  - **Probability Calculation:** Computes the likelihood of each word belonging to positive or negative classes.
  - **Classification:** Compares probabilities to classify input text as **positive** ("pos") or **negative** ("neg").

- **Data Visualization:**  
  - **Word Frequency Plots:** Displays the 10 most common words in positive and negative comments using horizontal bar charts.
  - **Word Clouds:** Creates engaging visual word clouds for both positive and negative sentiments.

## Prerequisites ✅
Ensure you have the following installed:

- **Python 3.x**

Additional libraries for visualization:
- **Matplotlib**
- **WordCloud**

You can install the necessary libraries with:
```bash
pip install matplotlib wordcloud
```

## Usage 💻
To run and explore the project:

### Run the Script:
```bash
python NaiveBayes_Sentiment_Analyzer.py
```
- **This will:**
  - Train the Naive Bayes classifier on the provided comments.
  - Test the classifier with sample texts.
  - Display word frequency bar charts.
  - Generate word clouds for both positive and negative comments.

- **Customize Your Input:**
  - Update the `post_comments_with_labels` list with your own labeled data.
  - Modify or add new test texts to evaluate the classifier’s performance.

- **Code Features 🛠️**

  - **NaiveBayesClassifier Class:**
    - **Tokenization:** Efficient text preprocessing to remove noise.
    - **Classification:** Uses simple probability estimates based on word counts.
    - **Visualization Methods:**
      - `plot_word_frequencies()` for bar charts.
      - `generate_word_cloud(label)` for creating word clouds.

  - **Visualization Tools:**
    - **Matplotlib:** For generating bar charts of word frequencies.
    - **WordCloud:** For creating visually appealing word clouds.

- **Learning Outcomes 💡**
  - **Sentiment Analysis:** Understand the basics of a classic machine learning algorithm.
  - **Text Processing:** Learn effective techniques to clean and tokenize text.
  - **Visual Data Insights:** Gain experience in representing textual data through plots and word clouds.
  - **Experimentation:** Customize training data and parameters to explore how they affect results.

- **Highlights 📌**
  - **Interactive Testing:** Try out sample texts and see real-time predictions.
  - **Visual Insights:** Quickly identify influential words in positive and negative contexts.
  - **Educational:** A beginner-friendly implementation that introduces core NLP concepts and data visualization techniques.

Enjoy exploring the blend of sentiment analysis and visual storytelling! Happy coding! 🚀
