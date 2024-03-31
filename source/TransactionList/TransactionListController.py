import datetime

from ..Controller import Controller
from .TransactionListView import TransactionListView
from .TransactionListModel import TransactionListModel
from ..TransactionFilter.TransactionFilterController import (
    TransactionFilterController
)

class TransactionListController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            TransactionListView(parent),
            TransactionListModel()
        )
        self.header = header
        self.user_id = user_id
        self.type_value = ""
        self.date_value = ""
        self.sort_value = "ORDER BY t_date DESC;"
        self.view.main()
        self.display_transactions_in_treeview()
        self.bind_view()

    def display_transactions_in_treeview(self):
        transactions = self.model.get_all_transactions(
            self.user_id,
            self.sort_value
        )
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

    def click_filter_button(self, event):
        TransactionFilterController(
            self.parent,
            self.header,
            self.user_id
        )

    def bind_view(self):
        self.view.add_button.bind(
            "<ButtonRelease-1>",
            self.header.click_add_transaction
        )
        self.view.filter_button.bind(
            "<ButtonRelease-1>",
            self.click_filter_button
        )