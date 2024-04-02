import datetime
import decimal

import matplotlib.pyplot as plt

from ..Controller import Controller
from .DashboardView import DashboardView
from .DashboardModel import DashboardModel

class DashboardController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            DashboardView(parent),
            DashboardModel()
        )
        self.header = header
        self.user_id = user_id
        self.view.main()
        self.set_account_name()
        self.create_latest_transaction_labels()
        self.create_active_alerts()
        self.plot_graph()
        self.bind_view()

    def set_account_name(self):
        first_name = self.model.get_user_first_name(self.user_id)
        last_name = self.model.get_user_last_name(self.user_id)
        self.view.account_name.config(
            text=f"Compte de {first_name} {last_name}"
        )

    def create_latest_transaction_labels(self):
        transactions = self.model.get_latest_transactions(self.user_id)
        self.view.create_latest_transaction_labels(transactions)

    def get_notable_transactions(self):
        transactions = self.model.get_this_months_transactions(self.user_id)
        notable_transactions = []

        for transaction in transactions:
            amount_string = decimal.Decimal(transaction[3])
            amount_string = amount_string.quantize(decimal.Decimal("0.00"))
            if transaction[3] >= 2000:
                message = (
                    f"Plafond dépassé le {transaction[4].strftime("%x")}"
                )
                notable_transactions.append(message)
            elif transaction[3] <= -500 or transaction[3] >= 500:
                message = (
                    f"Transaction conséquente "
                    f"le {transaction[4].strftime("%x")} "
                    f"de {amount_string} €"
                )
                notable_transactions.append(message)

        return notable_transactions

    def create_active_alerts(self):
        notifications = self.get_notable_transactions()
        if len(notifications) > 0:
            self.view.create_active_alerts(notifications)

    def plot_graph(self):
        fig, ax = plt.subplots(figsize=(13.15, 5.81))
        totals_list = self.model.get_this_years_monthly_totals(self.user_id)
        months = [
            "Jan",
            "Fév",
            "Mar",
            "Avr",
            "Mai",
            "Juin",
            "Juil",
            "Août",
            "Sep",
            "Oct",
            "Nov",
            "Déc"
        ]
        total_revenue = [month["total_revenue"] for month in totals_list]
        total_spending = [month["total_spending"] for month in totals_list]

        bar_width = 0.35
        index = range(len(months))

        ax.bar(
            [i - bar_width / 2 for i in index],
            total_revenue,
            bar_width,
            color="tab:green"
        )
        ax.bar(
            [i + bar_width / 2 for i in index],
            total_spending,
            bar_width,
            color="tab:red"
        )

        ax.set_ylabel("En €")
        current_year = datetime.datetime.now().year
        ax.set_title(f"Revenues et dépenses de {current_year}")
        ax.set_xticks(index)
        ax.set_xticklabels(months)
        plt.close()

        self.view.draw_graph(fig)

    def bind_view(self):
        if hasattr(self.view, "button"):
            self.view.button.bind(
                "<ButtonRelease-1>",
                self.header.click_notification_button
            )