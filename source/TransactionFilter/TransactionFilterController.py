from ..Controller import Controller
from .TransactionFilterView import TransactionFilterView
from .TransactionFilterModel import TransactionFilterModel


class TransactionFilterController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            TransactionFilterView(parent),
            TransactionFilterModel()
        )
        self.header = header
        self.user_id = user_id
        self.view.main()