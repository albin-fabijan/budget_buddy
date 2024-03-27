from functools import partial
import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.width = 700
        self.height = 850
        super().__init__(
            self.parent,
            width=self.width,
            height=self.height,
        )

    def main(self):
        self.place_frame()
        self.create_titletext()
        self.create_email()
        self.create_password()
        self.create_connectionbutton()
        self.create_clickabletext()

    def place_frame(self):
        x = (self.width / 2) / self.parent.width 

        self.config(background='#72D5FF')
        self.place(relx=x, rely=0)

    def create_titletext(self):
        text_label = tk.Label(
            self,
            text="Saisissez vos identifiants :",
            font=("Arial", 40),
            bg='#72D5FF'
        )
        text_label.pack(side=tk.TOP, pady=20)

    def create_email(self):
        self.email_entry = tk.Entry(
            self,
            font=("Arial", 32),
            bg='#FFFFFF'
        )
        additional_text = tk.Label(
            self,
            text="Email :",
            font=("Arial", 32),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=40)
        self.email_entry.pack(side=tk.TOP, pady=10)

    def create_password(self):
        self.password_entry = tk.Entry(self, font=("Arial", 32))
        additional_text = tk.Label(
            self,
            text="Mot de passe :",
            font=("Arial", 32),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=40)
        self.password_entry.pack(side=tk.TOP, pady=10)

    def create_connectionbutton(self):
        self.connection_button = tk.Button(
            self,
            text="connection",
            font=("Arial", 32),
            bg= "#FFFFFF",
            width=10,
            height=2,
        )
        self.connection_button.pack(side=tk.TOP, pady=40)

    def create_clickabletext(self):
        clickable_text = tk.Label(
            self,
            text="Pas encore de compte ? Inscrivez-vous",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        clickable_text.pack(side=tk.TOP, pady=20)
