import datetime

from ..Controller import Controller
from .TransactionListView import TransactionListView
from .TransactionListModel import TransactionListModel

class TransactionListController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            TransactionListView(parent),
            TransactionListModel()
        )
        self.header = header
        self.user_id = user_id
        self.view.main()
        self.display_transactions_in_treeview()

    def display_transactions_in_treeview(self):
        transactions = self.model.get_all_transactions(self.user_id)
        for i, transaction in enumerate(transactions):
            name = transaction[1]
            description = transaction[2]
            amount = f"{transaction[3]} €"
            date = transaction[4].strftime("%x %X")

            transaction_info = (
                date,
                name,
                description,
                amount
            )
            self.view.tree.insert(
                "",
                "end",
                text=i,
                values=transaction_info
            )