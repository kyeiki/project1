# BAB 25: Clipboard
# ==================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTextEdit, QPushButton, QLabel,
                              QVBoxLayout, QHBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class ClipboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clipboard Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📋 CLIPBOARD MANAGER")
        header.setStyleSheet("font-size: 18px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Source text
        layout.addWidget(QLabel("Teks Sumber:"))
        self.source = QTextEdit()
        self.source.setPlaceholderText("Ketik atau paste teks di sini...")
        self.source.setText("Halo! Ini adalah contoh teks untuk dicopy ke clipboard.")
        layout.addWidget(self.source)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        btn_copy = QPushButton("📋 Copy")
        btn_copy.clicked.connect(self.copy_text)
        btn_copy.setStyleSheet("padding: 10px;")
        btn_layout.addWidget(btn_copy)
        
        btn_cut = QPushButton("✂️ Cut")
        btn_cut.clicked.connect(self.cut_text)
        btn_cut.setStyleSheet("padding: 10px;")
        btn_layout.addWidget(btn_cut)
        
        btn_paste = QPushButton("📥 Paste")
        btn_paste.clicked.connect(self.paste_text)
        btn_paste.setStyleSheet("padding: 10px;")
        btn_layout.addWidget(btn_paste)
        
        btn_clear = QPushButton("🗑️ Clear")
        btn_clear.clicked.connect(self.clear_text)
        btn_clear.setStyleSheet("padding: 10px;")
        btn_layout.addWidget(btn_clear)
        
        layout.addLayout(btn_layout)
        
        # Destination text
        layout.addWidget(QLabel("Teks Tujuan (Paste di sini):"))
        self.dest = QTextEdit()
        self.dest.setPlaceholderText("Paste teks di sini...")
        layout.addWidget(self.dest)
        
        # Clipboard info
        self.info = QLabel("Info: -")
        self.info.setStyleSheet("padding: 10px; background: #f0f0f0;")
        layout.addWidget(self.info)
        
        # Monitor clipboard
        btn_monitor = QPushButton("🔍 Cek Clipboard Saat Ini")
        btn_monitor.clicked.connect(self.check_clipboard)
        layout.addWidget(btn_monitor)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Connect clipboard changes
        clipboard = QApplication.clipboard()
        clipboard.dataChanged.connect(self.on_clipboard_change)
    
    def copy_text(self):
        clipboard = QApplication.clipboard()
        text = self.source.textCursor().selectedText()
        if not text:
            text = self.source.toPlainText()
        clipboard.setText(text)
        self.info.setText(f"✅ Copied: {len(text)} karakter")
    
    def cut_text(self):
        clipboard = QApplication.clipboard()
        text = self.source.textCursor().selectedText()
        if text:
            clipboard.setText(text)
            self.source.textCursor().removeSelectedText()
        else:
            text = self.source.toPlainText()
            clipboard.setText(text)
            self.source.clear()
        self.info.setText(f"✂️ Cut: {len(text)} karakter")
    
    def paste_text(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        self.dest.setPlainText(text)
        self.info.setText(f"📥 Pasted: {len(text)} karakter")
    
    def clear_text(self):
        self.source.clear()
        self.dest.clear()
        self.info.setText("🗑️ Cleared")
    
    def check_clipboard(self):
        clipboard = QApplication.clipboard()
        text = clipboard.text()
        if text:
            preview = text[:100] + "..." if len(text) > 100 else text
            self.info.setText(f"📋 Clipboard: {len(text)} karakter\nPreview: {preview}")
        else:
            self.info.setText("📋 Clipboard kosong")
    
    def on_clipboard_change(self):
        self.info.setText("📋 Clipboard berubah!")

app = QApplication(sys.argv)
window = ClipboardDemo()
window.show()
sys.exit(app.exec_())
