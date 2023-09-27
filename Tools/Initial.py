from PySide2.QtGui import *
from Tools.features import increase_angle, decrease_angle, rotating_slider, save_rotated_map, crop_map
from Tools.function import get_user_coordinates

def init(call):
    call.connection, call.sql = None, None
    call.filename, call.map, call.keepout_map, call.speed_map = None, None, None, None
    call.image, call.pixmap = None, None
    call.yaml_data = None
    call.resolution, call.scale, call.width, call.height = 0, 0, 0, 0
    call.start_x, call.start_y, call.end_x, call.end_y = 0, 0, 0, 0
    call.undo_colored_map = []
    call.undo_keepout_map = []
    call.undo_speed_map = []
    call.ui.stackedWidget.setCurrentWidget(call.ui.front)
    call.ui.mdiArea.setBackground(QBrush(Qt.white))
    # waypoints
    call.waypoint_counter = 1
    call.ui.way_err.hide()
    call.ui.station1.textChanged.connect(lambda: call.ui.way_err.hide())
    call.ui.station2.textChanged.connect(lambda: call.ui.way_err.hide())
    # rotation
    call.ui.increase_angle.clicked.connect(lambda: increase_angle(call))
    call.ui.decrease_angle.clicked.connect(lambda: decrease_angle(call))
    call.ui.horizontalSlider.valueChanged.connect(lambda: rotating_slider(call))
    call.ui.rotate_done.clicked.connect(lambda: save_rotated_map(call))
    #crop
    call.ui.crop_btn.clicked.connect(lambda: crop_map(call))
    #get the ros coordinates
    call.ui.calculate.clicked.connect(lambda: get_user_coordinates(call))

