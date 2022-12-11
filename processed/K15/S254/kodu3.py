sisend = input('Sisestage failinimi: ')

fail = open(sisend, encoding='UTF-8')

järjend = []
for rida in fail:
    rida = rida.strip().split()
    järjend.append(rida)
fail.close()

sobivad_bussid = []
for algus1, lopp1, hind1 in järjend:
    sobib = True
    for algus2, lopp2, hind2 in järjend:
        if algus1 < algus2 and lopp1 > lopp2 and float(hind1) > float(hind2):
            sobib = False
    if sobib:
        sobivad_bussid.append([algus1, lopp1, hind1])

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')
sobivad_bussid.sort()
for i in sobivad_bussid:
    print(" ".join(i))