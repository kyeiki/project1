# BAB 13: Radio Button
# =====================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QRadioButton, QButtonGroup, QLabel,
                              QVBoxLayout, QHBoxLayout, QWidget, QGroupBox)

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadioButton Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 400, 300)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Grup 1: Ukuran
        grup_ukuran = QGroupBox("Pilih Ukuran:")
        layout_ukuran = QVBoxLayout()
        
        self.bg_ukuran = QButtonGroup()
        self.rb_s = QRadioButton("S (Small)")
        self.rb_m = QRadioButton("M (Medium)")
        self.rb_l = QRadioButton("L (Large)")
        self.rb_xl = QRadioButton("XL (Extra Large)")
        
        self.bg_ukuran.addButton(self.rb_s, 1)
        self.bg_ukuran.addButton(self.rb_m, 2)
        self.bg_ukuran.addButton(self.rb_l, 3)
        self.bg_ukuran.addButton(self.rb_xl, 4)
        self.rb_m.setChecked(True)  # Default
        
        layout_ukuran.addWidget(self.rb_s)
        layout_ukuran.addWidget(self.rb_m)
        layout_ukuran.addWidget(self.rb_l)
        layout_ukuran.addWidget(self.rb_xl)
        grup_ukuran.setLayout(layout_ukuran)
        
        # Grup 2: Warna
        grup_warna = QGroupBox("Pilih Warna:")
        layout_warna = QVBoxLayout()
        
        self.bg_warna = QButtonGroup()
        self.rb_merah = QRadioButton("🔴 Merah")
        self.rb_hijau = QRadioButton("🟢 Hijau")
        self.rb_biru = QRadioButton("🔵 Biru")
        self.rb_kuning = QRadioButton("🟡 Kuning")
        
        self.bg_warna.addButton(self.rb_merah, 1)
        self.bg_warna.addButton(self.rb_hijau, 2)
        self.bg_warna.addButton(self.rb_biru, 3)
        self.bg_warna.addButton(self.rb_kuning, 4)
        self.rb_merah.setChecked(True)
        
        layout_warna.addWidget(self.rb_merah)
        layout_warna.addWidget(self.rb_hijau)
        layout_warna.addWidget(self.rb_biru)
        layout_warna.addWidget(self.rb_kuning)
        grup_warna.setLayout(layout_warna)
        
        # Layout horizontal untuk 2 grup
        layout_h = QHBoxLayout()
        layout_h.addWidget(grup_ukuran)
        layout_h.addWidget(grup_warna)
        layout.addLayout(layout_h)
        
        # Label hasil
        self.hasil = QLabel("Ukuran: M | Warna: Merah")
        self.hasil.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(self.hasil)
        
        # Connect signals
        self.bg_ukuran.buttonClicked.connect(self.update_hasil)
        self.bg_warna.buttonClicked.connect(self.update_hasil)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def update_hasil(self):
        ukuran_map = {1: "S", 2: "M", 3: "L", 4: "XL"}
        warna_map = {1: "Merah", 2: "Hijau", 3: "Biru", 4: "Kuning"}
        
        ukuran = ukuran_map.get(self.bg_ukuran.checkedId(), "-")
        warna = warna_map.get(self.bg_warna.checkedId(), "-")
        
        self.hasil.setText(f"Ukuran: {ukuran} | Warna: {warna}")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
