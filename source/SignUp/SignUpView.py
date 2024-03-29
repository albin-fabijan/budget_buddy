import tkinter as tk
from tkinter import messagebox


class SignUpView(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(
            self.parent,
        )

    def main(self):
        self.place_frame()
        self.create_titletext()
        self.create_firstname()
        self.create_lastname()
        self.create_email()
        self.create_password()
        self.create_signup_button()

    def place_frame(self):
        self.config(background='#72D5FF')
        self.place(
            anchor=tk.CENTER,
            relheight = 1,
            relwidth = 0.5,
            relx = 0.5,
            rely = 0.5
        )

    def create_titletext(self):
        text_label = tk.Label(
            self,
            text="inscription :",
            font=("Arial", 26),
            bg='#72D5FF'
        )
        text_label.pack(side=tk.TOP, pady=20)

    def create_firstname(self):
        self.first_name_entry = tk.Entry(self, font=("Arial", 20))
        additional_text = tk.Label(
            self,
            text="Nom :",
            font=("Arial", 20),
            bg='#72D5FF',
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.first_name_entry.pack(side=tk.TOP, pady=5)

    def create_lastname(self):
        self.last_name_entry = tk.Entry(self, font=("Arial", 20))
        additional_text = tk.Label(
            self,
            text="Prénom :",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.last_name_entry.pack(side=tk.TOP, pady=5)
    
    def create_email(self):
        self.email_entry = tk.Entry(self, font=("Arial", 20))
        additional_text = tk.Label(
            self,
            text="Email :",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.email_entry.pack(side=tk.TOP, pady=5)
    
    def create_password(self):
        self.password_entry = tk.Entry(
            self,
            font=("Arial", 20),
            show="*"
        )
        additional_text = tk.Label(
            self,
            text="Mot de passe :",
            font=("Arial", 20),
            bg='#72D5FF'
        )
        additional_text.pack(side=tk.TOP, pady=10)
        self.password_entry.pack(side=tk.TOP, pady=5)

    def create_signup_button(self):
        self.signup_button = tk.Button(
            self,
            text="Inscription",
            font=("Arial", 20),
            bg='white',
            width=10,
            height=2,
        )
        self.signup_button.pack(side=tk.TOP, pady=40)

    def create_message_box(self, title, description):
        messagebox.showinfo(title, description)