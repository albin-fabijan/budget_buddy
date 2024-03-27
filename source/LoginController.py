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
        return self.view.email_entry.get()

    def get_password(self):
        return self.view.password_entry.get()

    def click_connection_button(self, event):
        self.get_email()
        self.get_password()

    def bind_connection_button(self):
        connection_button = self.view.connection_button
        connection_button.bind("<Button-1>", self.click_connection_button)