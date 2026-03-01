# BAB 3: Menambah Label - Jendela yang Bicara
# ============================================

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label Kustom - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)
        
        # Membuat label dengan styling
        label = QLabel("Halo, PyQt5!")
        label.setAlignment(Qt.AlignCenter)  # Teks di tengah
        label.setFont(QFont("Arial", 24, QFont.Bold))
        label.setStyleSheet("color: blue; background-color: #f0f0f0;")
        
        # Set sebagai widget utama
        self.setCentralWidget(label)

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
