"""
Palindrome Checker
------------------
Checks if a string is a palindrome (ignores spaces and case).
"""

def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome."""
    clean = "".join(c.lower() for c in text if c.isalnum())
    return clean == clean[::-1]

if __name__ == "__main__":
    s = input("Enter text: ")
    print("Is palindrome?" , is_palindrome(s))
