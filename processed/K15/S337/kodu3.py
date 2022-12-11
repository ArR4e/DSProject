fail = input('Sisesta faili nimi: ')
bussid = []
with open(fail, encoding='UTF-8') as f:
    for rida in f:
        rida = rida.split()
        bussid.append(rida)
sobivad = []
for buss in bussid:
    välja = buss[0]
    kohal = buss[1]
    hind = float(buss[2])
    sobivus = True
    for buss2 in bussid:
        if buss == buss2:
            continue
        else:
            välja2 = buss2[0]
            kohal2 = buss2[1]
            hind2 = float(buss2[2])
            if välja2 > välja and kohal2 < kohal and hind2 < hind:
                sobivus = False
    if sobivus:
       buss = ' '.join(buss)
       sobivad.append(buss)
sobivad.sort()
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')
print(*sobivad, sep='\n')
        
        