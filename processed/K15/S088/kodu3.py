a = input("Sisestage failinimi: ")

f = open(a, encoding = "utf-8")
sisu = f.readlines()
f.close()
for i in sisu:
    sisu[sisu.index(i)] = i.strip().split()
for i in sisu:
    if i[0] > i[1]:
        sisu.remove(i)
        
hind = 0
for i in sisu:
    if int(i[2]) > hind:
        hind = int(i[2])
        eemaldada = i
sisu.remove(eemaldada)

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
sisu.sort()
for i in sisu:
    for n in i:
        print(n, end =" ")
    print("")