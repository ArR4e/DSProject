failinimi = input("Sisesta failinimi: ")
sõiduajad = []
fail = open(failinimi, encoding = "utf-8")

for rida in fail:
    sõiduajad.append(rida.strip('\n'))
fail.close()

sobivad = []

for buss in sõiduajad:
    buss_rea_elemendid = buss.split(" ")
    buss_väljumine = buss_rea_elemendid[0]
    buss_saabumine = buss_rea_elemendid[1]
    buss_hind = int(buss_rea_elemendid[2])
    
    sobib = True
    
    for buss2 in sõiduajad:
        buss2_rea_elemendid = buss2.split(" ")
        buss2_väljumine = buss2_rea_elemendid[0]
        buss2_saabumine = buss2_rea_elemendid[1]
        buss2_hind = int(buss2_rea_elemendid[2])
        if buss2_väljumine > buss_väljumine and buss2_saabumine < buss_saabumine and buss2_hind < buss_hind:
            sobib = False
            
    if sobib == True:
        if buss not in sobivad:
            sobivad.append(buss)

sobivad.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")            
for sobiv in sobivad:
    print(sobiv)
            
