import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from source.Header import Header
from source.Transaction import Transaction
import decimal

class NotificationPage():
    def __init__(self, overview) :
        self.overview = overview
        self.header = Header()

    def example_add(self) :
        error_popup = tk.Toplevel()
        error_popup.title("Erreur")
        error_popup.geometry("400x100")
        error_popup.configure(bg='#FFFFFF')
        error_label = tk.Label(error_popup, text="Impossible de créer une transaction depuis les notifications", font=("Arial", 10), bg='#FFFFFF')
        error_label.pack(side=tk.TOP, pady=10)
        error_button = tk.Button(error_popup, text="OK", font=("Arial", 20), bg='white', width=10, height=2, command=error_popup.destroy)
        error_button.pack(side=tk.TOP, pady=10)
        error_popup.mainloop()

    def example_account(self, window) :
        self.clear(window)
        self.overview.run(window, "Djibril", "Mimouni")

    def example_search(self) :
        print("aller vers la recherche")

    def run(self, window, first_name, last_name, notifications):
        self.header.run(window, first_name, last_name, self.example_add, lambda : self.example_account(window), self.example_search)

        window.notif = tk.Frame(window.content, bg="#FFFFFF")
        window.notif.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.7, anchor='center')

        treeview = ttk.Treeview(window.notif)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 30))
        style.configure("Treeview", font=(None, 20), rowheight=40)

        treeview.heading("#0", text="Notifications", anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(window.notif, orient="vertical", command=treeview.yview)

        # Configure the Treeview to use the scrollbar
        treeview.configure(yscrollcommand=scrollbar.set)

        # Place the scrollbar on the right side of the Treeview
        scrollbar.pack(side="right", fill="y")

        for i in range(len(notifications)) :
            treeview.insert(parent="", index=tk.END, text=notifications[-1-i])

        treeview.pack(fill=tk.BOTH, expand=True)

    def clear(self, window) :
        self.header.clear_page(window)