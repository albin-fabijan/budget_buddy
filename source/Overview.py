import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from source.Header import Header
import decimal

class Overview():
    def __init__(self) :
        self.transactions = [10.90, -40, -20, 280, 50, 0, -160]

    def run(self, window, first_name, last_name):
        header = Header()
        header.run(window, first_name, last_name)

        window.account = tk.Frame(window, bg="#007DB2")
        window.account.place(relx=0.05, rely=0.25, relwidth=0.65, relheight=0.3)

        window.account_frame = tk.Frame(window.account, bg="#FFFFFF")        
        window.account_frame.place(relx=0.004, rely=0.01, relwidth=0.992, relheight=0.98)

        window.alerts = tk.Frame(window, bg="#007DB2")
        window.alerts.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.3)

        window.alerts_frame = tk.Frame(window.alerts, bg="#FFFFFF")        
        window.alerts_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        window.graph = tk.Frame(window, bg="#007DB2")
        window.graph.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.3)

        window.graph_frame = tk.Frame(window.graph, bg="#FFFFFF")        
        window.graph_frame.place(relx=0.002, rely=0.01, relwidth=0.996, relheight=0.98)
        self.plot_graph1(window)
        self.account(window, first_name, last_name)

    def account(self, window, first_name, last_name) :
        account_name = tk.Label(window.account_frame,
            text="Compte de " + first_name + " " + last_name,
            bg="#FFFFFF",
            font=('Arial', 20),
        )
        account_name.place(relx=0.03, rely=0.1)

        amount = 0
        for tr in self.transactions :
            amount += tr

        # Converting the above number into decimal  
        decimal_value = decimal.Decimal(amount)
        
        # rounding off  
        rounded_amount = decimal_value.quantize(decimal.Decimal('0.00')) 

        symbol = ""
        if (amount < 0) :
            symbol = "-"
        else :
            symbol = "+"

        account_amount = tk.Label(window.account_frame,
            text=symbol + " " + str(rounded_amount) + "€",
            bg="#FFFFFF",
            font=('Arial', 20),
        )
        account_amount.place(relx=0.97, rely=0.1, anchor='ne')

        count_transactions = 0
        i = 0

        while count_transactions < 3 :
            tr = self.transactions[-1-i]
            date = 27-i
            if (tr != 0) :
                transaction_text = tk.Label(window.account_frame,
                    text=str(date) + "/3   Nom de la transaction",
                    bg="#FFFFFF",
                    font=('Arial', 15),
                )
                transaction_text.place(relx=0.03, rely=0.35+(0.15*count_transactions))
                decimal_tr = decimal.Decimal(tr)
                rounded_tr = decimal_tr.quantize(decimal.Decimal('0.00'))
                symbol = ""
                if (tr < 0) :
                    symbol = "-"
                    rounded_tr *= -1
                else :
                    symbol = "+"
                transaction_amount = tk.Label(window.account_frame,
                    text=symbol + " " + str(rounded_tr) + "€",
                    bg="#FFFFFF",
                    font=('Arial', 15),
                )
                transaction_amount.place(relx=0.97, rely=0.35+(0.15*count_transactions), anchor='ne')
                count_transactions += 1
            i += 1
            

    def plot_graph1(self, window):
        fig, ax = plt.subplots(figsize=(13.15, 5.81))

        dates = ['21/3', '22/3', '23/3', '24/3', '25/3', '26/3', '27/3']
        counts = []
        bar_colors = []
        for tr in self.transactions :
            if (tr < 0) :
                counts.append(tr*-1)
                bar_colors.append('tab:red')
            else :
                counts.append(tr)
                bar_colors.append('tab:blue')

        ax.bar(dates, counts, color=bar_colors)

        ax.set_ylabel('en €')
        ax.set_title('Dépenses et Revenus')

        canvas1 = FigureCanvasTkAgg(fig, master=window.graph_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack()