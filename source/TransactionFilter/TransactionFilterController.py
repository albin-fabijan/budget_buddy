from datetime import datetime
import re
from tkinter import END

from ..Controller import Controller
from .TransactionFilterView import TransactionFilterView
from .TransactionFilterModel import TransactionFilterModel


class TransactionFilterController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            TransactionFilterView(parent),
            None
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
    
    def is_date_valid(self, date_string):
        # "DD/MM/YYYY"
        date_regex = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
        return bool(re.match(date_regex, date_string))

    def is_date_order_good(self):
        min_date = self.view.date_min_entry.get()
        max_date = self.view.date_max_entry.get()

        min_date = datetime.strptime(min_date, "%d/%m/%Y")
        max_date = datetime.strptime(max_date, "%d/%m/%Y")

        return min_date < max_date

    def invalid_date_error(self):
        min_date = self.view.date_min_entry.get()
        max_date = self.view.date_max_entry.get()

        if not self.is_date_valid(min_date) or not self.is_date_valid(max_date):
            self.view.create_message_box(
                "Dates invalides",
                "Il faut que les dates suivent ce format:\n"
                "JJ/MM/AAAA"
            )
            return True

        # If dates are valid, then check the order
        if not self.is_date_order_good():
            self.view.create_message_box(
                "Ordre de dates incorrect",
                "La date de début doit être antérieure à la date de fin."
            )
            return True

        return False


    def convert_to_sql_date_range(self, min_date, max_date):
        sql_date_format = "%Y-%m-%d 00:00:00"

        min_date = datetime.strptime(min_date, "%d/%m/%Y")
        min_date = min_date.strftime(sql_date_format)

        max_date = datetime.strptime(max_date, "%d/%m/%Y")
        max_date = max_date.strftime(sql_date_format)

        date_range = f"AND {min_date} < t_date < {max_date} "
        return date_range

    def apply_filter_button(self, event):
        min_date = self.view.date_min_entry.get()
        max_date = self.view.date_max_entry.get()
        date_range = ""

        if not (min_date == "" and max_date == ""):
            if self.invalid_date_error():
                return
            date_range = self.convert_to_sql_date_range(min_date, max_date)

        type_values = {
            "...": "",
            "Revenus": "AND t_amount >= 0 ",
            "Dépenses": "AND t_amount < 0 "
        }
        sort_values = {
            "Récent → Ancien": "ORDER BY t_date DESC;",
            "Ancient → Récent": "ORDER BY t_date ASC;",
            "Montant décroissant": "ORDER BY t_amount DESC;",
            "Montant croissant": "ORDER BY t_amount ASC;"
        }
        selected_type = type_values[self.view.type_var.get()]
        selected_sort = sort_values[self.view.sort_var.get()]

        self.view.destroy() 
        return (selected_type, date_range, selected_sort)

    def bind_view(self):
        self.view.erase_button.bind(
            "<ButtonRelease-1>",
            self.reset_filter_options
        )
        self.view.apply_button.bind(
            "<ButtonRelease-1>",
            self.apply_filter_button
        )