# BAB 20: Scroll Area
# ====================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QScrollArea, QWidget, QLabel, 
                              QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

class ScrollDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scroll Area Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 500)
        
        # Scroll Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        # Container
        container = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📜 KONTEN PANJANG")
        header.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Banyak konten untuk demo scroll
        for i in range(50):
            item = self.create_item(i)
            layout.addWidget(item)
        
        container.setLayout(layout)
        scroll.setWidget(container)
        
        self.setCentralWidget(scroll)
    
    def create_item(self, index):
        widget = QWidget()
        layout = QHBoxLayout()
        
        # Label
        label = QLabel(f"Item #{index + 1}")
        label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(label)
        
        # Spacer
        layout.addStretch()
        
        # Buttons
        btn1 = QPushButton("View")
        btn1.setFixedWidth(60)
        btn1.clicked.connect(lambda checked, i=index: print(f"View item {i+1}"))
        layout.addWidget(btn1)
        
        btn2 = QPushButton("Delete")
        btn2.setFixedWidth(60)
        btn2.setStyleSheet("background-color: #e74c3c; color: white;")
        layout.addWidget(btn2)
        
        widget.setLayout(layout)
        widget.setStyleSheet("""
            QWidget {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 5px;
                margin: 2px;
            }
            QWidget:hover {
                background-color: #f0f0f0;
            }
        """)
        
        return widget

app = QApplication(sys.argv)
window = ScrollDemo()
window.show()
sys.exit(app.exec_())
