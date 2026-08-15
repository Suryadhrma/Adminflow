import sqlite3
import os

def inisialisasi_database():
    db_path = os.path.join("src/database/database.db")

    koneksi = sqlite3.connect(db_path)
    kursor = koneksi.cursor()

    kursor.execute('''
        CREATE TABLE Barang (
        kode_barang TEXT PRIMARY KEY,
        nama_barang TEXT,
        stok INTEGER,
        kategori TEXT
        )
    ''')

    koneksi.close()

inisialisasi_database()



