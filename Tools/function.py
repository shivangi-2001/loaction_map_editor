import cv2, os, yaml
import numpy as np
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

def serach_yaml(name):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == name + ".yaml":
                yaml_file = os.path.join(root, file)
                print("Found YAML file:", yaml_file)
                with open(yaml_file, "r") as f:
                    yaml_data = yaml.safe_load(f)
                    resolution = yaml_data["resolution"]
                    return yaml_data, resolution

# aspect ratio of the Qlabel and map image
def _resize(image,height=None,width=None):
        (h,w) = image.shape[:2]
        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
            # print(dim,w,w*r)
        else:
            r = width / float(w)
            dim = (width, int(h * r))
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized, r


def qimage_to_cv2(self, qimage):
    width = qimage.width()
    height = qimage.height()
    image_data = qimage.constBits()
    img = np.frombuffer(image_data, dtype=np.uint8).reshape((height, width, 4))
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    return img

def meters_to_ros2(height,yaml_data, x, y):
        try:
            if yaml_data:
                origin = yaml_data['origin']
                resolution = yaml_data['resolution']
                if origin[0] == origin[1]:
                    X = float(x) - (-origin[0])
                    Y = -(float(y) - (-origin[1]))
                else:
                    origin_y = origin[1] + height * resolution
                    X = float(x) - (-origin[0])
                    Y = -float(y) + (origin_y)
                return X, Y
        except Exception as e:
            pass

def ros2_to_meters(height, yaml_data, ros_x, ros_y):
    origin = yaml_data['origin']
    resolution = yaml_data['resolution']
    ros_x = float(ros_x)
    ros_y = float(ros_y)
    if origin[0] == origin[1]:
        x_m = ros_x + (-origin[0])
        y_m = -ros_y + (-origin[1])
    else:
        origin_y = origin[1] + height * resolution
        x_m = ros_x + (-origin[0])
        y_m = -(ros_y-(origin_y))
    return x_m, y_m


def choose_zoneType_color(call,zone):
        if zone == 'Aisle':
            color = (0, 255, 0)
            keepout_color = None
            speed_color = int(255 * (1 - 0 / 100))
            return color, keepout_color, speed_color
        elif zone == 'Buffer Zone':
            color = (0, 255, 255)
            keepout_color = None
            speed_color = int(255 * (1 - 80 / 100))
            return color, keepout_color, speed_color
        elif zone == 'Restricted':
            color = (0, 0, 255)
            keepout_color = int(255 * (1 - 100 / 100))
            speed_color = None
            return color, keepout_color, speed_color
        elif zone == 'Walkway':
            color = (255, 192, 203)
            keepout_color = None
            speed_color = int(255 * (1 - 80 / 100))
            return color, keepout_color, speed_color
        elif zone == 'Parking Location':
            color = (212,170,255)
            keepout_color = None
            speed_color = int(255 * (1 - 20 / 100))
            return  color, keepout_color, speed_color
        elif zone == 'Charging Location':
            color = (255, 170, 86)
            keepout_color = None
            speed_color = int(255 * (1 - 60 / 100))
            return color, keepout_color, speed_color
        # elif zone.isdigit():
        #     return None, None, int(zone)
        # elif zone.isalnum():
        #     letter_part = re.findall(r'[a-zA-Z]+', zone)[0]
        #     number_part = int(re.findall(r'\d+', zone)[0])
        #     if letter_part == 'Aisle' or letter_part == 'BufferZone' or letter_part == 'Restricted' or letter_part == 'Walkway' or letter_part == 'ParkingLocation' or letter_part == 'ChargingLocation':
        #         color, keep, speed = choose_zoneType_color(call, letter_part)
        #         return color ,keep, number_part
        #     else:
        #         QMessageBox.warning(call, "Error", "Invalid zone type. Please select a valid zone type.")
        #         color, keepout_color, speed_color = None, None, None
        #         return color, keepout_color, speed_color
        else:
           QMessageBox.warning(call,"Error", "Please select a zone before continuing.")
           color ,keepout_color , speed_color = None, None, None
           return color, keepout_color, speed_color

def Arrow(call):
        call.draw_widget.rectangle = False
        call.draw_widget.setCursor(Qt.ArrowCursor)

def Rectangle(call):
        call.draw_widget.rectangle = True
        call.draw_widget.setCursor(Qt.CrossCursor)

def get_user_coordinates(self):
    if self.height and self.yaml_data:
        x_m, y_m = ros2_to_meters(self.height, self.yaml_data, self.ui.X_user_input.text(),
                                  self.ui.Y_user_input.text())
        x_p, y_p = int(x_m / self.resolution), int(y_m / self.resolution)
        self.ui.station_x.setText(str(round(float(x_m), 2)))
        self.ui.station_y.setText(str(round(float(y_m), 2)))
        self.ui.dock_x.setText(str(round(float(x_m), 2)))
        self.ui.dock_y.setText(str(round(float(y_m), 2)))
        self.ui.coord_status.setText("Done!")
    else:
        QMessageBox.information(self, "info", "Load Map for getting the coordinates")







































    # def marking(map, resolution, x, y, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
#         x,y = float(x), float(y)
#         x_p, y_p = int(x / resolution), int(y / resolution)  # convert the coordinates into pixel
#         center = (x_p, y_p)
#         radius = 10
#         map = cv2.circle(map, center, radius, (0,0,0), -1)
#         pixmap = QPixmap.fromImage(QImage(map, map.shape[1], map.shape[0], QImage.Format_BGR888))
#
#         undo_colored_map.append(map.copy())
#         undo_keepout_map.append(map.copy())
#         undo_speed_map.append(map.copy())
#
#         steps += 1
#         print("Marking:", steps)
#         return map,pixmap, undo_colored_map, undo_keepout_map, undo_speed_map, steps
#
#
def qimage_to_cv2(qimage):
    width = qimage.width()
    height = qimage.height()
    image_data = qimage.constBits()
    img = np.frombuffer(image_data, dtype=np.uint8).reshape((height, width, 4))
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    return img
# #
#
#





