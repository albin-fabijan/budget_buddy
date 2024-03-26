from functools import partial

from HeaderView import HeaderView
from FirstController import FirstController

class HeaderController:
    def __init__(self, parent):
        self.parent = parent
        self.view = HeaderView(parent)
        self.controls_initialization()

        self.pages = {
            0: partial(FirstController, self.parent)
        }

    def load_page(self, event):
        for child in self.view.master.winfo_children():
            if child != self.view:
                child.destroy()

        current_tab = self.view.index("current")

        if current_tab in self.pages:
            self.pages[current_tab]()

    def controls_initialization(self):
        self.view.bind("<<NotebookTabChanged>>", self.load_page)