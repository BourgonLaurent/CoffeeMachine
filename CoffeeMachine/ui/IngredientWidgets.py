## IngredientWidgets.py - CoffeeMachine.ui: Custom Widgets for CoffeeMachine
# GPLv3 (c) 2020 Laurent Bourgon
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Librairies
from typing import cast
from PySide2.QtWidgets import QCheckBox, QLabel, QLineEdit
from PySide2.QtCore import SignalInstance, Signal

# Project
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
