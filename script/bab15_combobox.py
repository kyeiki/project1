# BAB 15: ComboBox (Dropdown)
# ============================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QComboBox, QLabel, QPushButton,
                              QVBoxLayout, QHBoxLayout, QWidget)

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # ComboBox dengan teks saja
        layout.addWidget(QLabel("Pilih Kota:"))
        self.combo_kota = QComboBox()
        self.combo_kota.addItems([
            "Jakarta",
            "Bandung", 
            "Surabaya",
            "Yogyakarta",
            "Semarang",
            "Malang",
            "Bali"
        ])
        self.combo_kota.currentTextChanged.connect(self.kota_dipilih)
        layout.addWidget(self.combo_kota)
        
        # ComboBox dengan data tersembunyi
        layout.addWidget(QLabel("\nPilih Produk:"))
        self.combo_produk = QComboBox()
        
        # Format: (nama, harga)
        produk = [
            ("Laptop ASUS ROG", 15000000),
            ("MacBook Air M2", 18000000),
            ("Dell XPS 15", 20000000),
            ("Lenovo ThinkPad", 12000000),
            ("HP Spectre", 16500000),
        ]
        
        for nama, harga in produk:
            self.combo_produk.addItem(f"{nama}", harga)
        
        self.combo_produk.currentIndexChanged.connect(self.produk_dipilih)
        layout.addWidget(self.combo_produk)
        
        # Label harga
        self.label_harga = QLabel("Harga: Rp 15,000,000")
        self.label_harga.setStyleSheet("font-size: 16px; font-weight: bold; color: #2980b9;")
        layout.addWidget(self.label_harga)
        
        # ComboBox editable
        layout.addWidget(QLabel("\nComboBox Editable:"))
        self.combo_edit = QComboBox()
        self.combo_edit.setEditable(True)
        self.combo_edit.addItems(["Java", "Python", "JavaScript", "C++", "Go"])
        self.combo_edit.setInsertPolicy(QComboBox.InsertAtTop)
        layout.addWidget(self.combo_edit)
        
        # Tombol tambah
        btn = QPushButton("Tambah Bahasa Baru")
        btn.clicked.connect(lambda: self.combo_edit.addItem(self.combo_edit.currentText()))
        layout.addWidget(btn)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def kota_dipilih(self, kota):
        print(f"Kota dipilih: {kota}")
    
    def produk_dipilih(self, index):
        harga = self.combo_produk.itemData(index)
        nama = self.combo_produk.itemText(index)
        self.label_harga.setText(f"Harga: Rp {harga:,}")
        print(f"Produk: {nama}, Harga: {harga}")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
