# BAB 22: Dialog Standar
# =======================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QPushButton, QLabel, QVBoxLayout, 
                              QWidget, QFileDialog, QColorDialog, 
                              QFontDialog, QInputDialog, QMessageBox)
from PyQt5.QtCore import Qt

class DialogDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 450)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("💬 DIALOG STANDAR")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # File Dialog
        layout.addWidget(QLabel("\n📁 File Dialog:"))
        
        btn_open = QPushButton("Buka File...")
        btn_open.clicked.connect(self.open_file)
        layout.addWidget(btn_open)
        
        btn_save = QPushButton("Simpan File...")
        btn_save.clicked.connect(self.save_file)
        layout.addWidget(btn_save)
        
        btn_folder = QPushButton("Pilih Folder...")
        btn_folder.clicked.connect(self.select_folder)
        layout.addWidget(btn_folder)
        
        # Color Dialog
        layout.addWidget(QLabel("\n🎨 Color Dialog:"))
        btn_color = QPushButton("Pilih Warna...")
        btn_color.clicked.connect(self.select_color)
        layout.addWidget(btn_color)
        
        # Font Dialog
        layout.addWidget(QLabel("\n🔤 Font Dialog:"))
        btn_font = QPushButton("Pilih Font...")
        btn_font.clicked.connect(self.select_font)
        layout.addWidget(btn_font)
        
        # Input Dialog
        layout.addWidget(QLabel("\n✏️ Input Dialog:"))
        btn_text = QPushButton("Input Teks...")
        btn_text.clicked.connect(self.input_text)
        layout.addWidget(btn_text)
        
        btn_int = QPushButton("Input Angka...")
        btn_int.clicked.connect(self.input_int)
        layout.addWidget(btn_int)
        
        btn_item = QPushButton("Pilih Item...")
        btn_item.clicked.connect(self.select_item)
        layout.addWidget(btn_item)
        
        # Result
        self.result = QLabel("Hasil akan muncul di sini")
        self.result.setStyleSheet("padding: 10px; background: #f0f0f0; border-radius: 5px;")
        self.result.setWordWrap(True)
        layout.addWidget(self.result)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Buka File", "",
            "Text Files (*.txt);;Python Files (*.py);;All Files (*)"
        )
        if file_path:
            self.result.setText(f"📁 File dipilih:\n{file_path}")
    
    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Simpan File", "",
            "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            self.result.setText(f"💾 Simpan ke:\n{file_path}")
    
    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Pilih Folder")
        if folder:
            self.result.setText(f"📂 Folder dipilih:\n{folder}")
    
    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.result.setText(f"🎨 Warna: RGB({color.red()}, {color.green()}, {color.blue()})")
            self.result.setStyleSheet(f"background-color: {color.name()}; padding: 10px;")
    
    def select_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.result.setText(f"🔤 Font: {font.family()}, Size: {font.pointSize()}")
            self.result.setFont(font)
    
    def input_text(self):
        text, ok = QInputDialog.getText(self, "Input Teks", "Masukkan nama Anda:")
        if ok:
            self.result.setText(f"✏️ Nama: {text}")
    
    def input_int(self):
        num, ok = QInputDialog.getInt(self, "Input Angka", "Masukkan umur:", min=0, max=100)
        if ok:
            self.result.setText(f"🔢 Umur: {num}")
    
    def select_item(self):
        items = ["Java", "Python", "JavaScript", "C++", "Go", "Rust"]
        item, ok = QInputDialog.getItem(self, "Pilih Item", "Bahasa favorit:", items, 0, False)
        if ok:
            self.result.setText(f"📝 Bahasa: {item}")

app = QApplication(sys.argv)
window = DialogDemo()
window.show()
sys.exit(app.exec_())
