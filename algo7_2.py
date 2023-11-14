print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

def vokal_dan_konsonan(kalimat):
    kalimat = kalimat.lower()  # Ubah jadi huruf kecil untuk memudahkan perhitungan
    vokal1 = "aeiou"
    konsonan = 0
    vokal = 0
    
    for huruf in kalimat:
        if huruf.isalpha():
            if huruf in vokal1:
                vokal += 1
            else:
                konsonan += 1
    
    return vokal, konsonan

while True:
    # Input dari user
    kalimat = input("Masukkan kalimat: ")

    vokal, konsonan = vokal_dan_konsonan(kalimat)
    print(f"Jumlah vokal: {vokal}")
    print(f"Jumlah konsonan: {konsonan}")

    ulangi = input("Ulangi proses? (y/n): ")
    if ulangi.lower() != "y":
        break

