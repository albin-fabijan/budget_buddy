from ..Controller import Controller
from .HeaderView import HeaderView
from .HeaderModel import HeaderModel
from ..Dashboard.DashboardController import DashboardController
from ..Notifications.NotificationsController import NotificationsController
from ..AddTransaction.AddTransactionController import AddTransactionController
from ..TransactionList.TransactionListController import TransactionListController


class HeaderController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            HeaderView(parent),
            HeaderModel()
        )

        self.view.main()
        self.set_user_name()
        self.bind_view()

        self.current_page = DashboardController
        self.launch_current_page()

    def set_user_name(self):
        first_name = self.model.get_user_first_name(self.parent.user_id)
        last_name = self.model.get_user_last_name(self.parent.user_id)
        self.view.name.config(
            text=f"{first_name} {last_name}"
        )

    def click_logout_button(self, event):
        self.parent.launch_page("login")

    def click_add_transaction(self, event):
        AddTransactionController(
            self.parent,
            self,
            self.parent.user_id
        )

    def launch_current_page(self):
        for child in self.view.content_frame.winfo_children():
            child.destroy()
        self.current_page(
            self.view.content_frame,
            self,
            self.parent.user_id
        )

    def launch_dashboard(self, event):
        self.current_page = DashboardController
        self.launch_current_page()

    def launch_transaction_list(self, event):
        self.current_page = TransactionListController
        self.launch_current_page()

    def click_notification_button(self, event):
        self.current_page = NotificationsController
        self.launch_current_page()

    def bind_view(self):
        self.view.logout_button.bind(
            "<ButtonRelease-1>",
            self.click_logout_button
        )

        self.view.button1.bind(
            "<ButtonRelease-1>",
            self.click_add_transaction
        )
        self.view.button2.bind(
            "<ButtonRelease-1>",
            self.launch_dashboard
        )

        self.view.button3.bind(
            "<ButtonRelease-1>",
            self.launch_transaction_list
        )