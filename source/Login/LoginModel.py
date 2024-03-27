from ..Model import Model


class LoginModel(Model):
    def __init__(self):
        super().__init__()

    def read_all_users(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()

        cursor.close()
        connection.close()

        return users