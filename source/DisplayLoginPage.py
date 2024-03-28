import tkinter as tk

class DisplayLoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("login page")
        self.geometry("1440x1024")
        self.configure(bg='#FFFFFF')

        self.frame_width = 700
        self.frame_height = 850
        self.main()

    def main(self):
        self.create_frame()
        self.create_titletext()
        self.create_email()
        self.create_password()
        self.create_connexionbutton()
        self.create_clickabletext()

    def create_frame(self):
        x = (self.winfo_screenwidth() - self.frame_width) // 2
        y = (self.winfo_screenheight() - self.frame_height) // 2

        self.frame = tk.Frame(self, width=self.frame_width, height=self.frame_height)
        self.frame.config(background='#72D5FF')
        self.frame.place(x=x, y=y)

    def create_titletext(self):
        text_label = tk.Label(self.frame, text="Saisissez vos identifiants :", font=("Arial", 40), bg='#72D5FF')
        text_label.pack(side=tk.TOP, pady=20)

    def create_email(self):
        self.email_entry = tk.Entry(self.frame, font=("Arial", 32), bg='#FFFFFF')
        additional_text = tk.Label(self.frame, text="Email :", font=("Arial", 32), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=40)
        self.email_entry.pack(side=tk.TOP, pady=10)

    def create_password(self):
        self.password_entry = tk.Entry(self.frame, font=("Arial", 32))
        additional_text = tk.Label(self.frame, text="Mot de passe :", font=("Arial", 32), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=40)
        self.password_entry.pack(side=tk.TOP, pady=10)

    def create_connexionbutton(self):
        connexion_button = tk.Button(self.frame, text="Connexion", font=("Arial", 32), bg= "#FFFFFF", width=10, height=2, command=self.on_connection)
        connexion_button.pack(side=tk.TOP, pady=40)

    def on_connection(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        print("Email:", email)
        print("Password:", password)

    def create_clickabletext(self):
        clickable_text = tk.Label(self.frame, text="Pas encore de compte ? Inscrivez-vous", font=("Arial", 26), bg='#72D5FF')
        clickable_text.pack(side=tk.TOP, pady=20)
        #clickable_text.bind("<Button-1>", self.open_registration_page)

if True:
    app = DisplayLoginPage()
    app.mainloop()