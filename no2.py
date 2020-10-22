"""
DESKRIPSI SOAL
Pak Blangkon dan Pak Semar sedang bernostalgia dengan permainannya masa kecil dulu, suit. Anda tentu pernah bermain suit bukan? Nah kali ini Pak Blangkon dan Pak Semar tidak ingin memainkannya secara offline, karena di era gadget sekarang, mereka berdua ingin memainkannya secara online. Buatlah program suit sederhana yang nantinya akan dikembangkan untuk menyenangkan Pak Blangkon dan Pak Semar yang ingin bernostalgia.

PETUNJUK MASUKAN
Dua baris simbol yang terdiri dari dua karakter: [] = Kertas, () = Batu, 8< = Gunting. Baris Pertama adalah simbol yang dipilih Pak Blangkon dan baris kedua adalah simbol yang dipilih Pak Semar.

PETUNJUK KELUARAN
Pemenang suit. "Blangkon" atau "Semar" atau "Seri".

CONTOH MASUKAN
[]
()
CONTOH KELUARAN
Blangkon
"""

r = "()"
p = "[]"
s = "8<"
winners = ["Seri", "Blangkon", "Semar"]
poss = {
    p: {r: 1, p: 0, s: 2},
    r: {r: 0, p: 2, s: 1},
    s: {r: 2, p: 1, s: 0}
}
hand0 = input()
hand1 = input()
print(winners[poss[hand0][hand1]])