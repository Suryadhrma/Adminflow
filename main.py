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

            barang = input("Masukkan Nama Barang: ")

            jumlah = input(f"Masukkan Jumlah Barang {barang}: ")

            barang_lengkap[barang] = jumlah

            if not jumlah.isdigit():
                print("Masukkan angka bang!")
                input("\ntekan enter untuk lanjut")
                continue


            print(f"Barang dengan nama {barang}, dengan jumlah {jumlah}, berhasil di tambahkan!")

            jawaban_user = input("\nTekan enter untuk kembali ke menu utama")
            break
            
    elif pilihan == 2:
        print("Belum Ada Juga Cuy")
        input("\ntekan enter untuk lanjut")

    elif pilihan == 3:
        print("Tunggu update kocak")
        input("\ntekan enter untuk lanjut")

    elif pilihan == 4:
        print("Nah cuma ini doang yang ada wkkwkw")
        break

    else:
        print("Pilih yang bener bang")
        input("\ntekan enter untuk lanjut")
