import sys
import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QFileDialog, QGroupBox, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QFormLayout, QPushButton, QWidget
from openpyxl import Workbook




class Ui_FormGca3F(object):
    def setupUi(self, FormGca3F):
        FormGca3F.setObjectName("FormGca3F")
        FormGca3F.resize(787, 671)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/home_1946488.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FormGca3F.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 341, 251))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.txtAsal = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtAsal.setEnabled(False)
        self.txtAsal.setObjectName("txtAsal")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAsal)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txtLok = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtLok.setEnabled(False)
        self.txtLok.setObjectName("txtLok")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLok)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtSiteID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtSiteID.setEnabled(False)
        self.txtSiteID.setObjectName("txtSiteID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtSiteID)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtLapis = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtLapis.setEnabled(False)
        self.txtLapis.setObjectName("txtLapis")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLapis)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtBulan = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtBulan.setEnabled(False)
        self.txtBulan.setObjectName("txtBulan")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBulan)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.txtBrtTbg = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtBrtTbg.setEnabled(False)
        self.txtBrtTbg.setObjectName("txtBrtTbg")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtTbg)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.btnPrev = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnPrev.setObjectName("btnPrev")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.btnPrev)
        self.btnNext = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnNext.setObjectName("btnNext")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btnNext)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 140, 243, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.txtBrtP48 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtP48.setObjectName("txtBrtP48")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtP48)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.txtBrtP100 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtP100.setObjectName("txtBrtP100")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtP100)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.txtBrtM100 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtM100.setObjectName("txtBrtM100")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtM100)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.txtTotBrt = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtTotBrt.setEnabled(False)
        self.txtTotBrt.setObjectName("txtTotBrt")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtTotBrt)
        self.btnUpload = QtWidgets.QPushButton(parent=FormGca3F)
        self.btnUpload.setGeometry(QtCore.QRect(10, 50, 80, 26))
        self.btnUpload.setObjectName("btnUpload")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 320, 321, 341))
        self.groupBox_3.setObjectName("groupBox_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox_3)
        self.scrollArea.setGeometry(QtCore.QRect(15, 59, 291, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 274, 708))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_5 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_5.setObjectName("formLayout_5")
        self.cbM1 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM1.setObjectName("cbM1")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM1)
        self.leM1 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM1.setObjectName("leM1")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM1)
        self.cbM2 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM2.setObjectName("cbM2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM2)
        self.leM2 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM2.setObjectName("leM2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM2)
        self.cbM3 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM3.setObjectName("cbM3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM3)
        self.leM3 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM3.setObjectName("leM3")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM3)
        self.cbM4 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM4.setObjectName("cbM4")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM4)
        self.leM4 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM4.setObjectName("leM4")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM4)
        self.cbM5 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM5.setObjectName("cbM5")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM5)
        self.leM5 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM5.setObjectName("leM5")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM5)
        self.leM6 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM6.setObjectName("leM6")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM6)
        self.cbM7 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM7.setObjectName("cbM7")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM7)
        self.leM7 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM7.setObjectName("leM7")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM7)
        self.cbM8 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM8.setObjectName("cbM8")
        self.formLayout_5.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM8)
        self.leM8 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM8.setObjectName("leM8")
        self.formLayout_5.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM8)
        self.cbM9 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM9.setObjectName("cbM9")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM9)
        self.leM9 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM9.setObjectName("leM9")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM9)
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
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(70, 30, 44, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(180, 30, 75, 16))
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 320, 350, 341))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.cbSR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbSR.setObjectName("cbSR")
        self.gridLayout.addWidget(self.cbSR, 2, 1, 1, 1)
        self.cbSA = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbSA.setObjectName("cbSA")
        self.gridLayout.addWidget(self.cbSA, 1, 1, 1, 1)
        self.cbA = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbA.setObjectName("cbA")
        self.gridLayout.addWidget(self.cbA, 1, 0, 1, 1)
        self.cbR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbR.setObjectName("cbR")
        self.gridLayout.addWidget(self.cbR, 2, 0, 1, 1)
        self.cbWR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbWR.setObjectName("cbWR")
        self.gridLayout.addWidget(self.cbWR, 3, 0, 1, 1)
        self.cbSASR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbSASR.setObjectName("cbSASR")
        self.gridLayout.addWidget(self.cbSASR, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbCH = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbCH.setObjectName("rbCH")
        self.verticalLayout_2.addWidget(self.rbCH)
        self.rbCM = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbCM.setObjectName("rbCM")
        self.verticalLayout_2.addWidget(self.rbCM)
        self.rbCK = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbCK.setObjectName("rbCK")
        self.verticalLayout_2.addWidget(self.rbCK)
        self.rbC = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbC.setObjectName("rbC")
        self.verticalLayout_2.addWidget(self.rbC)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.btnOk = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk)

        self.retranslateUi(FormGca3F)
        QtCore.QMetaObject.connectSlotsByName(FormGca3F)

    def retranslateUi(self, FormGca3F):
        _translate = QtCore.QCoreApplication.translate
        FormGca3F.setWindowTitle(_translate("FormGca3F", "Form GCA 3 Fraksi"))
        self.groupBox.setTitle(_translate("FormGca3F", "Informasi Sampel"))
        self.label_2.setText(_translate("FormGca3F", "Lokasi"))
        self.label_3.setText(_translate("FormGca3F", "Site ID"))
        self.label_4.setText(_translate("FormGca3F", "Lapis"))
        self.label_5.setText(_translate("FormGca3F", "Bulan/Tahun"))
        self.label_6.setText(_translate("FormGca3F", "Berat Timbang"))
        self.label.setText(_translate("FormGca3F", "Asal Conto"))
        self.btnPrev.setText(_translate("FormGca3F", "Prev"))
        self.btnNext.setText(_translate("FormGca3F", "Next"))
        self.groupBox_2.setTitle(_translate("FormGca3F", "Berat Sampel (gr)"))
        self.label_7.setText(_translate("FormGca3F", "#+48"))
        self.label_8.setText(_translate("FormGca3F", "#+100"))
        self.label_9.setText(_translate("FormGca3F", "#-100"))
        self.label_10.setText(_translate("FormGca3F", "Berat Total"))
        self.btnUpload.setText(_translate("FormGca3F", "Upload"))
        self.groupBox_3.setTitle(_translate("FormGca3F", "Analisa Multi Mineral"))
        self.label_11.setText(_translate("FormGca3F", "Mineral"))
        self.label_12.setText(_translate("FormGca3F", "Jumlah Butir"))
        self.groupBox_4.setTitle(_translate("FormGca3F", "Karakter Cassiterite"))
        self.groupBox_5.setTitle(_translate("FormGca3F", "Bentuk Butir"))
        self.cbSR.setText(_translate("FormGca3F", "Sub Rounded"))
        self.cbSA.setText(_translate("FormGca3F", "Sub Angular"))
        self.cbA.setText(_translate("FormGca3F", "Angular"))
        self.cbR.setText(_translate("FormGca3F", "Rounded"))
        self.cbWR.setText(_translate("FormGca3F", "Well Rounded"))
        self.cbSASR.setText(_translate("FormGca3F", "Sub Angular - Sub Rounded"))
        self.groupBox_6.setTitle(_translate("FormGca3F", "Warna"))
        self.rbCH.setText(_translate("FormGca3F", "Cokelat Kehitaman"))
        self.rbCM.setText(_translate("FormGca3F", "Cokelat Kemerahan"))
        self.rbCK.setText(_translate("FormGca3F", "Cokelat Kekuningan"))
        self.rbC.setText(_translate("FormGca3F", "Kecokelatan"))
        self.btnOk.setText(_translate("FormGca3F", "OK"))


