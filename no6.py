"""
DESKRIPSI SOAL
Buatlah program untuk menghitung berapa banyak bit nol pada bilangan biner 5 bit. Misalnya diketahui bilangan biner S = “01110” maka outputnya adalah 2. Input bilangan biner tersebut bertipe string.

PETUNJUK MASUKAN
Input terdiri atas 1 string

PETUNJUK KELUARAN
Outputkan banyak angka 0 yang ada

CONTOH MASUKAN
01110
CONTOH KELUARAN
2
"""

print(sum([1 for i in input() if int(i)==0]))