import tkinter as tk
from tkinter import messagebox


class SignUpView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.width = 700
        self.height = 850
        super().__init__(
            self.parent,
            width = self.width,
            height = self.height
        )

    def main(self):
        self.place_frame()
        self.create_titletext()
        self.create_firstname()
        self.creat_lastname()
        self.create_email()
        self.create_password()
        self.create_signup_button()

    def place_frame(self):
        x = (self.width / 2) / self.parent.width

        self.config(background='#72D5FF')
        self.place(relx=x, y=0)

    def create_titletext(self):
        text_label = tk.Label(
            self,
            text="           inscription :           ",
            font=("Arial", 40),
            bg='#72D5FF'
        )
        text_label.pack(side=tk.TOP, pady=20)

    def create_firstname(self):
        self.first_name_entry = tk.Entry(self, font=("Arial", 26))
        additional_text = tk.Label(
            self,
            text="Nom :",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.first_name_entry.pack(side=tk.TOP, pady=5)

    def creat_lastname(self):
        self.last_name_entry = tk.Entry(self, font=("Arial", 26))
        additional_text = tk.Label(
            self,
            text="Prénom :",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.last_name_entry.pack(side=tk.TOP, pady=5)
    
    def create_email(self):
        self.email_entry = tk.Entry(self, font=("Arial", 26))
        additional_text = tk.Label(
            self,
            text="Email :",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.email_entry.pack(side=tk.TOP, pady=5)
    
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
        additional_text.pack(side=tk.TOP, pady=10)
        self.password_entry.pack(side=tk.TOP, pady=5)

    def create_signup_button(self):
        self.signup_button = tk.Button(
            self,
            text="Inscription",
            font=("Arial", 26),
            bg='white',
            width=10,
            height=2,
        )
        self.signup_button.pack(side=tk.TOP, pady=40)

    def create_message_box(self, title, description):
        messagebox.showinfo(title, description)