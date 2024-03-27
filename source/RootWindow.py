import tkinter as tk

from .LoginController import LoginController
from .SignUpView import SignUpView

class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.width = 1440
        self.height = 1024
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.title("Root")

        self.pages = {
            "login": LoginController,
            "signup": SignUpView
        }

        self.launch_page("login")

        self.mainloop()

    def launch_page(self, page_name):
        for child in self.winfo_children():
            child.destroy()
        self.current_page = self.pages[page_name](self)