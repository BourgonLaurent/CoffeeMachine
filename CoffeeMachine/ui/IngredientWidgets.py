## IngredientWidgets.py - CoffeeMachine.ui
# Custom Widgets for CoffeeMachine

from typing import cast
from PySide2.QtWidgets import QCheckBox, QLabel, QLineEdit
from PySide2.QtCore import SignalInstance, Signal

from ..coffee_lang import STATUS_EXCEEDING


class IngredientSelector(QLineEdit):
    textEdited: SignalInstance

    def __init__(self, parent):
        super().__init__(parent)

    def setSafeText(self, value: int):
        if len(str(value)) > len(str(self.inputMask())):
            cast(
                QLabel,
                self.parent().findChild(
                    QLabel, f"{self.objectName().replace('Selector', '')}StatusLabel"
                ),
            ).setText(STATUS_EXCEEDING)

        self.setText(str(value))


class IngredientInfinity(QCheckBox):
    clicked = cast(SignalInstance, Signal())

    def __init__(self, parent):
        super().__init__(parent)
