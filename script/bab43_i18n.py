# BAB 43: Internationalization (i18n)
# ====================================
# Multi-language support

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QPushButton, QLineEdit,
                              QComboBox, QVBoxLayout, QWidget,
                              QFormLayout, QGroupBox)
from PyQt5.QtCore import Qt, QTranslator, QLocale

class Translator:
    """Simple translator class"""
    
    translations = {
        "en": {
            "title": "Internationalization Demo - Politeknik Negeri Bandung M Rizqi S",
            "language": "Language:",
            "welcome": "Welcome to the App!",
            "name": "Name:",
            "email": "Email:",
            "submit": "Submit",
            "cancel": "Cancel",
            "greeting": "Hello, {name}!",
            "info": "This app supports multiple languages."
        },
        "id": {
            "title": "Demo Internasionalisasi",
            "language": "Bahasa:",
            "welcome": "Selamat datang di Aplikasi!",
            "name": "Nama:",
            "email": "Email:",
            "submit": "Kirim",
            "cancel": "Batal",
            "greeting": "Halo, {name}!",
            "info": "Aplikasi ini mendukung banyak bahasa."
        },
        "ja": {
            "title": "国際化デモ",
            "language": "言語：",
            "welcome": "アプリへようこそ！",
            "name": "名前：",
            "email": "メール：",
            "submit": "送信",
            "cancel": "キャンセル",
            "greeting": "こんにちは、{name}さん！",
            "info": "このアプリは多言語をサポートしています。"
        },
        "zh": {
            "title": "国际化演示",
            "language": "语言：",
            "welcome": "欢迎使用本应用！",
            "name": "姓名：",
            "email": "邮箱：",
            "submit": "提交",
            "cancel": "取消",
            "greeting": "你好，{name}！",
            "info": "此应用支持多种语言。"
        }
    }
    
    def __init__(self, lang="en"):
        self.lang = lang
    
    def set_language(self, lang):
        self.lang = lang
    
    def tr(self, key, **kwargs):
        text = self.translations.get(self.lang, {}).get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text


class I18nDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.translator = Translator("en")
        
        self.setWindowTitle("Internationalization Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 450, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        self.header = QLabel()
        self.header.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.header.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.header)
        
        # Language selector
        lang_layout = QVBoxLayout()
        
        self.lang_label = QLabel()
        lang_layout.addWidget(self.lang_label)
        
        self.lang_combo = QComboBox()
        self.lang_combo.addItem("🇬🇧 English", "en")
        self.lang_combo.addItem("🇮🇩 Bahasa Indonesia", "id")
        self.lang_combo.addItem("🇯🇵 日本語", "ja")
        self.lang_combo.addItem("🇨🇳 中文", "zh")
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        lang_layout.addWidget(self.lang_combo)
        
        layout.addLayout(lang_layout)
        
        # Welcome message
        self.welcome = QLabel()
        self.welcome.setStyleSheet("font-size: 18px; padding: 10px; background: #f0f0f0; border-radius: 5px;")
        self.welcome.setAlignment(Qt.AlignCenter)
        self.welcome.setWordWrap(True)
        layout.addWidget(self.welcome)
        
        # Form
        form_group = QGroupBox()
        form_layout = QFormLayout()
        
        self.name_label = QLabel()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("John Doe")
        form_layout.addRow(self.name_label, self.name_input)
        
        self.email_label = QLabel()
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("john@example.com")
        form_layout.addRow(self.email_label, self.email_input)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        # Buttons
        btn_layout = QVBoxLayout()
        
        self.btn_submit = QPushButton()
        self.btn_submit.setStyleSheet("background-color: #27ae60; color: white; padding: 10px;")
        self.btn_submit.clicked.connect(self.submit)
        btn_layout.addWidget(self.btn_submit)
        
        self.btn_cancel = QPushButton()
        self.btn_cancel.clicked.connect(self.cancel)
        btn_layout.addWidget(self.btn_cancel)
        
        layout.addLayout(btn_layout)
        
        # Result
        self.result = QLabel()
        self.result.setStyleSheet("font-size: 14px; padding: 10px;")
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setWordWrap(True)
        layout.addWidget(self.result)
        
        # Info
        self.info = QLabel()
        self.info.setStyleSheet("color: gray; font-size: 12px;")
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setWordWrap(True)
        layout.addWidget(self.info)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Initial translation
        self.update_ui()
    
    def change_language(self, index):
        lang = self.lang_combo.currentData()
        self.translator.set_language(lang)
        self.update_ui()
    
    def update_ui(self):
        """Update all UI text based on current language"""
        t = self.translator.tr
        
        self.setWindowTitle(t("title"))
        self.header.setText("🌍 " + t("title"))
        self.lang_label.setText(t("language"))
        self.welcome.setText(t("welcome"))
        self.name_label.setText(t("name"))
        self.email_label.setText(t("email"))
        self.btn_submit.setText(t("submit"))
        self.btn_cancel.setText(t("cancel"))
        self.info.setText(t("info"))
        
        # Clear result when changing language
        self.result.clear()
    
    def submit(self):
        name = self.name_input.text() or "User"
        greeting = self.translator.tr("greeting", name=name)
        self.result.setText(greeting)
        self.result.setStyleSheet("font-size: 14px; padding: 10px; color: #27ae60;")
    
    def cancel(self):
        self.name_input.clear()
        self.email_input.clear()
        self.result.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = I18nDemo()
    window.show()
    sys.exit(app.exec_())
