f = open(input('Sisesta failinimi: '))

bussid = []
sobivad = []
sisaldab = False

for rida in f:
    bussid.append(rida.strip())
    
for i in bussid:
    start = int(i[0:2])*60 + int(i[3:5])
    kohal = int(i[6:8])*60 + int(i[9:11])
    hind = int(i[-2:])
    for j in bussid:
        start2 = int(j[0:2])*60 + int(j[3:5])
        kohal2 = int(j[6:8])*60 + int(j[9:11])
        hind2 = int(j[-2:])
        if start2 > start and kohal2 < kohal and hind2 < hind:
            sisaldab = True
    if not sisaldab:
        sobivad.append(i)
    sisaldab = False

while sobivad != []:
    varaseim = 24*60
    buss = 0
    for i in sobivad:
        valjumine = int(i[0:2])*60 + int(i[3:5])
        if valjumine <= varaseim:
            varaseim = valjumine
            buss = sobivad.index(i)
    print(sobivad[buss])
    del sobivad[buss]   

f.close()