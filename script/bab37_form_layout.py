# BAB 37: Form Layout
# ====================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QWidget, QLabel, QLineEdit, 
                              QSpinBox, QDoubleSpinBox, QComboBox,
                              QCheckBox, QDateEdit, QTextEdit,
                              QPushButton, QFormLayout, QVBoxLayout,
                              QGroupBox, QMessageBox)
from PyQt5.QtCore import Qt, QDate

class FormLayoutDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 600)
        
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Header
        header = QLabel("📝 FORM LAYOUT")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        # Personal Info Group
        group_personal = QGroupBox("Informasi Pribadi")
        form_personal = QFormLayout()
        
        # Name
        self.name = QLineEdit()
        self.name.setPlaceholderText("Nama lengkap")
        form_personal.addRow("Nama:", self.name)
        
        # Email
        self.email = QLineEdit()
        self.email.setPlaceholderText("email@contoh.com")
        form_personal.addRow("Email:", self.email)
        
        # Phone
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("08xxxxxxxxxx")
        form_personal.addRow("Telepon:", self.phone)
        
        # Gender
        self.gender = QComboBox()
        self.gender.addItems(["Laki-laki", "Perempuan"])
        form_personal.addRow("Jenis Kelamin:", self.gender)
        
        # Birth Date
        self.birthdate = QDateEdit()
        self.birthdate.setCalendarPopup(True)
        self.birthdate.setDate(QDate(2000, 1, 1))
        self.birthdate.setDisplayFormat("dd/MM/yyyy")
        form_personal.addRow("Tanggal Lahir:", self.birthdate)
        
        group_personal.setLayout(form_personal)
        main_layout.addWidget(group_personal)
        
        # Address Group
        group_address = QGroupBox("Alamat")
        form_address = QFormLayout()
        
        # Street
        self.street = QLineEdit()
        self.street.setPlaceholderText("Nama jalan dan nomor")
        form_address.addRow("Jalan:", self.street)
        
        # City
        self.city = QComboBox()
        self.city.addItems(["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Lainnya"])
        self.city.setEditable(True)
        form_address.addRow("Kota:", self.city)
        
        # Postal Code
        self.postal = QSpinBox()
        self.postal.setRange(10000, 99999)
        self.postal.setPrefix("Kode Pos: ")
        form_address.addRow("", self.postal)
        
        # Full Address
        self.full_address = QTextEdit()
        self.full_address.setPlaceholderText("Alamat lengkap...")
        self.full_address.setMaximumHeight(80)
        form_address.addRow("Alamat Lengkap:", self.full_address)
        
        group_address.setLayout(form_address)
        main_layout.addWidget(group_address)
        
        # Preferences Group
        group_prefs = QGroupBox("Preferensi")
        form_prefs = QFormLayout()
        
        # Experience
        self.experience = QSpinBox()
        self.experience.setRange(0, 50)
        self.experience.setSuffix(" tahun")
        form_prefs.addRow("Pengalaman:", self.experience)
        
        # Expected Salary
        self.salary = QDoubleSpinBox()
        self.salary.setRange(0, 1000000000)
        self.salary.setPrefix("Rp ")
        self.salary.setDecimals(0)
        self.salary.setSingleStep(1000000)
        form_prefs.addRow("Gaji yang Diharapkan:", self.salary)
        
        # Agreement
        self.agree = QCheckBox("Saya setuju dengan syarat dan ketentuan")
        form_prefs.addRow("", self.agree)
        
        # Newsletter
        self.newsletter = QCheckBox("Berlangganan newsletter")
        self.newsletter.setChecked(True)
        form_prefs.addRow("", self.newsletter)
        
        group_prefs.setLayout(form_prefs)
        main_layout.addWidget(group_prefs)
        
        # Buttons
        btn_layout = QVBoxLayout()
        
        btn_submit = QPushButton("📝 Submit")
        btn_submit.setStyleSheet("background-color: #27ae60; color: white; padding: 15px; font-size: 14px;")
        btn_submit.clicked.connect(self.submit_form)
        btn_layout.addWidget(btn_submit)
        
        btn_clear = QPushButton("🗑️ Clear Form")
        btn_clear.clicked.connect(self.clear_form)
        btn_layout.addWidget(btn_clear)
        
        main_layout.addLayout(btn_layout)
        
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
    
    def submit_form(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "Error", "Nama harus diisi!")
            return
        
        if not self.email.text().strip():
            QMessageBox.warning(self, "Error", "Email harus diisi!")
            return
        
        if not self.agree.isChecked():
            QMessageBox.warning(self, "Error", "Anda harus menyetujui syarat dan ketentuan!")
            return
        
        # Success
        data = f"""
Nama: {self.name.text()}
Email: {self.email.text()}
Telepon: {self.phone.text()}
Gender: {self.gender.currentText()}
Tanggal Lahir: {self.birthdate.text()}
Kota: {self.city.currentText()}
Pengalaman: {self.experience.value()} tahun
Gaji: Rp {self.salary.value():,.0f}
Newsletter: {'Ya' if self.newsletter.isChecked() else 'Tidak'}
        """
        
        QMessageBox.information(self, "Data Submitted", f"Data berhasil disimpan!{data}")
    
    def clear_form(self):
        self.name.clear()
        self.email.clear()
        self.phone.clear()
        self.gender.setCurrentIndex(0)
        self.birthdate.setDate(QDate(2000, 1, 1))
        self.street.clear()
        self.city.setCurrentIndex(0)
        self.postal.setValue(10000)
        self.full_address.clear()
        self.experience.setValue(0)
        self.salary.setValue(0)
        self.agree.setChecked(False)
        self.newsletter.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormLayoutDemo()
    window.show()
    sys.exit(app.exec_())
