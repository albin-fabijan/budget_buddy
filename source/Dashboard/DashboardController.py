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
        transactions = self.model.get_this_weeks_transactions(self.user_id)
        notable_transactions = []

        for transaction in transactions:
            amount_string = decimal.Decimal(transaction[3])
            amount_string = amount_string.quantize(decimal.Decimal("0.00"))
            if transaction[3] > 2000:
                message = (
                    f"Plafond dépassé le {transaction[4].strftime("%x")}"
                )
                notable_transactions.append(message)
            elif transaction[3] < -500 or transaction[3] > 500:
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
        dates = []
        amounts = []
        bar_colors = []
        transactions = self.model.get_this_weeks_transactions(self.user_id)
        for transaction in transactions:
            dates.append(transaction[4].strftime("%x\n%X"))
            if transaction[3] < 0:
                amounts.append(transaction[3] * -1)
                bar_colors.append("tab:red")
            else:
                amounts.append(transaction[3])
                bar_colors.append("tab:blue")
        ax.bar(dates, amounts, color = bar_colors)
        ax.set_ylabel("en €")
        ax.set_title("Dépenses et Revenus")
        plt.close()

        self.view.draw_graph(fig)

    def bind_view(self):
        if hasattr(self.view, "button"):
            self.view.button.bind(
                "<ButtonRelease-1>",
                self.header.click_notification_button
            )