import hashlib

from ..Model import Model


class LoginModel(Model):
    def __init__(self):
        super().__init__()

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

    def hash_password(self, password):
        bytes_password = password.encode()
        sha256 = hashlib.sha256()
        sha256.update(bytes_password)
        hashed_password = sha256.hexdigest()
        return hashed_password

    def is_password_correct(self, email, password):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT * FROM user "
            f"WHERE u_email = '{email}'"
            f"AND u_password_hash = '{self.hash_password(password)}';"
        )
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(result) != 0:
            return True
        else:
            return False

    def get_user_id(self, email, password):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT u_id FROM user "
            f"WHERE u_email = '{email}'"
            f"AND u_password_hash = '{self.hash_password(password)}';"
        )
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result[0][0]