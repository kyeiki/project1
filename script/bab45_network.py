# BAB 45: Network Request
# ========================
# HTTP requests dengan QNetworkAccessManager

import sys
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QTextEdit, QLineEdit, QPushButton,
                              QLabel, QVBoxLayout, QHBoxLayout,
                              QWidget, QComboBox, QProgressBar)
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtCore import QUrl, Qt

class NetworkDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Request Demo - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 600, 500)
        
        # Network manager
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.on_response)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🌐 NETWORK REQUEST")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Method selector
        method_layout = QHBoxLayout()
        
        method_layout.addWidget(QLabel("Method:"))
        self.method = QComboBox()
        self.method.addItems(["GET", "POST", "PUT", "DELETE"])
        method_layout.addWidget(self.method)
        
        layout.addLayout(method_layout)
        
        # URL input
        url_layout = QHBoxLayout()
        
        url_layout.addWidget(QLabel("URL:"))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://jsonplaceholder.typicode.com/posts/1")
        self.url_input.setText("https://jsonplaceholder.typicode.com/posts/1")
        url_layout.addWidget(self.url_input)
        
        btn_send = QPushButton("Send")
        btn_send.setStyleSheet("background-color: #27ae60; color: white;")
        btn_send.clicked.connect(self.send_request)
        url_layout.addWidget(btn_send)
        
        layout.addLayout(url_layout)
        
        # Request body (for POST/PUT)
        layout.addWidget(QLabel("Request Body (JSON):"))
        self.body_input = QTextEdit()
        self.body_input.setPlaceholderText('{"title": "Test", "body": "Content", "userId": 1}')
        self.body_input.setMaximumHeight(100)
        self.body_input.setText('{\n  "title": "Test Post",\n  "body": "This is a test",\n  "userId": 1\n}')
        layout.addWidget(self.body_input)
        
        # Progress
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        layout.addWidget(self.progress)
        
        # Status
        self.status = QLabel("Ready")
        self.status.setStyleSheet("color: gray;")
        layout.addWidget(self.status)
        
        # Response
        layout.addWidget(QLabel("Response:"))
        self.response = QTextEdit()
        self.response.setReadOnly(True)
        layout.addWidget(self.response)
        
        # Quick API buttons
        quick_layout = QHBoxLayout()
        
        btn_posts = QPushButton("Get Posts")
        btn_posts.clicked.connect(lambda: self.quick_request("https://jsonplaceholder.typicode.com/posts"))
        quick_layout.addWidget(btn_posts)
        
        btn_users = QPushButton("Get Users")
        btn_users.clicked.connect(lambda: self.quick_request("https://jsonplaceholder.typicode.com/users"))
        quick_layout.addWidget(btn_users)
        
        btn_comments = QPushButton("Get Comments")
        btn_comments.clicked.connect(lambda: self.quick_request("https://jsonplaceholder.typicode.com/comments"))
        quick_layout.addWidget(btn_comments)
        
        layout.addLayout(quick_layout)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def send_request(self):
        url = self.url_input.text().strip()
        
        if not url:
            self.status.setText("Error: URL is required")
            self.status.setStyleSheet("color: red;")
            return
        
        method = self.method.currentText()
        
        self.status.setText(f"Sending {method} request...")
        self.status.setStyleSheet("color: blue;")
        self.progress.setVisible(True)
        self.progress.setRange(0, 0)  # Indeterminate
        
        request = QNetworkRequest(QUrl(url))
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        if method == "GET":
            self.network_manager.get(request)
        elif method == "POST":
            body = self.body_input.toPlainText().encode()
            self.network_manager.post(request, body)
        elif method == "PUT":
            body = self.body_input.toPlainText().encode()
            self.network_manager.put(request, body)
        elif method == "DELETE":
            self.network_manager.deleteResource(request)
    
    def quick_request(self, url):
        self.url_input.setText(url)
        self.method.setCurrentText("GET")
        self.send_request()
    
    def on_response(self, reply):
        self.progress.setVisible(False)
        
        # Get status code
        status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
        
        # Get response body
        data = reply.readAll().data().decode()
        
        # Try to format JSON
        try:
            parsed = json.loads(data)
            formatted = json.dumps(parsed, indent=2)
        except:
            formatted = data
        
        # Display
        self.response.setPlainText(formatted)
        
        if reply.error():
            self.status.setText(f"Error: {reply.errorString()}")
            self.status.setStyleSheet("color: red;")
        else:
            self.status.setText(f"Success! Status: {status_code}")
            self.status.setStyleSheet("color: green;")
        
        reply.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetworkDemo()
    window.show()
    sys.exit(app.exec_())
