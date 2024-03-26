import tkinter as tk
import tkinter.ttk as ttk


class HeaderView(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        self.first_tab = ttk.Frame(self)
        self.second_tab = ttk.Frame(self)

        self.header_initialisation()

    def header_initialisation(self):
        self.pack(anchor=tk.NW)

        self.add(self.first_tab, text="First")
        self.add(self.second_tab, text="Second")