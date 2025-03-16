from string import punctuation
from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Training data
post_comments_with_labels = [
    ("This is lovely", "pos"),
    ("This is looking ugly", "neg"),
    ("Absolutely stunning!", "pos"),
    ("I hate this", "neg"),
    ("Such a beautiful picture", "pos"),
    ("This is the worst thing I’ve seen", "neg"),
    ("So creative and unique!", "pos"),
    ("Not a fan of this at all", "neg"),
    ("Love the colors in this", "pos"),
    ("This looks awful", "neg"),
    ("Brilliant work!", "pos"),
    ("I don’t like how this turned out", "neg"),
    ("Wow, this is amazing!", "pos"),
    ("This makes no sense", "neg"),
    ("Super impressive!", "pos"),
    ("It’s really bad", "neg"),
    ("Fantastic effort!", "pos"),
    ("This is a disaster", "neg"),
    ("I’m in love with this", "pos"),
    ("This is poorly done", "neg"),
    ("So well executed!", "pos"),
    ("Not good at all", "neg"),
    ("I adore this!", "pos"),
    ("This is just horrible", "neg"),
    ("Very impressive!", "pos"),
    ("Looks really weird", "neg"),
    ("A masterpiece!", "pos"),
    ("Who approved this?", "neg"),
    ("Absolutely breathtaking", "pos"),
    ("This is a mess", "neg"),
    ("Phenomenal work!", "pos"),
    ("Couldn’t be worse", "neg"),
    ("So inspiring!", "pos"),
    ("Not appealing at all", "neg"),
    ("This is pure talent", "pos"),
    ("I expected better", "neg"),
    ("Beyond amazing!", "pos"),
    ("This ruins everything", "neg"),
    ("This made my day!", "pos"),
    ("Such an eyesore", "neg"),
    ("I appreciate this a lot", "pos"),
    ("Disappointing result", "neg"),
    ("Absolutely perfect", "pos"),
    ("This is just bad", "neg"),
    ("Incredible!", "pos"),
    ("Not my taste at all", "neg"),
    ("Such a warm and inviting feel", "pos"),
    ("It’s a failure", "neg"),
    ("So much effort put into this", "pos"),
    ("Why would anyone like this?", "neg"),
    ("Completely stunning", "pos"),
    ("Hard to look at", "neg"),
    ("So much beauty in this", "pos"),
    ("This is terrible", "neg"),
    ("I love every detail", "pos"),
    ("It’s too messy", "neg"),
    ("Perfectly done!", "pos"),
    ("This looks rushed", "neg"),
    ("So elegant!", "pos"),
    ("It’s just boring", "neg"),
    ("I can’t stop admiring this", "pos"),
    ("This is way off", "neg"),
]

class NaiveBayesClassifier:
    def __init__(self, samples):
        self.mapping = {"pos": [], "neg": []}  # To store tokens for each label
        self.sample_count = len(samples)  # Total number of samples

        for text, label in samples:
            tokens = self.tokenize(text)  # Get tokens for the current text
            self.mapping[label].extend(tokens)  # Append tokens to the corresponding label

        # Count word occurrences for each label
        self.pos_counter = Counter(self.mapping["pos"])
        self.neg_counter = Counter(self.mapping["neg"])

    @staticmethod
    def tokenize(text):
        # Tokenizes the text: removes punctuation, numbers, and splits by spaces
        return [
            word.lower() for word in text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
            if word
        ]

    def classify(self, text):
        tokens = self.tokenize(text)  # Tokenize the input text

        pos_prob = 0  # Initialize pos probability (log scale)
        neg_prob = 0  # Initialize neg probability (log scale)

        # Iterate through tokens and calculate probabilities
        for token in tokens:
            # Probability of token given pos and neg
            pos_prob += self.pos_counter[token] / self.sample_count if token in self.pos_counter else 0
            neg_prob += self.neg_counter[token] / self.sample_count if token in self.neg_counter else 0

        # Return the label with the highest probability
        return "pos" if pos_prob > neg_prob else "neg"

        #Another basic Approach could be
        # if sum(pos)> sum(neg):
        #     return "pos"
        # elif sum(neg) > sum(pos):
        #     return "neg"
        # else:
        #     return "net"

#Additional logic for visualization

    def plot_word_frequencies(self):
        # Plot the most common words in positive and negative categories

        # Most common words in 'pos' category
        pos_most_common = self.pos_counter.most_common(10)
        neg_most_common = self.neg_counter.most_common(10)

        pos_words, pos_freqs = zip(*pos_most_common)
        neg_words, neg_freqs = zip(*neg_most_common)

        # Plotting the word frequencies for positive and negative comments
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        ax1.barh(pos_words, pos_freqs, color='g')
        ax1.set_title('Most Common Words in Positive Comments')
        ax1.set_xlabel('Frequency')

        ax2.barh(neg_words, neg_freqs, color='r')
        ax2.set_title('Most Common Words in Negative Comments')
        ax2.set_xlabel('Frequency')

        plt.tight_layout()
        plt.show()

    def generate_word_cloud(self, label):
        # Generate a word cloud for a given label (pos/neg)
        if label == "pos":
            words = self.mapping["pos"]
        else:
            words = self.mapping["neg"]

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f"Word Cloud for {label} Comments")
        plt.show()





# Training the Naive Bayes Classifier
nb = NaiveBayesClassifier(post_comments_with_labels)

# Test predictions
test_text = "ugly"
print(f"Prediction for '{test_text}': {nb.classify(test_text)}")

# Play around with test texts.
test_text2 = "absolutely This is opposite of breathtakingly beautiful absolutely very absolutely"


print(f"Prediction for '{test_text2}': {nb.classify(test_text2)}")

nb.plot_word_frequencies()

# Generate word clouds for positive and negative comments
nb.generate_word_cloud("pos")
nb.generate_word_cloud("neg")