sisend = input('Sisesta failinimi:')

with open(sisend, 'r', encoding='UTF-8') as fail:
    bussid = []
    for rida in fail:
        rea_järj = rida.strip().split()
        bussid.append((rea_järj[0], rea_järj[1], rea_järj[2]))

indeksid = set()
for i in range(len(bussid)):
    for j in range(len(bussid)):
        if bussid[i] != bussid[j]:
            if float(bussid[i][0].replace(':', '.')) < float(bussid[j][0].replace(':', '.')) and float(bussid[i][1].replace(':', '.')) > float(bussid[j][1].replace(':', '.')) and int(bussid[i][2]) > int(bussid[j][2]):
                indeksid.add(i)

indeksid_järj = reversed(sorted(list(indeksid)))

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

for n in indeksid_järj:
    bussid.pop(n)

bussid = sorted(bussid)

for el in bussid:
    print(' '.join(el))
