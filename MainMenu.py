# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MenuBooking import Ui_Booking
from MenuCheckIn import Ui_ChekIn
from Cetak import Ui_CetakNota
from MenuEdit import Ui_Edit

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 499)
        Form.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.FrameAkun = QtWidgets.QFrame(Form)
        self.FrameAkun.setGeometry(QtCore.QRect(0, -1, 271, 501))
        self.FrameAkun.setStyleSheet("background-color: rgb(0, 150, 136);")
        self.FrameAkun.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameAkun.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameAkun.setObjectName("FrameAkun")
        self.LogoAkun = QtWidgets.QLabel(self.FrameAkun)
        self.LogoAkun.setGeometry(QtCore.QRect(50, 130, 161, 161))
        self.LogoAkun.setText("")
        self.LogoAkun.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/uji.png"))
        self.LogoAkun.setScaledContents(True)
        self.LogoAkun.setObjectName("LogoAkun")
        self.TitleHotel = QtWidgets.QLabel(self.FrameAkun)
        self.TitleHotel.setGeometry(QtCore.QRect(0, 50, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Z003 [UKWN]")
        font.setPointSize(20)
        self.TitleHotel.setFont(font)
        self.TitleHotel.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.TitleHotel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleHotel.setObjectName("TitleHotel")
        self.TitleService = QtWidgets.QLabel(self.FrameAkun)
        self.TitleService.setGeometry(QtCore.QRect(0, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        self.TitleService.setFont(font)
        self.TitleService.setStyleSheet("color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.TitleService.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleService.setObjectName("TitleService")
        self.LogoUser = QtWidgets.QLabel(self.FrameAkun)
        self.LogoUser.setGeometry(QtCore.QRect(60, 300, 41, 41))
        self.LogoUser.setText("")
        self.LogoUser.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/man.png"))
        self.LogoUser.setScaledContents(True)
        self.LogoUser.setObjectName("LogoUser")
        self.username = QtWidgets.QLabel(self.FrameAkun)
        self.username.setGeometry(QtCore.QRect(111, 300, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.username.setFont(font)
        self.username.setStyleSheet("color: rgb(255, 255, 255);")
        self.username.setObjectName("username")
        self.BtnLogOut = QtWidgets.QPushButton(self.FrameAkun)
        self.BtnLogOut.setGeometry(QtCore.QRect(50, 430, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.BtnLogOut.setFont(font)
        self.BtnLogOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnLogOut.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(204, 0, 0);\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(255, 255, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnLogOut.setIcon(icon)
        self.BtnLogOut.setIconSize(QtCore.QSize(19, 19))
        self.BtnLogOut.setObjectName("BtnLogOut")
        self.BtnLogOut.clicked.connect(self.PopUpLogOut)
        self.LogoGen = QtWidgets.QLabel(self.FrameAkun)
        self.LogoGen.setGeometry(QtCore.QRect(70, 350, 21, 31))
        self.LogoGen.setText("")
        self.LogoGen.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/gender.png"))
        self.LogoGen.setScaledContents(True)
        self.LogoGen.setObjectName("LogoGen")
        self.Gender = QtWidgets.QLabel(self.FrameAkun)
        self.Gender.setGeometry(QtCore.QRect(110, 346, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.Gender.setFont(font)
        self.Gender.setStyleSheet("color: rgb(255, 255, 255);")
        self.Gender.setObjectName("Gender")
        self.FrameMenu = QtWidgets.QFrame(Form)
        self.FrameMenu.setGeometry(QtCore.QRect(269, -1, 471, 501))
        self.FrameMenu.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.FrameMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameMenu.setObjectName("FrameMenu")
        self.FrameBooking = QtWidgets.QFrame(self.FrameMenu)
        self.FrameBooking.setGeometry(QtCore.QRect(40, 20, 191, 221))
        self.FrameBooking.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FrameBooking.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameBooking.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameBooking.setObjectName("FrameBooking")
        self.BtnBooking = QtWidgets.QPushButton(self.FrameBooking)
        self.BtnBooking.setGeometry(QtCore.QRect(20, 160, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.BtnBooking.setFont(font)
        self.BtnBooking.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnBooking.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(0, 150, 136);\n"
"}")
        self.BtnBooking.setObjectName("BtnBooking")
        self.BtnBooking.clicked.connect(self.MenuBooking)
        self.TitleBooking = QtWidgets.QLabel(self.FrameBooking)
        self.TitleBooking.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TitleBooking.setFont(font)
        self.TitleBooking.setStyleSheet("color: rgb(0, 150, 136);")
        self.TitleBooking.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleBooking.setObjectName("TitleBooking")
        self.LogoBooking = QtWidgets.QLabel(self.FrameBooking)
        self.LogoBooking.setGeometry(QtCore.QRect(20, 50, 151, 101))
        self.LogoBooking.setText("")
        self.LogoBooking.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/booking.png"))
        self.LogoBooking.setScaledContents(True)
        self.LogoBooking.setObjectName("LogoBooking")
        self.FrameCheckIn = QtWidgets.QFrame(self.FrameMenu)
        self.FrameCheckIn.setGeometry(QtCore.QRect(40, 260, 191, 221))
        self.FrameCheckIn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FrameCheckIn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCheckIn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCheckIn.setObjectName("FrameCheckIn")
        self.BtnCheckIn = QtWidgets.QPushButton(self.FrameCheckIn)
        self.BtnCheckIn.setGeometry(QtCore.QRect(20, 160, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.BtnCheckIn.setFont(font)
        self.BtnCheckIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCheckIn.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(0, 150, 136);\n"
"}")
        self.BtnCheckIn.setObjectName("BtnCheckIn")
        self.BtnCheckIn.clicked.connect(self.MenuCheckIn)
        self.LogoCheckIn = QtWidgets.QLabel(self.FrameCheckIn)
        self.LogoCheckIn.setGeometry(QtCore.QRect(30, 60, 131, 81))
        self.LogoCheckIn.setText("")
        self.LogoCheckIn.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/checkin.png"))
        self.LogoCheckIn.setScaledContents(True)
        self.LogoCheckIn.setObjectName("LogoCheckIn")
        self.TitleCheckIn = QtWidgets.QLabel(self.FrameCheckIn)
        self.TitleCheckIn.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(72)
        self.TitleCheckIn.setFont(font)
        self.TitleCheckIn.setStyleSheet("color: rgb(0, 150, 136);")
        self.TitleCheckIn.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleCheckIn.setObjectName("TitleCheckIn")
        self.FrameDaftar = QtWidgets.QFrame(self.FrameMenu)
        self.FrameDaftar.setGeometry(QtCore.QRect(250, 20, 191, 221))
        self.FrameDaftar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FrameDaftar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameDaftar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameDaftar.setObjectName("FrameDaftar")
        self.BtnDaftar = QtWidgets.QPushButton(self.FrameDaftar)
        self.BtnDaftar.setGeometry(QtCore.QRect(20, 160, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.BtnDaftar.setFont(font)
        self.BtnDaftar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnDaftar.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(0, 150, 136);\n"
"}")
        self.BtnDaftar.setObjectName("BtnDaftar")
        self.BtnDaftar.clicked.connect(self.MenuEdit)
        self.LogoDaftar = QtWidgets.QLabel(self.FrameDaftar)
        self.LogoDaftar.setGeometry(QtCore.QRect(40, 50, 111, 91))
        self.LogoDaftar.setText("")
        self.LogoDaftar.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/Daftar.png"))
        self.LogoDaftar.setScaledContents(True)
        self.LogoDaftar.setObjectName("LogoDaftar")
        self.TitleDaftar = QtWidgets.QLabel(self.FrameDaftar)
        self.TitleDaftar.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TitleDaftar.setFont(font)
        self.TitleDaftar.setStyleSheet("color: rgb(0, 150, 136);")
        self.TitleDaftar.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleDaftar.setObjectName("TitleDaftar")
        self.FrameCheckOut = QtWidgets.QFrame(self.FrameMenu)
        self.FrameCheckOut.setGeometry(QtCore.QRect(250, 260, 191, 221))
        self.FrameCheckOut.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FrameCheckOut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCheckOut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCheckOut.setObjectName("FrameCheckOut")
        self.BtnCheckOut = QtWidgets.QPushButton(self.FrameCheckOut)
        self.BtnCheckOut.setGeometry(QtCore.QRect(20, 160, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.BtnCheckOut.setFont(font)
        self.BtnCheckOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCheckOut.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(0, 150, 136);\n"
"}")
        self.BtnCheckOut.setObjectName("BtnCheckOut")
        self.BtnCheckOut.clicked.connect(self.Cetak)
        self.TitleCheckOut = QtWidgets.QLabel(self.FrameCheckOut)
        self.TitleCheckOut.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TitleCheckOut.setFont(font)
        self.TitleCheckOut.setStyleSheet("color: rgb(0, 150, 136);")
        self.TitleCheckOut.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleCheckOut.setObjectName("TitleCheckOut")
        self.LogoCheckOut = QtWidgets.QLabel(self.FrameCheckOut)
        self.LogoCheckOut.setGeometry(QtCore.QRect(20, 50, 161, 101))
        self.LogoCheckOut.setText("")
        self.LogoCheckOut.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/Print.jpg"))
        self.LogoCheckOut.setScaledContents(True)
        self.LogoCheckOut.setObjectName("LogoCheckOut")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form menu"))
        self.TitleHotel.setText(_translate("Form", "Hotel Madridistas"))
        self.TitleService.setText(_translate("Form", "Resepsonis Service"))
        self.username.setText(_translate("Form", "Username"))
        self.BtnLogOut.setText(_translate("Form", "Log Out"))
        self.Gender.setText(_translate("Form", "Gender"))
        self.BtnBooking.setText(_translate("Form", "Klik Disini"))
        self.TitleBooking.setText(_translate("Form", "Booking Hotel"))
        self.BtnCheckIn.setText(_translate("Form", "Klik Disini"))
        self.TitleCheckIn.setText(_translate("Form", "Check-In/Out"))
        self.BtnDaftar.setText(_translate("Form", "Klik Disini"))
        self.TitleDaftar.setText(_translate("Form", "Update/Edit"))
        self.BtnCheckOut.setText(_translate("Form", "Klik Disini"))
        self.TitleCheckOut.setText(_translate("Form", "Cetak Nota"))

    def MenuBooking(self):
        self.windowBooking = QtWidgets.QWidget()
        self.uiBooking = Ui_Booking()
        self.uiBooking.setupUi(self.windowBooking)
        self.windowBooking.show()

    def MenuEdit(self):
        self.windowEdit = QtWidgets.QWidget()
        self.uiEdit = Ui_Edit()
        self.uiEdit.setupUi(self.windowEdit)
        self.windowEdit.show()

    def MenuCheckIn(self):
        self.windowCheckIn = QtWidgets.QWidget()
        self.uiCheckIn = Ui_ChekIn()
        self.uiCheckIn.setupUi(self.windowCheckIn)
        self.windowCheckIn.show()

    def Cetak(self):
        self.windowCetak = QtWidgets.QWidget()
        self.uiCetakNota = Ui_CetakNota()
        self.uiCetakNota.setupUi(self.windowCetak)
        self.windowCetak.show()

    def PopUpLogOut(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Log Out Hotel Madridistas")
        msg.setText("Are you sure log out?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.LogOut)

        x = msg.exec_()

    def LogOut(self, i):
        if i.text() == "&Yes":
            QtWidgets.QApplication.quit()