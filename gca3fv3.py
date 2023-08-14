import datetime

from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import QDate
import pyodbc
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 796)


        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 821, 771))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.mainGroup = QtWidgets.QGroupBox(parent=self.groupBox)
        self.mainGroup.setGeometry(QtCore.QRect(10, 140, 801, 661))
        self.mainGroup.setTitle("")
        self.mainGroup.setObjectName("mainGroup")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.mainGroup)
        self.groupBox_5.setGeometry(QtCore.QRect(360, 280, 350, 341))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.groupBox_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName("gridLayout")
        self.cbSR = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.cbSR.setObjectName("cbSR")
        self.gridLayout.addWidget(self.cbSR, 2, 1, 1, 1)
        self.cbSA = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.cbSA.setObjectName("cbSA")
        self.gridLayout.addWidget(self.cbSA, 1, 1, 1, 1)
        self.cbA = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.cbA.setObjectName("cbA")
        self.gridLayout.addWidget(self.cbA, 1, 0, 1, 1)
        self.cbR = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.cbR.setObjectName("cbR")
        self.gridLayout.addWidget(self.cbR, 2, 0, 1, 1)
        self.cbWR = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.cbWR.setObjectName("cbWR")
        self.gridLayout.addWidget(self.cbWR, 3, 0, 1, 1)
        self.cbSASR = QtWidgets.QCheckBox(parent=self.groupBox_6)
        self.cbSASR.setObjectName("cbSASR")
        self.gridLayout.addWidget(self.cbSASR, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.groupBox_5)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbCH = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.rbCH.setObjectName("rbCH")
        self.verticalLayout_2.addWidget(self.rbCH)
        self.rbCM = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.rbCM.setObjectName("rbCM")
        self.verticalLayout_2.addWidget(self.rbCM)
        self.rbCK = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.rbCK.setObjectName("rbCK")
        self.verticalLayout_2.addWidget(self.rbCK)
        self.rbC = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.rbC.setObjectName("rbC")
        self.verticalLayout_2.addWidget(self.rbC)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.btnOk = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.mainGroup)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 30, 243, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.txtBrtP48 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtBrtP48.setObjectName("txtBrtP48")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtP48)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.txtBrtP100 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtBrtP100.setObjectName("txtBrtP100")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtP100)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.txtBrtM100 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtBrtM100.setObjectName("txtBrtM100")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtM100)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.txtTotBrt = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.txtTotBrt.setEnabled(False)
        self.txtTotBrt.setObjectName("txtTotBrt")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtTotBrt)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.mainGroup)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 280, 341, 341))
        self.groupBox_4.setObjectName("groupBox_4")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox_4)
        self.scrollArea.setGeometry(QtCore.QRect(15, 59, 291, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 272, 512))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_5 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_5.setObjectName("formLayout_5")
        self.cbM1 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM1.setObjectName("cbM1")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM1)
        self.leM01 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM01.setObjectName("leM01")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM01)
        self.cbM2 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM2.setObjectName("cbM2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM2)
        self.leM02 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM02.setObjectName("leM02")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM02)
        self.cbM3 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM3.setObjectName("cbM3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM3)
        self.leM03 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM03.setObjectName("leM03")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM03)
        self.cbM4 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM4.setObjectName("cbM4")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM4)
        self.leM04 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM04.setObjectName("leM04")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM04)
        self.cbM5 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM5.setObjectName("cbM5")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM5)
        self.leM05 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM05.setObjectName("leM05")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM05)
        self.leM06 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM06.setObjectName("leM06")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM06)
        self.cbM7 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM7.setObjectName("cbM7")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM7)
        self.leM07 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM07.setObjectName("leM07")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM07)
        self.cbM8 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM8.setObjectName("cbM8")
        self.formLayout_5.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM8)
        self.leM08 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM08.setObjectName("leM08")
        self.formLayout_5.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM08)
        self.cbM9 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM9.setObjectName("cbM9")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM9)
        self.leM09 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM09.setObjectName("leM09")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM09)
        self.cbM10 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM10.setObjectName("cbM10")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM10)
        self.leM10 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM10.setObjectName("leM10")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM10)
        self.cbM11 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM11.setObjectName("cbM11")
        self.formLayout_5.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM11)
        self.leM11 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM11.setObjectName("leM11")
        self.formLayout_5.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM11)
        self.cbM12 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM12.setObjectName("cbM12")
        self.formLayout_5.setWidget(12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM12)
        self.leM12 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM12.setObjectName("leM12")
        self.formLayout_5.setWidget(12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM12)
        self.cbM13 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM13.setObjectName("cbM13")
        self.formLayout_5.setWidget(13, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM13)
        self.leM13 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM13.setObjectName("leM13")
        self.formLayout_5.setWidget(13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM13)
        self.cbM14 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM14.setObjectName("cbM14")
        self.formLayout_5.setWidget(14, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM14)
        self.leM14 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM14.setObjectName("leM14")
        self.formLayout_5.setWidget(14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM14)
        self.cbM15 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM15.setObjectName("cbM15")
        self.formLayout_5.setWidget(15, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM15)
        self.leM15 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM15.setObjectName("leM15")
        self.formLayout_5.setWidget(15, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM15)
        self.cbM16 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM16.setObjectName("cbM16")
        self.formLayout_5.setWidget(16, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM16)
        self.leM16 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM16.setObjectName("leM16")
        self.formLayout_5.setWidget(16, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM16)
        self.cbM17 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM17.setObjectName("cbM17")
        self.formLayout_5.setWidget(17, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM17)
        self.leM17 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM17.setObjectName("leM17")
        self.formLayout_5.setWidget(17, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM17)
        self.cbM18 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM18.setObjectName("cbM18")
        self.formLayout_5.setWidget(18, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM18)
        self.leM18 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM18.setObjectName("leM18")
        self.formLayout_5.setWidget(18, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM18)
        self.cbM19 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM19.setObjectName("cbM19")
        self.formLayout_5.setWidget(19, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM19)
        self.leM19 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM19.setObjectName("leM19")
        self.formLayout_5.setWidget(19, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM19)
        self.cbM6 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM6.setObjectName("cbM6")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(70, 30, 44, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(180, 30, 75, 16))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.mainGroup)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 341, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.txtAsal = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtAsal.setEnabled(False)
        self.txtAsal.setObjectName("txtAsal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAsal)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txtLok = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtLok.setEnabled(False)
        self.txtLok.setObjectName("txtLok")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLok)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtSiteID = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtSiteID.setEnabled(False)
        self.txtSiteID.setObjectName("txtSiteID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtSiteID)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtLapis = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtLapis.setEnabled(False)
        self.txtLapis.setObjectName("txtLapis")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLapis)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtBulan = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBulan.setEnabled(False)
        self.txtBulan.setObjectName("txtBulan")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBulan)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.txtBrtTbg = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtTbg.setEnabled(False)
        self.txtBrtTbg.setObjectName("txtBrtTbg")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtTbg)
        self.btnPrev = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnPrev.setObjectName("btnPrev")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.btnPrev)
        self.btnNext = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnNext.setObjectName("btnNext")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btnNext)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 10, 191, 121))
        self.groupBox_8.setObjectName("groupBox_8")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_8)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.tglDari = QtWidgets.QDateEdit(parent=self.groupBox_8)
        self.tglDari.setCalendarPopup(True)
        self.tglDari.setObjectName("tglDari")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tglDari)
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_8)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)
        self.tglSampai = QtWidgets.QDateEdit(parent=self.groupBox_8)
        self.tglSampai.setCalendarPopup(True)
        self.tglSampai.setObjectName("tglSampai")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tglSampai)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.txtBrtP48.textChanged.connect(self.updateTotalBerat)
        self.txtBrtP100.textChanged.connect(self.updateTotalBerat)
        self.txtBrtM100.textChanged.connect(self.updateTotalBerat)

        mineral_options = [
            "Cassiterite", "Monazite", "Pyrit/Marc", "Ilmenite",
            "Zircon", "Xenotime", "Anatase", "Limonite",
            "Topaz", "Tourmaline", "Siderite", "Magnetite",
            "Spinel", "Oksida Besi", "Lp.Pasir", "Quartz"
        ]
        combo_boxes = [self.cbM1, self.cbM2, self.cbM3, self.cbM4, self.cbM5, self.cbM6, self.cbM7, self.cbM8, self.cbM9, self.cbM10, self.cbM11, self.cbM12, self.cbM13, self.cbM14, self.cbM15, self.cbM16, self.cbM17, self.cbM18, self.cbM19]


        for cb in combo_boxes:
            cb.addItem("")  # Default empty item
            cb.addItems(mineral_options)


        MainWindow.setStatusBar(self.statusbar)

        # Inisialisasi tanggal pada form
        today = QDate.currentDate()
        one_month_ago = today.addMonths(-1)
        self.tglDari.setDate(one_month_ago)
        self.tglSampai.setDate(today)

        # Hubungkan tombol OK dengan fungsi filter_records
        self.pushButton.clicked.connect(self.filter_records)

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
        self.btnPrev.clicked.connect(self.load_previous_record)
        self.btnNext.clicked.connect(self.load_next_record)

        # Load the initial record
        self.current_record_index = 0
        self.load_record(self.current_record_index)

    # Fungsi untuk menghitung dan memperbarui total berat
    def updateTotalBerat(self):
        try:
            berat_p48 = float(self.txtBrtP48.text() or 0)
            berat_p100 = float(self.txtBrtP100.text() or 0)
            berat_m100 = float(self.txtBrtM100.text() or 0)
            total_berat = berat_p48 + berat_p100 + berat_m100
            self.txtTotBrt.setText(str(total_berat))
        except ValueError:
            self.txtTotBrt.setText("")

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
                self.txtSiteID.setText(str(record[2]))
                self.txtLapis.setText(str(record[4]))
                self.txtBrtTbg.setText(str(record[10]))
                self.txtBulan.setText(str(record[5]))
                self.txtLok.setText(str(record[8]))
                self.txtAsal.setText(str(record[7]))
        else:
            self.txtSiteID.clear()
            self.txtLapis.clear()
            self.txtBrtTbg.clear()
            self.txtBulan.clear()
            self.txtLok.clear()
            self.txtAsal.clear()

    def filter_records(self):
        tgl_dari = self.tglDari.date()
        tgl_sampai = self.tglSampai.date()

        tgl_dari_datetime = datetime.datetime(tgl_dari.year(), tgl_dari.month(), tgl_dari.day())
        tgl_sampai_datetime = datetime.datetime(tgl_sampai.year(), tgl_sampai.month(), tgl_sampai.day())

        if tgl_dari_datetime > tgl_sampai_datetime:
            QMessageBox.critical(self.centralwidget, "Error", "Tanggal Dari harus lebih awal dari Tanggal Sampai")
            return


        query = "SELECT * FROM GB_GCA_SAMPLE WHERE SAMPLE_DATE BETWEEN ? AND ?"
        self.db_cursor.execute(query, (tgl_dari_datetime, tgl_sampai_datetime))
        records = self.db_cursor.fetchall()

        if records:
            self.current_record_index = 0
            self.records = records
            self.load_record(self.current_record_index)
        else:
            QMessageBox.information(self.centralwidget, "Info", "Tidak ada data yang cocok dengan filter tanggal")


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



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.clicked.connect(self.filter_records)
        self.groupBox_5.setTitle(_translate("MainWindow", "Karakter Cassiterite"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Bentuk Butir"))
        self.cbSR.setText(_translate("MainWindow", "Sub Rounded"))
        self.cbSA.setText(_translate("MainWindow", "Sub Angular"))
        self.cbA.setText(_translate("MainWindow", "Angular"))
        self.cbR.setText(_translate("MainWindow", "Rounded"))
        self.cbWR.setText(_translate("MainWindow", "Well Rounded"))
        self.cbSASR.setText(_translate("MainWindow", "Sub Angular - Sub Rounded"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Warna"))
        self.rbCH.setText(_translate("MainWindow", "Cokelat Kehitaman"))
        self.rbCM.setText(_translate("MainWindow", "Cokelat Kemerahan"))
        self.rbCK.setText(_translate("MainWindow", "Cokelat Kekuningan"))
        self.rbC.setText(_translate("MainWindow", "Kecokelatan"))
        self.btnOk.setText(_translate("MainWindow", "OK"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Berat Sampel (gr)"))
        self.label_7.setText(_translate("MainWindow", "#+48"))
        self.label_8.setText(_translate("MainWindow", "#+100"))
        self.label_9.setText(_translate("MainWindow", "#-100"))
        self.label_10.setText(_translate("MainWindow", "Berat Total"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Analisa Multi Mineral"))
        self.label_11.setText(_translate("MainWindow", "Mineral"))
        self.label_12.setText(_translate("MainWindow", "Jumlah Butir"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Informasi Sampel"))
        self.label.setText(_translate("MainWindow", "Asal Conto"))
        self.label_2.setText(_translate("MainWindow", "Lokasi"))
        self.label_3.setText(_translate("MainWindow", "Site ID"))
        self.label_4.setText(_translate("MainWindow", "Lapis"))
        self.label_5.setText(_translate("MainWindow", "Bulan/Tahun"))
        self.label_6.setText(_translate("MainWindow", "Berat Timbang"))
        self.btnPrev.setText(_translate("MainWindow", "Prev"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Filter"))
        self.label_13.setText(_translate("MainWindow", "Dari"))
        self.label_14.setText(_translate("MainWindow", "Sampai"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

        self.btnOk.clicked.connect(self.printToConsole)


    def printToConsole(self):
        mineral1 = self.cbM1.currentText()
        mineral2 = self.cbM2.currentText()
        asal = self.txtAsal.text()
        sampleid = self.txtSiteID.text()
        btrM1 = self.leM01.text()

        hasil = f"{sampleid} {mineral1} {btrM1} butir dari {asal}"
        print("mineral 1", mineral1,btrM1,"butir")
        print("mineral 2", mineral2)
        print("asal", asal)
        print("sample id", sampleid)
        print(hasil)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
