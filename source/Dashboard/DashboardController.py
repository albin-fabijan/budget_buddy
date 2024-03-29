from ..Controller import Controller
from .DashboardView import DashboardView
from .DashboardModel import DashboardModel

class DashboardController(Controller):
    def __init__(self, parent, user_id):
        super().__init__(
            parent,
            DashboardView(parent),
            DashboardModel()
        )
        self.user_id = user_id
        self.view.main()
        self.set_account_name()

    def set_account_name(self):
        first_name = self.model.get_user_first_name(self.user_id)
        last_name = self.model.get_user_last_name(self.user_id)
        self.view.account_name.config(
            text=f"Compte de {first_name} {last_name}"
        )