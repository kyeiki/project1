# BAB 11: Proyek Akhir - To-Do List App
# =====================================
# Aplikasi lengkap dengan fitur:
# - Menambah tugas
# - Menandai selesai
# - Menghapus tugas
# - Menyimpan ke file

import sys
import json
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                              QLineEdit, QListWidget, QListWidgetItem,
                              QPushButton, QVBoxLayout, QHBoxLayout,
                              QWidget, QMessageBox, QCheckBox, QLabel)
from PyQt5.QtCore import Qt
from datetime import datetime

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✅ To-Do List App - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 450, 550)
        
        self.tasks = []
        self.file_path = os.path.join(os.path.dirname(__file__), "tasks.json")
        self.load_tasks()
        
        self.setup_ui()
    
    def setup_ui(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QLineEdit {
                padding: 15px;
                border: 2px solid #dee2e6;
                border-radius: 10px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #EA6689;
            }
            QPushButton {
                padding: 12px 20px;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton#add {
                background-color: #EA6689;
                color: white;
            }
            QPushButton#add:hover {
                background-color: #5a6fd6;
            }
            QPushButton#done {
                background-color: #28a745;
                color: white;
            }
            QPushButton#done:hover {
                background-color: #218838;
            }
            QPushButton#delete {
                background-color: #dc3545;
                color: white;
            }
            QPushButton#delete:hover {
                background-color: #c82333;
            }
            QPushButton#clear {
                background-color: #6c757d;
                color: white;
            }
            QPushButton#clear:hover {
                background-color: #5a6268;
            }
            QListWidget {
                border: 2px solid #dee2e6;
                border-radius: 10px;
                background-color: white;
                font-size: 14px;
                padding: 5px;
            }
            QListWidget::item {
                padding: 12px;
                border-radius: 5px;
                margin: 2px;
            }
            QListWidget::item:selected {
                background-color: #e3f2fd;
            }
            QListWidget::item:hover {
                background-color: #f8f9fa;
            }
            QLabel#stats {
                color: #6c757d;
                font-size: 12px;
            }
        """)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📝 MY TO-DO LIST")
        header.setStyleSheet("""
            font-size: 24px; 
            font-weight: bold; 
            color: #2c3e50;
            padding: 10px;
        """)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Input area
        input_layout = QHBoxLayout()
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Tambah tugas baru...")
        self.input.returnPressed.connect(self.add_task)
        input_layout.addWidget(self.input)
        
        btn_add = QPushButton("➕")
        btn_add.setObjectName("add")
        btn_add.clicked.connect(self.add_task)
        btn_add.setFixedWidth(50)
        input_layout.addWidget(btn_add)
        
        layout.addLayout(input_layout)
        
        # List widget
        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.toggle_task)
        layout.addWidget(self.list_widget)
        
        # Stats
        self.label_stats = QLabel()
        self.label_stats.setObjectName("stats")
        self.update_stats()
        layout.addWidget(self.label_stats)
        
        # Button area
        btn_layout = QHBoxLayout()
        
        btn_done = QPushButton("✓ Selesai")
        btn_done.setObjectName("done")
        btn_done.clicked.connect(self.mark_done)
        btn_layout.addWidget(btn_done)
        
        btn_delete = QPushButton("🗑 Hapus")
        btn_delete.setObjectName("delete")
        btn_delete.clicked.connect(self.delete_task)
        btn_layout.addWidget(btn_delete)
        
        btn_clear = QPushButton("Clear All")
        btn_clear.setObjectName("clear")
        btn_clear.clicked.connect(self.clear_all)
        btn_layout.addWidget(btn_clear)
        
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.refresh_list()
    
    def add_task(self):
        text = self.input.text().strip()
        if text:
            task = {
                "text": text, 
                "done": False, 
                "created": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.tasks.append(task)
            self.save_tasks()
            self.refresh_list()
            self.input.clear()
    
    def toggle_task(self, item):
        index = self.list_widget.row(item)
        if index >= 0:
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.save_tasks()
            self.refresh_list()
    
    def mark_done(self):
        current = self.list_widget.currentRow()
        if current >= 0:
            self.tasks[current]["done"] = True
            self.save_tasks()
            self.refresh_list()
    
    def delete_task(self):
        current = self.list_widget.currentRow()
        if current >= 0:
            del self.tasks[current]
            self.save_tasks()
            self.refresh_list()
    
    def clear_all(self):
        if not self.tasks:
            return
        reply = QMessageBox.question(self, "Konfirmasi", 
                                     "Hapus semua tugas?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.tasks = []
            self.save_tasks()
            self.refresh_list()
    
    def refresh_list(self):
        self.list_widget.clear()
        for task in self.tasks:
            item = QListWidgetItem(task["text"])
            if task["done"]:
                item.setForeground(Qt.gray)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
            self.list_widget.addItem(item)
        self.update_stats()
    
    def update_stats(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        pending = total - done
        self.label_stats.setText(f"📊 Total: {total} | ✅ Selesai: {done} | ⏳ Pending: {pending}")
    
    def load_tasks(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as f:
                    self.tasks = json.load(f)
        except:
            self.tasks = []
    
    def save_tasks(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            print(f"Error saving: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
