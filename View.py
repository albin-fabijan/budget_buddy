import tkinter as tk


class View(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack(side=tk.TOP)

        self.button = tk.Button(
            self.root,
            height=1,
            width=8
        )
        self.button.pack()