import sys
import mysql.connector
from fpdf import FPDF
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget, QMessageBox, QTableWidget
from PyQt5.QtGui import QIcon

class CetakNota(QtWidgets.QMainWindow):
    def init_ui(self):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setWindowTitle('Cetak Nota')
        self.setWindowIcon(QIcon('C:\\Users\\shafira\\Documents\\New folder\\project pbo\\fix\\img/madrid.png'))
        vbox = QVBoxLayout(central_widget)
        

        btn = QPushButton('Cetak Nota',self)
        btn.setMinimumWidth(300) #
        btn.clicked.connect(self.on_click)

        vbox.addWidget(btn)
        self.setLayout(vbox)

    def on_click(self):
        db_config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'hotel',
            'raise_on_warnings': True
        }

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = ("SELECT id_tamu, id_transaksi, nama_tamu, tanggal_in, tanggal_out, jumlah FROM Tamu JOIN Kamar JOIN Transaksi ON Tamu.id_tamu = Kamar.id_tamuFK AND Kamar.no_kamar = Transaksi.no_kamarFK")
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            id_tamu, id_transaksi, nama_tamu, tanggal_in, tanggal_out, jumlah = row

            # Create a PDF payment receipt
            self.create_payment_receipt(id_tamu, id_transaksi, jumlah, nama_tamu, tanggal_in, tanggal_out)

            # Display a message
            self.show_message("Cetak Nota", f"Payment receipt created: {nama_tamu}_{id_transaksi}.pdf")

        cursor.close()
        conn.close()

    def create_payment_receipt(self, id_tamu, id_transaksi, total_cost, nama_tamu, tanggal_in, tanggal_out):
        file_name = f"{nama_tamu}_{id_transaksi}.pdf"
        c = FPDF('P', 'mm', 'A4')

        # Set font
        c.set_font('Arial', 'B', 16)

        # Add content to the PDF
        c.add_page()
        c.cell(0, 10, "Hotel Payment Receipt", 0, 1, 'C')
        c.set_font('Arial', '', 12)
        c.cell(0, 10, f"Customer Name: {nama_tamu}", 0, 1, 'L')
        c.cell(0, 10, f"Check-in Date: {tanggal_in}", 0, 1, 'L')
        c.cell(0, 10, f"Check-out Date: {tanggal_out}", 0, 1, 'L')
        c.cell(0, 10, f"Total Amount: Rp. {total_cost:,.2f}", 0, 1, 'L')

        # Add a line separator
        c.line(10, 66, 200, 66)

        c.cell(0, 10, "Thank you for choosing our hotel!", 0, 1, 'C')

        # Save the PDF
        c.output(file_name)

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CetakNota()
    ex.init_ui()
    ex.show()
    sys.exit(app.exec_())