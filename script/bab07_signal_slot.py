# BAB 7: Signal & Slot - Menghubungkan Kepingan
# =============================================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLineEdit, QLabel, QPushButton,
                              QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal & Slot Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Label instruksi
        instruksi = QLabel("Ketik nama Anda, lalu klik Sapa atau tekan Enter:")
        layout.addWidget(instruksi)
        
        # Input
        self.input = QLineEdit()
        self.input.setPlaceholderText("Ketik nama Anda...")
        layout.addWidget(self.input)
        
        # Label untuk menampilkan salam
        self.label_salam = QLabel("Halo, ...")
        self.label_salam.setStyleSheet("font-size: 24px; color: #2c3e50;")
        self.label_salam.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_salam)
        
        # Tombol
        self.tombol = QPushButton("Sapa!")
        self.tombol.setStyleSheet("padding: 15px; font-size: 16px;")
        layout.addWidget(self.tombol)
        
        # Label status
        self.status = QLabel("Status: Menunggu...")
        self.status.setStyleSheet("color: gray; font-style: italic;")
        layout.addWidget(self.status)
        
        # === MENGHUBUNGKAN SIGNAL DENGAN SLOT ===
        
        # Signal: textChanged -> dipicu setiap kali teks berubah
        self.input.textChanged.connect(self.nama_berubah)
        
        # Signal: returnPressed -> dipicu ketika Enter ditekan
        self.input.returnPressed.connect(self.sapa)
        
        # Signal: clicked -> dipicu ketika tombol diklik
        self.tombol.clicked.connect(self.sapa)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def nama_berubah(self, teks):
        """Slot: dipanggil ketika teks berubah"""
        self.status.setText(f"Status: Mengetik '{teks}'")
    
    def sapa(self):
        """Slot: dipanggil ketika tombol diklik atau Enter ditekan"""
        nama = self.input.text()
        if nama:
            self.label_salam.setText(f"Halo, {nama}! 👋")
            self.status.setText("Status: Sudah disapa!")
        else:
            self.label_salam.setText("Halo, ...")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
