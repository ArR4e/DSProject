
def sorteeri(li):

    for i in range(len(li)):
        for j in range(len(li)-i-1):
            valjumis1 = float(bussid[j][0][0:2]) + float(bussid[j][0][3:5]) * 0.01
            valjumis2 = float(bussid[j+1][0][0:2]) + float(bussid[j+1][0][3:5]) * 0.01
            if valjumis1 > valjumis2:
                bussid[j], bussid[j+1] = bussid[j+1], bussid[j]


bussid = []
fail = input('sisesta failinimi: ')
with open(fail) as f:
    for rida in f:
        andmed = rida.strip().split()
        bussid.append(andmed)

for x in bussid[:]:
    valjumis1 = float(x[0][0:2]) + float(x[0][3:5])*0.01
    saabumis1 = float(x[1][0:2]) + float(x[1][3:5])*0.01
    hind1 = float(x[2])
    for y in bussid[:]:
        valjumis2 = float(y[0][0:2]) + float(y[0][3:5]) * 0.01
        saabumis2 = float(y[1][0:2]) + float(y[1][3:5]) * 0.01
        hind2 = float(y[2])
        if valjumis2 > valjumis1 and saabumis2 < saabumis1 and hind2 < hind1:
            bussid.remove(x)
            break

sorteeri(bussid)

print('Esimest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

for i in bussid:
    print(*i, sep=' ')
