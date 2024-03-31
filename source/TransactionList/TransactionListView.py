import tkinter as tk
from tkinter import ttk

class TransactionListView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(
            self.parent,
            bg = "#72D5FF"
        )

    def main(self):
        self.create_frame()
        self.create_treeview()
        self.create_filterbutton()
        self.create_add_button()

    def create_frame(self):
        self.place(relx=0.2, rely=0.25 , width=730, height=500)

    def create_treeview(self):
        self.tree = ttk.Treeview(self.parent)
        self.tree["columns"] = ("1", "2", "3")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("1", anchor=tk.W, width=100)
        self.tree.column("2", anchor=tk.W, width=100)
        self.tree.column("3", anchor=tk.W, width=100)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("1", text="Date", anchor=tk.W)
        self.tree.heading("2", text="Nom", anchor=tk.W)
        self.tree.heading("3", text="Montant", anchor=tk.W)

        self.tree.column("1", width=10)
        self.tree.column("2", width=20)
        self.tree.column("3", width=300)
        self.tree.place(relx=0.2, rely=0.25, width=730, height=500)

    def create_filterbutton(self):
        self.filter_button = tk.Button(
            self.parent,
            text="Filtrer",
            font=("Arial", 16,),
            width=10,
            height=1
        )
        self.filter_button.place(x=260, y=120)

    def create_add_button(self):
        self.add_button = tk.Button(
            self.parent,
            text="+",
            font=("Arial", 16,),
            width=2,
            height=1
        )
        self.add_button.place(x=950, y=120)