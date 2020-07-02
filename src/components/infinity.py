from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap


class InfinityButton(QLabel):
    clicked = Signal()
    infinity = True

    def __init__(self, parent=None):
        super().__init__(parent)

        self.on = QPixmap(u":/icons/assets/infinity_on.svg")
        self.off = QPixmap(u":/icons/assets/infinity_off.svg")

        self.setPixmap(self.on)

        self.clicked.connect(self.setInfinity)

    def mousePressEvent(self, event):
        self.clicked.emit()
        return super().mousePressEvent(event)

    def setInfinity(self, state=None):
        if self.infinity or state:
            self.setPixmap(self.off)
            self.infinity = False
        else:
            self.setPixmap(self.on)
            self.infinity = True
