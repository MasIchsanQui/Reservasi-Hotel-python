# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuCheckIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import datetime
import mysql.connector
from fpdf import FPDF
import sys
from datetime import datetime

class Ui_CetakNota(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 677)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.TableInform = QtWidgets.QTableWidget(Form)
        self.TableInform.setGeometry(QtCore.QRect(10, 90, 791, 521))
        self.TableInform.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TableInform.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TableInform.setObjectName("TableInform")
        self.TableInform.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(7, item)
        self.FramHeader = QtWidgets.QFrame(Form)
        self.FramHeader.setGeometry(QtCore.QRect(10, 0, 771, 51))
        self.FramHeader.setStyleSheet("background-color: rgb(200, 150, 136);")
        self.FramHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramHeader.setObjectName("FramHeader")
        self.LabelTittle = QtWidgets.QLabel(self.FramHeader)
        self.LabelTittle.setGeometry(QtCore.QRect(8, 0, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(60)
        self.LabelTittle.setFont(font)
        self.LabelTittle.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelTittle.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTittle.setObjectName("LabelTittle")
        self.BtnExit = QtWidgets.QPushButton(Form)
        self.BtnExit.setGeometry(QtCore.QRect(500, 620, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
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
        self.BtnReload.setGeometry(QtCore.QRect(320, 620, 121, 41))
        self.BtnReload.clicked.connect(self.ClickedReload)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
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
        
        self.BtnCetak = QtWidgets.QPushButton(Form)
        self.BtnCetak.setGeometry(QtCore.QRect(140, 620, 121, 41))
        self.BtnCetak.clicked.connect(self.ClickedCetak)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.BtnCetak.setFont(font)
        self.BtnCetak.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCetak.setStyleSheet("QPushButton{\n"
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
        self.BtnCetak.setObjectName("BtnCetak")

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
        item.setText(_translate("Form", "Harga"))
        item = self.TableInform.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Check In"))
        item = self.TableInform.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Check Out"))
        self.LabelTittle.setText(_translate("Form", "Cetak Nota"))
        self.BtnExit.setText(_translate("Form", "EXIT APP"))
        self.BtnReload.setText(_translate("Form", "RELOAD"))
        self.BtnCetak.setText(_translate("Form", "Cetak"))

    def show_message1(self, title="text", message="text"):
        QtWidgets.QMessageBox.information(None, title, message)

    def ReloadData(self):
        db = mysql.connector.connect(user="root", database="Hotelst")
        cursor = db.cursor()

        query = (
            "SELECT "
            "`Kamar`.`no_kamar`, "
            "`Tamu`.`nama_tamu`, "
            "`Tamu`.`alamat`, "
            "`Transaksi`.`tanggal_in`, "
            "`Transaksi`.`tanggal_out`, "
            "`Transaksi`.`jumlah`, "
            "`Transaksi`.`check_in`, "
            "`Transaksi`.`check_out` "
            "FROM Transaksi, Kamar, Tamu "
            "WHERE Kamar.no_kamar = Transaksi.no_kamarFK AND Tamu.id_tamu = Transaksi.id_tamuFK "
            "ORDER BY `Kamar`.`no_kamar` ASC"
        )
        cursor.execute(query)

        self.TableInform.setRowCount(0)
        for row_number, row_data in enumerate(cursor):
            self.TableInform.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.TableInform.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        db.commit()
        cursor.close()
        db.close()

    def ClickedReload(self):
        self.ReloadData()
        self.show_message1("Reload Data", "Reload Data Selesai")
    
    def ClickedCetak(self):
        db_config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'hotelst',
            'raise_on_warnings': True
         }

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = (
        "SELECT "
            "Transaksi.id_tamuFK AS id_tamu, "
            "Transaksi.id_transaksi, "
            "Tamu.nama_tamu, "
            "Transaksi.tanggal_in, "
            "Transaksi.tanggal_out, "
            "Kamar.no_kamar, "
            "Transaksi.check_out AS num_days, "
            "Kamar.jenis_kamar, "
            "CASE "
                "WHEN Kamar.jenis_kamar = 'Ekonomi' THEN 300000 "
                "WHEN Kamar.jenis_kamar = 'VVIP' THEN 400000 "
                "ELSE 0 "
            "END AS harga "
        "FROM Transaksi "
        "JOIN Tamu ON Transaksi.id_tamuFK = Tamu.id_tamu "
        "JOIN Kamar ON Transaksi.no_kamarFK = Kamar.no_kamar;")

        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            id_tamu, id_transaksi, nama_tamu, tanggal_in, tanggal_out, no_kamar, num_days, jenis_kamar, harga = row
            tanggal_in = tanggal_in.strftime("%Y-%m-%d")
            tanggal_out = tanggal_out.strftime("%Y-%m-%d")

            tanggal_out = datetime.strptime(tanggal_out, "%Y-%m-%d")
            tanggal_in = datetime.strptime(tanggal_in, "%Y-%m-%d")
            num_days = (tanggal_out - tanggal_in).days

            
            if jenis_kamar in ['VVIP', 'Ekonomi']:
                total_cost_float = 0.0  # Set a default value for 'VVIP' and 'Ekonomi'
            else:
                print(f"Raw Harga: {harga}")
                try:
                    total_cost_float = float(harga)
                    print(f"Parsed Harga: {total_cost_float}")
                except ValueError:
                    print("Invalid total_cost value")
                    total_cost_float = 0.0

                # Create a PDF payment receipt
            self.create_payment_receipt(
            file_name=f"{nama_tamu}_{id_transaksi}.pdf",
            id_transaksi=id_transaksi,
            nama_tamu=nama_tamu,
            jenis_kamar=jenis_kamar,
            no_kamar=no_kamar,
            tanggal_in=tanggal_in,
            tanggal_out=tanggal_out,
            harga=harga,
            total_cost=num_days*harga,
            num_days=num_days
            )
                # Display a message
            self.show_message("Cetak Nota", f"Payment receipt created: {nama_tamu}_{id_transaksi}.pdf")


        cursor.close()
        conn.close()

    def create_payment_receipt(self, file_name, id_transaksi, nama_tamu, no_kamar, jenis_kamar, tanggal_in, tanggal_out, harga, total_cost, num_days):
        file_name = f"{nama_tamu}_{id_transaksi}.pdf"
        c = FPDF('P', 'mm', 'A4')

        c.add_page()

        # Add the logo
        logo_path = "C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png"
        c.image(logo_path, x=15, y=10, w=30)

        # Adjust margins and spacing
        c.set_margins(20, 20, 50)
        c.set_auto_page_break(auto=True, margin=15)
        indentation = 5

        # Add header and contact details
        c.set_font('Arial', 'B', 16)
        c.set_x(50)
        c.cell(0, 10, "HOTEL MADRIDISTAS", 0, 1, 'L')

        c.set_font('Arial', '', 12)
        c.set_x(50)
        c.cell(0, 10, "Kwitansi Pembayaran", 0, 1, 'L')
        c.set_x(50)
        c.cell(0, 10, "Jl. Ahmad Yani No.31 Gurah, Kediri, Jawa Timur", 0, 1, 'L')
        c.cell(0, 10, "", 0, 1, 'L')
        # Add a horizontal line
        c.line(10, c.get_y(), 200, c.get_y())

        # Add transaction details
        c.set_font('Arial', '', 12)
        c.cell(0, 10, f"Nomor Transaksi : {id_transaksi}", 0, 1, 'L')
        c.set_font('Arial', '', 12)
        c.cell(0, 10, f"Nama                   : {nama_tamu}", 0, 1, 'L')
        c.cell(0, 10, f"No. Kamar            : {no_kamar}", 0, 1, 'L')
        c.cell(0, 10, f"Jenis Kamar        : {jenis_kamar}", 0, 1, 'L')
        c.cell(0, 10, f"Check In              : {tanggal_in}", 0, 1, 'L')
        c.cell(0, 10, f"Check Out           : {tanggal_out}", 0, 1, 'L')

        # Add a horizontal line
        c.line(10, c.get_y(), 200, c.get_y())
        # Add billing details
        c.set_font('Arial', '', 12)
        c.cell(0, 10, f"Harga Kamar      : Rp. {float(harga):,.2f}", 0, 1, 'L')
        c.set_font('Arial', '', 12)
        c.cell(0, 10, f"Lama Inap           : {num_days} hari", 0, 1, 'L')
        c.cell(0, 10, f"Total tagihan       : Rp. {float(total_cost):,.2f}", 0, 1, 'L')

        # Add payment details
        c.set_font('Arial', '', 12)
        c.cell(0, 10, f"Terbayar              : Rp. {float(total_cost):,.2f}", 0, 1, 'L')
        c.set_font('Arial', '', 12)
        c.cell(0, 10, "Sisa/Kurang         : Rp. 0", 0, 1, 'L')
        c.cell(0, 10, "Kembali                : Rp. 0", 0, 1, 'L')

        # Add a horizontal line
        c.line(10, c.get_y(), 200, c.get_y())
        c.cell(0, 5, "", 0, 1, 'L')
        c.set_x(135)
        c.cell(70, 10, f"Kediri, {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'L')
        c.cell(0, 10, "", 0, 1, 'R')
        c.cell(0, 10, "", 0, 1, 'L')
        c.set_x(100)
        c.cell(70, 10, "Admin", 0, 1, 'R')
        c.cell(0, 10, "", 0, 1, 'L')
        dot_length = 2
        space_length = 1
        x_position = 10
        while x_position < 200:
            c.line(x_position, c.get_y(), x_position + dot_length, c.get_y())
            x_position += dot_length + space_length
        c.output(file_name)

    def show_message(self, title, message):
        QMessageBox.information(None, title, message)

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