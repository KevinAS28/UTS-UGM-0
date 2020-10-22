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