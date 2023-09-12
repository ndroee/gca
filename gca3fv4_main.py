import datetime
import sys
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import QDate
import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets
from gca3fv4_ui import Ui_MainWindow



class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.records = None
        self.current_record_index = None
        self.db_cursor = None
        self.db_connection = None
        self.sample_id = None
        self.lab_id = None
        self.project = None
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

        self.ui.btnOk.clicked.connect(self.printToConsole)

        self.ui.txtBrtP48.textChanged.connect(self.enablingScrollP48)
        self.ui.txtBrtP100.textChanged.connect(self.enablingScrollP100)
        self.ui.txtBrtM100.textChanged.connect(self.enablingScrollM100)
        # List semua nama objek combobox yang ingin Anda hubungkan dengan metode toggleLineEdit
        combobox_names = [
                             f'cbM{i}_P48' for i in range(1, 20)] + [
                             f'cbM{i}_P100' for i in range(1, 20)] + [
                             f'cbM{i}_M100' for i in range(1, 20)]

        # Loop melalui daftar nama objek combobox dan menghubungkan sinyal ke metode toggleLineEdit
        for combobox_name in combobox_names:
            combobox = getattr(self.ui, combobox_name)
            combobox.currentTextChanged.connect(self.toggleLineEdit)


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

        # Nonaktifkan objek teks awal
        self.ui.txtBrtP48.setEnabled(False)
        self.ui.txtBrtP100.setEnabled(False)
        self.ui.txtBrtM100.setEnabled(False)

        widgets_to_disable = [
            self.ui.leM1_P48, self.ui.leM2_P48, self.ui.leM3_P48, self.ui.leM4_P48, self.ui.leM5_P48, self.ui.leM6_P48,
            self.ui.leM7_P48, self.ui.leM8_P48, self.ui.leM9_P48, self.ui.leM10_P48, self.ui.leM11_P48, self.ui.leM12_P48,
            self.ui.leM13_P48, self.ui.leM14_P48, self.ui.leM15_P48, self.ui.leM16_P48, self.ui.leM17_P48, self.ui.leM18_P48,
            self.ui.leM19_P48, self.ui.leM1_P100, self.ui.leM2_P100, self.ui.leM3_P100, self.ui.leM4_P100,
            self.ui.leM5_P100, self.ui.leM6_P100, self.ui.leM7_P100, self.ui.leM8_P100, self.ui.leM9_P100,
            self.ui.leM10_P100, self.ui.leM11_P100, self.ui.leM12_P100, self.ui.leM13_P100, self.ui.leM14_P100,
            self.ui.leM15_P100, self.ui.leM16_P100, self.ui.leM17_P100, self.ui.leM18_P100, self.ui.leM19_P100,
            self.ui.leM1_M100, self.ui.leM2_M100, self.ui.leM3_M100, self.ui.leM4_M100, self.ui.leM5_M100,
            self.ui.leM6_M100, self.ui.leM7_M100, self.ui.leM8_M100, self.ui.leM9_M100, self.ui.leM10_M100,
            self.ui.leM11_M100, self.ui.leM12_M100, self.ui.leM13_M100, self.ui.leM14_M100, self.ui.leM15_M100,
            self.ui.leM16_M100, self.ui.leM17_M100, self.ui.leM18_M100, self.ui.leM19_M100
        ]

        for widget in widgets_to_disable:
            widget.setEnabled(False)


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
            if self.ui.txtTotBrt.text() and self.ui.txtBrtTbg.text():
                txt_tot_brt = float(self.ui.txtTotBrt.text())
                txt_brt_tbg = float(self.ui.txtBrtTbg.text())

                selisih_persen = ((txt_tot_brt - txt_brt_tbg) / txt_brt_tbg) * 100

                # Menentukan teks yang akan ditampilkan di QLabel 'validation'
                if abs(selisih_persen) >= 10:
                    self.ui.validation.setText("WARNING: Selisih lebih dari 10%!")
                    self.ui.validation.setStyleSheet("color: blue; background-color : red")
                else:
                    self.ui.validation.setText("OK")
                    self.ui.validation.setStyleSheet("color: white; background-color : green")

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
                self.sample_id = str(record[2])
                self.lab_id = str(record[3])
                self.project = str(record[0])
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
            self.ui.txtBrtP48.setEnabled(True)
            self.ui.txtBrtP100.setEnabled(True)
            self.ui.txtBrtM100.setEnabled(True)
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

    def toggleLineEdit(self):
        comboboxes = [
            self.ui.cbM1_P48, self.ui.cbM2_P48, self.ui.cbM3_P48, self.ui.cbM4_P48,
            self.ui.cbM5_P48, self.ui.cbM6_P48, self.ui.cbM7_P48, self.ui.cbM8_P48,
            self.ui.cbM9_P48, self.ui.cbM10_P48, self.ui.cbM11_P48, self.ui.cbM12_P48,
            self.ui.cbM13_P48, self.ui.cbM14_P48, self.ui.cbM15_P48, self.ui.cbM16_P48,
            self.ui.cbM17_P48, self.ui.cbM18_P48, self.ui.cbM19_P48,self.ui.cbM1_P100,
            self.ui.cbM2_P100, self.ui.cbM3_P100, self.ui.cbM4_P100,
            self.ui.cbM5_P100, self.ui.cbM6_P100, self.ui.cbM7_P100, self.ui.cbM8_P100,
            self.ui.cbM9_P100, self.ui.cbM10_P100, self.ui.cbM11_P100, self.ui.cbM12_P100,
            self.ui.cbM13_P100, self.ui.cbM14_P100, self.ui.cbM15_P100, self.ui.cbM16_P100,
            self.ui.cbM17_P100, self.ui.cbM18_P100, self.ui.cbM19_P100,self.ui.cbM1_M100,
            self.ui.cbM2_M100, self.ui.cbM3_M100, self.ui.cbM4_M100,
            self.ui.cbM5_M100, self.ui.cbM6_M100, self.ui.cbM7_M100, self.ui.cbM8_M100,
            self.ui.cbM9_M100, self.ui.cbM10_M100, self.ui.cbM11_M100, self.ui.cbM12_M100,
            self.ui.cbM13_M100, self.ui.cbM14_M100, self.ui.cbM15_M100, self.ui.cbM16_M100,
            self.ui.cbM17_M100, self.ui.cbM18_M100, self.ui.cbM19_M100
        ]

        lineedits = [
            self.ui.leM1_P48, self.ui.leM2_P48, self.ui.leM3_P48, self.ui.leM4_P48,
            self.ui.leM5_P48, self.ui.leM6_P48, self.ui.leM7_P48, self.ui.leM8_P48,
            self.ui.leM9_P48, self.ui.leM10_P48, self.ui.leM11_P48, self.ui.leM12_P48,
            self.ui.leM13_P48, self.ui.leM14_P48, self.ui.leM15_P48, self.ui.leM16_P48,
            self.ui.leM17_P48, self.ui.leM18_P48, self.ui.leM19_P48,
            self.ui.leM1_P100, self.ui.leM2_P100, self.ui.leM3_P100, self.ui.leM4_P100,
            self.ui.leM5_P100, self.ui.leM6_P100, self.ui.leM7_P100, self.ui.leM8_P100,
            self.ui.leM9_P100, self.ui.leM10_P100, self.ui.leM11_P100, self.ui.leM12_P100,
            self.ui.leM13_P100, self.ui.leM14_P100, self.ui.leM15_P100, self.ui.leM16_P100,
            self.ui.leM17_P100, self.ui.leM18_P100, self.ui.leM19_P100,
            self.ui.leM1_M100, self.ui.leM2_M100, self.ui.leM3_M100, self.ui.leM4_M100,
            self.ui.leM5_M100, self.ui.leM6_M100, self.ui.leM7_M100, self.ui.leM8_M100,
            self.ui.leM9_M100, self.ui.leM10_M100, self.ui.leM11_M100, self.ui.leM12_M100,
            self.ui.leM13_M100, self.ui.leM14_M100, self.ui.leM15_M100, self.ui.leM16_M100,
            self.ui.leM17_M100, self.ui.leM18_M100, self.ui.leM19_M100,
        ]


        for i, combobox in enumerate(comboboxes):
            if not combobox.currentText():
                lineedits[i].setEnabled(False)
                lineedits[i].clear()
            else:
                lineedits[i].setEnabled(True)


    def mineralValueP48(self):
        mineral1P48 = self.ui.cbM1_P48.currentText()
        mineral2P48 = self.ui.cbM2_P48.currentText()
        mineral3P48 = self.ui.cbM3_P48.currentText()
        mineral4P48 = self.ui.cbM4_P48.currentText()
        mineral5P48 = self.ui.cbM5_P48.currentText()
        mineral6P48 = self.ui.cbM6_P48.currentText()
        mineral7P48 = self.ui.cbM7_P48.currentText()
        mineral8P48 = self.ui.cbM8_P48.currentText()
        mineral9P48 = self.ui.cbM9_P48.currentText()
        mineral10P48 = self.ui.cbM10_P48.currentText()
        mineral11P48 = self.ui.cbM11_P48.currentText()
        mineral12P48 = self.ui.cbM12_P48.currentText()
        mineral13P48 = self.ui.cbM13_P48.currentText()
        mineral14P48 = self.ui.cbM14_P48.currentText()
        mineral15P48 = self.ui.cbM15_P48.currentText()
        mineral16P48 = self.ui.cbM16_P48.currentText()
        mineral17P48 = self.ui.cbM17_P48.currentText()
        mineral18P48 = self.ui.cbM18_P48.currentText()
        mineral19P48 = self.ui.cbM19_P48.currentText()
        butir1P48 = self.ui.leM1_P48.text()
        butir2P48 = self.ui.leM2_P48.text()
        butir3P48 = self.ui.leM3_P48.text()
        butir4P48 = self.ui.leM4_P48.text()
        butir5P48 = self.ui.leM5_P48.text()
        butir6P48 = self.ui.leM6_P48.text()
        butir7P48 = self.ui.leM7_P48.text()
        butir8P48 = self.ui.leM8_P48.text()
        butir9P48 = self.ui.leM9_P48.text()
        butir10P48 = self.ui.leM10_P48.text()
        butir11P48 = self.ui.leM11_P48.text()
        butir12P48 = self.ui.leM12_P48.text()
        butir13P48 = self.ui.leM13_P48.text()
        butir14P48 = self.ui.leM14_P48.text()
        butir15P48 = self.ui.leM15_P48.text()
        butir16P48 = self.ui.leM16_P48.text()
        butir17P48 = self.ui.leM17_P48.text()
        butir18P48 = self.ui.leM18_P48.text()
        butir19P48 = self.ui.leM19_P48.text()

        return (
            mineral1P48 ,mineral2P48 ,mineral3P48 ,
            mineral4P48 ,mineral5P48 ,mineral6P48 ,
            mineral7P48 ,mineral8P48 ,mineral9P48 ,
            mineral10P48 ,mineral11P48 ,mineral12P48 ,
            mineral13P48 ,mineral14P48 ,mineral15P48 ,
            mineral16P48 ,mineral17P48 ,mineral18P48 ,
            mineral19P48 ,
            butir1P48 ,butir2P48 ,butir3P48 ,
            butir4P48 ,butir5P48 ,butir6P48 ,
            butir7P48 ,butir8P48 ,butir9P48 ,
            butir10P48 ,butir11P48 ,butir12P48 ,
            butir13P48 ,butir14P48 ,butir15P48 ,
            butir16P48 ,butir17P48 ,butir18P48 ,
            butir19P48
        )
    def mineralValueP100(self):
        mineral1P100 = self.ui.cbM1_P100.currentText()
        mineral2P100 = self.ui.cbM2_P100.currentText()
        mineral3P100 = self.ui.cbM3_P100.currentText()
        mineral4P100 = self.ui.cbM4_P100.currentText()
        mineral5P100 = self.ui.cbM5_P100.currentText()
        mineral6P100 = self.ui.cbM6_P100.currentText()
        mineral7P100 = self.ui.cbM7_P100.currentText()
        mineral8P100 = self.ui.cbM8_P100.currentText()
        mineral9P100 = self.ui.cbM9_P100.currentText()
        mineral10P100 = self.ui.cbM10_P100.currentText()
        mineral11P100 = self.ui.cbM11_P100.currentText()
        mineral12P100 = self.ui.cbM12_P100.currentText()
        mineral13P100 = self.ui.cbM13_P100.currentText()
        mineral14P100 = self.ui.cbM14_P100.currentText()
        mineral15P100 = self.ui.cbM15_P100.currentText()
        mineral16P100 = self.ui.cbM16_P100.currentText()
        mineral17P100 = self.ui.cbM17_P100.currentText()
        mineral18P100 = self.ui.cbM18_P100.currentText()
        mineral19P100 = self.ui.cbM19_P100.currentText()
        butir1P100 = self.ui.leM1_P100.text()
        butir2P100 = self.ui.leM2_P100.text()
        butir3P100 = self.ui.leM3_P100.text()
        butir4P100 = self.ui.leM4_P100.text()
        butir5P100 = self.ui.leM5_P100.text()
        butir6P100 = self.ui.leM6_P100.text()
        butir7P100 = self.ui.leM7_P100.text()
        butir8P100 = self.ui.leM8_P100.text()
        butir9P100 = self.ui.leM9_P100.text()
        butir10P100 = self.ui.leM10_P100.text()
        butir11P100 = self.ui.leM11_P100.text()
        butir12P100 = self.ui.leM12_P100.text()
        butir13P100 = self.ui.leM13_P100.text()
        butir14P100 = self.ui.leM14_P100.text()
        butir15P100 = self.ui.leM15_P100.text()
        butir16P100 = self.ui.leM16_P100.text()
        butir17P100 = self.ui.leM17_P100.text()
        butir18P100 = self.ui.leM18_P100.text()
        butir19P100 = self.ui.leM19_P100.text()

        return (
            mineral1P100 ,mineral2P100 ,mineral3P100 ,
            mineral4P100 ,mineral5P100 ,mineral6P100 ,
            mineral7P100 ,mineral8P100 ,mineral9P100 ,
            mineral10P100 ,mineral11P100 ,mineral12P100 ,
            mineral13P100 ,mineral14P100 ,mineral15P100 ,
            mineral16P100 ,mineral17P100 ,mineral18P100 ,
            mineral19P100 ,
            butir1P100 ,butir2P100 ,butir3P100 ,
            butir4P100 ,butir5P100 ,butir6P100 ,
            butir7P100 ,butir8P100 ,butir9P100 ,
            butir10P100 ,butir11P100 ,butir12P100 ,
            butir13P100 ,butir14P100 ,butir15P100 ,
            butir16P100 ,butir17P100 ,butir18P100 ,
            butir19P100
        )

    def mineralValueM100(self):
        mineral1M100 = self.ui.cbM1_M100.currentText()
        mineral2M100 = self.ui.cbM2_M100.currentText()
        mineral3M100 = self.ui.cbM3_M100.currentText()
        mineral4M100 = self.ui.cbM4_M100.currentText()
        mineral5M100 = self.ui.cbM5_M100.currentText()
        mineral6M100 = self.ui.cbM6_M100.currentText()
        mineral7M100 = self.ui.cbM7_M100.currentText()
        mineral8M100 = self.ui.cbM8_M100.currentText()
        mineral9M100 = self.ui.cbM9_M100.currentText()
        mineral10M100 = self.ui.cbM10_M100.currentText()
        mineral11M100 = self.ui.cbM11_M100.currentText()
        mineral12M100 = self.ui.cbM12_M100.currentText()
        mineral13M100 = self.ui.cbM13_M100.currentText()
        mineral14M100 = self.ui.cbM14_M100.currentText()
        mineral15M100 = self.ui.cbM15_M100.currentText()
        mineral16M100 = self.ui.cbM16_M100.currentText()
        mineral17M100 = self.ui.cbM17_M100.currentText()
        mineral18M100 = self.ui.cbM18_M100.currentText()
        mineral19M100 = self.ui.cbM19_M100.currentText()
        butir1M100 = self.ui.leM1_M100.text()
        butir2M100 = self.ui.leM2_M100.text()
        butir3M100 = self.ui.leM3_M100.text()
        butir4M100 = self.ui.leM4_M100.text()
        butir5M100 = self.ui.leM5_M100.text()
        butir6M100 = self.ui.leM6_M100.text()
        butir7M100 = self.ui.leM7_M100.text()
        butir8M100 = self.ui.leM8_M100.text()
        butir9M100 = self.ui.leM9_M100.text()
        butir10M100 = self.ui.leM10_M100.text()
        butir11M100 = self.ui.leM11_M100.text()
        butir12M100 = self.ui.leM12_M100.text()
        butir13M100 = self.ui.leM13_M100.text()
        butir14M100 = self.ui.leM14_M100.text()
        butir15M100 = self.ui.leM15_M100.text()
        butir16M100 = self.ui.leM16_M100.text()
        butir17M100 = self.ui.leM17_M100.text()
        butir18M100 = self.ui.leM18_M100.text()
        butir19M100 = self.ui.leM19_M100.text()

        return (
            mineral1M100 ,mineral2M100 ,mineral3M100 ,
            mineral4M100 ,mineral5M100 ,mineral6M100 ,
            mineral7M100 ,mineral8M100 ,mineral9M100 ,
            mineral10M100 ,mineral11M100 ,mineral12M100 ,
            mineral13M100 ,mineral14M100 ,mineral15M100 ,
            mineral16M100 ,mineral17M100 ,mineral18M100 ,
            mineral19M100 ,
            butir1M100 ,butir2M100 ,butir3M100 ,
            butir4M100 ,butir5M100 ,butir6M100 ,
            butir7M100 ,butir8M100 ,butir9M100 ,
            butir10M100 ,butir11M100 ,butir12M100 ,
            butir13M100 ,butir14M100 ,butir15M100 ,
            butir16M100 ,butir17M100 ,butir18M100 ,
            butir19M100
        )

    def printToConsole(self):
        date_inserted = datetime.date.today()
        print(date_inserted)
        project = self.project
        site_id  = self.ui.txtSiteID.text()
        lapis = self.ui.txtLapis.text()
        sample_id = self.sample_id
        lab_id = self.lab_id
        # Fungsi untuk mencetak nilai mineral dan butir
        def print_mineral_butir(values, prefix):
            num_minerals = 19
            for i in range(1, num_minerals + 1):
                mineral_var = values[i - 1]
                butir_var = values[i + num_minerals - 1]
                if mineral_var or butir_var:
                    print(f"{prefix}-{i}: {mineral_var} - butir{i}: {butir_var}")

        # Cetak nilai dari mineralValueP48
        valuesP48 = self.mineralValueP48()
        print_mineral_butir(valuesP48, "mineralP48")

        # Cetak nilai dari mineralValueP100
        valuesP100 = self.mineralValueP100()
        print_mineral_butir(valuesP100, "mineralP100")

        # Cetak nilai dari mineralValueM100
        valuesM100 = self.mineralValueM100()
        print_mineral_butir(valuesM100, "mineralM100")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())