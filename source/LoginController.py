from functools import partial

from .Controller import Controller
from .LoginView import LoginView

class LoginController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            LoginView(parent),
            "OHGODNO",
        )
        self.view.main()
        self.bind_connection_button()

    def get_email(self):
        print(self.view.email_entry.get())

    def get_password(self):
        print(self.view.password_entry.get())

    def click_connection_button(self, event):
        print("hello!")

    def bind_connection_button(self):
        connection_button = self.view.connection_button
        print(connection_button.bind())
        connection_button.bind("<Button-1>", self.click_connection_button)
        print(connection_button.bind())