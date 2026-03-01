# BAB 12: Input Angka - Spin dan Dial
# ================================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QSpinBox, QDoubleSpinBox, QDial,
                              QLabel, QVBoxLayout, QWidget)

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spin & Dial Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 350, 400)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # SpinBox - Integer
        layout.addWidget(QLabel("Jumlah (Integer):"))
        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 100)
        self.spinbox.setValue(1)
        self.spinbox.setPrefix("Qty: ")
        self.spinbox.setSuffix(" pcs")
        self.spinbox.valueChanged.connect(self.spin_berubah)
        layout.addWidget(self.spinbox)
        
        # DoubleSpinBox - Decimal
        layout.addWidget(QLabel("Harga (Decimal):"))
        self.doublespin = QDoubleSpinBox()
        self.doublespin.setRange(0.0, 1000000.0)
        self.doublespin.setDecimals(2)
        self.doublespin.setPrefix("Rp ")
        self.doublespin.setSingleStep(1000)
        layout.addWidget(self.doublespin)
        
        # Dial
        layout.addWidget(QLabel("Volume:"))
        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.setValue(50)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.dial_berubah)
        layout.addWidget(self.dial)
        
        # Label hasil
        self.label = QLabel("Volume: 50%")
        self.label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(self.label)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def spin_berubah(self, nilai):
        print(f"Qty: {nilai}")
    
    def dial_berubah(self, nilai):
        self.label.setText(f"Volume: {nilai}%")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
