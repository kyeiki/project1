# BAB 38: Validator
# =================
# Input validation dengan QValidator

import sys
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QWidget, QLabel, QLineEdit, 
                              QPushButton, QVBoxLayout, QFormLayout,
                              QGroupBox)
from PyQt5.QtCore import Qt, QRegularExpression
from PyQt5.QtGui import QValidator, QIntValidator, QDoubleValidator, QRegularExpressionValidator


class EmailValidator(QValidator):
    """Custom validator untuk email"""
    
    def validate(self, input_str, pos):
        # Simple email regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not input_str:
            return (QValidator.Intermediate, input_str, pos)
        
        if re.match(pattern, input_str):
            return (QValidator.Acceptable, input_str, pos)
        else:
            return (QValidator.Intermediate, input_str, pos)
    
    def fixup(self, input_str):
        return input_str.lower()


class PhoneValidator(QValidator):
    """Custom validator untuk nomor telepon Indonesia"""
    
    def validate(self, input_str, pos):
        # Format: 08xxxxxxxxxx (10-13 digit)
        pattern = r'^08[0-9]{0,11}$'
        
        if not input_str:
            return (QValidator.Intermediate, input_str, pos)
        
        if re.match(pattern, input_str) and len(input_str) >= 10:
            return (QValidator.Acceptable, input_str, pos)
        elif re.match(pattern, input_str):
            return (QValidator.Intermediate, input_str, pos)
        else:
            return (QValidator.Invalid, input_str, pos)


class ValidatorDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validator Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 500)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("✅ INPUT VALIDATOR")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        info = QLabel("Validator membatasi input yang bisa dimasukkan user")
        info.setStyleSheet("color: gray;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # Integer validation
        group_int = QGroupBox("Integer Validator (QIntValidator)")
        form_int = QFormLayout()
        
        self.int_input = QLineEdit()
        self.int_input.setPlaceholderText("Hanya angka 0-100")
        
        # Set validator
        int_validator = QIntValidator(0, 100)
        self.int_input.setValidator(int_validator)
        
        form_int.addRow("Angka (0-100):", self.int_input)
        
        self.int_status = QLabel("Status: -")
        form_int.addRow("", self.int_status)
        
        self.int_input.textChanged.connect(self.check_int)
        group_int.setLayout(form_int)
        layout.addWidget(group_int)
        
        # Double validation
        group_double = QGroupBox("Double Validator (QDoubleValidator)")
        form_double = QFormLayout()
        
        self.double_input = QLineEdit()
        self.double_input.setPlaceholderText("Angka desimal 0.0 - 1000.0")
        
        # Set validator
        double_validator = QDoubleValidator(0.0, 1000.0, 2)  # 2 decimal places
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        self.double_input.setValidator(double_validator)
        
        form_double.addRow("Harga (0-1000):", self.double_input)
        
        self.double_status = QLabel("Status: -")
        form_double.addRow("", self.double_status)
        
        self.double_input.textChanged.connect(self.check_double)
        group_double.setLayout(form_double)
        layout.addWidget(group_double)
        
        # Email validation
        group_email = QGroupBox("Custom Email Validator")
        form_email = QFormLayout()
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("email@contoh.com")
        self.email_input.setValidator(EmailValidator())
        
        form_email.addRow("Email:", self.email_input)
        
        self.email_status = QLabel("Status: -")
        form_email.addRow("", self.email_status)
        
        self.email_input.textChanged.connect(self.check_email)
        group_email.setLayout(form_email)
        layout.addWidget(group_email)
        
        # Phone validation
        group_phone = QGroupBox("Custom Phone Validator (Indonesia)")
        form_phone = QFormLayout()
        
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("08xxxxxxxxxx")
        self.phone_input.setValidator(PhoneValidator())
        
        form_phone.addRow("Telepon:", self.phone_input)
        
        self.phone_status = QLabel("Status: -")
        form_phone.addRow("", self.phone_status)
        
        self.phone_input.textChanged.connect(self.check_phone)
        group_phone.setLayout(form_phone)
        layout.addWidget(group_phone)
        
        # Regex validation
        group_regex = QGroupBox("Regex Validator (Kode Produk: ABC-123)")
        form_regex = QFormLayout()
        
        self.regex_input = QLineEdit()
        self.regex_input.setPlaceholderText("Format: ABC-123")
        
        # Regex: 3 huruf besar, strip, 3 digit
        regex = QRegularExpression(r'^[A-Z]{0,3}-?[0-9]{0,3}$')
        self.regex_input.setValidator(QRegularExpressionValidator(regex))
        
        form_regex.addRow("Kode Produk:", self.regex_input)
        
        self.regex_status = QLabel("Status: -")
        form_regex.addRow("", self.regex_status)
        
        self.regex_input.textChanged.connect(self.check_regex)
        group_regex.setLayout(form_regex)
        layout.addWidget(group_regex)
        
        # Submit button
        btn = QPushButton("Validate All")
        btn.setStyleSheet("padding: 15px;")
        btn.clicked.connect(self.validate_all)
        layout.addWidget(btn)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def get_status_color(self, validator, text):
        if not text:
            return "gray", "Empty"
        
        state, _, _ = validator.validate(text, 0)
        
        if state == QValidator.Acceptable:
            return "#27ae60", "✅ Valid"
        elif state == QValidator.Intermediate:
            return "#f39c12", "⏳ Incomplete"
        else:
            return "#e74c3c", "❌ Invalid"
    
    def check_int(self):
        validator = self.int_input.validator()
        color, status = self.get_status_color(validator, self.int_input.text())
        self.int_status.setStyleSheet(f"color: {color};")
        self.int_status.setText(f"Status: {status}")
    
    def check_double(self):
        validator = self.double_input.validator()
        color, status = self.get_status_color(validator, self.double_input.text())
        self.double_status.setStyleSheet(f"color: {color};")
        self.double_status.setText(f"Status: {status}")
    
    def check_email(self):
        validator = self.email_input.validator()
        color, status = self.get_status_color(validator, self.email_input.text())
        self.email_status.setStyleSheet(f"color: {color};")
        self.email_status.setText(f"Status: {status}")
    
    def check_phone(self):
        validator = self.phone_input.validator()
        color, status = self.get_status_color(validator, self.phone_input.text())
        self.phone_status.setStyleSheet(f"color: {color};")
        self.phone_status.setText(f"Status: {status}")
    
    def check_regex(self):
        validator = self.regex_input.validator()
        color, status = self.get_status_color(validator, self.regex_input.text())
        self.regex_status.setStyleSheet(f"color: {color};")
        self.regex_status.setText(f"Status: {status}")
    
    def validate_all(self):
        results = []
        
        for field, name in [
            (self.int_input, "Integer"),
            (self.double_input, "Double"),
            (self.email_input, "Email"),
            (self.phone_input, "Phone"),
            (self.regex_input, "Regex")
        ]:
            validator = field.validator()
            text = field.text()
            
            if validator:
                state, _, _ = validator.validate(text, 0)
                if state == QValidator.Acceptable:
                    results.append(f"✅ {name}: Valid")
                elif state == QValidator.Intermediate:
                    results.append(f"⏳ {name}: Incomplete")
                else:
                    results.append(f"❌ {name}: Invalid")
        
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(self, "Validation Results", "\n".join(results))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ValidatorDemo()
    window.show()
    sys.exit(app.exec_())
