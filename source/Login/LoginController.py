from ..Controller import Controller
from .LoginView import LoginView
from .LoginModel import LoginModel

class LoginController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            LoginView(parent),
            LoginModel(),
        )
        self.view.main()
        self.bind_view()

    def get_email(self):
        return self.view.email_entry.get()

    def get_password(self):
        return self.view.password_entry.get()

    def get_users(self):
        print(self.model.read_all_users())

    def click_connection_button(self, event):
        self.get_users()

    def click_sign_up_button(self, event):
        self.parent.launch_page("signup")

    def bind_view(self):
        connection_button = self.view.connection_button
        connection_button.bind("<ButtonRelease-1>", self.click_connection_button)
        
        clickable_text = self.view.clickable_text
        clickable_text.bind("<ButtonRelease-1>", self.click_sign_up_button)