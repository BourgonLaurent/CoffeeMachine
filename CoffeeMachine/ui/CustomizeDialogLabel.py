## CustomizeDialogLabel.py - CoffeeMachine.ui: Clicking label that activates a QDialog
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
from PySide2.QtWidgets import QGroupBox, QLabel
from PySide2.QtCore import SignalInstance, Signal
from PySide2.QtCore import SignalInstance

# Project
from .coffee_customize_dialog import CoffeeCustomizeDialog


class CustomizeDialogLabel(QLabel):
    clicked = cast(SignalInstance, Signal())

    def __init__(self, parent=QGroupBox):
        super().__init__(parent)
        self.clicked.connect(self.openDialog)

        self.dialog = CoffeeCustomizeDialog()

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super().mousePressEvent(event)

    def openDialog(self):
        self.dialog.openDialog()
