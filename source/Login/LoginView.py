from functools import partial
import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(
            self.parent,
        )

    def main(self):
        self.place_frame()
        self.create_titletext()
        self.create_email()
        self.create_password()
        self.create_connectionbutton()
        self.create_clickabletext()

    def place_frame(self):
        self.config(background='#72D5FF')
        self.pack(fill=tk.Y, expand=True, anchor=tk.CENTER)

    def create_titletext(self):
        text_label = tk.Label(
            self,
            text="Saisissez vos identifiants :",
            font=("Arial", 32),
            bg='#72D5FF'
        )
        text_label.pack(side=tk.TOP, pady=20)

    def create_email(self):
        self.email_entry = tk.Entry(
            self,
            font=("Arial", 26),
            bg='#FFFFFF'
        )
        additional_text = tk.Label(
            self,
            text="Email :",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=40)
        self.email_entry.pack(side=tk.TOP, pady=10)

    def create_password(self):
        self.password_entry = tk.Entry(
            self,
            font=("Arial", 26),
            show="*"
        )
        additional_text = tk.Label(
            self,
            text="Mot de passe :",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=40)
        self.password_entry.pack(side=tk.TOP, pady=10)

    def create_connectionbutton(self):
        self.connection_button = tk.Button(
            self,
            text="connection",
            font=("Arial", 26),
            bg= "#FFFFFF",
            width=10,
            height=2,
        )
        self.connection_button.pack(side=tk.TOP, pady=40)

    def create_clickabletext(self):
        self.clickable_text = tk.Label(
            self,
            text="Pas encore de compte ? Inscrivez-vous",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        self.clickable_text.pack(side=tk.TOP)

    def create_message_box(self, title, description):
        messagebox.showinfo(title, description)