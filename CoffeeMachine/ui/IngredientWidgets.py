## IngredientWidgets.py - CoffeeMachine.ui
# Custom Widgets for CoffeeMachine
from PySide2.QtCore import SignalInstance
from ..coffee_lang import STATUS_EXCEEDING
from PySide2.QtWidgets import QCheckBox, QLabel, QLineEdit


class IngredientSelector(QLineEdit):
    textEdited: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)

    def setSafeText(self, value: int):
        # word = self.objectName().replace("Selector", "")
        status: QLabel = self.parent().findChild(QLabel, f"{self.objectName().replace('Selector', '')}StatusLabel")  # type: ignore
        if len(str(value)) > len(str(self.inputMask())):
            status.setText(STATUS_EXCEEDING)

        self.setText(str(value))


class IngredientInfinity(QCheckBox):
    clicked: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)
