import sys
import os
import sqlite3
import hashlib
from sqlite3 import Error
from PySide2.QtWidgets import *
from login_ui_py.login import Login_Page
# from ui_py.landing_page import Landing_MainWindow


try:
    sql = sqlite3.connect("Users.db")
    connection = sql.cursor()
    print("Login Database connection is started ")
except Error:
    print("Error: ", Error)




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Login_Page()
        self.ui.setupUi(self)
        self.center()
        self.ui.icon.setPixmap("image/fb.png")
        self.ui.log_btn.clicked.connect(self.authenticate)

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def authenticate(self):
        self.username = self.ui.user_input.text()
        self.password = self.ui.pass_input.text()
        pass_token  = hashlib.sha256(self.password.encode()).hexdigest()

        self.ui.user_input.textChanged.connect(lambda: self.ui.error.hide())

        connection.execute("SELECT * FROM accounts WHERE tokens='%s'"%(pass_token))
        row = connection.fetchone()
        if row is None:
            self.ui.error.setText("Invalid Username and Password")
        else:
            is_username_valid = self.check_Username(row,self.username)
            if row[-1] == pass_token and is_username_valid:
                connection.executescript(""" UPDATE session SET session_token = '%s' """ % (row[-1]))
                print("succesfully log in\nWelcome to futruistic bots")
                # it will help you return on previous function - it's callback
                self.restart_program()
                return True
            else:
                # error msg display above the login application
                self.ui.error.setText("Invalid Username and Password")


    # this is used for checking valid username that you enter or not otherwise you will not able to login
    def check_Username(self,row,username):
        if username == row[1]:
            return True
        else:
            return False


    # this function is used to check the user is active or not mean it check previously user logout or not
    def user_authenticated(self):
        connection.execute("SELECT * FROM session")
        row = connection.fetchone()
        if row[0] != None:
            return True

    
    
    # def landing(self):
    #     self.ui = Landing_MainWindow()
    #     self.ui.setupUi(self)


    # logout function for the apply on logout button - it will help us to logout and
    # terminate the user session
    def user_logout(self):
        connection.executescript("""
            UPDATE session SET session_token = NULL""")
        sql.commit()
        sys.exit()




    # centering the widget 
    def center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QApplication.primaryScreen().geometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

if __name__ == "__main__":
    try:
        app = QApplication()
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass




