import decimal
import datetime

from ..Model import Model


class DashboardModel(Model):
    def __init__(self):
        super().__init__()

    def get_user_first_name(self, user_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT u_first_name FROM user WHERE u_id = {user_id}")
        first_name = cursor.fetchall()

        cursor.close()
        connection.close()

        return first_name[0][0]

    def get_user_last_name(self, user_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(f"SELECT u_last_name FROM user WHERE u_id = {user_id}")
        last_name = cursor.fetchall()

        cursor.close()
        connection.close()

        return last_name[0][0]

    def get_latest_transactions(self, user_id):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            f"SELECT * FROM transaction WHERE u_id = {user_id} "
            f"ORDER BY t_date DESC LIMIT 3;"
        )
        transactions = cursor.fetchall()

        cursor.close()
        connection.close()

        return transactions

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

    def get_this_years_monthly_totals(self, user_id):
        current_year = datetime.datetime.now().year
        totals_list = []

        connection = self.connect()
        cursor = connection.cursor()

        for month in range(1, 12+1):
            month_total = {
                "total_revenue": 0,
                "total_spending": 0,
            }

            cursor.execute(
                f"SELECT t_amount FROM transaction WHERE u_id = {user_id} "
                f"AND t_amount > 0 AND MONTH(t_date) = {month} "
                f"AND YEAR(t_date) = {current_year}"
            )
            revenue = cursor.fetchall()
            for amount in revenue:
                month_total["total_revenue"] += amount[0]

            cursor.execute(
                f"SELECT t_amount FROM transaction WHERE u_id = {user_id} "
                f"AND t_amount < 0 AND MONTH(t_date) = {month} "
                f"AND YEAR(t_date) = {current_year}"
            )
            spending = cursor.fetchall()
            for amount in spending:
                month_total["total_spending"] += (amount[0] * -1)

            totals_list.append(month_total)

        cursor.close()
        connection.close()

        return totals_list