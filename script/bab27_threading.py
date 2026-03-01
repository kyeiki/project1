# BAB 27: Threading Dasar
# ========================
# QThread untuk operasi berat tanpa freeze UI

import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QPushButton, QLabel, QProgressBar,
                              QVBoxLayout, QWidget)
from PyQt5.QtCore import QThread, pyqtSignal, Qt

class WorkerThread(QThread):
    """Worker thread untuk tugas berat"""
    # Signals untuk komunikasi ke main thread
    progress = pyqtSignal(int)      # Kirim progress (0-100)
    finished = pyqtSignal(str)      # Kirim hasil saat selesai
    error = pyqtSignal(str)         # Kirim error jika ada
    
    def __init__(self, duration=10):
        super().__init__()
        self.duration = duration
        self._is_running = True
    
    def run(self):
        """Method yang dijalankan di thread terpisah"""
        try:
            for i in range(self.duration + 1):
                if not self._is_running:
                    self.finished.emit("Dibatalkan!")
                    return
                
                # Simulasi tugas berat
                time.sleep(1)
                
                # Kirim progress ke main thread
                progress = int((i / self.duration) * 100)
                self.progress.emit(progress)
            
            self.finished.emit(f"Selesai dalam {self.duration} detik!")
            
        except Exception as e:
            self.error.emit(str(e))
    
    def stop(self):
        """Hentikan thread"""
        self._is_running = False


class ThreadingDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Threading Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)
        
        self.worker = None
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🧵 THREADING")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Info
        info = QLabel("Contoh QThread untuk operasi berat.\nUI tidak freeze saat thread berjalan!")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("color: gray;")
        layout.addWidget(info)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setStyleSheet("QProgressBar { height: 30px; }")
        layout.addWidget(self.progress)
        
        # Status
        self.status = QLabel("Status: Siap")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status)
        
        # Buttons
        btn_start = QPushButton("▶️ Mulai Tugas (10 detik)")
        btn_start.setStyleSheet("padding: 15px; font-size: 14px;")
        btn_start.clicked.connect(self.start_task)
        layout.addWidget(btn_start)
        
        self.btn_stop = QPushButton("⏹️ Batalkan")
        self.btn_stop.setStyleSheet("padding: 15px; font-size: 14px; background-color: #e74c3c; color: white;")
        self.btn_stop.clicked.connect(self.stop_task)
        self.btn_stop.setEnabled(False)
        layout.addWidget(self.btn_stop)
        
        # Counter untuk demo UI responsive
        self.counter_label = QLabel("Counter: 0 (klik untuk tambah)")
        self.counter_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.counter_label)
        
        btn_counter = QPushButton("➕ Tambah Counter")
        btn_counter.clicked.connect(self.increment_counter)
        layout.addWidget(btn_counter)
        
        self.counter = 0
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def start_task(self):
        self.progress.setValue(0)
        self.status.setText("Status: Sedang berjalan...")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; color: #3498db;")
        self.btn_stop.setEnabled(True)
        
        # Buat dan jalankan worker thread
        self.worker = WorkerThread(duration=10)
        self.worker.progress.connect(self.on_progress)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)
        self.worker.start()
    
    def stop_task(self):
        if self.worker:
            self.worker.stop()
    
    def on_progress(self, value):
        self.progress.setValue(value)
    
    def on_finished(self, message):
        self.status.setText(f"Status: {message}")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; color: #27ae60;")
        self.btn_stop.setEnabled(False)
    
    def on_error(self, error_msg):
        self.status.setText(f"Error: {error_msg}")
        self.status.setStyleSheet("font-size: 16px; font-weight: bold; color: #e74c3c;")
        self.btn_stop.setEnabled(False)
    
    def increment_counter(self):
        self.counter += 1
        self.counter_label.setText(f"Counter: {self.counter} (UI tetap responsive!)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThreadingDemo()
    window.show()
    sys.exit(app.exec_())
