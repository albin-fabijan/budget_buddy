import tkinter as tk

class Displayaddtransaction(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add transaction")
        self.geometry("428x926")
        self.configure(bg='#72D5FF')

    def main(self):
        self.creat_name()   
        self.creat_amount()
        


    def creat_name(self):
        self.name_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Nom de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.name_entry.pack(side=tk.TOP, pady=5)

    def creat_amount(self):
        self.amount_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Montant de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.amount_entry.pack(side=tk.TOP, pady=5)
    
    def creat_type(self):
        additional_text = tk.Label(self.frame, text="Type de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)

    

    
if __name__ == "__main__":
    fenetre = Displayaddtransaction()
    fenetre.mainloop()
