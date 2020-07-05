# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coffee_interface_ui.ui'
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

from  . import coffee_interface_resources_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(795, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(795, 570))
        mainWindow.setMaximumSize(QSize(795, 570))
        icon = QIcon()
        icon.addFile(u":/icons/assets/logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"QMainWindow {\n"
"  background-color: #C7CBD0;\n"
"}\n"
"\n"
"QGroupBox {\n"
"  border: 7px solid #4D5984;\n"
"  border-radius: 14px;\n"
"}\n"
"\n"
"QLabel#coffeeSelectionLabel,\n"
"QLabel#waterSelectionLabel,\n"
"QLabel#milkSelectionLabe,\n"
"QLabel#beansSelectionLabel,\n"
"QLabel#priceSelectionLabel {\n"
"  font-family: Segoe UI;\n"
"  font-style: normal;\n"
"  font-weight: bold;\n"
"  font-size: 15px;\n"
"  color: #BEA887;\n"
"}\n"
"\n"
"QLineEdit#coffeeSelector,\n"
"QLineEdit#waterSelector,\n"
"QLineEdit#milkSelector,\n"
"QLineEdit#beansSelector,\n"
"QLineEdit#priceSelector {\n"
"  background: rgba(190, 168, 135, 0.58);\n"
"  border: 2px solid #6F7987;\n"
"  border-radius: 12px;\n"
"  font-family: Segoe UI;\n"
"  font-weight: 900;\n"
"  font-size: 23px;\n"
"  color: #4D5984;\n"
"  padding-left: 5px;\n"
"}\n"
"\n"
"QLabel#coffeeSelectorSuffix,\n"
"QLabel#waterSelectorSuffix,\n"
"QLabel#milkSelectorSuffix,\n"
"QLabel#beansSelectorSuffix,\n"
"QLabel#priceSelectorSuffix {\n"
"  font-family: Segoe UI;\n"
"  fon"
                        "t-size: 14px;\n"
"  color: #6F7987;\n"
"}\n"
"\n"
"QPushButton#adminPushButton {\n"
"  background: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/assets/infinity_on.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/icons/assets/infinity_off.svg);\n"
"}\n"
"\n"
"QPushButton#adminPanelLabel:pressed {\n"
"  background-color: #c2b7a6;\n"
"  border-radius: 14px;\n"
"}")
        self.mainWidget = QWidget(mainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy1)
        self.coffeeGroupBox = QGroupBox(self.mainWidget)
        self.coffeeGroupBox.setObjectName(u"coffeeGroupBox")
        self.coffeeGroupBox.setGeometry(QRect(17, 23, 203, 250))
        self.coffeeSelectionLabel = QLabel(self.coffeeGroupBox)
        self.coffeeSelectionLabel.setObjectName(u"coffeeSelectionLabel")
        self.coffeeSelectionLabel.setGeometry(QRect(67, 85, 61, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.coffeeSelectionLabel.setFont(font)
        self.coffeeSelectionLabel.setAlignment(Qt.AlignCenter)
        self.coffeeSelector = QLineEdit(self.coffeeGroupBox)
        self.coffeeSelector.setObjectName(u"coffeeSelector")
        self.coffeeSelector.setGeometry(QRect(36, 157, 131, 38))
        self.coffeeSelectorSuffix = QLabel(self.coffeeGroupBox)
        self.coffeeSelectorSuffix.setObjectName(u"coffeeSelectorSuffix")
        self.coffeeSelectorSuffix.setGeometry(QRect(79, 168, 81, 16))
        self.coffeeInfinityCheckBox = QCheckBox(self.coffeeGroupBox)
        self.coffeeInfinityCheckBox.setObjectName(u"coffeeInfinityCheckBox")
        self.coffeeInfinityCheckBox.setGeometry(QRect(82, 210, 41, 21))
        self.coffeeInfinityCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.coffeeInfinityCheckBox.setStyleSheet(u"")
        self.coffeeSelectionSvg = QSvgWidget(self.coffeeGroupBox)
        self.coffeeSelectionSvg.setObjectName(u"coffeeSelectionSvg")
        self.coffeeSelectionSvg.setGeometry(QRect(47, 26, 100, 114))
        self.coffeeSelector.raise_()
        self.coffeeSelectorSuffix.raise_()
        self.coffeeInfinityCheckBox.raise_()
        self.coffeeSelectionSvg.raise_()
        self.coffeeSelectionLabel.raise_()
        self.ingredientsGroupBox = QGroupBox(self.mainWidget)
        self.ingredientsGroupBox.setObjectName(u"ingredientsGroupBox")
        self.ingredientsGroupBox.setGeometry(QRect(238, 23, 541, 250))
        self.waterSelector = QLineEdit(self.ingredientsGroupBox)
        self.waterSelector.setObjectName(u"waterSelector")
        self.waterSelector.setGeometry(QRect(19, 157, 161, 38))
        self.waterSelectorSuffix = QLabel(self.ingredientsGroupBox)
        self.waterSelectorSuffix.setObjectName(u"waterSelectorSuffix")
        self.waterSelectorSuffix.setGeometry(QRect(101, 168, 80, 16))
        self.milkSelector = QLineEdit(self.ingredientsGroupBox)
        self.milkSelector.setObjectName(u"milkSelector")
        self.milkSelector.setGeometry(QRect(191, 157, 161, 38))
        self.milkSelectorSuffix = QLabel(self.ingredientsGroupBox)
        self.milkSelectorSuffix.setObjectName(u"milkSelectorSuffix")
        self.milkSelectorSuffix.setGeometry(QRect(274, 168, 80, 16))
        self.beansSelectorSuffix = QLabel(self.ingredientsGroupBox)
        self.beansSelectorSuffix.setObjectName(u"beansSelectorSuffix")
        self.beansSelectorSuffix.setGeometry(QRect(446, 166, 80, 21))
        self.beansSelector = QLineEdit(self.ingredientsGroupBox)
        self.beansSelector.setObjectName(u"beansSelector")
        self.beansSelector.setGeometry(QRect(363, 157, 161, 38))
        self.waterInfinityCheckBox = QCheckBox(self.ingredientsGroupBox)
        self.waterInfinityCheckBox.setObjectName(u"waterInfinityCheckBox")
        self.waterInfinityCheckBox.setGeometry(QRect(81, 210, 41, 21))
        self.waterInfinityCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.waterInfinityCheckBox.setStyleSheet(u"")
        self.waterInfinityCheckBox.setChecked(True)
        self.milkInfinityCheckBox = QCheckBox(self.ingredientsGroupBox)
        self.milkInfinityCheckBox.setObjectName(u"milkInfinityCheckBox")
        self.milkInfinityCheckBox.setGeometry(QRect(249, 210, 41, 21))
        self.milkInfinityCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.milkInfinityCheckBox.setStyleSheet(u"")
        self.milkInfinityCheckBox.setChecked(True)
        self.beansInfinityCheckBox = QCheckBox(self.ingredientsGroupBox)
        self.beansInfinityCheckBox.setObjectName(u"beansInfinityCheckBox")
        self.beansInfinityCheckBox.setGeometry(QRect(422, 210, 41, 21))
        self.beansInfinityCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.beansInfinityCheckBox.setStyleSheet(u"")
        self.beansInfinityCheckBox.setChecked(True)
        self.waterSelectionSvg = QSvgWidget(self.ingredientsGroupBox)
        self.waterSelectionSvg.setObjectName(u"waterSelectionSvg")
        self.waterSelectionSvg.setGeometry(QRect(51, 40, 101, 101))
        self.milkSelectionSvg = QSvgWidget(self.ingredientsGroupBox)
        self.milkSelectionSvg.setObjectName(u"milkSelectionSvg")
        self.milkSelectionSvg.setGeometry(QRect(208, 46, 131, 81))
        self.beansSelectionSvg = QSvgWidget(self.ingredientsGroupBox)
        self.beansSelectionSvg.setObjectName(u"beansSelectionSvg")
        self.beansSelectionSvg.setGeometry(QRect(396, 41, 91, 91))
        self.beansSelector.raise_()
        self.waterSelector.raise_()
        self.waterSelectorSuffix.raise_()
        self.milkSelector.raise_()
        self.milkSelectorSuffix.raise_()
        self.beansSelectorSuffix.raise_()
        self.waterInfinityCheckBox.raise_()
        self.milkInfinityCheckBox.raise_()
        self.beansInfinityCheckBox.raise_()
        self.waterSelectionSvg.raise_()
        self.milkSelectionSvg.raise_()
        self.beansSelectionSvg.raise_()
        self.priceGroupBox = QGroupBox(self.mainWidget)
        self.priceGroupBox.setObjectName(u"priceGroupBox")
        self.priceGroupBox.setGeometry(QRect(295, 295, 203, 250))
        self.priceSelectorSuffix = QLabel(self.priceGroupBox)
        self.priceSelectorSuffix.setObjectName(u"priceSelectorSuffix")
        self.priceSelectorSuffix.setGeometry(QRect(138, 159, 21, 31))
        self.priceSelector = QLineEdit(self.priceGroupBox)
        self.priceSelector.setObjectName(u"priceSelector")
        self.priceSelector.setGeometry(QRect(48, 156, 111, 38))
        self.priceInfinityCheckBox = QCheckBox(self.priceGroupBox)
        self.priceInfinityCheckBox.setObjectName(u"priceInfinityCheckBox")
        self.priceInfinityCheckBox.setGeometry(QRect(85, 209, 41, 21))
        self.priceInfinityCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceInfinityCheckBox.setStyleSheet(u"")
        self.priceInfinityCheckBox.setChecked(True)
        self.priceSelectionSvg = QSvgWidget(self.priceGroupBox)
        self.priceSelectionSvg.setObjectName(u"priceSelectionSvg")
        self.priceSelectionSvg.setGeometry(QRect(47, 29, 111, 111))
        self.priceSelector.raise_()
        self.priceSelectorSuffix.raise_()
        self.priceInfinityCheckBox.raise_()
        self.priceSelectionSvg.raise_()
        self.adminPanelLabel = QPushButton(self.mainWidget)
        self.adminPanelLabel.setObjectName(u"adminPanelLabel")
        self.adminPanelLabel.setGeometry(QRect(641, 459, 121, 91))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/users-cog.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adminPanelLabel.setIcon(icon1)
        self.adminPanelLabel.setIconSize(QSize(105, 73))
        self.adminPanelLabel.setFlat(True)
        mainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        self.coffeeGroupBox.setTitle("")
        self.coffeeSelectionLabel.setText(QCoreApplication.translate("mainWindow", u"Regular", None))
        self.coffeeSelector.setInputMask(QCoreApplication.translate("mainWindow", u"99", None))
        self.coffeeSelector.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.coffeeSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"cup of coffee", None))
        self.coffeeInfinityCheckBox.setText("")
        self.ingredientsGroupBox.setTitle("")
        self.waterSelector.setInputMask(QCoreApplication.translate("mainWindow", u"99999", None))
        self.waterSelector.setText(QCoreApplication.translate("mainWindow", u"00001", None))
        self.waterSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"mL of water", None))
        self.milkSelector.setInputMask(QCoreApplication.translate("mainWindow", u"99999", None))
        self.milkSelector.setText(QCoreApplication.translate("mainWindow", u"00001", None))
        self.milkSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"mL of milk", None))
        self.beansSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"g of beans", None))
        self.beansSelector.setInputMask(QCoreApplication.translate("mainWindow", u"99999", None))
        self.beansSelector.setText(QCoreApplication.translate("mainWindow", u"00001", None))
        self.waterInfinityCheckBox.setText("")
        self.milkInfinityCheckBox.setText("")
        self.beansInfinityCheckBox.setText("")
        self.priceGroupBox.setTitle("")
        self.priceSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"$", None))
        self.priceSelector.setInputMask(QCoreApplication.translate("mainWindow", u"99", None))
        self.priceSelector.setText(QCoreApplication.translate("mainWindow", u"01", None))
        self.priceInfinityCheckBox.setText("")
        pass
    # retranslateUi

