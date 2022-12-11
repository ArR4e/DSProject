failinimi = input("Sisesta failinimi: ")

bussid = []
f = open(failinimi)
for rida in f:
    bussid.append((rida.strip().split()))
f.close()

sobivad = []
for buss1 in bussid:
    sobib = True
    for buss2 in bussid:
        if buss2[0] > buss1[0] and buss2[1] < buss1[1] and int(buss2[2]) < int(buss1[2]):
            sobib = False
    if sobib:
        sobivad.append(buss1)

sobivad.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")       
for buss in sobivad:
    print(buss[0], buss[1], buss[2])   