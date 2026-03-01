# BAB 42: Shortcut Keys
# =====================
# Global dan local keyboard shortcuts

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QPushButton, QTextEdit,
                              QVBoxLayout, QWidget, QShortcut,
                              QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class ShortcutDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shortcut Keys Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("⌨️ KEYBOARD SHORTCUTS")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        info = QLabel("Try the keyboard shortcuts below:")
        info.setStyleSheet("color: gray;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # Shortcuts list
        shortcuts_list = """
Available Shortcuts:
━━━━━━━━━━━━━━━━━━━━━━━━━
Ctrl+N    → New
Ctrl+S    → Save
Ctrl+O    → Open
Ctrl+Q    → Quit
Ctrl+Z    → Undo
Ctrl+Y    → Redo
Ctrl+Shift+S → Save As
F1        → Help
F5        → Refresh
Esc       → Clear
Space     → Show Message
        """
        
        shortcuts_label = QLabel(shortcuts_list)
        shortcuts_label.setStyleSheet("font-family: monospace; padding: 20px; background: #f0f0f0; border-radius: 10px;")
        layout.addWidget(shortcuts_label)
        
        # Status
        self.status = QLabel("Press a shortcut key...")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status)
        
        # Text edit for undo/redo demo
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Type here and try Ctrl+Z / Ctrl+Y for undo/redo...")
        self.text_edit.setMaximumHeight(100)
        layout.addWidget(self.text_edit)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Setup shortcuts
        self.setup_shortcuts()
    
    def setup_shortcuts(self):
        # Ctrl+N - New
        shortcut_new = QShortcut(QKeySequence("Ctrl+N"), self)
        shortcut_new.activated.connect(self.action_new)
        
        # Ctrl+S - Save
        shortcut_save = QShortcut(QKeySequence("Ctrl+S"), self)
        shortcut_save.activated.connect(self.action_save)
        
        # Ctrl+O - Open
        shortcut_open = QShortcut(QKeySequence("Ctrl+O"), self)
        shortcut_open.activated.connect(self.action_open)
        
        # Ctrl+Q - Quit
        shortcut_quit = QShortcut(QKeySequence("Ctrl+Q"), self)
        shortcut_quit.activated.connect(self.close)
        
        # Ctrl+Z - Undo (using QAction would be better for this)
        shortcut_undo = QShortcut(QKeySequence("Ctrl+Z"), self)
        shortcut_undo.activated.connect(self.action_undo)
        
        # Ctrl+Y - Redo
        shortcut_redo = QShortcut(QKeySequence("Ctrl+Y"), self)
        shortcut_redo.activated.connect(self.action_redo)
        
        # Ctrl+Shift+S - Save As
        shortcut_saveas = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
        shortcut_saveas.activated.connect(self.action_save_as)
        
        # F1 - Help
        shortcut_help = QShortcut(QKeySequence("F1"), self)
        shortcut_help.activated.connect(self.action_help)
        
        # F5 - Refresh
        shortcut_refresh = QShortcut(QKeySequence("F5"), self)
        shortcut_refresh.activated.connect(self.action_refresh)
        
        # Esc - Clear
        shortcut_clear = QShortcut(QKeySequence("Esc"), self)
        shortcut_clear.activated.connect(self.action_clear)
        
        # Space - Show message
        shortcut_space = QShortcut(QKeySequence("Space"), self)
        shortcut_space.activated.connect(self.action_show_message)
    
    def action_new(self):
        self.status.setText("📄 Action: New File")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #27ae60;")
    
    def action_save(self):
        self.status.setText("💾 Action: Save")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #3498db;")
    
    def action_save_as(self):
        self.status.setText("💾 Action: Save As...")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #9b59b6;")
    
    def action_open(self):
        self.status.setText("📂 Action: Open File")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #e67e22;")
    
    def action_undo(self):
        self.text_edit.undo()
        self.status.setText("↩️ Action: Undo")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #f39c12;")
    
    def action_redo(self):
        self.text_edit.redo()
        self.status.setText("↪️ Action: Redo")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #1abc9c;")
    
    def action_help(self):
        QMessageBox.information(self, "Help", "This is a demo of keyboard shortcuts in PyQt5!")
    
    def action_refresh(self):
        self.status.setText("🔄 Action: Refresh")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #3498db;")
    
    def action_clear(self):
        self.text_edit.clear()
        self.status.setText("🗑️ Action: Clear")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #e74c3c;")
    
    def action_show_message(self):
        self.status.setText("␣ Space pressed!")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px; color: #2ecc71;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShortcutDemo()
    window.show()
    sys.exit(app.exec_())
