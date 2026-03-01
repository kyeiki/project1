# BAB 48: Proyek Akhir - File Manager Mini
# =========================================
# Simple file manager dengan tree dan list view

import sys
import os
import shutil
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTreeView, QListView, QListWidget,
                              QListWidgetItem, QLabel, QPushButton,
                              QLineEdit, QVBoxLayout, QHBoxLayout,
                              QWidget, QSplitter, QMessageBox,
                              QMenu, QAction, QFileDialog, QFileIconProvider,
                              QInputDialog)
from PyQt5.QtCore import Qt, QDir, QFileInfo, QSize
from PyQt5.QtGui import QIcon


class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📁 File Manager Mini - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 900, 600)
        
        self.current_path = QDir.homePath()
        self.icon_provider = QFileIconProvider()
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QListWidget {
                background-color: white;
                border: 1px solid #ddd;
            }
            QListWidget::item {
                padding: 5px;
            }
            QListWidget::item:selected {
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
            }
        """)
        
        self.setup_ui()
        self.load_directory(self.current_path)
    
    def setup_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Toolbar
        toolbar = QHBoxLayout()
        
        btn_back = QPushButton("⬅ Back")
        btn_back.clicked.connect(self.go_back)
        toolbar.addWidget(btn_back)
        
        btn_up = QPushButton("⬆ Up")
        btn_up.clicked.connect(self.go_up)
        toolbar.addWidget(btn_up)
        
        btn_home = QPushButton("🏠 Home")
        btn_home.clicked.connect(self.go_home)
        toolbar.addWidget(btn_home)
        
        btn_refresh = QPushButton("🔄 Refresh")
        btn_refresh.clicked.connect(self.refresh)
        toolbar.addWidget(btn_refresh)
        
        toolbar.addStretch()
        
        btn_new_folder = QPushButton("📁 New Folder")
        btn_new_folder.clicked.connect(self.new_folder)
        toolbar.addWidget(btn_new_folder)
        
        btn_new_file = QPushButton("📄 New File")
        btn_new_file.clicked.connect(self.new_file)
        toolbar.addWidget(btn_new_file)
        
        layout.addLayout(toolbar)
        
        # Path bar
        path_layout = QHBoxLayout()
        
        path_layout.addWidget(QLabel("Path:"))
        self.path_input = QLineEdit()
        self.path_input.returnPressed.connect(self.navigate_to_path)
        path_layout.addWidget(self.path_input)
        
        btn_go = QPushButton("Go")
        btn_go.clicked.connect(self.navigate_to_path)
        path_layout.addWidget(btn_go)
        
        layout.addLayout(path_layout)
        
        # Main content (splitter)
        splitter = QSplitter(Qt.Horizontal)
        
        # Left: Quick access
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        left_layout.addWidget(QLabel("Quick Access:"))
        
        self.quick_access = QListWidget()
        self.quick_access.setFixedWidth(150)
        
        quick_items = [
            ("🏠 Home", QDir.homePath()),
            ("📄 Documents", QDir.homePath() + "/Documents"),
            ("Downloads", QDir.homePath() + "/Downloads"),
            ("Desktop", QDir.homePath() + "/Desktop"),
            ("📁 Root", "/"),
        ]
        
        for name, path in quick_items:
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, path)
            self.quick_access.addItem(item)
        
        self.quick_access.itemClicked.connect(self.quick_access_click)
        left_layout.addWidget(self.quick_access)
        
        left_panel.setLayout(left_layout)
        splitter.addWidget(left_panel)
        
        # Right: File list
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        
        right_layout.addWidget(QLabel("Contents:"))
        
        self.file_list = QListWidget()
        self.file_list.setViewMode(QListWidget.IconMode)
        self.file_list.setIconSize(QSize(48, 48))
        self.file_list.setResizeMode(QListWidget.Adjust)
        self.file_list.itemDoubleClicked.connect(self.item_double_click)
        self.file_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.file_list.customContextMenuRequested.connect(self.show_context_menu)
        right_layout.addWidget(self.file_list)
        
        right_panel.setLayout(right_layout)
        splitter.addWidget(right_panel)
        
        # Set splitter sizes
        splitter.setSizes([150, 750])
        
        layout.addWidget(splitter)
        
        # Status bar
        self.status = QLabel("Ready")
        self.status.setStyleSheet("padding: 5px;")
        layout.addWidget(self.status)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.path_history = []
    
    def load_directory(self, path):
        if not os.path.exists(path):
            QMessageBox.warning(self, "Error", f"Directory not found: {path}")
            return
        
        self.current_path = os.path.abspath(path)
        self.path_input.setText(self.current_path)
        
        self.file_list.clear()
        
        try:
            entries = os.listdir(self.current_path)
            
            # Sort: folders first, then files
            folders = []
            files = []
            
            for entry in entries:
                full_path = os.path.join(self.current_path, entry)
                if os.path.isdir(full_path):
                    folders.append(entry)
                else:
                    files.append(entry)
            
            folders.sort(key=str.lower)
            files.sort(key=str.lower)
            
            # Add folders
            for folder in folders:
                full_path = os.path.join(self.current_path, folder)
                item = QListWidgetItem(f"📁 {folder}")
                item.setData(Qt.UserRole, full_path)
                item.setData(Qt.UserRole + 1, "folder")
                icon = self.icon_provider.icon(QFileInfo(full_path))
                item.setIcon(icon)
                self.file_list.addItem(item)
            
            # Add files
            for file in files:
                full_path = os.path.join(self.current_path, file)
                item = QListWidgetItem(file)
                item.setData(Qt.UserRole, full_path)
                item.setData(Qt.UserRole + 1, "file")
                icon = self.icon_provider.icon(QFileInfo(full_path))
                item.setIcon(icon)
                self.file_list.addItem(item)
            
            total = len(folders) + len(files)
            self.status.setText(f"{len(folders)} folders, {len(files)} files | {self.current_path}")
            
        except PermissionError:
            QMessageBox.warning(self, "Error", "Permission denied!")
            self.status.setText("Permission denied!")
    
    def navigate_to_path(self):
        path = self.path_input.text()
        if os.path.exists(path):
            self.path_history.append(self.current_path)
            self.load_directory(path)
        else:
            QMessageBox.warning(self, "Error", "Path not found!")
    
    def go_back(self):
        if self.path_history:
            path = self.path_history.pop()
            self.load_directory(path)
    
    def go_up(self):
        parent = os.path.dirname(self.current_path)
        if parent and parent != self.current_path:
            self.path_history.append(self.current_path)
            self.load_directory(parent)
    
    def go_home(self):
        self.path_history.append(self.current_path)
        self.load_directory(QDir.homePath())
    
    def refresh(self):
        self.load_directory(self.current_path)
    
    def quick_access_click(self, item):
        path = item.data(Qt.UserRole)
        if os.path.exists(path):
            self.path_history.append(self.current_path)
            self.load_directory(path)
    
    def item_double_click(self, item):
        path = item.data(Qt.UserRole)
        item_type = item.data(Qt.UserRole + 1)
        
        if item_type == "folder":
            self.path_history.append(self.current_path)
            self.load_directory(path)
        else:
            # Open file with system default
            import subprocess
            if sys.platform == 'win32':
                os.startfile(path)
            elif sys.platform == 'darwin':
                subprocess.run(['open', path])
            else:
                subprocess.run(['xdg-open', path])
    
    def show_context_menu(self, position):
        item = self.file_list.itemAt(position)
        
        menu = QMenu()
        
        if item:
            path = item.data(Qt.UserRole)
            
            action_open = QAction("Open", self)
            action_open.triggered.connect(lambda: self.item_double_click(item))
            menu.addAction(action_open)
            
            menu.addSeparator()
            
            action_copy = QAction("Copy", self)
            action_copy.triggered.connect(lambda: self.copy_item(path))
            menu.addAction(action_copy)
            
            action_cut = QAction("Cut", self)
            action_cut.triggered.connect(lambda: self.cut_item(path))
            menu.addAction(action_cut)
            
            action_rename = QAction("Rename", self)
            action_rename.triggered.connect(lambda: self.rename_item(path))
            menu.addAction(action_rename)
            
            menu.addSeparator()
            
            action_delete = QAction("Delete", self)
            action_delete.triggered.connect(lambda: self.delete_item(path))
            menu.addAction(action_delete)
        else:
            # Context menu for empty space
            action_new_folder = QAction("New Folder", self)
            action_new_folder.triggered.connect(self.new_folder)
            menu.addAction(action_new_folder)
            
            action_new_file = QAction("New File", self)
            action_new_file.triggered.connect(self.new_file)
            menu.addAction(action_new_file)
            
            menu.addSeparator()
            
            action_refresh = QAction("Refresh", self)
            action_refresh.triggered.connect(self.refresh)
            menu.addAction(action_refresh)
        
        menu.exec_(self.file_list.mapToGlobal(position))
    
    def new_folder(self):
        name, ok = QInputDialog.getText(self, "New Folder", "Folder name:")
        if ok and name:
            path = os.path.join(self.current_path, name)
            try:
                os.mkdir(path)
                self.refresh()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
    
    def new_file(self):
        name, ok = QInputDialog.getText(self, "New File", "File name:")
        if ok and name:
            path = os.path.join(self.current_path, name)
            try:
                open(path, 'w').close()
                self.refresh()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
    
    def copy_item(self, path):
        self.clipboard = ("copy", path)
        self.status.setText(f"Copied: {os.path.basename(path)}")
    
    def cut_item(self, path):
        self.clipboard = ("cut", path)
        self.status.setText(f"Cut: {os.path.basename(path)}")
    
    def paste(self):
        if hasattr(self, 'clipboard'):
            operation, src = self.clipboard
            name = os.path.basename(src)
            dst = os.path.join(self.current_path, name)
            
            try:
                if operation == "copy":
                    if os.path.isdir(src):
                        shutil.copytree(src, dst)
                    else:
                        shutil.copy2(src, dst)
                else:  # cut
                    shutil.move(src, dst)
                
                self.refresh()
                self.status.setText(f"Pasted: {name}")
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
    
    def rename_item(self, path):
        old_name = os.path.basename(path)
        new_name, ok = QInputDialog.getText(self, "Rename", "New name:", text=old_name)
        
        if ok and new_name and new_name != old_name:
            new_path = os.path.join(os.path.dirname(path), new_name)
            try:
                os.rename(path, new_path)
                self.refresh()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
    
    def delete_item(self, path):
        name = os.path.basename(path)
        
        reply = QMessageBox.question(
            self, "Confirm Delete",
            f"Delete '{name}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                self.refresh()
                self.status.setText(f"Deleted: {name}")
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec_())
