# BAB 2: Kepingan Pertama - Jendela Kosong
# ================================
# Ini adalah baseplate kita - fondasi untuk semua aplikasi PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jendela Pertamaku - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)  # x, y, lebar, tinggi

# Baris-baris ini SELALU ada di setiap aplikasi PyQt5
app = QApplication(sys.argv)  # Membuat aplikasi
jendela = JendelaKu()          # Membuat jendela
jendela.show()                 # Menampilkan jendela
sys.exit(app.exec_())          # Memulai event loop
