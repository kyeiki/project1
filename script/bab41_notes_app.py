# BAB 41: Proyek Akhir - Notes App
# =================================
# Aplikasi catatan lengkap dengan fitur CRUD

import sys
import json
import os
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTextEdit, QListWidget, QListWidgetItem,
                              QLineEdit, QPushButton, QLabel,
                              QVBoxLayout, QHBoxLayout, QWidget,
                              QSplitter, QMessageBox, QInputDialog,
                              QFileDialog)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon

class Note:
    """Model untuk satu catatan"""
    def __init__(self, title="", content="", created=None, modified=None):
        self.title = title
        self.content = content
        self.created = created or datetime.now().isoformat()
        self.modified = modified or datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "created": self.created,
            "modified": self.modified
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title", ""),
            content=data.get("content", ""),
            created=data.get("created"),
            modified=data.get("modified")
        )


class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📝 Notes App - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 800, 600)
        
        self.notes = []
        self.current_note = None
        self.file_path = os.path.join(os.path.dirname(__file__), "notes.json")
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QListWidget {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton {
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        
        self.setup_ui()
        self.load_notes()
    
    def setup_ui(self):
        # Main widget
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Header
        header = QLabel("📝 MY NOTES")
        header.setStyleSheet("font-size: 24px; font-weight: bold; padding: 10px;")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)
        
        # Toolbar
        toolbar = QHBoxLayout()
        
        btn_new = QPushButton("➕ New")
        btn_new.setStyleSheet("background-color: #27ae60; color: white;")
        btn_new.clicked.connect(self.new_note)
        toolbar.addWidget(btn_new)
        
        btn_delete = QPushButton("🗑️ Delete")
        btn_delete.setStyleSheet("background-color: #e74c3c; color: white;")
        btn_delete.clicked.connect(self.delete_note)
        toolbar.addWidget(btn_delete)
        
        btn_save = QPushButton("💾 Save")
        btn_save.setStyleSheet("background-color: #3498db; color: white;")
        btn_save.clicked.connect(self.save_current_note)
        toolbar.addWidget(btn_save)
        
        toolbar.addStretch()
        
        btn_export = QPushButton("📤 Export")
        btn_export.clicked.connect(self.export_note)
        toolbar.addWidget(btn_export)
        
        btn_import = QPushButton("📥 Import")
        btn_import.clicked.connect(self.import_notes)
        toolbar.addWidget(btn_import)
        
        main_layout.addLayout(toolbar)
        
        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel - Notes list
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        # Search
        self.search = QLineEdit()
        self.search.setPlaceholderText("🔍 Search notes...")
        self.search.textChanged.connect(self.filter_notes)
        left_layout.addWidget(self.search)
        
        # Notes list
        self.notes_list = QListWidget()
        self.notes_list.currentItemChanged.connect(self.on_note_selected)
        left_layout.addWidget(self.notes_list)
        
        # Stats
        self.stats = QLabel("0 notes")
        self.stats.setStyleSheet("color: gray; padding: 5px;")
        left_layout.addWidget(self.stats)
        
        left_panel.setLayout(left_layout)
        splitter.addWidget(left_panel)
        
        # Right panel - Note editor
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        
        # Title
        self.title = QLineEdit()
        self.title.setPlaceholderText("Note title...")
        self.title.textChanged.connect(self.mark_modified)
        right_layout.addWidget(self.title)
        
        # Meta info
        self.meta = QLabel("Created: - | Modified: -")
        self.meta.setStyleSheet("color: gray; font-size: 11px;")
        right_layout.addWidget(self.meta)
        
        # Editor
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Write your note here...")
        self.editor.textChanged.connect(self.mark_modified)
        right_layout.addWidget(self.editor)
        
        # Status
        self.status = QLabel("Ready")
        self.status.setStyleSheet("color: #27ae60;")
        right_layout.addWidget(self.status)
        
        right_panel.setLayout(right_layout)
        splitter.addWidget(right_panel)
        
        # Set splitter sizes
        splitter.setSizes([200, 600])
        
        main_layout.addWidget(splitter)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
    
    def new_note(self):
        # Save current note first
        if self.current_note is not None:
            self.save_current_note()
        
        # Create new note
        note = Note(title="Untitled", content="")
        self.notes.insert(0, note)
        self.refresh_list()
        
        # Select new note
        self.notes_list.setCurrentRow(0)
        self.title.setFocus()
        self.title.selectAll()
    
    def delete_note(self):
        if self.current_note is None:
            return
        
        reply = QMessageBox.question(
            self, "Delete Note",
            f"Delete '{self.notes[self.current_note].title}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            del self.notes[self.current_note]
            self.current_note = None
            self.refresh_list()
            self.clear_editor()
            self.save_notes_to_file()
    
    def save_current_note(self):
        if self.current_note is None:
            return
        
        note = self.notes[self.current_note]
        note.title = self.title.text() or "Untitled"
        note.content = self.editor.toPlainText()
        note.modified = datetime.now().isoformat()
        
        self.refresh_list()
        self.update_meta()
        self.save_notes_to_file()
        
        self.status.setText(f"✅ Saved at {datetime.now().strftime('%H:%M:%S')}")
    
    def save_notes_to_file(self):
        try:
            data = [note.to_dict() for note in self.notes]
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Could not save: {e}")
    
    def load_notes(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                self.notes = [Note.from_dict(d) for d in data]
        except:
            self.notes = []
        
        self.refresh_list()
    
    def refresh_list(self):
        self.notes_list.clear()
        
        for note in self.notes:
            item = QListWidgetItem(note.title)
            item.setData(Qt.UserRole, note.created)
            
            # Preview
            preview = note.content[:50] + "..." if len(note.content) > 50 else note.content
            item.setToolTip(preview)
            
            self.notes_list.addItem(item)
        
        self.stats.setText(f"{len(self.notes)} notes")
    
    def on_note_selected(self, current, previous):
        if current is None:
            self.current_note = None
            self.clear_editor()
            return
        
        row = self.notes_list.row(current)
        self.current_note = row
        
        note = self.notes[row]
        self.title.blockSignals(True)
        self.title.setText(note.title)
        self.title.blockSignals(False)
        
        self.editor.blockSignals(True)
        self.editor.setPlainText(note.content)
        self.editor.blockSignals(False)
        
        self.update_meta()
    
    def clear_editor(self):
        self.title.clear()
        self.editor.clear()
        self.meta.setText("Created: - | Modified: -")
    
    def update_meta(self):
        if self.current_note is None:
            return
        
        note = self.notes[self.current_note]
        
        created = datetime.fromisoformat(note.created).strftime("%d/%m/%Y %H:%M")
        modified = datetime.fromisoformat(note.modified).strftime("%d/%m/%Y %H:%M")
        
        self.meta.setText(f"Created: {created} | Modified: {modified}")
    
    def mark_modified(self):
        if self.current_note is not None:
            self.status.setText("⚠️ Unsaved changes")
    
    def filter_notes(self, text):
        text = text.lower()
        
        for i in range(self.notes_list.count()):
            item = self.notes_list.item(i)
            note = self.notes[i]
            
            if text in note.title.lower() or text in note.content.lower():
                item.setHidden(False)
            else:
                item.setHidden(True)
    
    def export_note(self):
        if self.current_note is None:
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Note",
            f"{self.notes[self.current_note].title}.txt",
            "Text Files (*.txt)"
        )
        
        if file_path:
            note = self.notes[self.current_note]
            with open(file_path, 'w') as f:
                f.write(f"Title: {note.title}\n")
                f.write(f"Created: {note.created}\n")
                f.write(f"Modified: {note.modified}\n")
                f.write("-" * 40 + "\n\n")
                f.write(note.content)
            
            self.status.setText(f"✅ Exported to {file_path}")
    
    def import_notes(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Import Notes",
            "",
            "JSON Files (*.json);;Text Files (*.txt)"
        )
        
        if file_path:
            if file_path.endswith('.json'):
                with open(file_path, 'r') as f:
                    data = json.load(f)
                imported = [Note.from_dict(d) for d in data]
                self.notes = imported + self.notes
            else:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                note = Note(
                    title=os.path.basename(file_path),
                    content=content
                )
                self.notes.insert(0, note)
            
            self.refresh_list()
            self.save_notes_to_file()
            self.status.setText(f"✅ Imported {file_path}")
    
    def closeEvent(self, event):
        # Auto-save on close
        self.save_current_note()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec_())
