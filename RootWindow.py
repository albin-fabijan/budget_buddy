import tkinter as tk

from View import View
from Controller import Controller
from Model import Model

class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Root")

        self.main_frame = tk.Frame(
            self,
            width=800,
            height=600
        )
        self.main_frame.place(
            anchor=tk.CENTER,
            relx=0.5,
            rely=0.5,
        )

        self.view = View(self.main_frame)
        self.model = Model()
        self.controller = Controller(self.view, self.model)
        self.controller.set_button_text() 
        self.controller.bind_button()

        self.mainloop()
