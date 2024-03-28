from ..Model import Model


class HeaderModel(Model):
    def __init__(self):
        super().__init__()

    def get_user_first_name(self, u_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT u_first_name FROM user WHERE u_id = {u_id}")
        first_name = cursor.fetchall()

        cursor.close()
        connection.close()

        return first_name[0][0] 

    def get_user_last_name(self, u_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT u_last_name FROM user WHERE u_id = {u_id}")
        last_name = cursor.fetchall()

        cursor.close()
        connection.close()

        return last_name[0][0] 