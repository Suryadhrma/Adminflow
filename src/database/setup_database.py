import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db") 

def inisialisasi_database():
    koneksi = sqlite3.connect(db_path)
    kursor = koneksi.cursor()

    kursor.execute('''
        CREATE TABLE IF NOT EXIST Barang(
        kode_barang TEXT PRIMARY KEY,
        nama_barang TEXT,
        stok INTEGER,
        harga INTEGER,
        kategori TEXT
        )
    ''')

    koneksi.close()

inisialisasi_database()