class SampleForm(QWidget):
    def save_to_excel(self):
        if self.data is not None:
            wb = Workbook()
            ws = wb.active

            header_row = ["Asal Conto", "Lokasi", "Site ID", "Lapis", "Bulan/Tahun", "Berat Timbang",
                          "#+48", "#+100", "#-100", "Berat Total", "Bentuk Butir", "Warna", "Mineral", "Jumlah"]
            ws.append(header_row)

            for row_index in range(len(self.data)):
                row_data = self.data.iloc[row_index]

                bentuk_butir = []
                if self.ui.cbA.isChecked():
                    bentuk_butir.append("Angular")
                if self.ui.cbR.isChecked():
                    bentuk_butir.append("Rounded")
                if self.ui.cbSA.isChecked():
                    bentuk_butir.append("Sub Angular")
                if self.ui.cbSR.isChecked():
                    bentuk_butir.append("Sub Rounded")
                if self.ui.cbWR.isChecked():
                    bentuk_butir.append("Well Rounded")
                if self.ui.cbSASR.isChecked():
                    bentuk_butir.append("Sub Angular - Sub Rounded")

                warna = ""
                if self.ui.rbCH.isChecked():
                    warna = "Cokelat Kehitaman"
                elif self.ui.rbCM.isChecked():
                    warna = "Cokelat Kemerahan"
                elif self.ui.rbCK.isChecked():
                    warna = "Cokelat Kekuningan"
                elif self.ui.rbC.isChecked():
                    warna = "Kecokelatan"

                mineral_values = [
                    self.ui.leM1.text(),
                    self.ui.leM2.text(),
                    self.ui.leM3.text(),
                    self.ui.leM4.text(),
                    self.ui.leM5.text(),
                    self.ui.leM6.text(),
                    self.ui.leM7.text(),
                    self.ui.leM8.text(),
                    self.ui.leM9.text(),
                    self.ui.leM10.text(),
                    self.ui.leM11.text(),
                    self.ui.leM12.text(),
                    self.ui.leM13.text(),
                    self.ui.leM14.text(),
                    self.ui.leM15.text(),
                    self.ui.leM16.text(),
                    self.ui.leM17.text(),
                    self.ui.leM18.text(),
                    self.ui.leM19.text(),
                ]

                # Ambil nama mineral yang tidak kosong beserta jumlahnya
                mineral_data = [(self.mineral_options[i], mineral_values[i]) for i in range(len(mineral_values)) if
                                mineral_values[i]]

                row_values = [
                    str(row_data["Asal Conto"]),
                    str(row_data["Lokasi"]),
                    str(row_data["Site ID"]),
                    str(row_data["Lapis"]),
                    str(row_data["Bulan/Tahun"]),
                    str(row_data["Berat Timbang"]),
                    str(self.ui.txtBrtP48.text()),
                    str(self.ui.txtBrtP100.text()),
                    str(self.ui.txtBrtM100.text()),
                    str(self.ui.txtTotBrt.text()),
                    ", ".join(bentuk_butir),
                    warna,
                    ", ".join([mineral[0] for mineral in mineral_data]),
                    ", ".join([mineral[1] for mineral in mineral_data]),
                ]
                ws.append(row_values)

            save_file_name, _ = QFileDialog.getSaveFileName(self, "Save Excel File", "",
                                                            "Excel Files (*.xlsx);;All Files (*)")
            if save_file_name:
                wb.save(save_file_name)

    def __init__(self):
        super().__init__()

        self.ui = Ui_FormGca3F()
        self.ui.setupUi(self)

        # Tambahkan koneksi untuk tombol OK
        self.ui.btnOk.clicked.connect(self.save_to_excel)

        self.current_row = 0
        self.data = None

        self.ui.btnUpload.clicked.connect(self.open_excel_file)
        self.ui.btnNext.clicked.connect(self.show_next_row)
        self.ui.btnPrev.clicked.connect(self.show_previous_row)

        self.ui.txtBrtP48.textChanged.connect(self.handle_input_changed)
        self.ui.txtBrtP100.textChanged.connect(self.handle_input_changed)
        self.ui.txtBrtM100.textChanged.connect(self.handle_input_changed)

        self.mineral_options = ['Cassiterite', 'Monazite', 'Pyrit/Marc', 'Ilmenite', 'Zircon', 'Xenotime', 'Anatase',
                                'Limonite', 'Topaz', 'Tourmaline', 'Siderite', 'Magnetite', 'Spinel', 'Oksida Besi',
                                'Lp.Pasir', 'Quartz']

        self.ui.cbM1.addItems(self.mineral_options)
        self.ui.cbM2.addItems(self.mineral_options)
        self.ui.cbM3.addItems(self.mineral_options)
        self.ui.cbM4.addItems(self.mineral_options)
        self.ui.cbM5.addItems(self.mineral_options)
        self.ui.cbM6.addItems(self.mineral_options)
        self.ui.cbM7.addItems(self.mineral_options)
        self.ui.cbM8.addItems(self.mineral_options)
        self.ui.cbM9.addItems(self.mineral_options)
        self.ui.cbM10.addItems(self.mineral_options)
        self.ui.cbM11.addItems(self.mineral_options)
        self.ui.cbM12.addItems(self.mineral_options)
        self.ui.cbM13.addItems(self.mineral_options)
        self.ui.cbM14.addItems(self.mineral_options)
        self.ui.cbM15.addItems(self.mineral_options)
        self.ui.cbM16.addItems(self.mineral_options)
        self.ui.cbM17.addItems(self.mineral_options)
        self.ui.cbM18.addItems(self.mineral_options)
        self.ui.cbM19.addItems(self.mineral_options)

        # Mengatur opsi default pada QComboBox
        self.default_combobox_text = "Pilih Mineral"
        self.ui.cbM1.setCurrentIndex(self.ui.cbM1.findText(self.default_combobox_text))
        self.ui.cbM2.setCurrentIndex(self.ui.cbM2.findText(self.default_combobox_text))
        self.ui.cbM3.setCurrentIndex(self.ui.cbM3.findText(self.default_combobox_text))
        self.ui.cbM4.setCurrentIndex(self.ui.cbM4.findText(self.default_combobox_text))
        self.ui.cbM5.setCurrentIndex(self.ui.cbM5.findText(self.default_combobox_text))
        self.ui.cbM6.setCurrentIndex(self.ui.cbM6.findText(self.default_combobox_text))
        self.ui.cbM7.setCurrentIndex(self.ui.cbM7.findText(self.default_combobox_text))
        self.ui.cbM8.setCurrentIndex(self.ui.cbM8.findText(self.default_combobox_text))
        self.ui.cbM9.setCurrentIndex(self.ui.cbM9.findText(self.default_combobox_text))
        self.ui.cbM10.setCurrentIndex(self.ui.cbM10.findText(self.default_combobox_text))
        self.ui.cbM11.setCurrentIndex(self.ui.cbM11.findText(self.default_combobox_text))
        self.ui.cbM12.setCurrentIndex(self.ui.cbM12.findText(self.default_combobox_text))
        self.ui.cbM13.setCurrentIndex(self.ui.cbM13.findText(self.default_combobox_text))
        self.ui.cbM14.setCurrentIndex(self.ui.cbM14.findText(self.default_combobox_text))
        self.ui.cbM15.setCurrentIndex(self.ui.cbM15.findText(self.default_combobox_text))
        self.ui.cbM16.setCurrentIndex(self.ui.cbM16.findText(self.default_combobox_text))
        self.ui.cbM17.setCurrentIndex(self.ui.cbM17.findText(self.default_combobox_text))
        self.ui.cbM18.setCurrentIndex(self.ui.cbM18.findText(self.default_combobox_text))
        self.ui.cbM19.setCurrentIndex(self.ui.cbM19.findText(self.default_combobox_text))

    def handle_input_changed(self):
        # Ambil nilai dari QLineEdit txtBrtP48, txtBrtP100, dan txtBrtM100
        brt_p48 = float(self.ui.txtBrtP48.text()) if self.ui.txtBrtP48.text() else 0
        brt_p100 = float(self.ui.txtBrtP100.text()) if self.ui.txtBrtP100.text() else 0
        brt_m100 = float(self.ui.txtBrtM100.text()) if self.ui.txtBrtM100.text() else 0

        # Hitung total berat dan set ke QLineEdit txtTotBrt
        total_berat = brt_p48 + brt_p100 + brt_m100
        self.ui.txtTotBrt.setText(str(total_berat))

    def open_excel_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            self.data = pd.read_excel(file_name)
            self.current_row = 0
            self.show_data_row(self.current_row)

    def show_data_row(self, row_index):
        if self.data is not None and 0 <= row_index < len(self.data):
            row_data = self.data.iloc[row_index]
            self.ui.txtAsal.setText(str(row_data["Asal Conto"]))
            self.ui.txtLok.setText(str(row_data["Lokasi"]))
            self.ui.txtSiteID.setText(str(row_data["Site ID"]))
            self.ui.txtLapis.setText(str(row_data["Lapis"]))
            self.ui.txtBulan.setText(str(row_data["Bulan/Tahun"]))
            self.ui.txtBrtTbg.setText(str(row_data["Berat Timbang"]))

    def show_next_row(self):
        if self.data is not None and self.current_row < len(self.data) - 1:
            self.current_row += 1
            self.show_data_row(self.current_row)

    def show_previous_row(self):
        if self.data is not None and self.current_row > 0:
            self.current_row -= 1
            self.show_data_row(self.current_row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SampleForm()
    window.show()
    sys.exit(app.exec())
