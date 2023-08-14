from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contoh Aplikasi")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.labelM1 = QLabel("Mineral 1:")
        self.cbM1 = QComboBox()
        self.cbM1.addItem("Pilihan 1")
        self.cbM1.addItem("Pilihan 2")
        self.cbM1.addItem("Pilihan 3")

        self.labelM2 = QLabel("Mineral 2:")
        self.cbM2 = QComboBox()
        self.cbM2.addItem("Pilihan 1")
        self.cbM2.addItem("Pilihan 2")
        self.cbM2.addItem("Pilihan 3")

        self.btnOk = QPushButton("OK")
        self.btnOk.clicked.connect(self.printToConsole)  # Menghubungkan ke fungsi printToConsole

        layout.addWidget(self.labelM1)
        layout.addWidget(self.cbM1)
        layout.addWidget(self.labelM2)
        layout.addWidget(self.cbM2)
        layout.addWidget(self.btnOk)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def printToConsole(self):
        mineral1 = self.cbM1.currentText()  # Menggunakan currentText() untuk mendapatkan teks terpilih
        mineral2 = self.cbM2.currentText()

        print("Mineral 1:", mineral1)
        print("Mineral 2:", mineral2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
