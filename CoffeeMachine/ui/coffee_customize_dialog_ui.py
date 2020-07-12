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

from PySide2.QtSvg import QSvgWidget


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
        QListWidgetItem(self.coffeeListWidget)
        self.coffeeListWidget.setObjectName(u"coffeeListWidget")
        self.coffeeListWidget.setGeometry(QRect(20, 20, 181, 221))
        self.coffeeListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.coffeeListWidget.setSpacing(4)
        self.coffeeListWidget.setItemAlignment(Qt.AlignCenter)
        self.coffeeListWidget.setSortingEnabled(True)
        self.formLayoutWidget = QWidget(coffeeSelectionDialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(220, 20, 171, 222))
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

        self.waterSvg = QSvgWidget(self.formLayoutWidget)
        self.waterSvg.setObjectName(u"waterSvg")
        self.waterSvg.setMinimumSize(QSize(50, 50))
        self.waterSvg.setMaximumSize(QSize(50, 50))

        self.coffeeLayout.setWidget(0, QFormLayout.LabelRole, self.waterSvg)

        self.milkSvg = QSvgWidget(self.formLayoutWidget)
        self.milkSvg.setObjectName(u"milkSvg")
        self.milkSvg.setMinimumSize(QSize(65, 40))
        self.milkSvg.setMaximumSize(QSize(65, 40))

        self.coffeeLayout.setWidget(1, QFormLayout.LabelRole, self.milkSvg)

        self.beansSvg = QSvgWidget(self.formLayoutWidget)
        self.beansSvg.setObjectName(u"beansSvg")
        self.beansSvg.setMinimumSize(QSize(50, 50))
        self.beansSvg.setMaximumSize(QSize(50, 50))

        self.coffeeLayout.setWidget(2, QFormLayout.LabelRole, self.beansSvg)

        self.priceSvg = QSvgWidget(self.formLayoutWidget)
        self.priceSvg.setObjectName(u"priceSvg")
        self.priceSvg.setMinimumSize(QSize(50, 50))
        self.priceSvg.setMaximumSize(QSize(50, 50))

        self.coffeeLayout.setWidget(3, QFormLayout.LabelRole, self.priceSvg)


        self.retranslateUi(coffeeSelectionDialog)

        self.coffeeListWidget.setCurrentRow(0)


        QMetaObject.connectSlotsByName(coffeeSelectionDialog)
    # setupUi

    def retranslateUi(self, coffeeSelectionDialog):
        coffeeSelectionDialog.setWindowTitle(QCoreApplication.translate("coffeeSelectionDialog", u"Select a coffee", None))

        __sortingEnabled = self.coffeeListWidget.isSortingEnabled()
        self.coffeeListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.coffeeListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("coffeeSelectionDialog", u"Cappucino", None));
        self.coffeeListWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

