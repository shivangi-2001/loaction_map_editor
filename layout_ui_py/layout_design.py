# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout_designer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LayoutDesigner(object):
    def setupUi(self, LayoutDesigner):
        if not LayoutDesigner.objectName():
            LayoutDesigner.setObjectName(u"LayoutDesigner")
        LayoutDesigner.resize(1383, 986)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LayoutDesigner.sizePolicy().hasHeightForWidth())
        LayoutDesigner.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        LayoutDesigner.setFont(font)
        LayoutDesigner.setStyleSheet(u"")
        self.actionNew = QAction(LayoutDesigner)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(LayoutDesigner)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setEnabled(True)
        self.ExportCostMap = QAction(LayoutDesigner)
        self.ExportCostMap.setObjectName(u"ExportCostMap")
        self.actionSave = QAction(LayoutDesigner)
        self.actionSave.setObjectName(u"actionSave")
        self.actionRecent = QAction(LayoutDesigner)
        self.actionRecent.setObjectName(u"actionRecent")
        self.actionUndo = QAction(LayoutDesigner)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(LayoutDesigner)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionMarks = QAction(LayoutDesigner)
        self.actionMarks.setObjectName(u"actionMarks")
        self.actionMark = QAction(LayoutDesigner)
        self.actionMark.setObjectName(u"actionMark")
        self.actionEdit = QAction(LayoutDesigner)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionRotate = QAction(LayoutDesigner)
        self.actionRotate.setObjectName(u"actionRotate")
        self.actionCrop = QAction(LayoutDesigner)
        self.actionCrop.setObjectName(u"actionCrop")
        self.actionLog_out = QAction(LayoutDesigner)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.actionZoom_In = QAction(LayoutDesigner)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        self.actionZoom_out = QAction(LayoutDesigner)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionclean_map = QAction(LayoutDesigner)
        self.actionclean_map.setObjectName(u"actionclean_map")
        self.actionStation = QAction(LayoutDesigner)
        self.actionStation.setObjectName(u"actionStation")
        self.actionChange_speed = QAction(LayoutDesigner)
        self.actionChange_speed.setObjectName(u"actionChange_speed")
        self.actionChange_Speed = QAction(LayoutDesigner)
        self.actionChange_Speed.setObjectName(u"actionChange_Speed")
        self.actionStation_Window = QAction(LayoutDesigner)
        self.actionStation_Window.setObjectName(u"actionStation_Window")
        self.actionChanged_Speed = QAction(LayoutDesigner)
        self.actionChanged_Speed.setObjectName(u"actionChanged_Speed")
        self.action2D_Pose = QAction(LayoutDesigner)
        self.action2D_Pose.setObjectName(u"action2D_Pose")
        self.actionSelect = QAction(LayoutDesigner)
        self.actionSelect.setObjectName(u"actionSelect")
        self.actionExport_clean_map = QAction(LayoutDesigner)
        self.actionExport_clean_map.setObjectName(u"actionExport_clean_map")
        self.actionWaypoints = QAction(LayoutDesigner)
        self.actionWaypoints.setObjectName(u"actionWaypoints")
        self.centralwidget = QWidget(LayoutDesigner)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(936, 700))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.heading = QLabel(self.widget)
        self.heading.setObjectName(u"heading")
        self.heading.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Sawasdee")
        font1.setPointSize(7)
        self.heading.setFont(font1)
        self.heading.setTabletTracking(True)
        self.heading.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.heading.setFrameShadow(QFrame.Raised)
        self.heading.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.heading, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(225, 16777215))
        self.widget_3.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(10, -1, -1, -1)
        self.type_zone = QComboBox(self.widget_3)
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.addItem("")
        self.type_zone.setObjectName(u"type_zone")
        self.type_zone.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.type_zone.setFont(font2)
        self.type_zone.setCursor(QCursor(Qt.PointingHandCursor))
        self.type_zone.setTabletTracking(False)
        self.type_zone.setAcceptDrops(True)
        self.type_zone.setAutoFillBackground(False)
        self.type_zone.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 3px;\n"
"    padding:3px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color:rgba(114, 159, 207, 0.7);\n"
"	color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"")
        self.type_zone.setEditable(False)

        self.gridLayout_2.addWidget(self.type_zone, 0, 0, 1, 1)

        self.shape_zone = QComboBox(self.widget_3)
        self.shape_zone.addItem("")
        self.shape_zone.addItem("")
        self.shape_zone.addItem("")
        self.shape_zone.setObjectName(u"shape_zone")
        self.shape_zone.setMaximumSize(QSize(16777215, 35))
        self.shape_zone.setFont(font2)
        self.shape_zone.setCursor(QCursor(Qt.PointingHandCursor))
        self.shape_zone.setAcceptDrops(True)
        self.shape_zone.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 3px;\n"
