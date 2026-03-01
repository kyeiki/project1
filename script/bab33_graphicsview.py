# BAB 33: Graphics View (Simple)
# ===============================
# Basic drawing with QGraphicsView

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QGraphicsScene, QGraphicsView, 
                              QGraphicsRectItem, QGraphicsEllipseItem,
                              QGraphicsLineItem, QGraphicsTextItem,
                              QPushButton, QVBoxLayout, QHBoxLayout,
                              QWidget, QColorDialog, QSpinBox, QLabel)
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush, QColor, QFont, QPainter

class GraphicsDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphics View Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 800, 600)
        
        self.current_color = QColor("#3498db")
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Toolbar
        toolbar = QHBoxLayout()
        
        toolbar.addWidget(QLabel("Color:"))
        btn_color = QPushButton("🎨")
        btn_color.clicked.connect(self.choose_color)
        toolbar.addWidget(btn_color)
        
        toolbar.addWidget(QLabel("Size:"))
        self.size_spin = QSpinBox()
        self.size_spin.setRange(20, 200)
        self.size_spin.setValue(50)
        toolbar.addWidget(self.size_spin)
        
        btn_rect = QPushButton("Add Rectangle")
        btn_rect.clicked.connect(self.add_rect)
        toolbar.addWidget(btn_rect)
        
        btn_ellipse = QPushButton("Add Ellipse")
        btn_ellipse.clicked.connect(self.add_ellipse)
        toolbar.addWidget(btn_ellipse)
        
        btn_line = QPushButton("Add Line")
        btn_line.clicked.connect(self.add_line)
        toolbar.addWidget(btn_line)
        
        btn_text = QPushButton("Add Text")
        btn_text.clicked.connect(self.add_text)
        toolbar.addWidget(btn_text)
        
        btn_clear = QPushButton("Clear All")
        btn_clear.setStyleSheet("background-color: #e74c3c; color: white;")
        btn_clear.clicked.connect(self.clear_scene)
        toolbar.addWidget(btn_clear)
        
        toolbar.addStretch()
        layout.addLayout(toolbar)
        
        # Graphics view
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 750, 500)
        
        self.view = QGraphicsView(self.scene)
        self.view.setStyleSheet("background-color: white; border: 2px solid #ccc;")
        self.view.setRenderHint(QPainter.Antialiasing)
        layout.addWidget(self.view)
        
        # Info
        self.info = QLabel("Click buttons to add shapes. Drag shapes to move them.")
        self.info.setStyleSheet("padding: 5px; background: #f0f0f0;")
        layout.addWidget(self.info)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Add some initial shapes
        self.add_sample_shapes()
    
    def add_sample_shapes(self):
        """Add some sample shapes"""
        # Rectangle
        rect = QGraphicsRectItem(100, 100, 100, 80)
        rect.setBrush(QBrush(QColor("#3498db")))
        rect.setPen(QPen(QColor("#2980b9"), 2))
        rect.setFlag(rect.ItemIsMovable)
        rect.setFlag(rect.ItemIsSelectable)
        self.scene.addItem(rect)
        
        # Ellipse
        ellipse = QGraphicsEllipseItem(300, 150, 120, 80)
        ellipse.setBrush(QBrush(QColor("#e74c3c")))
        ellipse.setPen(QPen(QColor("#c0392b"), 2))
        ellipse.setFlag(ellipse.ItemIsMovable)
        ellipse.setFlag(ellipse.ItemIsSelectable)
        self.scene.addItem(ellipse)
        
        # Line
        line = QGraphicsLineItem(50, 300, 200, 350)
        line.setPen(QPen(QColor("#27ae60"), 4))
        self.scene.addItem(line)
        
        # Text
        text = self.scene.addText("Hello Graphics!")
        text.setDefaultTextColor(QColor("#2c3e50"))
        text.setFont(QFont("Arial", 16, QFont.Bold))
        text.setPos(400, 100)
        text.setFlag(text.ItemIsMovable)
    
    def choose_color(self):
        color = QColorDialog.getColor(self.current_color)
        if color.isValid():
            self.current_color = color
    
    def add_rect(self):
        size = self.size_spin.value()
        x = 200
        y = 200
        
        rect = QGraphicsRectItem(x, y, size, size * 0.8)
        rect.setBrush(QBrush(self.current_color))
        rect.setPen(QPen(self.current_color.darker(), 2))
        rect.setFlag(rect.ItemIsMovable)
        rect.setFlag(rect.ItemIsSelectable)
        self.scene.addItem(rect)
        
        self.info.setText(f"Added rectangle at ({x}, {y})")
    
    def add_ellipse(self):
        size = self.size_spin.value()
        x = 300
        y = 200
        
        ellipse = QGraphicsEllipseItem(x, y, size, size * 0.6)
        ellipse.setBrush(QBrush(self.current_color))
        ellipse.setPen(QPen(self.current_color.darker(), 2))
        ellipse.setFlag(ellipse.ItemIsMovable)
        ellipse.setFlag(ellipse.ItemIsSelectable)
        self.scene.addItem(ellipse)
        
        self.info.setText(f"Added ellipse at ({x}, {y})")
    
    def add_line(self):
        size = self.size_spin.value()
        x1, y1 = 100, 300
        x2, y2 = x1 + size * 2, y1 + size // 2
        
        line = QGraphicsLineItem(x1, y1, x2, y2)
        line.setPen(QPen(self.current_color, 4))
        self.scene.addItem(line)
        
        self.info.setText(f"Added line from ({x1}, {y1}) to ({x2}, {y2})")
    
    def add_text(self):
        text = self.scene.addText("Text")
        text.setDefaultTextColor(self.current_color)
        text.setFont(QFont("Arial", self.size_spin.value() // 3))
        text.setPos(250, 250)
        text.setFlag(text.ItemIsMovable)
        text.setFlag(text.ItemIsSelectable)
        
        self.info.setText("Added text (double-click to edit)")
    
    def clear_scene(self):
        """Clear all items from the scene"""
        self.scene.clear()
        self.info.setText("Scene cleared")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphicsDemo()
    window.show()
    sys.exit(app.exec_())
