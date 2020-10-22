"""
DESKRIPSI SOAL
Pernah main rubik? ya kalau kalian perhatikan rubik merupakan kubus besar yang tersusun dari kubus-kubus kecil. Pada soal ini Kalian akan diberikan panjang sisi kubus kecil dan banyak kubus kecil yang menyusun kubus besar. Tentukan volume kubus total!

PETUNJUK MASUKAN
Dua buah bilangan bulat X dan Y. X merupakan panjang sisi kubus kecil dalam centimeter. Dan Y adalah banyak kubus kecil yang menyusun panjang sisi kubus besar.(1 ≤ X,Y ≤ 100)

PETUNJUK KELUARAN
Sebuah bilangan bulat volume akhir sebuah rubik

CONTOH MASUKAN 1
2 3
CONTOH KELUARAN 1
216

CONTOH MASUKAN 2
4 5
CONTOH KELUARAN 2
8000
"""

num = list(map(int, input().split()))
print(num[0]**3 * num[1]**3)