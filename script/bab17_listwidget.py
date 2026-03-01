# BAB 17: ListWidget (Daftar)
# ============================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QListWidget, QListWidgetItem, QLineEdit,
                              QPushButton, QLabel, QVBoxLayout, 
                              QHBoxLayout, QWidget)

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ListWidget Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 450)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("📝 DAFTAR TUGAS")
        header.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        layout.addWidget(header)
        
        # Input area
        input_layout = QHBoxLayout()
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Tambah tugas baru...")
        self.input.returnPressed.connect(self.tambah_item)
        input_layout.addWidget(self.input)
        
        btn_add = QPushButton("➕")
        btn_add.setFixedWidth(50)
        btn_add.clicked.connect(self.tambah_item)
        input_layout.addWidget(btn_add)
        
        layout.addLayout(input_layout)
        
        # List widget
        self.list = QListWidget()
        self.list.addItems([
            "Belajar PyQt5",
            "Kerjakan tugas matematika",
            "Meeting jam 14:00",
            "Review kode project"
        ])
        self.list.currentItemChanged.connect(self.item_dipilih)
        self.list.itemDoubleClicked.connect(self.item_double_click)
        layout.addWidget(self.list)
        
        # Info label
        self.label_info = QLabel("Total: 4 item | Klik item untuk memilih")
        layout.addWidget(self.label_info)
        
        # Button area
        btn_layout = QHBoxLayout()
        
        btn_edit = QPushButton("✏️ Edit")
        btn_edit.clicked.connect(self.edit_item)
        btn_layout.addWidget(btn_edit)
        
        btn_delete = QPushButton("🗑️ Hapus")
        btn_delete.clicked.connect(self.hapus_item)
        btn_layout.addWidget(btn_delete)
        
        btn_clear = QPushButton("🧹 Clear")
        btn_clear.clicked.connect(self.clear_all)
        btn_layout.addWidget(btn_clear)
        
        layout.addLayout(btn_layout)
        
        # Selection mode
        btn_select_all = QPushButton("Pilih Semua")
        btn_select_all.clicked.connect(lambda: self.list.selectAll())
        layout.addWidget(btn_select_all)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.update_info()
    
    def tambah_item(self):
        text = self.input.text().strip()
        if text:
            self.list.addItem(text)
            self.input.clear()
            self.update_info()
    
    def item_dipilih(self, current, previous):
        if current:
            self.label_info.setText(f"Dipilih: {current.text()}")
    
    def item_double_click(self, item):
        self.label_info.setText(f"Double click: {item.text()}")
    
    def edit_item(self):
        current = self.list.currentItem()
        if current:
            self.input.setText(current.text())
            self.list.takeItem(self.list.row(current))
            self.update_info()
    
    def hapus_item(self):
        current = self.list.currentRow()
        if current >= 0:
            self.list.takeItem(current)
            self.update_info()
    
    def clear_all(self):
        self.list.clear()
        self.update_info()
    
    def update_info(self):
        count = self.list.count()
        self.label_info.setText(f"Total: {count} item")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
