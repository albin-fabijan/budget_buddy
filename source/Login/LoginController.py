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

    def is_entry_filled(self, entry):
        return entry.get().split(" ")[0] != ""

    def are_all_entries_filled(self):
        entries = (
            self.view.email_entry,
            self.view.password_entry
        )

        for entry in entries:
            if not self.is_entry_filled(entry):
                return False
        return True

    def set_user_id(self):
        self.parent.user_id = self.model.get_user_id(
            self.view.email_entry.get(),
            self.view.password_entry.get()
        )

    def verify_all(self):
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()

        if not self.are_all_entries_filled():
            return (
                "Echec de connexion",
                "Veuillez remplir tout les champs."
            )
        elif not self.model.is_email_in_database(email):
            return (
                "Compte n'existe pas",
                "Il n'y a pas de compte qui utilise cette adresse mail."
            )
        elif not self.model.is_password_correct(email, password):
            return (
                "Mot de passe incorrect",
                "Le mot de passe que vous avez mis n'est pas correct."
            )

    def click_connection_button(self, event):
        message = self.verify_all()
        if message:
            self.view.create_message_box(message[0], message[1])
            return
        self.parent.user_id = self.model.get_user_id(
            self.view.email_entry.get(),
            self.view.password_entry.get()
        )
        self.parent.launch_page("header")

    def click_sign_up_button(self, event):
        self.parent.launch_page("signup")

    def bind_view(self):
        connection_button = self.view.connection_button
        connection_button.bind("<ButtonRelease-1>", self.click_connection_button)
        
        clickable_text = self.view.clickable_text
        clickable_text.bind("<ButtonRelease-1>", self.click_sign_up_button)