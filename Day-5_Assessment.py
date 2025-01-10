from collections import Counter
import re
def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    for word, count in word_counts.items():
        print(f"{word}: {count}")

text = "Hello everyone. Welcome to the world of Python."
word_frequency(text)
