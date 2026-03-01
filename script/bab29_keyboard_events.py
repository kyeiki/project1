# BAB 29: Keyboard Events
# ========================
# Handling key press, release, shortcuts

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

class KeyboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keyboard Events Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 400)
        
        self.setStyleSheet("background-color: #1a1a2e;")
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("⌨️ KEYBOARD EVENTS")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Instructions
        info = QLabel("Tekan tombol keyboard untuk melihat event")
        info.setStyleSheet("color: #bdc3c7;")
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # Key display
        self.key_label = QLabel("Key: -")
        self.key_label.setStyleSheet("""
            font-size: 28px; 
            font-weight: bold;
            color: #e94560; 
            padding: 20px;
            background-color: #16213e;
            border-radius: 10px;
        """)
        self.key_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.key_label)
        
        # Key code display
        self.code_label = QLabel("Key Code: -")
        self.code_label.setStyleSheet("""
            font-size: 18px; 
            color: #0f3460;
            padding: 10px;
            background-color: #eee;
            border-radius: 5px;
        """)
        self.code_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.code_label)
        
        # Modifiers display
        self.mod_label = QLabel("Modifiers: None")
        self.mod_label.setStyleSheet("""
            font-size: 16px; 
            color: #3498db;
            padding: 10px;
            background-color: #16213e;
            border-radius: 5px;
        """)
        self.mod_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.mod_label)
        
        # History
        self.history = QLabel("History: -")
        self.history.setStyleSheet("color: #95a5a6; font-size: 12px;")
        self.history.setAlignment(Qt.AlignCenter)
        self.history.setWordWrap(True)
        layout.addWidget(self.history)
        
        self.key_history = []
        
        # Shortcuts info
        shortcuts = QLabel("""
Shortcuts:
• Ctrl+Q = Keluar
• Ctrl+C = Copy message
• Arrow keys = Gerak
• Space = Pause
        """)
        shortcuts.setStyleSheet("color: #7f8c8d; padding: 20px;")
        layout.addWidget(shortcuts)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        modifiers = event.modifiers()
        text = event.text()
        
        # Get key name
        key_name = self.get_key_name(key)
        
        # Update display
        self.key_label.setText(f"Key: {key_name}")
        self.code_label.setText(f"Key Code: {key}")
        
        # Check modifiers
        mods = []
        if modifiers & Qt.ControlModifier:
            mods.append("Ctrl")
        if modifiers & Qt.ShiftModifier:
            mods.append("Shift")
        if modifiers & Qt.AltModifier:
            mods.append("Alt")
        
        self.mod_label.setText(f"Modifiers: {' + '.join(mods) if mods else 'None'}")
        
        # Add to history
        self.key_history.append(key_name)
        if len(self.key_history) > 10:
            self.key_history.pop(0)
        self.history.setText(f"History: {' → '.join(self.key_history)}")
        
        # Handle shortcuts
        if modifiers & Qt.ControlModifier:
            if key == Qt.Key_Q:
                self.close()
            elif key == Qt.Key_C:
                self.key_label.setText("Key: Copied!")
        
        # Special keys
        if key == Qt.Key_Space:
            self.key_label.setText("Key: SPACE (Pause)")
        elif key == Qt.Key_Return:
            self.key_label.setText("Key: ENTER")
        elif key == Qt.Key_Escape:
            self.key_label.setText("Key: ESCAPE")
    
    def keyReleaseEvent(self, event: QKeyEvent):
        key_name = self.get_key_name(event.key())
        self.code_label.setText(f"Released: {key_name}")
    
    def get_key_name(self, key):
        key_names = {
            Qt.Key_Space: "Space",
            Qt.Key_Return: "Enter",
            Qt.Key_Enter: "Enter (Numpad)",
            Qt.Key_Escape: "Escape",
            Qt.Key_Tab: "Tab",
            Qt.Key_Backspace: "Backspace",
            Qt.Key_Delete: "Delete",
            Qt.Key_Insert: "Insert",
            Qt.Key_Home: "Home",
            Qt.Key_End: "End",
            Qt.Key_PageUp: "Page Up",
            Qt.Key_PageDown: "Page Down",
            Qt.Key_Up: "↑",
            Qt.Key_Down: "↓",
            Qt.Key_Left: "←",
            Qt.Key_Right: "→",
            Qt.Key_Shift: "Shift",
            Qt.Key_Control: "Ctrl",
            Qt.Key_Alt: "Alt",
            Qt.Key_F1: "F1",
            Qt.Key_F2: "F2",
            Qt.Key_F3: "F3",
            Qt.Key_F4: "F4",
            Qt.Key_F5: "F5",
            Qt.Key_F6: "F6",
            Qt.Key_F7: "F7",
            Qt.Key_F8: "F8",
            Qt.Key_F9: "F9",
            Qt.Key_F10: "F10",
            Qt.Key_F11: "F11",
            Qt.Key_F12: "F12",
        }
        return key_names.get(key, chr(key) if 32 <= key <= 126 else f"Key({key})")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyboardDemo()
    window.show()
    sys.exit(app.exec_())
