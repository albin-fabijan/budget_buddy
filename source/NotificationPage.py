import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import decimal

class NotificationPage(tk.Frame):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            bg = "#FFFFFF"
        )
        self.parent = parent
        self.header = header
        self.user_id = user_id
        self.main()

    def example_add(self):
        error_popup = tk.Toplevel()
        error_popup.title("Erreur")
        error_popup.geometry("400x100")
        error_popup.configure(bg='#FFFFFF')
        error_label = tk.Label(error_popup, text="Impossible de créer une transaction depuis les notifications", font=("Arial", 10), bg='#FFFFFF')
        error_label.pack(side=tk.TOP, pady=10)
        error_button = tk.Button(error_popup, text="OK", font=("Arial", 20), bg='white', width=10, height=2, command=error_popup.destroy)
        error_button.pack(side=tk.TOP, pady=10)
        error_popup.mainloop()

    def main(self):
        self.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.7, anchor='center')

        treeview = ttk.Treeview(self)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 30))
        style.configure("Treeview", font=(None, 20), rowheight=40)

        treeview.heading("#0", text="Notifications", anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=treeview.yview)

        # Configure the Treeview to use the scrollbar
        treeview.configure(yscrollcommand=scrollbar.set)

        # Place the scrollbar on the right side of the Treeview
        scrollbar.pack(side="right", fill="y")

        for i in range(len(notifications)) :
            treeview.insert(parent="", index=tk.END, text=notifications[-1-i])

        treeview.pack(fill=tk.BOTH, expand=True)