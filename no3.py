"""
DESKRIPSI SOAL
Pak Blangkon ingin memberi nilai siswa-siswanya. Aturan penilaiannya adalah sebagai berikut

Semua nilai angka yang lebih dari sama dengan 75 maka akan dapat A
Semua nilai angka yang tidak lebih dari sama dengan 45 maka akan dapat B/C
Nilai angka yang belum dapat nilai huruf, jika nilai angka tersebut lebih besar dari rata-rata maka akan dapat A/B
Nilai angka yang belum dapat nilai huruf akan otomatis mendapat B
Bantu Pak Blangkon untuk membuat program yang dapat menentukan berapa banyak yang dapat A, A/B, B, dan B/C.
PETUNJUK MASUKAN
Pada baris pertama adalah sebuah bilangan bulat N yang merupakan banyak siswa yang akan diinputkan. Pada baris kedua terdapat N buah nilai siswa. Maksimal akan terdapat 30 siswa dengan nilai siswa antara 0 sampai 100.

PETUNJUK KELUARAN
Outputkan empat buah nilai, yakni banyak siswa yang dapat A, A/B, B, dan B/C secara berturut-turut.

CONTOH MASUKAN
5
100 70 49 49 30
CONTOH KELUARAN
1 1 2 1
KETERANGAN
Pada contoh di atas ada satu siswa yang mendapat A (nilai 100) dan satu siswa yang mendapat nilai B/C (nilai 30). Jika dihitung rata-rata nilainya, akan diperoleh rata-rata = 59.6. Maka siswa dengna nilai 70 akan mendapat A/B sedangkan dua siswa yang memiliki nilai 49 akan mendapat nilai huruf B.
"""

l = int(input())
scores = list(map(float, input().split()))
letters = [0, 0, 0, 0]
for sc in scores:
    let = ""
    if sc >= 75:
        letters[0]+=1
    elif not (sc >= 45):
        letters[-1]+=1
    elif sc > (sum(scores)/l):
        letters[1]+=1
    else:
        letters[2]+=1

print(" ".join([str(i) for i in letters]))
