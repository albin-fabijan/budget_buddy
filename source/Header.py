import tkinter as tk
from tkinter import ttk

class Header():
    def run(self, window):
        window.header = tk.Frame(window, bg="#72D5FF")
        window.header.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        icon = tk.PhotoImage(file='budget_buddy/images/acajou_accounts.png')
        switch = tk.PhotoImage(file='budget_buddy/images/switch_off.png')
        window.logo = icon.subsample(9)
        window.switch = switch.subsample(40)

        logo_label = tk.Label(window.header,
            image=window.logo,
            background="#72D5FF"
        )
        logo_label.place(relx=0.01, rely=0, relheight=1)

        name = tk.Label(window.header,
            text="Nom Prenom",
            font=('Arial', 15),
            foreground="black",
            background= '#72D5FF'
        )
        name.place(relx=0.33333, rely=0, relwidth=0.33333, relheight=1)

        logout_button = tk.Button(window.header,
            width=50,
            height=50,
            background="#007DB2",
            foreground="black",
            image=window.switch,
            borderwidth=0
        )
        logout_button.place(relx=0.995, rely=0.5, anchor='e')

        button1 = tk.Button(window,
            text="1",
            background="#40AFFF",
            foreground="black",
            activebackground="#005897",
            borderwidth=0
        )
        button1.place(relx=0, rely=0.1, relwidth=0.33333, relheight=0.06)

        button2 = tk.Button(window,
            text="2",
            background="#007DB2",
            foreground="black",
            activebackground="#005897",
            borderwidth=0
        )
        button2.place(relx=0.33333, rely=0.1, relwidth=0.33333, relheight=0.06)

        button3 = tk.Button(window,
            text="3",
            background="#40AFFF",
            foreground="black",
            activebackground="#005897",
            borderwidth=0
        )
        button3.place(relx=0.66666, rely=0.1, relwidth=0.33333, relheight=0.06)