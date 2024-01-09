# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuCheckIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pymysql
import mysql.connector

class Ui_ChekIn(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 677)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.TableInform = QtWidgets.QTableWidget(Form)
        self.TableInform.setGeometry(QtCore.QRect(10, 90, 701, 521))
        self.TableInform.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TableInform.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TableInform.setObjectName("TableInform")
        self.TableInform.setColumnCount(7)
        self.TableInform.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        item.setFont(font)
        self.TableInform.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        item.setFont(font)
        self.TableInform.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(6, item)
        self.FramHeader = QtWidgets.QFrame(Form)
        self.FramHeader.setGeometry(QtCore.QRect(-10, 0, 741, 51))
        self.FramHeader.setStyleSheet("background-color: rgb(0, 150, 136);")
        self.FramHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramHeader.setObjectName("FramHeader")
        self.LabelTittle = QtWidgets.QLabel(self.FramHeader)
        self.LabelTittle.setGeometry(QtCore.QRect(10, 0, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(60)
        self.LabelTittle.setFont(font)
        self.LabelTittle.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelTittle.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTittle.setObjectName("LabelTittle")
        self.LogoTitle = QtWidgets.QLabel(self.FramHeader)
        self.LogoTitle.setGeometry(QtCore.QRect(40, 10, 36, 36))
        self.LogoTitle.setText("")
        self.LogoTitle.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/LogMenu.png"))
        self.LogoTitle.setScaledContents(True)
        self.LogoTitle.setObjectName("LogoTitle")
        self.BtnEdit_2 = QtWidgets.QPushButton(Form)
        self.BtnEdit_2.setGeometry(QtCore.QRect(70, 620, 110, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.BtnCheckIn = QtWidgets.QPushButton(Form)
        self.BtnCheckIn.setGeometry(QtCore.QRect(100, 620, 110, 41))
        self.setup_button(self.BtnCheckIn, "CHECK IN", self.ClickedCheckIn)
        self.BtnCheckOut = QtWidgets.QPushButton(Form)
        self.BtnCheckOut.setGeometry(QtCore.QRect(230, 620, 110, 41))
        self.setup_button(self.BtnCheckOut, "CHECK OUT", self.ClickedCheckOut)
        self.BtnExit = QtWidgets.QPushButton(Form)
        self.BtnExit.setGeometry(QtCore.QRect(490, 620, 110, 41))
        self.setup_button2(self.BtnExit, "EXIT APP", self.ClickedExit)
        self.BtnReload = QtWidgets.QPushButton(Form)
        self.BtnReload.setGeometry(QtCore.QRect(360, 620, 110, 41))
        self.setup_button(self.BtnReload, "RELOAD", self.ClickedReload)

        self.LabelSearch = QtWidgets.QLabel(Form)
        self.LabelSearch.setGeometry(QtCore.QRect(15, 53, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelSearch.setFont(font)
        self.LabelSearch.setObjectName("LabelSearch")
        self.LabelSearch.setText("Cari No. Kamar:")
        self.LineSearch = QtWidgets.QLineEdit(Form)
        self.LineSearch.setGeometry(QtCore.QRect(130, 53, 191, 31))
        self.LineSearch.setObjectName("LineSearch")
        self.LineSearch.textChanged.connect(self.SearchData)
        self.LineSearch.returnPressed.connect(self.SearchData)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.TableInform.horizontalHeaderItem(0)
        item.setText(_translate("Form", "No. Kamar"))
        item = self.TableInform.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama"))
        item = self.TableInform.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Jenis Kamar"))
        item = self.TableInform.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Tanggal In"))
        item = self.TableInform.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tanggal Out"))
        item = self.TableInform.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Check In"))
        item = self.TableInform.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Check Out"))
        self.LabelTittle.setText(_translate("Form", "FORM CHECK IN/OUT HOTEL MADRIDISTAS"))
        self.LabelSearch.setText(_translate("Form", "Cari No. Kamar:"))
        
    def setup_button(self, button, text, slot):
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(20)
        button.setFont(font)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("QPushButton{\n"
                             "background-color: rgb(0, 150, 136);\n"
                             "color:white;\n"
                             "border-style:outset;\n"
                             "border-radius:20px;\n"
                             "}\n"
                             "QPushButton::hover{\n"
                             "background-color: rgb(255, 255, 255);\n"
                             "color:black;\n"
                             "border-style:outset;\n"
                             "border-width:2px;\n"
                             "border-radius:20px;\n"
                             "border-color:rgb(0,150,136);\n"
                             "}")
        button.setObjectName(f"{text}Button")
        button.setText(text)
        button.clicked.connect(slot)

    def setup_button2(self, button, text, slot):
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(20)
        button.setFont(font)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("QPushButton{\n"
"background-color: rgb(204, 0, 0);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color:rgb(204, 0, 0);\n"
"}")
        button.setObjectName(f"{text}Button")
        button.setText(text)
        button.clicked.connect(slot)

    def show_message(self, title="text", message="text"):
        QtWidgets.QMessageBox.information(None, title, message)

    def ReloadData(self):
        db = mysql.connector.connect(user="root", database="Hotelst")
        cursor = db.cursor()

        query = ("SELECT `Kamar`.`no_kamar`, `Tamu`.`nama_tamu`, `Tamu`.`alamat`, `Transaksi`.`tanggal_in`, `Transaksi`.`tanggal_out`, `Transaksi`.`check_in`, `Transaksi`.check_out FROM Transaksi, Kamar, Tamu WHERE Kamar.no_kamar = Transaksi.no_kamarFK AND Tamu.id_tamu = Transaksi.id_tamuFK")
        cursor.execute(query)

        self.TableInform.setRowCount(0)
        for row_number, row_data in enumerate(cursor):
            self.TableInform.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.TableInform.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        
        db.commit()
        cursor.close()
        db.close()

    def SearchData(self):
        search_text = self.LineSearch.text().lower()

        # Reload data and sort it based on room number
        self.ReloadData()
        self.SortData()

        if not search_text:
            return

        # Perform binary search on the sorted data
        left, right = 0, self.TableInform.rowCount() - 1

        while left <= right:
            mid = (left + right) // 2
            item = self.TableInform.item(mid, 0)

            if item and search_text in item.text().lower():
                for col in range(self.TableInform.columnCount()):
                    self.TableInform.item(mid, col).setBackground(QtGui.QColor(255, 255, 0))
                return
            elif item and search_text < item.text().lower():
                right = mid - 1
            else:
                left = mid + 1

    def SortData(self):
        self.TableInform.sortItems(0, QtCore.Qt.AscendingOrder)

    def SelectedItems(self):
        return self.TableInform.item(self.TableInform.currentRow(), 0).text()

    def ClickedReload(self):
        self.ReloadData()
        self.show_message("Reload Data", "Reload Data Selesai")

    def ClickedCheckIn(self):
        conn = pymysql.connect(user="root", db="Hotelst", autocommit=True)
        cursor = conn.cursor()

        Date = datetime.datetime.now()
        Year = str(Date.year)
        Month = str(Date.month)
        Day = str(Date.day)

        equery = ("UPDATE Transaksi SET check_in = %s WHERE no_kamarFK = %s")
        cursor.execute(equery, (Year+"-"+Month+"-"+Day, self.SelectedItems()))

        cursor.close()
        conn.close()
        self.ReloadData()
        self.show_message("Check In", "Check In Selesai")

    def ClickedCheckOut(self):
        conn = pymysql.connect(user="root", db="Hotelst", autocommit=True)
        cursor = conn.cursor()

        Date = datetime.datetime.now()
        Year = str(Date.year)
        Month = str(Date.month)
        Day = str(Date.day)

        equery = ("UPDATE Transaksi SET check_out = %s WHERE no_kamarFK = %s")
        cursor.execute(equery, (Year+"-"+Month+"-"+Day, self.SelectedItems()))

        cursor.close()
        conn.close()
        self.ReloadData()
        self.show_message("Check Out", "Check Out Selesai")

    def ClickedExit(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Exit Aplication")
        msg.setText("Are you sure exit?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.LogOut)

        x = msg.exec_()

    def LogOut(self, i):
        if i.text() == "&Yes":
            QtWidgets.QApplication.quit()