# BAB 44: Database SQLite
# ========================
# SQLite database dengan PyQt5

import sys
import sqlite3
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTableWidget, QTableWidgetItem, 
                              QLineEdit, QPushButton, QLabel,
                              QVBoxLayout, QHBoxLayout, QWidget,
                              QMessageBox, QHeaderView, QComboBox)
from PyQt5.QtCore import Qt

class DatabaseDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database SQLite Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 700, 500)
        
        # Database setup
        self.db_path = os.path.join(os.path.dirname(__file__), "demo.db")
        self.setup_database()
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🗄️ DATABASE SQLITE")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Search & Filter
        search_layout = QHBoxLayout()
        
        search_layout.addWidget(QLabel("Search:"))
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search by name...")
        self.search.textChanged.connect(self.search_records)
        search_layout.addWidget(self.search)
        
        search_layout.addWidget(QLabel("Filter:"))
        self.filter_combo = QComboBox()
        self.filter_combo.addItem("All", "")
        self.filter_combo.addItem("A-E", "ae")
        self.filter_combo.addItem("F-J", "fj")
        self.filter_combo.addItem("K-O", "ko")
        self.filter_combo.addItem("P-T", "pt")
        self.filter_combo.addItem("U-Z", "uz")
        self.filter_combo.currentIndexChanged.connect(self.filter_records)
        search_layout.addWidget(self.filter_combo)
        
        layout.addLayout(search_layout)
        
        # Input form
        form_layout = QHBoxLayout()
        
        form_layout.addWidget(QLabel("Name:"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        form_layout.addWidget(self.name_input)
        
        form_layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        form_layout.addWidget(self.email_input)
        
        form_layout.addWidget(QLabel("Age:"))
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        self.age_input.setFixedWidth(50)
        form_layout.addWidget(self.age_input)
        
        btn_add = QPushButton("Add")
        btn_add.setStyleSheet("background-color: #27ae60; color: white;")
        btn_add.clicked.connect(self.add_record)
        form_layout.addWidget(btn_add)
        
        layout.addLayout(form_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Age", "Actions"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        layout.addWidget(self.table)
        
        # Stats
        self.stats = QLabel()
        self.stats.setStyleSheet("padding: 5px;")
        layout.addWidget(self.stats)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        btn_refresh = QPushButton("🔄 Refresh")
        btn_refresh.clicked.connect(self.load_records)
        btn_layout.addWidget(btn_refresh)
        
        btn_clear = QPushButton("🗑️ Clear All")
        btn_clear.setStyleSheet("background-color: #e74c3c; color: white;")
        btn_clear.clicked.connect(self.clear_all)
        btn_layout.addWidget(btn_clear)
        
        btn_backup = QPushButton("💾 Backup to JSON")
        btn_backup.clicked.connect(self.backup_to_json)
        btn_layout.addWidget(btn_backup)
        
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Load initial data
        self.load_records()
    
    def setup_database(self):
        """Create database and table if not exists"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                age INTEGER
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def load_records(self):
        """Load all records from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users ORDER BY id DESC")
        records = cursor.fetchall()
        
        conn.close()
        
        self.display_records(records)
    
    def display_records(self, records):
        """Display records in table"""
        self.table.setRowCount(len(records))
        
        for row, record in enumerate(records):
            id_, name, email, age = record
            
            self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
            self.table.setItem(row, 1, QTableWidgetItem(name))
            self.table.setItem(row, 2, QTableWidgetItem(email or ""))
            self.table.setItem(row, 3, QTableWidgetItem(str(age) if age else ""))
            
            # Action buttons
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            action_layout.setContentsMargins(0, 0, 0, 0)
            
            btn_edit = QPushButton("Edit")
            btn_edit.setStyleSheet("background-color: #3498db; color: white; padding: 2px 8px;")
            btn_edit.clicked.connect(lambda checked, r=row: self.edit_record(r))
            action_layout.addWidget(btn_edit)
            
            btn_delete = QPushButton("Del")
            btn_delete.setStyleSheet("background-color: #e74c3c; color: white; padding: 2px 8px;")
            btn_delete.clicked.connect(lambda checked, r=row: self.delete_record(r))
            action_layout.addWidget(btn_delete)
            
            action_widget.setLayout(action_layout)
            self.table.setCellWidget(row, 4, action_widget)
        
        self.stats.setText(f"Total records: {len(records)}")
    
    def add_record(self):
        """Add new record to database"""
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        
        if not name:
            QMessageBox.warning(self, "Error", "Name is required!")
            return
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, int(age) if age else None)
        )
        
        conn.commit()
        conn.close()
        
        # Clear inputs
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        
        # Refresh
        self.load_records()
    
    def edit_record(self, row):
        """Edit record in database"""
        id_ = self.table.item(row, 0).text()
        current_name = self.table.item(row, 1).text()
        current_email = self.table.item(row, 2).text()
        current_age = self.table.item(row, 3).text()
        
        # Populate inputs
        self.name_input.setText(current_name)
        self.email_input.setText(current_email)
        self.age_input.setText(current_age)
        
        # Delete old record
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (id_,))
        conn.commit()
        conn.close()
        
        # Focus on name input
        self.name_input.setFocus()
        self.name_input.selectAll()
        
        self.load_records()
    
    def delete_record(self, row):
        """Delete record from database"""
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        
        reply = QMessageBox.question(
            self, "Confirm Delete",
            f"Delete '{name}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (id_,))
            conn.commit()
            conn.close()
            
            self.load_records()
    
    def search_records(self, text):
        """Search records by name"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT * FROM users WHERE name LIKE ? ORDER BY id DESC",
            (f"%{text}%",)
        )
        records = cursor.fetchall()
        conn.close()
        
        self.display_records(records)
    
    def filter_records(self):
        """Filter records by first letter"""
        filter_val = self.filter_combo.currentData()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if filter_val == "":
            cursor.execute("SELECT * FROM users ORDER BY id DESC")
        elif filter_val == "ae":
            cursor.execute(
                "SELECT * FROM users WHERE name LIKE '[A-E]%' ORDER BY id DESC"
            )
        elif filter_val == "fj":
            cursor.execute(
                "SELECT * FROM users WHERE name LIKE '[F-J]%' ORDER BY id DESC"
            )
        elif filter_val == "ko":
            cursor.execute(
                "SELECT * FROM users WHERE name LIKE '[K-O]%' ORDER BY id DESC"
            )
        elif filter_val == "pt":
            cursor.execute(
                "SELECT * FROM users WHERE name LIKE '[P-T]%' ORDER BY id DESC"
            )
        elif filter_val == "uz":
            cursor.execute(
                "SELECT * FROM users WHERE name LIKE '[U-Z]%' ORDER BY id DESC"
            )
        
        records = cursor.fetchall()
        conn.close()
        
        self.display_records(records)
    
    def clear_all(self):
        """Clear all records"""
        reply = QMessageBox.question(
            self, "Confirm Clear",
            "Delete ALL records?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users")
            conn.commit()
            conn.close()
            
            self.load_records()
    
    def backup_to_json(self):
        """Backup database to JSON file"""
        import json
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        records = cursor.fetchall()
        conn.close()
        
        data = [
            {"id": r[0], "name": r[1], "email": r[2], "age": r[3]}
            for r in records
        ]
        
        backup_path = os.path.join(os.path.dirname(__file__), "backup.json")
        with open(backup_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        QMessageBox.information(self, "Backup", f"Backed up {len(records)} records to backup.json")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseDemo()
    window.show()
    sys.exit(app.exec_())
