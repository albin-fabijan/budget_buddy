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

    def apply_filter_button(self, event):
        type_values = {
            "...": "",
            "Revenus": "AND WHERE t_amount >= 0 ",
            "Dépenses": "AND WHERE t_amount < 0 "
        }
        sort_values = {
            "Récent → Ancien": "ORDER BY t_date DESC;",
            "Ancien → Récent": "ORDER BY t_date ASC;",
            "Montant décroissant": "ORDER BY t_amount DESC;",
            "Montant croissant": "ORDER BY t_amount ASC;"
        }
        selected_type = type_values[self.view.type_var.get()]
        selected_sort = sort_values[self.view.sort_var.get()]
        
        return (selected_type, selected_sort)

    def bind_view(self):
        self.view.erase_button.bind(
            "<ButtonRelease-1>",
            self.reset_filter_options
        )
        self.view.apply_button.bind(
            "<ButtonRelease-1>",
            self.apply_filter_button
        )