import os

menu_utama = ["Tambah Barang", "Edit Barang", "Hapus Barang", "Lihat Barang", "Cari Barang", "Filter Stok", "Keluar"]
barang_lengkap = {}

def bersihin_layar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system(clear)

def tampilan_menu ():
    print("===== MENU UTAMA =====")
    for nomor, menu in enumerate(menu_utama, start=1):
        print(f"{nomor}. {menu}")

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
                barang = input("Masukkan Nama Barang: ")
                if barang == "":
                    print("Data Tidak Boleh Kosong")
                else:
                    break

            while True:
                bersihin_layar()
                input_jumlah = input(f"Masukkan Jumlah Barang {barang}: ")
                if not input_jumlah.isdigit():
                    print("Masukkan angka bang!")
                else:
                    break

            jumlah = int(input_jumlah)
            
            while True:
                bersihin_layar()
                input_harga = input(f"Masukkan Harga Barang {barang}: ")
                if not input_harga.isdigit():
                    print("Masukkan angka bang!")
                else:
                    break

            harga = int(input_harga)

            while True:
                bersihin_layar()
                kategori = input(f"Masukkan Kategori Barang {barang}: ")
                if kategori == "":
                    print("Wajib Diisi inimah!")
                else:
                    break

            bersihin_layar()

            barang_lengkap[barang] = {
                "Stok" : jumlah,
                "Harga" : harga,
                "Kategori" : kategori
            }

            print(f"Barang dengan nama {barang}, berjumlah {jumlah}, dengan harga Rp.{harga},00, berhasil di tambahkan pada kategori {kategori}!")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Edit Barang
    elif pilihan == 2:
        while True:
            bersihin_layar()

            if not barang_lengkap:
                print("Barang sedang kosong")
                jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
                break
            elif barang_lengkap:
                for nomor, (barang, atribut) in enumerate(barang_lengkap.items(), start=1):
                    jumlah = atribut["Stok"]
                    harga = atribut["Harga"]
                    kategori = atribut["Kategori"]

                    daftarKunci = list(barang_lengkap.keys())
                    print(f"{nomor}. {barang}, Stok: {jumlah}, Harga :Rp.{harga},00 , Kategori: {kategori}")

            while True:
                jwbEdit = input("Silahkan Pilih Barang yang ingin di edit: ")
                if not jwbEdit.isdigit():
                    print("Isi dengan angka")
                    continue

                barangPilihan = int(jwbEdit)

                if barangPilihan <= 0:
                    print("Silahkan Pilih Barang Yang tersedia!")
                    continue
                elif barangPilihan > len(daftarKunci):
                    print("Pilih Barang yang Tersedia!")
                    continue
                break

            listAsli = barangPilihan - 1
            targetBarang = daftarKunci[listAsli]

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

            del barang_lengkap[targetBarang]

            barang_lengkap[editBarang] ={
                "Stok" : editJumlah,
                "Harga" : editHarga,
                "Kategori" : inputeditKategori
            }

            bersihin_layar()

            print(f"Barang Berhasil Diperbarui Menjadi {editBarang}, dengan stok {editJumlah}, dengan harga sebesar {editHarga} pada kategori {inputeditKategori}")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Hapus Barang
    elif pilihan == 3:
        while True:
            bersihin_layar()

            if not barang_lengkap:
                print("Barang sedang kosong")
                jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
                break
            elif barang_lengkap:
                for nomor, (barang, atribut) in enumerate(barang_lengkap.items(), start=1):
                    jumlah = atribut["Stok"]
                    harga = atribut["Harga"]
                    kategori = atribut["Kategori"]

                    daftarKunci = list(barang_lengkap.keys())
                    print(f"{nomor}. {barang}, Stok: {jumlah}, Harga :Rp.{harga},00 , Kategori: {kategori}")

            while True:
                jwbHapus = input("Silahkan Pilih Barang yang ingin di Hapus: ")
                if not jwbHapus.isdigit():
                    print("Isi dengan angka")
                    continue

                barangPilihanhps = int(jwbHapus)

                if barangPilihanhps <= 0:
                    print("Silahkan Pilih Barang Yang tersedia!")
                    continue
                elif barangPilihanhps > len(daftarKunci):
                    print("Pilih Barang yang Tersedia!")
                    continue
                break

            listAsli = barangPilihanhps - 1
            targetBarang = daftarKunci[listAsli]

            del barang_lengkap[targetBarang]

            bersihin_layar()

            print("Barang Berhasil Di hapus")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Lihat Barang
    elif pilihan == 4:
        while True:
            bersihin_layar()

            if not barang_lengkap:
                print("Barang sedang kosong")
                jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
                break
            elif barang_lengkap:
                for nomor, (barang, atribut) in enumerate(barang_lengkap.items(), start=1):
                    jumlah = atribut["Stok"]
                    harga = atribut["Harga"]
                    kategori = atribut["Kategori"]

                    print(f"{nomor}. {barang}, Stok: {jumlah}, Harga :Rp.{harga},00 , Kategori: {kategori}")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Cari Barang
    elif pilihan == 5:
        while True:
            bersihin_layar()

            while True:
                cari_barang = input("Masukkan Nama Barang yang Ingin dicari: ")
                if cari_barang == "":
                    print("Data Tidak Boleh Kosong") 
                    continue
                elif barang_lengkap:
                    for (barang, atribut) in (barang_lengkap.items()):
                        jumlah = atribut["Stok"]
                        harga = atribut["Harga"]
                        kategori = atribut["Kategori"]
                break


            if cari_barang not in barang_lengkap:
                print("Barang Tidak Ditemukan!")
                balik = input("\nTekan enter untuk kembali mencari")
                continue
            elif cari_barang in barang_lengkap:
                    detail = barang_lengkap.get(cari_barang)
                    detailStok = detail["Stok"]
                    detailHarga = detail["Harga"]
                    detailKategori = detail["Kategori"]

            print(f"Barang dengan nama {cari_barang}, dengan jumlah stok {detailStok}, Harganya Rp.{detailHarga}, Pada kategori {detailKategori} berhasil ditemukan")
            
            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    elif pilihan == 6:
        print("Nah cuma ini doang yang ada wkkwkw")
        break

    elif pilihan == 7:
        print("Nah cuma ini doang yang ada wkkwkw")
        break

    else:
        print("Pilih yang bener bang")
        input("\ntekan enter untuk lanjut")
