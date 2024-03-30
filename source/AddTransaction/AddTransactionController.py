import datetime

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
        self.header = header
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

    def set_category_on_keystroke(self, event):
        transaction_type = {
            "+": 0,
            "-": 1
        }

        amount_entry = self.view.amount_entry.get()
        if len(amount_entry) == 0:
            return

        character = amount_entry[0]
        if character not in transaction_type:
            return

        self.view.selected_option.set(
            self.view.options[transaction_type[character]]
        )

    def get_amount(self):
        amount = self.view.amount_entry.get()
        if amount[0] == "-" or amount[0] == "+":
            amount = amount[1:]
        
        amount = float(amount)
        if self.view.selected_option.get() == "Dépense":
            amount = amount * -1
            
        return amount

    def add_transaction(self):
        t_name = self.view.name_entry.get()
        t_description = self.view.description_entry.get("1.0", "end")[:-1]
        t_amount = self.get_amount()
        date_format = "%Y-%m-%d %H:%M:%S"
        t_date = datetime.datetime.now().strftime(date_format)
        u_id = self.user_id

        self.model.add_transaction(
            t_name,
            t_description,
            t_amount,
            t_date,
            u_id
        )

    def click_add_button(self, event):
        message = self.verify_all()

        if message is not None:
            self.view.create_message_box(message[0], message[1])
            return

        self.add_transaction()
        self.view.destroy()
        self.header.launch_current_page()


    def bind_view(self):
        self.view.amount_entry.bind("<Key>", self.set_category_on_keystroke)
        self.view.add_button.bind("<ButtonRelease-1>", self.click_add_button)