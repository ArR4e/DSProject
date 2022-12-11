failinimi = input("Sisesta faili nimi: ")
fail = open(failinimi, 'r', encoding='utf-8')
bussid = []
for rida in fail:
    sisu = rida.strip().split(' ')
    sõiduaeg = (float((sisu[1].split(':'))[0])*60 + float((sisu[1].split(':'))[1])) - (float((sisu[0].split(':'))[0])*60 + float((sisu[0].split(':'))[1]))
    sisu.append(sõiduaeg)
    bussid.append(sisu)
bussid.sort()
sobivad_bussid = []
print("Esimesest linnast teise sõitmiseks võid kaaluda järgmisi busse: ")
for i in range(len(bussid)):
    väljumisaeg = bussid[i][0]
    saabumisaeg = bussid[i][1]
    hind = int(bussid[i][2])
    sobib = True
    for j in range(i+1, len(bussid)):
        väljumisaeg2 = bussid[j][0]
        saabumisaeg2 = bussid[j][1]
        hind2 = int(bussid[j][2])
        if väljumisaeg < väljumisaeg2 and saabumisaeg > saabumisaeg2:
            if hind2 < hind:
                sobib = False
    if sobib == True and bussid[i] not in sobivad_bussid:
        sobivad_bussid.append(bussid[i])
for el in range(len(sobivad_bussid)):
    print(sobivad_bussid[el][0]+str(' ')+sobivad_bussid[el][1]+str(' ')+sobivad_bussid[el][2])