# BAB 40: Status Bar
# ===================
# Status bar dengan informasi dan widget

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QPushButton, QLineEdit,
                              QProgressBar, QWidget, QVBoxLayout,
                              QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Status Bar Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📊 STATUS BAR")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Instructions
        info = QLabel("Lihat status bar di bawah untuk informasi.\n"
                     "Status bar bisa menampilkan teks, widget, dan progress.")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: gray; padding: 20px;")
        layout.addWidget(info)
        
        # Buttons to interact with status bar
        btn_layout = QVBoxLayout()
        
        btn_msg = QPushButton("Show Temporary Message")
        btn_msg.clicked.connect(lambda: self.statusBar().showMessage("Hello! This message will disappear in 3 seconds", 3000))
        btn_layout.addWidget(btn_msg)
        
        btn_perm = QPushButton("Show Permanent Message")
        btn_perm.clicked.connect(lambda: self.status_label.setText("Permanent message"))
        btn_layout.addWidget(btn_perm)
        
        btn_clear = QPushButton("Clear Status")
        btn_clear.clicked.connect(lambda: self.status_label.setText("Ready"))
        btn_layout.addWidget(btn_clear)
        
        btn_progress = QPushButton("Show Progress")
        btn_progress.clicked.connect(self.show_progress)
        btn_layout.addWidget(btn_progress)
        
        btn_coords = QPushButton("Toggle Coordinates Display")
        btn_coords.clicked.connect(self.toggle_coords)
        btn_layout.addWidget(btn_coords)
        
        layout.addLayout(btn_layout)
        
        # Input to demonstrate
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Type here:"))
        
        self.input = QLineEdit()
        self.input.textChanged.connect(self.on_text_changed)
        input_layout.addWidget(self.input)
        
        layout.addLayout(input_layout)
        
        # Mouse position display
        self.mouse_label = QLabel("Mouse: (0, 0)")
        layout.addWidget(self.mouse_label)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Setup status bar
        self.setup_status_bar()
        
        # Timer for clock
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        
        self.show_coords = True
    
    def setup_status_bar(self):
        status = self.statusBar()
        
        # Normal message
        status.showMessage("Ready")
        
        # Permanent widgets (from right to left)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setFixedWidth(150)
        self.progress.setValue(0)
        status.addPermanentWidget(self.progress)
        
        # Status label
        self.status_label = QLabel(" Ready ")
        self.status_label.setStyleSheet("padding: 0 10px;")
        status.addPermanentWidget(self.status_label)
        
        # Coordinates
        self.coords_label = QLabel(" (0, 0) ")
        status.addPermanentWidget(self.coords_label)
        
        # Clock
        self.clock_label = QLabel(" 00:00:00 ")
        self.clock_label.setStyleSheet("padding: 0 10px; background: #3498db; color: white; border-radius: 3px;")
        status.addPermanentWidget(self.clock_label)
        
        # Status bar style
        status.setStyleSheet("""
            QStatusBar {
                background-color: #f8f9fa;
                border-top: 1px solid #dee2e6;
            }
            QStatusBar::item {
                border: none;
            }
        """)
    
    def update_clock(self):
        from datetime import datetime
        now = datetime.now()
        self.clock_label.setText(f" {now.strftime('%H:%M:%S')} ")
    
    def show_progress(self):
        self.progress.setValue(0)
        
        def update():
            current = self.progress.value()
            if current < 100:
                self.progress.setValue(current + 5)
                QTimer.singleShot(100, update)
        
        update()
    
    def toggle_coords(self):
        self.show_coords = not self.show_coords
        self.coords_label.setVisible(self.show_coords)
    
    def on_text_changed(self, text):
        self.status_label.setText(f" Typing... ({len(text)} chars) ")
    
    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        self.mouse_label.setText(f"Mouse: ({x}, {y})")
        
        if self.show_coords:
            self.coords_label.setText(f" ({x}, {y}) ")
        
        super().mouseMoveEvent(event)
    
    def enterEvent(self, event):
        self.statusBar().showMessage("Mouse entered window")
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.statusBar().showMessage("Mouse left window")
        super().leaveEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StatusBarDemo()
    window.setMouseTracking(True)
    window.show()
    sys.exit(app.exec_())
