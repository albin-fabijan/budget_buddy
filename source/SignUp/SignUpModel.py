import hashlib
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

    def is_email_in_database(self, email):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT u_id FROM user WHERE u_email = '{email}'")
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(result) != 0:
            return True
        else:
            return False

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

    def hash_password(self, password):
        bytes_password = password.encode()
        sha256 = hashlib.sha256()
        sha256.update(bytes_password)
        hashed_password = sha256.hexdigest()
        return hashed_password

    def create_user(self, first_name, last_name, email, hashed_password):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"INSERT INTO user ("
            f"u_first_name, "
            f"u_last_name, "
            f"u_email, "
            f"u_password_hash, "
            f"u_balance"
            f") "
            f"VALUES ("
            f"'{first_name}', "
            f"'{last_name}', "
            f"'{email}', "
            f"'{hashed_password}', "
            f"0"
            f");"
            )
        connection.commit()

        cursor.close()
        connection.close()
        