# BAB 4: Tombol Interaktif
# ========================

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tombol dengan Aksi - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)
        
        # Tombol 1 - Sapa
        tombol1 = QPushButton("Klik Aku!", self)
        tombol1.move(150, 80)
        tombol1.resize(100, 40)
        tombol1.clicked.connect(self.tombol_diklik)
        
        # Tombol 2 - Info
        tombol2 = QPushButton("Info", self)
        tombol2.move(150, 130)
        tombol2.resize(100, 40)
        tombol2.clicked.connect(self.tampilkan_info)
        
        # Tombol 3 - Keluar
        tombol3 = QPushButton("Keluar", self)
        tombol3.move(150, 180)
        tombol3.resize(100, 40)
        tombol3.setStyleSheet("background-color: #e74c3c; color: white;")
        tombol3.clicked.connect(self.close)
    
    def tombol_diklik(self):
        QMessageBox.information(self, "Info", "Tombol berhasil diklik!")
    
    def tampilkan_info(self):
        QMessageBox.about(self, "Tentang", "Aplikasi Demo PyQt5\nVersi 1.0")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
