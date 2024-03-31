import tkinter as tk

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
        self.date_var = tk.IntVar(value=0)

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
            "Montant croissant",
            "Montant décroissant",
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

        de_label = tk.Label(self, text="De", font=("Arial", 14), bg='#72D5FF')
        de_label.place(x=120, y=250)

        self.date_minentry = tk.Entry(self, font=("Arial", 16), width=7)
        self.date_minentry.place(x=150, y=250)

        a_label = tk.Label(self, text="à", font=("Arial", 14), bg='#72D5FF')
        a_label.place(x=230, y=250)

        self.date_maxentry = tk.Entry(self, font=("Arial", 16), width=7)
        self.date_maxentry.place(x=250, y=250)

    def create_erase_button(self):
        erase_button = tk.Button(
            self,
            text="Effacer",
            font=("Arial", 16),
        )
        erase_button.place(x=250, y=350)

    def create_apply_button(self):
        apply_button = tk.Button(
            self,
            text="Appliquer",
            font=("Arial", 16),
        )
        apply_button.place(x=50, y=350)
