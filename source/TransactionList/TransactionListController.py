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
