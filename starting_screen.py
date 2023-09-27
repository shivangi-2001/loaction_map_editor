import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from layout_ui_py.starting import Ui_Dialog
from layoutdesigner import LayoutDesigner
from login_application import MainWindow


class Login(MainWindow):
    def __init__(self):
        super(Login, self).__init__()


class starting(QDialog):
    def __init__(self):
        super(starting,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ld = None
        self.ui.label_4.setPixmap('image/futuristics.jpg')
        self.ui.progressBar.setRange(0,110)
        self.center()

        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

    def progress(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 2)
        if self.ui.progressBar.value() > 100:
            self.close()
            self.ld = LayoutDesigner()
            self.ld.show()
            self.timer.setSingleShot(True)

    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        login = Login()
        login.show()
        if login.user_authenticated():  # updated the if statement to reference the login variable
            print("you are already authenticated !")
            print("Welcome to the Futuristics Bots - Layout Designer")
            login.close()
            window = starting()
            window.show()
        else:
            print("You are not Logged in!\nYou need to authenticated first\nLogin application run")
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass