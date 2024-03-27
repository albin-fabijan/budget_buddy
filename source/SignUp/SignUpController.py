from ..Controller import Controller
from .SignUpView import SignUpView
from .SignUpModel import SignUpModel


class SignUpController(Controller):
    def __init__(self, parent):
        super().__init__(
            parent,
            SignUpView(parent),
            "abab"
        )
        self.view.main()