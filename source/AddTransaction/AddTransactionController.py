from ..Controller import Controller
from .AddTransactionView import AddTransactionView
from .AddTransactionModel import AddTransactionModel


class AddTransactionController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            AddTransactionView(parent),
            AddTransactionModel()
        )
        self.user_id = user_id
        self.view.main()