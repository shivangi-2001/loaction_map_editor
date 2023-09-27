# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Login_Page(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(833, 685)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font: \"Georgia, serif;\";")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.formFrame = QFrame(self.centralwidget)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setMinimumSize(QSize(475, 475))
        self.formFrame.setMaximumSize(QSize(475, 475))
        self.formFrame.setLayoutDirection(Qt.LeftToRight)
        self.formFrame.setAutoFillBackground(False)
        self.formFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(243, 243, 243,0.3);\n"
"border-radius:12px;\n"
"border:0px;\n"
"}\n"
"")
        self.formFrame.setFrameShadow(QFrame.Plain)
        self.formFrame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.formFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(30, 20, 30, 10)
        self.icon = QLabel(self.formFrame)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(140, 93))
        self.icon.setMaximumSize(QSize(1600, 93))
        font = QFont()
        font.setPointSize(2)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.icon.setFont(font)
        self.icon.setStyleSheet(u"background-color: rgba(243, 243, 243,0.1);")
        self.icon.setPixmap(QPixmap(u"fb.png"))
        self.icon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.icon, 0, 0, 1, 2)

        self.fb = QLabel(self.formFrame)
        self.fb.setObjectName(u"fb")
        self.fb.setMinimumSize(QSize(312, 70))
        self.fb.setMaximumSize(QSize(475, 70))
        font1 = QFont()
        font1.setFamily(u"Georgia, serif;")
        font1.setPointSize(31)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.fb.setFont(font1)
        self.fb.setStyleSheet(u"margin-bottom: 15px;\n"
"color: rgb(32, 74, 135);\n"
"background-color: rgba(243, 243, 243,0.1);")
        self.fb.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fb, 2, 1, 1, 1)

        self.pass_box = QFrame(self.formFrame)
        self.pass_box.setObjectName(u"pass_box")
        self.pass_box.setMinimumSize(QSize(0, 68))
        self.pass_box.setMaximumSize(QSize(400, 60))
        self.pass_box.setStyleSheet(u"padding-left:5px;\n"
"padding-right:5px;\n"
"background-color: rgba(243, 243, 243,0.1);")
        self.pass_box.setFrameShape(QFrame.StyledPanel)
        self.pass_box.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.pass_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.pass_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(90, 20))

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.pass_input = QLineEdit(self.pass_box)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setMinimumSize(QSize(280, 50))
        self.pass_input.setMaximumSize(QSize(280, 50))
        self.pass_input.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(128,128,128);\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"    background-color: #fff;\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid  rgb(114, 159, 207);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.setCursorPosition(0)
        self.pass_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.pass_input, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.pass_box, 6, 1, 1, 1)

        self.user_box = QFrame(self.formFrame)
        self.user_box.setObjectName(u"user_box")
        self.user_box.setMinimumSize(QSize(0, 68))
        self.user_box.setMaximumSize(QSize(400, 60))
        self.user_box.setStyleSheet(u"padding-left:5px;\n"
"background-color: rgba(243, 243, 243,0.1);\n"
"padding-right:5px;")
        self.gridLayout_3 = QGridLayout(self.user_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.user_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(90, 20))

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.user_input = QLineEdit(self.user_box)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setMinimumSize(QSize(280, 50))
        self.user_input.setMaximumSize(QSize(280, 50))
        font2 = QFont()
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.user_input.setFont(font2)
        self.user_input.setAcceptDrops(False)
        self.user_input.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(128,128,128);\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"    background-color: #fff;\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid  rgb(114, 159, 207);\n"
"    color: rgb(0,0,0);\n"
"}")
        self.user_input.setEchoMode(QLineEdit.Normal)
        self.user_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.user_input, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.user_box, 4, 1, 1, 1)

        self.log_btn = QPushButton(self.formFrame)
        self.log_btn.setObjectName(u"log_btn")
        self.log_btn.setMinimumSize(QSize(130, 42))
        self.log_btn.setMaximumSize(QSize(130, 42))
        self.log_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.log_btn.setLayoutDirection(Qt.LeftToRight)
        self.log_btn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px;\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")
        self.log_btn.setCheckable(False)
        self.log_btn.setAutoRepeat(False)

        self.gridLayout_2.addWidget(self.log_btn, 9, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.error = QLabel(self.formFrame)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(280, 20))
        self.error.setMaximumSize(QSize(280, 20))
        self.error.setStyleSheet(u"color: rgb(230, 0, 92);\n"
"background-color: rgba(243, 243, 243,0.1);")

        self.gridLayout_2.addWidget(self.error, 3, 1, 1, 1, Qt.AlignRight)


        self.gridLayout.addWidget(self.formFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login to futuristic bots", None))
        self.icon.setText("")
        self.fb.setText(QCoreApplication.translate("MainWindow", u"futuristic bots", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.pass_input.setText("")
        self.pass_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.user_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.log_btn.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.error.setText("")
    # retranslateUi




