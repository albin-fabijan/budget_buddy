from ..Controller import Controller
from .AddTransactionView import AddTransactionView
from .AddTransactionModel import AddTransactionModel


class AddTransactionController(Controller):
    def __init__(self, parent, header, user_id):
        super().__init__(
            parent,
            AddTransactionView(parent),
            AddTransactionModel()
        )
        self.user_id = user_id
        self.view.main()
        self.bind_view()

    def is_entry_filled(self, entry):
        return entry.get().replace(" ", "") != ""

    def are_all_entries_filled(self):
        entries = (self.view.name_entry, self.view.amount_entry)
        for entry in entries:
            if not self.is_entry_filled(entry):
                return False
        return True

    def is_amount_number(self):
        amount = self.view.amount_entry.get()
        if amount[0] == "-" or amount[0] == "+":
            amount = amount[1:]
        return amount.replace(".", "", 1).isdigit()

    def verify_all(self):
        if not self.are_all_entries_filled():
            return (
                "Champs non remplis",
                "Veuillez au moins remplir le nom "
                "et la valeur de la transaction."
            )
        elif not self.is_amount_number():
            return (
                "Valeur de transaction non valide",
                "La valeur doit être un nombre entier ou décimal avec '.'"
            )

    def click_add_button(self, event):
        message = self.verify_all()
        if message is None:
            return
        self.view.create_message_box(message[0], message[1])

    def bind_view(self):
        self.view.add_button.bind("<ButtonRelease-1>", self.click_add_button)