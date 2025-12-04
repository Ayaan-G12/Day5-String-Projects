"""
Word Reverser
--------------
Reverses each word in a sentence.
"""

def reverse_words(sentence: str) -> str:
    """Reverse every word in the sentence."""
    words = sentence.split()
    reversed_words = [w[::-1] for w in words]
    return " ".join(reversed_words)

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(reverse_words(text))
