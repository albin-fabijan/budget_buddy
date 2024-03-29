from ..Controller import Controller
from .HeaderView import HeaderView
from .HeaderModel import HeaderModel
from ..Dashboard.DashboardController import DashboardController
from ..NotificationPage import NotificationPage


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

    def click_placeholder(self, event):
        print(event)

    def click_logout_button(self, event):
        self.parent.launch_page("login")

    def launch_current_page(self):
        for child in self.view.content_frame.winfo_children():
            child.destroy()
        self.current_page(
            self.view.content_frame,
            self,
            self.parent.user_id
        )

    def click_button_two(self, event):
        self.current_page = DashboardController
        self.launch_current_page()

    def click_notification_button(self, event):
        self.current_page = NotificationPage
        self.launch_current_page()

    def bind_view(self):
        self.view.logout_button.bind(
            "<ButtonRelease-1>",
            self.click_logout_button
        )

        self.view.button1.bind(
            "<ButtonRelease-1>",
            self.click_placeholder
        )
        self.view.button2.bind(
            "<ButtonRelease-1>",
            self.click_button_two
        )

        self.view.button3.bind(
            "<ButtonRelease-1>",
            self.click_placeholder
        )