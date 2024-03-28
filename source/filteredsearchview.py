import tkinter as tk
from source.Header  import Header
from tkinter import ttk

class filteredsearchview(tk.Frame):
    def __init__(self):
        pass
    def test1(self):
        pass
    def test2(self):
        pass
    def test3(self):
        pass
    def main(self,window, first_name, last_name):
        x = Header()
        x.run(window, first_name, last_name , self.test1, self.test2, self.test3)
        self.creat_frame(window)
        self.creat_treeview(window , position = "1" , info = ( "2024-03-27", "John Doe", "100"))
        self.creat_filterbutton(window)
        self.creat_addbutton(window)

    def creat_frame(self, window):
        frame = tk.Frame(window, bg="#72D5FF")
        frame.place(relx=0.2, rely=0.25 , width=730, height=500)

    def creat_treeview(self, window , position, info):
        tree = ttk.Treeview(window)
        tree["columns"] = ("1", "2", "3")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("1", anchor=tk.W, width=100)
        tree.column("2", anchor=tk.W, width=100)
        tree.column("3", anchor=tk.W, width=100)

        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("1", text="Date", anchor=tk.W)
        tree.heading("2", text="nom", anchor=tk.W)
        tree.heading("3", text="Montant", anchor=tk.W)

        tree.column("1", width=10)
        tree.column("2", width=20)
        tree.column("3", width=300)
        tree.place(relx=0.2, rely=0.25, width=730, height=500)
    

        tree.insert('', 'end', text= position, values= info)

    def creat_filterbutton(self, window):
        filter_button = tk.Button(window, text="Filtrer", font=("Arial", 16,), width=10, height=1 , command=self.on_filter)
        filter_button.place(x=260, y=120)
    
    def on_filter(self):
        pass

    def creat_addbutton(self, window):
        add_button = tk.Button(window, text="+", font=("Arial", 16,), width=2, height=1 , command=self.on_addbutton)
        add_button.place(x=860, y=120)
    
    def on_addbutton(self):
        pass




