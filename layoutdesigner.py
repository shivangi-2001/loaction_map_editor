import sys, os, cv2
import math

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from layout_ui_py.layout_design import Ui_LayoutDesigner
from Tools.database import Database, Layout_Database
from Tools.Menu import menu
from Tools.Initial import init
from Tools.function import center, serach_yaml, _resize, meters_to_ros2, choose_zoneType_color
from Tools.DrawWithMouse import DrawWidget
from Tools.apply_shape import rectangle, circle, station, dock, waypoint, reflector, text_notation
from Tools.redraw_shape import redraw_rectangle, redraw_circle, redraw_station, redraw_docks, redraw_waypoints, redraw_reflector, redraw_textnotation
from Tools.offset import offsetWindow

class LayoutDesigner(QMainWindow):
    def __init__(self):
        super(LayoutDesigner, self).__init__()
        self.ui = Ui_LayoutDesigner()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(QPixmap('image/fb-icon.png')))
        init(self)
        menu(self)
        center(self)

        self.steps = 0
        self.sub = QMdiSubWindow()
        self.draw_widget = DrawWidget()
        self.draw_widget.send_all_coordinates.connect(self.coordinates_label)
        self.ui.shape_zone.currentIndexChanged.connect(self.shapeOfZone)
        self.ui.type_zone.currentIndexChanged.connect(self.typeOfZone)
        self.ui.apply_rectangle.clicked.connect(self.apply_rectangle)
        self.ui.apply_circle.clicked.connect(self.apply_circle)
        self.ui.station.clicked.connect(self.apply_station)
        self.ui.dock.clicked.connect(self.apply_dock)
        self.ui.waypoints.clicked.connect(self.apply_waypoint)
        self.ui.reflector.clicked.connect(self.apply_reflector)
        self.ui.text_notation.clicked.connect(self.apply_text)

        self.draw_widget.mouseDoubleClickEvent = self.select_shape_doubleclick

        self.offset_window = offsetWindow()
        self.offset_window.ui.buttonBox.accepted.connect(self.offset_coordinates)


    def shapeOfZone(self):
        if self.ui.shape_zone.currentText() == 'Rectangle Shape':
            self.ui.stackedWidget.setCurrentWidget(self.ui.Rectangle_page)
        elif self.ui.shape_zone.currentText() == 'Circle Shape':
            self.ui.stackedWidget.setCurrentWidget(self.ui.circle_page)
        else: self.ui.stackedWidget.setCurrentWidget(self.ui.front)

    def typeOfZone(self):
        if self.ui.type_zone.currentText() == 'Station with ID':
            self.ui.stackedWidget.setCurrentWidget(self.ui.station_location)
        elif self.ui.type_zone.currentText() == 'Dock Station':
            self.ui.stackedWidget.setCurrentWidget(self.ui.dock_location)
        elif self.ui.type_zone.currentText() == 'Waypoints':
            self.ui.stackedWidget.setCurrentWidget(self.ui.waypoints_stack)
        elif self.ui.type_zone.currentText() == 'Reflector location':
            self.ui.stackedWidget.setCurrentWidget(self.ui.Reflector)
        elif self.ui.type_zone.currentText() == 'Text Notation':
            self.ui.stackedWidget.setCurrentWidget(self.ui.Text_Notation)
        elif self.ui.type_zone.currentText() == 'Insert Manual Coordinates':
            self.ui.stackedWidget.setCurrentWidget(self.ui.Manual)
        elif self.ui.type_zone.currentText() == 'Update Location':
            self.ui.stackedWidget.setCurrentWidget(self.ui.upadatelocation)

    def translateGroundTruthtoopencv(self, map_height, x, y):
        print(x, (map_height - float(y)))
        return x, (map_height - float(y))

    def New_Layout(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "New File", directory=os.getcwd(),
                                                       filter="Image files (*.pgm *.png *.jpg)",
                                                       options=QFileDialog.DontUseNativeDialog)
        if self.filename:
            self.connection, self.sql = Database()
            self.map = cv2.imread(self.filename)  # cv2 read colored image
            self.keepout_map = cv2.imread(self.filename)  # cv2 read keepout image
            self.speed_map = cv2.imread(self.filename)  # cv2 speed image
            name_of_map = os.path.splitext(os.path.basename(self.filename))[0]
            print("Working Map: ", name_of_map)
            self.yaml_data, self.resolution = serach_yaml(name_of_map)
            if self.map is not None:
                self.height, self.width = self.map.shape[:2]
                self.scale = self.ui.mdiArea.minimumHeight() / self.height
                self.undo_colored_map.append(self.map.copy())
                self.undo_keepout_map.append(self.keepout_map.copy())
                self.undo_speed_map.append(self.speed_map.copy())
                self.set_map(self.map)
                self.offset_window.show()

    def set_map(self, map):
        resized_image = _resize(map, height=self.ui.mdiArea.minimumHeight() )[0]
        self.image = QImage(resized_image, resized_image.shape[1], resized_image.shape[0], resized_image.strides[0], QImage.Format_BGR888)
        self.pixmap = QPixmap.fromImage(self.image)
        self.sub.setFixedSize(self.pixmap.size())
        self.sub.setWindowFlags(Qt.FramelessWindowHint)
        self.draw_widget.setFixedSize(self.pixmap.size())
        self.draw_widget.setPixmap(self.pixmap)
        if not self.sub.widget():
            self.sub.setWidget(self.draw_widget)
        if not self.ui.mdiArea.subWindowList():
            self.ui.mdiArea.setFixedSize(self.pixmap.size())
            self.ui.mdiArea.addSubWindow(self.sub)
        self.sub.show()

    def offset_coordinates(self):
        self.offset_x, self.offset_y = float(self.offset_window.ui.offset_x.text()), float(
            self.offset_window.ui.offset_y.text())
        self.ui.offset.setText("offset_x: " + str(self.offset_x) + ", offset_y: " + str(self.offset_y))

    def coordinates_label(self,start_x,start_y,end_x,end_y):
        self.start_x = round((start_x / self.scale * self.resolution),2)
        self.start_y = round((start_y / self.scale * self.resolution),2)
        self.end_x = round((end_x / self.scale * self.resolution),2)
        self.end_y = round((end_y / self.scale * self.resolution),2)

        self.real_start_x, self.real_start_y = meters_to_ros2(self.height, self.yaml_data, self.start_x, self.start_y)
        self.real_end_x, self.real_end_y = meters_to_ros2(self.height, self.yaml_data, self.end_x, self.end_y)

        delta_x, delta_y = self.end_x - self.start_x, self.end_y - self.start_y
        distance = round(math.sqrt(delta_x ** 2 + delta_y ** 2), 2)

        self.ui.coordinates_label.setText(" X_p:  " + str(int(self.start_x / self.resolution)) + "  Y_p:  " + str(
            int(self.start_y / self.resolution)) + " | " + "X:  " + str(self.end_x) + "  Y:  " + str(
            self.end_y) + "  |   " + str(distance) + "  meter")

        self.pose_orientation()

        self.ui.TLX.setText(str(self.start_x))
        self.ui.TLY.setText(str(self.start_y))
        self.ui.BRX.setText(str(self.end_x))
        self.ui.BRY.setText(str(self.end_y))
        self.ui.centerX.setText(str(self.end_x))
        self.ui.centerY.setText(str(self.end_y))
        self.ui.station_x.setText(str(float(self.start_x)))
        self.ui.station_y.setText(str(float(self.start_y)))
        self.ui.dock_x.setText(str(float(self.start_x)))
        self.ui.dock_y.setText(str(float(self.start_y)))
        self.ui.wx.setText(str(float(self.start_x)))
        self.ui.wy.setText(str(float(self.start_y)))
        self.ui.r_x.setText(str(float(self.start_x)))
        self.ui.r_y.setText(str(float(self.start_y)))

        self.ui.crop_sx.setText(str(float(self.start_x)))
        self.ui.crop_sy.setText(str(float(self.start_y)))
        self.ui.crop_ex.setText(str(float(self.end_x)))
        self.ui.crop_ey.setText(str(float(self.end_y)))

        self.offset_window.ui.offset_x.setText(str(float(self.start_x)))
        self.offset_window.ui.offset_y.setText(str(float(self.start_y)))

    def pose_orientation(self):
        if self.real_start_x and self.real_start_y and self.real_end_x and self.real_end_y:
            mouse_movement = QVector3D(self.real_end_x - self.real_start_x, self.real_end_y - self.real_start_y, 0.0)
            angle = math.degrees(math.acos(QVector3D.dotProduct(mouse_movement.normalized(), QVector3D(1.0, 0.0, 0.0))))
            axis = QVector3D.crossProduct(QVector3D(1.0, 0.0, 0.0), mouse_movement.normalized())
            rotation = QQuaternion.fromAxisAndAngle(axis, angle)
            self.ui.PoseZ.setText(str(round(rotation.z(), 4)))
            self.ui.PoseW.setText(str(round(rotation.scalar(), 4)))
            self.ui.dock_pose_z.setText(str(round(rotation.z(), 4)))
            self.ui.dock_pose_w.setText(str(round(rotation.scalar(), 4)))
            self.ui.wz_pose.setText(str(round(rotation.z(), 4)))
            self.ui.ww_pose.setText(str(round(rotation.scalar(), 4)))

    def apply_rectangle(self):
        print(self.map.shape)
        new_tlx, new_tly = self.translateGroundTruthtoopencv((self.map.shape[1]*self.resolution) ,self.ui.TLX.text(), self.ui.TLY.text())
        new_brx, new_bry = self.translateGroundTruthtoopencv((self.map.shape[1]*self.resolution), self.ui.BRX.text(), self.ui.BRY.text())
        self.map, self.keepout_map, self.speed_map, self.pixmap, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.connection, self.sql, self.steps = \
            rectangle(self.map, self.keepout_map, self.speed_map, self.offset_x, self.offset_y, new_tlx, str(new_tly), new_brx, str(new_bry), self.resolution, self, self.ui.type_zone.currentText(),
                      self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.connection, self.sql, self.steps)
        if self.pixmap is not None:
            self.set_map(self.map)

    def apply_circle(self):
        self.map, self.keepout_map, self.speed_map, self.pixmap, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql = \
            circle(self.map, self.keepout_map, self.speed_map, self.ui.radius_validate, self.ui.centerX.text(), self.ui.centerY.text(), self.ui.radius_input.text(), self.resolution,
                   self, self.ui.type_zone.currentText(), self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.ui.shape_zone.currentText(), self.connection, self.sql)
        self.ui.radius_input.textChanged.connect(lambda : self.ui.radius_validate.hide())
        if self.pixmap is not None:
            self.set_map(self.map)

    def apply_station(self):
        ros_x, ros_y = meters_to_ros2(self.height, self.yaml_data, self.ui.station_x.text(), self.ui.station_y.text())
        self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps ,self.connection, self.sql= \
            station(self.map, ros_x, ros_y, self.ui.station_x.text(), self.ui.station_y.text(), self.resolution, self.ui.station_name.text(),
                    self.ui.Level.text(), self.ui.Height.currentText(), self.ui.PoseZ.text(), self.ui.PoseW.text(), self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql)
        self.set_map(self.map)

    def apply_dock(self):
        ros_x, ros_y = meters_to_ros2(self.height, self.yaml_data, self.ui.dock_x.text(), self.ui.dock_y.text())
        self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql = \
            dock(self.map, ros_x, ros_y, self.ui.dock_x.text(), self.ui.dock_y.text(), self.ui.dock_name.text(), self.resolution, self.ui.station_link.text(),
                 self.ui.dock_pose_z.text(), self.ui.dock_pose_w.text(), self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql)
        self.set_map(self.map)

    def apply_waypoint(self):
        ros_x, ros_y = meters_to_ros2(self.height, self.yaml_data, self.ui.wx.text(), self.ui.wy.text())
        self.map, self.waypoint_counter, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql = \
            waypoint(self.map, ros_x, ros_y, self.ui.wx.text(), self.ui.wy.text(), self.waypoint_counter,
                     self.ui.station1.text(), self.ui.station2.text(), float(self.ui.wz_pose.text()), float(self.ui.ww_pose.text()),
                     self, self.resolution, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql)
        if self.map is not None:
            self.set_map(self.map)

    def apply_reflector(self):
        ros_x, ros_y = meters_to_ros2(self.height, self.yaml_data, self.ui.r_x.text(), self.ui.r_y.text())
        self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql = \
            reflector(self.map, ros_x, ros_y, self.ui.r_x.text(), self.ui.r_y.text(), self.ui.r_name.text(),
                 self.resolution, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql)
        self.set_map(self.map)

    def apply_text(self):
        if self.start_x and self.start_y is not None:
            self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql = \
                text_notation(self.map, self.start_x, self.start_y, self.resolution, self.ui.text.text(), self.undo_colored_map,
                              self.undo_keepout_map, self.undo_speed_map, self.steps, self.connection, self.sql)
            self.set_map(self.map)
        else:
            QMessageBox.warning(self, "Error", "Select location where add Text", QMessageBox.Ok)

    def undo(self):
        if len(self.undo_colored_map) > 0 and len(self.undo_keepout_map) > 0 and len(self.undo_speed_map) > 0:
            try:
                self.undo_colored_map.pop()
                self.undo_keepout_map.pop()
                self.undo_speed_map.pop()
                self.map = self.undo_colored_map[-1]
                self.set_map(self.map)
                self.keepout_map = self.undo_keepout_map[-1]
                self.speed_map = self.undo_speed_map[-1]
                self.connection.executescript("DELETE FROM rectangle_shape WHERE steps = '%d'" % self.steps)
                self.connection.executescript("DELETE FROM circle_shape WHERE steps = '%d'" % self.steps)
                self.connection.executescript("DELETE FROM station WHERE steps = '%d'" % self.steps)
                self.connection.executescript("DELETE FROM docks WHERE steps = '%d'" % self.steps)
                self.connection.executescript("DELETE FROM waypoints WHERE steps = '%d'" % self.steps)
                self.connection.executescript("DELETE FROM reflector WHERE steps = '%d'" % self.steps)
                self.connection.executescript("DELETE FROM text WHERE steps = '%d'" % self.steps)
                self.steps -= 1
                self.sql.commit()
            except Exception as e:
                print(f'An error occurred during undo: {e}')

    def Edit_layout(self):
        layout_database, _ = QFileDialog.getOpenFileName(self, "Select Layout Database", directory=os.getcwd(),
                                                         filter="Database Files (*.db)",
                                                         options=QFileDialog.DontUseNativeDialog)
        self.layout_image, _ = QFileDialog.getOpenFileName(self, "Select Layout Image", directory=os.getcwd(),
                                                      filter="Image Files (*.pgm *.png *.jpg)",
                                                      options=QFileDialog.DontUseNativeDialog)
        if layout_database and self.layout_image:
            self.connection, self.sql = Layout_Database(layout_database)
            self.map = cv2.imread(self.layout_image)  # cv2 read colored image
            self.keepout_map = cv2.imread(self.layout_image)  # cv2 read keepout image
            self.speed_map = cv2.imread(self.layout_image)  # cv2 speed image
            name_of_map = os.path.splitext(os.path.basename(self.layout_image))[0]
            print("Working Map: ", name_of_map)
            self.yaml_data, self.resolution = serach_yaml(name_of_map)
            if self.map is not None:
                self.height, self.width = self.map.shape[:2]
                self.scale = self.ui.mdiArea.minimumHeight() / self.height
                self.undo_colored_map.append(self.map.copy())
                self.undo_keepout_map.append(self.keepout_map.copy())
                self.undo_speed_map.append(self.speed_map.copy())
                self.set_map(self.map)
                self.redraw_shape()

    def redraw_shape(self):
        self.redrawRectangle()
        self.redrawCircle()
        self.redraw_station()
        self.redraw_docks()
        self.redraw_waypoints()
        self.redraw_reflector()
        self.redraw_textnotation()

    def redrawRectangle(self):
        rectangle = self.connection.execute("SELECT * FROM rectangle_shape").fetchall()
        for rect in rectangle:
            self.map, self.keepout_map, self.speed_map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
            redraw_rectangle(self.map, self.keepout_map, self.speed_map, self.offset_x, self.offset_y, self.resolution,
                             rect[7], rect[8], rect[9], rect[10], rect[1], self,
                             self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps)
        self.set_map(self.map)


    def redrawCircle(self):
        circle = self.connection.execute("SELECT * FROM circle_shape").fetchall()
        for cir in circle:
            self.map, self.keepout_map, self.speed_map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
                redraw_circle(self.map, self.keepout_map, self.speed_map, cir[4], cir[5], cir[3], cir[1], self,
                              self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps)
        self.set_map(self.map)

    def redraw_station(self):
        station = self.connection.execute("SELECT * FROM station").fetchall()
        for st in station:
            self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
                redraw_station(self.map, self.height, self.yaml_data, self.resolution,
                               st[7], st[8], self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map,
                               self.steps)
        self.set_map(self.map)

    def redraw_docks(self):
        docks = self.connection.execute("SELECT * FROM docks").fetchall()
        for doc in docks:
            self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
                redraw_docks(self.map, self.height, self.yaml_data, self.resolution,
                             doc[8], doc[9], self.undo_colored_map, self.undo_keepout_map,
                             self.undo_speed_map, self.steps)
        self.set_map(self.map)

    def redraw_waypoints(self):
        waypoints = self.connection.execute("SELECT * FROM waypoints").fetchall()
        for way in waypoints:
            self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
                redraw_waypoints(self.map, self.height, self.yaml_data, self.resolution,
                             way[7], way[8], self.undo_colored_map, self.undo_keepout_map,
                             self.undo_speed_map, self.steps)
        self.set_map(self.map)

    def redraw_reflector(self):
        reflector = self.connection.execute("SELECT * FROM reflector").fetchall()
        for ref in reflector:
            self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
                redraw_reflector(self.map, self.height, self.yaml_data, self.resolution,
                             ref[7], ref[8], self.undo_colored_map, self.undo_keepout_map,
                             self.undo_speed_map, self.steps)
        self.set_map(self.map)

    def redraw_textnotation(self):
        text = self.connection.execute("SELECT * FROM text").fetchall()
        for tx in text:
            self.map, self.undo_colored_map, self.undo_keepout_map, self.undo_speed_map, self.steps = \
                redraw_textnotation(self.map, tx[2], tx[3], tx[4], self.undo_colored_map, self.undo_keepout_map,
                                 self.undo_speed_map, self.steps)
        self.set_map(self.map)

    def select_shape_doubleclick(self, event: QMouseEvent):
        fetch_x = float(round((event.pos().x() / self.scale * self.resolution), 2))
        fetch_y = float(round((event.pos().y() / self.scale * self.resolution), 2))

        rectangle_query = self.connection.execute("SELECT * FROM rectangle_shape").fetchall()
        circle_query = self.connection.execute("SELECT * FROM circle_shape").fetchall()
        station_query = self.connection.execute("SELECT * FROM station").fetchall()
        dock_query = self.connection.execute("SELECT * FROM docks").fetchall()
        waypoint_query = self.connection.execute("SELECT * FROM waypoints").fetchall()
        reflector_query = self.connection.execute("SELECT * FROM reflector").fetchall()

        for rect in rectangle_query:
            con1 = (rect[7] < fetch_x < rect[9] and rect[8] < fetch_y < rect[10])
            con2 = (rect[7] > fetch_x > rect[9] and rect[8] > fetch_y > rect[10])
            con3 = (rect[7] > fetch_x > rect[9] and rect[8] < fetch_y < rect[10])
            con4 = (rect[7] < fetch_x < rect[9] and rect[8] > fetch_y > rect[10])
            if con1 or con2 or con3 or con4:
                self.process_rectangle(event, rect)

        for cir in circle_query:
            if ((fetch_x - cir[6]) ** 2) + ((fetch_y - cir[7]) ** 2) <= cir[8] ** 2:
                self.process_circle(event, cir)


        stat_radius = 15 * self.resolution
        for stat in station_query:
            if ((fetch_x - stat[5]) ** 2) + ((fetch_y - stat[6]) ** 2) <=  stat_radius ** 2:
               self.process_station(event, stat)

        docks_radius = 15 * self.resolution
        for dock in dock_query:
            if ((fetch_x - dock[6]) ** 2) + ((fetch_y - dock[7]) ** 2) <= docks_radius ** 2:
                self.process_dock(event, dock)

        waypoint_radius = 15 * self.resolution
        for way in waypoint_query:
            if ((fetch_x - way[5]) ** 2) + ((fetch_y - way[6]) ** 2) <= waypoint_radius ** 2:
                self.process_waypoints(event, way)

        fetch_x_p, fetch_y_p = int(fetch_x/self.resolution), int(fetch_y/self.resolution)
        for ref in reflector_query:
            if (fetch_x_p - 20 < ref[3] < fetch_x_p + 20) and (fetch_y_p - 25 < ref[4] < fetch_y_p + 25):
                print(ref)

    def process_rectangle(self, event, rect):
        start = (int(rect[7] / self.resolution), int(rect[8] / self.resolution))
        end = (int(rect[9] / self.resolution), int(rect[10] / self.resolution))
        self.map = cv2.rectangle(self.map, start, end, (0, 0, 0), 2)
        self.set_map(self.map)
        action = self.menu_box_selected_shape(event, self.delete_selected_rectangle, rect, None)
        if not action:
            map = self.remove_border_rectangle(rect)
            self.set_map(map)

    def process_circle(self, event, cir):
        center = (int(cir[6] / self.resolution), int(cir[7] / self.resolution))
        radius = int(cir[8] / self.resolution)
        self.map = cv2.circle(self.map, center, radius, (0, 0, 0), 1)
        self.set_map(self.map)
        action = self.menu_box_selected_shape(event, self.delete_selected_circle, cir, None)
        if not action:
            color = choose_zoneType_color(self, cir[1])
            self.map = cv2.circle(self.map, center, radius, (255, 255, 255), 1)
            overlay = self.map.copy()
            draw_map = cv2.circle(overlay, center, radius, color[0], 1)
            self.map = cv2.addWeighted(draw_map, 0.4, self.map, 1 - 0.4, 0)
            self.set_map(self.map)

    def process_station(self, event, stat):
        stations_in_same_location = []
        self.map = cv2.circle(self.map, (stat[3], stat[4]), 3, (0, 0, 0), 1)
        self.set_map(self.map)
        stations_in_same_location.append(stat)
        if stations_in_same_location:
            action = self.menu_box_selected_shape(event, self.delete_selected_station, stat, stations_in_same_location)
            if not action:
                for stat in stations_in_same_location:
                    self.map = cv2.circle(self.map, (stat[3], stat[4]), 3, (255, 0, 0), 1)
                self.set_map(self.map)

    def process_dock(self, event, dock):
        dock_in_smae_loaction = []
        self.map = cv2.circle(self.map, (dock[4], dock[5]), 3, (0, 0, 0), 1)
        self.set_map(self.map)
        dock_in_smae_loaction.append(dock)
        if dock_in_smae_loaction:
            action = self.menu_box_selected_shape(event, self.delete_selected_dock, dock, dock_in_smae_loaction)
            if not action:
                for dock in dock_in_smae_loaction:
                    self.map = cv2.circle(self.map, (dock[4], dock[5]), 3, (255, 0, 0), 1)
                self.set_map(self.map)

    def process_waypoints(self, event, way):
        way_in_smae_loaction = []
        self.map = cv2.circle(self.map, (way[3], way[4]), 3, (0, 0, 0), 1)
        self.set_map(self.map)
        way_in_smae_loaction.append(way)
        if way_in_smae_loaction:
            action = self.menu_box_selected_shape(event, self.delete_selected_waypoint, way, way_in_smae_loaction)
            if not action:
                for WAY in way_in_smae_loaction:
                    self.map = cv2.circle(self.map, (WAY[3], WAY[4]), 3, (255, 0, 0), 1)
                self.set_map(self.map)

    def menu_box_selected_shape(self, event, func, shape, stations_in_same_location):
        if stations_in_same_location is not None:
            context_menu = QMenu(self)
            context_menu.setStyleSheet(
                " QMenu::item:selected { background-color: rgba(114, 159, 207, 0.7); color: rgb(0, 0, 0);}")
            delete = QAction("Delete", self)
            delete.triggered.connect(lambda: func(shape))
            info = QAction("Info", self)
            info.setMenu(self.information_menu(stations_in_same_location))
            context_menu.addAction(delete)
            context_menu.addAction(info)
            action = context_menu.exec_(event.globalPos())
            return action
        else:
            context_menu = QMenu(self)
            context_menu.setStyleSheet(" QMenu::item:selected { background-color: rgba(114, 159, 207, 0.7); color: rgb(0, 0, 0);}")
            delete = QAction("Delete", self)
            delete.triggered.connect(lambda: func(shape))
            context_menu.addAction(delete)
            change_speed = QAction("change speed", self)
            change_speed.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.speed))
            change_speed.triggered.connect(lambda: self.changing_speed(shape))
            context_menu.addAction(change_speed)
            action = context_menu.exec_(event.globalPos())
            return action

    def information_menu(self, station_list):
        info_submenu = QMenu("Station Info")
        info_submenu.setStyleSheet(
            " QMenu::item:selected { background-color: rgba(114, 159, 207, 0.7); color: rgb(0, 0, 0);}")
        for stat in station_list:
            info_submenu.addAction(str(stat[2]) + "-  level: " + str(stat[9]) + "  height: " + str(stat[10]))
        return info_submenu

    def delete_selected_rectangle(self, rect):
        query = "DELETE FROM rectangle_shape WHERE TL_x_meter = ? and TL_y_meter = ? and BR_x_meter = ? and BR_y_meter = ?"
        self.connection.execute(query, (rect[7], rect[8], rect[9], rect[10]))
        self.sql.commit()
        self.map = cv2.imread(self.layout_image)
        self.keepout_map = cv2.imread(self.layout_image)
        self.speed_map = cv2.imread(self.layout_image)
        self.set_map(self.map)
        self.redraw_shape()

    def remove_border_rectangle(self, shape):
        tx, ty, bx, by = shape[7], shape[8], shape[9], shape[10]
        tx_p, ty_p, bx_p, by_p = int(tx / self.resolution), int(ty / self.resolution), int(bx / self.resolution), int(by / self.resolution)
        start = (tx_p, ty_p)
        end = (bx_p, by_p)
        color = choose_zoneType_color(self, shape[1])
        self.map = cv2.rectangle(self.map, start, end, (255, 255, 255), 1)
        overlay = self.map.copy()
        draw_map = cv2.rectangle(overlay, start, end, color[0], 1)
        self.map = cv2.addWeighted(draw_map, 0.4, self.map, 1 - 0.4, 0)
        return self.map

    def delete_selected_circle(self, cir):
        query = "DELETE FROM circle_shape WHERE cx_meter = ? and cy_meter = ? and radius_meter = ?"
        self.connection.execute(query, (cir[6], cir[7], cir[8]))
        self.sql.commit()
        self.map = cv2.imread(self.layout_image)
        self.keepout_map = cv2.imread(self.layout_image)
        self.speed_map = cv2.imread(self.layout_image)
        self.set_map(self.map)
        self.redraw_shape()

    def delete_selected_station(self, stat):
        query = "DELETE FROM station WHERE x_meter = ? and y_meter= ?"
        self.connection.execute(query, (stat[5], stat[6]))
        self.sql.commit()
        self.map = cv2.imread(self.layout_image)
        self.keepout_map = cv2.imread(self.layout_image)
        self.speed_map = cv2.imread(self.layout_image)
        self.set_map(self.map)
        self.redraw_shape()

    def delete_selected_dock(self, dock):
        query = "DELETE FROM docks WHERE dx_meter = ? and dy_meter= ?"
        self.connection.execute(query, (dock[6], dock[7]))
        self.sql.commit()
        self.map = cv2.imread(self.layout_image)
        self.keepout_map = cv2.imread(self.layout_image)
        self.speed_map = cv2.imread(self.layout_image)
        self.set_map(self.map)
        self.redraw_shape()

    def delete_selected_waypoint(self, way):
        query = "DELETE FROM waypoints WHERE x_m = ? and y_m = ?"
        self.connection.execute(query, (way[5], way[6]))
        self.sql.commit()
        self.map = cv2.imread(self.layout_image)
        self.keepout_map = cv2.imread(self.layout_image)
        self.speed_map = cv2.imread(self.layout_image)
        self.set_map(self.map)
        self.redraw_shape()




if __name__ == "__main__":
    try:
        app = QApplication()
        window = LayoutDesigner()
        window.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
