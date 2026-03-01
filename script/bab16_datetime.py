# BAB 16: Tanggal dan Waktu
# ==========================

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QDateEdit, QTimeEdit, QDateTimeEdit,
                              QCalendarWidget, QLabel, QPushButton,
                              QVBoxLayout, QHBoxLayout, QWidget, QGroupBox)
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

class JendelaKu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Date & Time Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 500)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Date Edit
        grup_date = QGroupBox("Pilih Tanggal:")
        layout_date = QVBoxLayout()
        
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setDisplayFormat("dddd, dd MMMM yyyy")
        self.date_edit.dateChanged.connect(self.tanggal_berubah)
        layout_date.addWidget(self.date_edit)
        
        self.label_date = QLabel(f"Tanggal: {QDate.currentDate().toString('dddd, dd MMMM yyyy')}")
        layout_date.addWidget(self.label_date)
        
        grup_date.setLayout(layout_date)
        layout.addWidget(grup_date)
        
        # Time Edit
        grup_time = QGroupBox("Pilih Waktu:")
        layout_time = QVBoxLayout()
        
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())
        self.time_edit.setDisplayFormat("HH:mm:ss")
        self.time_edit.timeChanged.connect(self.waktu_berubah)
        layout_time.addWidget(self.time_edit)
        
        self.label_time = QLabel(f"Waktu: {QTime.currentTime().toString('HH:mm:ss')}")
        layout_time.addWidget(self.label_time)
        
        grup_time.setLayout(layout_time)
        layout.addWidget(grup_time)
        
        # DateTime Edit
        grup_datetime = QGroupBox("Tanggal & Waktu:")
        layout_datetime = QVBoxLayout()
        
        self.datetime_edit = QDateTimeEdit()
        self.datetime_edit.setCalendarPopup(True)
        self.datetime_edit.setDateTime(QDateTime.currentDateTime())
        self.datetime_edit.setDisplayFormat("dd/MM/yyyy HH:mm")
        layout_datetime.addWidget(self.datetime_edit)
        
        grup_datetime.setLayout(layout_datetime)
        layout.addWidget(grup_datetime)
        
        # Calendar Widget
        layout.addWidget(QLabel("\nKalender:"))
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.tanggal_kalender_dipilih)
        layout.addWidget(self.calendar)
        
        self.label_calendar = QLabel("Klik tanggal di kalender...")
        self.label_calendar.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.label_calendar)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def tanggal_berubah(self, date):
        self.label_date.setText(f"Tanggal: {date.toString('dddd, dd MMMM yyyy')}")
    
    def waktu_berubah(self, time):
        self.label_time.setText(f"Waktu: {time.toString('HH:mm:ss')}")
    
    def tanggal_kalender_dipilih(self, date):
        self.label_calendar.setText(f"Dipilih: {date.toString('dddd, dd MMMM yyyy')}")

app = QApplication(sys.argv)
jendela = JendelaKu()
jendela.show()
sys.exit(app.exec_())
