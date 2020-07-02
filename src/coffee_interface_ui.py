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

from components.infinity import InfinityButton

import coffee_interface_resources_rc

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
"QLabel#beanSelectionLabel,\n"
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
"QLineEdit#beanSelector,\n"
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
"QLabel#beanSelectorSuffix,\n"
"QLabel#priceSelectorSuffix {\n"
"  font-family: Segoe UI;\n"
"  font-s"
                        "ize: 14px;\n"
"  color: #6F7987;\n"
"}\n"
"\n"
"QPushButton#adminPushButton {\n"
"  background: none;\n"
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
        self.coffeeGroupBox.setGeometry(QRect(32, 23, 203, 250))
        self.coffeeSelectionPixmap = QLabel(self.coffeeGroupBox)
        self.coffeeSelectionPixmap.setObjectName(u"coffeeSelectionPixmap")
        self.coffeeSelectionPixmap.setGeometry(QRect(47, 26, 100, 114))
        self.coffeeSelectionPixmap.setPixmap(QPixmap(u":/icons/assets/logo.svg"))
        self.coffeeSelectionPixmap.setScaledContents(True)
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
        self.coffeeInfinityPixmap = InfinityButton(self.coffeeGroupBox)
        self.coffeeInfinityPixmap.setObjectName(u"coffeeInfinityPixmap")
        self.coffeeInfinityPixmap.setGeometry(QRect(80, 210, 41, 21))
        self.coffeeInfinityPixmap.setCursor(QCursor(Qt.PointingHandCursor))
        self.coffeeInfinityPixmap.setPixmap(QPixmap(u":/icons/assets/infinity_on.svg"))
        self.coffeeSelector = QLineEdit(self.coffeeGroupBox)
        self.coffeeSelector.setObjectName(u"coffeeSelector")
        self.coffeeSelector.setGeometry(QRect(32, 157, 130, 38))
        self.coffeeSelectorSuffix = QLabel(self.coffeeGroupBox)
        self.coffeeSelectorSuffix.setObjectName(u"coffeeSelectorSuffix")
        self.coffeeSelectorSuffix.setGeometry(QRect(77, 168, 80, 16))
        self.ingredientsGroupBox = QGroupBox(self.mainWidget)
        self.ingredientsGroupBox.setObjectName(u"ingredientsGroupBox")
        self.ingredientsGroupBox.setGeometry(QRect(252, 23, 511, 250))
        self.waterSelector = QLineEdit(self.ingredientsGroupBox)
        self.waterSelector.setObjectName(u"waterSelector")
        self.waterSelector.setGeometry(QRect(20, 157, 153, 38))
        self.waterSelectionPixmap = QLabel(self.ingredientsGroupBox)
        self.waterSelectionPixmap.setObjectName(u"waterSelectionPixmap")
        self.waterSelectionPixmap.setGeometry(QRect(44, 27, 100, 114))
        self.waterSelectionPixmap.setPixmap(QPixmap(u":/icons/assets/faucet-drip.svg"))
        self.waterSelectionPixmap.setScaledContents(False)
        self.waterSelectorSuffix = QLabel(self.ingredientsGroupBox)
        self.waterSelectorSuffix.setObjectName(u"waterSelectorSuffix")
        self.waterSelectorSuffix.setGeometry(QRect(90, 168, 80, 16))
        self.waterInfinityPixmap = InfinityButton(self.ingredientsGroupBox)
        self.waterInfinityPixmap.setObjectName(u"waterInfinityPixmap")
        self.waterInfinityPixmap.setGeometry(QRect(79, 210, 41, 21))
        self.waterInfinityPixmap.setCursor(QCursor(Qt.PointingHandCursor))
        self.waterInfinityPixmap.setPixmap(QPixmap(u":/icons/assets/infinity_on.svg"))
        self.milkSelector = QLineEdit(self.ingredientsGroupBox)
        self.milkSelector.setObjectName(u"milkSelector")
        self.milkSelector.setGeometry(QRect(180, 157, 153, 38))
        self.milkInfinityPixmap = InfinityButton(self.ingredientsGroupBox)
        self.milkInfinityPixmap.setObjectName(u"milkInfinityPixmap")
        self.milkInfinityPixmap.setGeometry(QRect(239, 210, 41, 21))
        self.milkInfinityPixmap.setCursor(QCursor(Qt.PointingHandCursor))
        self.milkInfinityPixmap.setPixmap(QPixmap(u":/icons/assets/infinity_on.svg"))
        self.milkSelectorSuffix = QLabel(self.ingredientsGroupBox)
        self.milkSelectorSuffix.setObjectName(u"milkSelectorSuffix")
        self.milkSelectorSuffix.setGeometry(QRect(250, 168, 80, 16))
        self.milkSelectionPixmap = QLabel(self.ingredientsGroupBox)
        self.milkSelectionPixmap.setObjectName(u"milkSelectionPixmap")
        self.milkSelectionPixmap.setGeometry(QRect(191, 38, 131, 101))
        self.milkSelectionPixmap.setPixmap(QPixmap(u":/icons/assets/cow.svg"))
        self.milkSelectionPixmap.setScaledContents(False)
        self.beanSelectionPixmap = QLabel(self.ingredientsGroupBox)
        self.beanSelectionPixmap.setObjectName(u"beanSelectionPixmap")
        self.beanSelectionPixmap.setGeometry(QRect(368, 40, 100, 101))
        self.beanSelectionPixmap.setPixmap(QPixmap(u":/icons/assets/coffee-beans.svg"))
        self.beanSelectionPixmap.setScaledContents(False)
        self.beanSelectorSuffix = QLabel(self.ingredientsGroupBox)
        self.beanSelectorSuffix.setObjectName(u"beanSelectorSuffix")
        self.beanSelectorSuffix.setGeometry(QRect(412, 167, 80, 21))
        self.beanSelector = QLineEdit(self.ingredientsGroupBox)
        self.beanSelector.setObjectName(u"beanSelector")
        self.beanSelector.setGeometry(QRect(340, 157, 153, 38))
        self.beanInfinityPixmap = InfinityButton(self.ingredientsGroupBox)
        self.beanInfinityPixmap.setObjectName(u"beanInfinityPixmap")
        self.beanInfinityPixmap.setGeometry(QRect(399, 210, 41, 21))
        self.beanInfinityPixmap.setCursor(QCursor(Qt.PointingHandCursor))
        self.beanInfinityPixmap.setPixmap(QPixmap(u":/icons/assets/infinity_on.svg"))
        self.beanSelector.raise_()
        self.waterSelector.raise_()
        self.waterSelectionPixmap.raise_()
        self.waterSelectorSuffix.raise_()
        self.waterInfinityPixmap.raise_()
        self.milkSelector.raise_()
        self.milkInfinityPixmap.raise_()
        self.milkSelectorSuffix.raise_()
        self.milkSelectionPixmap.raise_()
        self.beanSelectionPixmap.raise_()
        self.beanSelectorSuffix.raise_()
        self.beanInfinityPixmap.raise_()
        self.priceGroupBox = QGroupBox(self.mainWidget)
        self.priceGroupBox.setObjectName(u"priceGroupBox")
        self.priceGroupBox.setGeometry(QRect(295, 295, 203, 250))
        self.priceInfinityPixmap = InfinityButton(self.priceGroupBox)
        self.priceInfinityPixmap.setObjectName(u"priceInfinityPixmap")
        self.priceInfinityPixmap.setGeometry(QRect(85, 209, 41, 21))
        self.priceInfinityPixmap.setCursor(QCursor(Qt.PointingHandCursor))
        self.priceInfinityPixmap.setPixmap(QPixmap(u":/icons/assets/infinity_on.svg"))
        self.priceSelectionPixmap = QLabel(self.priceGroupBox)
        self.priceSelectionPixmap.setObjectName(u"priceSelectionPixmap")
        self.priceSelectionPixmap.setGeometry(QRect(47, 30, 121, 111))
        self.priceSelectionPixmap.setPixmap(QPixmap(u":/icons/assets/usd-square.svg"))
        self.priceSelectionPixmap.setScaledContents(False)
        self.priceSelectorSuffix = QLabel(self.priceGroupBox)
        self.priceSelectorSuffix.setObjectName(u"priceSelectorSuffix")
        self.priceSelectorSuffix.setGeometry(QRect(138, 159, 21, 31))
        self.priceSelector = QLineEdit(self.priceGroupBox)
        self.priceSelector.setObjectName(u"priceSelector")
        self.priceSelector.setGeometry(QRect(48, 156, 111, 38))
        self.priceSelector.raise_()
        self.priceInfinityPixmap.raise_()
        self.priceSelectionPixmap.raise_()
        self.priceSelectorSuffix.raise_()
        self.label = QLabel(self.mainWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(658, 463, 111, 91))
        mainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        self.coffeeGroupBox.setTitle("")
        self.coffeeSelectionPixmap.setText("")
        self.coffeeSelectionLabel.setText(QCoreApplication.translate("mainWindow", u"Regular", None))
        self.coffeeInfinityPixmap.setText("")
        self.coffeeSelector.setInputMask(QCoreApplication.translate("mainWindow", u"99", None))
        self.coffeeSelector.setText(QCoreApplication.translate("mainWindow", u"01", None))
        self.coffeeSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"cup of coffee", None))
        self.ingredientsGroupBox.setTitle("")
        self.waterSelector.setInputMask(QCoreApplication.translate("mainWindow", u"9999", None))
        self.waterSelector.setText(QCoreApplication.translate("mainWindow", u"0001", None))
        self.waterSelectionPixmap.setText("")
        self.waterSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"mL of water", None))
        self.waterInfinityPixmap.setText("")
        self.milkSelector.setInputMask(QCoreApplication.translate("mainWindow", u"9999", None))
        self.milkSelector.setText(QCoreApplication.translate("mainWindow", u"0001", None))
        self.milkInfinityPixmap.setText("")
        self.milkSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"mL of milk", None))
        self.milkSelectionPixmap.setText("")
        self.beanSelectionPixmap.setText("")
        self.beanSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"g of beans", None))
        self.beanSelector.setInputMask(QCoreApplication.translate("mainWindow", u"9999", None))
        self.beanSelector.setText(QCoreApplication.translate("mainWindow", u"0001", None))
        self.beanInfinityPixmap.setText("")
        self.priceGroupBox.setTitle("")
        self.priceInfinityPixmap.setText("")
        self.priceSelectionPixmap.setText("")
        self.priceSelectorSuffix.setText(QCoreApplication.translate("mainWindow", u"$", None))
        self.priceSelector.setInputMask(QCoreApplication.translate("mainWindow", u"999", None))
        self.priceSelector.setText(QCoreApplication.translate("mainWindow", u"001", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><a href=\"none\"><img src=\":/icons/assets/users-cog.svg\"/></a></p></body></html>", None))
        pass
    # retranslateUi

