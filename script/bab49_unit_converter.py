# BAB 49: Proyek Akhir - Unit Converter
# ======================================
# Aplikasi konversi satuan lengkap

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
                              QLineEdit, QLabel, QComboBox,
                              QPushButton, QVBoxLayout, QHBoxLayout,
                              QWidget, QTabWidget, QFormLayout,
                              QGroupBox)
from PyQt5.QtCore import Qt

class UnitConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔄 Unit Converter - © Politeknik Negeri Bandung - M Rizqi S.")
        self.setGeometry(100, 100, 500, 450)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLineEdit {
                padding: 10px;
                font-size: 16px;
                border: 2px solid #ddd;
                border-radius: 8px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
            QComboBox {
                padding: 10px;
                font-size: 14px;
                border: 2px solid #ddd;
                border-radius: 8px;
            }
            QPushButton {
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
            }
            QLabel#result {
                font-size: 24px;
                font-weight: bold;
                color: #27ae60;
            }
        """)
        
        self.setup_ui()
    
    def setup_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🔄 UNIT CONVERTER")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Tabs for different categories
        tabs = QTabWidget()
        
        # Length tab
        tabs.addTab(self.create_converter_tab(
            "Length",
            ["m", "km", "cm", "mm", "mile", "yard", "foot", "inch"],
            {
                "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001,
                "mile": 1609.344, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254
            }
        ), "📏 Length")
        
        # Weight tab
        tabs.addTab(self.create_converter_tab(
            "Weight",
            ["kg", "g", "mg", "lb", "oz", "ton"],
            {
                "kg": 1, "g": 0.001, "mg": 0.000001,
                "lb": 0.453592, "oz": 0.0283495, "ton": 1000
            }
        ), "⚖️ Weight")
        
        # Temperature tab
        tabs.addTab(self.create_temperature_tab(), "🌡️ Temperature")
        
        # Volume tab
        tabs.addTab(self.create_converter_tab(
            "Volume",
            ["L", "mL", "gal", "qt", "pt", "cup", "fl oz"],
            {
                "L": 1, "mL": 0.001, "gal": 3.78541,
                "qt": 0.946353, "pt": 0.473176, "cup": 0.236588, "fl oz": 0.0295735
            }
        ), "🧪 Volume")
        
        # Area tab
        tabs.addTab(self.create_converter_tab(
            "Area",
            ["m²", "km²", "ha", "acre", "ft²", "yd²"],
            {
                "m²": 1, "km²": 1000000, "ha": 10000,
                "acre": 4046.86, "ft²": 0.092903, "yd²": 0.836127
            }
        ), "📐 Area")
        
        # Speed tab
        tabs.addTab(self.create_converter_tab(
            "Speed",
            ["m/s", "km/h", "mph", "knot", "ft/s"],
            {
                "m/s": 1, "km/h": 0.277778, "mph": 0.44704,
                "knot": 0.514444, "ft/s": 0.3048
            }
        ), "🚀 Speed")
        
        # Time tab
        tabs.addTab(self.create_converter_tab(
            "Time",
            ["s", "ms", "min", "h", "day", "week", "year"],
            {
                "s": 1, "ms": 0.001, "min": 60,
                "h": 3600, "day": 86400, "week": 604800, "year": 31536000
            }
        ), "⏱️ Time")
        
        # Data tab
        tabs.addTab(self.create_converter_tab(
            "Data",
            ["B", "KB", "MB", "GB", "TB", "bit"],
            {
                "B": 1, "KB": 1024, "MB": 1048576,
                "GB": 1073741824, "TB": 1099511627776, "bit": 0.125
            }
        ), "💾 Data")
        
        layout.addWidget(tabs)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def create_converter_tab(self, category, units, conversions):
        """Create a standard converter tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Input section
        input_group = QGroupBox("Input")
        input_layout = QFormLayout()
        
        # Value input
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("Enter value")
        self.value_input.textChanged.connect(lambda: self.convert(category))
        input_layout.addRow("Value:", self.value_input)
        
        # From unit
        self.from_unit = QComboBox()
        self.from_unit.addItems(units)
        self.from_unit.currentIndexChanged.connect(lambda: self.convert(category))
        input_layout.addRow("From:", self.from_unit)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Swap button
        btn_swap = QPushButton("🔄 Swap Units")
        btn_swap.setStyleSheet("background-color: #3498db; color: white;")
        btn_swap.clicked.connect(self.swap_units)
        layout.addWidget(btn_swap)
        
        # Output section
        output_group = QGroupBox("Output")
        output_layout = QFormLayout()
        
        # To unit
        self.to_unit = QComboBox()
        self.to_unit.addItems(units)
        self.to_unit.setCurrentIndex(1)  # Default to second unit
        self.to_unit.currentIndexChanged.connect(lambda: self.convert(category))
        output_layout.addRow("To:", self.to_unit)
        
        # Result
        self.result = QLabel("0")
        self.result.setObjectName("result")
        output_layout.addRow("Result:", self.result)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Formula
        self.formula = QLabel("Formula: -")
        self.formula.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self.formula)
        
        layout.addStretch()
        
        # Store conversions
        self.conversions = conversions
        
        widget.setLayout(layout)
        return widget
    
    def create_temperature_tab(self):
        """Special tab for temperature (different formula)"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Input section
        input_group = QGroupBox("Input")
        input_layout = QFormLayout()
        
        self.temp_value = QLineEdit()
        self.temp_value.setPlaceholderText("Enter temperature")
        self.temp_value.textChanged.connect(self.convert_temperature)
        input_layout.addRow("Value:", self.temp_value)
        
        self.temp_from = QComboBox()
        self.temp_from.addItems(["Celsius", "Fahrenheit", "Kelvin"])
        self.temp_from.currentIndexChanged.connect(self.convert_temperature)
        input_layout.addRow("From:", self.temp_from)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Swap button
        btn_swap = QPushButton("🔄 Swap Units")
        btn_swap.setStyleSheet("background-color: #3498db; color: white;")
        btn_swap.clicked.connect(self.swap_temperature)
        layout.addWidget(btn_swap)
        
        # Output section
        output_group = QGroupBox("Output")
        output_layout = QFormLayout()
        
        self.temp_to = QComboBox()
        self.temp_to.addItems(["Celsius", "Fahrenheit", "Kelvin"])
        self.temp_to.setCurrentIndex(1)
        self.temp_to.currentIndexChanged.connect(self.convert_temperature)
        output_layout.addRow("To:", self.temp_to)
        
        self.temp_result = QLabel("0")
        self.temp_result.setObjectName("result")
        output_layout.addRow("Result:", self.temp_result)
        
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)
        
        # Formula
        self.temp_formula = QLabel("Formula: -")
        self.temp_formula.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(self.temp_formula)
        
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def convert(self, category):
        """Convert units"""
        try:
            value = float(self.value_input.text())
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()
            
            # Convert to base unit, then to target
            base_value = value * self.conversions[from_unit]
            result = base_value / self.conversions[to_unit]
            
            # Format result
            if abs(result) >= 1000 or (abs(result) < 0.01 and result != 0):
                self.result.setText(f"{result:.6e}")
            else:
                self.result.setText(f"{result:.6f}".rstrip('0').rstrip('.'))
            
            # Show formula
            if from_unit == to_unit:
                self.formula.setText("Formula: Same unit")
            else:
                ratio = self.conversions[from_unit] / self.conversions[to_unit]
                self.formula.setText(f"Formula: {value} {from_unit} × {ratio:.6f} = {result:.6f} {to_unit}")
                
        except ValueError:
            self.result.setText("0")
            self.formula.setText("Formula: -")
    
    def convert_temperature(self):
        """Convert temperature with special formulas"""
        try:
            value = float(self.temp_value.text())
            from_unit = self.temp_from.currentText()
            to_unit = self.temp_to.currentText()
            
            # Convert to Celsius first
            if from_unit == "Celsius":
                celsius = value
            elif from_unit == "Fahrenheit":
                celsius = (value - 32) * 5/9
            else:  # Kelvin
                celsius = value - 273.15
            
            # Convert from Celsius to target
            if to_unit == "Celsius":
                result = celsius
            elif to_unit == "Fahrenheit":
                result = celsius * 9/5 + 32
            else:  # Kelvin
                result = celsius + 273.15
            
            # Format result
            self.temp_result.setText(f"{result:.2f}".rstrip('0').rstrip('.'))
            
            # Formula
            self.temp_formula.setText(f"Formula: {value} {from_unit} → {result:.2f} {to_unit}")
            
        except ValueError:
            self.temp_result.setText("0")
            self.temp_formula.setText("Formula: -")
    
    def swap_units(self):
        """Swap from and to units"""
        from_idx = self.from_unit.currentIndex()
        to_idx = self.to_unit.currentIndex()
        
        self.from_unit.setCurrentIndex(to_idx)
        self.to_unit.setCurrentIndex(from_idx)
    
    def swap_temperature(self):
        """Swap temperature units"""
        from_idx = self.temp_from.currentIndex()
        to_idx = self.temp_to.currentIndex()
        
        self.temp_from.setCurrentIndex(to_idx)
        self.temp_to.setCurrentIndex(from_idx)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UnitConverter()
    window.show()
    sys.exit(app.exec_())
