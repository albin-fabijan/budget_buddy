from ..Model import Model

class TransactionListModel(Model):
    def __init__(self):
        super().__init__()

    def get_all_transactions(
        self,
        user_id,
        sort_value
    ):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT * FROM transaction WHERE u_id = {user_id} "
            f"{sort_value};"
        )
        transactions = cursor.fetchall()

        cursor.close()
        connection.close()

        return transactions