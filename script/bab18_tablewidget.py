# BAB 18: TableWidget (Tabel)
# ============================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTableWidget, QTableWidgetItem, QLineEdit,
                              QPushButton, QLabel, QVBoxLayout, 
                              QHBoxLayout, QWidget, QHeaderView)
from PyQt5.QtCore import Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TableWidget Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 450)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📊 DATA MAHASISWA")
        header.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        layout.addWidget(header)
        
        # Input form
        input_layout = QHBoxLayout()
        
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("NIM")
        input_layout.addWidget(self.input_nim)
        
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Nama")
        input_layout.addWidget(self.input_nama)
        
        self.input_nilai = QLineEdit()
        self.input_nilai.setPlaceholderText("Nilai (0-100)")
        self.input_nilai.setFixedWidth(100)
        input_layout.addWidget(self.input_nilai)
        
        btn_add = QPushButton("➕ Tambah")
        btn_add.clicked.connect(self.tambah_baris)
        input_layout.addWidget(btn_add)
        
        layout.addLayout(input_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["NIM", "Nama", "Nilai", "Grade"])
        
        # Header stretch
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        # Sample data
        data = [
            ("12345", "Andi Pratama", 85),
            ("12346", "Budi Santoso", 75),
            ("12347", "Caca Wijaya", 90),
            ("12348", "Doni Putra", 65),
        ]
        
        for row, (nim, nama, nilai) in enumerate(data):
            self.add_row(row, nim, nama, nilai)
        
        layout.addWidget(self.table)
        
        # Stats
        self.label_stats = QLabel()
        self.update_stats()
        layout.addWidget(self.label_stats)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        btn_delete = QPushButton("🗑️ Hapus Baris")
        btn_delete.clicked.connect(self.hapus_baris)
        btn_layout.addWidget(btn_delete)
        
        btn_clear = QPushButton("🧹 Clear All")
        btn_clear.clicked.connect(self.clear_table)
        btn_layout.addWidget(btn_clear)
        
        layout.addLayout(btn_layout)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def add_row(self, row, nim, nama, nilai):
        self.table.insertRow(row)
        
        grade = self.hitung_grade(nilai)
        
        self.table.setItem(row, 0, QTableWidgetItem(nim))
        self.table.setItem(row, 1, QTableWidgetItem(nama))
        
        item_nilai = QTableWidgetItem(str(nilai))
        # Warna berdasarkan nilai
        if nilai >= 85:
            item_nilai.setBackground(Qt.green)
        elif nilai >= 70:
            item_nilai.setBackground(Qt.yellow)
        else:
            item_nilai.setBackground(Qt.red)
        self.table.setItem(row, 2, item_nilai)
        
        self.table.setItem(row, 3, QTableWidgetItem(grade))
    
    def tambah_baris(self):
        nim = self.input_nim.text().strip()
        nama = self.input_nama.text().strip()
        nilai_text = self.input_nilai.text().strip()
        
        if nim and nama and nilai_text:
            try:
                nilai = int(nilai_text)
                if 0 <= nilai <= 100:
                    row = self.table.rowCount()
                    self.add_row(row, nim, nama, nilai)
                    
                    self.input_nim.clear()
                    self.input_nama.clear()
                    self.input_nilai.clear()
                    self.update_stats()
            except ValueError:
                pass
    
    def hitung_grade(self, nilai):
        if nilai >= 85: return "A"
        elif nilai >= 70: return "B"
        elif nilai >= 55: return "C"
        elif nilai >= 40: return "D"
        else: return "E"
    
    def hapus_baris(self):
        current = self.table.currentRow()
        if current >= 0:
            self.table.removeRow(current)
            self.update_stats()
    
    def clear_table(self):
        self.table.setRowCount(0)
        self.update_stats()
    
    def update_stats(self):
        count = self.table.rowCount()
        total_nilai = 0
        for row in range(count):
            try:
                nilai = int(self.table.item(row, 2).text())
                total_nilai += nilai
            except:
                pass
        
        rata = total_nilai / count if count > 0 else 0
        self.label_stats.setText(f"📊 Total: {count} mahasiswa | Rata-rata: {rata:.1f}")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
