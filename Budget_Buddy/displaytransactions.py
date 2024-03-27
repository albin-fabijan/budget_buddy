import tkinter as tk

class DisplayTransactions(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Transactions")
        self.geometry("1440x1024")
        self.configure(bg='#72D5FF')
        self.main()

    def main(self):
        self.create_frame()

    def create_frame(self):
        
        