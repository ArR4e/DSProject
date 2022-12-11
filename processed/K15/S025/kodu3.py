a = input('Sisesta failinimi: ')
bussid = []

f = open(a)
for rida in f:
    jär = rida.strip('\n').split(' ')
    bussid.append(jär)

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

b = []
for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if buss[0] < buss2[0] and buss[1] > buss2[1] and float(buss[2]) > float(buss2[2]):
            sobib = False
    if sobib == True:
        b.append(buss)
b.sort()
for i in b:
    print(i[0], i[1], i[2])