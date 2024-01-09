from PyQt5 import QtCore, QtGui, QtWidgets
from MainMenu import Ui_Form
import mysql.connector


class Ui_LogInMenu(object):
    def setupUi(self, LogInMenu, database):
        LogInMenu.setObjectName("LogInMenu")
        LogInMenu.resize(1200, 675)
        self.BackgroundLabel = QtWidgets.QLabel(LogInMenu)
        self.BackgroundLabel.setGeometry(QtCore.QRect(0, 0, 1200, 675))
        self.BackgroundLabel.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/santiago bernabeu.jpg"))
        self.BackgroundLabel.setScaledContents(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogInMenu.setWindowIcon(icon)
        LogInMenu.setStyleSheet("")
        self.db = database
        self.FrameTitle = QtWidgets.QFrame(LogInMenu)
        self.FrameTitle.setGeometry(QtCore.QRect(-1, -1, 500, 1500))
        self.FrameTitle.setStyleSheet("")
        self.FrameTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameTitle.setObjectName("FrameTitle")
        self.LogoMadrid = QtWidgets.QLabel(self.FrameTitle)
        self.LogoMadrid.setGeometry(QtCore.QRect(200, 180, 220, 210))
        self.LogoMadrid.setText("")
        self.LogoMadrid.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"))
        self.LogoMadrid.setScaledContents(True)
        self.LogoMadrid.setObjectName("LogoMadrid")
        self.TitleHotel = QtWidgets.QLabel(self.FrameTitle)
        self.TitleHotel.setGeometry(QtCore.QRect(120, 400, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Copperplate")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(90)
        self.TitleHotel.setFont(font)
        self.TitleHotel.setStyleSheet("color: white;")
        self.TitleHotel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleHotel.setObjectName("TitleHotel")

        self.LabelBox = QtWidgets.QFrame(LogInMenu)
        self.LabelBox.setGeometry(QtCore.QRect(750, 120, 400, 400))
        self.LabelBox.setStyleSheet("background-color: white; border-radius: 15px;")
        
        self.SignIn = QtWidgets.QLabel(LogInMenu)
        self.SignIn.setParent(self.LabelBox)
        self.SignIn.setGeometry(QtCore.QRect(100, 30, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(26)
        self.SignIn.setFont(font)
        self.SignIn.setStyleSheet("color: rgb(0, 150, 136);")
        self.SignIn.setAlignment(QtCore.Qt.AlignCenter)
        self.SignIn.setObjectName("SignIn")
        self.username = QtWidgets.QLineEdit(LogInMenu)
        self.username.setParent(self.LabelBox)
        self.username.setGeometry(QtCore.QRect(30, 140, 330, 30))
        self.username.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: black;\n"
"border-bottom: 2px solid rgb(0, 150, 136);")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(LogInMenu)
        self.password.setParent(self.LabelBox)
        self.password.setGeometry(QtCore.QRect(30, 210, 330, 30))
        self.password.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: black;\n"
"border-bottom: 2px solid rgb(0, 150, 136);")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.EHUsername = QtWidgets.QLabel(LogInMenu)
        self.EHUsername.setParent(self.LabelBox)
        self.EHUsername.setGeometry(QtCore.QRect(30, 170, 160, 17))
        self.EHUsername.setObjectName("EHUsername")
        self.EHPassword = QtWidgets.QLabel(LogInMenu)
        self.EHPassword.setParent(self.LabelBox)
        self.EHPassword.setGeometry(QtCore.QRect(30, 240, 160, 17))
        self.EHPassword.setObjectName("EHPassword")
        self.ButtonLogIn = QtWidgets.QPushButton(LogInMenu)
        self.ButtonLogIn.setParent(self.LabelBox)
        self.ButtonLogIn.setGeometry(QtCore.QRect(90, 325, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(19)
        self.ButtonLogIn.setFont(font)
        self.ButtonLogIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonLogIn.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:grey;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:15px;\n"
"border-color:rgb(0,150,136);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/akun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonLogIn.setIcon(icon1)
        self.ButtonLogIn.setIconSize(QtCore.QSize(33, 33))
        self.ButtonLogIn.setObjectName("ButtonLogIn")
        self.ButtonLogIn.clicked.connect(self.LogInClicked)

        self.retranslateUi(LogInMenu)
        QtCore.QMetaObject.connectSlotsByName(LogInMenu)

    def retranslateUi(self, LogInMenu):
        _translate = QtCore.QCoreApplication.translate
        LogInMenu.setWindowTitle(_translate("LogInMenu", "Home Hotel Madridistas"))
        self.TitleHotel.setText(_translate("LogInMenu", "HOTEL MADRIDISTAS"))
        self.SignIn.setText(_translate("LogInMenu", "SIGN IN"))
        self.username.setPlaceholderText(_translate("LogInMenu", "Username"))
        self.password.setPlaceholderText(_translate("LogInMenu", "Password"))
        self.ButtonLogIn.setText(_translate("LogInMenu", "LOG IN"))

    def openMainWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        LogInMenu.hide()
        self.window.show()

    def LogInClicked(self):
        _translate = QtCore.QCoreApplication.translate

        cursor = self.db.cursor()
        infoAdmin = ("SELECT `username`, `password` FROM Admin")
        cursor.execute(infoAdmin)

        infoUser = False
        infoPass = False

        for (username, password) in cursor:
            if self.username.text() == username:
                infoUser = True
            if self.password.text() == password:
                infoPass = True
        
        if infoPass == True and infoUser == True:
            self.openMainWindow()
        elif infoUser == False:
            self.EHUsername.setText(_translate("LogInMenu", "<font color=\"red\">Username anda salah</font>"))
            self.EHPassword.setText(_translate("LogInMenu", "<font color=\"red\">Password anda salah</font>"))
        else :
            self.EHUsername.setText(_translate("LogInMenu", "<font color=\"red\"> </font>"))
            self.EHPassword.setText(_translate("LogInMenu", "<2font color=\"red\">Password anda salah</font>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogInMenu = QtWidgets.QWidget()
    DataBase = mysql.connector.connect(user="root", database="Hotelst")
    ui = Ui_LogInMenu()
    ui.setupUi(LogInMenu, DataBase)
    LogInMenu.show()
    sys.exit(app.exec_())
