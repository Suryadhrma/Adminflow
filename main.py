import os
import json

menu_utama = ["Tambah Barang", "Edit Barang", "Hapus Barang", "Lihat Barang", "Cari Barang", "Filter Stok", "Urutkan Harga", "Keluar"]
menu_sorting =["Urutkan Harga Dari Yang Termurah", "Urutkan Harga Dari Yang Termahal"]
barang_lengkap = {}

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
                kode_barang = input("Masukkan Kode Barang: ")
                if kode_barang == "":
                    print("Data Tidak Boleh Kosong")
                    input("\n Tekan Enter....")
                    continue
                else:
                    break

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

            barang_lengkap [kode_barang]= {
                "Nama Barang" : nama_barang,
                "Stok" : jumlah,
                "Harga" : harga,
                "Kategori" : kategori
            }

            print(f"Barang dengan kode {kode_barang}, nama {nama_barang}, berjumlah {jumlah}, dengan harga Rp.{harga},00, berhasil di tambahkan pada kategori {kategori}!")

            with open("data_barang.json", "w") as file:
                json.dump(barang_lengkap, file, indent=4)

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Edit Barang
    elif pilihan == 2:
        while True:
            bersihin_layar()

            try:
                with open("data_barang.json", "r") as file:
                    barang_lengkap = json.load(file)
            except json.JSONDecodeError:
                print("Error Format JSON Tidak Valid")
            except Exception as e:
                print("Terjadi Kesalahan")

            if not barang_lengkap:
                print("Barang sedang kosong")
                jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
                break
            elif barang_lengkap:
                for nomor, (kode_barang,atribut) in enumerate(barang_lengkap.items(), start=1):
                    nama_barang = atribut["Nama Barang"]
                    jumlah = atribut["Stok"]
                    harga = atribut["Harga"]
                    kategori = atribut["Kategori"]

                    daftarKunci = list(barang_lengkap.keys())
                    print(f"{nomor}. {kode_barang} {nama_barang}, Stok: {jumlah}, Harga :Rp.{harga},00 , Kategori: {kategori}")

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
                editkodeBarang = input("\n Ubah Kode Barangnya Menjadi: ")
                if editkodeBarang == "":
                    print("\n Kode Barangnya wajib di isi!")
                    continue
                else:
                    break

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

            barang_lengkap [editkodeBarang]={
                "Nama Barang" : editBarang,
                "Stok" : editJumlah,
                "Harga" : editHarga,
                "Kategori" : inputeditKategori
            }

            with open("data_barang.json", "w") as file:
                json.dump(barang_lengkap, file, indent=4)

            bersihin_layar()

            print(f"Barang Berhasil Diperbarui Menjadi {editBarang}, dengan stok {editJumlah}, dengan harga sebesar {editHarga} pada kategori {inputeditKategori}")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Hapus Barang
    elif pilihan == 3:
        while True:
            bersihin_layar()

            with open("data_barang.json", "r") as file:
                barang_lengkap = json.load(file)

            if not barang_lengkap:
                print("Barang sedang kosong")
                input("\nTekan enter untuk kembali ke menu utama")
                break
            elif barang_lengkap:
                for nomor, (kode_barang, atribut) in enumerate(barang_lengkap.items(), start=1):
                    nama_barang = atribut["Nama Barang"]
                    jumlah = atribut["Stok"]
                    harga = atribut["Harga"]
                    kategori = atribut["Kategori"]

                    daftarKunci = list(barang_lengkap.keys())
                    print(f"{nomor}. {nama_barang}, Stok: {jumlah}, Harga :Rp.{harga},00 , Kategori: {kategori}")

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

            with open("data_barang.json", "w") as file:
                json.dump(barang_lengkap, file, indent=4)

            bersihin_layar()

            print("Barang Berhasil Di hapus")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Lihat Barang
    elif pilihan == 4:
        while True:
            bersihin_layar()

            with open("data_barang.json", "r") as file:
                barang_lengkap = json.load(file)

            if not barang_lengkap:
                print("Barang sedang kosong")
                jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
                break
            elif barang_lengkap:
                for nomor, (kode_barang, atribut) in enumerate(barang_lengkap.items(), start=1):
                    nama_barang = atribut["Nama Barang"]
                    jumlah = atribut["Stok"]
                    harga = atribut["Harga"]
                    kategori = atribut["Kategori"]

                    print(f"{nomor}. {kode_barang} {nama_barang}, Stok: {jumlah}, Harga :Rp.{harga},00 , Kategori: {kategori}")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    #Cari Barang
    elif pilihan == 5:
        while True:
            bersihin_layar()

            with open("data_barang.json", "r") as file:
                barang_lengkap = json.load(file)

            cari_barang = input("Masukkan Nama Barang yang Ingin dicari: ")
            if cari_barang == "":
                print("Data Tidak Boleh Kosong") 
                input("Tekan Enter Untuk Lanjut")
                continue

            hasil_cari = False

            for (kode_barang, atribut) in (barang_lengkap.items()):
                nama_barang = atribut["Nama Barang"]
                jumlah = atribut["Stok"]
                harga = atribut["Harga"]
                kategori = atribut["Kategori"]
                if cari_barang == nama_barang:
                    print(f"Kode Barang: {kode_barang}, Nama Barang: {nama_barang}, Jumlah Stok: {jumlah}, Harga: {harga}, Kategori: {kategori}")
                    hasil_cari = True
                    
            if not hasil_cari:
                print("Barang Tidak Ditemukan")

            input("\n Kembali Ke Menu Utama")
            break

    #Filter Barang
    elif pilihan == 6:
        while True:
            bersihin_layar()

            with open("data_barang.json", "r") as file:
                barang_lengkap = json.load(file)
        
            jwbKategori = input("Silahkan Cari Kategori Barang yang ingin Anda Lihat: ")
            if jwbKategori == "":
                print("Kategori Wajib Diisi!")
                input("\n Tekan Enter Untuk Kembali")
                continue

            barang_ditemukan = False

            for kode_barang in barang_lengkap:
                detail = barang_lengkap.get(kode_barang)
                detailNamaBarang = detail["Nama Barang"]
                detailStok = detail["Stok"]
                detailHarga = detail["Harga"]
                detailKategori = detail["Kategori"]
                
                if jwbKategori == detailKategori:
                    barang_ditemukan = True
                    print(f"{detailNamaBarang}, Stok: {detailStok}, Harga: {detailHarga}")

            if not barang_ditemukan:
                print("Tidak ditemukan Barang")

            input("\nTekan Enter Untuk Kembali ke Menu Utama")
            break

    #Urut Harga
    elif pilihan == 7:
        while True: 
            bersihin_layar()

            with open("data_barang.json", "r") as file:
                barang_lengkap = json.load(file)

            tampilan_menu_sorting()

            inputan_user = input("Pilih Menu Pengurutan: ")

            if not inputan_user.isdigit():
                print("Masukkan Angka")

            input_sorting = int(inputan_user)

            if input_sorting == 1:
                bersihin_layar()

                hasilurutMurah = sorted(
                    barang_lengkap.items(),
                    key=lambda x: x[1]["Harga"]
                )


                for kode_barang, detail in hasilurutMurah:
                    detailNamaBarang = detail["Nama Barang"]
                    detailStok = detail["Stok"]
                    detailHarga = detail["Harga"]
                    detailKategori = detail["Kategori"]

                    print(f"{detailNamaBarang}, Stok: {detailStok}, Harga: Rp.{detailHarga},00")
                            
            elif input_sorting == 2:
                bersihin_layar()

                hasilurutMahal = sorted(
                    barang_lengkap.items(),
                    key=lambda x: x[1]["Harga"],
                    reverse=True
                )

                for kode_barang, detail in hasilurutMahal:
                    detailNamaBarang = detail["Nama Barang"]
                    detailStok = detail["Stok"]
                    detailHarga = detail["Harga"]
                    detailKategori = detail["Kategori"]

                    print(f"{detailNamaBarang}, Stok: {detailStok}, Harga: Rp.{detailHarga},00")

            input("\nTekan Enter Untuk Kembali ke Menu Utama")
            break

    elif pilihan == 8:
        print("Terimakasih")
        break

    else:
        print("Pilih yang bener bang")
        input("\ntekan enter untuk lanjut")
        continue
