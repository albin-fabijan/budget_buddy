import tkinter as tk


class FirstView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        self.button = tk.Button(
            self,
            height=1,
            width=8
        )
        self.button.pack()