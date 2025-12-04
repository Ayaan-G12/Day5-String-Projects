"""
String Analyzer
--------------
Analyzes a string for different characteristics:
length, uppercase count, lowercase count, digits, and spaces.
"""

def analyze_string(text: str) -> dict:
    """Return analysis statistics for the given text."""
    return {
        "length": len(text),
        "uppercase": sum(1 for c in text if c.isupper()),
        "lowercase": sum(1 for c in text if c.islower()),
        "digits": sum(1 for c in text if c.isdigit()),
        "spaces": text.count(" ")
    }

if __name__ == "__main__":
    text = input("Enter a string: ")
    stats = analyze_string(text)
    print(stats)
