import tkinter as tk
from tkinter import ttk

from .Paths import Paths as p


class Header(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent, bg="#75D5FF")
        self.run()

    def run(self):
        self.place(relx=0, rely=0, relwidth=1, relheight=0.18)

        self.icon = tk.PhotoImage(file=p().select_image_file("acajou_accounts.png"))
        self.switch = tk.PhotoImage(file=p().select_image_file("switch_off.png"))
        self.logo = self.icon.subsample(9)
        self.switch = self.switch.subsample(40)

        logo_label = tk.Label(
            self,
            image=self.logo,
            background="#72D5FF"
        )
        logo_label.place(relx=0.01, rely=0, relheight=0.5)

        name = tk.Label(
            self,
            text=f"FirstName LastName",
            font=('Arial', 15),
            foreground="black",
            background= '#72D5FF'
        )
        name.place(relx=0.33333, rely=0, relwidth=0.33333, relheight=0.5)

        logout_button = tk.Button(
            self,
            width=50,
            height=50,
            background="#007DB2",
            foreground="black",
            image=self.switch,
            borderwidth=0,
            cursor="hand2",
        )
        logout_button.place(relx=0.995, rely=0.25, anchor='e')

        button1 = tk.Button(
            self,
            text="Ajouter une transaction",
            background="#40AFFF",
            foreground="black",
            activebackground="#005897",
            borderwidth=0,
            font=('Arial', 12),
            cursor="hand2",
        )
        button1.place(relx=0, rely=0.5, relwidth=0.33333, relheight=0.5)

        button2 = tk.Button(
            self,
            text="Comptes",
            background="#007DB2",
            foreground="black",
            activebackground="#005897",
            borderwidth=0,
            font=('Arial', 12),
            cursor="hand2",
        )
        button2.place(relx=0.33333, rely=0.5, relwidth=0.33333, relheight=0.5)

        button3 = tk.Button(
            self,
            text="Recherche filtrée",
            background="#40AFFF",
            foreground="black",
            activebackground="#005897",
            borderwidth=0,
            font=('Arial', 12),
            cursor="hand2",
        )
        button3.place(relx=0.66666, rely=0.5, relwidth=0.33333, relheight=0.5)