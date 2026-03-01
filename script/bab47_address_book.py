# BAB 47: Proyek Akhir - Address Book
# =====================================
# Aplikasi buku alamat lengkap dengan database

import sys
import sqlite3
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTableWidget, QTableWidgetItem, 
                              QLineEdit, QPushButton, QLabel,
                              QVBoxLayout, QHBoxLayout, QWidget,
                              QMessageBox, QHeaderView, QDialog,
                              QFormLayout, QComboBox, QDialogButtonBox)
from PyQt5.QtCore import Qt

class ContactDialog(QDialog):
    """Dialog untuk tambah/edit kontak"""
    
    def __init__(self, parent=None, contact=None):
        super().__init__(parent)
        self.setWindowTitle("Add Contact" if not contact else "Edit Contact")
        self.setFixedSize(400, 300)
        
        self.contact = contact
        self.result_data = None
        
        layout = QVBoxLayout()
        
        form = QFormLayout()
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("Full name")
        form.addRow("Name*:", self.name)
        
        self.email = QLineEdit()
        self.email.setPlaceholderText("email@example.com")
        form.addRow("Email:", self.email)
        
        self.phone = QLineEdit()
        self.phone.setPlaceholderText("08xxxxxxxxxx")
        form.addRow("Phone:", self.phone)
        
        self.address = QLineEdit()
        self.address.setPlaceholderText("Address")
        form.addRow("Address:", self.address)
        
        self.city = QLineEdit()
        self.city.setPlaceholderText("City")
        form.addRow("City:", self.city)
        
        self.category = QComboBox()
        self.category.addItems(["Family", "Friend", "Work", "Business", "Other"])
        form.addRow("Category:", self.category)
        
        layout.addLayout(form)
        
        # Buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel
        )
        buttons.accepted.connect(self.save)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        # Fill if editing
        if contact:
            self.name.setText(contact[1])
            self.email.setText(contact[2] or "")
            self.phone.setText(contact[3] or "")
            self.address.setText(contact[4] or "")
            self.city.setText(contact[5] or "")
            index = self.category.findText(contact[6] or "Other")
            if index >= 0:
                self.category.setCurrentIndex(index)
        
        self.setLayout(layout)
    
    def save(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "Error", "Name is required!")
            return
        
        self.result_data = {
            "name": self.name.text().strip(),
            "email": self.email.text().strip(),
            "phone": self.phone.text().strip(),
            "address": self.address.text().strip(),
            "city": self.city.text().strip(),
            "category": self.category.currentText()
        }
        self.accept()


