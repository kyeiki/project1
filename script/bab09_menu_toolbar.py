# BAB 9: Menu & Toolbar
# =====================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLabel, QAction, QToolBar, QMessageBox)
from PyQt5.QtCore import Qt

class AplikasiKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi dengan Menu & Toolbar - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 400)
        
        # Label utama
        self.label = QLabel("Selamat datang! Pilih menu atau klik toolbar.")
        self.label.setStyleSheet("font-size: 18px; padding: 20px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)
        
        # === MENU BAR ===
        menubar = self.menuBar()
        
        # Menu File
        menu_file = menubar.addMenu("File")
        
        aksi_baru = QAction("Baru", self)
        aksi_baru.setShortcut("Ctrl+N")
        aksi_baru.setStatusTip("Buat file baru")
        aksi_baru.triggered.connect(self.file_baru)
        menu_file.addAction(aksi_baru)
        
        aksi_buka = QAction("Buka", self)
        aksi_buka.setShortcut("Ctrl+O")
        aksi_buka.triggered.connect(self.file_buka)
        menu_file.addAction(aksi_buka)
        
        aksi_simpan = QAction("Simpan", self)
        aksi_simpan.setShortcut("Ctrl+S")
        aksi_simpan.triggered.connect(self.file_simpan)
        menu_file.addAction(aksi_simpan)
        
        menu_file.addSeparator()
        
        aksi_keluar = QAction("Keluar", self)
        aksi_keluar.setShortcut("Ctrl+Q")
        aksi_keluar.triggered.connect(self.close)
        menu_file.addAction(aksi_keluar)
        
        # Menu Edit
        menu_edit = menubar.addMenu("Edit")
        
        aksi_undo = QAction("Undo", self)
        aksi_undo.setShortcut("Ctrl+Z")
        menu_edit.addAction(aksi_undo)
        
        aksi_redo = QAction("Redo", self)
        aksi_redo.setShortcut("Ctrl+Y")
        menu_edit.addAction(aksi_redo)
        
        # Menu Bantuan
        menu_bantuan = menubar.addMenu("Bantuan")
        
        aksi_tentang = QAction("Tentang", self)
        aksi_tentang.triggered.connect(self.tentang)
        menu_bantuan.addAction(aksi_tentang)
        
        # === TOOLBAR ===
        toolbar = QToolBar("Toolbar Utama")
        toolbar.setStyleSheet("QToolBar { spacing: 5px; padding: 5px; }")
        self.addToolBar(toolbar)
        
        aksi_tb_baru = QAction("📄 Baru", self)
        aksi_tb_baru.triggered.connect(self.file_baru)
        toolbar.addAction(aksi_tb_baru)
        
        aksi_tb_buka = QAction("📂 Buka", self)
        aksi_tb_buka.triggered.connect(self.file_buka)
        toolbar.addAction(aksi_tb_buka)
        
        aksi_tb_simpan = QAction("💾 Simpan", self)
        aksi_tb_simpan.triggered.connect(self.file_simpan)
        toolbar.addAction(aksi_tb_simpan)
        
        toolbar.addSeparator()
        
        aksi_tb_keluar = QAction("❌ Keluar", self)
        aksi_tb_keluar.triggered.connect(self.close)
        toolbar.addAction(aksi_tb_keluar)
        
        # === STATUS BAR ===
        self.statusBar().showMessage("Siap")
    
    def file_baru(self):
        self.label.setText("📄 File baru dibuat!")
        self.statusBar().showMessage("File baru dibuat")
    
    def file_buka(self):
        self.label.setText("📂 Membuka file...")
        self.statusBar().showMessage("Membuka file")
    
    def file_simpan(self):
        self.label.setText("💾 File disimpan!")
        self.statusBar().showMessage("File disimpan", 3000)
    
    def tentang(self):
        QMessageBox.about(self, "Tentang", 
            "Aplikasi Demo PyQt5\n"
            "Versi 1.0\n\n"
            "Dibuat untuk pembelajaran\n"
            "PyQt5 dari 0 to Hero!")

app = QApplication(sys.argv)
jendela = AplikasiKu()
jendela.show()
sys.exit(app.exec_())
