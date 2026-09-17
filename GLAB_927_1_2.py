#Task 1

#importing NLTK library
import nltk

#checking NLTK version
nltk_version = nltk.__version__

#print confirmation message and NLTK version
print(f"NLTK library imported successfully! Version: {nltk_version}")

#Task 2

from nlkt.stem import PorterStemmer

#download NLTK resources (tokenizers)
nltk.download('punkt')

#sample email content for stemming
email_content = "Our team is working on the upcoming project deadlines. Please ensure that all deliverables are submitted before the end of the week."

#create a Porter Stemmer instance
porter_stemmer = PorterStemmer()

#apply stemming to each word in the email content
stemmed_words = [porter_stemmer.stem(word) for word in nltk.word_tokenize(email_content)]

#print the original and stemmed text
print("Original Email Content:", email_content)
print("Stemmed Email Content:", " ".join(stemmed_words))

#Task 3

