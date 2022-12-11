
fail = input("Faili nimi: ")

f = open(fail)
bussid = []

for rida in f:
    jupid = rida.strip().split()
    bussid.append(jupid)
f.close()

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
sobivad_bussid = []

for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if buss == buss2:
            continue
        else:
            if buss[0] < buss2[0] and buss[1] > buss2[1] and float(buss[2]) > float(buss2[2]):
                sobib = False
    if sobib:
        sobivad_bussid.append(buss)
        
sobivad_bussid.sort()
for buss in sobivad_bussid:
    print(' '.join(buss))