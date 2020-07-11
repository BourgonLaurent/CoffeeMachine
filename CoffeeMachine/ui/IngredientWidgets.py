## IngredientWidgets.py - CoffeeMachine.ui
# Custom Widgets for CoffeeMachine
from PySide2.QtCore import SignalInstance
from ..coffee_lang import STATUS_EXCEEDING
from PySide2.QtWidgets import QCheckBox, QLabel, QLineEdit


class IngredientSelector(QLineEdit):
    textEdited: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)
        self.word: str = self.objectName().replace("Selector", "")
        self.status: QLabel = self.parent().findChild(QLabel, f"{self.word}StatusLabel")  # type: ignore

    def setSafeText(self, value: int):
        if len(str(value)) > len(str(self.inputMask())):
            self.status.setText(STATUS_EXCEEDING)
        self.setText(str(value))


class IngredientInfinity(QCheckBox):
    clicked: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)
