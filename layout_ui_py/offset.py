# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offset.ui'
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
        Dialog.resize(241, 187)
        Dialog.setMaximumSize(QSize(241, 187))
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.offsets = QWidget()
        self.offsets.setObjectName(u"offsets")
        self.gridLayout_3 = QGridLayout(self.offsets)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonBox = QDialogButtonBox(self.offsets)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.label = QLabel(self.offsets)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.formWidget = QWidget(self.offsets)
        self.formWidget.setObjectName(u"formWidget")
        self.gridLayout_2 = QGridLayout(self.formWidget)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 20, 20)
        self.xLabel = QLabel(self.formWidget)
        self.xLabel.setObjectName(u"xLabel")

        self.gridLayout_2.addWidget(self.xLabel, 0, 0, 1, 1)

        self.offset_x = QLineEdit(self.formWidget)
        self.offset_x.setObjectName(u"offset_x")

        self.gridLayout_2.addWidget(self.offset_x, 0, 1, 1, 1)

        self.yLabel = QLabel(self.formWidget)
        self.yLabel.setObjectName(u"yLabel")

        self.gridLayout_2.addWidget(self.yLabel, 1, 0, 1, 1)

        self.offset_y = QLineEdit(self.formWidget)
        self.offset_y.setObjectName(u"offset_y")

        self.gridLayout_2.addWidget(self.offset_y, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.formWidget, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.offsets)
        self.scale = QWidget()
        self.scale.setObjectName(u"scale")
        self.gridLayout_4 = QGridLayout(self.scale)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.width_scale = QGroupBox(self.scale)
        self.width_scale.setObjectName(u"width_scale")
        self.gridLayout_5 = QGridLayout(self.width_scale)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setContentsMargins(6, 0, 6, 0)
        self.label_2 = QLabel(self.width_scale)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.current_width = QLineEdit(self.width_scale)
        self.current_width.setObjectName(u"current_width")

        self.gridLayout_5.addWidget(self.current_width, 0, 1, 1, 1)

        self.label_3 = QLabel(self.width_scale)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)

        self.original_width = QLineEdit(self.width_scale)
        self.original_width.setObjectName(u"original_width")

        self.gridLayout_5.addWidget(self.original_width, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.width_scale, 0, 0, 1, 1)

        self.height_scale = QGroupBox(self.scale)
        self.height_scale.setObjectName(u"height_scale")
        self.gridLayout_6 = QGridLayout(self.height_scale)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(2)
        self.gridLayout_6.setContentsMargins(6, 0, 6, 0)
        self.label_5 = QLabel(self.height_scale)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.height_scale)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.current_height = QLineEdit(self.height_scale)
        self.current_height.setObjectName(u"current_height")

        self.gridLayout_6.addWidget(self.current_height, 0, 1, 1, 1)

        self.original_height = QLineEdit(self.height_scale)
        self.original_height.setObjectName(u"original_height")

        self.gridLayout_6.addWidget(self.original_height, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.height_scale, 1, 0, 1, 1)

        self.scale_button = QDialogButtonBox(self.scale)
        self.scale_button.setObjectName(u"scale_button")
        self.scale_button.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_4.addWidget(self.scale_button, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.scale)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Set Offset", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select Offset of  the Map", None))
        self.xLabel.setText(QCoreApplication.translate("Dialog", u"X:", None))
        self.yLabel.setText(QCoreApplication.translate("Dialog", u"Y:", None))
        self.width_scale.setTitle(QCoreApplication.translate("Dialog", u"Width scale:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Current:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Original:", None))
        self.height_scale.setTitle(QCoreApplication.translate("Dialog", u"Height Scale: ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Original:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Current:", None))
    # retranslateUi

