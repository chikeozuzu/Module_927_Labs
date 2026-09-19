# Task 1 Named Entity Recognition (NER) to extract business entities

import nltk
# Download necessary NLTK data for NER
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Sample business document
business_document = """
The recent feedback from Acme Corp. highlighted issues with the new model of the Omega widget.
Customers from New York and San Francisco have reported delays in shipping.
The CEO of Acme Corp., Jane Doe, has promised to address these concerns by Q3.
"""

# Tokenizing the document
tokens = nltk.word_tokenize(business_document)

# Applying NER
ner_results = nltk.ne_chunk(nltk.pos_tag(tokens))

# Printing named entities
print("Named Entities:")
for entity in ner_results:
    if isinstance(entity, nltk.Tree):
        print("".join([word for word, tag in entity.leaves()]))

# Task 2 Named Entity Recognition (NER) to print entity categories
# Printing named entities along with their categories

print("\nNamed Entities with Categories:")
for entity in ner_results:
    if isinstance(entity, nltk.Tree):
        entity_name = " ".join([word for word, tag in entity.leaves()])
        entity_category = entity.label()
        print(f"{entity_name}: {entity_category}")

# Task 3 Part-of-Speech (POS) Tagging to analyze business text

# Sample business document
business_document = """
The recent feedback from Acme Corp. highlighted issues with the new model of the Omega widget.
Customers from New York and San Francisco have reported delays in shipping.
The CEO of Acme Corp., Jane Doe, has promised to address these concerns by Q3.
"""

# Tokenizing the document
tokens = nltk.word_tokenize(business_document)

# Applying POS tagging
pos_tags = nltk.pos_tag(tokens)

# Printing words and their POS tags
print("Words and POS Tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")

