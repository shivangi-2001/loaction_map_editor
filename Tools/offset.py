from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from layout_ui_py.offset import Ui_Dialog
import sys

class offsetWindow(QDialog):
    def __init__(self):
        super(offsetWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ui.stackedWidget.setCurrentWidget(self.ui.offsets)
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        center_point = screen_geometry.center()
        window_position = center_point - self.rect().center()
        self.move(window_position)


    def closeEvent(self, event):
        settings = QSettings('MyCompany', 'MyApp')
        settings.setValue('window_geometry', self.geometry())
        super().closeEvent(event)






if __name__ == "__main__":
    try:
        app = QApplication()
        window = offsetWindow()
        window.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass