import datetime

from ..Model import Model

class NotificationsModel(Model):
    def __init__(self):
        super().__init__()

    def get_this_weeks_transactions(self, user_id):
        current_date = datetime.datetime.now()
        last_week = current_date - datetime.timedelta(days = 7)

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT * FROM transaction "
            f"WHERE u_id = {user_id} AND t_date > '{last_week}' "
            f"ORDER by t_date DESC;"
        )
        transactions = cursor.fetchall()

        cursor.close()
        connection.close()

        return transactions