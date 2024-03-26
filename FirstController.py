from FirstModel import FirstModel
from FirstView import FirstView

class FirstController:
    def __init__(self, parent):
        self.model = FirstModel()
        self.view = FirstView(parent)
        self.controls_initialization()

    def set_button_text(self):
        button = self.view.button
        button.config(text=self.model.get_thing())

    def button_add_thing(self, event):
        self.model.add_thing()
        self.set_button_text()

    def bind_button(self):
        button = self.view.button
        button.bind("<Button-1>", self.button_add_thing)

    def controls_initialization(self):
        self.set_button_text()
        self.bind_button()