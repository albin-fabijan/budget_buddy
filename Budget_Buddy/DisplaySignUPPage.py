import tkinter as tk

class DisplaySignUPPAGE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign up page")
        self.geometry("1440x1024")

        self.frame_width = 700
        self.frame_height = 850
        self.main()

    def main(self):
        self.create_frame()
        self.create_titletext()
        self.create_firstname()
        self.creat_lastname()
        self.create_email()
        self.create_password()
        self.create_signupbutton()
        self.on_signup()

    def create_frame(self):
        x = (self.winfo_screenwidth() - self.frame_width) // 2
        y = (self.winfo_screenheight() - self.frame_height) // 2

        self.frame = tk.Frame(self, width=self.frame_width, height=self.frame_height)
        self.frame.config(background='#72D5FF')
        self.frame.place(x=x, y=y)

    def create_titletext(self):
        text_label = tk.Label(self.frame, text="           inscription :           ", font=("Arial", 40), bg='#72D5FF')
        text_label.pack(side=tk.TOP, pady=20)

    def create_firstname(self):
        self.first_name_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Nom :", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.first_name_entry.pack(side=tk.TOP, pady=5)

    def creat_lastname(self):
        self.last_name_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Prénom :", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.last_name_entry.pack(side=tk.TOP, pady=5)
    
    def create_email(self):
        self.email_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Email :", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.email_entry.pack(side=tk.TOP, pady=5)
    
    def create_password(self):
        self.password_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Mot de passe :", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.password_entry.pack(side=tk.TOP, pady=5)

    def create_signupbutton(self):
        signup_button = tk.Button(self.frame, text="Inscription", font=("Arial", 26), bg='white', width=10, height=2, command=self.on_signup)
        signup_button.pack(side=tk.TOP, pady=40)

    def on_signup(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        print("Nom:", first_name)
        print("Prénom:", last_name)
        print("Email:", email)
        print("Password:", password)


if __name__ == "__main__":
    fenetre = DisplaySignUPPAGE()
    fenetre.mainloop()