"""
DESKRIPSI SOAL
Buatlah program untuk menghitung selisih waktu dalam jam, menit, detik. Masukan adalah jam, menit, detik mulaidan jam, menit, detik selesai. Keluaran adalah selisih waktunya.

PETUNJUK MASUKAN
Input terdiri atas 2 baris dengan masing-masing baris terdiri dari 3 angka yang dipisahkan spasi

PETUNJUK KELUARAN
Outputkan Terdiri dari 3 angka dalam satu baris (pisahkan dengan spasi) yang merupakan selisih dari input pada baris pertama dan kedua

CONTOH MASUKAN
10  25  40 
12  25  30 
CONTOH KELUARAN
1 59 50 
"""

inp0 = list(map(int, input().split(" ")))
inp1 = list(map(int, input().split(" ")))

def convert_to_detik(jmd):
    return jmd[0]*3600 + jmd[1]*60 + jmd[2]

diff = abs(convert_to_detik(inp0) - convert_to_detik(inp1))
print(diff//3600, (diff%3600)//60, (diff%3600%60))