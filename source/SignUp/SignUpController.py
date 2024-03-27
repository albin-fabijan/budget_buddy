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

    def verify_all(self):
        first_name = self.view.first_name_entry.get()
        last_name = self.view.last_name_entry.get()
        email = self.view.email_entry.get()
        password = self.view.password_entry.get()
        if not self.are_all_entries_filled():
            return (
                "Echec de création de compte",
                "Veuillez remplir tout les champs."
            )
        elif not self.model.is_email_valid(email):
            return (
                "E-mail Invalide",
                "L'e-mail doit inclure un '@', "
                "et une extension de domaine.\n"
                "N'utilisez que des lettres ASCII, des chiffres, "
                "et ces caractères spéciaux ci-dessous:\n"
                " - _ . "
            )
        elif not self.model.is_password_valid(password):
            return (
                "Mot de passe invalide",
                "Le mot de passe doit inclure au moins "
                "Une lettre majuscule, une lettre minuscule, "
                "un chiffre, un caractère spécial et doit faire "
                "minimum 10 caractères."
            )
        else:
            self.model.create_user(
                first_name,
                last_name,
                email,
                self.model.hash_password(password)
            )
            return (
                "Succès",
                "Votre compte a été crée, vous pouvez vous connecter."
            )

    def click_signup_button(self, event):
        message = self.verify_all()
        self.view.create_message_box(message[0], message[1])
        if message[0] == "Succès":
            self.parent.launch_page("login")


    def bind_view_buttons(self):
        signup_button = self.view.signup_button
        signup_button.bind(
            "<ButtonRelease-1>",
            self.click_signup_button
        )