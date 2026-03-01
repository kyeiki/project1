# BAB 21: Splitter
# ================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QSplitter, QListWidget, QTextEdit,
                              QTreeView, QFileSystemModel, QLabel,
                              QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt, QDir

class SplitterDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Splitter Demo - File Explorer - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 800, 500)
        
        # Main splitter (horizontal)
        main_splitter = QSplitter(Qt.Horizontal)
        
        # Panel kiri: File tree
        self.tree = QTreeView()
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.homePath()))
        self.tree.setColumnHidden(1, True)  # Hide size column
        self.tree.setColumnHidden(2, True)  # Hide type column
        self.tree.setColumnHidden(3, True)  # Hide date column
        self.tree.clicked.connect(self.file_clicked)
        
        main_splitter.addWidget(self.tree)
        
        # Panel kanan: Vertical splitter
        right_splitter = QSplitter(Qt.Vertical)
        
        # Preview area
        self.preview = QTextEdit()
        self.preview.setReadOnly(True)
        self.preview.setPlaceholderText("Pilih file untuk melihat preview...")
        right_splitter.addWidget(self.preview)
        
        # Info area
        info_widget = QWidget()
        info_layout = QVBoxLayout()
        
        info_label = QLabel("📁 INFO FILE")
        info_label.setStyleSheet("font-weight: bold;")
        info_layout.addWidget(info_label)
        
        self.info = QLabel("Pilih file di panel kiri")
        self.info.setWordWrap(True)
        info_layout.addWidget(self.info)
        
        info_widget.setLayout(info_layout)
        right_splitter.addWidget(info_widget)
        
        # Set ukuran proporsi
        right_splitter.setSizes([350, 100])
        
        main_splitter.addWidget(right_splitter)
        
        # Set ukuran proporsi
        main_splitter.setSizes([200, 600])
        
        self.setCentralWidget(main_splitter)
    
    def file_clicked(self, index):
        path = self.model.filePath(index)
        is_dir = self.model.isDir(index)
        
        if is_dir:
            self.preview.setPlainText(f"📁 Folder: {path}")
            self.info.setText(f"Jenis: Folder\nPath: {path}")
        else:
            # Coba baca file teks
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(5000)  # Limit 5000 chars
                    self.preview.setPlainText(content)
            except:
                self.preview.setPlainText(f"❌ Tidak dapat membaca file: {path}")
            
            # Info file
            file_info = self.model.fileInfo(index)
            size = file_info.size()
            ext = file_info.suffix()
            
            self.info.setText(f"Nama: {file_info.fileName()}\n"
                            f"Ukuran: {size:,} bytes\n"
                            f"Ekstensi: {ext if ext else '-'}\n"
                            f"Path: {path}")

app = QApplication(sys.argv)
window = SplitterDemo()
window.show()
sys.exit(app.exec_())
