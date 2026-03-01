# BAB 35: System Tray Icon
# =========================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QPushButton, QLabel, QVBoxLayout,
                              QWidget, QSystemTrayIcon, QMenu, QAction,
                              QSpinBox, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class SystemTrayDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Tray Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 350)
        
        # Create system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        
        # Use built-in icon (in real app, use custom icon)
        self.tray_icon.setIcon(self.style().standardIcon(self.style().SP_ComputerIcon))
        self.tray_icon.setToolTip("System Tray Demo")
        
        # Tray menu
        tray_menu = QMenu()
        
        action_show = QAction("Show Window", self)
        action_show.triggered.connect(self.show)
        tray_menu.addAction(action_show)
        
        action_hide = QAction("Hide Window", self)
        action_hide.triggered.connect(self.hide)
        tray_menu.addAction(action_hide)
        
        tray_menu.addSeparator()
        
        action_notify = QAction("Send Notification", self)
        action_notify.triggered.connect(self.send_notification)
        tray_menu.addAction(action_notify)
        
        tray_menu.addSeparator()
        
        action_quit = QAction("Quit", self)
        action_quit.triggered.connect(self.close)
        tray_menu.addAction(action_quit)
        
        self.tray_icon.setContextMenu(tray_menu)
        
        # Handle tray icon click
        self.tray_icon.activated.connect(self.on_tray_activated)
        
        # Show tray icon
        self.tray_icon.show()
        
        # Main window UI
        widget = QWidget()
        layout = QVBoxLayout()
        
        header = QLabel("🖥️ SYSTEM TRAY ICON")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        info = QLabel("This app can minimize to system tray.\n\nTry:\n• Click 'Hide' to minimize to tray\n• Click tray icon to restore\n• Right-click tray icon for menu")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("padding: 20px;")
        layout.addWidget(info)
        
        # Notification settings
        layout.addWidget(QLabel("Notification Title:"))
        self.title = QLabel("Title")
        self.title.setStyleSheet("padding: 5px; background: #f0f0f0;")
        layout.addWidget(self.title)
        
        layout.addWidget(QLabel("Notification Message:"))
        self.message = QLabel("This is a notification message!")
        self.message.setStyleSheet("padding: 5px; background: #f0f0f0;")
        layout.addWidget(self.message)
        
        # Duration
        duration_layout = QVBoxLayout()
        duration_layout.addWidget(QLabel("Duration (ms):"))
        self.duration = QSpinBox()
        self.duration.setRange(1000, 30000)
        self.duration.setValue(3000)
        self.duration.setSingleStep(1000)
        layout.addWidget(self.duration)
        
        # Buttons
        btn_notify = QPushButton("📩 Send Notification")
        btn_notify.setStyleSheet("padding: 15px;")
        btn_notify.clicked.connect(self.send_notification)
        layout.addWidget(btn_notify)
        
        btn_hide = QPushButton("👁️ Hide to Tray")
        btn_hide.setStyleSheet("padding: 15px;")
        btn_hide.clicked.connect(self.hide)
        layout.addWidget(btn_hide)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def on_tray_activated(self, reason):
        """Handle tray icon activation"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()
            self.activateWindow()
        elif reason == QSystemTrayIcon.Trigger:
            # Single click - show message
            self.tray_icon.showMessage(
                "Clicked!",
                "Double-click to show window",
                QSystemTrayIcon.Information,
                2000
            )
    
    def send_notification(self):
        """Send system notification"""
        self.tray_icon.showMessage(
            "Notification Title",
            "This is a notification from the system tray app!",
            QSystemTrayIcon.Information,
            self.duration.value()
        )
    
    def closeEvent(self, event):
        """Handle window close - minimize to tray instead of closing"""
        if self.tray_icon.isVisible():
            QMessageBox.information(
                self, "Minimizing to Tray",
                "The app will minimize to the system tray.\n"
                "Right-click the tray icon to quit."
            )
            self.hide()
            event.ignore()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Don't quit when window closes
    
    # Check if system tray is available
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Error", "System tray is not available on this system")
        sys.exit(1)
    
    window = SystemTrayDemo()
    window.show()
    
    sys.exit(app.exec_())
