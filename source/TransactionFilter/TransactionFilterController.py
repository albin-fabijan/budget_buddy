from tkinter import END

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
        self.bind_view()

    def reset_filter_options(self, event):
        self.view.sort_var.set("Récent → Ancien")
        self.view.type_var.set("...")
        self.view.date_min_entry.delete(0, END)
        self.view.date_max_entry.delete(0, END)

    def bind_view(self):
        self.view.erase_button.bind(
            "<ButtonRelease-1>",
            self.reset_filter_options
        )