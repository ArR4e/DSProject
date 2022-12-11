#alustasin 13.10.2021 (18:29)
pikkus = float(input('Sisesta tee pikkus kilomeetrites: '))

fail = open('taksohinnad.txt', encoding = 'utf8')

nimed = []
hinnad = []

while True:
    rida = fail.readline().strip()
    if rida == '':
        break
    info = rida.split(",")
    nimi = info[0]
    hind = float(info[1])  + (float(info[2]) * pikkus)
    nimed.append(nimi)
    hinnad.append(hind)

if hinnad != []: #kui faili sisu on tühi, siis programm lõppeb
    minimuum = min(hinnad)
    indeks = hinnad.index(minimuum)
    nimi = nimed[indeks]
    print('Kõige odavam on', nimi + '.')
    fail.close()

fail.close() #kui faili sisu on tühi, siis ikka paneme kinni faili