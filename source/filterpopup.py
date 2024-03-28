import tkinter as tk

class filterpopup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Filtre")
        self.geometry("400x400")
        self.configure(bg='#FFFFFF')
        
        self.main()

    def main(self):
        self.ordre_var = tk.IntVar(value=0)
        self.type_var = tk.IntVar(value=0)
        self.date_var = tk.IntVar(value=0)

        self.create_ordre()
        self.create_type()
        self.create_date()
        self.create_eraisedbutton()
        self.create_applybutton()

    def create_ordre(self):
        ordre_label = tk.Label(self, text="Ordre", font=("Arial", 16), bg='#FFFFFF')
        ordre_label.place(x=30, y=50)

        ordre_options = ["montant croissant", "montant décroissant", "date croissante", "date décroissante"]
        self.ordre_select = tk.OptionMenu(self, tk.StringVar(), *ordre_options)
        self.ordre_select.config(font=("Arial", 16), bg='#FFFFFF', width=15)
        self.ordre_select.place(x=150, y=50)

        check_button = tk.Checkbutton(self, variable=self.ordre_var, bg='#FFFFFF')
        check_button.place(x=375, y=55)

    def create_type(self):
        type_label = tk.Label(self, text="Type", font=("Arial", 16), bg='#FFFFFF')
        type_label.place(x=30, y=150)

        type_options = ["ressource", "dépense"]
        self.type_select = tk.OptionMenu(self, tk.StringVar(), *type_options)
        self.type_select.config(font=("Arial", 16), bg='#FFFFFF', width=15)
        self.type_select.place(x=150, y=150)

        check_button = tk.Checkbutton(self, variable=self.type_var, bg='#FFFFFF')
        check_button.place(x=375, y=155)
        
    def create_date(self):
        date_label = tk.Label(self, text="Date :", font=("Arial", 16), bg='#FFFFFF')
        date_label.place(x=30, y=250)

        de_label = tk.Label(self, text="De", font=("Arial", 14), bg='#FFFFFF')
        de_label.place(x=120, y=250)

        self.date_minentry = tk.Entry(self, font=("Arial", 16), width=7)
        self.date_minentry.place(x=150, y=250)

        a_label = tk.Label(self, text="à", font=("Arial", 14), bg='#FFFFFF')
        a_label.place(x=230, y=250)

        self.date_maxentry = tk.Entry(self, font=("Arial", 16), width=7)
        self.date_maxentry.place(x=250, y=250)

        check_button = tk.Checkbutton(self, variable=self.date_var, bg='#FFFFFF')
        check_button.place(x=375, y=255)

    def create_eraisedbutton(self):
        eraised_button = tk.Button(self, text="Effacer", font=("Arial", 16), command=self.eraised_filter)
        eraised_button.place(x=250, y=350)

    def create_applybutton(self):
        apply_button = tk.Button(self, text="Appliquer", font=("Arial", 16), command=self.apply_filter)
        apply_button.place(x=50, y=350)

    def apply_filter(self):
        print("Filtre appliqué")
        if self.ordre_var.get() == 1:
            print("Ordre sélectionné :", self.ordre_select.cget("text"))
        if self.type_var.get() == 1:
            print("Type sélectionné :", self.type_select.cget("text"))
        if self.date_var.get() == 1:
            print("Date sélectionnée :", self.date_minentry.get(), "à", self.date_maxentry.get())

    def eraised_filter(self):
        # Cette méthode sera appelée lorsque le bouton "Effacer" est cliqué
        # Ajoutez ici le code pour effacer le filtre
        print("Filtre effacé")
