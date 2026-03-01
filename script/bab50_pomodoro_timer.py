# BAB 50: Proyek Akhir - Pomodoro Timer
# ======================================
# Aplikasi produktivitas dengan teknik Pomodoro

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QPushButton, QVBoxLayout,
                              QHBoxLayout, QWidget, QSpinBox,
                              QComboBox, QListWidget, QListWidgetItem,
                              QGroupBox, QProgressBar, QMessageBox)
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QFont
import winsound  # For sound on Windows (optional)


class PomodoroTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🍅 Pomodoro Timer - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 450, 600)
        
        # Timer state
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
        self.time_remaining = 25 * 60  # 25 minutes in seconds
        self.is_running = False
        self.is_break = False
        self.pomodoro_count = 0
        self.current_task = ""
        
        # Settings
        self.work_duration = 25  # minutes
        self.short_break = 5
        self.long_break = 15
        self.pomodoros_until_long_break = 4
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                border: none;
            }
            QProgressBar {
                border: 2px solid #34495e;
                border-radius: 10px;
                text-align: center;
                font-weight: bold;
                color: white;
            }
            QProgressBar::chunk {
                background-color: #e74c3c;
                border-radius: 8px;
            }
            QSpinBox, QComboBox {
                padding: 10px;
                font-size: 14px;
                border-radius: 8px;
                border: 2px solid #34495e;
                background-color: #34495e;
                color: white;
            }
            QListWidget {
                background-color: #34495e;
                border: 2px solid #34495e;
                border-radius: 10px;
                color: white;
            }
            QListWidget::item {
                padding: 10px;
            }
            QListWidget::item:selected {
                background-color: #e74c3c;
            }
        """)
        
        self.setup_ui()
    
    def setup_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🍅 POMODORO TIMER")
        header.setStyleSheet("font-size: 28px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Status
        self.status = QLabel("Ready to Focus!")
        self.status.setStyleSheet("font-size: 18px; color: #ecf0f1;")
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status)
        
        # Timer display
        self.timer_display = QLabel("25:00")
        self.timer_display.setStyleSheet("""
            font-size: 72px; 
            font-weight: bold; 
            color: #ecf0f1;
            background-color: #34495e;
            border-radius: 20px;
            padding: 20px;
        """)
        self.timer_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_display)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.setFixedHeight(25)
        layout.addWidget(self.progress)
        
        # Control buttons
        btn_layout = QHBoxLayout()
        
        self.btn_start = QPushButton("▶ Start")
        self.btn_start.setStyleSheet("background-color: #27ae60; color: white;")
        self.btn_start.clicked.connect(self.start_timer)
        btn_layout.addWidget(self.btn_start)
        
        self.btn_pause = QPushButton("⏸ Pause")
        self.btn_pause.setStyleSheet("background-color: #f39c12; color: white;")
        self.btn_pause.clicked.connect(self.pause_timer)
        self.btn_pause.setEnabled(False)
        btn_layout.addWidget(self.btn_pause)
        
        self.btn_reset = QPushButton("⏹ Reset")
        self.btn_reset.setStyleSheet("background-color: #e74c3c; color: white;")
        self.btn_reset.clicked.connect(self.reset_timer)
        btn_layout.addWidget(self.btn_reset)
        
        layout.addLayout(btn_layout)
        
        # Skip button
        btn_skip = QPushButton("⏭ Skip to Break")
        btn_skip.clicked.connect(self.skip_to_break)
        layout.addWidget(btn_skip)
        
        # Stats
        stats_group = QGroupBox("📊 Today's Stats")
        stats_group.setStyleSheet("QGroupBox { color: white; font-weight: bold; }")
        stats_layout = QHBoxLayout()
        
        self.pomodoro_label = QLabel("🍅 0 Pomodoros")
        self.pomodoro_label.setStyleSheet("font-size: 16px;")
        stats_layout.addWidget(self.pomodoro_label)
        
        self.time_label = QLabel("⏱ 0 min focused")
        self.time_label.setStyleSheet("font-size: 16px;")
        stats_layout.addWidget(self.time_label)
        
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)
        
        # Tasks
        task_group = QGroupBox("📋 Current Task")
        task_group.setStyleSheet("QGroupBox { color: white; font-weight: bold; }")
        task_layout = QVBoxLayout()
        
        task_input_layout = QHBoxLayout()
        
        from PyQt5.QtWidgets import QLineEdit
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("What are you working on?")
        self.task_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border-radius: 8px;
                border: 2px solid #34495e;
                background-color: #34495e;
                color: white;
            }
        """)
        self.task_input.returnPressed.connect(self.add_task)
        task_input_layout.addWidget(self.task_input)
        
        btn_add = QPushButton("+")
        btn_add.setFixedWidth(50)
        btn_add.clicked.connect(self.add_task)
        task_input_layout.addWidget(btn_add)
        
        task_layout.addLayout(task_input_layout)
        
        self.task_list = QListWidget()
        self.task_list.setMaximumHeight(100)
        self.task_list.itemClicked.connect(self.select_task)
        task_layout.addWidget(self.task_list)
        
        task_group.setLayout(task_layout)
        layout.addWidget(task_group)
        
        # Settings
        settings_group = QGroupBox("⚙️ Settings")
        settings_group.setStyleSheet("QGroupBox { color: white; font-weight: bold; }")
        settings_layout = QVBoxLayout()
        
        duration_layout = QHBoxLayout()
        
        duration_layout.addWidget(QLabel("Work:"))
        self.spin_work = QSpinBox()
        self.spin_work.setRange(1, 60)
        self.spin_work.setValue(25)
        self.spin_work.setSuffix(" min")
        self.spin_work.valueChanged.connect(self.update_settings)
        duration_layout.addWidget(self.spin_work)
        
        duration_layout.addWidget(QLabel("Short Break:"))
        self.spin_short = QSpinBox()
        self.spin_short.setRange(1, 30)
        self.spin_short.setValue(5)
        self.spin_short.setSuffix(" min")
        duration_layout.addWidget(self.spin_short)
        
        duration_layout.addWidget(QLabel("Long Break:"))
        self.spin_long = QSpinBox()
        self.spin_long.setRange(1, 60)
        self.spin_long.setValue(15)
        self.spin_long.setSuffix(" min")
        duration_layout.addWidget(self.spin_long)
        
        settings_layout.addLayout(duration_layout)
        
        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def format_time(self, seconds):
        """Format seconds to MM:SS"""
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"
    
    def update_timer(self):
        """Update timer every second"""
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_display.setText(self.format_time(self.time_remaining))
            
            # Update progress
            total = self.work_duration * 60 if not self.is_break else self.get_break_duration() * 60
            progress = int((1 - self.time_remaining / total) * 100)
            self.progress.setValue(progress)
            
        else:
            # Timer finished
            self.timer.stop()
            self.is_running = False
            
            if self.is_break:
                # Break finished, start work
                self.is_break = False
                self.time_remaining = self.work_duration * 60
                self.status.setText("⏰ Break over! Back to work!")
                self.timer_display.setStyleSheet("""
                    font-size: 72px; 
                    font-weight: bold; 
                    color: #ecf0f1;
                    background-color: #e74c3c;
                    border-radius: 20px;
                    padding: 20px;
                """)
            else:
                # Work finished, start break
                self.pomodoro_count += 1
                self.update_stats()
                
                self.is_break = True
                self.time_remaining = self.get_break_duration() * 60
                
                if self.pomodoro_count % self.pomodoros_until_long_break == 0:
                    self.status.setText("🎉 Long break time! You've earned it!")
                else:
                    self.status.setText(f"✅ Pomodoro #{self.pomodoro_count} complete!")
                
                self.timer_display.setStyleSheet("""
                    font-size: 72px; 
                    font-weight: bold; 
                    color: #ecf0f1;
                    background-color: #27ae60;
                    border-radius: 20px;
                    padding: 20px;
                """)
            
            self.timer_display.setText(self.format_time(self.time_remaining))
            self.progress.setValue(0)
            
            # Play sound (Windows only)
            try:
                winsound.Beep(1000, 500)
            except:
                pass
            
            # Ask to continue
            reply = QMessageBox.question(
                self, "Timer Complete",
                "Start " + ("break" if not self.is_break else "next pomodoro") + "?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                self.start_timer()
            else:
                self.btn_start.setEnabled(True)
                self.btn_pause.setEnabled(False)
    
    def get_break_duration(self):
        """Get break duration based on pomodoro count"""
        if self.pomodoro_count % self.pomodoros_until_long_break == 0:
            return self.long_break
        return self.short_break
    
    def start_timer(self):
        """Start or resume the timer"""
        if not self.is_running:
            self.is_running = True
            self.timer.start(1000)  # Update every second
            
            self.btn_start.setEnabled(False)
            self.btn_pause.setEnabled(True)
            
            if not self.is_break:
                self.status.setText(f"🔥 Focusing on: {self.current_task or 'Task'}")
                self.timer_display.setStyleSheet("""
                    font-size: 72px; 
                    font-weight: bold; 
                    color: #ecf0f1;
                    background-color: #e74c3c;
                    border-radius: 20px;
                    padding: 20px;
                """)
            else:
                self.status.setText("☕ Taking a break...")
                self.timer_display.setStyleSheet("""
                    font-size: 72px; 
                    font-weight: bold; 
                    color: #ecf0f1;
                    background-color: #27ae60;
                    border-radius: 20px;
                    padding: 20px;
                """)
    
    def pause_timer(self):
        """Pause the timer"""
        if self.is_running:
            self.is_running = False
            self.timer.stop()
            
            self.btn_start.setEnabled(True)
            self.btn_pause.setEnabled(False)
            self.status.setText("⏸ Paused")
    
    def reset_timer(self):
        """Reset the timer"""
        self.timer.stop()
        self.is_running = False
        self.is_break = False
        self.time_remaining = self.work_duration * 60
        
        self.timer_display.setText(self.format_time(self.time_remaining))
        self.progress.setValue(0)
        self.status.setText("Ready to Focus!")
        
        self.btn_start.setEnabled(True)
        self.btn_pause.setEnabled(False)
        
        self.timer_display.setStyleSheet("""
            font-size: 72px; 
            font-weight: bold; 
            color: #ecf0f1;
            background-color: #34495e;
            border-radius: 20px;
            padding: 20px;
        """)
    
    def skip_to_break(self):
        """Skip to break"""
        if not self.is_break:
            self.timer.stop()
            self.is_break = True
            self.time_remaining = self.get_break_duration() * 60
            self.timer_display.setText(self.format_time(self.time_remaining))
            self.status.setText("☕ Taking a break...")
            self.progress.setValue(0)
            
            self.timer_display.setStyleSheet("""
                font-size: 72px; 
                font-weight: bold; 
                color: #ecf0f1;
                background-color: #27ae60;
                border-radius: 20px;
                padding: 20px;
            """)
    
    def update_settings(self):
        """Update settings from spinboxes"""
        self.work_duration = self.spin_work.value()
        self.short_break = self.spin_short.value()
        self.long_break = self.spin_long.value()
        
        if not self.is_running and not self.is_break:
            self.time_remaining = self.work_duration * 60
            self.timer_display.setText(self.format_time(self.time_remaining))
    
    def update_stats(self):
        """Update statistics display"""
        self.pomodoro_label.setText(f"🍅 {self.pomodoro_count} Pomodoros")
        
        total_minutes = self.pomodoro_count * self.work_duration
        if total_minutes >= 60:
            hours = total_minutes // 60
            mins = total_minutes % 60
            self.time_label.setText(f"⏱ {hours}h {mins}m focused")
        else:
            self.time_label.setText(f"⏱ {total_minutes} min focused")
    
    def add_task(self):
        """Add a task to the list"""
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
            
            # Select first task if none selected
            if self.task_list.count() == 1:
                self.task_list.setCurrentRow(0)
                self.current_task = task
    
    def select_task(self, item):
        """Select a task to focus on"""
        self.current_task = item.text()
        if self.is_running and not self.is_break:
            self.status.setText(f"🔥 Focusing on: {self.current_task}")
    
    def closeEvent(self, event):
        """Handle window close"""
        if self.is_running:
            reply = QMessageBox.question(
                self, "Timer Running",
                "Timer is still running. Exit anyway?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if reply == QMessageBox.No:
                event.ignore()
                return
        
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroTimer()
    window.show()
    sys.exit(app.exec_())
