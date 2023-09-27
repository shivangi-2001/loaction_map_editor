from PySide2.QtGui import *
from Tools.function import Arrow, Rectangle
from Tools.features import clean_map, Export_clean_map, zoom
from Tools.save import save_as

def menu(call):
    call.ui.actionNew.setIcon(QIcon(QPixmap('icon/new.png')))
    call.ui.actionOpen.setIcon(QIcon(QPixmap('icon/open.png')))
    call.ui.ExportCostMap.setIcon(QIcon(QPixmap('icon/saveas.png')))
    call.ui.actionLog_out.setIcon(QIcon(QPixmap('icon/logout.png')))

    call.ui.actionUndo.setIcon(QIcon(QPixmap('icon/undo.png')))
    call.ui.actionMark.setIcon(QIcon(QPixmap('icon/mark.png')))
    call.ui.actionRotate.setIcon(QIcon(QPixmap('icon/rotate.png')))
    call.ui.actionCrop.setIcon((QIcon(QPixmap('icon/crop.png'))))

    call.ui.actionZoom_In.setIcon(QIcon(QPixmap('icon/zoomin.png')))
    call.ui.actionZoom_out.setIcon(QIcon(QPixmap('icon/zoomout.png')))
    call.ui.actionSelect.setIcon(QIcon(QPixmap('icon/arrow.png')))
    call.ui.action2D_Pose.setIcon(QIcon(QPixmap('icon/rect.png')))

    call.ui.actionNew.triggered.connect(call.New_Layout)
    call.ui.actionOpen.triggered.connect(call.Edit_layout)
    call.ui.ExportCostMap.triggered.connect(lambda: save_as(call))
    # call.ui.actionLog_out.triggered.connect(call.logout)
    #
    call.ui.actionUndo.triggered.connect(call.undo)
    # call.ui.actionMark.triggered.connect(call.marking)
    call.ui.actionRotate.triggered.connect(lambda: call.ui.stackedWidget.setCurrentWidget(call.ui.Rotate))
    call.ui.actionCrop.triggered.connect(lambda: call.ui.stackedWidget.setCurrentWidget(call.ui.crop))
    #
    call.ui.actionZoom_In.triggered.connect(lambda: zoom(call, 1.1))
    call.ui.actionZoom_out.triggered.connect(lambda: zoom(call, 0.9))
    call.ui.actionclean_map.triggered.connect(lambda: clean_map(call))
    call.ui.actionExport_clean_map.triggered.connect(lambda: Export_clean_map(call))
    #
    call.ui.action2D_Pose.triggered.connect(lambda: Arrow(call))
    call.ui.actionSelect.triggered.connect(lambda: Rectangle(call))

