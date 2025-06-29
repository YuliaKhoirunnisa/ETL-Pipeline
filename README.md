###ETL Pipeline: Fashion Studio

📦 Cara menjalankan script ETL Pipeline:
1. Pastikan semua dependensi sudah terinstal dengan menjalankan:
   pip install -r requirements.txt

2. Jalankan pipeline utama dengan perintah:
   python main.py

Script ini akan melakukan:
- Extract: Mengambil data dari website Fashion Studio.
- Transform: Membersihkan dan mengolah data (konversi harga, parsing rating, dll).
- Load: Menyimpan data ke file CSV dan Google Sheets.

📦 Cara menjalankan Unit Test:
Untuk saat ini, project ini belum dilengkapi dengan Unit Test terpisah.
Unit Test direkomendasikan dibuat di folder `tests/` menggunakan framework `pytest`.
Contoh dasar (belum tersedia):
- Test untuk fungsi `transform_data` pada file `transform.py`
- Test koneksi Google Sheets di `load.py`

📦 Cara menjalankan Test Coverage:
Project ini belum dilengkapi dengan laporan Test Coverage.
Test Coverage dapat dihasilkan menggunakan `pytest` dan plugin `pytest-cov` dengan contoh perintah:
   pytest --cov=.

📦 URL Google Sheets:
https://docs.google.com/spreadsheets/d/1cDnMTZvIsQxJTwOwTtJzlZpqnGCyBdLZO-ILYYctOtc/edit?usp=sharing
