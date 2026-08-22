import os
import sqlite3
import uuid

menu_utama = ["Tambah Barang", "Edit Barang", "Hapus Barang", "Lihat Barang", "Cari Barang", "Filter Stok", "Urutkan Harga", "Keluar"]
menu_sorting =["Urutkan Harga Dari Yang Termurah", "Urutkan Harga Dari Yang Termahal"]

#Koneksi Database
db_path = os.path.join("src/database/database.db")
koneksi = sqlite3.connect(db_path)
kursor = koneksi.cursor()

def bersihin_layar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tampilan_menu ():
    print("===== MENU UTAMA =====")
    for nomor, menu in enumerate(menu_utama, start=1):
        print(f"{nomor}. {menu}")

def tampilan_menu_sorting ():
    print("===== MENU PENGURUTAN =====")
    for nomor, menup in enumerate(menu_sorting, start=1):
        print(f"{nomor}. {menup}")

def bongkar_db ():
    list_barang = []

    try:
        kursor.execute("SELECT * FROM Barang")
        for barang in enumerate(kursor, start=1):
            print(f"{barang[0]}. Kode Barang: {barang[1][0]} | Nama Barang: {barang[1][1]} | Stok: {barang[1][2]} | Harga: {barang[1][3]} |")
            list_barang.append(barang[1])

        return list_barang
    except sqlite3.DatabaseError:
        print("Database Tidak Merespon")
        return

def getbarangbyKode():
    list_barang = []

    try:
        kursor.execute("SELECT * FROM Barang")
        for barang in kursor:
            list_barang.append(barang)
        return list_barang
    except sqlite3.Error as e:
        print(f"Database Tidak Merespon: {e}")
        return []

def cari_barang (barang, carinama_barang):
    hasil_cari = False

    for nomor, brg in enumerate(barang, start= 1):
        if carinama_barang.lower() == brg[1].lower():
            print(f"{nomor}. Kode Barang: {brg[0]} | Nama Barang: {brg[1]} | Stok: {brg[2]} | Harga: {brg[3]} | Kategori: {brg[4]}")
            hasil_cari = True
    if not hasil_cari:
        print("Barang Tidak Ditemukan")
    return hasil_cari

def cari_kategori (barang, carinamakategori):
    barang_ditemukan = False

    for nomor,brg in enumerate(barang, start=1):
        if carinamakategori.lower() == brg[4].lower():
            barang_ditemukan = True
            print(f"{nomor}. Kode Barang: {brg[0]} | Nama Barang: {brg[1]} | Stok: {brg[2]} | Harga: {brg[3]} | Kategori: {brg[4]}")

    if not barang_ditemukan:
        print("Tidak ditemukan Barang")
    return barang_ditemukan

