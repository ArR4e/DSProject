nimi = input('Sisesta faili nimi: ')

fail = open(nimi, encoding = 'UTF-8')

järjend = []
for rida in fail:
    sisemine_järjend = []
    rida_ok = rida.strip().split()
    for el in rida_ok:
        sisemine_järjend.append(el)
    järjend.append(sisemine_järjend)
fail.close()

sobivad_bussid = []
for buss1 in järjend:
    hind1 = float(buss1[2])
    sobib = True
    for buss2 in järjend:
        hind2 = float(buss2[2])
        if buss2[0] > buss1[0] and buss2[1] < buss1[1] and hind2 < hind1:
            sobib = False
    if sobib == True:
        sobivad_bussid.append(buss1)

sobivad_bussid.sort()

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for el in sobivad_bussid:
    print(el[0], el[1], el[2])