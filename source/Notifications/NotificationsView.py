import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import decimal

class NotificationsView(tk.Frame):
    def __init__(self, parent):
        super().__init__(
            parent,
            bg = "#FFFFFF"
        )
        self.parent = parent

    def main(self):
        self.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.7, anchor='center')

        self.treeview = ttk.Treeview(self)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 30))
        style.configure("Treeview", font=(None, 20), rowheight=40)

        self.treeview.heading("#0", text="Notifications", anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.treeview.yview
        )

        # Configure the Treeview to use the scrollbar
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Place the scrollbar on the right side of the Treeview
        scrollbar.pack(side="right", fill="y")
        self.treeview.pack(fill=tk.BOTH, expand=True)