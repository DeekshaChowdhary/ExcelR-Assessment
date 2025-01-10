import nltk
nltk.download('punkt')
def tokenize_paragraph(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    words = nltk.word_tokenize(paragraph)
    return sentences, words
sample_paragraph = """
Tokenization is the process of breaking a text into smaller units. These units can be sentences or words. 
It's a crucial step in text preprocessing for natural language processing tasks.
"""
sentences, words = tokenize_paragraph(sample_paragraph)
print("Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}: {sentence}")
print("\nWords:")
print(words)
