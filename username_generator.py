"""
Username Generator
------------------
Generates three possible usernames based on first and last name.
"""

import random
import string

def generate_usernames(first: str, last: str) -> list:
    """Generate three username suggestions."""
    first, last = first.lower(), last.lower()
    return [
        first + last,
        first[0] + last,
        last + str(random.randint(10, 99))
    ]

if __name__ == "__main__":
    f = input("First name: ").strip()
    l = input("Last name: ").strip()
    print(generate_usernames(f, l))
