# BAB 46: Animation
# ==================
# Animasi dengan QPropertyAnimation

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QPushButton, QLabel, QWidget,
                              QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import (QPropertyAnimation, QPoint, QSize, 
                           QRect, QEasingCurve, pyqtProperty, Qt)
from PyQt5.QtGui import QColor


class AnimatedWidget(QWidget):
    """Widget dengan animatable color property"""
    
    def __init__(self):
        super().__init__()
        self._color = QColor("#3498db")
        self.setFixedSize(100, 100)
    
    def get_color(self):
        return self._color
    
    def set_color(self, color):
        self._color = QColor(color)
        self.update()
    
    color = pyqtProperty(QColor, get_color, set_color)
    
    def paintEvent(self, event):
        from PyQt5.QtGui import QPainter, QBrush
        painter = QPainter(self)
        painter.setBrush(QBrush(self._color))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.rect())


class AnimationDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 500)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🎬 ANIMATION")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Animated widget
        self.animated = AnimatedWidget()
        
        # Position animation
        layout.addWidget(QLabel("\n1. Position Animation:"))
        
        btn_layout1 = QHBoxLayout()
        
        btn_left = QPushButton("← Move Left")
        btn_left.clicked.connect(self.move_left)
        btn_layout1.addWidget(btn_left)
        
        btn_right = QPushButton("Move Right →")
        btn_right.clicked.connect(self.move_right)
        btn_layout1.addWidget(btn_right)
        
        layout.addLayout(btn_layout1)
        
        # Container for animated widget
        self.container = QWidget()
        self.container.setFixedHeight(150)
        self.container.setStyleSheet("background-color: #f0f0f0; border-radius: 10px;")
        
        container_layout = QHBoxLayout()
        container_layout.addStretch()
        container_layout.addWidget(self.animated)
        container_layout.addStretch()
        
        self.container.setLayout(container_layout)
        layout.addWidget(self.container)
        
        # Size animation
        layout.addWidget(QLabel("\n2. Size Animation:"))
        
        btn_layout2 = QHBoxLayout()
        
        btn_grow = QPushButton("Grow ▲")
        btn_grow.clicked.connect(self.grow)
        btn_layout2.addWidget(btn_grow)
        
        btn_shrink = QPushButton("Shrink ▼")
        btn_shrink.clicked.connect(self.shrink)
        btn_layout2.addWidget(btn_shrink)
        
        layout.addLayout(btn_layout2)
        
        # Color animation
        layout.addWidget(QLabel("\n3. Color Animation:"))
        
        btn_layout3 = QHBoxLayout()
        
        btn_red = QPushButton("Red")
        btn_red.setStyleSheet("background-color: #e74c3c; color: white;")
        btn_red.clicked.connect(lambda: self.change_color("#e74c3c"))
        btn_layout3.addWidget(btn_red)
        
        btn_green = QPushButton("Green")
        btn_green.setStyleSheet("background-color: #27ae60; color: white;")
        btn_green.clicked.connect(lambda: self.change_color("#27ae60"))
        btn_layout3.addWidget(btn_green)
        
        btn_blue = QPushButton("Blue")
        btn_blue.setStyleSheet("background-color: #3498db; color: white;")
        btn_blue.clicked.connect(lambda: self.change_color("#3498db"))
        btn_layout3.addWidget(btn_blue)
        
        btn_purple = QPushButton("Purple")
        btn_purple.setStyleSheet("background-color: #9b59b6; color: white;")
        btn_purple.clicked.connect(lambda: self.change_color("#9b59b6"))
        btn_layout3.addWidget(btn_purple)
        
        layout.addLayout(btn_layout3)
        
        # Easing curve demo
        layout.addWidget(QLabel("\n4. Easing Curve Demo:"))
        
        self.easing_combo = QHBoxLayout()
        
        btn_linear = QPushButton("Linear")
        btn_linear.clicked.connect(lambda: self.demo_easing(QEasingCurve.Linear))
        self.easing_combo.addWidget(btn_linear)
        
        btn_inout = QPushButton("InOutQuad")
        btn_inout.clicked.connect(lambda: self.demo_easing(QEasingCurve.InOutQuad))
        self.easing_combo.addWidget(btn_inout)
        
        btn_bounce = QPushButton("Bounce")
        btn_bounce.clicked.connect(lambda: self.demo_easing(QEasingCurve.OutBounce))
        self.easing_combo.addWidget(btn_bounce)
        
        btn_elastic = QPushButton("Elastic")
        btn_elastic.clicked.connect(lambda: self.demo_easing(QEasingCurve.OutElastic))
        self.easing_combo.addWidget(btn_elastic)
        
        layout.addLayout(self.easing_combo)
        
        # Combo animation
        layout.addWidget(QLabel("\n5. Combo Animation:"))
        
        btn_combo = QPushButton("🎉 Run Combo Animation!")
        btn_combo.setStyleSheet("padding: 15px; font-size: 14px;")
        btn_combo.clicked.connect(self.combo_animation)
        layout.addWidget(btn_combo)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def move_left(self):
        self.anim = QPropertyAnimation(self.animated, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(self.animated.geometry())
        
        current = self.animated.geometry()
        self.anim.setEndValue(QRect(10, current.y(), current.width(), current.height()))
        
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
    
    def move_right(self):
        self.anim = QPropertyAnimation(self.animated, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(self.animated.geometry())
        
        current = self.animated.geometry()
        self.anim.setEndValue(QRect(400, current.y(), current.width(), current.height()))
        
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
    
    def grow(self):
        self.anim = QPropertyAnimation(self.animated, b"geometry")
        self.anim.setDuration(500)
        self.anim.setStartValue(self.animated.geometry())
        
        current = self.animated.geometry()
        self.anim.setEndValue(QRect(current.x(), current.y(), 150, 150))
        
        self.anim.setEasingCurve(QEasingCurve.OutElastic)
        self.anim.start()
    
    def shrink(self):
        self.anim = QPropertyAnimation(self.animated, b"geometry")
        self.anim.setDuration(500)
        self.anim.setStartValue(self.animated.geometry())
        
        current = self.animated.geometry()
        self.anim.setEndValue(QRect(current.x(), current.y(), 50, 50))
        
        self.anim.setEasingCurve(QEasingCurve.OutElastic)
        self.anim.start()
    
    def change_color(self, color):
        self.anim = QPropertyAnimation(self.animated, b"color")
        self.anim.setDuration(1000)
        self.anim.setStartValue(self.animated.get_color())
        self.anim.setEndValue(QColor(color))
        
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()
    
    def demo_easing(self, curve):
        self.anim = QPropertyAnimation(self.animated, b"geometry")
        self.anim.setDuration(1500)
        self.anim.setStartValue(QRect(10, 25, 100, 100))
        self.anim.setEndValue(QRect(400, 25, 100, 100))
        
        self.anim.setEasingCurve(curve)
        
        # Loop back
        self.anim.finished.connect(lambda: self.loop_back(curve))
        
        self.anim.start()
    
    def loop_back(self, curve):
        self.anim2 = QPropertyAnimation(self.animated, b"geometry")
        self.anim2.setDuration(1500)
        self.anim2.setStartValue(QRect(400, 25, 100, 100))
        self.anim2.setEndValue(QRect(10, 25, 100, 100))
        
        self.anim2.setEasingCurve(curve)
        self.anim2.start()
    
    def combo_animation(self):
        from PyQt5.QtCore import QSequentialAnimationGroup, QParallelAnimationGroup
        
        group = QSequentialAnimationGroup()
        
        # Move left
        anim1 = QPropertyAnimation(self.animated, b"geometry")
        anim1.setDuration(500)
        anim1.setStartValue(self.animated.geometry())
        anim1.setEndValue(QRect(10, 25, 100, 100))
        anim1.setEasingCurve(QEasingCurve.OutCubic)
        group.addAnimation(anim1)
        
        # Grow
        anim2 = QPropertyAnimation(self.animated, b"geometry")
        anim2.setDuration(300)
        anim2.setStartValue(QRect(10, 25, 100, 100))
        anim2.setEndValue(QRect(10, 0, 150, 150))
        anim2.setEasingCurve(QEasingCurve.OutElastic)
        group.addAnimation(anim2)
        
        # Change color
        anim3 = QPropertyAnimation(self.animated, b"color")
        anim3.setDuration(300)
        anim3.setStartValue(self.animated.get_color())
        anim3.setEndValue(QColor("#e74c3c"))
        group.addAnimation(anim3)
        
        # Shrink
        anim4 = QPropertyAnimation(self.animated, b"geometry")
        anim4.setDuration(300)
        anim4.setStartValue(QRect(10, 0, 150, 150))
        anim4.setEndValue(QRect(10, 25, 100, 100))
        group.addAnimation(anim4)
        
        # Move right with bounce
        anim5 = QPropertyAnimation(self.animated, b"geometry")
        anim5.setDuration(1000)
        anim5.setStartValue(QRect(10, 25, 100, 100))
        anim5.setEndValue(QRect(400, 25, 100, 100))
        anim5.setEasingCurve(QEasingCurve.OutBounce)
        group.addAnimation(anim5)
        
        # Change color back
        anim6 = QPropertyAnimation(self.animated, b"color")
        anim6.setDuration(500)
        anim6.setStartValue(QColor("#e74c3c"))
        anim6.setEndValue(QColor("#3498db"))
        group.addAnimation(anim6)
        
        group.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationDemo()
    window.show()
    sys.exit(app.exec_())
