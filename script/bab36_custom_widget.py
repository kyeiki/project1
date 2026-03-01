# BAB 36: Custom Widget
# ======================
# Membuat widget sendiri

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QWidget, QLabel, QVBoxLayout, 
                              QHBoxLayout, QPushButton)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont


class CircularProgress(QWidget):
    """Custom widget: Progress circular"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0
        self._max_value = 100
        self._color = QColor("#3498db")
        self._bg_color = QColor("#ecf0f1")
        self._text_color = QColor("#2c3e50")
        
        self.setMinimumSize(120, 120)
    
    def setValue(self, value):
        self._value = min(max(value, 0), self._max_value)
        self.update()
    
    def value(self):
        return self._value
    
    def setColor(self, color):
        self._color = QColor(color)
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Calculate dimensions
        size = min(self.width(), self.height())
        margin = 10
        pen_width = 15
        
        # Background circle
        painter.setPen(QPen(QBrush(self._bg_color), pen_width, Qt.SolidLine, Qt.RoundCap))
        center_x = self.width() // 2
        center_y = self.height() // 2
        radius = (size // 2) - margin - (pen_width // 2)
        
        painter.drawEllipse(center_x - radius, center_y - radius, radius * 2, radius * 2)
        
        # Progress arc
        if self._value > 0:
            progress = self._value / self._max_value
            angle = int(progress * 360 * 16)  # Qt uses 1/16th degree
            
            painter.setPen(QPen(QBrush(self._color), pen_width, Qt.SolidLine, Qt.RoundCap))
            painter.drawArc(
                center_x - radius, center_y - radius,
                radius * 2, radius * 2,
                90 * 16, -angle  # Start from top, go clockwise
            )
        
        # Text
        painter.setPen(self._text_color)
        painter.setFont(QFont("Arial", 20, QFont.Bold))
        painter.drawText(self.rect(), Qt.AlignCenter, f"{self._value}%")


class ToggleSwitch(QWidget):
    """Custom widget: Toggle switch"""
    
    toggled = pyqtSignal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._checked = False
        self._color_on = QColor("#27ae60")
        self._color_off = QColor("#bdc3c7")
        
        self.setFixedSize(60, 30)
        self.setCursor(Qt.PointingHandCursor)
    
    def isChecked(self):
        return self._checked
    
    def setChecked(self, checked):
        self._checked = checked
        self.toggled.emit(checked)
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Background
        color = self._color_on if self._checked else self._color_off
        painter.setBrush(QBrush(color))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 15, 15)
        
        # Circle
        circle_size = self.height() - 6
        circle_x = self.width() - circle_size - 3 if self._checked else 3
        painter.setBrush(QBrush(QColor("white")))
        painter.drawEllipse(circle_x, 3, circle_size, circle_size)
    
    def mousePressEvent(self, event):
        self.setChecked(not self._checked)


class StarRating(QWidget):
    """Custom widget: Star rating"""
    
    ratingChanged = pyqtSignal(int)
    
    def __init__(self, max_stars=5, parent=None):
        super().__init__(parent)
        self._rating = 0
        self._max_stars = max_stars
        self._hover = -1
        
        self.setMouseTracking(True)
        self.setFixedHeight(40)
    
    def rating(self):
        return self._rating
    
    def setRating(self, rating):
        self._rating = min(max(rating, 0), self._max_stars)
        self.ratingChanged.emit(self._rating)
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        star_size = 30
        spacing = 5
        x = 0
        
        for i in range(self._max_stars):
            # Determine if star is filled
            if i < self._rating or i <= self._hover:
                color = QColor("#f1c40f")  # Gold
            else:
                color = QColor("#bdc3c7")  # Gray
            
            self.draw_star(painter, x, 5, star_size, color)
            x += star_size + spacing
    
    def draw_star(self, painter, x, y, size, color):
        painter.setBrush(QBrush(color))
        painter.setPen(Qt.NoPen)
        
        # Simple star using polygon
        from PyQt5.QtGui import QPolygonF
        from PyQt5.QtCore import QPointF
        
        points = []
        for i in range(10):
            angle = i * 36 - 90  # degrees
            import math
            rad = math.radians(angle)
            
            if i % 2 == 0:
                r = size // 2
            else:
                r = size // 4
            
            px = x + size // 2 + r * math.cos(rad)
            py = y + size // 2 + r * math.sin(rad)
            points.append(QPointF(px, py))
        
        painter.drawPolygon(QPolygonF(points))
    
    def mouseMoveEvent(self, event):
        star_size = 30
        spacing = 5
        x = event.x()
        
        self._hover = -1
        for i in range(self._max_stars):
            star_x = i * (star_size + spacing)
            if star_x <= x <= star_x + star_size:
                self._hover = i
                break
        
        self.update()
    
    def leaveEvent(self, event):
        self._hover = -1
        self.update()
    
    def mousePressEvent(self, event):
        if self._hover >= 0:
            self.setRating(self._hover + 1)


class CustomWidgetDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Widget Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 500)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🎨 CUSTOM WIDGETS")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Circular Progress
        layout.addWidget(QLabel("\n1. Circular Progress:"))
        
        progress_layout = QHBoxLayout()
        
        self.progress = CircularProgress()
        progress_layout.addWidget(self.progress)
        
        progress_btns = QVBoxLayout()
        
        btn_0 = QPushButton("0%")
        btn_0.clicked.connect(lambda: self.progress.setValue(0))
        progress_btns.addWidget(btn_0)
        
        btn_50 = QPushButton("50%")
        btn_50.clicked.connect(lambda: self.progress.setValue(50))
        progress_btns.addWidget(btn_50)
        
        btn_100 = QPushButton("100%")
        btn_100.clicked.connect(lambda: self.progress.setValue(100))
        progress_btns.addWidget(btn_100)
        
        progress_layout.addLayout(progress_btns)
        layout.addLayout(progress_layout)
        
        # Toggle Switch
        layout.addWidget(QLabel("\n2. Toggle Switch:"))
        
        toggle_layout = QHBoxLayout()
        self.toggle = ToggleSwitch()
        self.toggle.toggled.connect(self.on_toggle)
        toggle_layout.addWidget(self.toggle)
        
        self.toggle_label = QLabel("OFF")
        toggle_layout.addWidget(self.toggle_label)
        toggle_layout.addStretch()
        
        layout.addLayout(toggle_layout)
        
        # Star Rating
        layout.addWidget(QLabel("\n3. Star Rating:"))
        
        rating_layout = QHBoxLayout()
        self.stars = StarRating()
        self.stars.ratingChanged.connect(self.on_rating_change)
        rating_layout.addWidget(self.stars)
        
        self.rating_label = QLabel("Rating: 0/5")
        rating_layout.addWidget(self.rating_label)
        rating_layout.addStretch()
        
        layout.addLayout(rating_layout)
        
        # Buttons
        btn_set_rating = QPushButton("Set Rating to 4")
        btn_set_rating.clicked.connect(lambda: self.stars.setRating(4))
        layout.addWidget(btn_set_rating)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def on_toggle(self, checked):
        self.toggle_label.setText("ON" if checked else "OFF")
    
    def on_rating_change(self, rating):
        self.rating_label.setText(f"Rating: {rating}/5")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWidgetDemo()
    window.show()
    sys.exit(app.exec_())
