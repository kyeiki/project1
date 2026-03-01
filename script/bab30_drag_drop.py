# BAB 30: Drag and Drop
# ======================
# Drag files, text, and custom data

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QListWidget, QListWidgetItem, QLabel,
                              QLineEdit, QPushButton, QVBoxLayout, 
                              QHBoxLayout, QWidget)
from PyQt5.QtCore import Qt, QMimeData, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

class DraggableListWidget(QListWidget):
    """ListWidget yang bisa di-drag item-nya"""
    
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QListWidget.InternalMove)
    
    def startDrag(self, supportedActions):
        item = self.currentItem()
        if item:
            # Create drag data
            drag = QDrag(self)
            mime = QMimeData()
            mime.setText(item.text())
            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)


class DropArea(QLabel):
    """Area yang menerima drop"""
    
    dropped = pyqtSignal(str)  # Signal saat ada item di-drop
    
    def __init__(self):
        super().__init__()
        self.setText("📁 Drop files or text here\n\nDrag file dari file manager\natau drag item dari list kiri")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                background-color: #34495e;
                color: #bdc3c7;
                border: 3px dashed #3498db;
                border-radius: 10px;
                padding: 20px;
                font-size: 14px;
            }
            QLabel:hover {
                background-color: #2c3e50;
                border-color: #e74c3c;
            }
        """)
        self.setAcceptDrops(True)
        self.setFixedHeight(150)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText() or event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet(self.styleSheet().replace("#34495e", "#27ae60").replace("#3498db", "#27ae60"))
    
    def dragLeaveEvent(self, event):
        self.setStyleSheet("""
            QLabel {
                background-color: #34495e;
                color: #bdc3c7;
                border: 3px dashed #3498db;
                border-radius: 10px;
                padding: 20px;
                font-size: 14px;
            }
            QLabel:hover {
                background-color: #2c3e50;
                border-color: #e74c3c;
            }
        """)
    
    def dropEvent(self, event: QDropEvent):
        mime = event.mimeData()
        
        # Check for URLs (files)
        if mime.hasUrls():
            files = [url.toLocalFile() for url in mime.urls()]
            self.dropped.emit("\n".join(files))
        # Check for text
        elif mime.hasText():
            self.dropped.emit(mime.text())
        
        event.acceptProposedAction()
        
        # Reset style
        self.dragLeaveEvent(None)


class DragDropDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag & Drop Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 500)
        
        self.setAcceptDrops(True)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🎯 DRAG AND DROP")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Main content
        content_layout = QHBoxLayout()
        
        # Left: Draggable list
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        
        left_layout.addWidget(QLabel("Draggable Items:"))
        
        self.drag_list = DraggableListWidget()
        self.drag_list.addItems([
            "🍎 Apple",
            "🍊 Orange", 
            "🍇 Grape",
            "🍌 Banana",
            "🥝 Kiwi"
        ])
        left_layout.addWidget(self.drag_list)
        
        # Add new item
        add_layout = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Add item...")
        self.input.returnPressed.connect(self.add_item)
        add_layout.addWidget(self.input)
        
        btn_add = QPushButton("➕")
        btn_add.setFixedWidth(40)
        btn_add.clicked.connect(self.add_item)
        add_layout.addWidget(btn_add)
        
        left_layout.addLayout(add_layout)
        left_widget.setLayout(left_layout)
        
        content_layout.addWidget(left_widget)
        
        # Right: Drop area
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        
        right_layout.addWidget(QLabel("Drop Area:"))
        
        self.drop_area = DropArea()
        self.drop_area.dropped.connect(self.on_drop)
        right_layout.addWidget(self.drop_area)
        
        right_layout.addWidget(QLabel("Dropped Items:"))
        
        self.dropped_list = QListWidget()
        right_layout.addWidget(self.dropped_list)
        
        right_widget.setLayout(right_layout)
        
        content_layout.addWidget(right_widget)
        
        layout.addLayout(content_layout)
        
        # Clear button
        btn_clear = QPushButton("Clear Dropped Items")
        btn_clear.clicked.connect(self.dropped_list.clear)
        layout.addWidget(btn_clear)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def add_item(self):
        text = self.input.text().strip()
        if text:
            self.drag_list.addItem(text)
            self.input.clear()
    
    def on_drop(self, data):
        items = data.split("\n")
        for item in items:
            if item.strip():
                self.dropped_list.addItem(f"📥 {item}")
        
        # Update drop area
        self.drop_area.setText(f"✅ Received {len(items)} item(s)\n\nDrop more here...")
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragDropDemo()
    window.show()
    sys.exit(app.exec_())
