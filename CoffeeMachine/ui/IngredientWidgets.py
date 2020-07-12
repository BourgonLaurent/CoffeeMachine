## IngredientWidgets.py - CoffeeMachine.ui
# Custom Widgets for CoffeeMachine

from ..coffee_lang import STATUS_EXCEEDING
from PySide2.QtWidgets import QCheckBox, QLabel, QLineEdit
from PySide2.QtCore import SignalInstance


class IngredientSelector(QLineEdit):
    textEdited: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)

    def setSafeText(self, value: int):
        if len(str(value)) > len(str(self.inputMask())):
            self.parent().findChild(
                QLabel, f"{self.objectName().replace('Selector', '')}StatusLabel"
            ).setText(  # type: ignore
                STATUS_EXCEEDING
            )

        self.setText(str(value))


class IngredientInfinity(QCheckBox):
    clicked: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)
