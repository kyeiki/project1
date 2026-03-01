# BAB 32: Stacked Widget
# =======================
# Multiple pages, one visible at a time

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QStackedWidget, QWidget, QPushButton,
                              QLabel, QLineEdit, QTextEdit, QComboBox,
                              QVBoxLayout, QHBoxLayout, QFormLayout,
                              QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt

class PageHome(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.stacked = stacked
        
        layout = QVBoxLayout()
        
        header = QLabel("🏠 HOME")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        welcome = QLabel("Welcome to the App!\n\nUse the menu on the left to navigate.")
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("font-size: 14px; color: gray;")
        layout.addWidget(welcome)
        
        # Quick actions
        layout.addWidget(QLabel("\nQuick Actions:"))
        
        btn_profile = QPushButton("Go to Profile")
        btn_profile.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        layout.addWidget(btn_profile)
        
        btn_settings = QPushButton("Go to Settings")
        btn_settings.clicked.connect(lambda: self.stacked.setCurrentIndex(2))
        layout.addWidget(btn_settings)
        
        layout.addStretch()
        self.setLayout(layout)


class PageProfile(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.stacked = stacked
        
        layout = QVBoxLayout()
        
        header = QLabel("👤 PROFILE")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Form
        form = QFormLayout()
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("Your name")
        form.addRow("Name:", self.name)
        
        self.email = QLineEdit()
        self.email.setPlaceholderText("email@example.com")
        form.addRow("Email:", self.email)
        
        self.bio = QTextEdit()
        self.bio.setPlaceholderText("Tell us about yourself...")
        self.bio.setMaximumHeight(100)
        form.addRow("Bio:", self.bio)
        
        layout.addLayout(form)
        
        # Save button
        btn_save = QPushButton("Save Profile")
        btn_save.setStyleSheet("background-color: #27ae60; color: white; padding: 10px;")
        btn_save.clicked.connect(self.save)
        layout.addWidget(btn_save)
        
        # Status
        self.status = QLabel("")
        layout.addWidget(self.status)
        
        # Back button
        btn_back = QPushButton("← Back to Home")
        btn_back.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        layout.addWidget(btn_back)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def save(self):
        name = self.name.text()
        email = self.email.text()
        self.status.setText(f"✅ Saved! Name: {name}, Email: {email}")


class PageSettings(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.stacked = stacked
        
        layout = QVBoxLayout()
        
        header = QLabel("⚙️ SETTINGS")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Settings form
        form = QFormLayout()
        
        self.theme = QComboBox()
        self.theme.addItems(["Light", "Dark", "System"])
        form.addRow("Theme:", self.theme)
        
        self.language = QComboBox()
        self.language.addItems(["English", "Indonesia", "日本語", "中文"])
        form.addRow("Language:", self.language)
        
        layout.addLayout(form)
        
        # Status
        self.status = QLabel("")
        layout.addWidget(self.status)
        
        # Back button
        btn_back = QPushButton("← Back to Home")
        btn_back.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        layout.addWidget(btn_back)
        
        layout.addStretch()
        self.setLayout(layout)


class PageAbout(QWidget):
    def __init__(self, stacked):
        super().__init__()
        self.stacked = stacked
        
        layout = QVBoxLayout()
        
        header = QLabel("ℹ️ ABOUT")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        info = QLabel("""
Stacked Widget Demo
Version 1.0

This app demonstrates QStackedWidget
for creating multi-page applications.

Features:
• Multiple pages
• Navigation via sidebar
• Each page is a separate class

Built with PyQt5 ❤️
        """)
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # Back button
        btn_back = QPushButton("← Back to Home")
        btn_back.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        layout.addWidget(btn_back)
        
        layout.addStretch()
        self.setLayout(layout)


class StackedDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stacked Widget Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 400)
        
        # Main layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        
        # Sidebar (navigation)
        sidebar = QListWidget()
        sidebar.setFixedWidth(150)
        sidebar.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: white;
                border: none;
                font-size: 14px;
            }
            QListWidget::item {
                padding: 15px;
            }
            QListWidget::item:selected {
                background-color: #3498db;
            }
            QListWidget::item:hover {
                background-color: #34495e;
            }
        """)
        
        sidebar.addItem("🏠 Home")
        sidebar.addItem("👤 Profile")
        sidebar.addItem("⚙️ Settings")
        sidebar.addItem("ℹ️ About")
        sidebar.setCurrentRow(0)
        
        main_layout.addWidget(sidebar)
        
        # Stacked widget (pages)
        self.stack = QStackedWidget()
        
        # Add pages
        self.stack.addWidget(PageHome(self.stack))     # Index 0
        self.stack.addWidget(PageProfile(self.stack))  # Index 1
        self.stack.addWidget(PageSettings(self.stack)) # Index 2
        self.stack.addWidget(PageAbout(self.stack))    # Index 3
        
        main_layout.addWidget(self.stack)
        
        # Connect sidebar to stack
        sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackedDemo()
    window.show()
    sys.exit(app.exec_())
