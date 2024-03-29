import datetime
import decimal
import tkinter as tk
from tkinter import ttk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt
# from source.Transaction import Transaction
# from source.NotificationPage import NotificationPage
# from source.displayaddtransaction import displayaddtransaction

class DashboardView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(
            self.parent,
            bg="#007DB2"
        )

    def main(self):
        self.place(relx=0.05, rely=0.1, relwidth=0.65, relheight=0.35)

        self.create_account_frame()

        self.alerts = tk.Frame(self.parent, bg="#007DB2")
        self.alerts.place(relx=0.75, rely=0.1, relwidth=0.2, relheight=0.35)

        self.alerts_frame = tk.Frame(self.alerts, bg="#FFFFFF")        
        self.alerts_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.graph = tk.Frame(self.parent, bg="#007DB2")
        self.graph.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.3)

        self.graph_frame = tk.Frame(self.graph, bg="#FFFFFF")        
        self.graph_frame.place(relx=0.002, rely=0.01, relwidth=0.996, relheight=0.98)

    def create_account_frame(self):
        self.account_frame = tk.Frame(self, bg="#FFFFFF")        
        self.account_frame.place(relx=0.004, rely=0.01, relwidth=0.992, relheight=0.98)

        self.account_name = tk.Label(self.account_frame,
            bg="#FFFFFF",
            font=('Arial', 20),
        )
        self.account_name.place(relx=0.03, rely=0.1)

    def create_latest_transaction_labels(self, transactions):
        for i, transaction in enumerate(transactions):
            transaction_date = tk.Label(
                self.account_frame,
                text = transaction[4].strftime("%x"),
                bg = "#FFFFFF",
                font = ("Arial", 15),
            )
            transaction_date.place(
                relx = 0.03,
                rely = 0.35 + (0.15 * (i + 1))
            )

            transaction_name = tk.Label(
                self.account_frame,
                text = transaction[1],
                bg = "#FFFFFF",
                font = ("Arial", 15)
            )
            transaction_name.place(
                relx = 0.2,
                rely = 0.35 + (0.15 * (i + 1))
            )

            amount = decimal.Decimal(transaction[3])
            amount = amount.quantize(decimal.Decimal("0.00"))
            if amount < 0:
                amount_text = f"{amount} €" 
            else:
                amount_text = f"+{amount} €"
            transaction_amount = tk.Label(
                self.account_frame,
                text = amount_text,
                bg = "#FFFFFF",
                font = ("Arial", 15)
            )
            transaction_amount.place(
                relx = 0.97,
                rely = 0.35 + (0.15 * (i + 1)),
                anchor = "ne"
            )