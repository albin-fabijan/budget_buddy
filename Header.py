import tkinter as tk


class Header(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack(side=tk.TOP)

        self.button_1_frame = tk.Frame(self)
        self.button_1_frame.pack()

        self.button_1_text = tk.Label(
            self.button_1_frame,
            text="Button1"
        )
        self.button_1_text.pack()