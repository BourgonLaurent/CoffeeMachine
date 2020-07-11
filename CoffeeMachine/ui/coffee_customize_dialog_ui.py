# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coffee_customize_dialog_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_coffeeSelectionDialog(object):
    def setupUi(self, coffeeSelectionDialog):
        if not coffeeSelectionDialog.objectName():
            coffeeSelectionDialog.setObjectName(u"coffeeSelectionDialog")
        coffeeSelectionDialog.resize(412, 266)
        coffeeSelectionDialog.setMinimumSize(QSize(412, 266))
        coffeeSelectionDialog.setMaximumSize(QSize(412, 266))
        coffeeSelectionDialog.setStyleSheet(u"QDialog {\n"
"  background-color: #C7CBD0;\n"
"}\n"
"\n"
"QListWidget {\n"
"  background: rgba(190, 168, 135, 0.58);\n"
"  border: 2px solid #6F7987;\n"
"  border-radius: 12px;\n"
"  font-family: Segoe UI;\n"
"  font-weight: 900;\n"
"  font-size: 23px;\n"
"  color: #4D5984;\n"
"  padding: 10px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"  text-align: center;\n"
"  padding: 5px\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"  background-color: #4D5984;\n"
"  color: rgb(190, 168, 135);\n"
"  border-radius: 14px;\n"
"}\n"
"\n"
"QLabel {\n"
"  font-family: Segoe UI;\n"
"  font-weight: 600;\n"
"  font-size: 14px;\n"
"  color: #6F7987;\n"
"}")
        self.coffeeListWidget = QListWidget(coffeeSelectionDialog)
        self.coffeeListWidget.setObjectName(u"coffeeListWidget")
        self.coffeeListWidget.setGeometry(QRect(20, 20, 141, 221))
        self.coffeeListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.coffeeListWidget.setSpacing(4)
        self.coffeeListWidget.setItemAlignment(Qt.AlignCenter)
        self.coffeeListWidget.setSortingEnabled(True)
        self.formLayoutWidget = QWidget(coffeeSelectionDialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(180, 20, 211, 222))
        self.coffeeLayout = QFormLayout(self.formLayoutWidget)
        self.coffeeLayout.setObjectName(u"coffeeLayout")
        self.coffeeLayout.setLabelAlignment(Qt.AlignCenter)
        self.coffeeLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.coffeeLayout.setHorizontalSpacing(15)
        self.coffeeLayout.setContentsMargins(0, 0, 0, 0)
        self.waterLabel = QLabel(self.formLayoutWidget)
        self.waterLabel.setObjectName(u"waterLabel")

        self.coffeeLayout.setWidget(0, QFormLayout.FieldRole, self.waterLabel)

        self.milkLabel = QLabel(self.formLayoutWidget)
        self.milkLabel.setObjectName(u"milkLabel")

        self.coffeeLayout.setWidget(1, QFormLayout.FieldRole, self.milkLabel)

        self.beansLabel = QLabel(self.formLayoutWidget)
        self.beansLabel.setObjectName(u"beansLabel")

        self.coffeeLayout.setWidget(2, QFormLayout.FieldRole, self.beansLabel)

        self.priceLabel = QLabel(self.formLayoutWidget)
        self.priceLabel.setObjectName(u"priceLabel")

        self.coffeeLayout.setWidget(3, QFormLayout.FieldRole, self.priceLabel)

        self.waterSvg = QWidget(self.formLayoutWidget)
        self.waterSvg.setObjectName(u"waterSvg")
        self.waterSvg.setMinimumSize(QSize(50, 50))
        self.waterSvg.setMaximumSize(QSize(50, 50))

        self.coffeeLayout.setWidget(0, QFormLayout.LabelRole, self.waterSvg)

        self.widget = QWidget(self.formLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(65, 40))
        self.widget.setMaximumSize(QSize(65, 40))

        self.coffeeLayout.setWidget(1, QFormLayout.LabelRole, self.widget)

        self.widget_2 = QWidget(self.formLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(50, 50))
        self.widget_2.setMaximumSize(QSize(50, 50))

        self.coffeeLayout.setWidget(2, QFormLayout.LabelRole, self.widget_2)

        self.widget_3 = QWidget(self.formLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(50, 50))
        self.widget_3.setMaximumSize(QSize(50, 50))

        self.coffeeLayout.setWidget(3, QFormLayout.LabelRole, self.widget_3)


        self.retranslateUi(coffeeSelectionDialog)

        self.coffeeListWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(coffeeSelectionDialog)
    # setupUi

    def retranslateUi(self, coffeeSelectionDialog):
        coffeeSelectionDialog.setWindowTitle(QCoreApplication.translate("coffeeSelectionDialog", u"Dialog", None))
        self.waterLabel.setText(QCoreApplication.translate("coffeeSelectionDialog", u"200 mL of water", None))
        self.milkLabel.setText(QCoreApplication.translate("coffeeSelectionDialog", u"20 mL of milk", None))
        self.beansLabel.setText(QCoreApplication.translate("coffeeSelectionDialog", u"5 g of beans", None))
        self.priceLabel.setText(QCoreApplication.translate("coffeeSelectionDialog", u"6 $", None))
    # retranslateUi

