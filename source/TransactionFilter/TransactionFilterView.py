import tkinter as tk
from tkinter import messagebox


class TransactionFilterView(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(
            parent,
            bg = "#72D5FF"
        )
        self.title("Filtre")
        self.geometry("400x400")
        self.grab_set()

    def main(self):
        self.sort_var = tk.StringVar(value="Récent → Ancien")
        self.type_var = tk.StringVar(value="...")

        self.create_sort()
        self.create_type()
        self.create_date()
        self.create_erase_button()
        self.create_apply_button()


    def create_sort(self):
        sort_label = tk.Label(
            self,
            text="Order",
            font=("Arial", 16),
            bg='#72D5FF'
        )
        sort_label.place(x=30, y=50)

        sort_options = [
            "Récent → Ancien",
            "Ancient → Récent",
            "Montant décroissant",
            "Montant croissant",
        ]
        self.sort_select = tk.OptionMenu(
            self,
            self.sort_var,
            *sort_options
        )
        self.sort_select.config(font=("Arial", 16), width=15)
        self.sort_select.place(x=150, y=50)

    def create_type(self):
        type_label = tk.Label(
            self,
            text="Type",
            font=("Arial", 16),
            bg='#72D5FF'
        )
        type_label.place(x=30, y=150)

        type_options = ["...", "Revenus", "Dépenses"]
        self.type_select = tk.OptionMenu(self, self.type_var, *type_options)
        self.type_select.config(font=("Arial", 16), width=15)
        self.type_select.place(x=150, y=150)
        
    def create_date(self):
        date_label = tk.Label(
            self,
            text="Date :",
            font=("Arial", 16),
            bg='#72D5FF'
        )
        date_label.place(x=30, y=250)

        from_label = tk.Label(self, text="De", font=("Arial", 14), bg='#72D5FF')
        from_label.place(x=120, y=250)

        self.date_min_entry = tk.Entry(self, font=("Arial", 16), width=9)
        self.date_min_entry.place(x=150, y=250)

        to_label = tk.Label(self, text="à", font=("Arial", 14), bg='#72D5FF')
        to_label.place(x=265, y=250)

        self.date_max_entry = tk.Entry(self, font=("Arial", 16), width=9)
        self.date_max_entry.place(x=280, y=250)

    def create_erase_button(self):
        self.erase_button = tk.Button(
            self,
            text="Effacer",
            font=("Arial", 16),
        )
        self.erase_button.place(x=250, y=350)

    def create_apply_button(self):
        self.apply_button = tk.Button(
            self,
            text="Appliquer",
            font=("Arial", 16),
        )
        self.apply_button.place(x=50, y=350)

    def create_message_box(self, title, description):
        messagebox.showinfo(title, description, parent=self)