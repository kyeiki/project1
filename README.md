# PyQt5: Dari Kepingan Menuju Karya

> **Belajar Membangun Aplikasi GUI Seperti Main Lego**
>
> *Penulis: Muhammad Rizqi Sholahuddin*

Modul ini berisi **50 bab** yang memandu Anda membangun aplikasi GUI menggunakan PyQt5 secara bertahap---dari jendela kosong hingga aplikasi lengkap.

## 🔗 Akses Repositori

Scan QR code berikut untuk mengakses repositori GitHub:

![QR Code ke GitHub](qr-lYo4g.png)

Atau kunjungi langsung: [https://github.com/kyeiki/project1](https://github.com/kyeiki/project1)

---

## Daftar Isi

- [Peta Perjalanan](#peta-perjalanan)
- [Persiapan](#persiapan)
- [Bagian 1: Fondasi (Bab 1--12)](#bagian-1-fondasi-bab-112)
- [Bagian 2: Widget Lanjutan (Bab 13--20)](#bagian-2-widget-lanjutan-bab-1320)
- [Bagian 3: Fitur Menengah (Bab 21--40)](#bagian-3-fitur-menengah-bab-2140)
- [Bagian 4: Proyek Akhir (Bab 41--50)](#bagian-4-proyek-akhir-bab-4150)
- [Struktur Folder](#struktur-folder)
- [Cara Compile](#cara-compile)

---

## Peta Perjalanan

| Fase | Bab | Fokus |
|------|-----|-------|
| Fondasi | 2--10 | Widget dasar, layout, styling |
| Mini Proyek | 11--12 | To-Do App, input angka |
| Widget Lanjutan | 13--20 | Radio, checkbox, combo, tabel, tab, scroll |
| Fitur Menengah | 21--40 | Dialog, timer, threading, drag-drop, custom widget, dll. |
| Proyek Akhir | 41--50 | Aplikasi lengkap berskala kecil hingga menengah |

---

## Persiapan

> **Opsional tapi Direkomendasikan:** gunakan virtual environment (venv) agar dependensi proyek ini terisolasi dari sistem utama.

1. Pastikan Python 3 sudah ter-install.
2. Dari folder proyek ini, buat virtual environment bernama `venv`:

```bash
python -m venv venv
```

3. Aktifkan virtual environment:

- **Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

- **Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

- **Linux/macOS (bash/zsh):**

```bash
source venv/bin/activate
```

4. Install dependensi dari `requirements.txt`:

```bash
pip install -r requirements.txt
```

Kalau Anda tidak ingin memakai venv, Anda bisa langsung menjalankan:

```bash
pip install -r requirements.txt
```

> **Kenapa venv penting (walau opsional)?**
>
> - Paket untuk proyek ini terpisah dari paket Python lain di sistem (tidak bentrok versi).
> - Memudahkan kolaborasi: semua orang cukup install dari `requirements.txt` di venv masing-masing.
> - Aman untuk eksperimen: kalau rusak, cukup hapus folder `venv` dan buat ulang.

---

## Bagian 1: Fondasi (Bab 1--12)

### Bab 1 -- Pendahuluan

Pengantar modul. Setiap bab terdiri dari: **Kode Program**, **Penjelasan Kode**, dan **Hasil Tampilan**.

---

### Bab 2 -- Kepingan Pertama: Jendela Kosong
> **Script:** [`bab02_jendela_kosong.py`](script/bab02_jendela_kosong.py)

Skrip 19 baris yang memuat seluruh kerangka dasar PyQt5: `QApplication` (mesin penggerak), `QMainWindow` (jendela utama), `setGeometry()` (posisi dan ukuran), dan `app.exec_()` (event loop).

**Pelajaran:** Pola empat langkah -- buat `QApplication` -> buat jendela -> `show()` -> `exec_()` -- muncul di *setiap* program PyQt5. Event loop adalah jantung aplikasi GUI.

---

### Bab 3 -- Menambah Label: Jendela yang Bicara
> **Script:** [`bab03_label.py`](script/bab03_label.py)

Widget pertama: `QLabel` untuk menampilkan teks statis. Menggunakan `setAlignment()` untuk perataan, `QFont` untuk tipografi, `setStyleSheet()` untuk CSS, dan `setCentralWidget()` untuk menjadikan label sebagai konten utama.

**Pelajaran:** `setStyleSheet()` membawa kekuatan CSS ke desktop. `setCentralWidget()` memastikan widget mengisi area utama secara otomatis.

---

### Bab 4 -- Tombol Interaktif
> **Script:** [`bab04_tombol.py`](script/bab04_tombol.py)

Memperkenalkan `QPushButton` dan **signal & slot** -- "kabel tak terlihat" yang menghubungkan aksi pengguna ke respons aplikasi. Tiga tombol dengan tiga aksi: informasi, about, dan keluar. `QMessageBox` untuk dialog bawaan.

**Pelajaran:** Signal & slot menggantikan polling manual. `QMessageBox` adalah cara tercepat berkomunikasi dengan pengguna.

---

### Bab 5 -- Layout Manager: Menyusun Kepingan
> **Script:** [`bab05_layout.py`](script/bab05_layout.py)

Tiga jenis layout: `QVBoxLayout` (vertikal), `QHBoxLayout` (horizontal), `QGridLayout` (grid). Nesting layout via `addLayout()` untuk tata letak kompleks. Pola `QWidget` + layout + `setCentralWidget`.

**Pelajaran:** Selalu gunakan layout manager agar UI responsif saat di-resize. Jangan posisi manual.

---

### Bab 6 -- Input Pengguna: Formulir Sederhana
> **Script:** [`bab06_form.py`](script/bab06_form.py)

Form registrasi dengan `QLineEdit` (input teks + placeholder), validasi sederhana (cek kosong), dan styling tombol dengan pseudo-state `:hover`.

**Pelajaran:** Pola "baca input -> validasi -> proses" adalah fondasi semua form.

---

### Bab 7 -- Signal & Slot: Menghubungkan Kepingan
> **Script:** [`bab07_signal_slot.py`](script/bab07_signal_slot.py)

Demonstrasi mendalam: `textChanged` (real-time), `returnPressed` (Enter), `clicked` (tombol). Satu slot bisa melayani banyak signal. Signal membawa data secara otomatis ke slot.

**Pelajaran:** Signal & slot memisahkan pengirim dan penerima. Fondasi arsitektur event-driven Qt.

---

### Bab 8 -- Widget Keren
> **Script:** [`bab08_widget_keren.py`](script/bab08_widget_keren.py)

Koleksi widget: `QComboBox` (dropdown), `QSlider` + `QProgressBar` (pasangan serasi), `QCheckBox` (pilihan ganda), `QRadioButton` (pilihan tunggal), dan `QGroupBox` (pengelompokan visual).

**Pelajaran:** Qt menyediakan widget untuk hampir semua kebutuhan input. `QGroupBox` mengelompokkan widget secara visual dan semantik.

---

### Bab 9 -- Menu & Toolbar
> **Script:** [`bab09_menu_toolbar.py`](script/bab09_menu_toolbar.py)

"Tiga serangkai" aplikasi profesional: menu bar, toolbar, status bar. `QAction` sebagai abstraksi aksi yang bisa muncul di menu *dan* toolbar sekaligus. Shortcut keyboard via `setShortcut()`.

**Pelajaran:** `QAction` memisahkan logika aksi dari tampilan -- satu definisi, banyak penempatan.

---

### Bab 10 -- Styling: Mewarnai Karya
> **Script:** [`bab10_styling.py`](script/bab10_styling.py)

Form "Create Account" dengan styling CSS lengkap: gradasi latar (`qlineargradient`), border-radius, pseudo-state (`:hover`, `:pressed`, `:focus`), selector tipe dan ID (`QLabel#title`), password field.

**Pelajaran:** `setStyleSheet()` mendukung hampir semua properti CSS. Styling terpusat lebih mudah dipelihara.

---

### Bab 11 -- Proyek Mini: Todo App
> **Script:** [`bab11_todo_app.py`](script/bab11_todo_app.py)

Proyek pertama! Menyatukan semua konsep: persistensi JSON, UI tiga bagian (input, daftar, aksi), styling modern, alur data konsisten (modifikasi -> simpan -> refresh), dan statistik real-time.

**Pelajaran:** Pola "modifikasi data -> simpan -> refresh UI" adalah arsitektur standar CRUD. ~250 baris, sudah layak digunakan sehari-hari.

---

### Bab 12 -- Input Angka: Spin dan Dial
> **Script:** [`bab12_spin_dial.py`](script/bab12_spin_dial.py)

`QSpinBox` (angka bulat + prefix/suffix), `QDoubleSpinBox` (desimal), `QDial` (kenop putar). Validasi input "gratis" -- pengguna tidak bisa memasukkan nilai di luar rentang.

**Pelajaran:** Signal `valueChanged` membuat pembaruan UI reaktif tanpa loop polling.

---

## Bagian 2: Widget Lanjutan (Bab 13--20)

### Bab 13 -- Pilihan Tunggal: Radio Button
> **Script:** [`bab13_radiobutton.py`](script/bab13_radiobutton.py)

`QRadioButton` dengan `QButtonGroup` untuk grup independen. Mapping ID ke teks via dictionary. Reaksi real-time lewat signal `buttonClicked`.

**Pelajaran:** `QRadioButton` untuk pilihan *mutually exclusive*. Dictionary lebih bersih dari `if-elif`.

---

### Bab 14 -- Pilihan Ganda: Checkbox
> **Script:** [`bab14_checkbox.py`](script/bab14_checkbox.py)

`QCheckBox` untuk pilihan ganda (topping pizza). Mode tristate untuk "Pilih Semua". Kalkulasi harga dinamis via `isChecked()`.

**Pelajaran:** Gunakan `QCheckBox` ketika pengguna boleh memilih nol, satu, atau banyak opsi.

---

### Bab 15 -- Dropdown: ComboBox
> **Script:** [`bab15_combobox.py`](script/bab15_combobox.py)

Tiga varian: sederhana (kota), data tersembunyi (`addItem(text, data)` untuk harga), dan editable (`setEditable(True)`).

**Pelajaran:** Simpan data tersembunyi via `addItem(text, userData)` untuk memisahkan tampilan dan logika.

---

### Bab 16 -- Tanggal dan Waktu
> **Script:** [`bab16_datetime.py`](script/bab16_datetime.py)

`QDateEdit` (kalender pop-up), `QTimeEdit`, `QDateTimeEdit`, dan `QCalendarWidget`. Format kustom via `setDisplayFormat()`.

**Pelajaran:** Widget tanggal/waktu bawaan Qt memastikan validasi format otomatis.

---

### Bab 17 -- Daftar: ListWidget
> **Script:** [`bab17_listwidget.py`](script/bab17_listwidget.py)

`QListWidget` untuk daftar tugas mini: tambah, edit (`takeItem`), hapus, clear, pilih semua. Signal `currentItemChanged` dan `itemDoubleClicked`.

**Pelajaran:** Pisahkan logika CRUD ke metode tersendiri. Selalu perbarui statistik setelah mutasi data.

---

### Bab 18 -- Tabel: TableWidget
> **Script:** [`bab18_tablewidget.py`](script/bab18_tablewidget.py)

`QTableWidget` untuk data mahasiswa (NIM, Nama, Nilai, Grade). Warna kontekstual (`setBackground`) berdasarkan nilai. Statistik real-time (rata-rata). `QHeaderView` untuk resize kolom.

**Pelajaran:** Warna latar sel meningkatkan keterbacaan data secara signifikan.

---

### Bab 19 -- Tab Widget
> **Script:** [`bab19_tabwidget.py`](script/bab19_tabwidget.py)

`QTabWidget` dengan empat tab: Home, Calculator, Notes, Settings. Setiap tab dibuat metode terpisah.

**Pelajaran:** `QTabWidget` memecah UI kompleks menjadi halaman mudah dijelajahi. Setiap tab adalah `QWidget` biasa.

---

### Bab 20 -- Scroll Area
> **Script:** [`bab20_scrollarea.py`](script/bab20_scrollarea.py)

`QScrollArea` dengan 50 kartu item ber-styling. `setWidgetResizable(True)` agar konten beradaptasi. Qt hanya merender yang terlihat.

**Pelajaran:** Wajib dipakai ketika konten berpotensi melebihi ukuran jendela.

---

## Bagian 3: Fitur Menengah (Bab 21--40)

### Bab 21 -- Splitter
> **Script:** [`bab21_splitter.py`](script/bab21_splitter.py)

`QSplitter` membagi jendela: panel kiri `QTreeView` (file system), panel kanan preview + info. Nested splitter (horizontal dalam vertikal). `setSizes()` untuk proporsi awal.

**Pelajaran:** `QFileSystemModel` + `QTreeView` = cara tercepat menampilkan isi disk.

---

### Bab 22 -- Dialog Standar
> **Script:** [`bab22_dialog.py`](script/bab22_dialog.py)

Dialog bawaan: `QFileDialog` (open/save/folder), `QColorDialog`, `QFontDialog`, `QInputDialog` (text/int/item). Selalu periksa `ok` sebelum proses.

**Pelajaran:** Dialog bawaan Qt konsisten dengan tampilan OS -- pengguna langsung familiar.

---

### Bab 23 -- Timer
> **Script:** [`bab23_timer.py`](script/bab23_timer.py)

`QTimer` periodik (jam digital, 1000ms), stopwatch cepat (1ms), dan `singleShot` (countdown). Timer berjalan di event loop -- UI tetap responsif.

**Pelajaran:** Periodik untuk update terus-menerus; `singleShot` untuk delay satu kali.

---

### Bab 24 -- Settings: Menyimpan Preferensi
> **Script:** [`bab24_settings.py`](script/bab24_settings.py)

`QSettings` menyimpan preferensi persisten (registry Windows / config Linux). `setValue()`/`value()` dengan tipe data. Auto-load saat startup.

**Pelajaran:** `QSettings` abstrak penyimpanan lintas platform. Selalu sediakan nilai default.

---

### Bab 25 -- Clipboard
> **Script:** [`bab25_clipboard.py`](script/bab25_clipboard.py)

`QApplication.clipboard()` untuk copy, cut, paste, clear. Signal `dataChanged` memonitor clipboard dari aplikasi mana pun.

**Pelajaran:** Clipboard Qt bersifat lintas aplikasi. `dataChanged` untuk monitoring real-time.

---

### Bab 26 -- Proyek Mini: Kalkulator
> **Script:** [`bab26_calculator.py`](script/bab26_calculator.py)

Kalkulator modern: `QGridLayout` untuk keypad, `QLineEdit` read-only untuk display, lambda di `connect()` untuk 20+ tombol. Fitur: +, -, *, /, %, +/-, backspace.

**Pelajaran:** Lambda di `connect()` = satu slot menangani banyak tombol. Pisahkan state dari UI.

---

### Bab 27 -- Threading Dasar
> **Script:** [`bab27_threading.py`](script/bab27_threading.py)

`QThread` untuk pekerjaan berat agar UI tidak membeku. WorkerThread dengan signal `progress`/`finished`/`error`. Komunikasi thread -> UI via signal. Flag kooperatif untuk stop aman.

**Pelajaran:** Jangan blokir thread utama. Komunikasi harus melalui signal, bukan akses langsung widget.

---

### Bab 28 -- Mouse Events
> **Script:** [`bab28_mouse_events.py`](script/bab28_mouse_events.py)

Override 6 handler: `mousePressEvent`, `mouseReleaseEvent`, `mouseMoveEvent`, `enterEvent`, `leaveEvent`, `mouseDoubleClickEvent`. `setMouseTracking(True)` untuk tracking tanpa klik. Deteksi drag (press -> move -> release).

**Pelajaran:** Pola press -> move -> release adalah dasar fitur drag, drawing, dan selection.

---

### Bab 29 -- Keyboard Events
> **Script:** [`bab29_keyboard_events.py`](script/bab29_keyboard_events.py)

`keyPressEvent`/`keyReleaseEvent` dengan `event.key()` dan `event.modifiers()`. Shortcut sederhana (Ctrl+Q, Ctrl+C). Riwayat 10 tombol terakhir.

**Pelajaran:** Untuk shortcut formal, pertimbangkan `QShortcut` (Bab 42).

---

### Bab 30 -- Drag and Drop
> **Script:** [`bab30_drag_drop.py`](script/bab30_drag_drop.py)

`DraggableListWidget` (sumber) dan `DropArea` (penerima). `QMimeData` sebagai format data universal. Visual feedback (border hijau saat drag). `setAcceptDrops(True)` wajib pada penerima.

**Pelajaran:** Visual feedback saat drag penting agar pengguna tahu area mana yang menerima drop.

---

### Bab 31 -- TreeWidget
> **Script:** [`bab31_treewidget.py`](script/bab31_treewidget.py)

`QTreeWidget` untuk data hierarkis. Multi-kolom (Name, Type, Size). Navigasi klik (full path via rekursi). Manipulasi: Add Root/Child, Delete, Expand/Collapse All.

**Pelajaran:** Ideal untuk data hierarkis dengan kedalaman tak terbatas.

---

### Bab 32 -- StackedWidget
> **Script:** [`bab32_stackedwidget.py`](script/bab32_stackedwidget.py)

`QStackedWidget` menampilkan satu halaman pada satu waktu. Empat kelas halaman. Sidebar `QListWidget` dengan `currentRowChanged` -> `setCurrentIndex`.

**Pelajaran:** Ideal untuk wizard, dashboard, atau aplikasi multi-view. Pisahkan halaman ke kelas terpisah.

---

### Bab 33 -- Graphics View
> **Script:** [`bab33_graphicsview.py`](script/bab33_graphicsview.py)

`QGraphicsScene` (kanvas) + `QGraphicsView` (jendela tampilan). Bentuk bawaan (rect, ellipse, line, text). `ItemIsMovable` + `ItemIsSelectable`. Toolbar interaktif + color dialog.

**Pelajaran:** Cocok untuk editor diagram, game 2D, atau visualisasi data interaktif.

---

### Bab 34 -- Context Menu
> **Script:** [`bab34_context_menu.py`](script/bab34_context_menu.py)

Menu klik kanan kustom: `CustomContextMenu` + `customContextMenuRequested`. Menu berbeda per konteks (item vs area kosong). CRUD: Open, Edit, Copy, Delete + konfirmasi.

**Pelajaran:** `menu.exec_(mapToGlobal(pos))` untuk posisi yang benar. Konfirmasi sebelum aksi destruktif.

---

### Bab 35 -- System Tray
> **Script:** [`bab35_system_tray.py`](script/bab35_system_tray.py)

`QSystemTrayIcon` untuk background app. Menu tray (Show/Hide/Notify/Quit). Override `closeEvent` untuk minimize-to-tray. Balloon notification via `showMessage()`.

**Pelajaran:** `setQuitOnLastWindowClosed(False)` agar app tidak mati saat jendela hilang.

---

### Bab 36 -- Custom Widget
> **Script:** [`bab36_custom_widget.py`](script/bab36_custom_widget.py)

Membuat widget kustom via `paintEvent()` + `QPainter`: CircularProgress (busur + teks), ToggleSwitch (on/off ala iOS), StarRating (5 bintang interaktif). Signal kustom `pyqtSignal`.

**Pelajaran:** Override `paintEvent()` + `QPainter` adalah kunci widget visual kustom. Panggil `update()` setelah ubah state.

---

### Bab 37 -- Form Layout
> **Script:** [`bab37_form_layout.py`](script/bab37_form_layout.py)

`QFormLayout` menata label-input dalam dua kolom. Tiga `QGroupBox` (Pribadi, Alamat, Preferensi). Ragam widget: `QLineEdit`, `QComboBox`, `QDateEdit`, `QSpinBox`, `QDoubleSpinBox`, `QCheckBox`, `QTextEdit`. Validasi saat submit.

**Pelajaran:** `QFormLayout` menghilangkan kerumitan menata label dan input secara manual.

---

### Bab 38 -- Validator
> **Script:** [`bab38_validator.py`](script/bab38_validator.py)

`QValidator` mencegah input salah sejak awal. `QIntValidator`/`QDoubleValidator` (bawaan), custom validator (Email, Phone), `QRegularExpressionValidator` (regex). Status visual real-time (hijau/kuning/merah).

**Pelajaran:** Tiga status (Acceptable, Intermediate, Invalid) membuat UX terasa responsif.

---

### Bab 39 -- Splash Screen
> **Script:** [`bab39_splash_screen.py`](script/bab39_splash_screen.py)

`QSplashScreen` kustom dengan `QPainter` menggambar judul dan progress bar ke `QPixmap`. Simulasi loading via `QTimer.singleShot`. `splash.finish(window)` menutup splash otomatis.

**Pelajaran:** Splash screen meningkatkan *perceived performance*. Bisa dibuat programatik tanpa file gambar.

---

### Bab 40 -- Status Bar
> **Script:** [`bab40_statusbar.py`](script/bab40_statusbar.py)

`statusBar().showMessage()` untuk pesan sementara. `addPermanentWidget()` untuk widget tetap (progress bar, jam, koordinat mouse). Interaksi real-time: karakter count, koordinat, animasi.

**Pelajaran:** Pesan sementara untuk notifikasi singkat, widget permanen untuk info terus-menerus.

---

## Bagian 4: Proyek Akhir (Bab 41--50)

### Bab 41 -- Notes App
> **Script:** [`bab41_notes_app.py`](script/bab41_notes_app.py)

Aplikasi catatan: arsitektur master-detail (`QSplitter` + sidebar + editor), CRUD catatan (dictionary JSON), pencarian instan (`setHidden`), persistensi JSON, ekspor/impor via `QFileDialog`.

**Pelajaran:** Pola master-detail adalah fondasi aplikasi produktivitas. Pencarian instan > pencarian tombol Submit.

---

### Bab 42 -- Shortcut Keys
> **Script:** [`bab42_shortcuts.py`](script/bab42_shortcuts.py)

`QShortcut` + `QKeySequence` untuk shortcut formal. Satu baris per shortcut. Undo/redo bawaan `QTextEdit`. Tabel referensi shortcut di UI.

**Pelajaran:** `QShortcut` lebih bersih dari `keyPressEvent`. Selalu sediakan referensi shortcut yang terlihat.

---

### Bab 43 -- Internationalization (i18n)
> **Script:** [`bab43_i18n.py`](script/bab43_i18n.py)

Kelas `Translator` (dictionary 4 bahasa: EN, ID, JP, CN). Combo box pemilih bahasa. Update UI dinamis tanpa restart. Cakupan: label, placeholder, tombol, judul, dialog, status bar.

**Pelajaran:** Pisahkan semua string UI ke sistem terjemahan. Untuk proyek besar, gunakan Qt Linguist.

---

### Bab 44 -- Database SQLite
> **Script:** [`bab44_database_sqlite.py`](script/bab44_database_sqlite.py)

SQLite tanpa instalasi. CRUD lengkap (INSERT/SELECT/UPDATE/DELETE) dengan parameterized queries. Pencarian `LIKE`. Tombol Edit/Delete per baris. Backup ke JSON. Tutup koneksi di `closeEvent`.

**Pelajaran:** SQLite ideal untuk desktop single-user. Selalu gunakan parameterized queries (`?`) untuk cegah SQL injection.

---

### Bab 45 -- Network Request
> **Script:** [`bab45_network.py`](script/bab45_network.py)

`QNetworkAccessManager` untuk HTTP asinkron (GET/POST/PUT/DELETE). Form: URL + metode + body JSON. Respons di-parse dan ditampilkan rapi. Signal `finished` untuk proses asinkron.

**Pelajaran:** Asinkron = UI tidak membeku. Selalu tangani error jaringan.

---

### Bab 46 -- Animation
> **Script:** [`bab46_animation.py`](script/bab46_animation.py)

`QPropertyAnimation` untuk posisi, ukuran, dan warna kustom (`pyqtProperty`). Easing curves: Linear, InOutCubic, OutElastic, OutBounce. Animation groups (sequential + parallel).

**Pelajaran:** Easing curves memberi karakter animasi. Gunakan secukupnya.

---

### Bab 47 -- Proyek Akhir: Address Book
> **Script:** [`bab47_address_book.py`](script/bab47_address_book.py)

Integrasi lengkap: database SQLite, `ContactDialog` (QDialog kustom), tabel dengan tombol View/Edit/Delete per baris, pencarian + filter kategori, ekspor/impor CSV.

**Pelajaran:** Proyek nyata menggabungkan banyak konsep kecil. CSV adalah format pertukaran paling universal.

---

### Bab 48 -- Proyek Akhir: File Manager
> **Script:** [`bab48_file_manager.py`](script/bab48_file_manager.py)

Navigasi direktori (Back/Up/Home/Refresh), `os.listdir()` + `QFileIconProvider`, context menu (New/Rename/Copy/Cut/Paste/Delete), `shutil` untuk operasi file, konfirmasi + try-except.

**Pelajaran:** Modul `os` dan `shutil` menyediakan semua operasi file. Selalu tangani error I/O.

---

### Bab 49 -- Proyek Akhir: Unit Converter
> **Script:** [`bab49_unit_converter.py`](script/bab49_unit_converter.py)

Konverter 8 kategori (Panjang, Berat, Suhu, Volume, Area, Kecepatan, Waktu, Data) via `QTabWidget`. Logika faktor basis (semua unit -> basis -> tujuan). Kasus khusus suhu (offset). Tampilan formula. Tombol swap.

**Pelajaran:** Konversi berbasis faktor basis skalabel -- mudah tambah unit baru. Suhu harus ditangani terpisah.

---

### Bab 50 -- Proyek Akhir: Pomodoro Timer
> **Script:** [`bab50_pomodoro_timer.py`](script/bab50_pomodoro_timer.py)

Timer Pomodoro lengkap: state machine (Work/Short Break/Long Break), countdown `QTimer` (1000ms), manajemen tugas (`QListWidget`), statistik (Pomodoro count + total waktu), pengaturan durasi (`QSpinBox`), notifikasi (`beep` + `QMessageBox`).

**Pelajaran:** State machine sederhana (variabel + if/elif) cukup untuk alur aplikasi kecil. Proyek ini merangkum seluruh modul.

---

## Struktur Folder

```
project1/
├── .gitignore                         # Aturan file yang diabaikan Git
├── MR_pyqt5_modul_pjbl1_d4_2026.pdf   # PDF modul
├── README.md                          # Dokumentasi proyek (file ini)
├── requirements.txt                   # Daftar dependensi Python
└── script/                            # Skrip Python per bab
    ├── bab02_jendela_kosong.py
    ├── bab03_label.py
    ├── bab04_tombol.py
    ├── bab05_layout.py
    ├── bab06_form.py
    ├── bab07_signal_slot.py
    ├── bab08_widget_keren.py
    ├── bab09_menu_toolbar.py
    ├── bab10_styling.py
    ├── bab11_todo_app.py
    ├── bab12_spin_dial.py
    ├── bab13_radiobutton.py
    ├── bab14_checkbox.py
    ├── bab15_combobox.py
    ├── bab16_datetime.py
    ├── bab17_listwidget.py
    ├── bab18_tablewidget.py
    ├── bab19_tabwidget.py
    ├── bab20_scrollarea.py
    ├── bab21_splitter.py
    ├── bab22_dialog.py
    ├── bab23_timer.py
    ├── bab24_settings.py
    ├── bab25_clipboard.py
    ├── bab26_calculator.py
    ├── bab27_threading.py
    ├── bab28_mouse_events.py
    ├── bab29_keyboard_events.py
    ├── bab30_drag_drop.py
    ├── bab31_treewidget.py
    ├── bab32_stackedwidget.py
    ├── bab33_graphicsview.py
    ├── bab34_context_menu.py
    ├── bab35_system_tray.py
    ├── bab36_custom_widget.py
    ├── bab37_form_layout.py
    ├── bab38_validator.py
    ├── bab39_splash_screen.py
    ├── bab40_statusbar.py
    ├── bab41_notes_app.py
    ├── bab42_shortcuts.py
    ├── bab43_i18n.py
    ├── bab44_database_sqlite.py
    ├── bab45_network.py
    ├── bab46_animation.py
    ├── bab47_address_book.py
    ├── bab48_file_manager.py
    ├── bab49_unit_converter.py
    └── bab50_pomodoro_timer.py
```

## Cara Aktivasi Virtual Env

Cara yang disarankan ada di bagian **Persiapan** di atas. Contoh singkat di Windows (PowerShell):

```powershell
cd "C:\project1"   # sesuaikan dengan lokasi folder proyek Anda
python -m venv venv
venv\Scripts\Activate.ps1
```

## Menjalankan Contoh Script PyQt5

Setelah virtual environment aktif dan dependensi terpasang, Anda bisa menjalankan contoh-contoh skrip di folder `script/`.

Contoh menjalankan bab 2 (jendela kosong) di Windows (PowerShell):

```powershell
cd "C:\project1"
venv\Scripts\Activate.ps1   # jika belum aktif
python script/bab02_jendela_kosong.py
```

---

*PyQt5 Version: 5.15.11*
*Last updated: 2026-02-21*
