# BAB 23: Timer
# ==============

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QPushButton, QVBoxLayout, 
                              QHBoxLayout, QWidget)
from PyQt5.QtCore import QTimer, QDateTime, Qt

class TimerDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 350, 350)
        
        self.stopwatch_running = False
        self.stopwatch_ms = 0
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # ===== CLOCK (Timer periodik) =====
        clock_label = QLabel("⏰ REALTIME CLOCK")
        clock_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(clock_label)
        
        self.clock = QLabel("00:00:00")
        self.clock.setStyleSheet("font-size: 36px; font-weight: bold; color: #2c3e50;")
        self.clock.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.clock)
        
        # Timer untuk clock (update setiap 1 detik)
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.update_clock()
        
        layout.addSpacing(20)
        
        # ===== STOPWATCH =====
        sw_label = QLabel("⏱️ STOPWATCH")
        sw_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(sw_label)
        
        self.stopwatch = QLabel("00:00:00.000")
        self.stopwatch.setStyleSheet("font-size: 36px; font-weight: bold; color: #e74c3c;")
        self.stopwatch.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.stopwatch)
        
        # Stopwatch buttons
        sw_btn_layout = QHBoxLayout()
        
        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.toggle_stopwatch)
        sw_btn_layout.addWidget(self.btn_start)
        
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.clicked.connect(self.reset_stopwatch)
        sw_btn_layout.addWidget(self.btn_reset)
        
        layout.addLayout(sw_btn_layout)
        
        # Timer untuk stopwatch (update setiap 1 ms)
        self.sw_timer = QTimer()
        self.sw_timer.timeout.connect(self.update_stopwatch)
        
        layout.addSpacing(20)
        
        # ===== COUNTDOWN =====
        cd_label = QLabel("⏳ COUNTDOWN (Single Shot)")
        cd_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(cd_label)
        
        self.countdown = QLabel("Klik tombol untuk mulai")
        self.countdown.setStyleSheet("font-size: 18px; color: #27ae60;")
        self.countdown.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.countdown)
        
        btn_countdown = QPushButton("Mulai Countdown 5 Detik")
        btn_countdown.clicked.connect(self.start_countdown)
        layout.addWidget(btn_countdown)
        
        self.countdown_value = 0
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def update_clock(self):
        now = QDateTime.currentDateTime()
        self.clock.setText(now.toString("HH:mm:ss"))
    
    def toggle_stopwatch(self):
        if self.stopwatch_running:
            self.sw_timer.stop()
            self.btn_start.setText("Start")
            self.stopwatch_running = False
        else:
            self.sw_timer.start(1)  # Update setiap 1ms
            self.btn_start.setText("Stop")
            self.stopwatch_running = True
    
    def update_stopwatch(self):
        self.stopwatch_ms += 1
        ms = self.stopwatch_ms % 1000
        total_sec = self.stopwatch_ms // 1000
        sec = total_sec % 60
        min = (total_sec // 60) % 60
        hour = total_sec // 3600
        
        self.stopwatch.setText(f"{hour:02d}:{min:02d}:{sec:02d}.{ms:03d}")
    
    def reset_stopwatch(self):
        self.sw_timer.stop()
        self.stopwatch_running = False
        self.stopwatch_ms = 0
        self.stopwatch.setText("00:00:00.000")
        self.btn_start.setText("Start")
    
    def start_countdown(self):
        self.countdown_value = 5
        self.countdown.setText(f"Countdown: {self.countdown_value}")
        self.do_countdown()
    
    def do_countdown(self):
        if self.countdown_value > 0:
            self.countdown.setText(f"Countdown: {self.countdown_value}")
            self.countdown_value -= 1
            QTimer.singleShot(1000, self.do_countdown)
        else:
            self.countdown.setText("🎉 SELESAI!")

app = QApplication(sys.argv)
window = TimerDemo()
window.show()
sys.exit(app.exec_())
