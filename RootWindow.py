import tkinter as tk

from Header import Header

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
            relx=0.5,
            rely=0.5,
        )

        self.header = Header(self.main_frame)

        self.mainloop()
