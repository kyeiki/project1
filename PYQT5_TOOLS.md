# Panduan pyqt5-tools & Qt Designer

## Apa itu pyqt5-tools?

`pyqt5-tools` adalah paket tambahan untuk PyQt5 yang menyediakan beberapa tools berguna, terutama **Qt Designer** — aplikasi visual untuk mendesain GUI dengan drag & drop tanpa coding!

## Instalasi

Sudah termasuk di `requirements.txt`:

```bash
pip install -r requirements.txt
```

Atau install manual:

```bash
pip install pyqt5-tools
```

## Mengakses Qt Designer

### Windows

Setelah install, Qt Designer bisa diakses dengan beberapa cara:

#### Cara 1: Via Command Line (Recommended)

```powershell
# Aktifkan virtual environment terlebih dahulu
venv\Scripts\Activate.ps1

# Jalankan Qt Designer
pyqt5-tools designer
```

Atau langsung akses executable:

```powershell
# Lokasi executable (jika via pip install)
venv\Lib\site-packages\pyqt5_tools\Qt\bin\designer.exe
```

#### Cara 2: Via Python Script

Buat file `run_designer.py`:

```python
import sys
import subprocess
from pathlib import Path

# Path ke designer.exe
venv_path = Path(sys.prefix)
designer_path = venv_path / "Lib" / "site-packages" / "pyqt5_tools" / "Qt" / "bin" / "designer.exe"

if designer_path.exists():
    subprocess.run([str(designer_path)])
else:
    print(f"Qt Designer tidak ditemukan di: {designer_path}")
```

Jalankan dengan:
```powershell
python run_designer.py
```

### Linux / macOS

```bash
# Aktifkan virtual environment
source venv/bin/activate

# Jalankan Qt Designer
pyqt5-tools designer
```

## Fitur Qt Designer

| Fitur | Deskripsi |
|-------|-----------|
| 🎨 **Drag & Drop** | Susun widget dengan mudah tanpa coding |
| 📐 **Layout Management** | Atur layout secara visual |
| 🔗 **Signal-Slot Editor** | Hubungkan signal dan slot tanpa kode |
| 📋 **Resource Editor** | Kelola gambar, icon, dan resource |
| 💾 **Save as .ui** | Simpan desain dalam format XML (.ui) |

## Mengkonversi .ui ke Python

File `.ui` yang dibuat Qt Designer perlu dikonversi ke Python:

### Cara 1: Via Command Line

```powershell
pyuic5 -o output.py input.ui
```

Contoh:
```powershell
pyuic5 -o my_window.py my_design.ui
```

### Cara 2: Load Langsung di Python

```python
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load file .ui langsung
        loadUi('my_design.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
```

## Workflow Recommended

1. **Desain** di Qt Designer → save sebagai `.ui`
2. **Konversi** ke `.py` dengan `pyuic5` (atau load langsung)
3. **Extend** dengan menambahkan logic di file Python terpisah
4. **Run** dan test aplikasi

## Tips & Tricks

### Tip 1: Jangan Edit File Hasil Konversi
File hasil `pyuic5` akan di-overwrite setiap kali konversi. Buat file terpisah untuk logic:

```python
# main.py
from PyQt5.QtWidgets import QApplication
from ui_my_window import Ui_MainWindow  # import dari file konversi
import sys

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Tambahkan logic di sini
        self.pushButton.clicked.connect(self.on_click)
    
    def on_click(self):
        print("Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
```

### Tip 2: Preview di Qt Designer
Tekan `Ctrl+R` di Qt Designer untuk preview desain tanpa perlu compile.

### Tip 3: Gunakan Layout
Selalu gunakan layout (VBoxLayout, QHBoxLayout, dll) agar UI responsive saat resize.

## Troubleshooting

### "designer.exe not found"
Pastikan `pyqt5-tools` sudah terinstall:
```powershell
pip show pyqt5-tools
```

### "ModuleNotFoundError: No module named 'PyQt5'"
Aktifkan virtual environment terlebih dahulu:
```powershell
venv\Scripts\Activate.ps1
```

### UI tidak responsive
Pastikan menggunakan layout, bukan posisi absolut. Di Qt Designer, pilih widget dan klik kanan → Layout.

---

## Resources

- [Dokumentasi Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Repo Ini](https://github.com/kyeiki/project1)
