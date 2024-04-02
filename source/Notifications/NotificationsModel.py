import datetime

from ..Model import Model

class NotificationsModel(Model):
    def __init__(self):
        super().__init__()

    def get_this_months_transactions(self, user_id):
        current_date = datetime.datetime.now()
        last_month = current_date - datetime.timedelta(days = 31)

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT * FROM transaction "
            f"WHERE u_id = {user_id} AND t_date > '{last_month}' "
            f"ORDER by t_date DESC;"
        )
        transactions = cursor.fetchall()

        cursor.close()
        connection.close()

        return transactions