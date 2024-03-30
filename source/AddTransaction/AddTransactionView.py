import tkinter as tk

class AddTransactionView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg = "#72D5FF"
        )
        self.parent = parent
        self.title("Add transaction")
        self.geometry("428x550")

    def main(self):
        self.create_frame()
        self.create_name()   
        self.create_amount()
        self.create_type()
        self.create_description()
        self.create_addbutton()

    def create_frame(self):
        self.frame = tk.Frame(
            self,
            height=100,
            background = "#72D5FF"
        )
        self.frame.config(background='#72D5FF')
        self.frame.place(relwidth = 1)

    def create_name(self):
        self.name_entry = tk.Entry(
            self.frame,
            font=("Arial", 20)
        )
        additional_text = tk.Label(
            self.frame,
            text="Nom de la transaction:",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=1)
        self.name_entry.pack(side=tk.TOP, pady=1)

    def create_amount(self):
        self.amount_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(
            self.frame,
            text="Montant de la transaction:",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=1)
        self.amount_entry.pack(side=tk.TOP, pady=1)
    
    def create_type(self):
        additional_text = tk.Label(
            self.frame,
            text="Type de la transaction:",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=1)

        options = ["Revenu", "Dépenses"]
        self.selected_option = tk.StringVar(self.frame)
        self.selected_option.set(options[0])
        dropdown = tk.OptionMenu(
            self.frame,
            self.selected_option,
            *options
        )
        dropdown.config(font=("Arial", 14), width=20)
        dropdown.pack(side=tk.TOP, pady=1)

    def create_description(self):
        additional_text = tk.Label(
            self.frame,
            text="Description de la transaction:",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.description_entry = tk.Text(
            self.frame,
            font=("Arial", 20),
            height=5,
            width=20
        )
        self.description_entry.pack(side=tk.TOP, pady=1)

    def create_addbutton(self):
        add_button = tk.Button(
            self.frame,
            text="Ajouter",
            font=("Arial", 20),
            bg='white',
            width=10,
            height=1,
        )
        add_button.pack(side=tk.TOP, pady=1)