class AddressBook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📚 Address Book - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 800, 600)
        
        # Database
        self.db_path = os.path.join(os.path.dirname(__file__), "contacts.db")
        self.setup_database()
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #ddd;
                gridline-color: #eee;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QPushButton {
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        
        self.setup_ui()
        self.load_contacts()
    
    def setup_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT,
                address TEXT,
                city TEXT,
                category TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def setup_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📚 ADDRESS BOOK")
        header.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Search and filter
        search_layout = QHBoxLayout()
        
        search_layout.addWidget(QLabel("Search:"))
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search by name, email, phone...")
        self.search.textChanged.connect(self.search_contacts)
        search_layout.addWidget(self.search)
        
        search_layout.addWidget(QLabel("Category:"))
        self.filter_category = QComboBox()
        self.filter_category.addItem("All", "")
        self.filter_category.addItems(["Family", "Friend", "Work", "Business", "Other"])
        self.filter_category.currentIndexChanged.connect(self.filter_contacts)
        search_layout.addWidget(self.filter_category)
        
        layout.addLayout(search_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "Email", "Phone", "City", "Category", "Actions"]
        )
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.doubleClicked.connect(self.edit_contact_dialog)
        
        layout.addWidget(self.table)
        
        # Stats
        self.stats = QLabel("Total: 0 contacts")
        self.stats.setStyleSheet("padding: 5px;")
        layout.addWidget(self.stats)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        btn_add = QPushButton("➕ Add Contact")
        btn_add.setStyleSheet("background-color: #27ae60; color: white;")
        btn_add.clicked.connect(self.add_contact_dialog)
        btn_layout.addWidget(btn_add)
        
        btn_edit = QPushButton("✏️ Edit")
        btn_edit.clicked.connect(self.edit_contact_dialog)
        btn_layout.addWidget(btn_edit)
        
        btn_delete = QPushButton("🗑️ Delete")
        btn_delete.setStyleSheet("background-color: #e74c3c; color: white;")
        btn_delete.clicked.connect(self.delete_contact)
        btn_layout.addWidget(btn_delete)
        
        btn_layout.addStretch()
        
        btn_export = QPushButton("📤 Export CSV")
        btn_export.clicked.connect(self.export_csv)
        btn_layout.addWidget(btn_export)
        
        btn_import = QPushButton("📥 Import CSV")
        btn_import.clicked.connect(self.import_csv)
        btn_layout.addWidget(btn_import)
        
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def load_contacts(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM contacts ORDER BY name")
        contacts = cursor.fetchall()
        conn.close()
        
        self.display_contacts(contacts)
    
    def display_contacts(self, contacts):
        self.table.setRowCount(len(contacts))
        
        for row, contact in enumerate(contacts):
            id_, name, email, phone, address, city, category, created = contact
            
            self.table.setItem(row, 0, QTableWidgetItem(str(id_)))
            self.table.setItem(row, 1, QTableWidgetItem(name))
            self.table.setItem(row, 2, QTableWidgetItem(email or ""))
            self.table.setItem(row, 3, QTableWidgetItem(phone or ""))
            self.table.setItem(row, 4, QTableWidgetItem(city or ""))
            self.table.setItem(row, 5, QTableWidgetItem(category or ""))
            
            # Action buttons
            action_widget = QWidget()
            action_layout = QHBoxLayout()
            action_layout.setContentsMargins(2, 2, 2, 2)
            
            btn_view = QPushButton("👁")
            btn_view.setFixedWidth(30)
            btn_view.clicked.connect(lambda checked, c=contact: self.view_contact(c))
            action_layout.addWidget(btn_view)
            
            btn_call = QPushButton("📞")
            btn_call.setFixedWidth(30)
            btn_call.clicked.connect(lambda checked, p=phone: self.call_contact(p))
            action_layout.addWidget(btn_call)
            
            action_widget.setLayout(action_layout)
            self.table.setCellWidget(row, 6, action_widget)
        
        self.stats.setText(f"Total: {len(contacts)} contacts")
    
    def add_contact_dialog(self):
        dialog = ContactDialog(self)
        if dialog.exec_():
            self.add_contact(dialog.result_data)
    
    def add_contact(self, data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO contacts (name, email, phone, address, city, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data["name"], data["email"], data["phone"], 
              data["address"], data["city"], data["category"]))
        
        conn.commit()
        conn.close()
        
        self.load_contacts()
    
    def edit_contact_dialog(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Warning", "Please select a contact!")
            return
        
        id_ = self.table.item(row, 0).text()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = ?", (id_,))
        contact = cursor.fetchone()
        conn.close()
        
        dialog = ContactDialog(self, contact)
        if dialog.exec_():
            self.update_contact(id_, dialog.result_data)
    
    def update_contact(self, id_, data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE contacts SET name=?, email=?, phone=?, address=?, city=?, category=?
            WHERE id=?
        ''', (data["name"], data["email"], data["phone"],
              data["address"], data["city"], data["category"], id_))
        
        conn.commit()
        conn.close()
        
        self.load_contacts()
    
    def delete_contact(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Warning", "Please select a contact!")
            return
        
        id_ = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        
        reply = QMessageBox.question(
            self, "Confirm Delete",
            f"Delete contact '{name}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contacts WHERE id = ?", (id_,))
            conn.commit()
            conn.close()
            
            self.load_contacts()
    
    def view_contact(self, contact):
        id_, name, email, phone, address, city, category, created = contact
        
        info = f"""
Name: {name}
Email: {email or '-'}
Phone: {phone or '-'}
Address: {address or '-'}
City: {city or '-'}
Category: {category or '-'}
Created: {created}
        """
        
        QMessageBox.information(self, "Contact Details", info.strip())
    
    def call_contact(self, phone):
        if phone:
            QMessageBox.information(self, "Call", f"Calling {phone}...")
        else:
            QMessageBox.warning(self, "Error", "No phone number!")
    
    def search_contacts(self, text):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM contacts 
            WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?
            ORDER BY name
        ''', (f"%{text}%", f"%{text}%", f"%{text}%"))
        
        contacts = cursor.fetchall()
        conn.close()
        
        self.display_contacts(contacts)
    
    def filter_contacts(self):
        category = self.filter_category.currentData()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if category:
            cursor.execute(
                "SELECT * FROM contacts WHERE category = ? ORDER BY name",
                (category,)
            )
        else:
            cursor.execute("SELECT * FROM contacts ORDER BY name")
        
        contacts = cursor.fetchall()
        conn.close()
        
        self.display_contacts(contacts)
    
    def export_csv(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export CSV", "contacts.csv", "CSV Files (*.csv)"
        )
        
        if file_path:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contacts")
            contacts = cursor.fetchall()
            conn.close()
            
            with open(file_path, 'w') as f:
                f.write("ID,Name,Email,Phone,Address,City,Category,Created\n")
                for c in contacts:
                    f.write(','.join(str(x or '') for x in c) + '\n')
            
            QMessageBox.information(self, "Export", f"Exported {len(contacts)} contacts!")
    
    def import_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Import CSV", "", "CSV Files (*.csv)"
        )
        
        if file_path:
            import csv
            
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                count = 0
                for row in reader:
                    cursor.execute('''
                        INSERT INTO contacts (name, email, phone, address, city, category)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        row.get('Name', ''),
                        row.get('Email', ''),
                        row.get('Phone', ''),
                        row.get('Address', ''),
                        row.get('City', ''),
                        row.get('Category', '')
                    ))
                    count += 1
                
                conn.commit()
                conn.close()
            
            self.load_contacts()
            QMessageBox.information(self, "Import", f"Imported {count} contacts!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddressBook()
    window.show()
    sys.exit(app.exec_())
