"""
Email Validator
--------------
Basic validation rules for email addresses.
"""

def is_valid_email(email: str) -> bool:
    """Return True if email meets simple validation rules."""
    if " " in email:
        return False
    if email.count("@") != 1:
        return False

    local, domain = email.split("@")
    if not local or not domain:
        return False

    if "." not in domain:
        return False

    return True


if __name__ == "__main__":
    e = input("Enter an email: ").strip()
    print("Valid email?" , is_valid_email(e))