while True:
    bersihin_layar()
    
    tampilan_menu()

    pilihan_user = input("\nPilih Menu:")

    if not pilihan_user.isdigit():
        print("Masukkan Angka")
        continue

    pilihan = int(pilihan_user)

    #Tambah Barang
    if pilihan == 1:
        while True:
            bersihin_layar()

            while True:
                bersihin_layar()
                nama_barang = input("Masukkan Nama Barang: ")
                if nama_barang == "":
                    print("Data Tidak Boleh Kosong")
                    input("\n Tekan Enter....")
                    continue
                else:
                    break

            while True:
                bersihin_layar()
                input_jumlah = input(f"Masukkan Jumlah Barang {nama_barang}: ")
                if not input_jumlah.isdigit():
                    print("Masukkan angka bang!")
                    input("\n Tekan Enter....")
                    continue
                else:
                    break

            jumlah = int(input_jumlah)
            
            while True:
                bersihin_layar()
                input_harga = input(f"Masukkan Harga Barang {nama_barang}: ")
                if not input_harga.isdigit():
                    print("Masukkan angka bang!")
                    input("\n Tekan Enter....")
                    continue
                else:
                    break

            harga = int(input_harga)

            while True:
                bersihin_layar()
                kategori = input(f"Masukkan Kategori Barang {nama_barang}: ")
                if kategori == "":
                    print("Wajib Diisi inimah!")
                    input("\n Tekan Enter....")
                    continue
                else:
                    break

            bersihin_layar()

            kode_barang = uuid.uuid4()

            try:
                kursor.execute("INSERT INTO Barang (kode_barang, nama_barang, stok, harga, kategori) VALUES (?, ?, ?, ?, ?) IF kode_barang NOT EXIST", (kode_barang, nama_barang, jumlah, harga, kategori))
                print(f"Barang dengan kode {kode_barang}, nama {nama_barang}, berjumlah {jumlah}, dengan harga Rp.{harga},00, berhasil di tambahkan pada kategori {kategori}!")
                koneksi.commit()

            except sqlite3.IntegrityError:
                print("Terdapat Data Duplikat")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Edit Barang
    elif pilihan == 2:
        while True:
            bersihin_layar()

            barang_lengkap = bongkar_db()

            while True:
                jwbEdit = input("Silahkan Pilih Barang yang ingin di edit: ")
                if not jwbEdit.isdigit():
                    print("Isi dengan angka")
                    continue

                barangPilihan = int(jwbEdit)

                if barangPilihan <= 0:
                    print("Silahkan Pilih Barang Yang tersedia!")
                    continue
                elif barangPilihan > len(barang_lengkap):
                    print("Pilih Barang yang Tersedia!")
                    continue
                break

            listAsli = barangPilihan - 1
            targetBarang = barang_lengkap[listAsli]

            bersihin_layar()

            while True:
                editBarang = input("\n Ubah Nama Barangnya Menjadi: ")
                if editBarang == "":
                    print("\n Nama Barangnya wajib di isi!")
                    continue
                else:
                    break

            while True:
                inputeditJumlah = input("\n Ubah Jumlah Barangnya Menjadi: ")

                if not inputeditJumlah.isdigit():
                    print("\n Harus Input Dengan Angka!")
                    continue

                editJumlah = int(inputeditJumlah)
                break
                

            while True:
                inputeditHarga = input("\n Ubah Harga Barangnya Menjadi: Rp.")

                if not inputeditHarga.isdigit():
                    print("\n Harus Input Dengan Angka!")
                    continue

                editHarga = int(inputeditHarga)
                break

            while True:
                inputeditKategori = input("\n Ubah Kategori Barangnya Menjadi: ")

                if inputeditKategori == "":
                    print("\n Harus Diisi!")
                    continue
                break
            
            data_update = (editBarang, editJumlah, editHarga, inputeditKategori, targetBarang[0])

            kursor.execute('''
            UPDATE Barang
            set nama_barang = ?, stok = ?, harga = ?, kategori = ?
            WHERE kode_barang = ?
            ''', data_update)

            koneksi.commit()

            bersihin_layar()

            print(f"Barang Berhasil Diperbarui Menjadi {editBarang}, dengan stok {editJumlah}, dengan harga sebesar {editHarga} pada kategori {inputeditKategori}")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Hapus Barang
    elif pilihan == 3:
        while True:
            bersihin_layar()

            barang_lengkap = bongkar_db()

            while True:
                jwbHapus = input("Silahkan Pilih Barang yang ingin di Hapus: ")
                if not jwbHapus.isdigit():
                    print("Isi dengan angka")
                    continue

                barangPilihanhps = int(jwbHapus)

                if barangPilihanhps <= 0:
                    print("Silahkan Pilih Barang Yang tersedia!")
                    continue
                elif barangPilihanhps > len(barang_lengkap):
                    print("Pilih Barang yang Tersedia!")
                    continue
                break

            listAsli = barangPilihanhps - 1
            targetBarang = barang_lengkap[listAsli]

            kursor.execute('''
                DELETE FROM Barang
                WHERE kode_barang = ?
            ''', targetBarang[0])

            koneksi.commit()

            bersihin_layar()

            print("Barang Berhasil Di hapus")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Lihat Barang
    elif pilihan == 4:
        while True:
            bersihin_layar()

            barang_lengkap = bongkar_db()

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Cari Barang
    elif pilihan == 5:
        while True:
            bersihin_layar()

            barang_lengkap = getbarangbyKode()

            inputcari_barang = input("Masukkan Nama Barang yang Ingin dicari: ")
            if inputcari_barang == "":
                print("Data Tidak Boleh Kosong") 
                input("Tekan Enter Untuk Lanjut")
                continue
            
            hasil = cari_barang(barang_lengkap, inputcari_barang)

            input("\n Kembali Ke Menu Utama")
            break

    #Filter Barang
    elif pilihan == 6:
        while True:
            bersihin_layar()

            barang_lengkap = getbarangbyKode()
        
            jwbKategori = input("Silahkan Cari Kategori Barang yang ingin Anda Lihat: ")
            if jwbKategori == "":
                print("Kategori Wajib Diisi!")
                input("\n Tekan Enter Untuk Kembali")
                continue

            hasil = cari_kategori(barang_lengkap, jwbKategori)

            input("\nTekan Enter Untuk Kembali ke Menu Utama")
            break

    #Urut Harga
    elif pilihan == 7:
        while True: 
            bersihin_layar()

            barang_lengkap = getbarangbyKode()

            tampilan_menu_sorting()

            inputan_user = input("Pilih Menu Pengurutan: ")

            if not inputan_user.isdigit():
                print("Masukkan Angka")
                input("\n Tekan Enter Untuk Lanjut")
                continue

            input_sorting = int(inputan_user)

            if input_sorting == 1:
                bersihin_layar()

                hasilurutMurah = sorted(
                    barang_lengkap,
                    key=lambda x: x[3]
                )

                for nomor,brg in enumerate(hasilurutMurah, start=1):
                    print(f"{nomor}. Kode Barang: {brg[0]} | Nama Barang: {brg[1]} | Stok: {brg[2]} | Harga: {brg[3]} | Kategori: {brg[4]}")
                            
            elif input_sorting == 2:
                bersihin_layar()

                hasilurutMahal = sorted(
                    barang_lengkap,
                    key=lambda x: x[3],
                    reverse=True
                )

                for nomor,brg in enumerate(hasilurutMahal, start=1):
                    print(f"{nomor}. Kode Barang: {brg[0]} | Nama Barang: {brg[1]} | Stok: {brg[2]} | Harga: {brg[3]} | Kategori: {brg[4]}")

            input("\nTekan Enter Untuk Kembali ke Menu Utama")
            break

    elif pilihan == 8:
        print("Terimakasih")
        koneksi.close()
        break

    else:
        print("Pilih yang bener bang")
        input("\ntekan enter untuk lanjut")
        continue
