takso = []
sisse = []
kmh = []
tasu = []

km = float(input('Sisesta tee pikkus kilomeetrites: '))

fail = open('taksohinnad.txt', encoding='UTF-8')

a=0

for rida in fail:
    rida.strip('\n')
    for sõna in rida.split(','):
        if a == 0:
            takso.append(sõna.strip('\n'))
        elif a == 1:
            sisse.append(float(sõna.strip('\n')))
        else:
            kmh.append(float(sõna.strip('\n')))
        a+=1
        if a == 3:
            a=0
fail.close()

if len(takso) > 0:

    for i in range(len(takso)):
        hind = sisse[i] + kmh[i]*km
        tasu.append(hind)


    odavaim = takso[tasu.index(min(tasu))]

    print(odavaim)
else:
    print('Fail on tühi!')