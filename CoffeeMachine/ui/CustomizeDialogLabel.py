## CustomizeDialogLabel.py - CoffeeMachine.ui
# Clicking label that activates a QDialog

from CoffeeMachine.coffee_creator import CoffeeCreator
from PySide2.QtWidgets import QDialog, QGroupBox, QLabel
from PySide2.QtCore import SignalInstance, Signal

from .coffee_customize_dialog import CoffeeCustomizeDialog


class CustomizeDialogLabel(QLabel):
    clicked: SignalInstance = Signal()  # type: ignore

    def __init__(self, parent=QGroupBox):
        super().__init__(parent)
        self.clicked.connect(self.openDialog)

        self.dialog = CoffeeCustomizeDialog()

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super().mousePressEvent(event)

    def openDialog(self):
        self.dialog.exec_()
