"""
Text Sanitizer
--------------
Cleans a noisy text by:
- removing non-alphanumeric characters (keeps spaces)
- reducing multiple spaces to one
- trimming leading/trailing spaces
"""

import re

def sanitize(text: str) -> str:
    """Clean text by removing special characters and extra spaces."""
    cleaned = re.sub(r"[^A-Za-z0-9 ]+", "", text)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()

if __name__ == "__main__":
    t = input("Enter messy text: ")
    print(sanitize(t))
