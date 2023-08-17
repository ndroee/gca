import datetime
import sys
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import QDate
import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets
from gca3f_ui import Ui_MainWindow


class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.records = None
        self.current_record_index = None
        self.db_cursor = None
        self.db_connection = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.records = []  # Inisialisasi records sebagai list kosong
        self.current_record_index = 0  # Inisialisasi current_record_index dengan nilai yang valid
        self.load_record(self.current_record_index)

        self.ui.txtBrtP48.textChanged.connect(self.updateTotalBerat)
        self.ui.txtBrtP100.textChanged.connect(self.updateTotalBerat)
        self.ui.txtBrtM100.textChanged.connect(self.updateTotalBerat)
        # Hubungkan tombol OK dengan fungsi filter_records
        self.ui.pushButton.clicked.connect(self.filter_records)

        self.ui.rbP48.toggled.connect(self.checkRadioButtons)
        self.ui.rbP100.toggled.connect(self.checkRadioButtons)
        self.ui.rbM100.toggled.connect(self.checkRadioButtons)

        self.ui.btnOk.clicked.connect(self.printToConsole)

        today = QDate.currentDate()
        one_month_ago = today.addMonths(-1)
        self.ui.tglDari.setDate(one_month_ago)
        self.ui.tglSampai.setDate(today)

        self.ui.scrollArea.setEnabled(False)

        # Create a connection to the local SQL Server database
        server_name = 'HPZ6PKPEKSPL1\LOCALSQL'  # Change this to your SQL Server's hostname or IP
        database_name = 'GCA'  # Change this to your database name
        username = 'sa'  # Change this to your SQL Server username
        password = 'P@ssw0rd123'  # Change this to your SQL Server password

        conn_str = (
            f'DRIVER={{SQL Server}};'
            f'SERVER={server_name};'
            f'DATABASE={database_name};'
            f'UID={username};'
            f'PWD={password};'
        )

        self.db_connection = pyodbc.connect(conn_str)
        self.db_cursor = self.db_connection.cursor()

        # Set up button connections
        self.ui.btnPrev.clicked.connect(self.load_previous_record)
        self.ui.btnNext.clicked.connect(self.load_next_record)

        # Load the initial record
        self.current_record_index = 0
        self.load_record(self.current_record_index)

    def updateTotalBerat(self):
        try:
            berat_p48 = float(self.ui.txtBrtP48.text() or 0)
            berat_p100 = float(self.ui.txtBrtP100.text() or 0)
            berat_m100 = float(self.ui.txtBrtM100.text() or 0)
            total_berat = berat_p48 + berat_p100 + berat_m100
            self.ui.txtTotBrt.setText(str(total_berat))
        except ValueError:
            self.ui.txtTotBrt.setText("")

    def handle_filter_button(self):
        try:
            self.filter_records()
        except Exception as e:
            print("Error:", e)

    def load_record(self, index):
        if hasattr(self, 'records'):
            records = self.records

            if 0 <= index < len(records):
                record = records[index]
                self.ui.txtSiteID.setText(str(record[2]))
                self.ui.txtLapis.setText(str(record[4]))
                self.ui.txtBrtTbg.setText(str(record[10]))
                self.ui.txtBulan.setText(str(record[5]))
                self.ui.txtLok.setText(str(record[8]))
                self.ui.txtAsal.setText(str(record[7]))
        else:
            self.ui.txtSiteID.clear()
            self.ui.txtLapis.clear()
            self.ui.txtBrtTbg.clear()
            self.ui.txtBulan.clear()
            self.ui.txtLok.clear()
            self.ui.txtAsal.clear()

    def filter_records(self):
        tgl_dari = self.ui.tglDari.date()
        tgl_sampai = self.ui.tglSampai.date()

        tgl_dari_datetime = datetime.datetime(tgl_dari.year(), tgl_dari.month(), tgl_dari.day())
        tgl_sampai_datetime = datetime.datetime(tgl_sampai.year(), tgl_sampai.month(), tgl_sampai.day())

        if tgl_dari_datetime > tgl_sampai_datetime:
            QMessageBox.critical(self.ui.centralwidget, "Error", "Tanggal Dari harus lebih awal dari Tanggal Sampai")
            return

        query = "SELECT * FROM GB_GCA_SAMPLE WHERE SAMPLE_DATE BETWEEN ? AND ?"
        self.db_cursor.execute(query, (tgl_dari_datetime, tgl_sampai_datetime))
        records = self.db_cursor.fetchall()

        if records:
            self.current_record_index = 0
            self.records = records
            self.load_record(self.current_record_index)
        else:
            QMessageBox.information(self.ui.centralwidget, "Info", "Tidak ada data yang cocok dengan filter tanggal")

    def load_previous_record(self):
        if self.current_record_index > 0:
            self.current_record_index -= 1
            self.load_record(self.current_record_index)

    def load_next_record(self):
        query = "SELECT * FROM GB_GCA_SAMPLE"
        self.db_cursor.execute(query)
        records = self.db_cursor.fetchall()

        if self.current_record_index < len(records) - 1:
            self.current_record_index += 1
            self.load_record(self.current_record_index)

    def checkRadioButtons(self):
        # Cek status tombol radio
        rbP48_checked = self.ui.rbP48.isChecked()
        rbP100_checked = self.ui.rbP100.isChecked()
        rbM100_checked = self.ui.rbM100.isChecked()

        # Aktifkan scrollArea jika salah satu tombol radio terpilih, nonaktifkan jika tidak ada yang terpilih
        self.ui.scrollArea.setEnabled(rbP48_checked or rbP100_checked or rbM100_checked)

    def printToConsole(self):
        mineral1 = self.ui.cbM1.currentText()
        mineral2 = self.ui.cbM2.currentText()
        asal = self.ui.txtAsal.text()
        sampleid = self.ui.txtSiteID.text()
        btrM1 = self.ui.leM01.text()
        angular = self.ui.cbA
        subangular = self.ui.cbSA
        rounded = self.ui.cbR
        wellrounded = self.ui.cbWR
        subrounded = self.ui.cbSR
        subangularwellrounded = self.ui.cbSASR

        hasil = f"{sampleid} {mineral1} {btrM1} butir dari {asal}"
        print("mineral 1", mineral1,btrM1,"butir")
        print("mineral 2", mineral2)
        print("asal", asal)
        print("sample id", sampleid)
        print(hasil)
        print()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
