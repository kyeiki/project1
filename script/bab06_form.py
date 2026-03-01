# BAB 6: Input Pengguna - Formulir Sederhana
# ==========================================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLineEdit, QLabel, QPushButton,
                              QVBoxLayout, QWidget, QMessageBox)

class FormRegistrasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Registrasi - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 350, 300)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Judul
        judul = QLabel("📝 FORM REGISTRASI")
        judul.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
        layout.addWidget(judul)
        
        # Nama
        layout.addWidget(QLabel("Nama:"))
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Nama lengkap")
        layout.addWidget(self.input_nama)
        
        # Email
        layout.addWidget(QLabel("Email:"))
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("email@contoh.com")
        layout.addWidget(self.input_email)
        
        # Telepon
        layout.addWidget(QLabel("Telepon:"))
        self.input_telepon = QLineEdit()
        self.input_telepon.setPlaceholderText("08xxxxxxxxxx")
        layout.addWidget(self.input_telepon)
        
        # Spacer
        layout.addSpacing(10)
        
        # Tombol
        tombol = QPushButton("DAFTAR")
        tombol.setStyleSheet("""
            QPushButton {
                background-color: #27ae60; 
                color: white; 
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        tombol.clicked.connect(self.daftar)
        layout.addWidget(tombol)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def daftar(self):
        nama = self.input_nama.text()
        email = self.input_email.text()
        telepon = self.input_telepon.text()
        
        if not nama or not email:
            QMessageBox.warning(self, "Peringatan", "Nama dan Email wajib diisi!")
            return
        
        pesan = f"Pendaftaran berhasil!\n\nNama: {nama}\nEmail: {email}\nTelepon: {telepon}"
        QMessageBox.information(self, "Sukses", pesan)

app = QApplication(sys.argv)
jendela = FormRegistrasi()
jendela.show()
sys.exit(app.exec_())
