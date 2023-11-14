print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

def kubik_angka(angka):
    return angka ** 3

def cek_dan_kalkulasi(angka):
    return kubik_angka(angka) if angka % 3 == 0 else False

while True:
    # Contoh penggunaan:
    angka_input = int(input("Masukkan Nilai: "))
    hasil = cek_dan_kalkulasi(angka_input)

    print(f"Hasil kubik dari {angka_input} adalah {hasil}" if hasil is not False else "False")

    ulangi = input("Ulangi proses? (y/n): ")
    if ulangi.lower() != "y":
        break
