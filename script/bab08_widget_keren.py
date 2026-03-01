# BAB 8: Widget Keren
# ===================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QComboBox, QSlider, QProgressBar,
                              QCheckBox, QRadioButton, QLabel, QPushButton,
                              QVBoxLayout, QHBoxLayout, QWidget, QGroupBox)
from PyQt5.QtCore import Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Keren - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 450, 500)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # === COMBOBOX ===
        grup_combo = QGroupBox("Pilih Warna Favorit:")
        layout_combo = QVBoxLayout()
        
        self.combo = QComboBox()
        self.combo.addItems(["Merah", "Hijau", "Biru", "Kuning", "Ungu"])
        self.combo.currentTextChanged.connect(self.warna_dipilih)
        layout_combo.addWidget(self.combo)
        
        self.label_warna = QLabel("Warna: -")
        layout_combo.addWidget(self.label_warna)
        
        grup_combo.setLayout(layout_combo)
        layout.addWidget(grup_combo)
        
        # === SLIDER & PROGRESS ===
        grup_slider = QGroupBox("Slider & Progress:")
        layout_slider = QVBoxLayout()
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.nilai_berubah)
        layout_slider.addWidget(self.slider)
        
        self.label_nilai = QLabel("Nilai: 50")
        self.label_nilai.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout_slider.addWidget(self.label_nilai)
        
        self.progress = QProgressBar()
        self.progress.setValue(50)
        layout_slider.addWidget(self.progress)
        
        grup_slider.setLayout(layout_slider)
        layout.addWidget(grup_slider)
        
        # === CHECKBOX & RADIO ===
        grup_pilihan = QGroupBox("Pilihan:")
        layout_pilihan = QHBoxLayout()
        
        # Checkbox
        layout_cb = QVBoxLayout()
        self.cb1 = QCheckBox("Membaca")
        self.cb2 = QCheckBox("Gaming")
        self.cb3 = QCheckBox("Olahraga")
        layout_cb.addWidget(self.cb1)
        layout_cb.addWidget(self.cb2)
        layout_cb.addWidget(self.cb3)
        
        # Radio
        layout_rb = QVBoxLayout()
        self.rb1 = QRadioButton("Laki-laki")
        self.rb2 = QRadioButton("Perempuan")
        layout_rb.addWidget(self.rb1)
        layout_rb.addWidget(self.rb2)
        
        layout_pilihan.addLayout(layout_cb)
        layout_pilihan.addLayout(layout_rb)
        
        grup_pilihan.setLayout(layout_pilihan)
        layout.addWidget(grup_pilihan)
        
        # Tombol tampilkan
        tombol = QPushButton("Tampilkan Pilihan")
        tombol.clicked.connect(self.tampilkan)
        layout.addWidget(tombol)
        
        self.hasil = QLabel("Hasil: -")
        self.hasil.setStyleSheet("font-weight: bold; color: #2c3e50;")
        layout.addWidget(self.hasil)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def warna_dipilih(self, warna):
        warna_map = {
            "Merah": "#e74c3c",
            "Hijau": "#27ae60", 
            "Biru": "#3498db",
            "Kuning": "#f1c40f",
            "Ungu": "#9b59b6"
        }
        self.label_warna.setText(f"Warna: {warna}")
        self.label_warna.setStyleSheet(f"color: {warna_map.get(warna, 'black')}; font-weight: bold; font-size: 18px;")
    
    def nilai_berubah(self, nilai):
        self.label_nilai.setText(f"Nilai: {nilai}")
        self.progress.setValue(nilai)
    
    def tampilkan(self):
        hobi = []
        if self.cb1.isChecked(): hobi.append("Membaca")
        if self.cb2.isChecked(): hobi.append("Gaming")
        if self.cb3.isChecked(): hobi.append("Olahraga")
        
        gender = "-"
        if self.rb1.isChecked(): gender = "Laki-laki"
        elif self.rb2.isChecked(): gender = "Perempuan"
        
        self.hasil.setText(f"Gender: {gender} | Hobi: {', '.join(hobi) if hobi else 'Tidak ada'}")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
