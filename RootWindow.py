import tkinter as tk

from FirstController import FirstController
from HeaderController import HeaderController

class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.resizable(False, False)
        self.title("Root")

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.header_controller = HeaderController(self.main_frame)

        self.mainloop()
