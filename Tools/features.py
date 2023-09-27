import cv2, os, datetime, random, string
from PySide2.QtGui import *
from PySide2.QtCore import *
from Tools.save import save_yaml, save_speed_yaml
from Tools.function import qimage_to_cv2

# clean the map area
def clean_map(call):
    try:
        tlx, tly, brx, bry = int(call.start_x / call.resolution), int(call.start_y / call.resolution), int(
            call.end_x / call.resolution), int(call.end_y / call.resolution)
        call.map = cv2.rectangle(call.map, (tlx, tly), (brx, bry), (255, 255, 255), -1)
        call.undo_colored_map.append(call.map.copy())
        call.undo_keepout_map.append(call.map.copy())
        call.undo_speed_map.append(call.map.copy())
        call.steps += 1
        call.set_map(call.map)
    except Exception as e:
        pass

def Export_clean_map(call):
    try:
        directory, filename = os.path.split(call.filename)
        output_path = os.path.join(directory, filename)
        clean_map_gray = cv2.cvtColor(call.map, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(output_path, clean_map_gray)
        print("Export Clean Map", "Clean map exported successfully.")
    except Exception as e:
        pass

# zoom in and  out
def zoom(call, factor):
    call.scale *= factor
    resized_image = cv2.resize(call.map, None, fx=call.scale, fy=call.scale, interpolation=cv2.INTER_CUBIC)
    call.image = QImage(resized_image, resized_image.shape[1], resized_image.shape[0], resized_image.strides[0],
                        QImage.Format_BGR888)
    call.pixmap = QPixmap.fromImage(call.image)
    call.ui.mdiArea.setFixedSize(call.pixmap.size())
    call.sub.setFixedSize(call.pixmap.size())
    call.draw_widget.setFixedSize(call.pixmap.size())
    call.draw_widget.setPixmap(call.pixmap)


# rotate the map and export it
def increase_angle(call):
    angle = call.ui.horizontalSlider.value() + 1
    call.ui.horizontalSlider.setValue(angle)
    call.ui.angle.setText(" " + str(angle))

def decrease_angle(call):
    angle = call.ui.horizontalSlider.value() - 1
    call.ui.horizontalSlider.setValue(angle)
    call.ui.angle.setText(" " + str(angle))

def rotating_slider(call):
    angle = - call.ui.horizontalSlider.value()
    call.ui.angle.setText(" " + str(-angle))
    rows, cols = call.map.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated = cv2.warpAffine(call.map, M, (cols, rows), flags=cv2.INTER_CUBIC)
    height, width, channel = rotated.shape
    bytesPerLine = channel * width
    rotate_image = QImage(rotated.data, width, height, bytesPerLine, QImage.Format_BGR888)
    pixmap = QPixmap(rotate_image)
    call.draw_widget.setPixmap(pixmap)
def save_rotated_map(self):
    pixmap = self.draw_widget.pixmap()
    q_image = pixmap.toImage()
    height, width = pixmap.height(), pixmap.width()
    rotated = q_image.copy(QRect(0, 0, width, height))
    rotated_img = qimage_to_cv2(rotated)
    current_datetime = datetime.datetime.now().strftime("%d%m_%H:%M")
    random_name = f"rotated_{current_datetime}"

    root, ext = os.path.splitext(self.filename)
    dir_path, last_part = os.path.split(root)
    yaml_path = os.path.join(dir_path, random_name)
    new_file_path = os.path.join(dir_path, f"{random_name}.pgm")

    gray = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(new_file_path, gray)
    print("Rotated image saved at ", new_file_path)

    new_yaml_filename = f"{random_name}.pgm"
    save_yaml(self.yaml_data, yaml_path, new_yaml_filename)


# crop the map and export it
def crop_map(self):
    ex_p, ey_p = int(float(self.ui.crop_ex.text())/self.resolution), int(float(self.ui.crop_ey.text())/self.resolution)
    sx_p, sy_p = int(float(self.ui.crop_sx.text())/self.resolution), int(float(self.ui.crop_sy.text())/self.resolution)
    cropped = self.map[sy_p:ey_p, sx_p:ex_p]

    current_datetime = datetime.datetime.now().strftime("%d%m_%H:%M")
    random_name = f"crop_{current_datetime}"
    root, ext = os.path.splitext(self.filename)
    dir_path, last_part = os.path.split(root)
    yaml_path = os.path.join(dir_path, random_name)
    new_file_path = os.path.join(dir_path, f"{random_name}.pgm")

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(new_file_path, gray)
    print("cropped image saved at ", new_file_path)

    new_yaml_filename = f"{random_name}.pgm"
    save_yaml(self.yaml_data, yaml_path, new_yaml_filename)