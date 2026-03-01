# BAB 28: Mouse Events
# =====================
# Handling mouse click, move, enter, leave

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

class MouseDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Events Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 400)
        
        self.setStyleSheet("background-color: #2c3e50;")
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🖱️ MOUSE EVENTS")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Instructions
        info = QLabel("Klik, geser, atau arahkan mouse di area bawah")
        info.setStyleSheet("color: #bdc3c7;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # Event display
        self.event_label = QLabel("Event: -")
        self.event_label.setStyleSheet("""
            font-size: 18px; 
            color: #2ecc71; 
            padding: 10px;
            background-color: #34495e;
            border-radius: 5px;
        """)
        self.event_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.event_label)
        
        # Position display
        self.pos_label = QLabel("Position: (0, 0)")
        self.pos_label.setStyleSheet("""
            font-size: 16px; 
            color: #3498db; 
            padding: 10px;
            background-color: #34495e;
            border-radius: 5px;
        """)
        self.pos_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.pos_label)
        
        # Drawing area
        self.draw_label = QLabel("Area Gambar (klik dan drag)")
        self.draw_label.setStyleSheet("""
            background-color: white;
            border: 3px solid #3498db;
            border-radius: 10px;
            min-height: 150px;
            font-size: 14px;
            color: gray;
        """)
        self.draw_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.draw_label)
        
        self.last_pos = None
        self.drawing = False
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Enable mouse tracking
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event: QMouseEvent):
        x, y = event.x(), event.y()
        button = event.button()
        
        if button == Qt.LeftButton:
            self.event_label.setText("Event: Left Click Pressed")
            self.drawing = True
            self.last_pos = (x, y)
        elif button == Qt.RightButton:
            self.event_label.setText("Event: Right Click Pressed")
        elif button == Qt.MiddleButton:
            self.event_label.setText("Event: Middle Click Pressed")
        
        self.pos_label.setText(f"Position: ({x}, {y})")
    
    def mouseReleaseEvent(self, event: QMouseEvent):
        x, y = event.x(), event.y()
        button = event.button()
        
        if button == Qt.LeftButton:
            self.event_label.setText("Event: Left Click Released")
            self.drawing = False
        
        self.pos_label.setText(f"Position: ({x}, {y})")
    
    def mouseMoveEvent(self, event: QMouseEvent):
        x, y = event.x(), event.y()
        self.pos_label.setText(f"Position: ({x}, {y})")
        
        if self.drawing:
            self.event_label.setText("Event: Dragging...")
    
    def enterEvent(self, event):
        self.event_label.setText("Event: Mouse Entered Window")
    
    def leaveEvent(self, event):
        self.event_label.setText("Event: Mouse Left Window")
    
    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.event_label.setText("Event: Double Click!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseDemo()
    window.show()
    sys.exit(app.exec_())
