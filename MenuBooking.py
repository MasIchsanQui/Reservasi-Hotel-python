# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuBooking.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import mysql.connector
import datetime

class Ui_Booking(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1082, 635)
        self.datetime = datetime.datetime.now()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.TableInform = QtWidgets.QTableWidget(Form)
        self.TableInform.setGeometry(QtCore.QRect(370, 80, 701, 521))
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
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        item.setFont(font)
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
        self.FramHeader.setGeometry(QtCore.QRect(-1, 0, 1091, 51))
        self.FramHeader.setStyleSheet("background-color: rgb(200, 150, 136);")
        self.FramHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramHeader.setObjectName("FramHeader")
        self.LabelTittle = QtWidgets.QLabel(self.FramHeader)
        self.LabelTittle.setGeometry(QtCore.QRect(50, 0, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTittle.setFont(font)
        self.LabelTittle.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelTittle.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTittle.setObjectName("LabelTittle")
        self.LogoTitle = QtWidgets.QLabel(self.FramHeader)
        self.LogoTitle.setGeometry(QtCore.QRect(50, 6, 51, 41))
        self.LogoTitle.setText("")
        self.LogoTitle.setPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/LogMenu.png"))
        self.LogoTitle.setScaledContents(True)
        self.LogoTitle.setObjectName("LogoTitle")
        self.FormNama = QtWidgets.QLineEdit(Form)
        self.FormNama.setGeometry(QtCore.QRect(20, 110, 331, 31))
        self.FormNama.setObjectName("FormNama")
        self.LabelNama = QtWidgets.QLabel(Form)
        self.LabelNama.setGeometry(QtCore.QRect(20, 90, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelNama.setFont(font)
        self.LabelNama.setObjectName("LabelNama")
        self.LabelAlamat = QtWidgets.QLabel(Form)
        self.LabelAlamat.setGeometry(QtCore.QRect(20, 160, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelAlamat.setFont(font)
        self.LabelAlamat.setObjectName("LabelAlamat")
        self.LineAlamat = QtWidgets.QLineEdit(Form)
        self.LineAlamat.setGeometry(QtCore.QRect(20, 180, 331, 71))
        self.LineAlamat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LineAlamat.setObjectName("LineAlamat")
        self.LabelKamar = QtWidgets.QLabel(Form)
        self.LabelKamar.setGeometry(QtCore.QRect(20, 270, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelKamar.setFont(font)
        self.LabelKamar.setObjectName("LabelKamar")
        self.RadioEkonomi = QtWidgets.QRadioButton(Form)
        self.RadioEkonomi.setGeometry(QtCore.QRect(140, 290, 112, 23))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.RadioEkonomi.setFont(font)
        self.RadioEkonomi.setObjectName("RadioEkonomi")
        self.RadioEkonomi.toggled.connect(lambda:self.clickedRadio(self.RadioEkonomi))
        self.RadioVVIP = QtWidgets.QRadioButton(Form)
        self.RadioVVIP.setGeometry(QtCore.QRect(70, 290, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.RadioVVIP.setFont(font)
        self.RadioVVIP.setObjectName("RadioVVIP")
        self.RadioVVIP.toggled.connect(lambda:self.clickedRadio(self.RadioVVIP))
        self.DateIn = QtWidgets.QDateEdit(Form)
        self.DateIn.setGeometry(QtCore.QRect(20, 350, 110, 26))
        self.DateIn.setObjectName("DateIn")
        self.DateIn.setMinimumDate(QtCore.QDate(self.datetime.year, self.datetime.month, self.datetime.day))
        self.LabelTanggalIn = QtWidgets.QLabel(Form)
        self.LabelTanggalIn.setGeometry(QtCore.QRect(20, 330, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelTanggalIn.setFont(font)
        self.LabelTanggalIn.setObjectName("LabelTanggalIn")
        self.LabelTanggalOut = QtWidgets.QLabel(Form)
        self.LabelTanggalOut.setGeometry(QtCore.QRect(20, 390, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelTanggalOut.setFont(font)
        self.LabelTanggalOut.setObjectName("LabelTanggalOut")
        self.DateOut = QtWidgets.QDateEdit(Form)
        self.DateOut.setGeometry(QtCore.QRect(20, 410, 110, 26))
        self.DateOut.setObjectName("DateOut")
        self.DateOut.setMinimumDate(QtCore.QDate(self.datetime.year, self.datetime.month, self.datetime.day))
        self.LabelHarga = QtWidgets.QLabel(Form)
        self.LabelHarga.setGeometry(QtCore.QRect(20, 450, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelHarga.setFont(font)
        self.LabelHarga.setObjectName("LabelHarga")
        self.FormHarga = QtWidgets.QLabel(Form)
        self.FormHarga.setGeometry(QtCore.QRect(150, 450, 191, 17))
        self.FormHarga.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FormHarga.setObjectName("FormHarga")
        self.BtnEdit = QtWidgets.QPushButton(Form)
        self.BtnEdit.setGeometry(QtCore.QRect(20, 480, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.BtnEdit.setFont(font)
        self.BtnEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEdit.setStyleSheet("QPushButton{\n"
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
        self.BtnEdit.setObjectName("BtnEdit")
        self.BtnEdit.clicked.connect(self.clickedSubmit)
        self.FormNoKamar = QtWidgets.QLineEdit(Form)
        self.FormNoKamar.setGeometry(QtCore.QRect(20, 290, 41, 25))
        self.FormNoKamar.setObjectName("FormNoKamar")
        self.BtnExit = QtWidgets.QPushButton(Form)
        self.BtnExit.setGeometry(QtCore.QRect(190, 540, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.BtnExit.setFont(font)
        self.BtnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnExit.setStyleSheet("QPushButton{\n"
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
        self.BtnExit.setObjectName("BtnExit")
        self.BtnExit.clicked.connect(self.ClickedExit)
        self.BtnReload = QtWidgets.QPushButton(Form)
        self.BtnReload.setGeometry(QtCore.QRect(190, 480, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.BtnReload.setFont(font)
        self.BtnReload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnReload.setStyleSheet("QPushButton{\n"
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
        self.BtnReload.setObjectName("BtnReload")
        self.BtnReload.clicked.connect(self.clickedReload)
        self.LabelTotalIncome = QtWidgets.QLabel(Form)
        self.LabelTotalIncome.setGeometry(QtCore.QRect(700, 600, 950, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(73)
        self.LabelTotalIncome.setFont(font)
        self.LabelTotalIncome.setObjectName("LabelTotalIncome")

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
        item.setText(_translate("Form", "Alamat"))
        item = self.TableInform.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jenis Kamar"))
        item = self.TableInform.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tanggal In"))
        item = self.TableInform.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tanggal Out"))
        item = self.TableInform.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Harga"))
        self.LabelTittle.setText(_translate("Form", "FORM BOOKING HOTEL MADRIDISTAS"))
        self.LabelNama.setText(_translate("Form", "Nama :"))
        self.LabelAlamat.setText(_translate("Form", "Alamat :"))
        self.LabelKamar.setText(_translate("Form", "No & Jenis Kamar :"))
        self.RadioEkonomi.setText(_translate("Form", "Ekonomi"))
        self.RadioVVIP.setText(_translate("Form", "VVIP"))
        self.LabelTanggalIn.setText(_translate("Form", "Tanggal In :"))
        self.LabelTanggalOut.setText(_translate("Form", "Tanggal Out :"))
        self.LabelHarga.setText(_translate("Form", "Harga :"))
        self.BtnEdit.setText(_translate("Form", "SUBMIT"))
        self.BtnExit.setText(_translate("Form", "EXIT APP"))
        self.BtnReload.setText(_translate("Form", "RELOAD"))


    def show_message(self, title="text", message="text"):
        QtWidgets.QMessageBox.information(None, title, message)

    def ReloadData(self):
        db = mysql.connector.connect(user="root", database="Hotelst")
        cursor = db.cursor()
        query = ("SELECT `Kamar`.`no_kamar`, `Tamu`.`nama_tamu`, `Tamu`.`alamat`, `Kamar`.`jenis_kamar`, `Transaksi`.`tanggal_in`, `Transaksi`.`tanggal_out`, `Transaksi`.`jumlah` FROM Transaksi, Kamar, Tamu WHERE Kamar.no_kamar = Transaksi.no_kamarFK AND Tamu.id_tamu = Transaksi.id_tamuFK")
        cursor.execute(query)
        self.TableInform.setRowCount(0)
        for row_number, row_data in enumerate(cursor):
            self.TableInform.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.TableInform.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

        total_income = self.calculate_total_income()  # Add this line
        self.LabelTotalIncome.setText(f"Total Income: Rp. {total_income:,.2f}")  # Update this line

        db.commit()
        cursor.close()
        db.close()

    def calculate_total_income(self):
        db = mysql.connector.connect(user="root", database="hotelst")
        cursor = db.cursor()

        query = "SELECT SUM(jumlah) FROM Transaksi"
        cursor.execute(query)

        total_income = cursor.fetchone()[0] or 0  # Handle the case where the result is None

        db.commit()
        cursor.close()
        db.close()

        return total_income

    def clickedReload(self):
        self.show_message("Reload Data", "Reload Data Selesai")
        self.ReloadData()

    def clickedRadio(self, b):
        _translate = QtCore.QCoreApplication.translate
        self.infoRadio = ""
        radioButton = b.sender()
        if radioButton.isChecked():
            if radioButton.text() == "Ekonomi":
                self.infoRadio = radioButton.text()
                self.FormHarga.setText(_translate("Form", "Rp. 300.000,00"))
            else :
                self.infoRadio = radioButton.text()
                self.FormHarga.setText(_translate("Form", "Rp. 400.000,00"))

    def clickedSubmit(self):
        db = mysql.connector.connect(user="root", database="Hotelst")
        cursor = db.cursor()
        conn = pymysql.connect(user="root", db="Hotelst", autocommit=True)
        cur = conn.cursor()

        DateIn = self.DateIn.date().toString("yyyy-MM-dd")
        formatted_date_in = datetime.datetime.strptime(DateIn, "%Y-%m-%d").date()

        DateOut = self.DateOut.date().toString("yyyy-MM-dd")
        formatted_date_out = datetime.datetime.strptime(DateOut, "%Y-%m-%d").date()

        # Extracting dates from the date edit widgets
        date_in = self.DateIn.date().toPyDate()
        date_out = self.DateOut.date().toPyDate()

        # Calculating the number of days
        num_days = (date_out - date_in).days

        

        id_tamu = 0
        id_transaksi = 0
        query1 = ("SELECT `Tamu`.`id_tamu`, `Transaksi`.`id_transaksi` FROM Transaksi, Tamu WHERE Tamu.id_tamu = Transaksi.id_tamuFK")
        cursor.execute(query1)
        for (dataTamu, dataTransaksi) in cursor:
            id_tamu = int(dataTamu)
            id_transaksi = int(dataTransaksi)

        harga = 0
        if self.infoRadio == "Ekonomi":
            harga = 300000
        else :
            harga = 400000

        total_cost = harga * num_days

        query2 = ("INSERT INTO Tamu(id_tamu, nama_tamu, alamat) VALUES(%s, %s, %s)")
        cur.execute(query2, (id_tamu+1, self.FormNama.text(), self.LineAlamat.text()))
        query3 = ("INSERT INTO Kamar(no_kamar, id_tamuFK, jenis_kamar) VALUES(%s, %s, %s)")
        cur.execute(query3, (self.FormNoKamar.text(), id_tamu+1, self.infoRadio))
        query4 = ("INSERT INTO Transaksi(id_transaksi, id_tamuFK, no_kamarFK, tanggal_in, tanggal_out, jumlah) VALUES(%s, %s, %s, %s, %s, %s)")
        cur.execute(query4, (id_transaksi+1, id_tamu+1, self.FormNoKamar.text(), formatted_date_in, formatted_date_out, total_cost))

        db.commit()
        cursor.close()
        cur.close()
        conn.close()
        db.close()

        self.ReloadData()
        self.show_message("Submit Tamu", f"Data tamu sudah tersubmit. Total cost: Rp. {total_cost:,.2f}")

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