failinimi = input("Sisesta failinimi: ")

f = open(failinimi)
bussid = []
for rida in f:
    algus, lõpp, hind = rida.strip().split(" ")
    buss = [algus, lõpp, int(hind)]
    bussid.append(buss)
f.close()

sõidame = []
bussid.sort()

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i, buss1 in enumerate(bussid):
    sobib = True
    for buss2 in bussid[i+1:]:
        if (buss2[0] > buss1[0]) and (buss2[1] < buss1[1]) and (buss2[2] < buss1[2]):
            sobib = False
    if sobib:
        for el in buss1:
            print(el, end = " ")
        print("")