## coffee_customize_dialog.py - CoffeeMachine.ui
# Dialog to select the coffee types

from ..coffee_creator import CoffeeCreator
from .coffee_customize_dialog_ui import Ui_coffeeSelectionDialog

from typing import List
from PySide2.QtWidgets import QDialog


class CoffeeCustomizeDialog(QDialog):
    coffees: List[CoffeeCreator]

    def __init__(self):
        super().__init__()
        self.ui = Ui_coffeeSelectionDialog()
        self.ui.setupUi(self)

    def openDialog(self):
        self.exec_()
