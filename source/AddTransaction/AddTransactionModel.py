from ..Model import Model


class AddTransactionModel(Model):
    def __init__(self):
        super().__init__()

    def add_transaction(
        self,
        t_name,
        t_description,
        t_amount,
        t_date,
        u_id
    ):

        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"INSERT INTO transaction (t_name, t_description, t_amount, t_date, u_id) "
            f"VALUES ('{t_name}', '{t_description}', {t_amount}, '{t_date}', {u_id});"
        )
        connection.commit()

        cursor.close()
        connection.close()