fail = input('Sisesta failinimi: ')
f = open(fail, 'r', encoding = 'utf-8')
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')

def sordi(järjend):
    return järjend[0]

bussid = []
# Koostab järjendi sõiduplaanist
for rida in f:
    buss = []
    rida = rida.strip().split(' ')
    buss.append(rida[0])
    buss.append(rida[1])
    buss.append(int(rida[2]))
    bussid.append(buss)

# Leiab sobimatud bussid sõiduplaanist
sobimatud_bussid = []
for buss in bussid:
    for buss_2 in bussid:
        if buss[0] < buss_2[0] and buss[1] > buss_2[1] and buss[2] > buss_2[2]:
            if buss not in sobimatud_bussid:
                sobimatud_bussid.append(buss)

# Kustutab sobimatud bussid sõiduplaanist
for buss in sobimatud_bussid:
    bussid.remove(buss)

# Sorteerib bussid
bussid.sort(key=sordi)

# Väljastab bussid
for buss in bussid:
    väljub = buss[0]
    saabub = buss[1]
    hind = buss[2]
    print(väljub,saabub,hind)