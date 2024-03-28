from ..Controller import Controller
from .HeaderView import HeaderView


class HeaderController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            HeaderView(parent),
            "PLACEHOLDER !!!"
        )
        self.view.main()