"    padding:3px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color:rgba(114, 159, 207, 0.7);\n"
"	color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"")
        self.shape_zone.setEditable(False)

        self.gridLayout_2.addWidget(self.shape_zone, 1, 0, 1, 1)

        self.offset_label = QWidget(self.widget_3)
        self.offset_label.setObjectName(u"offset_label")
        self.offset_label.setMinimumSize(QSize(0, 30))
        self.gridLayout_28 = QGridLayout(self.offset_label)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.offset = QLabel(self.offset_label)
        self.offset.setObjectName(u"offset")
        font3 = QFont()
        font3.setPointSize(10)
        self.offset.setFont(font3)
        self.offset.setAlignment(Qt.AlignCenter)
        self.offset.setMargin(-2)

        self.gridLayout_28.addWidget(self.offset, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.offset_label, 2, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(1)
        self.stackedWidget.setFont(font4)
        self.front = QWidget()
        self.front.setObjectName(u"front")
        self.stackedWidget.addWidget(self.front)
        self.Manual = QWidget()
        self.Manual.setObjectName(u"Manual")
        self.enter_coordinates = QWidget(self.Manual)
        self.enter_coordinates.setObjectName(u"enter_coordinates")
        self.enter_coordinates.setGeometry(QRect(-10, 20, 241, 211))
        self.enter_coordinates.setMaximumSize(QSize(16777215, 250))
        self.gridLayout_14 = QGridLayout(self.enter_coordinates)
        self.gridLayout_14.setSpacing(10)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(15, 15, 15, 15)
        self.s2 = QWidget(self.enter_coordinates)
        self.s2.setObjectName(u"s2")
        self.s2.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_17 = QGridLayout(self.s2)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 25, 0)
        self.xLabel_3 = QLabel(self.s2)
        self.xLabel_3.setObjectName(u"xLabel_3")

        self.gridLayout_17.addWidget(self.xLabel_3, 1, 0, 1, 1, Qt.AlignHCenter)

        self.X_user_input = QLineEdit(self.s2)
        self.X_user_input.setObjectName(u"X_user_input")
        self.X_user_input.setMinimumSize(QSize(0, 30))
        self.X_user_input.setMaximumSize(QSize(150, 16777215))
        self.X_user_input.setReadOnly(False)

        self.gridLayout_17.addWidget(self.X_user_input, 1, 1, 1, 1)


        self.gridLayout_14.addWidget(self.s2, 2, 0, 1, 1)

        self.s1 = QWidget(self.enter_coordinates)
        self.s1.setObjectName(u"s1")
        self.s1.setMaximumSize(QSize(16777215, 40))
        self.gridLayout_16 = QGridLayout(self.s1)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 25, 0)
        self.Y_user_input = QLineEdit(self.s1)
        self.Y_user_input.setObjectName(u"Y_user_input")
        self.Y_user_input.setMinimumSize(QSize(0, 30))
        self.Y_user_input.setMaximumSize(QSize(150, 16777215))
        self.Y_user_input.setReadOnly(False)

        self.gridLayout_16.addWidget(self.Y_user_input, 0, 1, 1, 1)

        self.label_13 = QLabel(self.s1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_16.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_14.addWidget(self.s1, 3, 0, 1, 1)

        self.coordinates_enter = QLabel(self.enter_coordinates)
        self.coordinates_enter.setObjectName(u"coordinates_enter")
        self.coordinates_enter.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.coordinates_enter.setFont(font5)

        self.gridLayout_14.addWidget(self.coordinates_enter, 0, 0, 1, 1, Qt.AlignHCenter)

        self.calculate = QPushButton(self.enter_coordinates)
        self.calculate.setObjectName(u"calculate")
        self.calculate.setMinimumSize(QSize(100, 32))
        self.calculate.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px;\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")

        self.gridLayout_14.addWidget(self.calculate, 4, 0, 1, 1, Qt.AlignHCenter)

        self.coord_status = QLabel(self.enter_coordinates)
        self.coord_status.setObjectName(u"coord_status")
        self.coord_status.setMaximumSize(QSize(16777215, 25))
        self.coord_status.setStyleSheet(u"color: rgb(51, 209, 122);")

        self.gridLayout_14.addWidget(self.coord_status, 1, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.Manual)
        self.upadatelocation = QWidget()
        self.upadatelocation.setObjectName(u"upadatelocation")
        self.gridWidget = QWidget(self.upadatelocation)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setGeometry(QRect(0, 0, 210, 729))
        self.gridWidget.setMinimumSize(QSize(210, 0))
        self.gridWidget.setMaximumSize(QSize(210, 16777215))
        self.gridLayout_22 = QGridLayout(self.gridWidget)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(6)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.update_box = QGroupBox(self.gridWidget)
        self.update_box.setObjectName(u"update_box")
        self.update_box.setMaximumSize(QSize(200, 280))
        self.update_box.setAlignment(Qt.AlignCenter)
        self.gridLayout_24 = QGridLayout(self.update_box)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.presnt_widget = QWidget(self.update_box)
        self.presnt_widget.setObjectName(u"presnt_widget")
        self.presnt_widget.setMinimumSize(QSize(0, 0))
        self.presnt_widget.setMaximumSize(QSize(16777215, 300))
        self.formLayout_3 = QFormLayout(self.presnt_widget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(9)
        self.formLayout_3.setVerticalSpacing(9)
        self.formLayout_3.setContentsMargins(20, 15, 20, 10)
        self.x_posLabel = QLabel(self.presnt_widget)
        self.x_posLabel.setObjectName(u"x_posLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.x_posLabel)

        self.x_posLineEdit = QLineEdit(self.presnt_widget)
        self.x_posLineEdit.setObjectName(u"x_posLineEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.x_posLineEdit)

        self.y_posLabel = QLabel(self.presnt_widget)
        self.y_posLabel.setObjectName(u"y_posLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.y_posLabel)

        self.y_posLineEdit = QLineEdit(self.presnt_widget)
        self.y_posLineEdit.setObjectName(u"y_posLineEdit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.y_posLineEdit)

        self.z_poseLabel = QLabel(self.presnt_widget)
        self.z_poseLabel.setObjectName(u"z_poseLabel")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.z_poseLabel)

        self.z_poseLineEdit = QLineEdit(self.presnt_widget)
        self.z_poseLineEdit.setObjectName(u"z_poseLineEdit")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.z_poseLineEdit)

        self.w_poseLabel_2 = QLabel(self.presnt_widget)
        self.w_poseLabel_2.setObjectName(u"w_poseLabel_2")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.w_poseLabel_2)

        self.w_poseLineEdit = QLineEdit(self.presnt_widget)
        self.w_poseLineEdit.setObjectName(u"w_poseLineEdit")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.w_poseLineEdit)

        self.Location_Label = QLabel(self.presnt_widget)
        self.Location_Label.setObjectName(u"Location_Label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Location_Label)

        self.Location_LineEdit = QLineEdit(self.presnt_widget)
        self.Location_LineEdit.setObjectName(u"Location_LineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.Location_LineEdit)

        self.label_20 = QLabel(self.presnt_widget)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.presnt_widget)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_21)

        self.level_LIneEdit = QLineEdit(self.presnt_widget)
        self.level_LIneEdit.setObjectName(u"level_LIneEdit")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.level_LIneEdit)

        self.Height_LineEdit = QLineEdit(self.presnt_widget)
        self.Height_LineEdit.setObjectName(u"Height_LineEdit")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.Height_LineEdit)


        self.gridLayout_24.addWidget(self.presnt_widget, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.update_box, 4, 0, 1, 1)

        self.question = QWidget(self.gridWidget)
        self.question.setObjectName(u"question")
        self.question.setMaximumSize(QSize(200, 100))
        self.formLayout_6 = QFormLayout(self.question)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(10, 15, 10, 10)
        self.label_19 = QLabel(self.question)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_19)

        self.question_text = QLineEdit(self.question)
        self.question_text.setObjectName(u"question_text")
        self.question_text.setMaximumSize(QSize(150, 16777215))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.question_text)

        self.OK = QDialogButtonBox(self.question)
        self.OK.setObjectName(u"OK")
        self.OK.setStandardButtons(QDialogButtonBox.Ok)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.OK)


        self.gridLayout_22.addWidget(self.question, 0, 0, 1, 2)

        self.button_box = QWidget(self.gridWidget)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setMinimumSize(QSize(0, 30))
        self.button_box.setMaximumSize(QSize(220, 30))
        self.gridLayout_25 = QGridLayout(self.button_box)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.run = QPushButton(self.button_box)
        self.run.setObjectName(u"run")
        self.run.setMaximumSize(QSize(50, 25))
        self.run.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px;\n"
