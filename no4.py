"""
DESKRIPSI SOAL
Keindahan puisi dinilai dari seberapa "mirip" akhiran suatu baris dengan baris yang lain yang berdekatan. Diinputkan dua buah string yang merupakan dua baris puisi. Beri nilai keindahan dengan cara menghitung berapa banyak huruf yang mirip diakhir kedua string tersebut.

PETUNJUK MASUKAN
Dua buah string dengan panjang huruf yang sama, tidak mengandung spasi dan hanya terdiri dari huruf tidak kapital

PETUNJUK KELUARAN
Outputkan sebuah bilangan bulat sesuai penjelasan di atas

CONTOH MASUKAN 1
adindaku
ocintaku
CONTOH KELUARAN 1
3
CONTOH MASUKAN 2
engkauseinda
cahyapurnama
CONTOH KELUARAN 2
1
"""

puisi = [input()[::-1] for i in range(2)]
lenght = list(map(len, puisi))

#pindahkan ke depan yang paling sedikit
index0 = lenght.index(min(lenght))
puisi.insert(0, puisi[index0])
del puisi[index0]

sama = 0
for i in range(len(puisi[0])):
    if (puisi[0][i]==puisi[1][i]):
        sama+=1
    else:
        break
print(sama)