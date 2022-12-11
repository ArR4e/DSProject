def odavaim(km):
    eelmine = 0
    nimed = []
    summad = []
    nimi = ''
    try:
        for a in nimekiri:
            sisse = a[1]
            km_hind = a[2]
            summa = float(sisse) + float(km_hind)*float(km)
            nimed.append(a[0])
            summad.append(summa)
        vahim = min(summad)
        number = summad.index(vahim)
            
        print('Kõige odavam on ' + str(nimed[number]) + '.')
    except:
        print(km)
            



f = open('taksohinnad.txt', 'r')
nimekiri = []
rida = []
for a in f:
    n = a.strip('\n').split(',')
    for x in n:
        rida.append(x)
    nimekiri.append(rida)
    rida = []

sisend = input('Sisesta tee pikkus kilomeetrites: ')
odavaim(sisend)
