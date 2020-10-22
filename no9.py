"""
DESKRIPSI SOAL
Buatlah program yang menerima 3 buah input nilai dan outputkan jumlah maksimal dari 2 bilangannya ! diantara ketiga input tersebut.

PETUNJUK MASUKAN
Input terdiri atas 3 angka dalam 1 baris

PETUNJUK KELUARAN
Outputkan angka jumlah terbesar dari 2 angka

CONTOH MASUKAN
10 9 11
CONTOH KELUARAN
21
"""

numbers = sorted(list(map(int, input().split())))
print(numbers[-1]+numbers[-2])