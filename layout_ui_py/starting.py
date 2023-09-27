# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'starting.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(795, 485)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 440, 251, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 10, 821, 41))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font:  arial11pt \"Ubuntu\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 70, 571, 291))
        self.label_3.setPixmap(QPixmap(u"400JpgdpiLogo-1.jpg"))
        self.label_3.setScaledContents(True)
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(140, 390, 491, 23))
        self.progressBar.setStyleSheet(u"border -radius: 25px; color: red;")
        self.progressBar.setValue(16)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 60, 601, 321))
        self.label_4.setPixmap(QPixmap(u"../image/futuristics.jpg"))
        self.label_4.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Copyright\u00a92022, Futuristic Bots LLP", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"   Layout  Designer", None))
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

