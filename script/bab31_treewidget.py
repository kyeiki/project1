# BAB 31: Tree Widget
# ====================
# Hierarchical data display

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTreeWidget, QTreeWidgetItem, QPushButton,
                              QLineEdit, QLabel, QVBoxLayout, QHBoxLayout,
                              QWidget)
from PyQt5.QtCore import Qt

class TreeWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tree Widget Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 500)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🌳 TREE WIDGET")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Input for adding items
        input_layout = QHBoxLayout()
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("New item name...")
        input_layout.addWidget(self.input)
        
        btn_add = QPushButton("Add Child")
        btn_add.clicked.connect(self.add_child)
        input_layout.addWidget(btn_add)
        
        btn_add_root = QPushButton("Add Root")
        btn_add_root.clicked.connect(self.add_root)
        input_layout.addWidget(btn_add_root)
        
        layout.addLayout(input_layout)
        
        # Tree widget
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Type", "Size"])
        self.tree.setColumnWidth(0, 200)
        
        # Add sample data
        self.add_sample_data()
        
        self.tree.itemClicked.connect(self.on_item_click)
        self.tree.itemDoubleClicked.connect(self.on_item_double_click)
        layout.addWidget(self.tree)
        
        # Info label
        self.info = QLabel("Click an item to see info")
        self.info.setStyleSheet("padding: 10px; background: #f0f0f0;")
        layout.addWidget(self.info)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        btn_expand = QPushButton("Expand All")
        btn_expand.clicked.connect(self.tree.expandAll)
        btn_layout.addWidget(btn_expand)
        
        btn_collapse = QPushButton("Collapse All")
        btn_collapse.clicked.connect(self.tree.collapseAll)
        btn_layout.addWidget(btn_collapse)
        
        btn_delete = QPushButton("Delete Selected")
        btn_delete.clicked.connect(self.delete_selected)
        btn_delete.setStyleSheet("background-color: #e74c3c; color: white;")
        btn_layout.addWidget(btn_delete)
        
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def add_sample_data(self):
        """Add sample hierarchical data"""
        
        # Root: Documents
        docs = QTreeWidgetItem(self.tree, ["📁 Documents", "Folder", ""])
        QTreeWidgetItem(docs, ["📄 resume.pdf", "PDF", "256 KB"])
        QTreeWidgetItem(docs, ["📄 letter.docx", "Word", "128 KB"])
        
        # Subfolder
        work = QTreeWidgetItem(docs, ["📁 Work", "Folder", ""])
        QTreeWidgetItem(work, ["📄 report.xlsx", "Excel", "512 KB"])
        QTreeWidgetItem(work, ["📄 presentation.pptx", "PowerPoint", "2 MB"])
        
        # Root: Pictures
        pics = QTreeWidgetItem(self.tree, ["📁 Pictures", "Folder", ""])
        QTreeWidgetItem(pics, ["🖼️ photo1.jpg", "Image", "3 MB"])
        QTreeWidgetItem(pics, ["🖼️ photo2.png", "Image", "5 MB"])
        
        # Subfolder
        vacation = QTreeWidgetItem(pics, ["📁 Vacation", "Folder", ""])
        QTreeWidgetItem(vacation, ["🖼️ beach.jpg", "Image", "4 MB"])
        QTreeWidgetItem(vacation, ["🖼️ mountain.jpg", "Image", "6 MB"])
        
        # Root: Music
        music = QTreeWidgetItem(self.tree, ["📁 Music", "Folder", ""])
        QTreeWidgetItem(music, ["🎵 song1.mp3", "Audio", "5 MB"])
        QTreeWidgetItem(music, ["🎵 song2.mp3", "Audio", "4 MB"])
        
        # Expand first level
        self.tree.expandToDepth(0)
    
    def add_root(self):
        text = self.input.text().strip()
        if text:
            item = QTreeWidgetItem(self.tree, [f"📁 {text}", "Folder", ""])
            self.tree.addTopLevelItem(item)
            self.input.clear()
    
    def add_child(self):
        text = self.input.text().strip()
        if text:
            current = self.tree.currentItem()
            if current:
                QTreeWidgetItem(current, [f"📄 {text}", "File", "New"])
                current.setExpanded(True)
            self.input.clear()
    
    def on_item_click(self, item, column):
        path = self.get_item_path(item)
        self.info.setText(f"Selected: {path}")
    
    def on_item_double_click(self, item, column):
        path = self.get_item_path(item)
        self.info.setText(f"Double-clicked: {path}")
    
    def get_item_path(self, item):
        """Get full path of item"""
        path = [item.text(0)]
        parent = item.parent()
        while parent:
            path.insert(0, parent.text(0))
            parent = parent.parent()
        return " / ".join(path)
    
    def delete_selected(self):
        item = self.tree.currentItem()
        if item:
            parent = item.parent()
            if parent:
                parent.removeChild(item)
            else:
                index = self.tree.indexOfTopLevelItem(item)
                self.tree.takeTopLevelItem(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TreeWidgetDemo()
    window.show()
    sys.exit(app.exec_())
