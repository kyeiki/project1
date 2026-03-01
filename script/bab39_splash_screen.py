# BAB 39: Splash Screen
# =====================
# Loading screen saat app startup

import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                              QSplashScreen, QLabel, QVBoxLayout,
                              QWidget, QProgressBar, QPushButton)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont


class CustomSplashScreen(QSplashScreen):
    """Custom splash screen dengan progress bar"""
    
    def __init__(self):
        # Create a pixmap for splash
        pixmap = QPixmap(400, 300)
        pixmap.fill(QColor("#2c3e50"))
        
        # Draw on pixmap
        painter = QPainter(pixmap)
        
        # Title
        painter.setPen(QColor("white"))
        painter.setFont(QFont("Arial", 28, QFont.Bold))
        painter.drawText(pixmap.rect(), Qt.AlignHCenter | Qt.AlignTop, "\n\nMyApp")
        
        # Subtitle
        painter.setFont(QFont("Arial", 12))
        painter.setPen(QColor("#bdc3c7"))
        painter.drawText(pixmap.rect(), Qt.AlignHCenter | Qt.AlignTop, "\n\n\n\n\nVersion 1.0.0")
        
        # Loading text placeholder
        painter.setFont(QFont("Arial", 10))
        painter.setPen(QColor("#3498db"))
        painter.drawText(20, 250, "Loading...")
        
        painter.end()
        
        super().__init__(pixmap)
        
        self.progress = 0
        self.messages = [
            "Initializing...",
            "Loading modules...",
            "Setting up database...",
            "Loading preferences...",
            "Preparing interface...",
            "Almost ready...",
            "Welcome!"
        ]
        self.message_index = 0
    
    def update_progress(self, value):
        self.progress = value
        self.update()  # Trigger repaint
    
    def drawContents(self, painter):
        # Draw progress bar
        bar_width = 360
        bar_height = 10
        bar_x = 20
        bar_y = 270
        
        # Background
        painter.setBrush(QColor("#34495e"))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(bar_x, bar_y, bar_width, bar_height, 5, 5)
        
        # Progress
        progress_width = int(bar_width * self.progress / 100)
        painter.setBrush(QColor("#3498db"))
        painter.drawRoundedRect(bar_x, bar_y, progress_width, bar_height, 5, 5)
        
        # Message
        if self.message_index < len(self.messages):
            painter.setPen(QColor("#3498db"))
            painter.drawText(20, 250, self.messages[self.message_index])
    
    def next_message(self):
        if self.message_index < len(self.messages) - 1:
            self.message_index += 1


class SplashScreenDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Welcome message
        header = QLabel("🎉 Welcome to MyApp!")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        info = QLabel("The splash screen showed while this app was loading.\n\n"
                     "In a real app, the splash screen would show during:\n"
                     "• Database initialization\n"
                     "• Loading configuration\n"
                     "• Preparing resources")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: gray; padding: 20px;")
        layout.addWidget(info)
        
        # Show splash again button
        btn = QPushButton("Show Splash Screen Again")
        btn.clicked.connect(self.show_splash_again)
        btn.setStyleSheet("padding: 15px;")
        layout.addWidget(btn)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def show_splash_again(self):
        # Create and show splash
        splash = CustomSplashScreen()
        splash.show()
        
        # Simulate loading
        def update():
            current = splash.progress
            if current < 100:
                splash.update_progress(current + 10)
                if current % 15 == 0:
                    splash.next_message()
                QTimer.singleShot(200, update)
            else:
                splash.finish(self)
        
        update()


def main():
    app = QApplication(sys.argv)
    
    # Create splash screen
    splash = CustomSplashScreen()
    splash.show()
    
    # Create main window
    window = SplashScreenDemo()
    
    # Simulate loading process
    def update_splash():
        current = splash.progress
        if current < 100:
            splash.update_progress(current + 10)
            if current % 15 == 0:
                splash.next_message()
            QTimer.singleShot(200, update_splash)
        else:
            # Loading complete, show main window
            splash.finish(window)
            window.show()
    
    # Start loading simulation
    QTimer.singleShot(100, update_splash)
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
