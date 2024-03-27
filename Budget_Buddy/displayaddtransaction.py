import tkinter as tk

class Displayaddtransaction(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Add transaction")
        self.geometry("428x926")
        self.configure(bg='#72D5FF')
        self.main()

    def main(self):
        self.create_frame()
        self.creat_name()   
        self.creat_amount()
        self.creat_type()
        self.creat_description()
        self.create_addbutton()

    def create_frame(self):

        self.frame_width = 428
        self.frame_height = 926
        self.frame = tk.Frame(self, width=self.frame_width, height=self.frame_height)
        self.frame.config(background='#72D5FF')
        self.frame.pack()

    def creat_name(self):

        self.name_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Nom de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.name_entry.pack(side=tk.TOP, pady=10)

    def creat_amount(self):

        self.amount_entry = tk.Entry(self.frame, font=("Arial", 26))
        additional_text = tk.Label(self.frame, text="Montant de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.amount_entry.pack(side=tk.TOP, pady=10)
    
    def creat_type(self):
        
        additional_text = tk.Label(self.frame, text="Type de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=50)

        options = ["Revenu", "Dépenses"]
        self.selected_option = tk.StringVar(self.frame)
        self.selected_option.set(options[0])
        dropdown = tk.OptionMenu(self.frame, self.selected_option, *options)
        dropdown.config(font=("Arial", 20), width=20)
        dropdown.pack(side=tk.TOP, pady=10)

    def creat_description(self):

        additional_text = tk.Label(self.frame, text="Description de la transaction:", font=("Arial", 26), bg='#72D5FF')
        additional_text.pack(side=tk.TOP, pady=10)
        self.description_entry = tk.Text(self.frame, font=("Arial", 26), height=5, width=20)
        self.description_entry.pack(side=tk.TOP, pady=10)

    def create_addbutton(self):

        add_button = tk.Button(self.frame, text="Ajouter", font=("Arial", 26), bg='white', width=10, height=2, command=self.on_add)
        add_button.pack(side=tk.TOP, pady=40)
    
    def on_add(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()
        transaction_type = self.selected_option.get()
        description = self.description_entry.get("1.0", "end-1c")
        print("Name:", name)
        print("Amount:", amount)
        print("Transaction type:", transaction_type)
        print("Description:", description)
    

    


    

    
if __name__ == "__main__":
    fenetre = Displayaddtransaction()
    fenetre.mainloop()