"   	color: rgb(0, 255, 0);\n"
"	border:1px solid rgb(0, 255, 0);\n"
"}\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.run, 0, 0, 1, 1)

        self.stop = QPushButton(self.button_box)
        self.stop.setObjectName(u"stop")
        self.stop.setMaximumSize(QSize(50, 25))
        self.stop.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px;\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")

        self.gridLayout_25.addWidget(self.stop, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.button_box, 3, 0, 1, 1)

        self.current_box = QGroupBox(self.gridWidget)
        self.current_box.setObjectName(u"current_box")
        self.current_box.setMaximumSize(QSize(200, 250))
        self.current_box.setAlignment(Qt.AlignCenter)
        self.gridLayout_23 = QGridLayout(self.current_box)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.current_widget = QWidget(self.current_box)
        self.current_widget.setObjectName(u"current_widget")
        self.current_widget.setMaximumSize(QSize(16777215, 300))
        self.formLayout_4 = QFormLayout(self.current_widget)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(9)
        self.formLayout_4.setVerticalSpacing(9)
        self.formLayout_4.setContentsMargins(20, 15, 20, 10)
        self.currentLocationLabel = QLabel(self.current_widget)
        self.currentLocationLabel.setObjectName(u"currentLocationLabel")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.currentLocationLabel)

        self.currentLocationLineEdit = QLineEdit(self.current_widget)
        self.currentLocationLineEdit.setObjectName(u"currentLocationLineEdit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.currentLocationLineEdit)

        self.current_xLabel = QLabel(self.current_widget)
        self.current_xLabel.setObjectName(u"current_xLabel")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.current_xLabel)

        self.current_xLineEdit = QLineEdit(self.current_widget)
        self.current_xLineEdit.setObjectName(u"current_xLineEdit")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.current_xLineEdit)

        self.current_yLabel = QLabel(self.current_widget)
        self.current_yLabel.setObjectName(u"current_yLabel")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.current_yLabel)

        self.current_yLineEdit = QLineEdit(self.current_widget)
        self.current_yLineEdit.setObjectName(u"current_yLineEdit")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.current_yLineEdit)

        self.currentzposeLabel = QLabel(self.current_widget)
        self.currentzposeLabel.setObjectName(u"currentzposeLabel")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.currentzposeLabel)

        self.currentzposeLineEdit = QLineEdit(self.current_widget)
        self.currentzposeLineEdit.setObjectName(u"currentzposeLineEdit")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.currentzposeLineEdit)

        self.currentwposeLabel = QLabel(self.current_widget)
        self.currentwposeLabel.setObjectName(u"currentwposeLabel")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.currentwposeLabel)

        self.currentwposeLineEdit = QLineEdit(self.current_widget)
        self.currentwposeLineEdit.setObjectName(u"currentwposeLineEdit")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.currentwposeLineEdit)

        self.currentLevelLabel = QLabel(self.current_widget)
        self.currentLevelLabel.setObjectName(u"currentLevelLabel")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.currentLevelLabel)

        self.currentLevelLineEdit = QLineEdit(self.current_widget)
        self.currentLevelLineEdit.setObjectName(u"currentLevelLineEdit")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.currentLevelLineEdit)

        self.currentHeightLabel = QLabel(self.current_widget)
        self.currentHeightLabel.setObjectName(u"currentHeightLabel")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.currentHeightLabel)

        self.currentHeightLineEdit = QLineEdit(self.current_widget)
        self.currentHeightLineEdit.setObjectName(u"currentHeightLineEdit")

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.currentHeightLineEdit)


        self.gridLayout_23.addWidget(self.current_widget, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.current_box, 2, 0, 1, 1)

        self.update = QPushButton(self.gridWidget)
        self.update.setObjectName(u"update")
        self.update.setMinimumSize(QSize(0, 30))
        self.update.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px;\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")

        self.gridLayout_22.addWidget(self.update, 5, 0, 1, 1)

        self.stackedWidget.addWidget(self.upadatelocation)
        self.Reflector = QWidget()
        self.Reflector.setObjectName(u"Reflector")
        self.reflector_location = QWidget(self.Reflector)
        self.reflector_location.setObjectName(u"reflector_location")
        self.reflector_location.setGeometry(QRect(-5, 17, 220, 221))
        self.reflector_location.setMinimumSize(QSize(220, 0))
        self.reflector_location.setMaximumSize(QSize(220, 16777215))
        self.gridLayout_26 = QGridLayout(self.reflector_location)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(15, -1, 20, -1)
        self.label_22 = QLabel(self.reflector_location)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_26.addWidget(self.label_22, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_24 = QLabel(self.reflector_location)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_26.addWidget(self.label_24, 3, 0, 1, 1, Qt.AlignHCenter)

        self.r_x = QLineEdit(self.reflector_location)
        self.r_x.setObjectName(u"r_x")

        self.gridLayout_26.addWidget(self.r_x, 1, 1, 1, 1)

        self.r_y = QLineEdit(self.reflector_location)
        self.r_y.setObjectName(u"r_y")

        self.gridLayout_26.addWidget(self.r_y, 2, 1, 1, 1)

        self.r_name = QLineEdit(self.reflector_location)
        self.r_name.setObjectName(u"r_name")

        self.gridLayout_26.addWidget(self.r_name, 3, 1, 1, 1)

        self.label_25 = QLabel(self.reflector_location)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 30))
        self.label_25.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_25.setFont(font6)

        self.gridLayout_26.addWidget(self.label_25, 0, 0, 1, 2, Qt.AlignHCenter)

        self.label_23 = QLabel(self.reflector_location)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_26.addWidget(self.label_23, 2, 0, 1, 1, Qt.AlignHCenter)

        self.reflector = QPushButton(self.reflector_location)
        self.reflector.setObjectName(u"reflector")
        self.reflector.setMaximumSize(QSize(16777215, 35))
        self.reflector.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_26.addWidget(self.reflector, 4, 0, 1, 2)

        self.stackedWidget.addWidget(self.Reflector)
        self.Text_Notation = QWidget()
        self.Text_Notation.setObjectName(u"Text_Notation")
        self.text_notation_widget = QWidget(self.Text_Notation)
        self.text_notation_widget.setObjectName(u"text_notation_widget")
        self.text_notation_widget.setGeometry(QRect(0, 20, 200, 151))
        self.text_notation_widget.setMinimumSize(QSize(200, 0))
        self.text_notation_widget.setMaximumSize(QSize(220, 16777215))
        self.gridLayout_27 = QGridLayout(self.text_notation_widget)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_27 = QLabel(self.text_notation_widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font6)

        self.gridLayout_27.addWidget(self.label_27, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_26 = QLabel(self.text_notation_widget)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_27.addWidget(self.label_26, 1, 0, 1, 1)

        self.text = QLineEdit(self.text_notation_widget)
        self.text.setObjectName(u"text")

        self.gridLayout_27.addWidget(self.text, 2, 0, 1, 1)

        self.text_notation = QPushButton(self.text_notation_widget)
        self.text_notation.setObjectName(u"text_notation")
        self.text_notation.setMaximumSize(QSize(16777215, 35))
        self.text_notation.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_27.addWidget(self.text_notation, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.Text_Notation)
        self.dock_location = QWidget()
        self.dock_location.setObjectName(u"dock_location")
        self.dock_widget = QWidget(self.dock_location)
        self.dock_widget.setObjectName(u"dock_widget")
        self.dock_widget.setGeometry(QRect(0, 10, 201, 331))
        self.gridLayout_18 = QGridLayout(self.dock_widget)
        self.gridLayout_18.setSpacing(10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(5, 15, 10, 15)
        self.label_15 = QLabel(self.dock_widget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_18.addWidget(self.label_15, 5, 0, 1, 1, Qt.AlignHCenter)

        self.dock_x = QLineEdit(self.dock_widget)
        self.dock_x.setObjectName(u"dock_x")
        self.dock_x.setMinimumSize(QSize(0, 30))
        self.dock_x.setReadOnly(False)

        self.gridLayout_18.addWidget(self.dock_x, 2, 1, 1, 1)

        self.station_link = QLineEdit(self.dock_widget)
        self.station_link.setObjectName(u"station_link")
        self.station_link.setMinimumSize(QSize(0, 30))
        self.station_link.setReadOnly(False)

        self.gridLayout_18.addWidget(self.station_link, 6, 1, 1, 1)

        self.xLabel_2 = QLabel(self.dock_widget)
        self.xLabel_2.setObjectName(u"xLabel_2")

        self.gridLayout_18.addWidget(self.xLabel_2, 2, 0, 1, 1, Qt.AlignHCenter)

        self.yLabel_2 = QLabel(self.dock_widget)
        self.yLabel_2.setObjectName(u"yLabel_2")

        self.gridLayout_18.addWidget(self.yLabel_2, 3, 0, 1, 1, Qt.AlignHCenter)

        self.dock_name = QLineEdit(self.dock_widget)
        self.dock_name.setObjectName(u"dock_name")
        self.dock_name.setMinimumSize(QSize(0, 30))

        self.gridLayout_18.addWidget(self.dock_name, 1, 1, 1, 1)

        self.dock = QPushButton(self.dock_widget)
        self.dock.setObjectName(u"dock")
        self.dock.setMinimumSize(QSize(0, 32))
        self.dock.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-radius: 20px;\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")

        self.gridLayout_18.addWidget(self.dock, 7, 0, 1, 2)

        self.associatedStationLabel = QLabel(self.dock_widget)
        self.associatedStationLabel.setObjectName(u"associatedStationLabel")

        self.gridLayout_18.addWidget(self.associatedStationLabel, 6, 0, 1, 1, Qt.AlignHCenter)

        self.dock_pose_z = QLineEdit(self.dock_widget)
        self.dock_pose_z.setObjectName(u"dock_pose_z")
        self.dock_pose_z.setMinimumSize(QSize(0, 30))
        self.dock_pose_z.setReadOnly(False)

        self.gridLayout_18.addWidget(self.dock_pose_z, 4, 1, 1, 1)

        self.dock_pose_w = QLineEdit(self.dock_widget)
        self.dock_pose_w.setObjectName(u"dock_pose_w")
        self.dock_pose_w.setMinimumSize(QSize(0, 30))
        self.dock_pose_w.setReadOnly(False)

        self.gridLayout_18.addWidget(self.dock_pose_w, 5, 1, 1, 1)

        self.poseLabel_2 = QLabel(self.dock_widget)
        self.poseLabel_2.setObjectName(u"poseLabel_2")

        self.gridLayout_18.addWidget(self.poseLabel_2, 4, 0, 1, 1, Qt.AlignHCenter)

        self.dock_y = QLineEdit(self.dock_widget)
        self.dock_y.setObjectName(u"dock_y")
        self.dock_y.setMinimumSize(QSize(0, 30))
        self.dock_y.setReadOnly(False)

        self.gridLayout_18.addWidget(self.dock_y, 3, 1, 1, 1)

        self.label_14 = QLabel(self.dock_widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_29 = QLabel(self.dock_widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font6)

        self.gridLayout_18.addWidget(self.label_29, 0, 0, 1, 2, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.dock_location)
        self.station_location = QWidget()
        self.station_location.setObjectName(u"station_location")
        self.formFrame = QFrame(self.station_location)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setGeometry(QRect(0, 20, 211, 541))
        self.formFrame.setMinimumSize(QSize(0, 0))
        self.formFrame.setMaximumSize(QSize(16777215, 16777215))
        self.formFrame.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_19 = QGridLayout(self.formFrame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(9, -1, 12, -1)
        self.stationNameLabel = QLabel(self.formFrame)
        self.stationNameLabel.setObjectName(u"stationNameLabel")

        self.gridLayout_19.addWidget(self.stationNameLabel, 1, 0, 1, 2, Qt.AlignHCenter)

        self.add_station_toggle = QGroupBox(self.formFrame)
        self.add_station_toggle.setObjectName(u"add_station_toggle")
        self.add_station_toggle.setMinimumSize(QSize(100, 0))
        self.add_station_toggle.setMaximumSize(QSize(306, 150))
        self.gridLayout_20 = QGridLayout(self.add_station_toggle)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setVerticalSpacing(10)
        self.gridLayout_20.setContentsMargins(9, 9, 9, 9)
        self.label_16 = QLabel(self.add_station_toggle)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_20.addWidget(self.label_16, 0, 0, 1, 1)

        self.add_station = QPushButton(self.add_station_toggle)
        self.add_station.setObjectName(u"add_station")
        self.add_station.setMinimumSize(QSize(0, 32))
        self.add_station.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_20.addWidget(self.add_station, 2, 0, 1, 2)

        self.label_17 = QLabel(self.add_station_toggle)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_20.addWidget(self.label_17, 1, 0, 1, 1)

        self.addHeight = QComboBox(self.add_station_toggle)
        self.addHeight.addItem("")
        self.addHeight.addItem("")
        self.addHeight.addItem("")
        self.addHeight.addItem("")
        self.addHeight.setObjectName(u"addHeight")
        self.addHeight.setMinimumSize(QSize(0, 30))
        self.addHeight.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 3px;\n"
"    padding:3px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: rgba(114, 159, 207,0.7);\n"
"color: rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.gridLayout_20.addWidget(self.addHeight, 1, 1, 1, 1)

        self.addLevel = QSpinBox(self.add_station_toggle)
        self.addLevel.setObjectName(u"addLevel")
        self.addLevel.setMinimumSize(QSize(0, 30))
        self.addLevel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_20.addWidget(self.addLevel, 0, 1, 1, 1)


        self.gridLayout_19.addWidget(self.add_station_toggle, 12, 0, 1, 3)

        self.xLabel_4 = QLabel(self.formFrame)
        self.xLabel_4.setObjectName(u"xLabel_4")

        self.gridLayout_19.addWidget(self.xLabel_4, 2, 0, 1, 2, Qt.AlignHCenter)

        self.levelLabel = QLabel(self.formFrame)
        self.levelLabel.setObjectName(u"levelLabel")

        self.gridLayout_19.addWidget(self.levelLabel, 6, 0, 1, 2, Qt.AlignHCenter)

        self.Height = QComboBox(self.formFrame)
        self.Height.addItem("")
        self.Height.addItem("")
        self.Height.addItem("")
        self.Height.addItem("")
        self.Height.addItem("")
        self.Height.setObjectName(u"Height")
        self.Height.setMinimumSize(QSize(0, 30))
        self.Height.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 3px;\n"
"    padding:3px;\n"
"    background-color: #FFFFFF;\n"
"    selection-background-color: rgba(114, 159, 207,0.7);\n"
"color: rgb(0,0,0);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.Height, 7, 2, 1, 1)

        self.poseLabel = QLabel(self.formFrame)
        self.poseLabel.setObjectName(u"poseLabel")

        self.gridLayout_19.addWidget(self.poseLabel, 4, 0, 1, 2, Qt.AlignHCenter)

        self.heightLabel = QLabel(self.formFrame)
        self.heightLabel.setObjectName(u"heightLabel")

        self.gridLayout_19.addWidget(self.heightLabel, 7, 0, 1, 2, Qt.AlignHCenter)

        self.station_button = QWidget(self.formFrame)
        self.station_button.setObjectName(u"station_button")
        self.station_button.setMinimumSize(QSize(0, 32))
        self.station_button.setMaximumSize(QSize(16777215, 32))
        self.gridLayout_21 = QGridLayout(self.station_button)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.station = QPushButton(self.station_button)
        self.station.setObjectName(u"station")
        self.station.setMinimumSize(QSize(0, 32))
        self.station.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_21.addWidget(self.station, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.station_button, 8, 0, 1, 3)

        self.yLabel_3 = QLabel(self.formFrame)
        self.yLabel_3.setObjectName(u"yLabel_3")

        self.gridLayout_19.addWidget(self.yLabel_3, 3, 0, 1, 2, Qt.AlignHCenter)

        self.label_18 = QLabel(self.formFrame)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_19.addWidget(self.label_18, 5, 0, 1, 2, Qt.AlignHCenter)

        self.PoseZ = QLineEdit(self.formFrame)
        self.PoseZ.setObjectName(u"PoseZ")
        self.PoseZ.setMinimumSize(QSize(0, 30))
        self.PoseZ.setReadOnly(False)

        self.gridLayout_19.addWidget(self.PoseZ, 4, 2, 1, 1)

        self.stack_btn = QToolButton(self.formFrame)
        self.stack_btn.setObjectName(u"stack_btn")
        self.stack_btn.setStyleSheet(u"border: 0px;\n"
"width: 15px;\n"
"height: 15px;")

        self.gridLayout_19.addWidget(self.stack_btn, 11, 0, 1, 1)

        self.Level = QSpinBox(self.formFrame)
        self.Level.setObjectName(u"Level")
        self.Level.setMinimumSize(QSize(0, 30))
        self.Level.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.Level, 6, 2, 1, 1)

        self.stack_station = QLabel(self.formFrame)
        self.stack_station.setObjectName(u"stack_station")
        self.stack_station.setMinimumSize(QSize(0, 0))
        self.stack_station.setMaximumSize(QSize(500, 16777215))
        self.stack_station.setStyleSheet(u"QLabel:hover {\n"
"    border-bottom: 1px solid rgb(65, 65, 65);\n"
"	color: rgb(65, 65, 65);	\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgba(0,0,0,0.7)\n"
"}")
        self.stack_station.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.stack_station, 11, 1, 1, 2)

        self.station_x = QLineEdit(self.formFrame)
        self.station_x.setObjectName(u"station_x")
        self.station_x.setMinimumSize(QSize(0, 30))
        self.station_x.setReadOnly(False)

        self.gridLayout_19.addWidget(self.station_x, 2, 2, 1, 1)

        self.station_y = QLineEdit(self.formFrame)
        self.station_y.setObjectName(u"station_y")
        self.station_y.setMinimumSize(QSize(0, 30))
        self.station_y.setReadOnly(False)

        self.gridLayout_19.addWidget(self.station_y, 3, 2, 1, 1)

        self.station_name = QLineEdit(self.formFrame)
        self.station_name.setObjectName(u"station_name")
        self.station_name.setMinimumSize(QSize(0, 30))

        self.gridLayout_19.addWidget(self.station_name, 1, 2, 1, 1)

        self.PoseW = QLineEdit(self.formFrame)
        self.PoseW.setObjectName(u"PoseW")
        self.PoseW.setMinimumSize(QSize(0, 30))
        self.PoseW.setReadOnly(False)

        self.gridLayout_19.addWidget(self.PoseW, 5, 2, 1, 1)

        self.label_28 = QLabel(self.formFrame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 30))
        self.label_28.setFont(font6)

        self.gridLayout_19.addWidget(self.label_28, 0, 0, 1, 3, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.station_location)
        self.waypoints_stack = QWidget()
        self.waypoints_stack.setObjectName(u"waypoints_stack")
        self.formWidget = QWidget(self.waypoints_stack)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(0, 30, 201, 281))
        self.waypoints_widget = QGridLayout(self.formWidget)
        self.waypoints_widget.setObjectName(u"waypoints_widget")
        self.label_12 = QLabel(self.formWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(100, 30))
        self.label_12.setFont(font6)
        self.label_12.setMargin(0)

        self.waypoints_widget.addWidget(self.label_12, 0, 0, 1, 2, Qt.AlignHCenter)

        self.pose_zlabel = QLabel(self.formWidget)
        self.pose_zlabel.setObjectName(u"pose_zlabel")

        self.waypoints_widget.addWidget(self.pose_zlabel, 3, 0, 1, 1, Qt.AlignHCenter)

        self.yLabel = QLabel(self.formWidget)
        self.yLabel.setObjectName(u"yLabel")

        self.waypoints_widget.addWidget(self.yLabel, 2, 0, 1, 1, Qt.AlignHCenter)

        self.wx = QLineEdit(self.formWidget)
        self.wx.setObjectName(u"wx")

        self.waypoints_widget.addWidget(self.wx, 1, 1, 1, 1)

        self.station2Label = QLabel(self.formWidget)
        self.station2Label.setObjectName(u"station2Label")

        self.waypoints_widget.addWidget(self.station2Label, 7, 0, 1, 1, Qt.AlignHCenter)

        self.station2 = QLineEdit(self.formWidget)
        self.station2.setObjectName(u"station2")

        self.waypoints_widget.addWidget(self.station2, 7, 1, 1, 1)

        self.station1 = QLineEdit(self.formWidget)
        self.station1.setObjectName(u"station1")

        self.waypoints_widget.addWidget(self.station1, 6, 1, 1, 1)

        self.station1Label = QLabel(self.formWidget)
        self.station1Label.setObjectName(u"station1Label")

        self.waypoints_widget.addWidget(self.station1Label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.pose_wLabel = QLabel(self.formWidget)
        self.pose_wLabel.setObjectName(u"pose_wLabel")

        self.waypoints_widget.addWidget(self.pose_wLabel, 4, 0, 1, 1, Qt.AlignHCenter)

        self.wy = QLineEdit(self.formWidget)
        self.wy.setObjectName(u"wy")

        self.waypoints_widget.addWidget(self.wy, 2, 1, 1, 1)

        self.ww_pose = QLineEdit(self.formWidget)
        self.ww_pose.setObjectName(u"ww_pose")

        self.waypoints_widget.addWidget(self.ww_pose, 4, 1, 1, 1)

        self.waypoints = QPushButton(self.formWidget)
        self.waypoints.setObjectName(u"waypoints")
        self.waypoints.setMinimumSize(QSize(50, 30))
        self.waypoints.setStyleSheet(u"QPushButton{\n"
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

        self.waypoints_widget.addWidget(self.waypoints, 8, 0, 1, 2)

        self.wz_pose = QLineEdit(self.formWidget)
        self.wz_pose.setObjectName(u"wz_pose")

        self.waypoints_widget.addWidget(self.wz_pose, 3, 1, 1, 1)

        self.xLabel = QLabel(self.formWidget)
        self.xLabel.setObjectName(u"xLabel")

        self.waypoints_widget.addWidget(self.xLabel, 1, 0, 1, 1, Qt.AlignHCenter)

        self.way_err = QLabel(self.formWidget)
        self.way_err.setObjectName(u"way_err")
        self.way_err.setMinimumSize(QSize(100, 0))
        self.way_err.setMaximumSize(QSize(250, 16777215))
        self.way_err.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.way_err.setAlignment(Qt.AlignCenter)

        self.waypoints_widget.addWidget(self.way_err, 5, 0, 1, 2, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.waypoints_stack)
        self.speed = QWidget()
        self.speed.setObjectName(u"speed")
        self.speed_widget = QWidget(self.speed)
        self.speed_widget.setObjectName(u"speed_widget")
        self.speed_widget.setGeometry(QRect(10, 10, 360, 211))
        self.verticalLayout = QVBoxLayout(self.speed_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.speed_label = QLabel(self.speed_widget)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setMaximumSize(QSize(16777215, 25))
        self.speed_label.setFont(font5)

        self.verticalLayout.addWidget(self.speed_label)

        self.speed_slider = QSlider(self.speed_widget)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setMaximumSize(QSize(180, 16777215))
        self.speed_slider.setMaximum(255)
        self.speed_slider.setSingleStep(5)
        self.speed_slider.setPageStep(10)
        self.speed_slider.setSliderPosition(0)
        self.speed_slider.setTracking(True)
        self.speed_slider.setOrientation(Qt.Horizontal)
        self.speed_slider.setInvertedAppearance(False)
        self.speed_slider.setTickPosition(QSlider.NoTicks)

        self.verticalLayout.addWidget(self.speed_slider)

        self.input_box = QWidget(self.speed_widget)
        self.input_box.setObjectName(u"input_box")
        self.input_box.setMaximumSize(QSize(180, 16777215))
        self.gridLayout_15 = QGridLayout(self.input_box)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_10 = QLabel(self.input_box)
        self.label_10.setObjectName(u"label_10")
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_10.setFont(font7)

        self.gridLayout_15.addWidget(self.label_10, 1, 1, 1, 1)

        self.NBR_X = QLineEdit(self.input_box)
        self.NBR_X.setObjectName(u"NBR_X")

        self.gridLayout_15.addWidget(self.NBR_X, 2, 1, 1, 1)

        self.NTL_x = QLineEdit(self.input_box)
        self.NTL_x.setObjectName(u"NTL_x")

        self.gridLayout_15.addWidget(self.NTL_x, 2, 0, 1, 1)

        self.label_11 = QLabel(self.input_box)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_15.addWidget(self.label_11, 0, 0, 1, 2)

        self.label_8 = QLabel(self.input_box)
        self.label_8.setObjectName(u"label_8")
        font8 = QFont()
        font8.setPointSize(8)
        self.label_8.setFont(font8)

        self.gridLayout_15.addWidget(self.label_8, 1, 0, 1, 1, Qt.AlignHCenter)

        self.NTL_y = QLineEdit(self.input_box)
        self.NTL_y.setObjectName(u"NTL_y")

        self.gridLayout_15.addWidget(self.NTL_y, 3, 0, 1, 1)

        self.NBR_y = QLineEdit(self.input_box)
        self.NBR_y.setObjectName(u"NBR_y")

        self.gridLayout_15.addWidget(self.NBR_y, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.input_box)

        self.speed_btn = QDialogButtonBox(self.speed_widget)
        self.speed_btn.setObjectName(u"speed_btn")
        self.speed_btn.setMaximumSize(QSize(180, 16777215))
        self.speed_btn.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.verticalLayout.addWidget(self.speed_btn)

        self.stackedWidget.addWidget(self.speed)
        self.crop = QWidget()
        self.crop.setObjectName(u"crop")
        self.crop_widget = QWidget(self.crop)
        self.crop_widget.setObjectName(u"crop_widget")
        self.crop_widget.setGeometry(QRect(0, 10, 201, 171))
        self.gridLayout_12 = QGridLayout(self.crop_widget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.crop_btn = QPushButton(self.crop_widget)
        self.crop_btn.setObjectName(u"crop_btn")
        self.crop_btn.setMinimumSize(QSize(70, 25))
        self.crop_btn.setMaximumSize(QSize(16777215, 16777215))
        self.crop_btn.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_12.addWidget(self.crop_btn, 5, 0, 1, 2, Qt.AlignHCenter)

        self.position = QLabel(self.crop_widget)
        self.position.setObjectName(u"position")
        self.position.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_12.addWidget(self.position, 1, 0, 1, 2)

        self.crop_sy = QLineEdit(self.crop_widget)
        self.crop_sy.setObjectName(u"crop_sy")

        self.gridLayout_12.addWidget(self.crop_sy, 2, 1, 1, 1)

        self.crop_ey = QLineEdit(self.crop_widget)
        self.crop_ey.setObjectName(u"crop_ey")

        self.gridLayout_12.addWidget(self.crop_ey, 4, 1, 1, 1)

        self.crop_ex = QLineEdit(self.crop_widget)
        self.crop_ex.setObjectName(u"crop_ex")

        self.gridLayout_12.addWidget(self.crop_ex, 4, 0, 1, 1)

        self.crop_sx = QLineEdit(self.crop_widget)
        self.crop_sx.setObjectName(u"crop_sx")

        self.gridLayout_12.addWidget(self.crop_sx, 2, 0, 1, 1)

        self.label_9 = QLabel(self.crop_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_12.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_30 = QLabel(self.crop_widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font6)

        self.gridLayout_12.addWidget(self.label_30, 0, 0, 1, 2, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.crop)
        self.Rectangle_page = QWidget()
        self.Rectangle_page.setObjectName(u"Rectangle_page")
        self.Rectangle_page.setMinimumSize(QSize(250, 0))
        font9 = QFont()
        font9.setPointSize(14)
        self.Rectangle_page.setFont(font9)
        self.widget_5 = QWidget(self.Rectangle_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 0, 191, 300))
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.widget_5.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.BottonRight = QWidget(self.widget_5)
        self.BottonRight.setObjectName(u"BottonRight")
        self.BottonRight.setMinimumSize(QSize(0, 2))
        self.BottonRight.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_7 = QGridLayout(self.BottonRight)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, -1, 5, -1)
        self.BRX = QLineEdit(self.BottonRight)
        self.BRX.setObjectName(u"BRX")
        self.BRX.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.BRX, 1, 1, 1, 1)

        self.label = QLabel(self.BottonRight)
        self.label.setObjectName(u"label")

        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1, Qt.AlignHCenter)

        self.BRY = QLineEdit(self.BottonRight)
        self.BRY.setObjectName(u"BRY")
        self.BRY.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.BRY, 2, 1, 1, 1)

        self.label1 = QLabel(self.BottonRight)
        self.label1.setObjectName(u"label1")

        self.gridLayout_7.addWidget(self.label1, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_3 = QLabel(self.BottonRight)
        self.label_3.setObjectName(u"label_3")
        font10 = QFont()
        font10.setPointSize(9)
        self.label_3.setFont(font10)

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 2, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.BottonRight, 2, 0, 1, 1)

        self.apply_rectangle = QPushButton(self.widget_5)
        self.apply_rectangle.setObjectName(u"apply_rectangle")
        self.apply_rectangle.setMinimumSize(QSize(100, 35))
        self.apply_rectangle.setMaximumSize(QSize(300, 35))
        font11 = QFont()
        font11.setBold(False)
        font11.setWeight(50)
        font11.setStrikeOut(False)
        self.apply_rectangle.setFont(font11)
        self.apply_rectangle.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_6.addWidget(self.apply_rectangle, 3, 0, 1, 1)

        self.TopLeft = QWidget(self.widget_5)
        self.TopLeft.setObjectName(u"TopLeft")
        self.TopLeft.setMinimumSize(QSize(0, 1))
        self.TopLeft.setMaximumSize(QSize(200, 16777215))
        self.gridLayout_5 = QGridLayout(self.TopLeft)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 9, 5, 9)
        self.label_4 = QLabel(self.TopLeft)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1, Qt.AlignHCenter)

        self.TLX = QLineEdit(self.TopLeft)
        self.TLX.setObjectName(u"TLX")
        self.TLX.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.TLX, 1, 1, 1, 1, Qt.AlignRight)

        self.label_5 = QLabel(self.TopLeft)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1, Qt.AlignHCenter)

        self.TLY = QLineEdit(self.TopLeft)
        self.TLY.setObjectName(u"TLY")
        self.TLY.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_5.addWidget(self.TLY, 2, 1, 1, 1)

        self.label_2 = QLabel(self.TopLeft)
        self.label_2.setObjectName(u"label_2")
        font12 = QFont()
        font12.setPointSize(9)
        font12.setBold(False)
        font12.setWeight(50)
        self.label_2.setFont(font12)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 2, Qt.AlignHCenter)


        self.gridLayout_6.addWidget(self.TopLeft, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Rectangle_page)
        self.circle_page = QWidget()
        self.circle_page.setObjectName(u"circle_page")
        self.widget_7 = QWidget(self.circle_page)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(0, 0, 201, 211))
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.widget_7.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_8 = QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.x = QWidget(self.widget_7)
        self.x.setObjectName(u"x")
        self.x.setMinimumSize(QSize(180, 50))
        self.x.setMaximumSize(QSize(180, 50))
        self.formLayout = QFormLayout(self.x)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(9, 9, 9, 9)
        self.label_6 = QLabel(self.x)
        self.label_6.setObjectName(u"label_6")
        font13 = QFont()
        font13.setPointSize(11)
        self.label_6.setFont(font13)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.centerX = QLineEdit(self.x)
        self.centerX.setObjectName(u"centerX")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.centerX)


        self.gridLayout_8.addWidget(self.x, 0, 0, 1, 1)

        self.y = QWidget(self.widget_7)
        self.y.setObjectName(u"y")
        self.y.setMinimumSize(QSize(180, 50))
        self.y.setMaximumSize(QSize(180, 50))
        self.formLayout_2 = QFormLayout(self.y)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_7 = QLabel(self.y)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font13)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.centerY = QLineEdit(self.y)
        self.centerY.setObjectName(u"centerY")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.centerY)


        self.gridLayout_8.addWidget(self.y, 1, 0, 1, 1)

        self.apply_circle = QPushButton(self.widget_7)
        self.apply_circle.setObjectName(u"apply_circle")
        self.apply_circle.setMinimumSize(QSize(0, 35))
        self.apply_circle.setMaximumSize(QSize(300, 16777215))
        font14 = QFont()
        self.apply_circle.setFont(font14)
        self.apply_circle.setStyleSheet(u"QPushButton{\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")

        self.gridLayout_8.addWidget(self.apply_circle, 4, 0, 1, 1)

        self.radius = QWidget(self.widget_7)
        self.radius.setObjectName(u"radius")
        self.radius.setMinimumSize(QSize(180, 50))
        self.radius.setMaximumSize(QSize(180, 50))
        self.gridLayout_11 = QGridLayout(self.radius)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.radius_label = QLabel(self.radius)
        self.radius_label.setObjectName(u"radius_label")
        self.radius_label.setFont(font13)
        self.radius_label.setStyleSheet(u"margin-right:15px;")
        self.radius_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.radius_label, 0, 0, 1, 1)

        self.radius_input = QLineEdit(self.radius)
        self.radius_input.setObjectName(u"radius_input")
        self.radius_input.setMinimumSize(QSize(0, 0))

        self.gridLayout_11.addWidget(self.radius_input, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.radius, 2, 0, 1, 1)

        self.radius_validate = QLabel(self.widget_7)
        self.radius_validate.setObjectName(u"radius_validate")
        self.radius_validate.setMaximumSize(QSize(1677215, 20))
        self.radius_validate.setStyleSheet(u"color: rgb(239, 41, 41);\n"
"font: 25 11pt \"Umpush\";")

        self.gridLayout_8.addWidget(self.radius_validate, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.circle_page)
        self.Rotate = QWidget()
        self.Rotate.setObjectName(u"Rotate")
        self.rotate_widget = QWidget(self.Rotate)
        self.rotate_widget.setObjectName(u"rotate_widget")
        self.rotate_widget.setGeometry(QRect(0, 30, 210, 142))
        self.rotate_widget.setMaximumSize(QSize(210, 16777215))
        self.gridLayout_9 = QGridLayout(self.rotate_widget)
        self.gridLayout_9.setSpacing(10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider = QSlider(self.rotate_widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        font15 = QFont()
        font15.setPointSize(30)
        self.horizontalSlider.setFont(font15)
        self.horizontalSlider.setMaximum(360)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_9.addWidget(self.horizontalSlider, 1, 0, 1, 1)

        self.rotate_done = QPushButton(self.rotate_widget)
        self.rotate_done.setObjectName(u"rotate_done")
        self.rotate_done.setMinimumSize(QSize(100, 30))
        self.rotate_done.setMaximumSize(QSize(16777215, 16777215))
        self.rotate_done.setStyleSheet(u"QPushButton{\n"
"    background-color:white;\n"
"	border: 1px solid rgb(128,128,128);\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"   	color: rgb(230, 0, 92);\n"
"	border:1px solid rgb(230, 0, 92);\n"
"}\n"
"\n"
"")

        self.gridLayout_9.addWidget(self.rotate_done, 4, 0, 1, 1, Qt.AlignHCenter)

        self.frame = QFrame(self.rotate_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"border: 0px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.increase_angle = QToolButton(self.frame)
        self.increase_angle.setObjectName(u"increase_angle")
        self.increase_angle.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 3px;\n"
"padding: 5px;")

        self.gridLayout_10.addWidget(self.increase_angle, 1, 2, 1, 1)

        self.decrease_angle = QToolButton(self.frame)
        self.decrease_angle.setObjectName(u"decrease_angle")
        self.decrease_angle.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 3px;\n"
"padding: 5px;")

        self.gridLayout_10.addWidget(self.decrease_angle, 1, 0, 1, 1)

        self.angle = QLabel(self.frame)
        self.angle.setObjectName(u"angle")
        self.angle.setMaximumSize(QSize(60, 25))
        self.angle.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 3px;")
        self.angle.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.angle, 1, 1, 1, 1)

        self.angle_label = QLabel(self.frame)
        self.angle_label.setObjectName(u"angle_label")
        self.angle_label.setMinimumSize(QSize(30, 0))
        self.angle_label.setMaximumSize(QSize(60, 25))

        self.gridLayout_10.addWidget(self.angle_label, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.frame, 3, 0, 1, 1)

        self.label_31 = QLabel(self.rotate_widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 30))
        self.label_31.setFont(font6)

        self.gridLayout_9.addWidget(self.label_31, 0, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.Rotate)

        self.gridLayout_2.addWidget(self.stackedWidget, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 2, 1, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(550, 800))
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setContentsMargins(9, 9, 0, 5)
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1147, 829))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"QScrollArea\n"
"{\n"
"    background-color: #ffffff;\n"
"    border: 0px solid #c0c0c0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 9, 0)
        self.mdiArea = QMdiArea(self.scrollAreaWidgetContents_2)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setMinimumSize(QSize(472, 670))

        self.gridLayout_13.addWidget(self.mdiArea, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.coordinates_label = QLabel(self.widget_2)
        self.coordinates_label.setObjectName(u"coordinates_label")
        self.coordinates_label.setMinimumSize(QSize(0, 30))
        self.coordinates_label.setStyleSheet(u"background-color: #F0F0F0;\n"
"padding-left: 20px;\n"
"padding-bottom:6px;\n"
"font-size: 16px;")

        self.gridLayout_4.addWidget(self.coordinates_label, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 1, 0, 2, 1)

        LayoutDesigner.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(LayoutDesigner)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1383, 29))
        self.menuBar.setMinimumSize(QSize(0, 25))
        self.menuBar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #F0F0F0;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 5px;\n"
