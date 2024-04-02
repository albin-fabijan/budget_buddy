import decimal
from tkinter import END

from ..Controller import Controller
from .NotificationsView import NotificationsView
from .NotificationsModel import NotificationsModel


class NotificationsController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            NotificationsView(parent),
            NotificationsModel()
        )
        self.header = header
        self.user_id = user_id
        self.view.main()
        self.insert_notifications()

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

    def insert_notifications(self):
        for transaction in self.get_notable_transactions():
            self.view.treeview.insert(
                parent="",
                index=END,
                text=transaction
            )