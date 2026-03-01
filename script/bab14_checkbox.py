# BAB 14: CheckBox
# ================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QCheckBox, QLabel, QPushButton,
                              QVBoxLayout, QWidget, QGroupBox)
from PyQt5.QtCore import Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 350, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Grup Topping
        grup_topping = QGroupBox("Pilih Topping Pizza:")
        layout_topping = QVBoxLayout()
        
        self.cb_keju = QCheckBox("🧀 Extra Keju (+Rp 10.000)")
        self.cb_jamur = QCheckBox("🍄 Jamur (+Rp 8.000)")
        self.cb_daging = QCheckBox("🥩 Daging Sapi (+Rp 20.000)")
        self.cb_sosis = QCheckBox("🌭 Sosis (+Rp 12.000)")
        self.cb_sayur = QCheckBox("🥬 Sayuran (+Rp 5.000)")
        
        layout_topping.addWidget(self.cb_keju)
        layout_topping.addWidget(self.cb_jamur)
        layout_topping.addWidget(self.cb_daging)
        layout_topping.addWidget(self.cb_sosis)
        layout_topping.addWidget(self.cb_sayur)
        grup_topping.setLayout(layout_topping)
        layout.addWidget(grup_topping)
        
        # Tristate checkbox
        self.cb_semua = QCheckBox("Pilih Semua (Tristate)")
        self.cb_semua.setTristate(True)
        self.cb_semua.stateChanged.connect(self.pilih_semua)
        layout.addWidget(self.cb_semua)
        
        # Tombol
        btn = QPushButton("Hitung Total")
        btn.clicked.connect(self.hitung_total)
        btn.setStyleSheet("padding: 10px; font-size: 14px;")
        layout.addWidget(btn)
        
        # Hasil
        self.hasil = QLabel("Total: Rp 0")
        self.hasil.setStyleSheet("font-size: 18px; font-weight: bold; color: #27ae60;")
        layout.addWidget(self.hasil)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def pilih_semua(self, state):
        checked = state == Qt.Checked
        self.cb_keju.setChecked(checked)
        self.cb_jamur.setChecked(checked)
        self.cb_daging.setChecked(checked)
        self.cb_sosis.setChecked(checked)
        self.cb_sayur.setChecked(checked)
    
    def hitung_total(self):
        total = 50000  # Harga dasar pizza
        
        if self.cb_keju.isChecked():
            total += 10000
        if self.cb_jamur.isChecked():
            total += 8000
        if self.cb_daging.isChecked():
            total += 20000
        if self.cb_sosis.isChecked():
            total += 12000
        if self.cb_sayur.isChecked():
            total += 5000
        
        self.hasil.setText(f"Total: Rp {total:,}")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
