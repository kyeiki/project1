# BAB 10: Styling - Mewarnai Karya Anda
# =====================================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLineEdit, QLabel, QPushButton,
                              QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class FormStylish(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Stylish - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 400)
        
        # === GLOBAL STYLESHEET ===
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #EA6689, stop:1 #4BA29F);
            }
            QLabel {
                color: white;
                font-size: 14px;
                font-weight: bold;
            }
            QLabel#title {
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
            QLineEdit {
                padding: 12px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 10px;
                font-size: 14px;
                background-color: rgba(255, 255, 255, 0.9);
            }
            QLineEdit:focus {
                border: 2px solid white;
                background-color: white;
            }
            QPushButton {
                padding: 15px;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton#register {
                background-color: #e74c3c;
                color: white;
            }
            QPushButton#register:hover {
                background-color: #c0392b;
            }
            QPushButton#register:pressed {
                background-color: #a93226;
            }
            QPushButton#login {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: 2px solid white;
            }
            QPushButton#login:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("🚀 CREATE ACCOUNT")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        layout.addSpacing(20)
        
        # Username
        layout.addWidget(QLabel("Username"))
        self.username = QLineEdit()
        self.username.setPlaceholderText("Masukkan username")
        layout.addWidget(self.username)
        
        # Email
        layout.addWidget(QLabel("Email"))
        self.email = QLineEdit()
        self.email.setPlaceholderText("email@contoh.com")
        layout.addWidget(self.email)
        
        # Password
        layout.addWidget(QLabel("Password"))
        self.password = QLineEdit()
        self.password.setPlaceholderText("Masukkan password")
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)
        
        # Confirm Password
        layout.addWidget(QLabel("Confirm Password"))
        self.confirm = QLineEdit()
        self.confirm.setPlaceholderText("Konfirmasi password")
        self.confirm.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm)
        
        layout.addSpacing(20)
        
        # Buttons
        btn_register = QPushButton("REGISTER")
        btn_register.setObjectName("register")
        btn_register.clicked.connect(self.register)
        layout.addWidget(btn_register)
        
        btn_login = QPushButton("Sudah punya akun? Login")
        btn_login.setObjectName("login")
        layout.addWidget(btn_login)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def register(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()
        confirm = self.confirm.text()
        
        if not username or not email or not password:
            self.statusBar().showMessage("⚠️ Semua field wajib diisi!")
            return
        
        if password != confirm:
            self.statusBar().showMessage("⚠️ Password tidak cocok!")
            return
        
        self.statusBar().showMessage("✅ Registrasi berhasil!")

app = QApplication(sys.argv)
jendela = FormStylish()
jendela.show()
sys.exit(app.exec_())
