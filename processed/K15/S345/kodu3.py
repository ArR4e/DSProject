failinimi = input("Sisestage faili nimi: ")
f = open(failinimi)

bussid = []
for rida in f:
    buss = rida.split()
    bussid.append(buss)

f.close()

for i in range(len(bussid)):
    min = i
    for j in range(i+1, len(bussid)):
        if bussid[j][1] < bussid[min][1]:
            min = j
    if i != min:
        bussid[i], bussid[min] = bussid[min], bussid[i]
sobivad = []
for buss in bussid[:-1]:
    for buss2 in bussid[1:]:
        if buss[0] > buss2[0] and buss[1] < buss2[1] and buss[2] < buss2[2]:
            sobivad.append(buss)
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for el in sobivad:
    print(el[0] + " " + el[1] + " " + el[2])