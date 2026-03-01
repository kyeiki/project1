# BAB 26: Calculator App
# =======================
# Aplikasi kalkulator lengkap dengan CSS styling

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLineEdit, QPushButton, QGridLayout, 
                              QWidget, QVBoxLayout)
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 320, 450)
        
        self.expression = ""
        
        # CSS Styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a2e;
            }
            QLineEdit {
                background-color: #16213e;
                color: #eee;
                font-size: 32px;
                padding: 15px;
                border: none;
                border-radius: 10px;
            }
            QPushButton {
                font-size: 22px;
                border-radius: 35px;
                min-height: 70px;
                min-width: 70px;
            }
            QPushButton#number {
                background-color: #0f3460;
                color: white;
            }
            QPushButton#number:hover {
                background-color: #1a4a7a;
            }
            QPushButton#op {
                background-color: #e94560;
                color: white;
            }
            QPushButton#op:hover {
                background-color: #ff6b6b;
            }
            QPushButton#func {
                background-color: #34836F;
                color: white;
            }
            QPushButton#func:hover {
                background-color: #4A91A8;
            }
            QPushButton#eq {
                background-color: #00b894;
                color: white;
            }
            QPushButton#eq:hover {
                background-color: #00d9a5;
            }
            QPushButton#clear {
                background-color: #d63031;
                color: white;
            }
            QPushButton#clear:hover {
                background-color: #ff4757;
            }
        """)
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setText("0")
        layout.addWidget(self.display)
        
        # Buttons grid
        grid = QGridLayout()
        grid.setSpacing(10)
        
        # Row 0: Clear and operations
        buttons = [
            # (text, row, col, id)
            ("C", 0, 0, "clear"),
            ("±", 0, 1, "func"),
            ("%", 0, 2, "func"),
            ("÷", 0, 3, "op"),
            
            # Row 1
            ("7", 1, 0, "number"),
            ("8", 1, 1, "number"),
            ("9", 1, 2, "number"),
            ("×", 1, 3, "op"),
            
            # Row 2
            ("4", 2, 0, "number"),
            ("5", 2, 1, "number"),
            ("6", 2, 2, "number"),
            ("-", 2, 3, "op"),
            
            # Row 3
            ("1", 3, 0, "number"),
            ("2", 3, 1, "number"),
            ("3", 3, 2, "number"),
            ("+", 3, 3, "op"),
            
            # Row 4
            ("0", 4, 0, "number"),
            (".", 4, 1, "number"),
            ("⌫", 4, 2, "func"),
            ("=", 4, 3, "eq"),
        ]
        
        for text, row, col, btn_id in buttons:
            btn = QPushButton(text)
            btn.setObjectName(btn_id)
            btn.clicked.connect(lambda checked, t=text: self.on_click(t))
            grid.addWidget(btn, row, col)
        
        layout.addLayout(grid)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def on_click(self, text):
        if text == "C":
            self.expression = ""
            self.display.setText("0")
        
        elif text == "⌫":  # Backspace
            self.expression = self.expression[:-1]
            self.display.setText(self.expression if self.expression else "0")
        
        elif text == "=":
            try:
                # Replace symbols untuk eval
                expr = self.expression.replace("×", "*").replace("÷", "/")
                result = eval(expr)
                
                # Format result
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 8)
                
                self.display.setText(str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                self.display.setText("Error: Div by 0")
                self.expression = ""
            except Exception as e:
                self.display.setText("Error")
                self.expression = ""
        
        elif text == "±":  # Plus/minus
            if self.expression:
                if self.expression[0] == "-":
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display.setText(self.expression)
        
        elif text == "%":  # Percent
            try:
                result = float(self.expression) / 100
                self.display.setText(str(result))
                self.expression = str(result)
            except:
                pass
        
        else:
            # Angka atau operator
            self.expression += text
            self.display.setText(self.expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
