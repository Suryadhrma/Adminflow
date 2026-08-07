import os

menu_utama = ["Tambah Barang", "Lihat Barang", "Cari Barang", "Keluar"]
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
    barang = []
    jumlah = []

    bersihin_layar()
    
    tampilan_menu()

    pilihan_user = input("\nPilih Menu:")

    if not pilihan_user.isdigit():
        print("Masukkan Angka")
        continue

    pilihan = int(pilihan_user)

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
                jumlah = input(f"Masukkan Jumlah Barang {barang}: ")
                if not jumlah.isdigit():
                    print("Masukkan angka bang!")
                else:
                    break

            bersihin_layar()

            barang_lengkap[barang] = jumlah
            print(f"Barang dengan nama {barang}, dengan jumlah {jumlah}, berhasil di tambahkan!")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break
            
    elif pilihan == 2:
        while True:

            bersihin_layar()

            if not barang_lengkap:
                print("Data Kosong")
            elif barang_lengkap:
                for barang, jumlah in barang_lengkap.items():
                    print(f"{barang}, dengan jumlah stok: {jumlah}")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    elif pilihan == 3:
        while True:
            bersihin_layar()

            while True:
                cari_barang = input("Masukkan Nama Barang yang Ingin dicari: ")
                if cari_barang == "":
                    print("Data Tidak Boleh Kosong")
                else:
                    break

            if cari_barang not in barang_lengkap:
                print("Data Barang Tidak Ditemukan")
            else:
                hasil_cari = barang_lengkap.get(cari_barang)
                print(f"Barang dengan nama {cari_barang}, dengan jumlah stok {hasil_cari} berhasil ditemukan")
            
            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break

    elif pilihan == 4:
        print("Nah cuma ini doang yang ada wkkwkw")
        break

    else:
        print("Pilih yang bener bang")
        input("\ntekan enter untuk lanjut")
