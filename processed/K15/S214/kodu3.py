failinimi = input("Sisesta failinimi: ")
f = open(failinimi)
bussid = []
for rida in f:
    buss = rida.strip().split(" ")
    bussid += [buss]

sobivad = []
for buss1 in bussid:
    sobib = True
    for buss2 in bussid:
        if buss1[0] < buss2[0] and buss1[1] > buss2[1] and int(buss1[2]) > int(buss2[2]):
            sobib = False
    if sobib:
        sobivad += [buss1]
for i in range(len(sobivad)):
    for j in range(len(sobivad)-1):
        if sobivad[j][0] > sobivad[j+1][0]:
            sobivad[j],sobivad[j+1]= sobivad[j+1],sobivad[j]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for buss in sobivad:
    print(" ".join(buss))