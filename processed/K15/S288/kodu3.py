bussid = []
vastus = []

fail = input('Sisesta failinimi: ')

with open(fail, encoding = 'UTF-8') as f:
    read = f.readlines()

for rida in read:
    valik = rida.strip().split(' ')
    buss = [valik[0], valik[1], int(valik[2])]
    bussid.append(buss)

for buss in bussid:
    indeks = bussid.index(buss)
    for buss2 in bussid[:indeks] + bussid[indeks + 1:]:
        if buss[0] == buss2[0] and buss[1] == buss2[1] and buss[2] > buss2[2]:
            break
        elif buss[0] < buss2[0] and buss[1] == buss2[1]:
            break
        elif buss[0] == buss2[0] and buss[1] > buss2[1]:
            break
        elif buss[0] < buss2[0] and buss[1] > buss2[1] and buss[2] < buss2[2]:
            continue
        elif buss[0] < buss2[0] and buss[1] > buss2[1]:
            break
    else:
        vastus.append(buss)

vastus.sort()

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

for x in vastus:
    sõne = ' '.join(map(str, x))
    print(sõne)