from ..Controller import Controller
from .DashboardView import DashboardView
from .DashboardModel import DashboardModel

class DashboardController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            DashboardView(parent),
            DashboardModel()
        )
        self.view.main()