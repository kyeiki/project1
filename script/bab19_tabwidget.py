# BAB 19: Tab Widget
# ===================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTabWidget, QWidget, QLabel, QLineEdit,
                              QTextEdit, QPushButton, QSpinBox,
                              QVBoxLayout, QHBoxLayout, QFormLayout)
from PyQt5.QtCore import Qt

class TabApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 400)
        
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(False)
        self.setCentralWidget(self.tabs)
        
        # Tab 1: Home
        self.create_home_tab()
        
        # Tab 2: Calculator
        self.create_calc_tab()
        
        # Tab 3: Notes
        self.create_notes_tab()
        
        # Tab 4: Settings
        self.create_settings_tab()
    
    def create_home_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("🏠 WELCOME")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        info = QLabel("Ini adalah aplikasi demo Tab Widget.\n\nKlik tab di atas untuk berpindah halaman.")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Home")
    
    def create_calc_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("🔢 KALKULATOR SEDERHANA")
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(label)
        
        form = QFormLayout()
        
        self.input_a = QSpinBox()
        self.input_a.setRange(-10000, 10000)
        form.addRow("Angka 1:", self.input_a)
        
        self.input_b = QSpinBox()
        self.input_b.setRange(-10000, 10000)
        form.addRow("Angka 2:", self.input_b)
        
        layout.addLayout(form)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        btn_add = QPushButton("+")
        btn_add.clicked.connect(lambda: self.calculate("+"))
        btn_layout.addWidget(btn_add)
        
        btn_sub = QPushButton("-")
        btn_sub.clicked.connect(lambda: self.calculate("-"))
        btn_layout.addWidget(btn_sub)
        
        btn_mul = QPushButton("×")
        btn_mul.clicked.connect(lambda: self.calculate("*"))
        btn_layout.addWidget(btn_mul)
        
        btn_div = QPushButton("÷")
        btn_div.clicked.connect(lambda: self.calculate("/"))
        btn_layout.addWidget(btn_div)
        
        layout.addLayout(btn_layout)
        
        self.result = QLabel("Hasil: -")
        self.result.setStyleSheet("font-size: 20px; font-weight: bold; color: #27ae60;")
        layout.addWidget(self.result)
        
        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Calculator")
    
    def create_notes_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("📝 CATATAN")
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(label)
        
        self.notes = QTextEdit()
        self.notes.setPlaceholderText("Tulis catatan di sini...")
        layout.addWidget(self.notes)
        
        btn_layout = QHBoxLayout()
        
        btn_clear = QPushButton("Clear")
        btn_clear.clicked.connect(self.notes.clear)
        btn_layout.addWidget(btn_clear)
        
        btn_copy = QPushButton("Copy All")
        btn_copy.clicked.connect(lambda: self.notes.selectAll())
        btn_layout.addWidget(btn_copy)
        
        layout.addLayout(btn_layout)
        
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Notes")
    
    def create_settings_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("⚙️ PENGATURAN")
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(label)
        
        form = QFormLayout()
        
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Nama Anda")
        form.addRow("Nama:", self.input_name)
        
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("email@contoh.com")
        form.addRow("Email:", self.input_email)
        
        layout.addLayout(form)
        
        btn_save = QPushButton("Simpan Pengaturan")
        btn_save.clicked.connect(self.save_settings)
        layout.addWidget(btn_save)
        
        self.status = QLabel("")
        layout.addWidget(self.status)
        
        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Settings")
    
    def calculate(self, op):
        a = self.input_a.value()
        b = self.input_b.value()
        
        try:
            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b if b != 0 else "Error: Div by 0"
            
            self.result.setText(f"Hasil: {result}")
        except Exception as e:
            self.result.setText(f"Error: {e}")
    
    def save_settings(self):
        name = self.input_name.text()
        email = self.input_email.text()
        self.status.setText(f"✅ Tersimpan! Nama: {name}, Email: {email}")

app = QApplication(sys.argv)
window = TabApp()
window.show()
sys.exit(app.exec_())
