import os, cv2, shutil
from PySide2.QtWidgets import *


def save_as(self):
    saveas, _ = QFileDialog.getSaveFileName(self, "Export Cost Map (.pgm)", '',
                                            filter="Save as: JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)",
                                            options=QFileDialog.DontUseNativeDialog)
    if saveas:
        root, ext = os.path.splitext(saveas)
        self.colored_map = root + '_colored.png'
        self.costmap_keepout = root + '_keepout.pgm'
        self.costmap_speed = root + '_speed.pgm'
        self.database_name = root + '.db'

        gray_keepout = cv2.cvtColor(self.keepout_map, cv2.COLOR_BGR2GRAY)
        gray_speed = cv2.cvtColor(self.speed_map, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(self.colored_map, self.map)
        cv2.imwrite(self.costmap_keepout, gray_keepout)
        cv2.imwrite(self.costmap_speed, gray_speed)
        shutil.copy("Database.db", self.database_name)

        print('colored Map saved as:', self.costmap_keepout)
        print('Filtered Map saved as:', self.costmap_keepout)
        print('Speed Filtered Map saved as:', self.costmap_speed)
        print("Database saved:", self.database_name)

        self.costmap_keepout = os.path.split(self.costmap_keepout)[1]
        self.costmap_speed = os.path.split(self.costmap_speed)[1]

        save_yaml(self.yaml_data, root + '_keepout', self.costmap_keepout)
        save_speed_yaml(self.yaml_data, root + '_speed', self.costmap_speed)

def save_yaml(yaml_data, root, map_name):
    yaml_data['image'] = map_name
    new_yaml_file = root + '.yaml'
    origin = [0, 0, 0]
    with open(new_yaml_file, "w") as f:
        lines = []
        lines.append("image: " + yaml_data['image'])
        lines.append("resolution: " + str(yaml_data['resolution']))
        lines.append("origin: " + str(origin))
        lines.append("negate: " + str(yaml_data['negate']))
        lines.append("occupied_thresh: " + str(yaml_data['occupied_thresh']))
        lines.append("free_thresh: " + str(yaml_data['free_thresh']))
        content = "\n".join(lines)
        f.write(content)
        print("YAML file saved at", new_yaml_file)

def save_speed_yaml(yaml_data, root, map_name):
    yaml_data['image'] = map_name
    new_yaml_file = root + '.yaml'
    origin = [0, 0, 0]
    with open(new_yaml_file, "w") as f:
        lines = []
        lines.append("image: " + yaml_data['image'])
        lines.append("resolution: " + str(yaml_data['resolution']))
        lines.append("origin: " + str(origin))
        lines.append("negate: " + str(yaml_data['negate']))
        lines.append("occupied_thresh: " + str(1.0))
        lines.append("free_thresh: " + str(0.0))
        content = "\n".join(lines)
        f.write(content)
        print("YAML file saved at", new_yaml_file)