"    border: 0px solid #BEBEBE;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"   background-color: \n"
"}\n"
"")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setMinimumSize(QSize(200, 0))
        self.menuEdit.setMaximumSize(QSize(200, 16777215))
        self.menuEdit.setStyleSheet(u"QMenu {\n"
"    background-color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    margin: 0px;\n"
"	padding: 0px;\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgba(114, 159, 207,0.7)\n"
"}\n"
"\n"
"QAction {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QAction:hover {\n"
"    background-color: #E0E0E0;\n"
"}\n"
"")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setStyleSheet(u"QMenu {\n"
"    background-color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    margin: 0px;\n"
"	padding: 0px;\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgba(114, 159, 207,0.7)\n"
"}\n"
"\n"
"QAction {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QAction:hover {\n"
"    background-color: #E0E0E0;\n"
"}\n"
"")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setMinimumSize(QSize(200, 0))
        self.menuFile.setAutoFillBackground(False)
        self.menuFile.setStyleSheet(u"QMenu {\n"
"    background-color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    margin: 0px;\n"
"	padding: 0px;\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgba(114, 159, 207,0.7);\n"
"}\n"
"\n"
"QAction {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QAction:hover {\n"
"    background-color: #E0E0E0;\n"
"}\n"
"")
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuFile.setToolTipsVisible(True)
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuTools.setStyleSheet(u"QMenu {\n"
"    background-color: #FFFFFF;\n"
"    font-size: 16px;\n"
"    margin: 0px;\n"
"	padding: 0px;\n"
"    border: 1px solid #BEBEBE;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgba(114, 159, 207,0.7)\n"
"}\n"
"\n"
"QAction {\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"}\n"
"\n"
"QAction:hover {\n"
"    background-color: #E0E0E0;\n"
"}\n"
"")
        self.menuTools.setToolTipsVisible(False)
        LayoutDesigner.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionMark)
        self.menuEdit.addAction(self.actionRotate)
        self.menuEdit.addAction(self.actionCrop)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_out)
        self.menuView.addAction(self.actionclean_map)
        self.menuView.addAction(self.actionExport_clean_map)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.ExportCostMap)
        self.menuFile.addAction(self.actionLog_out)
        self.menuTools.addAction(self.action2D_Pose)
        self.menuTools.addAction(self.actionSelect)

        self.retranslateUi(LayoutDesigner)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(LayoutDesigner)
    # setupUi

    def retranslateUi(self, LayoutDesigner):
        LayoutDesigner.setWindowTitle(QCoreApplication.translate("LayoutDesigner", u"Layout Designer", None))
        self.actionNew.setText(QCoreApplication.translate("LayoutDesigner", u"New Layout", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("LayoutDesigner", u"Edit Layout", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.ExportCostMap.setText(QCoreApplication.translate("LayoutDesigner", u"Export Cost Map", None))
#if QT_CONFIG(shortcut)
        self.ExportCostMap.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("LayoutDesigner", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecent.setText(QCoreApplication.translate("LayoutDesigner", u"Recent", None))
        self.actionUndo.setText(QCoreApplication.translate("LayoutDesigner", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("LayoutDesigner", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionMarks.setText(QCoreApplication.translate("LayoutDesigner", u"Marks", None))
#if QT_CONFIG(shortcut)
        self.actionMarks.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionMark.setText(QCoreApplication.translate("LayoutDesigner", u"Mark", None))
#if QT_CONFIG(shortcut)
        self.actionMark.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit.setText(QCoreApplication.translate("LayoutDesigner", u"Edit Map", None))
#if QT_CONFIG(shortcut)
        self.actionEdit.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionRotate.setText(QCoreApplication.translate("LayoutDesigner", u"Rotate", None))
#if QT_CONFIG(shortcut)
        self.actionRotate.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionCrop.setText(QCoreApplication.translate("LayoutDesigner", u"Crop", None))
        self.actionLog_out.setText(QCoreApplication.translate("LayoutDesigner", u"Log out", None))
        self.actionZoom_In.setText(QCoreApplication.translate("LayoutDesigner", u"zoom in", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_In.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Shift++", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom_out.setText(QCoreApplication.translate("LayoutDesigner", u"zoom out", None))
#if QT_CONFIG(shortcut)
        self.actionZoom_out.setShortcut(QCoreApplication.translate("LayoutDesigner", u"Shift+-", None))
#endif // QT_CONFIG(shortcut)
        self.actionclean_map.setText(QCoreApplication.translate("LayoutDesigner", u"clean map", None))
        self.actionStation.setText(QCoreApplication.translate("LayoutDesigner", u"Station", None))
        self.actionChange_speed.setText(QCoreApplication.translate("LayoutDesigner", u"Change speed ", None))
        self.actionChange_Speed.setText(QCoreApplication.translate("LayoutDesigner", u"Change Speed", None))
        self.actionStation_Window.setText(QCoreApplication.translate("LayoutDesigner", u"Station", None))
        self.actionChanged_Speed.setText(QCoreApplication.translate("LayoutDesigner", u"Change Speed", None))
        self.action2D_Pose.setText(QCoreApplication.translate("LayoutDesigner", u"2D Pose ", None))
        self.actionSelect.setText(QCoreApplication.translate("LayoutDesigner", u"Select", None))
        self.actionExport_clean_map.setText(QCoreApplication.translate("LayoutDesigner", u"Export clean map", None))
        self.actionWaypoints.setText(QCoreApplication.translate("LayoutDesigner", u"Waypoints", None))
        self.heading.setText(QCoreApplication.translate("LayoutDesigner", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-style:italic;\">Warehouse Layout Map Design </span></p></body></html>", None))
        self.type_zone.setItemText(0, QCoreApplication.translate("LayoutDesigner", u"Select Type of Zone", None))
        self.type_zone.setItemText(1, QCoreApplication.translate("LayoutDesigner", u"Aisle", None))
        self.type_zone.setItemText(2, QCoreApplication.translate("LayoutDesigner", u"Buffer Zone", None))
        self.type_zone.setItemText(3, QCoreApplication.translate("LayoutDesigner", u"Restricted", None))
        self.type_zone.setItemText(4, QCoreApplication.translate("LayoutDesigner", u"Walkway", None))
        self.type_zone.setItemText(5, QCoreApplication.translate("LayoutDesigner", u"Parking Location", None))
        self.type_zone.setItemText(6, QCoreApplication.translate("LayoutDesigner", u"Charging Location", None))
        self.type_zone.setItemText(7, QCoreApplication.translate("LayoutDesigner", u"Station with ID", None))
        self.type_zone.setItemText(8, QCoreApplication.translate("LayoutDesigner", u"Dock Station", None))
        self.type_zone.setItemText(9, QCoreApplication.translate("LayoutDesigner", u"Waypoints", None))
        self.type_zone.setItemText(10, QCoreApplication.translate("LayoutDesigner", u"Insert Manual Coordinates", None))
        self.type_zone.setItemText(11, QCoreApplication.translate("LayoutDesigner", u"Update Location", None))
        self.type_zone.setItemText(12, QCoreApplication.translate("LayoutDesigner", u"Reflector location", None))
        self.type_zone.setItemText(13, QCoreApplication.translate("LayoutDesigner", u"Text Notation", None))

        self.shape_zone.setItemText(0, QCoreApplication.translate("LayoutDesigner", u"Select the shape of zone", None))
        self.shape_zone.setItemText(1, QCoreApplication.translate("LayoutDesigner", u"Rectangle Shape", None))
        self.shape_zone.setItemText(2, QCoreApplication.translate("LayoutDesigner", u"Circle Shape", None))

        self.offset.setText("")
        self.xLabel_3.setText(QCoreApplication.translate("LayoutDesigner", u"X:", None))
        self.label_13.setText(QCoreApplication.translate("LayoutDesigner", u"Y:", None))
        self.coordinates_enter.setText(QCoreApplication.translate("LayoutDesigner", u"Enter Coordinates:", None))
        self.calculate.setText(QCoreApplication.translate("LayoutDesigner", u"Calculate ", None))
        self.coord_status.setText("")
        self.update_box.setTitle(QCoreApplication.translate("LayoutDesigner", u"Updated Status:", None))
        self.x_posLabel.setText(QCoreApplication.translate("LayoutDesigner", u"x:", None))
        self.y_posLabel.setText(QCoreApplication.translate("LayoutDesigner", u"y:", None))
        self.z_poseLabel.setText(QCoreApplication.translate("LayoutDesigner", u"pose_z", None))
        self.w_poseLabel_2.setText(QCoreApplication.translate("LayoutDesigner", u"pose_w", None))
        self.Location_Label.setText(QCoreApplication.translate("LayoutDesigner", u"Location:", None))
        self.label_20.setText(QCoreApplication.translate("LayoutDesigner", u"Level:", None))
        self.label_21.setText(QCoreApplication.translate("LayoutDesigner", u"Height:", None))
        self.label_19.setText(QCoreApplication.translate("LayoutDesigner", u"Enter the Location name: ", None))
        self.run.setText(QCoreApplication.translate("LayoutDesigner", u"Run", None))
        self.stop.setText(QCoreApplication.translate("LayoutDesigner", u"Stop", None))
        self.current_box.setTitle(QCoreApplication.translate("LayoutDesigner", u"Current Status:", None))
        self.currentLocationLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Location:", None))
        self.current_xLabel.setText(QCoreApplication.translate("LayoutDesigner", u"x:", None))
        self.current_yLabel.setText(QCoreApplication.translate("LayoutDesigner", u"y:", None))
        self.currentzposeLabel.setText(QCoreApplication.translate("LayoutDesigner", u"pose_z:", None))
        self.currentwposeLabel.setText(QCoreApplication.translate("LayoutDesigner", u"pose_w:", None))
        self.currentLevelLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Level:", None))
        self.currentHeightLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Height:", None))
        self.update.setText(QCoreApplication.translate("LayoutDesigner", u"Update", None))
        self.label_22.setText(QCoreApplication.translate("LayoutDesigner", u"x:", None))
        self.label_24.setText(QCoreApplication.translate("LayoutDesigner", u"name:", None))
        self.label_25.setText(QCoreApplication.translate("LayoutDesigner", u"Reflector Location", None))
        self.label_23.setText(QCoreApplication.translate("LayoutDesigner", u"y:", None))
        self.reflector.setText(QCoreApplication.translate("LayoutDesigner", u"Add Reflector", None))
        self.label_27.setText(QCoreApplication.translate("LayoutDesigner", u"Text Notattion", None))
        self.label_26.setText(QCoreApplication.translate("LayoutDesigner", u"Enter text:", None))
        self.text_notation.setText(QCoreApplication.translate("LayoutDesigner", u"Add Text", None))
        self.label_15.setText(QCoreApplication.translate("LayoutDesigner", u"Pose W:", None))
#if QT_CONFIG(tooltip)
        self.station_link.setToolTip(QCoreApplication.translate("LayoutDesigner", u"Near rack station name", None))
#endif // QT_CONFIG(tooltip)
        self.xLabel_2.setText(QCoreApplication.translate("LayoutDesigner", u"x:", None))
        self.yLabel_2.setText(QCoreApplication.translate("LayoutDesigner", u"y:", None))
        self.dock.setText(QCoreApplication.translate("LayoutDesigner", u"Add Dock Location", None))
        self.associatedStationLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Near By Station:", None))
        self.poseLabel_2.setText(QCoreApplication.translate("LayoutDesigner", u"Pose Z:", None))
        self.label_14.setText(QCoreApplication.translate("LayoutDesigner", u"Dock Name:", None))
        self.label_29.setText(QCoreApplication.translate("LayoutDesigner", u"Dock Location", None))
        self.stationNameLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Station ID:", None))
        self.add_station_toggle.setTitle(QCoreApplication.translate("LayoutDesigner", u"                 Add Station:", None))
        self.label_16.setText(QCoreApplication.translate("LayoutDesigner", u"Level:", None))
        self.add_station.setText(QCoreApplication.translate("LayoutDesigner", u"Add Station ", None))
        self.label_17.setText(QCoreApplication.translate("LayoutDesigner", u"Height:", None))
        self.addHeight.setItemText(0, QCoreApplication.translate("LayoutDesigner", u"Select Height", None))
        self.addHeight.setItemText(1, QCoreApplication.translate("LayoutDesigner", u"320 mm", None))
        self.addHeight.setItemText(2, QCoreApplication.translate("LayoutDesigner", u"1620 mm", None))
        self.addHeight.setItemText(3, QCoreApplication.translate("LayoutDesigner", u"2920 mm", None))

        self.xLabel_4.setText(QCoreApplication.translate("LayoutDesigner", u"x:", None))
        self.levelLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Level:", None))
        self.Height.setItemText(0, QCoreApplication.translate("LayoutDesigner", u"Select Height", None))
        self.Height.setItemText(1, QCoreApplication.translate("LayoutDesigner", u"0", None))
        self.Height.setItemText(2, QCoreApplication.translate("LayoutDesigner", u"320 mm", None))
        self.Height.setItemText(3, QCoreApplication.translate("LayoutDesigner", u"1620 mm ", None))
        self.Height.setItemText(4, QCoreApplication.translate("LayoutDesigner", u"2920 mm", None))

        self.poseLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Pose Z:", None))
        self.heightLabel.setText(QCoreApplication.translate("LayoutDesigner", u"Height:", None))
        self.station.setText(QCoreApplication.translate("LayoutDesigner", u"Select Station", None))
        self.yLabel_3.setText(QCoreApplication.translate("LayoutDesigner", u"y:", None))
        self.label_18.setText(QCoreApplication.translate("LayoutDesigner", u"Pose W:", None))
        self.stack_btn.setText(QCoreApplication.translate("LayoutDesigner", u"...", None))
#if QT_CONFIG(tooltip)
        self.stack_station.setToolTip(QCoreApplication.translate("LayoutDesigner", u"stack another station", None))
#endif // QT_CONFIG(tooltip)
        self.stack_station.setText(QCoreApplication.translate("LayoutDesigner", u"Stack another Station", None))
        self.label_28.setText(QCoreApplication.translate("LayoutDesigner", u" Station with ID", None))
        self.label_12.setText(QCoreApplication.translate("LayoutDesigner", u"Waypoints", None))
        self.pose_zlabel.setText(QCoreApplication.translate("LayoutDesigner", u"pose_z:", None))
        self.yLabel.setText(QCoreApplication.translate("LayoutDesigner", u"y:", None))
        self.station2Label.setText(QCoreApplication.translate("LayoutDesigner", u"2nd station:", None))
        self.station1Label.setText(QCoreApplication.translate("LayoutDesigner", u"1st station:", None))
        self.pose_wLabel.setText(QCoreApplication.translate("LayoutDesigner", u"pose_w:", None))
        self.waypoints.setText(QCoreApplication.translate("LayoutDesigner", u"Waypoint", None))
        self.xLabel.setText(QCoreApplication.translate("LayoutDesigner", u"x:", None))
        self.way_err.setText("")
        self.speed_label.setText(QCoreApplication.translate("LayoutDesigner", u"Change Speed:", None))
        self.label_10.setText(QCoreApplication.translate("LayoutDesigner", u"Bottom-right", None))
        self.label_11.setText(QCoreApplication.translate("LayoutDesigner", u"New Region:", None))
        self.label_8.setText(QCoreApplication.translate("LayoutDesigner", u"Top-Left", None))
        self.crop_btn.setText(QCoreApplication.translate("LayoutDesigner", u"Crop", None))
        self.position.setText(QCoreApplication.translate("LayoutDesigner", u"Start Postion:", None))
        self.label_9.setText(QCoreApplication.translate("LayoutDesigner", u"End Postion:", None))
        self.label_30.setText(QCoreApplication.translate("LayoutDesigner", u"Crop:", None))
        self.label.setText(QCoreApplication.translate("LayoutDesigner", u"X:", None))
        self.label1.setText(QCoreApplication.translate("LayoutDesigner", u"Y:", None))
        self.label_3.setText(QCoreApplication.translate("LayoutDesigner", u"Bottom-Right Coordinates:", None))
        self.apply_rectangle.setText(QCoreApplication.translate("LayoutDesigner", u"Apply Rectangle", None))
        self.label_4.setText(QCoreApplication.translate("LayoutDesigner", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("LayoutDesigner", u"Y:", None))
        self.label_2.setText(QCoreApplication.translate("LayoutDesigner", u"Top-Left Coordinates", None))
        self.label_6.setText(QCoreApplication.translate("LayoutDesigner", u"Center X:", None))
        self.label_7.setText(QCoreApplication.translate("LayoutDesigner", u"Center Y:", None))
        self.apply_circle.setText(QCoreApplication.translate("LayoutDesigner", u"Apply Circle", None))
        self.radius_label.setText(QCoreApplication.translate("LayoutDesigner", u"Radius:", None))
        self.radius_validate.setText("")
        self.rotate_done.setText(QCoreApplication.translate("LayoutDesigner", u"Rotate", None))
        self.increase_angle.setText(QCoreApplication.translate("LayoutDesigner", u">", None))
        self.decrease_angle.setText(QCoreApplication.translate("LayoutDesigner", u"<", None))
        self.angle.setText("")
        self.angle_label.setText(QCoreApplication.translate("LayoutDesigner", u"Angle:", None))
        self.label_31.setText(QCoreApplication.translate("LayoutDesigner", u"Rotate:", None))
        self.coordinates_label.setText("")
        self.menuEdit.setTitle(QCoreApplication.translate("LayoutDesigner", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("LayoutDesigner", u"View", None))
        self.menuFile.setTitle(QCoreApplication.translate("LayoutDesigner", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("LayoutDesigner", u"Tools", None))
    # retranslateUi

