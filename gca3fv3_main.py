import datetime
import sys
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import QDate
import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets
from gca3fv3_ui import Ui_MainWindow



class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.records = None
        self.current_record_index = None
        self.db_cursor = None
        self.db_connection = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database_connection()
        self.setup_initial_records()
        self.setup_connection()


    def setup_connection(self):
        self.ui.txtBrtP48.textChanged.connect(self.updateTotalBerat)
        self.ui.txtBrtP100.textChanged.connect(self.updateTotalBerat)
        self.ui.txtBrtM100.textChanged.connect(self.updateTotalBerat)
        self.ui.pushButton.clicked.connect(self.filter_records)
        self.ui.rbC.toggled.connect(self.warnacass)
        self.ui.rbCK.toggled.connect(self.warnacass)
        self.ui.rbCH.toggled.connect(self.warnacass)
        self.ui.rbCM.toggled.connect(self.warnacass)
        self.ui.rbInternal.toggled.connect(self.lab)
        self.ui.rbEksternal.toggled.connect(self.lab)
        self.ui.btnOk.clicked.connect(self.printToConsole)
        self.ui.txtBrtP48.textChanged.connect(self.enablingScrollP48)
        self.ui.txtBrtP100.textChanged.connect(self.enablingScrollP100)
        self.ui.txtBrtM100.textChanged.connect(self.enablingScrollM100)


    def setup_initial_records(self):
        self.records = []  # Inisialisasi records sebagai list kosong
        self.current_record_index = 0  # Inisialisasi current_record_index dengan nilai yang valid
        self.load_record(self.current_record_index)

        #set Date
        today = QDate.currentDate()
        one_month_ago = today.addMonths(-1)
        self.ui.tglDari.setDate(one_month_ago)
        self.ui.tglSampai.setDate(today)

        # disabling scroll area
        self.ui.scrollArea_P48.setEnabled(False)
        self.ui.scrollArea_P100.setEnabled(False)
        self.ui.scrollArea_M100.setEnabled(False)

        # Set up button connections
        self.ui.btnPrev.clicked.connect(self.load_previous_record)
        self.ui.btnNext.clicked.connect(self.load_next_record)

        # Load the initial record
        self.current_record_index = 0
        self.load_record(self.current_record_index)


        # Create a connection to the local SQL Server database
    def database_connection(self):
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

    def lab(self):
        internal = self.ui.rbInternal.isChecked()
        eksternal = self.ui.rbEksternal.isChecked()
        return internal,eksternal

    def warnacass(self):
        kecokelatan = self.ui.rbC.isChecked()
        cokelat_kemerahan = self.ui.rbCM.isChecked()
        cokelat_kehitaman = self.ui.rbCH.isChecked()
        cokelat_kekuningan = self.ui.rbCK.isChecked()

        return kecokelatan,cokelat_kemerahan,cokelat_kehitaman,cokelat_kekuningan

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
                self.ui.txtSiteID.setText(str(record[1]))
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


    def enablingScrollP48(self,text):
        if text and text != "0":
            self.ui.scrollArea_P48.setEnabled(True)
        else:
            self.ui.scrollArea_P48.setEnabled(False)

    def enablingScrollP100(self,text):
        if text and text != "0":
            self.ui.scrollArea_P100.setEnabled(True)
        else:
            self.ui.scrollArea_P100.setEnabled(False)

    def enablingScrollM100(self,text):
        if text and text != "0":
            self.ui.scrollArea_M100.setEnabled(True)
        else:
            self.ui.scrollArea_M100.setEnabled(False)



    def format_date_time(date_time):
        return f"{date_time:%Y-%m-%d %H:%M:%S}"

    def mineralValueP48(self):
        mineral1 = self.ui.cbM1.currentText()
        mineral2 = self.ui.cbM2.currentText()
        mineral3 = self.ui.cbM3.currentText()
        mineral4 = self.ui.cbM4.currentText()
        mineral5 = self.ui.cbM5.currentText()
        mineral6 = self.ui.cbM6.currentText()
        mineral7 = self.ui.cbM7.currentText()
        mineral8 = self.ui.cbM8.currentText()
        mineral9 = self.ui.cbM9.currentText()
        mineral10 = self.ui.cbM10.currentText()
        mineral11 = self.ui.cbM11.currentText()
        mineral12 = self.ui.cbM12.currentText()
        mineral13 = self.ui.cbM13.currentText()
        mineral14 = self.ui.cbM14.currentText()
        mineral15 = self.ui.cbM15.currentText()
        mineral16 = self.ui.cbM16.currentText()
        mineral17 = self.ui.cbM17.currentText()
        mineral18 = self.ui.cbM18.currentText()
        mineral19 = self.ui.cbM19.currentText()
        butir1 = self.ui.leM01.currentText()
        butir2 = self.ui.leM02.currentText()
        butir3 = self.ui.leM03.currentText()
        butir4 = self.ui.leM04.currentText()
        butir5 = self.ui.leM05.currentText()
        butir6 = self.ui.leM06.currentText()
        butir7 = self.ui.leM07.currentText()
        butir8 = self.ui.leM08.currentText()
        butir9 = self.ui.leM09.currentText()
        butir10 = self.ui.leM10.currentText()
        butir11 = self.ui.leM11.currentText()
        butir12 = self.ui.leM12.currentText()
        butir13 = self.ui.leM13.currentText()
        butir14 = self.ui.leM14.currentText()
        butir15 = self.ui.leM15.currentText()
        butir16 = self.ui.leM16.currentText()
        butir17 = self.ui.leM17.currentText()
        butir18 = self.ui.leM18.currentText()
        butir19 = self.ui.leM19.currentText()


    def printToConsole(self):
        mineral1 = self.ui.cbM1.currentText()
        mineral2 = self.ui.cbM2.currentText()
        asal = self.ui.txtAsal.text()
        siteid = self.ui.txtSiteID.text()
        btrM1 = self.ui.leM01.text()
        btrM2 = self.ui.leM02.text()
        lapis = self.ui.txtLapis.text()
        date_inserted = self.format_date_time(datetime())


        warna_values = self.warnacass()
        kecokelatan,cokelat_kemerahan,cokelat_kehitaman,cokelat_kekuningan = warna_values
        if kecokelatan:
            print("Kecokelatan")
        if cokelat_kemerahan:
            print("Cokelat Kemerahan")
        if cokelat_kehitaman:
            print("Cokelat Kehitaman")
        if cokelat_kekuningan:
            print("Cokelat Kekuningan")


        checkboxes = [
            ("Angular", self.ui.cbA.isChecked()),
            ("Sub Angular", self.ui.cbSA.isChecked()),
            ("Rounded", self.ui.cbR.isChecked()),
            ("Well Rounded", self.ui.cbWR.isChecked()),
            ("Sub Rounded", self.ui.cbSR.isChecked()),
            ("Sub Angular - Sub Rounded", self.ui.cbSASR.isChecked())
        ]
        for label, checked in checkboxes:
            if checked:
                print(f"Checkbox '{label}' terpilih.")

        print("Mineral 1:", mineral1)
        print("Mineral 2:", mineral2)
        print("Asal:", asal)
        print("Sample ID:", siteid)
        print("Jumlah Butir Mineral 1:", btrM1)

        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Icon.Question)
        confirm_dialog.setWindowTitle("Konfirmasi")
        confirm_dialog.setText("Apakah Anda yakin ingin melanjutkan?")
        confirm_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        confirm_dialog.setDefaultButton(QMessageBox.StandardButton.No)

        result = confirm_dialog.exec()

        if result == QMessageBox.StandardButton.Yes:
            # Lanjutkan dengan tindakan setelah konfirmasi
            sample_id = f"{siteid}-{lapis}"  # Gabungkan SITE_ID dan lapis di sini

            query = (
                f"INSERT INTO GB_GCA_RESULT (PROJECT, SITE_ID, SAMPLE_ID, LAB_ID, MINERAL, PLUS_48_GRAIN, DATE_INSERTED) "
                f"VALUES ('TIMAH', ?, ?, 'INTERNAL', ?, ?)"
            )

            try:
                self.db_cursor.execute(query, (siteid, sample_id, mineral1, btrM1))
                self.db_connection.commit()
                print("Data berhasil dimasukkan ke dalam tabel GB_GCA_RESULT.")
            except Exception as e:
                print("Error saat memasukkan data:", e)
        else:
            print("Tindakan dibatalkan.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())