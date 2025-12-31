
import random
pemain = []
tantangan = [
    'Tepuk tangan keras keras',
    'Nanyi',
    'Tampar dirimu sendiri',
    'Lompat tinggi',
    'Tampar orang dikiri mu atau di depan mu atau lawan mu',
    'Lakukan hal yang buat lawan mu tertawa',
    'Lakukan semuanya!'
]

print("===== SELAMAT DATANG DI GAME TANTANGAN =====")
# Mengatasi Game
def play():
    while True:
        pemain_dipilih = random.choice(pemain)
        tantangan_dipilih = random.choice(tantangan)
        print(f"tantangan nya akan diberikan kepada {pemain_dipilih} yaitu tantangannya {tantangan_dipilih}")
        print("atau simplenya kayak gini")
        print(pemain_dipilih + ": " + tantangan_dipilih)
        lanjut = input("Lanjut Y/n: ")
        lanjut.lower()
        if lanjut == "y":
            print("Oke permainan di lanjutkan")
            continue
        else:
            print("Permainan selesai!")
            exit()

# Mengatasi pemain 
def kosong():
    try:
        jumlah_pemain = int(input("Masukan jumlah pemain: "))
        for i in range(jumlah_pemain):
            nama_pemain = input(f"Masukan nama pemain {i + 1}: ")
            if nama_pemain == "":
                print("Nama tidak boleh kosong")
                exit()
            pemain.append(nama_pemain)
    except ValueError:
        print("Masukan angka")
if not pemain:
    kosong()
play()