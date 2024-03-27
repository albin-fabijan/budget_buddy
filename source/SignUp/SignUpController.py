from ..Controller import Controller
from .SignUpView import SignUpView
from .SignUpModel import SignUpModel


class SignUpController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            SignUpView(parent),
            SignUpModel()
        )
        self.view.main()
        self.bind_view_buttons()

    def is_entry_filled(self, entry):
        return entry.get().split(" ")[0] != ""

    def are_all_entries_filled(self):
        entries = (
            self.view.first_name_entry,
            self.view.last_name_entry,
            self.view.email_entry,
            self.view.password_entry
        )
        for entry in entries:
            if not self.is_entry_filled(entry):
                return False
        return True

    def click_signup_button(self, event):
        filled = self.are_all_entries_filled()
        print(f"Tout rempli: {filled}")

        email = self.view.email_entry.get() 
        valid = self.model.is_email_valid(email)
        print(f"Email valide: {valid}")

    def bind_view_buttons(self):
        signup_button = self.view.signup_button
        signup_button.bind(
            "<ButtonRelease-1>",
            self.click_signup_button
        )