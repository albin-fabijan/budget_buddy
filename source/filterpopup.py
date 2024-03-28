import tkinter as tk

class filterpopup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Filtre")
        self.geometry("400x400")
        self.configure(bg='#FFFFFF')
        
        self.main()

    def main(self):
        self.create_ordre()
        self.create_type()
        self.create_date()
        self.create_eraised()
        self.create_applybutton()

    def create_ordre(self):
        ordre_label = tk.Label(self, text="Ordre", font=("Arial", 16), bg='#FFFFFF')
        ordre_label.place(x=50, y=50)

        ordre_entry = tk.Entry(self, font=("Arial", 16), bg='#FFFFFF')
        ordre_entry.place(x=200, y=50)

    def create_type(self):
        type_label = tk.Label(self, text="Type", font=("Arial", 16), bg='#FFFFFF')
        type_label.place(x=50, y=100)

        type_entry = tk.Entry(self, font=("Arial", 16), bg='#FFFFFF')
        type_entry.place(x=200, y=100)
        
    def create_date(self):
        pass
        
    def create_eraised(self):
        pass

    def create_applybutton(self):
        apply_button = tk.Button(self, text="Appliquer", font=("Arial", 16), command=self.apply_filter)
        apply_button.place(x=150, y=350)

    def apply_filter(self):
        # Cette méthode sera appelée lorsque le bouton "Appliquer" est cliqué
        # Ajoutez ici le code pour appliquer le filtre
        print("Filtre appliqué")

x = filterpopup()
x.mainloop()
