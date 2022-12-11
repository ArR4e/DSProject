fail = open(input("Sisestage faili nimi"))
bussid = []
sobivad = []
for rida in fail:
    andmed = rida.strip().split()
    andmed[2]=int(andmed[2])
    bussid.append(andmed)
    
for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if buss[0] < buss2[0] and buss[1] > buss2[1] and buss[2] > buss2[2]:
            sobib = False
    if sobib:
        sobivad.append(buss)
            
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
sobivad.sort()
for buss in sobivad:
    print(buss[0]+" "+buss[1]+" "+str(buss[2]))