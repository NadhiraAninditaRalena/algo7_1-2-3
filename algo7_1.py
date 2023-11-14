print('@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@')
print('@ @ @ @  @ @   @  @   @ @ @     @   @   @')
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

import math

def faktorial(n):
    return n, math.factorial(n) if n >= 0 else None

#input dari user
bilangan = int(input("nilai: "))

# faktorial dan hasilnya
hasil = faktorial(bilangan)

if hasil:
    nilai, faktorial = hasil
    print(f"Faktorial dari {nilai} adalah {faktorial}")
    
