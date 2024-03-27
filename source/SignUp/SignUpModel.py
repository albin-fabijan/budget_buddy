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