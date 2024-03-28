import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from source.Header import Header
from source.Transaction import Transaction
from source.NotificationPage import NotificationPage
import decimal

class Overview():
    def __init__(self) :
        t1 = Transaction("Carte à gratter", "21/3", 10000)
        t2 = Transaction("Las Vegas", "22/3", -9000)
        t3 = Transaction("Franprix", "23/3", -10.90)
        t4 = Transaction("Babysitting", "24/3", 280)
        t5 = Transaction("Burger King", "25/7", -15)
        t6 = Transaction("Rien", "26/3", 0)
        t7 = Transaction("Loyer", "27/3", -160)
        self.transactions = [t1, t2, t3, t4, t5, t6, t7]
        self.notifications = []
        self.notifications_clicked = False
        self.header = Header()
        self.init_notif()

    def example_add(self) :
        print("ajouter une transaction")

    def example_account(self) :
        print("aller vers les comptes")

    def example_search(self) :
        print("aller vers la recherche")

    def on_notif_clicked(self, window) :
        notifications = NotificationPage(self)
        self.clear(window)
        notifications.run(window, "Djibril", "Mimouni", self.notifications)

    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    tk.Canvas.create_circle = _create_circle

    def run(self, window, first_name, last_name):
        header = Header()
        header.run(window, first_name, last_name, self.example_add, self.example_account, self.example_search)

        window.account = tk.Frame(window.content, bg="#007DB2")
        window.account.place(relx=0.05, rely=0.1, relwidth=0.65, relheight=0.35)

        window.account_frame = tk.Frame(window.account, bg="#FFFFFF")        
        window.account_frame.place(relx=0.004, rely=0.01, relwidth=0.992, relheight=0.98)

        window.alerts = tk.Frame(window.content, bg="#007DB2")
        window.alerts.place(relx=0.75, rely=0.1, relwidth=0.2, relheight=0.35)

        window.alerts_frame = tk.Frame(window.alerts, bg="#FFFFFF")        
        window.alerts_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        window.graph = tk.Frame(window.content, bg="#007DB2")
        window.graph.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.3)

        window.graph_frame = tk.Frame(window.graph, bg="#FFFFFF")        
        window.graph_frame.place(relx=0.002, rely=0.01, relwidth=0.996, relheight=0.98)
        self.plot_graph(window)
        self.account(window, first_name, last_name)
        self.notification_scroll(window)

    def clear(self, window) :
        self.header.clear_page(window)

    def account(self, window, first_name, last_name) :
        account_name = tk.Label(window.account_frame,
            text="Compte de " + first_name + " " + last_name,
            bg="#FFFFFF",
            font=('Arial', 20),
        )
        account_name.place(relx=0.03, rely=0.1)

        amount = 0
        for tr in self.transactions :
            amount += tr.amount

        # Converting the above number into decimal  
        decimal_value = decimal.Decimal(amount)
        
        # rounding off  
        rounded_amount = decimal_value.quantize(decimal.Decimal('0.00')) 

        symbol = ""
        if (amount < 0) :
            symbol = "-"
            rounded_amount *= -1
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
            tr = self.transactions[-1-i].amount
            date = self.transactions[-1-i].date
            name = self.transactions[-1-i].name
            if (tr != 0) :
                transaction_date = tk.Label(window.account_frame,
                    text=str(date),
                    bg="#FFFFFF",
                    font=('Arial', 15),
                )
                transaction_date.place(relx=0.03, rely=0.35+(0.15*count_transactions))
                transaction_text = tk.Label(window.account_frame,
                    text=name,
                    bg="#FFFFFF",
                    font=('Arial', 15),
                )
                transaction_text.place(relx=0.12, rely=0.35+(0.15*count_transactions))
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
            
    def notification_scroll(self, window) :
        canvas = tk.Canvas(window, width=40, height=40, borderwidth=0, highlightthickness=0,
                   bg="white")
        button = tk.Button(window,
            background="red",
            foreground="white",            
            activebackground="#DD0000",
            borderwidth=0,
            text=len(self.notifications),
            font=('Arial', 12),
            cursor="hand2",
            command=lambda : self.on_notif_clicked(window)
        )
        if (len(self.notifications) > 0) :
            canvas.place(relx=0.95, rely=0.25, anchor="center")
            canvas.create_circle(20, 20, 20, fill="red", outline="#F00")
            button.place(relx=0.95, rely=0.25, anchor="center", width=25, height=25)
            canvas.create_text(20, 20, font=('Arial', 16), text=str(len(self.notifications)), fill='white')
            for i in range(len(self.notifications)) :
                if (i < 5) : 
                    transaction_text = tk.Label(window.alerts_frame,
                        text=self.notifications[-1-i],
                        bg="#FFFFFF",
                        font=('Arial', 15),
                    )
                    transaction_text.place(relx=0.1, rely=0.15+(0.15*i))
        else :
            transaction_text = tk.Label(window.alerts_frame,
                text="Notifications",
                bg="#FFFFFF",
                font=('Arial', 15),
            )
            transaction_text.place(relx=0.5, rely=0.15, anchor="center")

    def init_notif(self) :
        amount = 0
        for tr in self.transactions :
            if (tr.amount < -500 or tr.amount > 500) :
                self.notifications.append("Transaction conséquente le " + tr.date + ", " + str(tr.amount) + "€")
            amount += tr.amount
            if (amount < 0) :
                self.notifications.append("Découvert le " + tr.date)
            elif (amount > 2000) :
                self.notifications.append("Plafond dépassé le " + tr.date)

    def plot_graph(self, window):
        fig, ax = plt.subplots(figsize=(13.15, 5.81))
        amount = 0
        dates = []
        for tr in self.transactions :
            dates.append(tr.date)
        counts = []
        bar_colors = []
        for tr in self.transactions :
            if (tr.amount < 0) :
                counts.append(tr.amount*-1)
                bar_colors.append('tab:red')
            else :
                counts.append(tr.amount)
                bar_colors.append('tab:blue')
            amount += tr.amount
        ax.bar(dates, counts, color=bar_colors)
        ax.set_ylabel('en €')
        ax.set_title('Dépenses et Revenus')

        canvas1 = FigureCanvasTkAgg(fig, master=window.graph_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack()