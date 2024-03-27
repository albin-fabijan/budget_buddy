import re

from ..Model import Model


class SignUpModel(Model):
    def __init__(self):
        super().__init__()

    def is_email_valid(self, email):
        email_regex = (
            r"([a-zA-Z\d_\-.]+)"
            r"@([a-zA-Z\d_\-.]+)"
            r"\.([a-zA-Z]+)"
        )

        result = re.match(email_regex, email)

        if not result:
            return False

        return result.group() == email

    def is_password_valid(self, password):
        has_uppercase = any(
            char.isupper()
            for char in password
        )
        has_lowercase = any(
            char.islower()
            for char in password
        )
        has_digit = any(
            char.isdigit()
            for char in password
        )
        has_special = any(
            not char.isalnum()
            for char in password
        )
        is_required_length = len(password) >= 10

        return (
            has_uppercase
            and has_lowercase
            and has_digit
            and has_special
            and is_required_length
        )