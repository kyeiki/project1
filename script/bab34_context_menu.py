# BAB 34: Context Menu (Right-Click Menu)
# ========================================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QListWidget, QListWidgetItem, QLabel,
                              QMenu, QAction, QMessageBox,
                              QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

class ContextMenuDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Context Menu Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📋 CONTEXT MENU (Right-Click)")
        header.setStyleSheet("font-size: 18px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        info = QLabel("Right-click on the list or anywhere in the window")
        info.setStyleSheet("color: gray;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # List with context menu
        self.list = QListWidget()
        self.list.addItems([
            "📄 Document 1",
            "📄 Document 2", 
            "📄 Document 3",
            "📁 Folder 1",
            "📁 Folder 2"
        ])
        
        # Enable custom context menu
        self.list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list.customContextMenuRequested.connect(self.show_list_context_menu)
        
        layout.addWidget(self.list)
        
        # Status
        self.status = QLabel("Right-click to see context menu")
        self.status.setStyleSheet("padding: 10px; background: #f0f0f0;")
        layout.addWidget(self.status)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Enable context menu for main window
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_window_context_menu)
    
    def show_list_context_menu(self, position):
        """Show context menu for list item"""
        item = self.list.itemAt(position)
        
        if item is None:
            return
        
        # Create menu
        menu = QMenu()
        
        # Actions
        action_open = QAction("📂 Open", self)
        action_open.triggered.connect(lambda: self.open_item(item))
        menu.addAction(action_open)
        
        action_edit = QAction("✏️ Edit", self)
        action_edit.triggered.connect(lambda: self.edit_item(item))
        menu.addAction(action_edit)
        
        menu.addSeparator()
        
        action_copy = QAction("📋 Copy", self)
        action_copy.triggered.connect(lambda: self.copy_item(item))
        menu.addAction(action_copy)
        
        action_cut = QAction("✂️ Cut", self)
        menu.addAction(action_cut)
        
        menu.addSeparator()
        
        action_delete = QAction("🗑️ Delete", self)
        action_delete.triggered.connect(lambda: self.delete_item(item))
        menu.addAction(action_delete)
        
        # Show menu at cursor position
        menu.exec_(self.list.mapToGlobal(position))
    
    def show_window_context_menu(self, position):
        """Show context menu for the window"""
        menu = QMenu()
        
        action_about = QAction("ℹ️ About", self)
        action_about.triggered.connect(self.show_about)
        menu.addAction(action_about)
        
        action_help = QAction("❓ Help", self)
        menu.addAction(action_help)
        
        menu.addSeparator()
        
        action_new = QAction("➕ New Item", self)
        action_new.triggered.connect(self.add_new_item)
        menu.addAction(action_new)
        
        # Show menu
        menu.exec_(self.mapToGlobal(position))
    
    def open_item(self, item):
        self.status.setText(f"Opened: {item.text()}")
    
    def edit_item(self, item):
        self.status.setText(f"Editing: {item.text()}")
        self.list.editItem(item)
    
    def copy_item(self, item):
        self.status.setText(f"Copied: {item.text()}")
        # Clone item
        new_item = item.clone()
        new_item.setText(item.text() + " (copy)")
        self.list.addItem(new_item)
    
    def delete_item(self, item):
        reply = QMessageBox.question(
            self, "Confirm Delete",
            f"Delete '{item.text()}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.list.takeItem(self.list.row(item))
            self.status.setText(f"Deleted: {item.text()}")
    
    def add_new_item(self):
        count = self.list.count() + 1
        self.list.addItem(f"📄 New Document {count}")
        self.status.setText("Added new item")
    
    def show_about(self):
        QMessageBox.about(
            self, "About",
            "Context Menu Demo\n\nRight-click to see context menus!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContextMenuDemo()
    window.show()
    sys.exit(app.exec_())
