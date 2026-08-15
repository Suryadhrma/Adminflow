import sqlite3

def inisialisasi_database():
    koneksi = sqlite3.connect("database.db")
    kursor = koneksi.cursor()

    kursor.execute('''
        CREATE TABLE IF NOT EXIST Barang (
        kode_barang TEXT PRIMARY KEY AUTOINCREMENT,
        nama_barang TEXT,
        stok INTEGER,
        kategori TEXT
        )
    ''')

    koneksi.close()



