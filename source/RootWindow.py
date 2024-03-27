import tkinter as tk

from .DisplayLoginPage import DisplayLoginPage

class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.width = 1440
        self.height = 1024
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.title("Root")

        self.login_page = DisplayLoginPage(self)

        self.mainloop()
