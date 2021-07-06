import secrets
import string


def generate_random_password(length=8,
                             allow_digits=False,
                             allow_special_characters=False):
    allowed_characters = string.ascii_letters

    if allow_digits:
        allowed_characters += string.digits
    if allow_special_characters:
        allowed_characters += string.punctuation

    password = ''.join(secrets.choice(allowed_characters) for _ in range(length))
    return password
