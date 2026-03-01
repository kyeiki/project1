# BAB 5: Layout Manager - Menyusun Kepingan
# =========================================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QPushButton, QLabel, QVBoxLayout, 
                              QHBoxLayout, QGridLayout, QWidget)
from PyQt5.QtCore import Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Campuran - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 350)
        
        widget = QWidget()
        layout_utama = QVBoxLayout()
        
        # HEADER
        header = QLabel("📊 DASHBOARD")
        header.setStyleSheet("""
            font-size: 20px; 
            font-weight: bold; 
            background-color: #3498db; 
            color: white; 
            padding: 10px;
        """)
        header.setAlignment(Qt.AlignCenter)
        layout_utama.addWidget(header)
        
        # Tombol horizontal
        layout_tombol = QHBoxLayout()
        
        btn1 = QPushButton("File")
        btn2 = QPushButton("Edit")
        btn3 = QPushButton("View")
        
        layout_tombol.addWidget(btn1)
        layout_tombol.addWidget(btn2)
        layout_tombol.addWidget(btn3)
        
        layout_utama.addLayout(layout_tombol)
        
        # Grid untuk konten
        layout_grid = QGridLayout()
        
        layout_grid.addWidget(QLabel("📈 Chart"), 0, 0)
        layout_grid.addWidget(QLabel("📋 Table"), 0, 1)
        layout_grid.addWidget(QLabel("📝 Notes"), 1, 0)
        layout_grid.addWidget(QLabel("⚙️ Settings"), 1, 1)
        
        layout_utama.addLayout(layout_grid)
        
        # FOOTER
        footer = QLabel("Status: Siap")
        footer.setStyleSheet("background-color: #2c3e50; color: white; padding: 5px;")
        layout_utama.addWidget(footer)
        
        widget.setLayout(layout_utama)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
