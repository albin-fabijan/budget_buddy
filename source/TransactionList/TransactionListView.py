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
        self.create_filter_button()
        self.create_add_button()

    def create_frame(self):
        self.place(
            anchor=tk.CENTER,
            relx=0.5,
            rely=0.5,
            width=730,
            height=500
        )

    def create_treeview(self):
        self.tree = ttk.Treeview(self.parent)
        self.tree["columns"] = ("1", "2", "3", "4")
        self.tree.column("#0", width=0, stretch=tk.NO)
        for column in self.tree["columns"]:
            self.tree.column(column, anchor = tk.W, width = 100)

        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("1", text="Date", anchor=tk.W)
        self.tree.heading("2", text="Nom", anchor=tk.W)
        self.tree.heading("3", text="Description", anchor=tk.W)
        self.tree.heading("4", text="Montant", anchor=tk.W)

        self.tree.column("1", width=11)
        self.tree.column("2", width=20)
        self.tree.column("3", width=270)
        self.tree.column("4", width=20)

        self.scrollbar = tk.Scrollbar(
            self.tree,
            orient=tk.VERTICAL,
            command=self.tree.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.config(yscrollcommand=self.scrollbar.set)
        self.tree.place(
            anchor=tk.CENTER,
            relx=0.5,
            rely=0.5,
            width=730,
            height=500
        )
        self.tree.tag_configure("Treeview", font=("Arial", 12))

    def create_filter_button(self):
        self.filter_button = tk.Button(
            self.parent,
            text="Filtrer",
            font=("Arial", 16,),
            width=10,
            height=1
        )
        self.filter_button.place(x=274, y=32)

    def create_add_button(self):
        self.add_button = tk.Button(
            self.parent,
            text="+",
            font=("Arial", 16,),
            width=2,
            height=1
        )
        self.add_button.place(x=971, y=32)