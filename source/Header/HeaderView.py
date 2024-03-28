import tkinter as tk
from tkinter import ttk

from ..Paths import Paths as p


class HeaderView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent, bg="#75D5FF")

    def main(self):
        self.place_frame()
        self.create_logo()
        self.create_name()
        self.create_logout_button()
        self.create_button_1()
        self.create_button_2()
        self.create_button_3()
        self.create_content_frame()

    def place_frame(self):
        self.place(relx=0, rely=0, relwidth=1, relheight=0.1)

    def create_logo(self):
        self.logo = tk.PhotoImage(file=p().select_image_file("acajou_accounts.png"))
        self.logo = self.logo.subsample(9)

        logo_label = tk.Label(
            self,
            image=self.logo,
            background="#72D5FF"
        )
        logo_label.place(relx=0.01, rely=0, relheight=1)

    def create_name(self):
        self.name = tk.Label(
            self,
            font=('Arial', 15),
            foreground="black",
            background= '#72D5FF'
        )
        self.name.place(relx=0.33333, rely=0, relwidth=0.33333, relheight=1)

    def create_logout_button(self):
        self.switch = tk.PhotoImage(file=p().select_image_file("switch_off.png"))
        self.switch = self.switch.subsample(40)

        self.logout_button = tk.Button(
            self,
            width=50,
            height=50,
            background="#007DB2",
            foreground="black",
            image=self.switch,
            borderwidth=0,
            cursor="hand2",
        )
        self.logout_button.place(relx=0.995, rely=0.5, anchor='e')

    def create_button_1(self):
        self.button1 = tk.Button(
            self.parent,
            text="Ajouter une transaction",
            background="#40AFFF",
            foreground="black",
            activebackground="#005897",
            borderwidth=0,
            font=('Arial', 12),
            cursor="hand2",
        )
        self.button1.place(relx=0, rely=0.1, relwidth=0.33333, relheight=0.06)

    def create_button_2(self):
        self.button2 = tk.Button(
            self.parent,
            text="Comptes",
            background="#007DB2",
            foreground="black",
            activebackground="#005897",
            borderwidth=0,
            font=('Arial', 12),
            cursor="hand2",
        )
        self.button2.place(relx=0.33333, rely=0.1, relwidth=0.33333, relheight=0.06)

    def create_button_3(self):
        self.button3 = tk.Button(
            self.parent,
            text="Recherche filtrée",
            background="#40AFFF",
            foreground="black",
            activebackground="#005897",
            borderwidth=0,
            font=('Arial', 12),
            cursor="hand2",
        )
        self.button3.place(relx=0.66666, rely=0.1, relwidth=0.33333, relheight=0.06)

    def create_content_frame(self):
        self.content_frame = tk.Frame(
            self.parent,
            background="#FFFFFF"
        )
        self.content_frame.place(relx=0, rely=0.16, relwidth=1, relheight=0.9)
