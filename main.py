import os

menu_utama = ["Tambah Barang", "Lihat Barang", "Cari Barang", "Keluar"]

def bersihin_layar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system(clear)

while True:
    bersihin_layar()
    
    print("===== MENU UTAMA =====")
    for nomor, menu in enumerate(menu_utama, start=1):
        print(f"{nomor}. {menu}")

    pilihan_user = input("\nPilih Menu:")

    if not pilihan_user.isdigit():
        print("Masukkan Angka")
        continue

    pilihan = int(pilihan_user)

    if pilihan == 1:
        print("Belum Ada jir")
        input("\ntekan enter untuk lanjut")

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
