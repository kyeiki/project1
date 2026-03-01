# BAB 24: Settings
# =================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLineEdit, QCheckBox, QSpinBox,
                              QComboBox, QPushButton, QLabel,
                              QVBoxLayout, QWidget, QFormLayout)
from PyQt5.QtCore import QSettings

class SettingsDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 400)
        
        # QSettings menyimpan ke registry (Windows) atau file config (Linux/Mac)
        self.settings = QSettings("MyCompany", "MyApp")
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("⚙️ PENGATURAN APLIKASI")
        header.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(header)
        
        layout.addWidget(QLabel("Pengaturan akan tersimpan secara otomatis\ndan dimuat saat aplikasi dibuka kembali."))
        
        # Form
        form = QFormLayout()
        
        # Username
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Masukkan username")
        form.addRow("Username:", self.input_username)
        
        # Email
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("email@contoh.com")
        form.addRow("Email:", self.input_email)
        
        # Theme
        self.combo_theme = QComboBox()
        self.combo_theme.addItems(["Light", "Dark", "System"])
        form.addRow("Theme:", self.combo_theme)
        
        # Font size
        self.spin_fontsize = QSpinBox()
        self.spin_fontsize.setRange(8, 32)
        self.spin_fontsize.setValue(12)
        form.addRow("Font Size:", self.spin_fontsize)
        
        # Remember me
        self.cb_remember = QCheckBox("Ingat saya")
        form.addRow("", self.cb_remember)
        
        # Notifications
        self.cb_notify = QCheckBox("Aktifkan notifikasi")
        self.cb_notify.setChecked(True)
        form.addRow("", self.cb_notify)
        
        layout.addLayout(form)
        
        # Buttons
        btn_layout = QVBoxLayout()
        
        btn_save = QPushButton("💾 Simpan Pengaturan")
        btn_save.setStyleSheet("background-color: #27ae60; color: white; padding: 10px;")
        btn_save.clicked.connect(self.save_settings)
        btn_layout.addWidget(btn_save)
        
        btn_load = QPushButton("📂 Muat Pengaturan")
        btn_load.setStyleSheet("background-color: #3498db; color: white; padding: 10px;")
        btn_load.clicked.connect(self.load_settings)
        btn_layout.addWidget(btn_load)
        
        btn_clear = QPushButton("🗑️ Hapus Semua Pengaturan")
        btn_clear.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px;")
        btn_clear.clicked.connect(self.clear_settings)
        btn_layout.addWidget(btn_clear)
        
        layout.addLayout(btn_layout)
        
        # Status
        self.status = QLabel("")
        self.status.setStyleSheet("padding: 10px; background: #f0f0f0;")
        layout.addWidget(self.status)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Auto load saat startup
        self.load_settings()
    
    def save_settings(self):
        self.settings.setValue("username", self.input_username.text())
        self.settings.setValue("email", self.input_email.text())
        self.settings.setValue("theme", self.combo_theme.currentText())
        self.settings.setValue("fontsize", self.spin_fontsize.value())
        self.settings.setValue("remember", self.cb_remember.isChecked())
        self.settings.setValue("notify", self.cb_notify.isChecked())
        
        self.status.setText("✅ Pengaturan berhasil disimpan!")
        print(f"Settings saved to: {self.settings.fileName()}")
    
    def load_settings(self):
        username = self.settings.value("username", "", type=str)
        email = self.settings.value("email", "", type=str)
        theme = self.settings.value("theme", "Light", type=str)
        fontsize = self.settings.value("fontsize", 12, type=int)
        remember = self.settings.value("remember", False, type=bool)
        notify = self.settings.value("notify", True, type=bool)
        
        self.input_username.setText(username)
        self.input_email.setText(email)
        
        index = self.combo_theme.findText(theme)
        if index >= 0:
            self.combo_theme.setCurrentIndex(index)
        
        self.spin_fontsize.setValue(fontsize)
        self.cb_remember.setChecked(remember)
        self.cb_notify.setChecked(notify)
        
        self.status.setText("✅ Pengaturan berhasil dimuat!")
    
    def clear_settings(self):
        self.settings.clear()
        
        # Reset form
        self.input_username.clear()
        self.input_email.clear()
        self.combo_theme.setCurrentIndex(0)
        self.spin_fontsize.setValue(12)
        self.cb_remember.setChecked(False)
        self.cb_notify.setChecked(True)
        
        self.status.setText("🗑️ Semua pengaturan telah dihapus!")

app = QApplication(sys.argv)
window = SettingsDemo()
window.show()
sys.exit(app.exec_())
