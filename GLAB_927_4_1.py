# Task 1: Importing Libraries
# Importing TextBlob library

# Sample text for checking TextBlob installation
sample_text = "TextBlob is a successfully installed and ready to use."

# Print confirmation message
print(f"TextBlob library imported successfully! Sample text: '{sample_text}'")

# Task 2: Implementing Sentiment Analysis

from textblob import TextBlob

# Sample text for sentiment analysis
sample_text = "I absolutely love this product! The quality is excellent and it arrived on time."

# Create a TextBlob object
blob = TextBlob(sample_text)

# Perform sentiment analysis
sentiment = blob.sentiment

# Print the original text and sentiment analysis results
print("Original Text:", sample_text)
print("Sentiment Analysis Results:")
print("Polarity:", sentiment.polarity) #Range from -1 (negative) to 1 (positive)
print("Subjectivity:", sentiment.subjectivity) #Range from 0 (objective) to 1 (subjective)

# Task 3: Analyzing Business Communication Data

